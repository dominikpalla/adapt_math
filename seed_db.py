"""
Naplnění databáze úlohami pro task checker.

Spuštění:  python seed_db.py
- Smaže tabulku math_tasks (a všechny FK na ni) a vytvoří ji znovu
- Naplní úlohami z proměnné TASKS (níže)

Konvence task_id:
- "cv{N}_{i}"  kde N je číslo cvičení (01..13) a i index úlohy ve cvičení (1..N).
- Aktuálně máme jen cv04 (Limita funkce — aritmetika limit).

Konvence pro `results`:
- Každá úloha má pole `results` = kolekce pojmenovaných výsledků.
- Frontend pro každý výsledek zobrazí `label_latex` jako prefix a vstupní
  pole (MathLive / číslo / radio / textarea) podle `type`.
- Viz docstring v model.py.
"""

from database import init_db
from model import MathTask, Base

DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"


# =============================================================================
# CVIČENÍ 4 — Limita funkce: definice a věta o aritmetice limit
# Zdroj: skripta „Základy matematiky 1", Pavel Pražák a Petr Bauer (KIKM FIM UHK)
# =============================================================================

TASKS = [
    # --- 4.1, 4.2, 4.3: negace výroků (open_text + případně obměna) ---
    {
        "task_id": "cv04_1",
        "content_latex": (
            r"Formulujte negaci výroku o tranzitivnosti uspořádání reálných čísel: "
            r"\textit{Pro libovolnou trojici } $x \in \mathbb{R},\ y \in \mathbb{R},\ z \in \mathbb{R}$ "
            r"\textit{ platí: jestliže } $x \le y$ \textit{ a } $y \le z,$ \textit{ pak } $x \le z.$"
        ),
        "results": [
            {
                "key": "negace",
                "label_latex": r"\text{Negace: }",
                "type": "open_text",
                "expected": (
                    r"Existuje trojice $x \in \mathbb{R},\ y \in \mathbb{R},\ z \in \mathbb{R}$ "
                    r"taková, že $x \le y$ a $y \le z$ a zároveň $x > z.$"
                ),
            },
        ],
        "cognitive_load": "B",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
    },
    {
        "task_id": "cv04_2",
        "content_latex": (
            r"Formulujte negaci a obměnu výroku: "
            r"\textit{Jsou-li } $U_1(a)$ \textit{ a } $U_2(a)$ \textit{ okolí bodu } $a \in \mathbb{R}^*,$ "
            r"\textit{ potom } $U_1(a) \cap U_2(a)$ \textit{ je také okolí bodu } $a.$"
        ),
        "results": [
            {
                "key": "negace", "label_latex": r"\text{Negace: }", "type": "open_text",
                "expected": (
                    r"Existují okolí $U_1(a)$ a $U_2(a)$ bodu $a \in \mathbb{R}^*$ "
                    r"taková, že $U_1(a) \cap U_2(a)$ není okolí bodu $a.$"
                ),
            },
            {
                "key": "obmena", "label_latex": r"\text{Obměna: }", "type": "open_text",
                "expected": (
                    r"Jestliže $U_1(a) \cap U_2(a)$ není okolí bodu $a \in \mathbb{R}^*,$ "
                    r"potom $U_1(a)$ není okolí bodu $a$ nebo $U_2(a)$ není okolí bodu $a.$"
                ),
            },
        ],
        "cognitive_load": "C",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
    },
    {
        "task_id": "cv04_3",
        "content_latex": (
            r"Formulujte negaci a obměnu výroku: "
            r"\textit{Jsou-li } $a, b \in \mathbb{R}^*,\ a \ne b,$ \textit{ pak existují } $U(a)$ "
            r"\textit{ a } $U(b)$ \textit{ taková, že } $U(a) \cap U(b) = \emptyset.$"
        ),
        "results": [
            {
                "key": "negace", "label_latex": r"\text{Negace: }", "type": "open_text",
                "expected": (
                    r"Existují $a, b \in \mathbb{R}^*,\ a \ne b,$ taková, že pro každá okolí "
                    r"$U(a)$ a $U(b)$ platí $U(a) \cap U(b) \ne \emptyset.$"
                ),
            },
            {
                "key": "obmena", "label_latex": r"\text{Obměna: }", "type": "open_text",
                "expected": (
                    r"Jestliže pro každá okolí $U(a)$ a $U(b)$ bodů $a, b \in \mathbb{R}^*$ platí "
                    r"$U(a) \cap U(b) \ne \emptyset,$ pak $a = b.$"
                ),
            },
        ],
        "cognitive_load": "C",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
    },

    # --- 4.4 a)–o): aritmetika limit (15 úloh) ---
    # Pro každou limitu má `results` jedno pole "lim".
    # `label_latex` necháme prázdný (= zobrazí se rovnou MathLive input).
    {
        "task_id": "cv04_4",
        "content_latex": r"\lim_{x \to 3} \frac{5x^2 - 8x - 13}{x^2 - 5}",
        "results": [{"key": "lim", "label_latex": "", "type": "decimal",
                     "expected": 2.0, "tolerance": 0.001}],
        "cognitive_load": "B", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_5",
        "content_latex": r"\lim_{x \to 2} \frac{3x^2 - x - 10}{x^2 - 4}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"\frac{11}{4}"}],
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_6",
        "content_latex": r"\lim_{x \to 3} \frac{x^4 - 81}{2x^2 - 5x - 3}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"\frac{108}{7}"}],
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_7",
        "content_latex": r"\lim_{x \to -2} \frac{\frac{1}{x} + \frac{1}{2}}{x^3 + 8}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"-\frac{1}{48}"}],
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_8",
        "content_latex": r"\lim_{x \to 2} \frac{x^3 - 2x^2 - 4x + 8}{x^4 - 8x^2 + 16}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"\frac{1}{4}"}],
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_9",
        "content_latex": r"\lim_{x \to 2} \frac{x^4 - 2x^3 + 2x^2 - 5x + 2}{x - 2}",
        "results": [{"key": "lim", "label_latex": "", "type": "decimal",
                     "expected": 11.0, "tolerance": 0.001}],
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_10",
        "content_latex": r"\lim_{x \to 4} \frac{3 - \sqrt{x + 5}}{x - 4}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"-\frac{1}{6}"}],
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_11",
        "content_latex": r"\lim_{x \to -1} \frac{x^3 + 1}{\sqrt{x^2 - 3x} + 2x}",
        "results": [{"key": "lim", "label_latex": "", "type": "decimal",
                     "expected": 4.0, "tolerance": 0.001}],
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_12",
        "content_latex": r"\lim_{x \to 0} \frac{x^3 - 7x}{x^3}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"-\infty"}],
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_13",
        "content_latex": r"\lim_{x \to 0} \frac{x^2 - 1}{x^2}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"-\infty"}],
        "cognitive_load": "B", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_14",
        "content_latex": r"\lim_{x \to 0} \frac{x^4 + 5x - 3}{2 - \sqrt{x^2 + 4}}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"\infty"}],
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
    },
    {
        # Limita zleva = -∞, zprava = +∞ → neexistuje. Multiple choice je tu nejjistější.
        "task_id": "cv04_15",
        "content_latex": r"\lim_{x \to 1} \frac{x^3 - 1}{(x - 1)^2}",
        "results": [{
            "key": "lim", "label_latex": "",
            "type": "multiple_choice",
            "options": [
                {"key": "finite", "label_latex": r"\text{konečná hodnota}"},
                {"key": "plus_inf", "label_latex": r"+\infty"},
                {"key": "minus_inf", "label_latex": r"-\infty"},
                {"key": "dne", "label_latex": r"\text{limita neexistuje}"},
            ],
            "expected": "dne",
        }],
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_16",
        "content_latex": r"\lim_{x \to +\infty} \frac{x^2 + 3x - 4}{1 - 5x^2}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"-\frac{1}{5}"}],
        "cognitive_load": "B", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_17",
        "content_latex": r"\lim_{x \to +\infty} \frac{2x^2 + 7x - 2}{6x^3 - 4x + 3}",
        "results": [{"key": "lim", "label_latex": "", "type": "decimal",
                     "expected": 0.0, "tolerance": 0.001}],
        "cognitive_load": "B", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv04_18",
        "content_latex": r"\lim_{x \to -\infty} \frac{(1 - 2x)^2 (3 - x)}{x^2 - 7x + 10}",
        "results": [{"key": "lim", "label_latex": "", "type": "latex_expr",
                     "expected": r"\infty"}],
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
    },
]


def seed_database():
    print("🌱 Plním databázi…")
    SessionLocal = init_db(DB_URL)
    session = SessionLocal()
    try:
        # 1) Drop & recreate (cascade kvůli starým FK z předchozí verze schématu)
        from sqlalchemy import text
        session.execute(text("DROP TABLE IF EXISTS interaction_logs CASCADE"))
        session.execute(text("DROP TABLE IF EXISTS students CASCADE"))
        session.execute(text("DROP TABLE IF EXISTS math_tasks CASCADE"))
        session.commit()
        Base.metadata.create_all(bind=session.bind)
        print("🗑️  Tabulka math_tasks vyčištěna a znovu vytvořena.")

        # 2) Vložení úloh
        objs = [MathTask(**spec) for spec in TASKS]
        session.add_all(objs)
        session.commit()
        print(f"✅ Vloženo {len(objs)} úloh ({objs[0].task_id} … {objs[-1].task_id}).")

        # Stručná statistika typů
        from collections import Counter
        type_counts = Counter(r["type"] for t in TASKS for r in t["results"])
        print(f"   Typy výsledků: {dict(type_counts)}")

    except Exception as e:
        session.rollback()
        print(f"❌ Chyba: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed_database()
