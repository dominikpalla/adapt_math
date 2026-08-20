"""
Batch fix pro 112 text-answer úloh — 4 kategorie ošetřené různou logikou.

Bezpečnostní zábradlí:
  - Idempotentní: při druhém spuštění nic neudělá (kontroluje aktuální stav).
  - Přeskočí úlohy, které už mají multiple_choice nebo víc než 1 key.
  - Kontroluje, že expected pořád matches očekávanému text patternu.
  - Dry-run mode default, --commit pro zápis.

Kategorie:
  1. PURE_MATH (~82) — expected je math bez $...$ obalu → wrap $..$ + expand \\Ra/\\R.
  2. PURE_TEXT (11) — čistý text → multiple_choice s hardcoded distraktory (níže).
  3. MIXED (4) — text + math → multiple_choice.
  4. COMPOUND (15) — víc math bloků → split na keys, nebo MC pro edge cases.

Volání:
    DATABASE_URL=... python scripts/fix_text_answers_batch.py                   # dry-run
    DATABASE_URL=... python scripts/fix_text_answers_batch.py --commit
    DATABASE_URL=... python scripts/fix_text_answers_batch.py --commit --only-cat PURE_MATH
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy.orm.attributes import flag_modified

from database import init_db
from model import MathTask


# =============================================================================
# 1) PURE_MATH — mechanický wrap + macro expand
# =============================================================================

def _expand_umat_macros(s: str) -> str:
    """Expand UMAT-specific macros KaTeX nezná."""
    if not isinstance(s, str) or not s:
        return s
    s = re.sub(r"\\Ra\b",  r"\\Rightarrow", s)
    s = re.sub(r"\\R\b",   r"\\mathbb{R}", s)
    return s


def fix_pure_math(exp: str) -> str:
    """Wrap do $...$ pokud ne (a expand macros)."""
    e = _expand_umat_macros(exp.strip())
    if e.startswith("$") and e.endswith("$"):
        return e
    return f"${e}$"


# =============================================================================
# 2) PURE_TEXT — hardcoded MC options
# =============================================================================

PURE_TEXT_MC = {
    "e01_11": {  # negace A ∨ B
        "options": [
            ("a", "Na oslavu nepřijde ani Karel ani Eliška."),
            ("b", "Na oslavu nepřijde Karel nebo nepřijde Eliška."),
            ("c", "Karel i Eliška přijdou na oslavu."),
            ("d", "Není pravda, že Karel a Eliška přijdou na oslavu."),
        ],
        "correct": "a",
    },
    "e01_12": {  # negace A ⇒ B = A ∧ ¬B
        "options": [
            ("a", "Máme chuť a nejdeme na pivo."),
            ("b", "Nemáme chuť a jdeme na pivo."),
            ("c", "Když nemáme chuť, nejdeme na pivo."),
            ("d", "Jdeme na pivo, i když nemáme chuť."),
        ],
        "correct": "a",
    },
    "e01_13": {  # negace ∀x P(x) = ∃x ¬P(x)
        "options": [
            ("a", "Existuje Edudand, který nemá Francimora."),
            ("b", "Žádný Edudand nemá Francimora."),
            ("c", "Každý Edudand nemá Francimora."),
            ("d", "Existuje Edudand, který má alespoň jednoho Francimora."),
        ],
        "correct": "a",
    },
    "e01_15": {
        "options": [
            ("a", "Existují tři body v rovině, které neleží na jedné přímce."),
            ("b", "Žádné tři body v rovině neleží na jedné přímce."),
            ("c", "Každé tři body v rovině neleží na jedné přímce."),
            ("d", "Neexistují tři body v rovině."),
        ],
        "correct": "a",
    },
    # 6 úloh "prostá, důkaz sporem"
    "e04_07": {
        "options": [
            ("a", "Prostá; lze dokázat sporem"),
            ("b", "Není prostá; existují dvě různá $x$ se stejnou funkční hodnotou"),
            ("c", "Prostá jen pro $x \\ge 0$"),
            ("d", "O prostotě nelze rozhodnout bez dalších informací"),
        ],
        "correct": "a",
    },
    "e04_09": {
        "options": [
            ("a", "Prostá; lze dokázat sporem"),
            ("b", "Není prostá; obor hodnot má opakující se hodnoty"),
            ("c", "Prostá jen pro $x \\ge 0$"),
            ("d", "Prostá jen na omezeném intervalu"),
        ],
        "correct": "a",
    },
    "e04_11": {
        "options": [
            ("a", "Prostá; lze dokázat sporem"),
            ("b", "Není prostá; má symetrii kolem osy $x = 1$"),
            ("c", "Prostá jen pro $x < 1$"),
            ("d", "Prostota závisí na volbě definičního oboru"),
        ],
        "correct": "a",
    },
    "e04_12": {
        "options": [
            ("a", "Prostá; lze dokázat sporem"),
            ("b", "Není prostá; např. $f(2) = f(-2)$"),
            ("c", "Prostá jen na $\\mathbb{R} \\setminus \\{1\\}$"),
            ("d", "Prostota není definována pro racionální funkce"),
        ],
        "correct": "a",
    },
    "e04_13": {
        "options": [
            ("a", "Prostá; lze dokázat sporem"),
            ("b", "Není prostá; má maximum"),
            ("c", "Prostá jen pro $x > 0$"),
            ("d", "Prostota nelze určit"),
        ],
        "correct": "a",
    },
    "e04_17": {
        "options": [
            ("a", "Prostá; lze dokázat sporem"),
            ("b", "Není prostá; má asymptotu"),
            ("c", "Prostá jen na $\\mathbb{R} \\setminus \\{-1\\}$"),
            ("d", "Prostota není definována pro racionální funkce"),
        ],
        "correct": "a",
    },
    "umat_08_35": {  # lim s odmocninou z -x → neex
        "options": [
            ("a", "Limita neexistuje"),
            ("b", "$0$"),
            ("c", "$-1$"),
            ("d", "$\\frac{1}{2}$"),
        ],
        "correct": "a",
    },
}


# =============================================================================
# 3) MIXED_TEXT_MATH — MC options
# =============================================================================

MIXED_MC = {
    "e04_08": {  # y = x^3+x^2-1 není prostá, f(0)=f(-1)=-1
        "options": [
            ("a", "Není prostá; např. $f(0) = f(-1) = -1$"),
            ("b", "Prostá; lze dokázat sporem"),
            ("c", "Prostá jen pro $x > 0$"),
            ("d", "Prostota nelze určit"),
        ],
        "correct": "a",
    },
    "e04_10": {  # y = x^4 - 2x^2
        "options": [
            ("a", "Není prostá; např. $f(\\sqrt{2}) = f(-\\sqrt{2}) = 0$"),
            ("b", "Prostá; lze dokázat sporem"),
            ("c", "Prostá jen pro $x > 0$"),
            ("d", "Prostá jen pro $|x| > \\sqrt{2}$"),
        ],
        "correct": "a",
    },
    "e04_14": {  # y = x^3 - 4x + 5
        "options": [
            ("a", "Není prostá; např. $f(\\sqrt{2}) = f(-\\sqrt{2}) = 5$"),
            ("b", "Prostá; lze dokázat sporem"),
            ("c", "Prostá jen na intervalech monotonie"),
            ("d", "Prostota není definována pro polynomy"),
        ],
        "correct": "a",
    },
    "e10_02": {  # obdélník s min. obvodem při daném obsahu → čtverec 4 cm
        "options": [
            ("a", "Čtverec se stranou $a = 4$ cm"),
            ("b", "Obdélník $a = 8$ cm, $b = 2$ cm"),
            ("c", "Obdélník $a = 16$ cm, $b = 1$ cm"),
            ("d", "Čtverec se stranou $a = 2$ cm"),
        ],
        "correct": "a",
    },
}


# =============================================================================
# 4) COMPOUND — split na keys, nebo MC pro edge cases
# =============================================================================

def compound_split(task_id, exp):
    """Ručně navržený split podle patternu jednotlivých úloh."""
    handlers = {
        # e04_15, 16, 18: "není prostá, např. $f(x)=f(y)=z$" → MC
        "e04_15": lambda: mc_from_options([
            ("a", "Není prostá; např. $f(1) = f(-1) = 3$"),
            ("b", "Prostá; lze dokázat sporem"),
            ("c", "Prostá jen pro $x > 0$"),
            ("d", "Prostota není definována pro odmocniny"),
        ], "a"),
        "e04_16": lambda: mc_from_options([
            ("a", "Není prostá; např. $f(1) = f(-4) = -\\frac{1}{3}$"),
            ("b", "Prostá; lze dokázat sporem"),
            ("c", "Prostá na $\\mathbb{R} \\setminus \\{\\pm 2\\}$"),
            ("d", "Prostota nelze určit"),
        ], "a"),
        "e04_18": lambda: mc_from_options([
            ("a", "Není prostá; např. $f(0) = f(1) = 0$"),
            ("b", "Prostá na $[0, 1]$"),
            ("c", "Prostá; lze dokázat sporem"),
            ("d", "Prostota není definována pro odmocniny"),
        ], "a"),
        # e10_06: bazén — a=4m, v=2m → split 2 keys
        "e10_06": lambda: [
            {"key": "a", "label_latex": r"a = ", "type": "mathlive",
             "expected": r"4\ \text{m}", "tolerance": 0.0},
            {"key": "v", "label_latex": r"v = ", "type": "mathlive",
             "expected": r"2\ \text{m}", "tolerance": 0.0},
        ],
        # e10_07: rovnostranný trojúhelník → MC
        "e10_07": lambda: mc_from_options([
            ("a", "Rovnostranný trojúhelník se stranou $a = \\frac{o}{3}$"),
            ("b", "Rovnoramenný trojúhelník s poměrem stran $2:1$"),
            ("c", "Pravoúhlý trojúhelník s odvěsnou $a = \\frac{o}{4}$"),
            ("d", "Trojúhelník s minimálním obsahem neexistuje"),
        ], "a"),
        # e10_08: a=b=10√2 → 2 keys se stejnou hodnotou
        "e10_08": lambda: [
            {"key": "a", "label_latex": r"a = ", "type": "mathlive",
             "expected": r"10\sqrt{2}\ \text{m}", "tolerance": 0.0},
            {"key": "b", "label_latex": r"b = ", "type": "mathlive",
             "expected": r"10\sqrt{2}\ \text{m}", "tolerance": 0.0},
        ],
        # umat_07_02: "k=7, s_8=4066,3467" — desetinná čárka
        "umat_07_02": lambda: [
            {"key": "k",   "label_latex": r"k = ",   "type": "decimal",
             "expected": 7,          "tolerance": 0},
            {"key": "s_8", "label_latex": r"s_8 = ", "type": "decimal",
             "expected": 4066.3467,  "tolerance": 0.001},
        ],
        # umat_07_12: a_1=64, q=1/4
        "umat_07_12": lambda: [
            {"key": "a_1", "label_latex": r"a_1 = ", "type": "decimal",
             "expected": 64,   "tolerance": 0},
            {"key": "q",   "label_latex": r"q = ",   "type": "mathlive",
             "expected": r"\frac{1}{4}", "tolerance": 0.0},
        ],
        # umat_07_13: 2 řešení GP → MC (výběr správné dvojice)
        "umat_07_13": lambda: mc_from_options([
            ("a", "$a_1 = 3,\\ q = 2$ nebo $a_1 = -3072,\\ q = \\frac{1}{2}$"),
            ("b", "$a_1 = 3,\\ q = 2$ (jediné řešení)"),
            ("c", "$a_1 = 6,\\ q = 3$ nebo $a_1 = -1024,\\ q = 1$"),
            ("d", "Úloha nemá řešení v reálných číslech"),
        ], "a"),
        # umat_07_14: a_1=5, q=2
        "umat_07_14": lambda: [
            {"key": "a_1", "label_latex": r"a_1 = ", "type": "decimal",
             "expected": 5, "tolerance": 0},
            {"key": "q",   "label_latex": r"q = ",   "type": "decimal",
             "expected": 2, "tolerance": 0},
        ],
        # e03_35 (megablok) — přeskočit, potřebuje ruční review
        # e04_32, 33, 34, 37 (inverse funkce) — už opraveno dřív, přeskočit
    }
    handler = handlers.get(task_id)
    return handler() if handler else None


def mc_from_options(options, correct):
    return [{
        "key": "vysledek",
        "label_latex": r"\text{Odpověď: }",
        "type": "multiple_choice",
        "options": [{"key": k, "label_latex": v} for k, v in options],
        "expected": correct,
    }]


# =============================================================================
# 5) Klasifikace + orchestrace
# =============================================================================

def classify(exp: str) -> str:
    s = exp.strip()
    math_chars = re.search(r'[=<>\\^_{}\[\]$]', s)
    if not math_chars: return 'PURE_TEXT'
    dollar_blocks = s.count('$')
    if dollar_blocks >= 4 or (s.count('=') >= 2 and ',' in s): return 'COMPOUND'
    plain = re.sub(r'\$[^$]*\$', '', s)
    plain = re.sub(r'\\[a-zA-Z]+', '', plain)
    words = re.findall(r'[a-zA-Zá-žÁ-Ž]{4,}', plain)
    if len(words) >= 2: return 'MIXED_TEXT_MATH'
    return 'PURE_MATH'


def process_task(t, only_cat=None):
    """Vrátí (new_results, category, note) nebo None (skip)."""
    if not isinstance(t.results, list) or len(t.results) != 1:
        return None, None, "not 1 key (skip)"
    r = t.results[0]
    if not isinstance(r, dict) or r.get("type") == "multiple_choice":
        return None, None, "already MC (skip)"
    exp = r.get("expected", "")
    if not isinstance(exp, str): return None, None, "expected not str"

    cat = classify(exp)
    if only_cat and cat != only_cat:
        return None, cat, f"filtered out (only-cat={only_cat})"

    if cat == "PURE_MATH":
        new_exp = fix_pure_math(exp)
        new_r = dict(r)
        new_r["expected"] = new_exp
        return [new_r], cat, "wrap $..$ + expand"

    if cat == "PURE_TEXT":
        mc = PURE_TEXT_MC.get(t.task_id)
        if not mc: return None, cat, "no PURE_TEXT MC for this task"
        return mc_from_options(mc["options"], mc["correct"]), cat, "MC"

    if cat == "MIXED_TEXT_MATH":
        mc = MIXED_MC.get(t.task_id)
        if not mc: return None, cat, "no MIXED MC for this task"
        return mc_from_options(mc["options"], mc["correct"]), cat, "MC"

    if cat == "COMPOUND":
        new_results = compound_split(t.task_id, exp)
        if not new_results: return None, cat, "no compound handler (skip)"
        return new_results, cat, "split/MC"

    return None, cat, "unknown"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    p.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    p.add_argument("--only-cat", choices=["PURE_MATH", "PURE_TEXT", "MIXED_TEXT_MATH", "COMPOUND"])
    args = p.parse_args()
    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr); return 2

    sess = init_db(args.db_url)()
    try:
        tasks = sess.query(MathTask).filter(
            (MathTask.task_id.like("e%")) | (MathTask.task_id.like("umat_%"))
        ).all()

        changed = 0
        skipped = 0
        by_cat = {"PURE_MATH": 0, "PURE_TEXT": 0, "MIXED_TEXT_MATH": 0, "COMPOUND": 0}
        for t in tasks:
            new_results, cat, note = process_task(t, args.only_cat)
            if new_results is None:
                skipped += 1
                continue
            by_cat[cat] += 1
            changed += 1
            if changed <= 15 or changed % 10 == 0:
                print(f"  {t.task_id} [{cat}]: {note}")
            t.results = new_results
            flag_modified(t, "results")

        print()
        print(f"Změněno: {changed} úloh")
        for cat, n in by_cat.items():
            print(f"  {cat}: {n}")
        print(f"Skipped: {skipped}")

        if args.commit:
            sess.commit()
            print("COMMIT")
        else:
            sess.rollback()
            print("DRY-RUN (pro zápis přidej --commit)")
        return 0
    except Exception as e:
        sess.rollback()
        import traceback; traceback.print_exc()
        return 4
    finally:
        sess.close()


if __name__ == "__main__":
    sys.exit(main())
