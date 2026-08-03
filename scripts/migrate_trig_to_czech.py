"""
Bulk migrace anglických trigonometrických zápisů → české v obsahu úloh.

Aplikuje regex-nahradu (s word-boundary) na:
  - `math_tasks.content_latex`
  - `math_tasks.results[*].expected` (kde je string)
  - `math_tasks.results[*].label_latex`
  - `math_tasks.results[*].options[*].label_latex` (multiple_choice)

Nahrady:
  \\arctan  → \\arctg
  \\arccot  → \\arccotg
  \\tan     → \\tg          (ale ne \\tanh)
  \\cot     → \\cotg         (ale ne \\coth)

Pořadí je záměrně od nejdelšího vzoru, aby se \\arctan nezpracoval jako
\\arc\\tg. Word-boundary přes look-ahead na non-letter chrání před \\tanh
a podobně.

Použití:
    DATABASE_URL=... python scripts/migrate_trig_to_czech.py               # dry-run
    DATABASE_URL=... python scripts/migrate_trig_to_czech.py --commit      # ostrý
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy.orm.attributes import flag_modified

from database import init_db
from model import MathTask


# Pořadí je důležité: nejdelší vzory první, aby se \arctan neroznesl na \arctg.
REPLACEMENTS: list[tuple[str, str]] = [
    (r"\\arctan(?![a-zA-Z])",   r"\\arctg"),
    (r"\\arccot(?![a-zA-Z])",   r"\\arccotg"),
    (r"\\tan(?![a-zA-Z])",      r"\\tg"),      # ne \tanh
    (r"\\cot(?![a-zA-Z])",      r"\\cotg"),    # ne \coth
]
COMPILED = [(re.compile(p), r) for p, r in REPLACEMENTS]


def rewrite(s: str) -> tuple[str, bool]:
    """Vrátí (new_string, changed). Bezpečné vůči None."""
    if not isinstance(s, str) or not s:
        return s, False
    original = s
    for pat, repl in COMPILED:
        s = pat.sub(repl, s)
    return s, s != original


def rewrite_results(results):
    """Rewrite result array v place. Vrátí True, pokud se něco změnilo."""
    if not isinstance(results, list):
        return False
    any_changed = False
    for r in results:
        if not isinstance(r, dict):
            continue
        # label_latex
        if isinstance(r.get("label_latex"), str):
            new, ch = rewrite(r["label_latex"])
            if ch:
                r["label_latex"] = new
                any_changed = True
        # expected — může být string (mathlive/decimal-as-str/mc-key) nebo list (multi-variant)
        exp = r.get("expected")
        if isinstance(exp, str):
            new, ch = rewrite(exp)
            if ch:
                r["expected"] = new
                any_changed = True
        elif isinstance(exp, list):
            new_list = []
            list_changed = False
            for item in exp:
                if isinstance(item, str):
                    new_item, ch = rewrite(item)
                    if ch: list_changed = True
                    new_list.append(new_item)
                else:
                    new_list.append(item)
            if list_changed:
                r["expected"] = new_list
                any_changed = True
        # options (multiple_choice) — každá option má label_latex a key
        if isinstance(r.get("options"), list):
            for opt in r["options"]:
                if isinstance(opt, dict) and isinstance(opt.get("label_latex"), str):
                    new, ch = rewrite(opt["label_latex"])
                    if ch:
                        opt["label_latex"] = new
                        any_changed = True
    return any_changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Bulk migrace \\tan→\\tg v obsahu math_tasks.")
    parser.add_argument("--commit", action="store_true",
                        help="Bez tohoto flagu jen dry-run (žádný zápis).")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    parser.add_argument("--show", type=int, default=5,
                        help="Kolik ukázek before/after zobrazit (default 5).")
    args = parser.parse_args()

    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr)
        return 2

    SessionLocal = init_db(args.db_url)
    session = SessionLocal()
    try:
        tasks = session.query(MathTask).all()
        print(f"Načteno {len(tasks)} úloh z DB.")

        changed_content = 0
        changed_results = 0
        both = 0
        samples: list[dict] = []

        for t in tasks:
            new_content, cc = rewrite(t.content_latex)
            rc = rewrite_results(t.results)  # in-place
            if cc:
                if len(samples) < args.show:
                    samples.append({"task_id": t.task_id,
                                    "before_content": t.content_latex,
                                    "after_content":  new_content})
                t.content_latex = new_content
                changed_content += 1
            if rc:
                changed_results += 1
                if len(samples) < args.show:
                    r0 = t.results[0] if t.results else {}
                    samples.append({"task_id": t.task_id,
                                    "sample_result": r0})
            if cc and rc:
                both += 1
            if rc:
                flag_modified(t, "results")

        print()
        print(f"Změny:")
        print(f"  content_latex:  {changed_content} úloh")
        print(f"  results:        {changed_results} úloh")
        print(f"  obojí:          {both} úloh")
        total_dirty = changed_content + changed_results - both
        print(f"  dotčeno celkem: {total_dirty} úloh")

        if samples:
            print()
            print("── UKÁZKA ─────────────────────────────────────")
            for s in samples[:args.show]:
                print(f"  {s['task_id']}:")
                if 'before_content' in s:
                    print(f"    content před: {s['before_content'][:100]}")
                    print(f"    content po:   {s['after_content'][:100]}")
                if 'sample_result' in s:
                    print(f"    result[0]:    {json.dumps(s['sample_result'], ensure_ascii=False)[:150]}")

        if not args.commit:
            print()
            print("── DRY-RUN — nic se nezapisuje. Pro ostrý běh přidej --commit.")
            session.rollback()
            return 0

        if total_dirty == 0:
            print("Nic k migraci.")
            return 0

        print()
        print("── COMMIT — zapisuju ────────────────────────────")
        session.commit()
        print(f"✅ Migrace uložena. Dotčeno {total_dirty} úloh.")
        return 0
    except Exception as e:
        session.rollback()
        import traceback; traceback.print_exc()
        print(f"❌ Chyba, rollback: {e}", file=sys.stderr)
        return 4
    finally:
        session.close()


if __name__ == "__main__":
    sys.exit(main())
