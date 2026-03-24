from database import init_db
from model import MathTask, Student
import json

# URL k naší běžící Docker PostgreSQL databázi
DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"

def seed_database():
    print("🌱 Spouštím plnění databáze demo daty...")
    SessionLocal = init_db(DB_URL)
    session = SessionLocal()

    try:
        # 1. Vytvoření testovacího studenta, pokud ještě neexistuje
        student = session.query(Student).filter_by(student_id="student_1").first()
        if not student:
            # Výchozí kognitivní profil (neznalost tématu)
            initial_profile = {"topic_limity": 0.1, "topic_integraly": 0.1}
            student = Student(
                student_id="student_1",
                learning_style="visual",
                motivation="intrinsic",
                math_anxiety="low",
                personality_traits="INTJ",
                cognitive_profile=initial_profile
            )
            session.add(student)
            print("✅ Student 'student_1' byl vytvořen.")

        # 2. Vytvoření testovací úlohy (Limita)
        task = session.query(MathTask).filter_by(task_id="task_calc_01").first()
        if not task:
            task = MathTask(
                task_id="task_calc_01",
                content_latex=r"\lim_{x \to 0} \frac{\sin(x)}{x}",
                result_type="decimal",
                correct_answer=1.0,  # Správná odpověď
                tolerance=0.01,
                cognitive_load="C",
                graph_vector=["topic_limity"], # Navázáno na téma limity
                irt_difficulty=0.5,
                irt_discrimination=1.2
            )
            session.add(task)
            print("✅ Úloha 'task_calc_01' byla vytvořena.")

        # Uložení změn do databáze
        session.commit()
        print("🎉 Databáze je úspěšně naplněna a připravena!")

    except Exception as e:
        session.rollback()
        print(f"❌ Chyba při plnění DB: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()