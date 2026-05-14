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


def _task_to_dict(task):
    """Serializace MathTask pro předání do template / JS."""
    return {
        "task_id": task.task_id,
        "content_latex": task.content_latex,
        "has_image": task.has_image,
        "result_type": task.result_type,
        "correct_answer": task.correct_answer,
        "tolerance": task.tolerance,
        "cognitive_load": task.cognitive_load,
        "graph_vector": task.graph_vector,
        "irt_difficulty": task.irt_difficulty,
        "irt_discrimination": task.irt_discrimination,
    }


@app.route("/inspector")
def inspector_list():
    """Seznam všech úloh v DB pro výzkumný tým (tagování, kontrola)."""
    session = SessionLocal()
    try:
        tasks = session.query(MathTask).order_by(MathTask.task_id).all()
        return render_template(
            "inspector_list.html",
            tasks=[_task_to_dict(t) for t in tasks],
        )
    finally:
        session.close()


@app.route("/inspector/<task_id>")
def inspector_detail(task_id):
    """Detail úlohy: vlastnosti, živý KaTeX náhled, MathLive vstup a Compute Engine eval."""
    session = SessionLocal()
    try:
        task = session.query(MathTask).filter_by(task_id=task_id).first()
        if not task:
            return f"Úloha {task_id} nenalezena.", 404
        return render_template("inspector_detail.html", task=_task_to_dict(task))
    finally:
        session.close()


def _neighbor_task_ids(session, task_id):
    """Vrátí (prev_id, next_id, index, total) v abecedním pořadí podle task_id."""
    ids = [row[0] for row in session.query(MathTask.task_id).order_by(MathTask.task_id).all()]
    if task_id not in ids:
        return None, None, None, len(ids)
    i = ids.index(task_id)
    prev_id = ids[i - 1] if i > 0 else None
    next_id = ids[i + 1] if i + 1 < len(ids) else None
    return prev_id, next_id, i + 1, len(ids)


@app.route("/admin/task/<task_id>", methods=["GET"])
def admin_task_get(task_id):
    """Admin editor jedné úlohy. V hlavičce navigace prev/next mezi úlohami."""
    session = SessionLocal()
    try:
        task = session.query(MathTask).filter_by(task_id=task_id).first()
        if not task:
            return f"Úloha {task_id} nenalezena.", 404
        prev_id, next_id, idx, total = _neighbor_task_ids(session, task_id)
        return render_template(
            "admin_edit.html",
            task=_task_to_dict(task),
            prev_id=prev_id,
            next_id=next_id,
            position=idx,
            total=total,
        )
    finally:
        session.close()


_EDITABLE_FIELDS = {
    "content_latex", "has_image", "result_type", "correct_answer", "tolerance",
    "cognitive_load", "graph_vector", "irt_difficulty", "irt_discrimination",
}


@app.route("/admin/task/<task_id>", methods=["POST"])
def admin_task_save(task_id):
    """Uloží editovaná pole úlohy. Tělo: JSON s libovolnou podmnožinou polí."""
    session = SessionLocal()
    try:
        task = session.query(MathTask).filter_by(task_id=task_id).first()
        if not task:
            return jsonify({"error": f"Úloha {task_id} nenalezena."}), 404

        payload = request.get_json(silent=True) or {}
        unknown = set(payload) - _EDITABLE_FIELDS
        if unknown:
            return jsonify({"error": f"Neznámá pole: {sorted(unknown)}"}), 400

        for k, v in payload.items():
            setattr(task, k, v)
        # JSON sloupce SQLAlchemy potřebují explicitní flag, jinak by se update mohl ztratit
        for k in ("correct_answer", "graph_vector"):
            if k in payload:
                flag_modified(task, k)

        session.commit()
        return jsonify({"ok": True, "task": _task_to_dict(task)})
    except Exception as e:
        session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Chyba serveru: {str(e)}"}), 500
    finally:
        session.close()


@app.route("/reset-db", methods=["POST"])
def reset_db():
    """Hard-reset databáze pro demo účely (spustí logiku ze seed_db.py)."""
    try:
        # Naimportujeme tvou existující funkci z vedlejšího souboru
        from seed_db import seed_database

        # Spustíme ji (provede výmaz DB, vytvoří studenta a nahraje všechny úlohy)
        seed_database()

        return jsonify({"message": "Databáze byla úspěšně resetována přímo ze skriptu seed_db.py."})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Chyba při resetu: {str(e)}"}), 500


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