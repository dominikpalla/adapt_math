"""
AdaptMath — Task Checker.

Minimální Flask aplikace pro kontrolu importovaných úloh:
  GET  /                        → přesměruje na první úlohu
  GET  /tasks                   → seznam všech úloh
  GET  /tasks/<task_id>         → task checker (editor + sandbox)
  POST /api/tasks/<task_id>     → uložit změny v úloze
  DELETE /api/tasks/<task_id>   → smazat úlohu

Demo s IRT/BKT engine je zatím odloženo (viz historie commitů pro starší verzi).
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from sqlalchemy.orm.attributes import flag_modified
from database import init_db
from model import MathTask

DB_URL = "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath"

app = Flask(__name__)
SessionLocal = init_db(DB_URL)


@app.after_request
def disable_cache(response):
    """V dev režimu zakážeme browser cache pro HTML — jinak změny šablon
    nedojdou bez Cmd+Shift+R."""
    if response.mimetype == "text/html":
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

EDITABLE_FIELDS = {
    "task_id", "content_latex", "results",
    "cognitive_load", "graph_vector",
    "irt_difficulty", "irt_discrimination",
}


def task_to_dict(task):
    """Serializace MathTask pro template / JSON odpověď."""
    return {
        "task_id": task.task_id,
        "content_latex": task.content_latex,
        "results": task.results,
        "cognitive_load": task.cognitive_load,
        "graph_vector": task.graph_vector,
        "irt_difficulty": task.irt_difficulty,
        "irt_discrimination": task.irt_discrimination,
    }


def neighbor_task_ids(session, task_id):
    """Vrátí (prev_id, next_id, index, total) v abecedním pořadí podle task_id."""
    ids = [row[0] for row in session.query(MathTask.task_id).order_by(MathTask.task_id).all()]
    if task_id not in ids:
        return None, None, None, len(ids)
    i = ids.index(task_id)
    prev_id = ids[i - 1] if i > 0 else None
    next_id = ids[i + 1] if i + 1 < len(ids) else None
    return prev_id, next_id, i + 1, len(ids)


# --------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------

@app.route("/")
def index():
    """Default — přesměruje na první úlohu v DB (nebo prompt na seed)."""
    session = SessionLocal()
    try:
        first = session.query(MathTask.task_id).order_by(MathTask.task_id).first()
        if first is None:
            return (
                "<h1>Databáze je prázdná.</h1>"
                "<p>Spusť <code>python seed_db.py</code> a obnov tuto stránku.</p>",
                200,
            )
        return redirect(url_for("task_checker", task_id=first[0]))
    finally:
        session.close()


@app.route("/tasks")
def tasks_list():
    """Tabulka všech úloh — odkaz na detail pro každou."""
    session = SessionLocal()
    try:
        tasks = session.query(MathTask).order_by(MathTask.task_id).all()
        return render_template(
            "tasks_list.html",
            tasks=[task_to_dict(t) for t in tasks],
        )
    finally:
        session.close()


@app.route("/tasks/<task_id>")
def task_checker(task_id):
    """Task checker: zadání, parametry, výsledky, MathLive sandbox."""
    session = SessionLocal()
    try:
        task = session.query(MathTask).filter_by(task_id=task_id).first()
        if not task:
            return f"Úloha <code>{task_id}</code> nenalezena. <a href='/tasks'>Zpět na seznam</a>.", 404
        prev_id, next_id, idx, total = neighbor_task_ids(session, task_id)
        return render_template(
            "task_checker.html",
            task=task_to_dict(task),
            prev_id=prev_id,
            next_id=next_id,
            position=idx,
            total=total,
        )
    finally:
        session.close()


@app.route("/api/tasks/<task_id>", methods=["POST"])
def api_task_save(task_id):
    """Uloží editovaná pole úlohy. Tělo: JSON s libovolnou podmnožinou polí.
    Pokud se mění task_id, vrátí nové URL pro redirect na frontendu."""
    session = SessionLocal()
    try:
        task = session.query(MathTask).filter_by(task_id=task_id).first()
        if not task:
            return jsonify({"error": f"Úloha {task_id} nenalezena."}), 404

        payload = request.get_json(silent=True) or {}
        unknown = set(payload) - EDITABLE_FIELDS
        if unknown:
            return jsonify({"error": f"Neznámá pole: {sorted(unknown)}"}), 400

        new_id = payload.get("task_id")
        renamed = new_id and new_id != task.task_id
        if renamed:
            # Kolize?
            if session.query(MathTask).filter_by(task_id=new_id).first():
                return jsonify({"error": f"task_id '{new_id}' už existuje."}), 409

        for k, v in payload.items():
            setattr(task, k, v)
        for k in ("results", "graph_vector"):
            if k in payload:
                flag_modified(task, k)

        session.commit()
        return jsonify({
            "ok": True,
            "task": task_to_dict(task),
            "renamed_to": new_id if renamed else None,
        })
    except Exception as e:
        session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Chyba serveru: {e}"}), 500
    finally:
        session.close()


@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def api_task_delete(task_id):
    """Smaže úlohu."""
    session = SessionLocal()
    try:
        task = session.query(MathTask).filter_by(task_id=task_id).first()
        if not task:
            return jsonify({"error": f"Úloha {task_id} nenalezena."}), 404
        session.delete(task)
        session.commit()
        return jsonify({"ok": True})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


if __name__ == "__main__":
    print("🚀 AdaptMath Task Checker běží na http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
