"""
Konverze zsv_ úloh typu "Určete smysl" na multiple_choice.

Pokrývá 90 úloh:
  - "Určete hodnoty proměnné, pro které nemá výraz smysl." (typ NEMÁ, 30 úloh)
  - "Určete, kdy mají dané výrazy smysl." (typ MÁ, 60 úloh)

NENÍ pokryt typ "Určete, kdy má výraz smysl, a zjednodušte ho." (29 úloh,
dvě odpovědi — podmínky + zjednodušený výraz, nechává se jako mathlive).

Pro každou úlohu generuje 4 MC options:
  - Správná: aktuální expected (raw z \\left[\\,...\\,\\right])
  - Distraktor 1: opačná formulace (= ↔ ≠) typická chyba záměny role čit./jmen.
  - Distraktor 2: "žádné omezení (x ∈ ℝ)" nebo "neexistuje" (opak)
  - Distraktor 3: typická chybná hodnota (x = 0 u NEMÁ, extra x ≠ 0 u MÁ)

Správná odpověď rozprostřená mezi a/b/c/d (idx % 4).

Použití:
    DATABASE_URL=... python scripts/mc_zsv_smysl.py            # dry-run
    DATABASE_URL=... python scripts/mc_zsv_smysl.py --commit
"""
from __future__ import annotations
import argparse, os, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sqlalchemy.orm.attributes import flag_modified
from database import init_db
from model import MathTask


NEMA_PREFIX = "Určete hodnoty proměnné, pro které nemá výraz smysl."
MA_PREFIX = "Určete, kdy mají dané výrazy smysl."


def swap_eq_neq(s: str) -> str:
    """Zaměnit \\boldsymbol{=} ↔ \\boldsymbol{\\neq}. Používá placeholder."""
    placeholder = "@@EQ_SWAP@@"
    out = s.replace(r'\boldsymbol{=}', placeholder)
    out = out.replace(r'\boldsymbol{\neq}', r'\boldsymbol{=}')
    out = out.replace(placeholder, r'\boldsymbol{\neq}')
    return out


def pick_variable(expected: str) -> str:
    """Odhadne, kterou proměnnou úloha řeší — první samostatné malé písmeno
    v expected (vynechá písmena uvnitř \\boldsymbol, \\text, atd.)."""
    # Projdi znaky, vynech ty uvnitř \backslash command
    i = 0
    while i < len(expected):
        ch = expected[i]
        if ch == '\\':
            # přeskoč příkaz
            i += 1
            while i < len(expected) and expected[i].isalpha():
                i += 1
            continue
        if ch.isalpha() and ch.islower() and ch not in ('e',):  # e jako exp
            return ch
        i += 1
    return "x"


def build_distractors(expected: str, kind: str) -> list[str]:
    """Vrátí 3 distraktory podle typu úlohy (nema/ma)."""
    var = pick_variable(expected)
    distractors = []
    is_vsude = "\\mathbb{R}" in expected or "všude" in expected

    if kind == "nema":
        # Správná = "x = <hodnoty>" (co nulí jmenovatel). Distraktory:
        # 1) opak: "x ≠ ..." (častá záměna, student zamění role čitatele/jmenovatele)
        d1 = swap_eq_neq(expected)
        if d1 == expected:
            d1 = f"{var}\\;\\boldsymbol{{\\neq}}\\;0"
        distractors.append(d1)
        # 2) "smysl má všude" (žádná výluka)
        distractors.append(r"\text{neexistuje, smysl má všude}")
        # 3) typická špatná hypotéza: x = 0 (jen pokud není už ve správné)
        if "=0" in expected.replace(' ', '') or "= 0" in expected:
            distractors.append(f"{var}\\;\\boldsymbol{{=}}\\;{{\\pm}}1")
        else:
            distractors.append(f"{var}\\;\\boldsymbol{{=}}\\;0")

    elif kind == "ma":
        if is_vsude:
            # Správná = "x ∈ ℝ". Distraktory: ukázat typická omezení, kde student váhá.
            distractors.append(f"{var}\\;\\boldsymbol{{\\neq}}\\;0")
            distractors.append(f"{var}\\;\\boldsymbol{{\\neq}}\\;{{\\pm}}1")
            distractors.append(r"\text{výraz nemá smysl pro žádné }" + var)
        else:
            # Správná = "x ≠ ...". Distraktory:
            # 1) opak: "x = ..." (záměna role čitatele/jmenovatele)
            d1 = swap_eq_neq(expected)
            if d1 == expected:
                d1 = f"{var}\\;\\boldsymbol{{=}}\\;0"
            distractors.append(d1)
            # 2) "x ∈ ℝ" (žádná výluka)
            distractors.append(f"{var}\\;\\boldsymbol{{\\in}}\\;\\mathbb{{R}}")
            # 3) rozšířený rozsah: + x ≠ 0 (když tam ještě není)
            if re.search(r'\\neq\s*\\;?\s*0', expected):
                # už tam je 0; dej jinou typickou chybu — jen jeden z kořenů
                distractors.append(f"{var}\\;\\boldsymbol{{\\neq}}\\;0")
            else:
                distractors.append(f"{var}\\;\\boldsymbol{{\\neq}}\\;0,\\;" + expected.replace(f"{var}\\;\\boldsymbol{{\\neq}}\\;", "", 1).split(',')[0] if False else f"{var}\\;\\boldsymbol{{\\neq}}\\;0")
    # Dedup v případě shody; doplnit if potřeba
    seen = set()
    unique = []
    for d in distractors:
        if d not in seen and d != expected:
            seen.add(d)
            unique.append(d)
    while len(unique) < 3:
        unique.append(f"\\text{{jiná možnost {len(unique)+1}}}")
    return unique[:3]


def build_mc_options(idx: int, correct: str, distractors: list[str]):
    keys = ["a", "b", "c", "d"]
    pos = idx % 4
    correct_key = keys[pos]
    labels = distractors.copy()
    labels.insert(pos, correct)
    return correct_key, [{"key": k, "label_latex": f"${lab}$"} for k, lab in zip(keys, labels)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    args = parser.parse_args()
    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr); return 2

    SessionLocal = init_db(args.db_url)
    sess = SessionLocal()
    try:
        tasks = sess.query(MathTask).filter(MathTask.task_id.like("zsv_%")).all()
        candidates = []
        for t in tasks:
            c = t.content_latex or ""
            if c.startswith(NEMA_PREFIX):
                candidates.append((t, "nema"))
            elif c.startswith(MA_PREFIX):
                candidates.append((t, "ma"))
        print(f"Kandidátů: {len(candidates)}")

        changed = 0
        for idx, (t, kind) in enumerate(candidates):
            if isinstance(t.results, list) and len(t.results) == 1 and t.results[0].get("type") == "multiple_choice":
                continue
            expected = t.results[0].get("expected", "")
            distractors = build_distractors(expected, kind)
            correct_key, options = build_mc_options(idx, expected, distractors)
            new_results = [{
                "key": "vysledek",
                "label_latex": r"\text{Odpověď: }",
                "type": "multiple_choice",
                "options": options,
                "expected": correct_key,
            }]
            t.results = new_results
            flag_modified(t, "results")
            changed += 1
            if idx < 5:
                print(f"  {t.task_id} ({kind}): correct={correct_key}")
                for o in options:
                    marker = " ←" if o["key"] == correct_key else ""
                    print(f"    {o['key']}) {o['label_latex'][:80]}{marker}")

        print(f"\nZměněno: {changed}")
        if args.commit:
            sess.commit()
            print("✓ COMMIT proveden.")
        else:
            sess.rollback()
            print("(DRY-RUN — nic nezapsáno.)")
        return 0
    finally:
        sess.close()


if __name__ == "__main__":
    sys.exit(main())
