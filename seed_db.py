"""
Naplnění databáze úlohami pro task checker.

Spuštění:  python seed_db.py
- Smaže tabulku math_tasks (a všechny FK na ni)
- Vytvoří ji znovu a naplní ji úlohami ze složky tasks/

Definice jednotlivých úloh leží v `tasks/cvNN.py` (jeden soubor =
jedno cvičení ze skripta „Základy matematiky 1").
"""

from sqlalchemy import text

import os

from database import init_db
from model import MathTask, Base
from tasks import ALL_TASKS

# Pro produkci preferujeme DATABASE_URL env var (stejně jako app.py);
# lokálně padá zpět na výchozí dev hodnotu.
DB_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath",
)


def seed_database():
    print(f"🌱 Plním databázi… ({len(ALL_TASKS)} úloh celkem)")
    SessionLocal = init_db(DB_URL)
    session = SessionLocal()
    try:
        # 1) Drop & recreate (cascade kvůli starým FK z předchozí verze schématu)
        session.execute(text("DROP TABLE IF EXISTS interaction_logs CASCADE"))
        session.execute(text("DROP TABLE IF EXISTS students CASCADE"))
        session.execute(text("DROP TABLE IF EXISTS math_tasks CASCADE"))
        session.commit()
        Base.metadata.create_all(bind=session.bind)
        print("🗑️  Tabulka math_tasks vyčištěna a znovu vytvořena.")

        # 2) Vložení úloh
        if not ALL_TASKS:
            print("⚠️  ALL_TASKS je prázdný — žádné úlohy nebyly vloženy.")
            return
        objs = [MathTask(**spec) for spec in ALL_TASKS]
        session.add_all(objs)
        session.commit()
        print(f"✅ Vloženo {len(objs)} úloh ({objs[0].task_id} … {objs[-1].task_id}).")

        # 3) Statistika typů
        from collections import Counter
        type_counts = Counter(r["type"] for t in ALL_TASKS for r in t["results"])
        print(f"   Typy výsledků: {dict(type_counts)}")

        # 4) Distribuce po cvičeních
        by_cv = Counter(t["task_id"].split("_")[0] for t in ALL_TASKS)
        print(f"   Po cvičeních:  {dict(sorted(by_cv.items()))}")

    except Exception as e:
        session.rollback()
        print(f"❌ Chyba: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed_database()
