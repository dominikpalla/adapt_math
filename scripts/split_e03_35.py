"""
Rozdělení úlohy e03_35 (megablok 9 nerovnic) na 9 samostatných úloh
e03_35_1..e03_35_9. Řeší připomínku Andrei 2026-08-28.

Postup:
  1. Přečte původní e03_35 (jen ověření, že existuje).
  2. INSERT 9 nových úloh e03_35_1..e03_35_9 s odpovídajícím zadáním
     a jedinou správnou odpovědí.
  3. DELETE původní e03_35.
  Vše v jedné transakci.

Idempotentní: druhé spuštění selže na tom, že e03_35 už neexistuje.

Použití:
    DATABASE_URL=... python scripts/split_e03_35.py                # dry-run
    DATABASE_URL=... python scripts/split_e03_35.py --commit
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from database import init_db
from model import MathTask

# 9 podúloh: (task_id_suffix, zadání_LaTeX, expected_LaTeX)
SUBTASKS = [
    ("1", r"x^3-x^2\leq 0",
        r"x\in(-\infty,1\rangle"),
    ("2", r"(x^2+x+1)(x^2-20)>0",
        r"x\in(-\infty,-2\sqrt{5})\cup(2\sqrt{5},\infty)"),
    ("3", r"\frac{x^2-4}{x^2+2x}\geq 0",
        r"x\in(-\infty,-2)\cup(-2,0)\cup(2,\infty)"),
    ("4", r"\frac{x^2+1}{1-x^2}\geq 0",
        r"x\in(-1,1)"),
    ("5", r"\frac{2-x^2}{x^2+x+1}\geq 0",
        r"x\in\langle-\sqrt{2},\sqrt{2}\rangle"),
    ("6", r"\frac{x^2-x}{x-3}\geq x",
        r"x\in(-\infty,0\rangle\cup(3,\infty)"),
    ("7", r"\frac{x^5-4x^4}{2x^4-x^3}\geq 1",
        r"x\in(-\infty,0)\cup\langle 3-2\sqrt{2},1/2)\cup\langle 3+2\sqrt{2},\infty)"),
    ("8", r"\frac{1-x^2}{(-x^2-4)^3}\geq 0",
        r"x\in\langle-1,1\rangle"),
    ("9", r"(x^3-1)(x^2+1)<0",
        r"x\in(-\infty,1)"),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    args = parser.parse_args()
    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr)
        return 2

    SessionLocal = init_db(args.db_url)
    sess = SessionLocal()
    try:
        orig = sess.query(MathTask).filter_by(task_id="e03_35").first()
        if not orig:
            print("e03_35 neexistuje. Nic se nedělá (možná už rozdělené?).")
            return 1

        # 1) INSERT 9 nových
        for suffix, latex, expected in SUBTASKS:
            new_id = f"e03_35_{suffix}"
            if sess.query(MathTask).filter_by(task_id=new_id).first():
                print(f"⚠ {new_id} už existuje, přeskakuji.")
                continue
            new_task = MathTask(
                task_id=new_id,
                content_latex=f"Řešte nerovnici: ${latex}$",
                results=[{
                    "key": "vysledek",
                    "label_latex": "= ",
                    "type": "mathlive",
                    "expected": expected,
                    "tolerance": 0.0,
                }],
                category=orig.category,
                properties=orig.properties,
                task_type=orig.task_type,
                skills=orig.skills,
                cognitive_load=orig.cognitive_load,
                irt_difficulty=orig.irt_difficulty,
                irt_discrimination=orig.irt_discrimination,
                knowledge_vector=orig.knowledge_vector,
                graph_vector=orig.graph_vector,
            )
            sess.add(new_task)
            print(f"+ {new_id}: {latex[:50]}... -> {expected[:40]}...")

        # 2) DELETE původní
        sess.delete(orig)
        print(f"- e03_35 (původní megablok) smazána")

        if args.commit:
            sess.commit()
            print("\n✓ COMMIT proveden.")
        else:
            sess.rollback()
            print("\n(DRY-RUN — nic se nezapsalo. Pro zápis přidej --commit.)")
        return 0
    finally:
        sess.close()


if __name__ == "__main__":
    sys.exit(main())
