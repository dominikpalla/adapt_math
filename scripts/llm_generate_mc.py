"""
LLM-assisted konverze text-answer úloh na multiple_choice.

Pro každou úlohu s textovou odpovědí (nezná se distraktor) zavolá Claude
API s content_latex + expected a nechá model vygenerovat 4 možnosti
(1 správnou + 3 pedagogicky rozumné distraktory) v strukturovaném JSON.

Bezpečnostní zábradlí:
  - Dry-run mode (default): zapisuje jen do JSON preview souboru, ne do DB.
  - Přeskočí úlohy, které už mají multiple_choice.
  - Validuje, že Claude vrátí přesně 4 možnosti a expected key mezi nimi.
  - Vyžaduje explicitní --commit pro zápis do DB.
  - Idempotentní na commit-mode: druhé spuštění nic nezmění (task už má MC).

Použití:
    ANTHROPIC_API_KEY=... DATABASE_URL=... python scripts/llm_generate_mc.py \
        --limit 5                                # preview 5 úloh, jen JSON out
    ANTHROPIC_API_KEY=... DATABASE_URL=... python scripts/llm_generate_mc.py \
        --commit --limit 20                      # ostrý běh 20 úloh
    ANTHROPIC_API_KEY=... DATABASE_URL=... python scripts/llm_generate_mc.py \
        --commit --task-ids e01_11,e01_12         # jen vybrané úlohy
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy.orm.attributes import flag_modified

from database import init_db
from model import MathTask

MODEL = "claude-sonnet-5"

SYSTEM_PROMPT = """\
Jsi expert český matematik. Konvertuješ úlohy z textbook do multiple-choice
formátu pro adaptivní online učení. Dostaneš zadání úlohy a její známou správnou
odpověď. Vygeneruj JSON přes tool s POUZE 4 možnostmi (klíče "a","b","c","d")
a označením správné. Distraktory musí být:
  - Pedagogicky smysluplné (typické studentské chyby, ne úplně absurdní)
  - Různorodé (ne jen mírné variace téhož)
  - Ve formátu odpovídajícím správné odpovědi (matematický výraz ↔ matematický
    výraz, text ↔ text, číslo ↔ číslo)
  - LaTeX v $...$ pro matematiku, prostý text jinak
Správná odpověď MUSÍ přesně sedět k té z inputu (může být přeformátovaná pro
konzistenci, ale sémanticky totožná). Rozmisti správnou odpověď náhodně mezi
distraktory (ne vždy jako "a")."""

TOOL_SCHEMA = {
    "name": "record_mc_options",
    "description": "Uložit 4 multiple-choice možnosti pro úlohu.",
    "input_schema": {
        "type": "object",
        "properties": {
            "options": {
                "type": "array",
                "minItems": 4, "maxItems": 4,
                "items": {
                    "type": "object",
                    "properties": {
                        "key":         {"type": "string", "enum": ["a", "b", "c", "d"]},
                        "label_latex": {"type": "string", "description": "Text nebo LaTeX v $...$"},
                    },
                    "required": ["key", "label_latex"],
                },
            },
            "correct_key": {"type": "string", "enum": ["a", "b", "c", "d"]},
        },
        "required": ["options", "correct_key"],
    },
}


def is_text_answer(exp: str) -> bool:
    """Heuristika: expected začíná písmenem (ne $, ne číslicí, ne -, ne \\)."""
    if not isinstance(exp, str) or not exp:
        return False
    s = exp.strip()
    # $-obalené math nebo číslo nebo LaTeX makro nebo interval/set NENÍ text
    if re.match(r'^[\$\d\-\+\(\[\{\\]', s):
        return False
    return bool(re.match(r'^[a-zA-Zá-žÁ-Ž]', s))


def call_claude(client, content_latex: str, expected: str) -> dict:
    user_msg = (
        f"Zadání úlohy:\n{content_latex}\n\n"
        f"Známá správná odpověď: {expected}\n\n"
        f"Vygeneruj 4 multiple-choice možnosti a označ správnou."
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        tools=[TOOL_SCHEMA],
        tool_choice={"type": "tool", "name": "record_mc_options"},
        messages=[{"role": "user", "content": user_msg}],
    )
    for block in resp.content:
        if block.type == "tool_use" and block.name == "record_mc_options":
            return block.input
    raise RuntimeError("Claude nevrátil tool_use blok")


def validate_mc(mc: dict) -> str | None:
    """Vrátí error message nebo None."""
    if not isinstance(mc, dict): return "not a dict"
    opts = mc.get("options")
    if not isinstance(opts, list) or len(opts) != 4: return "options must be list of 4"
    keys = [o.get("key") for o in opts]
    if sorted(keys) != ["a", "b", "c", "d"]: return f"keys must be a,b,c,d got {keys}"
    ck = mc.get("correct_key")
    if ck not in ["a", "b", "c", "d"]: return f"correct_key invalid: {ck}"
    for o in opts:
        if not isinstance(o.get("label_latex"), str) or not o["label_latex"].strip():
            return f"empty label_latex for {o.get('key')}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    parser.add_argument("--anthropic-key", default=os.environ.get("ANTHROPIC_API_KEY"))
    parser.add_argument("--limit", type=int, default=None, help="Zpracovat jen N úloh (pro test).")
    parser.add_argument("--task-ids", default=None, help="Čárkou oddělený seznam konkrétních task_id.")
    parser.add_argument("--out", default="llm_mc_preview.jsonl", help="Preview log JSONL.")
    args = parser.parse_args()

    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr); return 2
    if not args.anthropic_key:
        print("Chyba: ANTHROPIC_API_KEY.", file=sys.stderr); return 2

    try:
        from anthropic import Anthropic
    except ImportError:
        print("Chyba: `pip install anthropic`.", file=sys.stderr); return 2
    client = Anthropic(api_key=args.anthropic_key)

    SessionLocal = init_db(args.db_url)
    sess = SessionLocal()
    try:
        q = sess.query(MathTask).filter(
            (MathTask.task_id.like("e%")) | (MathTask.task_id.like("umat_%"))
        )
        if args.task_ids:
            wanted = [x.strip() for x in args.task_ids.split(",")]
            q = q.filter(MathTask.task_id.in_(wanted))
        candidates = []
        for t in q.all():
            if not isinstance(t.results, list) or len(t.results) != 1:
                continue
            r = t.results[0]
            if not isinstance(r, dict): continue
            if r.get("type") == "multiple_choice":
                continue  # už MC, skip
            if is_text_answer(r.get("expected", "")):
                candidates.append(t)
        if args.limit:
            candidates = candidates[:args.limit]
        print(f"Kandidátů (text-answer + ne-MC): {len(candidates)}")
        if not candidates:
            return 0

        out_path = Path(args.out)
        changed = 0
        errors = 0
        with out_path.open("w") as out_f:
            for i, t in enumerate(candidates, 1):
                print(f"[{i}/{len(candidates)}] {t.task_id} ...", end=" ", flush=True)
                r = t.results[0]
                orig_content = t.content_latex
                orig_expected = r.get("expected", "")
                try:
                    mc = call_claude(client, orig_content, orig_expected)
                    err = validate_mc(mc)
                    if err:
                        print(f"❌ validation: {err}")
                        errors += 1
                        out_f.write(json.dumps({
                            "task_id": t.task_id, "status": "invalid", "error": err,
                            "claude_output": mc,
                        }, ensure_ascii=False) + "\n")
                        continue
                    new_results = [{
                        "key": r.get("key", "vysledek"),
                        "label_latex": r.get("label_latex", ""),
                        "type": "multiple_choice",
                        "options": [{"key": o["key"], "label_latex": o["label_latex"]} for o in mc["options"]],
                        "expected": mc["correct_key"],
                    }]
                    out_f.write(json.dumps({
                        "task_id": t.task_id, "status": "ok",
                        "content": orig_content, "original_expected": orig_expected,
                        "new_results": new_results,
                    }, ensure_ascii=False) + "\n")
                    if args.commit:
                        t.results = new_results
                        flag_modified(t, "results")
                        sess.commit()
                    changed += 1
                    print("✓")
                except Exception as e:
                    print(f"❌ {e}")
                    errors += 1
                    out_f.write(json.dumps({
                        "task_id": t.task_id, "status": "error", "error": str(e)
                    }, ensure_ascii=False) + "\n")
                # jemný rate-limit pojistka
                time.sleep(0.5)

        print(f"\nHotovo: {changed} úspěch, {errors} chyb.")
        print(f"Preview: {out_path.resolve()}")
        if not args.commit:
            print("(DRY-RUN — pro zápis přidej --commit)")
        return 0
    finally:
        sess.close()


if __name__ == "__main__":
    sys.exit(main())
