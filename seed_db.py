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
        # Vyčištění předchozích dat pro čisté demo (volitelné, ale doporučené pro opakované testování)
        session.query(InteractionLog).delete()
        session.query(Student).delete()
        session.query(MathTask).delete()
        session.commit()
        print("🗑️ Stará data byla vymazána.")

        # 1. Vytvoření testovacího studenta s 20 kategoriemi (Open Learner Model)
        # Inicializujeme různé hodnoty, aby to na webu vypadalo realisticky
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
            "Limity funkcí": 0.10,  # Zde operuje naše testovací úloha
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

        # 2. Vytvoření testovací úlohy
        task = MathTask(
            task_id="task_calc_01",
            content_latex=r"\lim_{x \to 0} \frac{\sin(x)}{x}",
            result_type="decimal",
            correct_answer=1.0,
            tolerance=0.01,
            cognitive_load="C",
            graph_vector=["Limity funkcí"], # Navázáno přesně na kategorii v profilu
            irt_difficulty=0.5,
            irt_discrimination=1.2
        )
        session.add(task)
        print("✅ Úloha 'task_calc_01' byla úspěšně vytvořena.")

        session.commit()
        print("🎉 Databáze je kompletně naplněna a připravena pro demo!")

    except Exception as e:
        session.rollback()
        print(f"❌ Chyba při plnění DB: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()