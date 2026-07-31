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

# Přijmout jak `/tasks`, tak `/tasks/` — jinak Flask defaultně vrací 404
# pro variantu, která neodpovídá dekorátoru. Chrome/Windows některým
# uživatelům v adresním řádku doplňuje koncové lomítko, případně mají
# záložku s `/tasks/`. Musí být nastaveno před tím, než se @app.route
# dekorátory vezmou (kopírují si tuhle hodnotu do každého Rule).
app.url_map.strict_slashes = False

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

        # task_id validace — chránit před tím, aby autosave nechtěně
        # neuložil prázdný nebo whitespace-only ID (autor se stalo, viz
        # incident 2026-07-31: úloha s task_id='' šla z UI 404 a v seznamu
        # měla prázdný sloupec, ačkoli fyzicky v DB stále existovala).
        if "task_id" in payload:
            raw = payload["task_id"]
            if not isinstance(raw, str) or not raw.strip():
                return jsonify({
                    "error": "task_id nesmí být prázdné (autosave odmítnut)."
                }), 400
            payload["task_id"] = raw.strip()  # normalizovaně bez whitespace

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


@app.route("/api/tasks/bulk", methods=["POST"])
@require_login
def api_task_bulk():
    """Hromadná anotace: pro vybrané task_ids aplikuj operace na jednotlivá
    anotační pole. Vše v jedné transakci — buď všechny změny nebo žádná.

    Očekávaný payload (všechna pole `operations` jsou volitelná):
        {
          "task_ids": ["cv01_01", "cv01_02", ...],
          "operations": {
            "category":   {"mode": "always"|"only_if_null", "value": "SŠ - Rovnice"},
            "properties": {"mode": "add"|"replace"|"remove", "values": [...]},
            "task_type":  {"mode": "add"|"replace"|"remove", "values": [...]},
            "skills":     {"mode": "add"|"replace"|"remove", "values": [...]}
          }
        }

    Vrací:
        {
          "ok": true,
          "changed": <int>,   # kolik řádků reálně změněno
          "skipped": <int>,   # kolik zůstalo beze změny (např. only_if_null a už mělo hodnotu)
          "not_found": [...], # task_ids, které v DB neexistují
        }
    """
    payload = request.get_json(silent=True) or {}
    task_ids = payload.get("task_ids") or []
    ops = payload.get("operations") or {}

    if not isinstance(task_ids, list) or not task_ids:
        return jsonify({"error": "task_ids musí být neprázdné pole."}), 400
    if not isinstance(ops, dict) or not ops:
        return jsonify({"error": "operations musí obsahovat alespoň jednu operaci."}), 400

    # Validace jednotlivých operací
    if "category" in ops:
        op = ops["category"]
        if op.get("mode") not in ("always", "only_if_null"):
            return jsonify({"error": "category.mode musí být 'always' nebo 'only_if_null'."}), 400
        if not isinstance(op.get("value"), (str, type(None))):
            return jsonify({"error": "category.value musí být string nebo null."}), 400
    for field in ("properties", "task_type", "skills"):
        if field in ops:
            op = ops[field]
            if op.get("mode") not in ("add", "replace", "remove"):
                return jsonify({"error": f"{field}.mode musí být 'add', 'replace' nebo 'remove'."}), 400
            if not isinstance(op.get("values"), list):
                return jsonify({"error": f"{field}.values musí být pole."}), 400
            if not all(isinstance(v, str) for v in op["values"]):
                return jsonify({"error": f"{field}.values musí obsahovat jen stringy."}), 400

    from sqlalchemy import select
    session = SessionLocal()
    try:
        rows = session.query(MathTask).filter(MathTask.task_id.in_(task_ids)).all()
        found_ids = {r.task_id for r in rows}
        not_found = [tid for tid in task_ids if tid not in found_ids]

        changed = 0
        skipped = 0
        for task in rows:
            row_changed = False

            # 1) category (single-value string)
            if "category" in ops:
                op = ops["category"]
                new_val = op["value"] or None
                if op["mode"] == "always":
                    if task.category != new_val:
                        task.category = new_val
                        row_changed = True
                elif op["mode"] == "only_if_null":
                    # Aplikuj jen když v DB je NULL (nikoli když je prázdný string)
                    if task.category is None:
                        task.category = new_val
                        row_changed = True

            # 2) multi-select pole (properties / task_type / skills)
            for field in ("properties", "task_type", "skills"):
                if field not in ops:
                    continue
                op = ops[field]
                current = list(getattr(task, field) or [])
                new_list = list(current)
                if op["mode"] == "add":
                    for v in op["values"]:
                        if v not in new_list:
                            new_list.append(v)
                elif op["mode"] == "replace":
                    new_list = list(op["values"])
                elif op["mode"] == "remove":
                    new_list = [v for v in current if v not in op["values"]]
                if new_list != current:
                    setattr(task, field, new_list)
                    flag_modified(task, field)
                    row_changed = True

            if row_changed:
                changed += 1
            else:
                skipped += 1

        session.commit()
        return jsonify({
            "ok": True,
            "changed": changed,
            "skipped": skipped,
            "not_found": not_found,
        })
    except Exception as e:
        session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Chyba serveru: {e}"}), 500
    finally:
        session.close()


if __name__ == "__main__":
    print("🚀 AdaptMath Task Checker běží na http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
