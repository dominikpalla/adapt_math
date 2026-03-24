from flask import Flask, render_template, request, jsonify
from database import init_db
from model import MathTask, Student, InteractionLog

app = Flask(__name__)

# Připojení na naši Docker DB
DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"
SessionLocal = init_db(DB_URL)


@app.route("/")
def index():
    """Vykreslí UI s načtenou úlohou z databáze."""
    session = SessionLocal()
    try:
        # Pro účely dema načítáme natvrdo studenta 1 a naši limitu
        student = session.query(Student).filter_by(student_id="student_1").first()
        task = session.query(MathTask).filter_by(task_id="task_calc_01").first()

        if not student or not task:
            return "❌ Databáze není naplněna! Spusť nejprve skript seed_db.py."

        return render_template("index.html", task=task, student=student)
    finally:
        session.close()


@app.route("/evaluate", methods=["POST"])
def evaluate():
    """Přijme odpověď, vyhodnotí ji, uloží log a provede BKT update."""
    data = request.get_json()
    session = SessionLocal()

    try:
        task = session.query(MathTask).filter_by(task_id=data['task_id']).first()
        student = session.query(Student).filter_by(student_id=data['student_id']).first()

        # 1. Vyhodnocení správnosti
        is_correct = abs(float(data['student_answer']) - task.correct_answer) <= task.tolerance

        # 2. Zápis do behaviorálních dat (logů)
        log = InteractionLog(
            student_id=student.student_id,
            task_id=task.task_id,
            session_id="flask_iframe_session",
            time_spent=12.0,  # V produkci budeme měřit reálný čas na frontendu
            is_correct=is_correct,
            certainty_level=float(data['certainty']),
            used_llm_hint=data['used_hint']
        )
        session.add(log)

        # 3. Zjednodušený BKT update kognitivního profilu
        topic = task.graph_vector[0]
        current_p = student.cognitive_profile.get(topic, 0.1)

        # Výpočet odměny/trestu dle jistoty a LLM nápovědy
        alpha = 0.2 + (0.2 * float(data['certainty']))
        if data['used_hint']:
            alpha *= 0.5

        beta = 0.03 + (0.02 * float(data['certainty']))

        if is_correct:
            new_p = current_p + alpha * (1.0 - current_p)
        else:
            new_p = current_p - beta * current_p

        new_p = max(0.01, min(0.99, new_p))

        # 4. Uložení updatovaného profilu
        updated_profile = dict(student.cognitive_profile)
        updated_profile[topic] = new_p
        student.cognitive_profile = updated_profile
        session.flag_modified(student, "cognitive_profile")  # Nutné pro JSON pole v SQLAlchemy

        session.commit()

        return jsonify({
            "is_correct": is_correct,
            "correct_answer": task.correct_answer,
            "new_mastery": round(new_p * 100)
        })

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


if __name__ == "__main__":
    # Spuštění Flask serveru
    app.run(debug=True, port=5000)