import math
from flask import Flask, render_template, request, jsonify
from sqlalchemy.orm.attributes import flag_modified
from database import init_db
from model import MathTask, Student, InteractionLog
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)

# Konfigurace připojení k Docker PostgreSQL databázi
DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"
SessionLocal = init_db(DB_URL)


@app.route("/")
def index():
    """
    Úvodní stránka: Načte data studenta a adaptivně vybere první nevyřešenou úlohu.
    """
    session = SessionLocal()
    try:
        student = session.query(Student).filter_by(student_id="student_1").first()

        if not student:
            return "❌ Databáze není naplněna! Spusť nejprve skript seed_db.py."

        # Zjistíme, co už student řešil
        solved_logs = session.query(InteractionLog.task_id).filter_by(student_id=student.student_id).all()
        solved_task_ids = [log.task_id for log in solved_logs]

        # Vybereme libovolnou první nevyřešenou úlohu pro začátek dema (bezpečný dotaz na prázdné pole)
        query = session.query(MathTask)
        if solved_task_ids:
            query = query.filter(~MathTask.task_id.in_(solved_task_ids))
        task = query.first()

        # Pokud už vyřešil vše, ukážeme mu pro jistotu první úlohu v DB, ať není stránka prázdná
        if not task:
            task = session.query(MathTask).first()

        return render_template("index.html", task=task, student=student)
    except Exception as e:
        return f"❌ Chyba při načítání dat: {str(e)}"
    finally:
        session.close()


@app.route("/evaluate", methods=["POST"])
def evaluate():
    """
    API endpoint pro vyhodnocení odpovědi a ADAPTIVNÍ VÝBĚR DALŠÍ ÚLOHY.
    """
    data = request.get_json()
    session = SessionLocal()

    try:
        task = session.query(MathTask).filter_by(task_id=data['task_id']).first()
        student = session.query(Student).filter_by(student_id=data['student_id']).first()

        if not task or not student:
            return jsonify({"error": "Úloha nebo student nebyl nalezen"}), 404

        # 1. Vyhodnocení správnosti
        student_val = float(data['student_answer'])
        correct_val = float(task.correct_answer)
        is_correct = abs(student_val - correct_val) <= task.tolerance

        # 2. BKT Update
        topic = task.graph_vector[0] if task.graph_vector else "Neznámé téma"
        current_p = student.cognitive_profile.get(topic, 0.1)

        alpha = 0.2 + (0.2 * float(data['certainty']))
        if data['used_hint']:
            alpha *= 0.5

        beta = 0.03 + (0.02 * float(data['certainty']))

        if is_correct:
            new_p = current_p + alpha * (1.0 - current_p)
        else:
            new_p = current_p - beta * current_p

        new_p = max(0.01, min(0.99, new_p))
        delta = new_p - current_p

        updated_profile = dict(student.cognitive_profile)
        updated_profile[topic] = new_p

        # 3. Uložení behaviorálního logu
        log = InteractionLog(
            student_id=student.student_id,
            task_id=task.task_id,
            session_id="research_demo_session",
            time_spent=15.0,
            is_correct=is_correct,
            certainty_level=float(data['certainty']),
            used_llm_hint=data['used_hint'],
            cognitive_profile_snapshot=updated_profile,
            changed_topic=topic,
            mastery_delta=delta
        )
        session.add(log)

        # 4. Aktualizace studenta v DB a Commit
        student.cognitive_profile = updated_profile
        flag_modified(student, "cognitive_profile")
        session.commit()

        # --- 5. ADAPTIVNÍ SELEKCE DALŠÍ ÚLOHY (IRT + BKT) ---
        theta = math.log(new_p / (1.0 - new_p))

        solved_logs = session.query(InteractionLog.task_id).filter_by(student_id=student.student_id).all()
        solved_task_ids = [l.task_id for l in solved_logs]

        # Nejprve vyřadíme vyřešené úlohy pomocí databáze (bezpečně)
        query = session.query(MathTask)
        if solved_task_ids:
            query = query.filter(~MathTask.task_id.in_(solved_task_ids))
        candidate_tasks = query.all()

        # Filtrování podle JSON pole (tématu) a hledání nejlepší úlohy provedeme bezpečně v Pythonu
        valid_tasks = [t for t in candidate_tasks if t.graph_vector and topic in t.graph_vector]

        # Seřadíme úlohy podle toho, jak moc se jejich IRT obtížnost blíží schopnosti studenta (theta)
        valid_tasks.sort(key=lambda t: abs((t.irt_difficulty or 0.0) - theta))

        next_task_data = None
        if valid_tasks:
            next_task = valid_tasks[0]
            next_task_data = {
                "task_id": next_task.task_id,
                "content_latex": next_task.content_latex
            }

        # 6. Odeslání všech dat zpět na frontend
        return jsonify({
            "is_correct": is_correct,
            "correct_answer": task.correct_answer,
            "new_profile": updated_profile,
            "next_task": next_task_data
        })

    except Exception as e:
        session.rollback()
        # Vypsání chyby do konzole pro snazší případný debugging
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Chyba serveru: {str(e)}"}), 500
    finally:
        session.close()


@app.route("/get-hint", methods=["POST"])
def get_hint():
    data = request.get_json()
    prompt = (
        f"Jsi asistent v systému AdaptMath. Student řeší úlohu: {data['latex']}. "
        "Dej mu stručnou didaktickou nápovědu, jak postupovat, ale NEPROZRAZUJ výsledek."
    )
    response = gemini_model.generate_content(prompt)
    return jsonify({"hint": response.text})


@app.route("/reset-db", methods=["POST"])
def reset_db():
    """Hard-reset databáze pro demo účely (vytvoří 3 úlohy a plný OLM profil)."""
    session = SessionLocal()
    try:
        session.query(InteractionLog).delete()
        session.query(Student).delete()
        session.query(MathTask).delete()

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
            "Limity funkcí": 0.10,
            "Derivace": 0.10,
            "Integrály": 0.10,
            "Matice a determinanty": 0.10
        }

        student = Student(
            student_id="student_1", learning_style="visual",
            motivation="intrinsic", cognitive_profile=initial_profile
        )
        session.add(student)

        task_easy = MathTask(
            task_id="task_lim_easy_01", content_latex=r"\lim_{x \to 3} (2x - 1)",
            result_type="decimal", correct_answer=5.0, tolerance=0.01,
            graph_vector=["Limity funkcí"], irt_difficulty=-1.5, irt_discrimination=0.8
        )
        task_medium = MathTask(
            task_id="task_lim_med_01", content_latex=r"\lim_{x \to 0} \frac{\sin(x)}{x}",
            result_type="decimal", correct_answer=1.0, tolerance=0.01,
            graph_vector=["Limity funkcí"], irt_difficulty=0.5, irt_discrimination=1.2
        )
        task_hard = MathTask(
            task_id="task_lim_hard_01", content_latex=r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2}",
            result_type="decimal", correct_answer=4.0, tolerance=0.01,
            graph_vector=["Limity funkcí"], irt_difficulty=2.0, irt_discrimination=1.5
        )

        session.add_all([task_easy, task_medium, task_hard])
        session.commit()
        return jsonify(
            {"message": "Databáze byla úspěšně resetována (Nahrány 3 adaptivní úlohy a obnoven plný profil studenta)."})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route("/get-logs", methods=["GET"])
def get_logs():
    """Vrátí všechny interakce seřazené od nejnovější pro tabulku logů."""
    session = SessionLocal()
    try:
        logs = session.query(InteractionLog).order_by(InteractionLog.timestamp.desc()).all()
        return jsonify([{
            "id": l.log_id,
            "task": l.task_id,
            "correct": l.is_correct,
            "certainty": l.certainty_level,
            "hint": l.used_llm_hint,
            "time": l.time_spent,
            "changed_topic": l.changed_topic,
            "mastery_delta": l.mastery_delta
        } for l in logs])
    finally:
        session.close()


if __name__ == "__main__":
    print("🚀 AdaptMath Engine běží na http://127.0.0.1:5000")
    app.run(debug=True, port=5000)