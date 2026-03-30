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
    2. Vypočítá BKT update kognitivního profilu.
    3. Zapíše behaviorální log (InteractionLog) včetně výzkumného JSON snapshotu a delty.
    4. Aktualizuje profil studenta v databázi.
    5. Vrací nový stav profilu pro Open Learner Model (OLM).
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

        # 2. Adaptivní logika: Bayesian Knowledge Tracing (BKT) Update
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

        # Výpočet změny pro frontend a uložení do logu
        delta = new_p - current_p

        # Vytvoření zaktualizovaného kognitivního profilu (JSON pole)
        # Vytvoříme kopii, abychom neměnili originál před commitem
        updated_profile = dict(student.cognitive_profile)
        updated_profile[topic] = new_p

        # 3. Záznam interakce (Behaviorální data pro budoucí IRT kalibraci a výzkum)
        log = InteractionLog(
            student_id=student.student_id,
            task_id=task.task_id,
            session_id="research_demo_session",
            time_spent=15.0,  # Simulovaný čas řešení
            is_correct=is_correct,
            certainty_level=float(data['certainty']),
            used_llm_hint=data['used_hint'],
            cognitive_profile_snapshot=updated_profile,  # Uložení celého JSONu po interakci
            changed_topic=topic,  # Uložení zasaženého tématu
            mastery_delta=delta  # Uložení změny v procentních bodech
        )
        session.add(log)

        # 4. Aktualizace kognitivního profilu studenta v DB
        student.cognitive_profile = updated_profile

        # Oznámíme SQLAlchemy změnu v JSON struktuře
        flag_modified(student, "cognitive_profile")

        session.commit()

        # 5. Odeslání výsledků zpět na frontend
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
    """Hard-reset databáze: Smaže vše a nahraje výchozí seed data."""
    session = SessionLocal()
    try:
        # Smazání dat v pořadí, které neporuší integritu (cizí klíče)
        session.query(InteractionLog).delete()
        session.query(Student).delete()
        session.query(MathTask).delete()

        # Znovunahrání výchozího studenta a úlohy
        initial_profile = {
            "Aritmetika": 0.85, "Zlomky": 0.60, "Mocniny": 0.45, "Algebra": 0.30,
            "Lin_rovnice": 0.25, "Kvad_rovnice": 0.15, "Soustavy": 0.10,
            "Planimetrie": 0.50, "Stereometrie": 0.20, "Goniometrie": 0.10,
            "Analytika": 0.10, "Komplex_cisla": 0.10, "Posloupnosti": 0.10,
            "Kombinatorika": 0.35, "Pravdepodobnost": 0.20, "Statistika": 0.40,
            "Limity": 0.10, "Derivace": 0.10, "Integraly": 0.10, "Matice": 0.10
        }
        student = Student(
            student_id="student_1", learning_style="vizuální",
            motivation="vnitřní", cognitive_profile=initial_profile
        )
        task = MathTask(
            task_id="task_calc_01", content_latex=r"\lim_{x \to 0} \frac{\sin(x)}{x}",
            result_type="decimal", correct_answer=1.0, tolerance=0.01,
            graph_vector=["Limity"]
        )
        session.add(student)
        session.add(task)
        session.commit()
        return jsonify({"message": "Databáze byla úspěšně resetována."})
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
            "changed_topic": l.changed_topic,  # Nově odesíláme na frontend zasažené téma
            "mastery_delta": l.mastery_delta  # Nově odesíláme na frontend změnu
        } for l in logs])
    finally:
        session.close()


if __name__ == "__main__":
    print("🚀 AdaptMath Engine běží na http://127.0.0.1:5000")
    app.run(debug=True, port=5000)