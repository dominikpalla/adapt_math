from flask import Flask, render_template, request, jsonify
from sqlalchemy.orm.attributes import flag_modified  # Importováno správně nahoře
from database import init_db
from model import MathTask, Student, InteractionLog

app = Flask(__name__)

# Konfigurace připojení k Docker PostgreSQL databázi
DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"
SessionLocal = init_db(DB_URL)


@app.route("/")
def index():
    """
    Úvodní stránka: Načte data studenta a úlohy pro zobrazení v UI.
    V reálném Moodlu by se ID studenta předávalo např. v parametru URL.
    """
    session = SessionLocal()
    try:
        # Načtení demo dat vytvořených skriptem seed_db.py
        student = session.query(Student).filter_by(student_id="student_1").first()
        task = session.query(MathTask).filter_by(task_id="task_calc_01").first()

        if not student or not task:
            return "❌ Databáze není naplněna! Spusť nejprve skript seed_db.py."

        return render_template("index.html", task=task, student=student)
    except Exception as e:
        return f"❌ Chyba při načítání dat: {str(e)}"
    finally:
        session.close()


@app.route("/evaluate", methods=["POST"])
def evaluate():
    """
    API endpoint pro vyhodnocení odpovědi:
    1. Ověří výsledek proti databázi.
    2. Zapíše behaviorální log (InteractionLog).
    3. Aktualizuje kognitivní profil studenta pomocí BKT logiky.
    4. Vrací nový stav profilu pro Open Learner Model (OLM).
    """
    data = request.get_json()
    session = SessionLocal()

    try:
        # Vyhledání objektů v databázi
        task = session.query(MathTask).filter_by(task_id=data['task_id']).first()
        student = session.query(Student).filter_by(student_id=data['student_id']).first()

        if not task or not student:
            return jsonify({"error": "Úloha nebo student nebyl nalezen"}), 404

        # 1. Vyhodnocení správnosti (využíváme toleranci definovanou v modelu)
        student_val = float(data['student_answer'])
        is_correct = abs(student_val - task.correct_answer) <= task.tolerance

        # 2. Záznam interakce (Behaviorální data pro budoucí IRT kalibraci)
        log = InteractionLog(
            student_id=student.student_id,
            task_id=task.task_id,
            session_id="research_demo_session",
            time_spent=15.0,  # Simulovaný čas řešení
            is_correct=is_correct,
            certainty_level=float(data['certainty']),
            used_llm_hint=data['used_hint']
        )
        session.add(log)

        # 3. Adaptivní logika: Bayesian Knowledge Tracing (BKT) Update
        # Určíme téma, kterého se úloha týká (z grafu znalostí)
        topic = task.graph_vector[0]
        current_p = student.cognitive_profile.get(topic, 0.1)

        # Výpočet parametrů učení (alfa) a trestu (beta) na základě jistoty a nápovědy
        # Hodnoty odpovídají doporučení dr. Ševčíkové (0.1 - 0.4)
        alpha = 0.2 + (0.2 * float(data['certainty']))
        if data['used_hint']:
            alpha *= 0.5  # Snížení odměny za použití AI nápovědy

        beta = 0.03 + (0.02 * float(data['certainty']))

        # Aktualizace pravděpodobnosti znalosti (P_know)
        if is_correct:
            new_p = current_p + alpha * (1.0 - current_p)
        else:
            new_p = current_p - beta * current_p

        # Saturace (hranice 1% až 99%)
        new_p = max(0.01, min(0.99, new_p))

        # 4. Aktualizace kognitivního profilu (JSON pole)
        # Vytvoříme kopii, abychom neměnili originál před commitem
        updated_profile = dict(student.cognitive_profile)
        updated_profile[topic] = new_p
        student.cognitive_profile = updated_profile

        # Oznámíme SQLAlchemy změnu v JSON struktuře
        flag_modified(student, "cognitive_profile")

        session.commit()

        # Odeslání výsledků zpět na frontend
        return jsonify({
            "is_correct": is_correct,
            "correct_answer": task.correct_answer,
            "new_profile": updated_profile
        })

    except Exception as e:
        session.rollback()
        # Vracíme detail chyby pro snadnější debugování dema
        return jsonify({"error": f"Chyba serveru: {str(e)}"}), 500
    finally:
        session.close()


if __name__ == "__main__":
    print("🚀 AdaptMath Engine běží na http://127.0.0.1:5000")
    app.run(debug=True, port=5000)