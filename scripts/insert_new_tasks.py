"""
Idempotentní insert nových úloh z tasks/ modulů do DB.

Bezpečnostní záruky:
  - Jen INSERT — nikdy DELETE ani UPDATE.
  - Skipuje task_id, které v DB už existují (žádný přepis anotací).
  - Před akcí ukazuje dry-run přehled a čeká na `--commit` flag.
  - Vše v jedné transakci — buď všechny nové úlohy, nebo žádná.

Použití:
    # dry-run: ukáže, co by se přidalo
    DATABASE_URL=postgresql://... python scripts/insert_new_tasks.py

    # ostrý insert
    DATABASE_URL=postgresql://... python scripts/insert_new_tasks.py --commit

Nikdy NEspoušit `python seed_db.py` — ta drop-recreatne tabulku a smaže
všechny existující anotace.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import init_db
from model import MathTask
from tasks import ALL_TASKS


ALLOWED_RESULT_TYPES = {"mathlive", "decimal", "multiple_choice"}


def validate_tasks(tasks: list[dict]) -> list[str]:
    """Základní validace před insertem. Vrací seznam problémů."""
    problems = []
    seen_ids: set[str] = set()
    for i, t in enumerate(tasks):
        prefix = f"[{i}] {t.get('task_id', '?')}: "
        tid = t.get("task_id")
        if not tid or not isinstance(tid, str) or not tid.strip():
            problems.append(f"{prefix}task_id prázdný")
            continue
        if tid in seen_ids:
            problems.append(f"{prefix}duplicitní task_id v modulech")
        seen_ids.add(tid)
        if not t.get("content_latex"):
            problems.append(f"{prefix}chybí content_latex")
        results = t.get("results") or []
        if not results:
            problems.append(f"{prefix}chybí results")
        for j, r in enumerate(results):
            rp = f"{prefix}results[{j}]: "
            rt = r.get("type")
            if rt not in ALLOWED_RESULT_TYPES:
                problems.append(f"{rp}nepovolený type={rt!r} (povoleny jen {sorted(ALLOWED_RESULT_TYPES)})")
            if "key" not in r or not r["key"]:
                problems.append(f"{rp}chybí key")
            if "expected" not in r:
                problems.append(f"{rp}chybí expected")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Idempotentní INSERT nových úloh do DB.")
    parser.add_argument("--commit", action="store_true",
                        help="Bez tohoto flagu jen dry-run (žádný zápis).")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    parser.add_argument("--prefix",
                        help="Zpracovat jen úlohy s task_id začínající tímto prefixem "
                             "(např. `ss` nebo `umat`).")
    args = parser.parse_args()

    if not args.db_url:
        print("Chyba: nastav DATABASE_URL nebo --db-url.", file=sys.stderr)
        return 2

    tasks_to_consider = list(ALL_TASKS)
    if args.prefix:
        tasks_to_consider = [t for t in tasks_to_consider if t["task_id"].startswith(args.prefix)]
        print(f"Filtr prefix={args.prefix!r} → {len(tasks_to_consider)} úloh z {len(ALL_TASKS)} v ALL_TASKS.")

    # 1) Validace
    problems = validate_tasks(tasks_to_consider)
    if problems:
        print("❌ Validace selhala:")
        for p in problems:
            print(f"  {p}")
        return 3
    print(f"✅ Validace prošla ({len(tasks_to_consider)} úloh).")

    # 2) Připojení k DB
    SessionLocal = init_db(args.db_url)
    session = SessionLocal()
    try:
        existing_ids = {row[0] for row in session.query(MathTask.task_id).all()}
        print(f"V DB je aktuálně {len(existing_ids)} úloh.")

        new = [t for t in tasks_to_consider if t["task_id"] not in existing_ids]
        skip = [t for t in tasks_to_consider if t["task_id"] in existing_ids]
        print(f"  Novy k INSERT:                 {len(new)}")
        print(f"  Skip (task_id už existuje):    {len(skip)}")
        if new:
            print(f"  Prvních 10 nových: {[t['task_id'] for t in new[:10]]}")
            print(f"  Posledních 10:     {[t['task_id'] for t in new[-10:]]}")

        if not args.commit:
            print()
            print("── DRY-RUN ─────────────────────────────────────")
            print("Nic se nezapisuje. Pro skutečný INSERT přidej --commit.")
            return 0

        if not new:
            print("Žádné nové úlohy — nic k INSERTu.")
            return 0

        # 3) INSERT v jedné transakci
        print()
        print("── COMMIT — insertuju ─────────────────────────")
        for t in new:
            obj = MathTask(
                task_id=t["task_id"],
                content_latex=t["content_latex"],
                results=t["results"],
                cognitive_load=t.get("cognitive_load"),
                category=t.get("category"),
                properties=t.get("properties"),
                task_type=t.get("task_type"),
                skills=t.get("skills"),
                knowledge_vector=t.get("knowledge_vector"),
                graph_vector=t.get("graph_vector"),
                irt_difficulty=t.get("irt_difficulty"),
                irt_discrimination=t.get("irt_discrimination"),
            )
            session.add(obj)
        session.commit()
        print(f"✅ Vloženo {len(new)} nových úloh.")

        # 4) Post-check
        after_count = session.query(MathTask).count()
        print(f"Řádků v DB nyní: {after_count}")

        return 0
    except Exception as e:
        session.rollback()
        print(f"❌ Chyba, rollback: {e}", file=sys.stderr)
        import traceback; traceback.print_exc()
        return 4
    finally:
        session.close()


if __name__ == "__main__":
    sys.exit(main())
