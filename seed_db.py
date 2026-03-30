from database import init_db
from model import MathTask, Student, InteractionLog, Base
import json

# URL k naší běžící Docker PostgreSQL databázi
DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"


def seed_database():
    print("🌱 Spouštím plnění databáze demo daty pro výzkumný tým...")
    SessionLocal = init_db(DB_URL)
    session = SessionLocal()

    try:
        # Vyčištění předchozích dat pro čisté demo
        session.query(InteractionLog).delete()
        session.query(Student).delete()
        session.query(MathTask).delete()
        session.commit()
        print("🗑️ Stará data byla vymazána.")

        # 1. Vytvoření testovacího studenta s 20 kategoriemi (Open Learner Model)
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
            "Limity funkcí": 0.10,  # Výchozí znalost limit je nastavena nízko (10 %)
            "Derivace": 0.10,
            "Integrály": 0.10,
            "Matice a determinanty": 0.10
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

        # 2. Vytvoření sady úloh pro adaptivní výběr (Kategorie: Limity funkcí)

        # A) LEHKÁ ÚLOHA (Dosazení)
        task_easy = MathTask(
            task_id="task_lim_easy_01",
            content_latex=r"\lim_{x \to 3} (2x - 1)",
            result_type="decimal",
            correct_answer=5.0,
            tolerance=0.01,
            cognitive_load="A",
            graph_vector=["Limity funkcí"],
            irt_difficulty=-1.5,  # Nízká obtížnost
            irt_discrimination=0.8
        )

        # B) STŘEDNÍ ÚLOHA (Základní tabulková limita)
        task_medium = MathTask(
            task_id="task_lim_med_01",
            content_latex=r"\lim_{x \to 0} \frac{\sin(x)}{x}",
            result_type="decimal",
            correct_answer=1.0,
            tolerance=0.01,
            cognitive_load="C",
            graph_vector=["Limity funkcí"],
            irt_difficulty=0.5,  # Střední obtížnost
            irt_discrimination=1.2
        )

        # C) TĚŽKÁ ÚLOHA (L'Hospitalovo pravidlo nebo rozklad polynomu)
        task_hard = MathTask(
            task_id="task_lim_hard_01",
            content_latex=r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2}",
            result_type="decimal",
            correct_answer=4.0,
            tolerance=0.01,
            cognitive_load="E",
            graph_vector=["Limity funkcí"],
            irt_difficulty=2.0,  # Vysoká obtížnost
            irt_discrimination=1.5
        )

        session.add_all([task_easy, task_medium, task_hard])
        print("✅ Sada 3 úloh na 'Limity funkcí' (lehká, střední, těžká) byla úspěšně vytvořena.")

        session.commit()
        print("🎉 Databáze je kompletně naplněna a připravena pro adaptivní engine!")

    except Exception as e:
        session.rollback()
        print(f"❌ Chyba při plnění DB: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_database()