"""
Vyčistí LaTeX layout junk z `results[*].expected` u e-prefix úloh.

Zdroj problému: parser v extract_umat_v2.py někdy nechal v answer
konečnovou značku `\\clubsuit` a různé `\\vspace{2mm}`, `\\pagebreak`,
`\\section{...}` — to jsou UMAT skriptum konvence, které neplatí
pro anotaci úloh.

Skript:
  - Nedělá žádné DELETE ani UPDATE task_id.
  - Nemění results[*].type (mathlive zůstává mathlive).
  - Nemění results[*].key.
  - Jen strip: \\clubsuit  |  \\vspace{...}  |  \\vspace ...  |
                \\pagebreak  |  \\section{...}  |  \\subsection{...}
  - Trim whitespace + koncové tečky.
  - Idempotentní.

Použití:
    DATABASE_URL=... python scripts/cleanup_e_layout_junk.py               # dry-run
    DATABASE_URL=... python scripts/cleanup_e_layout_junk.py --commit
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy.orm.attributes import flag_modified

from database import init_db
from model import MathTask


JUNK_PATTERNS = [
    re.compile(r"\\clubsuit\b"),
    re.compile(r"\\vspace\s*\{[^}]*\}"),
    re.compile(r"\\vspace\s+\S+"),            # \vspace 2mm bez závorek
    re.compile(r"\\pagebreak\b"),
    re.compile(r"\\newpage\b"),
    re.compile(r"\\section\s*\{[^}]*\}"),
    re.compile(r"\\subsection\s*\{[^}]*\}"),
    re.compile(r"\\bigskip\b"),
    re.compile(r"\\medskip\b"),
    re.compile(r"\\smallskip\b"),
]


def clean(s: str) -> tuple[str, bool]:
    if not isinstance(s, str) or not s:
        return s, False
    original = s
    for pat in JUNK_PATTERNS:
        s = pat.sub("", s)
    # Odstranit osiřelý prázdný `$$` pár, který zbyl po strippingu
    # (např. "$Df = ...$ \clubsuit" → "$Df = ...$ $$" po strippingu \clubsuit
    #  → chceme "$Df = ...$")
    s = re.sub(r"\$\s*\$", "", s)
    # Redukce whitespace
    s = re.sub(r"\s+", " ", s).strip()
    # Iterativně strip koncové artefakty (thin-space, osiřelý backslash,
    # středník, čárka, whitespace) — může jich být několik za sebou.
    # POZOR: NE tečku — ta může být součástí věty (u logika-tasků).
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\\,\s*$", "", s)     # \, thin space
        s = re.sub(r"\\\s*$", "", s)      # osiřelý backslash
        s = re.sub(r"[,;\s]+$", "", s)    # čárka, středník, whitespace
    return s.strip(), s.strip() != original


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    parser.add_argument("--prefix", default="e",
                        help="task_id prefix pro filtr (default 'e' — jen e-tasky).")
    args = parser.parse_args()

    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr)
        return 2

    SessionLocal = init_db(args.db_url)
    session = SessionLocal()
    try:
        tasks = session.query(MathTask).filter(
            MathTask.task_id.like(f"{args.prefix}%")
        ).all()
        print(f"Načteno {len(tasks)} úloh s prefixem '{args.prefix}%'.")

        changed = 0
        samples = []
        for t in tasks:
            if not isinstance(t.results, list):
                continue
            row_changed = False
            for r in t.results:
                if not isinstance(r, dict):
                    continue
                exp = r.get("expected")
                if isinstance(exp, str):
                    new, ch = clean(exp)
                    if ch:
                        if len(samples) < 12:
                            samples.append((t.task_id, exp, new))
                        r["expected"] = new
                        row_changed = True
                elif isinstance(exp, list):
                    new_list = []
                    list_changed = False
                    for item in exp:
                        if isinstance(item, str):
                            ni, ch = clean(item)
                            if ch: list_changed = True
                            new_list.append(ni)
                        else:
                            new_list.append(item)
                    if list_changed:
                        r["expected"] = new_list
                        row_changed = True
            if row_changed:
                flag_modified(t, "results")
                changed += 1

        print(f"Dotčeno: {changed} úloh.")
        if samples:
            print()
            print("── UKÁZKY (před → po) ───────────────────────────")
            for tid, before, after in samples:
                print(f"  {tid}")
                print(f"    před: {before[:110]}")
                print(f"    po:   {after[:110]}")
                print()

        if not args.commit:
            print("── DRY-RUN — nic se nezapisuje. Pro ostrý běh přidej --commit.")
            session.rollback()
            return 0

        if changed == 0:
            print("Nic k migraci.")
            return 0

        session.commit()
        print(f"✅ Uloženo. Dotčeno {changed} úloh.")
        return 0
    except Exception as e:
        session.rollback()
        import traceback; traceback.print_exc()
        return 4
    finally:
        session.close()


if __name__ == "__main__":
    sys.exit(main())
