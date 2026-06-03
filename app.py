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

import os
import secrets
from functools import wraps
from datetime import timedelta

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from werkzeug.middleware.proxy_fix import ProxyFix
from sqlalchemy.orm.attributes import flag_modified
from database import init_db
from model import MathTask
from tasks.knowledge_weights import (
    KNOWLEDGE_WEIGHTS,
    TASK_CATEGORIES,
    TASK_PROPERTIES,
    TASK_TYPES,
    TASK_SKILLS,
    WEIGHT_GROUPS,
    GROUP_LABELS,
)

# DB připojení. Pro produkci preferujeme DATABASE_URL env var (např. v systemd
# unit `Environment="DATABASE_URL=postgresql://..."`); lokálně padá zpět na
# výchozí dev hodnotu.
DB_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath",
)

app = Flask(__name__)

# Reverse-proxy podpora (Apache, Nginx). Pokud aplikace běží za reverzní
# proxy s sub-cestou (např. https://moodlefim.uhk.cz/adaptmath/), Apache
# odřízne /adaptmath/ z URL a pošle X-Forwarded-Prefix; ProxyFix prepne
# WSGI environ tak, aby url_for() generoval URL s prefixem.
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# --- Jednoduchá password ochrana (session-based) -----------------------------
# Heslo se zadává přes /login formulář; po úspěchu se uloží do session,
# která žije max APP_SESSION_DAYS dní. Heslo i SECRET_KEY jsou env-driven.
APP_PASSWORD = os.environ.get("APP_PASSWORD", "kikmjenejlepsi")
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)
app.permanent_session_lifetime = timedelta(days=int(os.environ.get("APP_SESSION_DAYS", "30")))


def require_login(view):
    """Decorator: pokud uživatel není přihlášený, přesměruj na /login.

    Do `next` parametru ukládáme **plnou** URL včetně reverse-proxy prefixu
    (request.script_root). Jinak by Flask po loginu vrátil redirect Location
    bez prefixu a browser by skončil mimo aplikaci (např. /tasks/... → Moodle).
    """
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("logged_in"):
            target = (request.script_root or "") + request.full_path.rstrip("?")
            return redirect(url_for("login", next=target))
        return view(*args, **kwargs)
    return wrapped


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
    "cognitive_load", "category",
    "properties", "task_type", "skills",
    "knowledge_vector",
    "graph_vector",  # ponecháno pro kompatibilitu, UI ho už needituje
    "irt_difficulty", "irt_discrimination",
}


def task_to_dict(task):
    """Serializace MathTask pro template / JSON odpověď.

    POZOR: u JSON polí (`properties`, `task_type`, `skills`) **schválně**
    NEMAPUJEME ``None`` na ``[]``. Frontend potřebuje rozlišit:
      - DB hodnota `NULL` (úloha ještě nebyla anotována) → frontend smí
        předvyplnit ze sticky storage;
      - DB hodnota `[]` (uživatel kdysi anotoval prázdně, vědomě) →
        frontend NESMÍ přepsat ze sticky.
    """
    return {
        "task_id": task.task_id,
        "content_latex": task.content_latex,
        "results": task.results,
        "cognitive_load": task.cognitive_load,
        "category": task.category,
        "properties": task.properties,   # může být None
        "task_type": task.task_type,     # může být None
        "skills": task.skills,           # může být None
        "knowledge_vector": task.knowledge_vector or {},
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

@app.route("/login", methods=["GET", "POST"])
def login():
    """Jednoduchá password ochrana — heslo se ověří proti APP_PASSWORD env var.
    Při úspěchu se uloží `logged_in=True` do session a uživatel se přesměruje
    na požadovanou stránku (parametr `next` nebo `/`)."""
    error = None
    if request.method == "POST":
        if request.form.get("password") == APP_PASSWORD:
            session["logged_in"] = True
            session.permanent = True
            next_url = request.args.get("next") or url_for("index")
            # Bezpečnostní pojistka: redirect jen na lokální URL.
            # Pokud `next` přišel bez script_root (např. stará session,
            # předchozí verze enginu), doplníme ho zde, ať redirect vede
            # na správný host (ne na Moodle).
            if not next_url.startswith("/"):
                next_url = url_for("index")
            elif request.script_root and not next_url.startswith(request.script_root + "/") \
                    and next_url != request.script_root:
                next_url = request.script_root + next_url
            return redirect(next_url)
        error = "Špatné heslo."
    return render_template("login.html", error=error)


@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


@app.route("/")
@require_login
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
@require_login
def tasks_list():
    """Tabulka všech úloh — odkaz na detail pro každou."""
    session = SessionLocal()
    try:
        tasks = session.query(MathTask).order_by(MathTask.task_id).all()
        return render_template(
            "tasks_list.html",
            tasks=[task_to_dict(t) for t in tasks],
            weight_groups=WEIGHT_GROUPS,
            group_labels=GROUP_LABELS,
            task_categories=TASK_CATEGORIES,
            task_properties=TASK_PROPERTIES,
            task_types=TASK_TYPES,
            task_skills=TASK_SKILLS,
        )
    finally:
        session.close()


@app.route("/tasks/<task_id>")
@require_login
def task_checker(task_id):
    """Task checker: zadání, parametry, výsledky, MathLive sandbox, vektor vah."""
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
            knowledge_weights=KNOWLEDGE_WEIGHTS,
            task_categories=TASK_CATEGORIES,
            task_properties=TASK_PROPERTIES,
            task_types=TASK_TYPES,
            task_skills=TASK_SKILLS,
            weight_groups=WEIGHT_GROUPS,
            group_labels=GROUP_LABELS,
        )
    finally:
        session.close()


@app.route("/api/tasks/<task_id>", methods=["POST"])
@require_login
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
        for k in ("results", "graph_vector", "knowledge_vector",
                  "properties", "task_type", "skills"):
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
@require_login
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
