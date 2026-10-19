"""
Parser ZŠ Výrazy (soubor Downloads/výrazy.tex) → task_id prefix `zsv_NNN`.

334 úloh, 12 typů zadání (Upravte, Zjednodušte, Vynásobte, Dělte, Rozložte,
Vytkněte -1, Doplňte výraz, Určete smysl, Určete smysl + zjednodušte, ...).

Struktura každé úlohy:
  \\item
  \\textbf{<nadpis>}
  \\begin{tabularx}{\\linewidth}{@{}Xr@{}}
  $\\displaystyle <výraz>\\; \\boldsymbol{=}$ &
  $\\displaystyle \\left[\\,<odpověď>\\,\\right]$
  \\end{tabularx}

Výstup:
  task_id = zsv_001..zsv_NNN
  content_latex = "<nadpis> $<výraz>$"
  results = [{"key": "vysledek", "label_latex": "= ", "type": "mathlive",
              "expected": "<odpověď>", "tolerance": 0}]
  category = "SŠ - Algebraické výrazy"
  cognitive_load = "A"
  irt_difficulty = -2.0, irt_discrimination = 1.0
  skills: podle typu zadání

Použití:
    DATABASE_URL=... python scripts/extract_zsv.py                # dry-run
    DATABASE_URL=... python scripts/extract_zsv.py --commit
"""

from __future__ import annotations
import argparse, os, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from database import init_db
from model import MathTask

SRC = Path("/Users/dominikpalla/Downloads/výrazy.tex")

# Mapování nadpisů (přesně jak jsou v souboru) → skills a cognitive_load
# Všechny ZŠ Výrazy jsou v kategorii "SŠ - Algebraické výrazy" (nejblíž v taxonomii).
HEADING_META = {
    "Upravte:": {
        "skills": ["Dovednosti - Vytýkání/roznásobení výrazu v závorce", "Dovednosti - Aplikace vzorce"],
    },
    "Zjednodušte:": {
        "skills": ["Dovednosti - Vytýkání/roznásobení výrazu v závorce"],
    },
    "Rozložte na součin [využijte vytýkání a vzorce $(a\\pm b)^2,\\ a^2-b^2$]:": {
        "skills": ["Dovednosti - Vytýkání/roznásobení výrazu v závorce", "Dovednosti - Aplikace vzorce"],
    },
    "Určete hodnoty proměnné, pro které nemá výraz smysl.": {
        "skills": ["Dovednosti - Ověření/využití vlastností"],
    },
    "Určete, kdy mají dané výrazy smysl.": {
        "skills": ["Dovednosti - Ověření/využití vlastností"],
    },
    "Určete, kdy má výraz smysl, a zjednodušte ho.": {
        "skills": ["Dovednosti - Ověření/využití vlastností", "Dovednosti - Úpravy zlomků"],
    },
    "Doplňte výraz tak, aby platila rovnost.": {
        "skills": ["Dovednosti - Úpravy zlomků"],
    },
    "Vynásobte výrazy:": {
        "skills": ["Dovednosti - Vytýkání/roznásobení výrazu v závorce"],
    },
    "Upravte výrazy:": {
        "skills": ["Dovednosti - Vytýkání/roznásobení výrazu v závorce"],
    },
    "Vytkněte $-1$ z výrazů:": {
        "skills": ["Dovednosti - Vytýkání/roznásobení výrazu v závorce"],
    },
    "Dané výrazy rozložte v součin vytknutím společného činitele před závorku:": {
        "skills": ["Dovednosti - Vytýkání/roznásobení výrazu v závorce"],
    },
    "Dělte:": {
        "skills": ["Dovednosti - Vytýkání/roznásobení výrazu v závorce", "Dovednosti - Úpravy zlomků"],
    },
}


ITEM_RE = re.compile(
    r'\\item\s*\n\s*'
    r'\\textbf\{((?:[^}]|\{[^}]*\})+)\}\s*\n\s*'
    r'\\begin\{tabularx\}\{\\linewidth\}\{@\{\}Xr@\{\}\}(.*?)\\end\{tabularx\}',
    re.DOTALL,
)


def parse_tabularx_body(body: str) -> tuple[str, str] | None:
    """Z těla tabularx (vlevo výraz $... \\boldsymbol{=}$ a vpravo $...\\left[\\,...\\,\\right]$)
    vrátí (zadání_latex, odpověď_latex) nebo None."""
    # oddělíme &
    parts = body.split('&')
    if len(parts) != 2:
        return None
    left, right = parts[0].strip(), parts[1].strip()
    # Vlevo: $\displaystyle <výraz>\; \boldsymbol{=}$ nebo bez \boldsymbol{=} (u 'Určete smysl')
    m_left = re.match(
        r'^\$\\displaystyle\s*(.*?)(?:\\;\s*\\boldsymbol\{=\})?\s*\$\s*$',
        left,
        re.DOTALL,
    )
    if not m_left:
        return None
    expr = m_left.group(1).strip()
    # Vpravo: $\displaystyle \left[\,<odp>\,\right]$
    m_right = re.match(
        r'^\$\\displaystyle\s*\\left\[\\,(.*?)\\,\\right\]\s*\$\s*$',
        right,
        re.DOTALL,
    )
    if not m_right:
        return None
    answer = m_right.group(1).strip()
    # strip whitespace + newlines
    expr = re.sub(r'\s+', ' ', expr).strip()
    answer = re.sub(r'\s+', ' ', answer).strip()
    return expr, answer


def build_task(idx: int, heading: str, expr: str, answer: str) -> dict:
    heading_clean = heading.strip()
    # Content: celé zadání jako česká věta + math inline
    # Pro úlohy, kde výraz už končí znaménkem "=" bez boldsymbol (např. "Určete smysl"), neposouváme
    has_eq_suffix = r'\boldsymbol{=}' in heading or heading_clean.endswith(':')
    # Všechny jsou mathlive s expected = raw answer
    results = [{
        "key": "vysledek",
        "label_latex": "= ",
        "type": "mathlive",
        "expected": answer,
        "tolerance": 0,
    }]
    meta = HEADING_META.get(heading_clean, {})
    skills = meta.get("skills", [])
    return {
        "task_id": f"zsv_{idx:03d}",
        "content_latex": f"{heading_clean} ${expr}$",
        "results": results,
        "category": "SŠ - Algebraické výrazy",
        "cognitive_load": "A",
        "irt_difficulty": -2.0,
        "irt_discrimination": 1.0,
        "skills": skills,
        "properties": [],
        "task_type": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    args = parser.parse_args()
    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr); return 2

    content = SRC.read_text(encoding='utf-8')
    items = []
    for m in ITEM_RE.finditer(content):
        heading = m.group(1)
        body = m.group(2)
        parsed = parse_tabularx_body(body)
        if not parsed:
            print(f"⚠ nepodařilo se parsovat položku s nadpisem {heading[:40]}...", file=sys.stderr)
            continue
        expr, answer = parsed
        items.append((heading, expr, answer))

    print(f"Extrahováno {len(items)} úloh z {SRC.name}.")

    # Rozdělení per nadpis
    from collections import Counter
    cnt = Counter(h for h, _, _ in items)
    for h, n in cnt.most_common():
        print(f"  {n:>3}× {h[:60]}")

    # Vlož do DB
    SessionLocal = init_db(args.db_url)
    sess = SessionLocal()
    try:
        inserted = 0
        skipped = 0
        for idx, (heading, expr, answer) in enumerate(items, start=1):
            task = build_task(idx, heading, expr, answer)
            exists = sess.query(MathTask).filter_by(task_id=task["task_id"]).first()
            if exists:
                skipped += 1
                continue
            new_task = MathTask(**{k: v for k, v in task.items()})
            sess.add(new_task)
            inserted += 1

        print(f"\nK vložení: {inserted}, přeskočeno (už existuje): {skipped}")
        if args.commit:
            sess.commit()
            print("✓ COMMIT proveden.")
        else:
            sess.rollback()
            print("(DRY-RUN — nic se nezapsalo. Pro zápis přidej --commit.)")
        return 0
    finally:
        sess.close()


if __name__ == "__main__":
    sys.exit(main())
