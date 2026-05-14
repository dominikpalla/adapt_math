from database import init_db
from model import MathTask, Student, InteractionLog, Base
import json
import math

# URL k naší běžící Docker PostgreSQL databázi
DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"

# ----------------------------------------------------------------------------
# Konvence pro `result_type` a `correct_answer`
# ----------------------------------------------------------------------------
# Frontend renderuje `content_latex` přes KaTeX a vstup řeší pomocí MathLive
# (https://github.com/arnog/mathlive). Pro vyhodnocení odpovědi využíváme
# MathLive Compute Engine, který LaTeX odpověď převede na MathJSON a porovná
# se vzorovým řešením (`.isSame()` symbolicky, `.N()` numericky s tolerancí).
#
#   result_type            | correct_answer (JSON)
#   -----------------------+------------------------------------------------
#   "decimal"              | float                  (porovnání numericky ± tolerance)
#   "fraction"             | {"num": int, "den": int}      (a/b, exaktně)
#   "latex_expr"           | "<latex>"              (Compute Engine .isSame nebo .N)
#   "multiple_choice"      | {"options":[{key,label}], "correct_key":"..."}
#   "open_text"            | {"expected_summary":"<latex/text>", "eval_method":"llm"}
#   "multi_field"          | {"fields":[{key, label, input_type, expected,
#                          |             tolerance?, eval_method?}]}
#
# `multi_field` je univerzální obálka — student vyplňuje N pojmenovaných polí
# přes MathLive (např. „interval roste", „lokální minimum", „inflexní bod").
# Každé pole má vlastní `input_type` (`latex_expr` / `decimal` / `open_text`).
# ----------------------------------------------------------------------------

# =============================================================================
# Cvičení 4 — Limita funkce: definice, věta o aritmetice limit
# Zdroj: skripta „Základy matematiky 1" (cv04.tex), Pavel Pražák a Petr Bauer.
# Pilotní převod — IRT obtížnost/diskriminace jsou orientační, expert doladí.
# =============================================================================

_CV04_TASKS = [
    # ----- Negace výroků (open_text / multi_field s obměnou) -----
    {
        "task_id": "cv04_neg_01_tranzitivnost",
        "content_latex": (
            r"Formulujte negaci výroku o tranzitivnosti uspořádání reálných čísel: "
            r"\textit{Pro libovolnou trojici } $x \in \mathbb{R},\ y \in \mathbb{R},\ z \in \mathbb{R}$ "
            r"\textit{ platí: jestliže } $x \le y$ \textit{ a } $y \le z,$ \textit{ pak } $x \le z.$"
        ),
        "result_type": "open_text",
        "correct_answer": {
            "expected_summary": (
                r"Existuje trojice $x \in \mathbb{R},\ y \in \mathbb{R},\ z \in \mathbb{R}$ "
                r"taková, že $x \le y$ a $y \le z$ a zároveň $x > z.$"
            ),
            "eval_method": "llm",
        },
        "cognitive_load": "B",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
        "irt_difficulty": -0.3, "irt_discrimination": 0.8,
    },
    {
        "task_id": "cv04_neg_02_okoli_prunik",
        "content_latex": (
            r"Formulujte negaci a obměnu výroku: "
            r"\textit{Jsou-li } $U_1(a)$ \textit{ a } $U_2(a)$ \textit{ okolí bodu } $a \in \mathbb{R}^*,$ "
            r"\textit{potom } $U_1(a) \cap U_2(a)$ \textit{ je také okolí bodu } $a.$"
        ),
        "result_type": "multi_field",
        "correct_answer": {
            "fields": [
                {
                    "key": "negace",
                    "label": "Negace",
                    "input_type": "open_text",
                    "expected": (
                        r"Existují okolí $U_1(a)$ a $U_2(a)$ bodu $a \in \mathbb{R}^*$ "
                        r"taková, že $U_1(a) \cap U_2(a)$ není okolí bodu $a.$"
                    ),
                    "eval_method": "llm",
                },
                {
                    "key": "obmena",
                    "label": "Obměna",
                    "input_type": "open_text",
                    "expected": (
                        r"Jestliže $U_1(a) \cap U_2(a)$ není okolí bodu $a \in \mathbb{R}^*,$ "
                        r"potom $U_1(a)$ není okolí bodu $a$ nebo $U_2(a)$ není okolí bodu $a.$"
                    ),
                    "eval_method": "llm",
                },
            ]
        },
        "cognitive_load": "C",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
        "irt_difficulty": 0.1, "irt_discrimination": 0.9,
    },
    {
        "task_id": "cv04_neg_03_disjunktni_okoli",
        "content_latex": (
            r"Formulujte negaci a obměnu výroku: "
            r"\textit{Jsou-li } $a, b \in \mathbb{R}^*,\ a \ne b,$ \textit{pak existují } $U(a)$ \textit{ a } $U(b)$ "
            r"\textit{ taková, že } $U(a) \cap U(b) = \emptyset.$"
        ),
        "result_type": "multi_field",
        "correct_answer": {
            "fields": [
                {
                    "key": "negace",
                    "label": "Negace",
                    "input_type": "open_text",
                    "expected": (
                        r"Existují $a, b \in \mathbb{R}^*,\ a \ne b,$ taková, že pro každá okolí "
                        r"$U(a)$ a $U(b)$ platí $U(a) \cap U(b) \ne \emptyset.$"
                    ),
                    "eval_method": "llm",
                },
                {
                    "key": "obmena",
                    "label": "Obměna",
                    "input_type": "open_text",
                    "expected": (
                        r"Jestliže pro každá okolí $U(a)$ a $U(b)$ bodů $a, b \in \mathbb{R}^*$ platí "
                        r"$U(a) \cap U(b) \ne \emptyset,$ pak $a = b.$"
                    ),
                    "eval_method": "llm",
                },
            ]
        },
        "cognitive_load": "C",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
        "irt_difficulty": 0.2, "irt_discrimination": 0.9,
    },

    # ----- Aritmetika limit: 15 výpočtových úloh -----
    # Pro `latex_expr` MathLive Compute Engine porovná student vs. correct_answer
    # přes `.isSame()` (symbolicky) nebo `.N()` (numericky s tolerancí).
    {
        "task_id": "cv04_lim_01",
        "content_latex": r"\lim_{x \to 3} \frac{5x^2 - 8x - 13}{x^2 - 5}",
        "result_type": "decimal", "correct_answer": 2.0, "tolerance": 0.001,
        "cognitive_load": "B", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": -1.8, "irt_discrimination": 0.9,
    },
    {
        "task_id": "cv04_lim_02",
        "content_latex": r"\lim_{x \to 2} \frac{3x^2 - x - 10}{x^2 - 4}",
        "result_type": "latex_expr", "correct_answer": r"\frac{11}{4}", "tolerance": 0.0,
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": -1.0, "irt_discrimination": 1.0,
    },
    {
        "task_id": "cv04_lim_03",
        "content_latex": r"\lim_{x \to 3} \frac{x^4 - 81}{2x^2 - 5x - 3}",
        "result_type": "latex_expr", "correct_answer": r"\frac{108}{7}", "tolerance": 0.0,
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": -0.5, "irt_discrimination": 1.0,
    },
    {
        "task_id": "cv04_lim_04",
        "content_latex": r"\lim_{x \to -2} \frac{\frac{1}{x} + \frac{1}{2}}{x^3 + 8}",
        "result_type": "latex_expr", "correct_answer": r"-\frac{1}{48}", "tolerance": 0.0,
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": 0.3, "irt_discrimination": 1.1,
    },
    {
        "task_id": "cv04_lim_05",
        "content_latex": r"\lim_{x \to 2} \frac{x^3 - 2x^2 - 4x + 8}{x^4 - 8x^2 + 16}",
        "result_type": "latex_expr", "correct_answer": r"\frac{1}{4}", "tolerance": 0.0,
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": 0.6, "irt_discrimination": 1.2,
    },
    {
        "task_id": "cv04_lim_06",
        "content_latex": r"\lim_{x \to 2} \frac{x^4 - 2x^3 + 2x^2 - 5x + 2}{x - 2}",
        "result_type": "decimal", "correct_answer": 11.0, "tolerance": 0.001,
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": -0.2, "irt_discrimination": 1.1,
    },
    {
        "task_id": "cv04_lim_07",
        "content_latex": r"\lim_{x \to 4} \frac{3 - \sqrt{x + 5}}{x - 4}",
        "result_type": "latex_expr", "correct_answer": r"-\frac{1}{6}", "tolerance": 0.0,
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": 0.8, "irt_discrimination": 1.2,
    },
    {
        "task_id": "cv04_lim_08",
        "content_latex": r"\lim_{x \to -1} \frac{x^3 + 1}{\sqrt{x^2 - 3x} + 2x}",
        "result_type": "decimal", "correct_answer": 4.0, "tolerance": 0.001,
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": 1.0, "irt_discrimination": 1.3,
    },
    {
        "task_id": "cv04_lim_09",
        "content_latex": r"\lim_{x \to 0} \frac{x^3 - 7x}{x^3}",
        "result_type": "latex_expr", "correct_answer": r"-\infty", "tolerance": 0.0,
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": 0.4, "irt_discrimination": 1.1,
    },
    {
        "task_id": "cv04_lim_10",
        "content_latex": r"\lim_{x \to 0} \frac{x^2 - 1}{x^2}",
        "result_type": "latex_expr", "correct_answer": r"-\infty", "tolerance": 0.0,
        "cognitive_load": "B", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": -0.4, "irt_discrimination": 1.0,
    },
    {
        "task_id": "cv04_lim_11",
        "content_latex": r"\lim_{x \to 0} \frac{x^4 + 5x - 3}{2 - \sqrt{x^2 + 4}}",
        "result_type": "latex_expr", "correct_answer": r"+\infty", "tolerance": 0.0,
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": 1.1, "irt_discrimination": 1.2,
    },
    {
        # Limita zleva = -∞, zprava = +∞ → neexistuje. Necháme MC, aby se ověření
        # nelámalo na konvenci „dne" v MathJSON.
        "task_id": "cv04_lim_12",
        "content_latex": r"\lim_{x \to 1} \frac{x^3 - 1}{(x - 1)^2}",
        "result_type": "multiple_choice",
        "correct_answer": {
            "options": [
                {"key": "finite", "label": r"Limita existuje a má konečnou hodnotu"},
                {"key": "plus_inf", "label": r"$+\infty$"},
                {"key": "minus_inf", "label": r"$-\infty$"},
                {"key": "dne", "label": r"Limita neexistuje"},
            ],
            "correct_key": "dne",
        },
        "cognitive_load": "D",
        "graph_vector": ["Limity funkcí"],
        "irt_difficulty": 1.3, "irt_discrimination": 1.4,
    },
    {
        "task_id": "cv04_lim_13",
        "content_latex": r"\lim_{x \to +\infty} \frac{x^2 + 3x - 4}{1 - 5x^2}",
        "result_type": "latex_expr", "correct_answer": r"-\frac{1}{5}", "tolerance": 0.0,
        "cognitive_load": "B", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": -0.6, "irt_discrimination": 1.0,
    },
    {
        "task_id": "cv04_lim_14",
        "content_latex": r"\lim_{x \to +\infty} \frac{2x^2 + 7x - 2}{6x^3 - 4x + 3}",
        "result_type": "decimal", "correct_answer": 0.0, "tolerance": 0.001,
        "cognitive_load": "B", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": -0.7, "irt_discrimination": 1.0,
    },
    {
        "task_id": "cv04_lim_15",
        "content_latex": r"\lim_{x \to -\infty} \frac{(1 - 2x)^2 (3 - x)}{x^2 - 7x + 10}",
        "result_type": "latex_expr", "correct_answer": r"+\infty", "tolerance": 0.0,
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
        "irt_difficulty": 0.5, "irt_discrimination": 1.1,
    },
]


def _build_cv04_tasks():
    """Vrátí list MathTask instancí pro cvičení 4 (limity funkcí)."""
    return [MathTask(**spec) for spec in _CV04_TASKS]


def seed_database():
    print("🌱 Spouštím plnění databáze rozšířenými demo daty pro výzkumný tým...")
    SessionLocal = init_db(DB_URL)
    session = SessionLocal()

    try:
        # Vyčištění předchozích dat pro čisté demo
        session.query(InteractionLog).delete()
        session.query(Student).delete()
        session.query(MathTask).delete()
        session.commit()
        print("🗑️ Stará data byla vymazána.")

        # 1. Vytvoření testovacího studenta s plným profilem (20 domén)
        initial_profile = {
            "Základní aritmetické operace": 0.85,
            "Zlomky a desetinná čísla": 0.60,
            "Mocniny a odmocniny": 0.45,
            "Základní algebraické výrazy": 0.30,
            "Lineární rovnice": 0.25,
            "Kvadratické rovnice": 0.15,
            "Soustavy rovnic": 0.10,
            "Planimetrie": 0.50,
            "Stereometrie": 0.20,
            "Goniometrie": 0.10,
            "Analytická geometrie": 0.10,
            "Komplexní čísla": 0.10,
            "Posloupnosti a řady": 0.10,
            "Kombinatorika": 0.35,
            "Pravděpodobnost": 0.20,
            "Statistika": 0.40,
            "Limity funkcí": 0.10,  # Student s limity začíná, umí je jen na 10 %
            "Derivace": 0.10,
            "Integrály": 0.10,
            "Matice a determinanty": 0.10,
            "Negace výroků": 0.30
        }

        student = Student(
            student_id="student_1",
            learning_style="visual",
            motivation="intrinsic",
            math_anxiety="low",
            personality_traits="INTJ",
            cognitive_profile=initial_profile
        )
        session.add(student)
        print("✅ Student 'student_1' byl úspěšně vytvořen s 20 doménami.")

        # 2. Vytvoření rozšířené sady 9 úloh pro adaptivní výběr (Kategorie: Limity funkcí)
        tasks = []

        # Úroveň 1: Velmi lehká (Pouhé dosazení)
        tasks.append(MathTask(
            task_id="lim_01_v_easy",
            content_latex=r"\lim_{x \to 2} (x + 3)",
            result_type="decimal", correct_answer=5.0, tolerance=0.01,
            cognitive_load="A", graph_vector=["Limity funkcí"],
            irt_difficulty=-2.5, irt_discrimination=0.8
        ))

        # Úroveň 2: Lehká (Základní lineární výraz)
        tasks.append(MathTask(
            task_id="lim_02_easy",
            content_latex=r"\lim_{x \to 3} (2x - 1)",
            result_type="decimal", correct_answer=5.0, tolerance=0.01,
            cognitive_load="A", graph_vector=["Limity funkcí"],
            irt_difficulty=-1.5, irt_discrimination=0.9
        ))

        # Úroveň 3: Lehce podprůměrná (Dosazení do zlomku bez nuly ve jmenovateli)
        tasks.append(MathTask(
            task_id="lim_03_med_easy",
            content_latex=r"\lim_{x \to 1} \frac{x + 3}{x + 1}",
            result_type="decimal", correct_answer=2.0, tolerance=0.01,
            cognitive_load="B", graph_vector=["Limity funkcí"],
            irt_difficulty=-0.8, irt_discrimination=1.0
        ))

        # Úroveň 4: Střední (Jednoduché krácení polynomu)
        tasks.append(MathTask(
            task_id="lim_04_medium",
            content_latex=r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2}",
            result_type="decimal", correct_answer=4.0, tolerance=0.01,
            cognitive_load="C", graph_vector=["Limity funkcí"],
            irt_difficulty=0.0, irt_discrimination=1.2
        ))

        # Úroveň 5: Středně těžká (Tabulková limita sin(x)/x)
        tasks.append(MathTask(
            task_id="lim_05_med_hard",
            content_latex=r"\lim_{x \to 0} \frac{\sin(x)}{x}",
            result_type="decimal", correct_answer=1.0, tolerance=0.01,
            cognitive_load="C", graph_vector=["Limity funkcí"],
            irt_difficulty=0.5, irt_discrimination=1.3
        ))

        # Úroveň 6: Těžší (Krácení polynomu 2. stupně / rozklad na součin)
        tasks.append(MathTask(
            task_id="lim_06_hard_1",
            content_latex=r"\lim_{x \to 1} \frac{x^2 + x - 2}{x - 1}",
            result_type="decimal", correct_answer=3.0, tolerance=0.01,
            cognitive_load="D", graph_vector=["Limity funkcí"],
            irt_difficulty=1.2, irt_discrimination=1.1
        ))

        # Úroveň 7: Těžká (L'Hospitalovo pravidlo nebo goniometrická úprava)
        tasks.append(MathTask(
            task_id="lim_07_hard_2",
            content_latex=r"\lim_{x \to 0} \frac{1 - \cos(x)}{x^2}",
            result_type="decimal", correct_answer=0.5, tolerance=0.01,
            cognitive_load="E", graph_vector=["Limity funkcí"],
            irt_difficulty=1.8, irt_discrimination=1.4
        ))

        # Úroveň 8: Velmi těžká (L'Hospital e^x)
        tasks.append(MathTask(
            task_id="lim_08_v_hard",
            content_latex=r"\lim_{x \to 0} \frac{e^x - 1}{x}",
            result_type="decimal", correct_answer=1.0, tolerance=0.01,
            cognitive_load="E", graph_vector=["Limity funkcí"],
            irt_difficulty=2.2, irt_discrimination=1.5
        ))

        # Úroveň 9: Extrémní (Definice Eulerova čísla)
        tasks.append(MathTask(
            task_id="lim_09_extreme",
            content_latex=r"\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x \quad \text{(zaokrouhli na 2 des. místa)}",
            result_type="decimal", correct_answer=2.72, tolerance=0.02, # tolerance mírně vyšší kvůli zaokrouhlení
            cognitive_load="F", graph_vector=["Limity funkcí"],
            irt_difficulty=2.8, irt_discrimination=1.6
        ))

        # Pilotní převod cvičení 4 ze skripta „Základy matematiky 1"
        # (3× negace výroků + 15× výpočet limity, čistý LaTeX bez vlastních maker)
        cv04_tasks = _build_cv04_tasks()
        tasks.extend(cv04_tasks)

        session.add_all(tasks)
        print(
            f"✅ Sada {len(tasks)} úloh vytvořena "
            f"({len(tasks) - len(cv04_tasks)} ukázkových limit + {len(cv04_tasks)} z cv04)."
        )

        session.commit()
        print("🎉 Databáze je kompletně naplněna a připravena pro adaptivní engine!")

    except Exception as e:
        session.rollback()
        print(f"❌ Chyba při plnění DB: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()