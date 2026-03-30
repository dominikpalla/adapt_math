from database import init_db
from model import MathTask, Student, InteractionLog, Base
import json
import math

# URL k naší běžící Docker PostgreSQL databázi
DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"

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

        session.add_all(tasks)
        print(f"✅ Sada {len(tasks)} úloh na 'Limity funkcí' s odstupňovanou obtížností byla úspěšně vytvořena.")

        session.commit()
        print("🎉 Databáze je kompletně naplněna a připravena pro adaptivní engine!")

    except Exception as e:
        session.rollback()
        print(f"❌ Chyba při plnění DB: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()