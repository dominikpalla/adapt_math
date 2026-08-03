"""
Parser UMAT skripta 2007-05-29 (Základy matematiky 1) → tasks/umat_NN.py.

Zdroj: /Users/dominikpalla/Downloads/skriptum_2007_05_29_finalni/texty/*.tex
(CP1250, custom makra \\zlom, \\lz, \\pz, \\tg, \\cotg, \\uloha, \\podul).

Extrahuje:
  \\uloha{content}{result}   — 2-arg makro s okamžitou odpovědí
  \\podul{content}{result}   — subitem podobně

Přeskočí:
  \\begin{ul}{...} \\end{ul} + \\noindent{\\bf Řešení:} ...
    (obsahuje \\begin{tabular} s a)-l) subitems + odpověď v následujícím
     odstavci; parsing by potřeboval speciální handling per chapter)

Použití:
    python scripts/extract_umat.py

Vypíše tasks/umat_01.py .. tasks/umat_11.py (per chapter).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

UMAT_DIR = Path("/Users/dominikpalla/Downloads/skriptum_2007_05_29_finalni/texty")
OUT_DIR = Path(__file__).resolve().parent.parent / "tasks"

CHAPTERS = [
    # Logika, důkazy, optimalizace mají textové odpovědi (nejsou matematické
    # výrazy) — nelze mechanicky konvertovat na mathlive/decimal. Přeskočeno.
    # ("umat_01", "1_logika.tex",         "Logika"),
    # ("umat_02", "2_dukazy.tex",         "Důkazy"),
    ("umat_03", "3_rovnice.tex",        "Rovnice a nerovnice"),
    ("umat_04", "4_realnefunkce.tex",   "Reálné funkce reálné proměnné"),
    ("umat_05", "5_explogfunkce.tex",   "Exponenciální a logaritmické funkce"),
    ("umat_06", "6_gon_rce_nrce.tex",   "Goniometrické rovnice a nerovnice"),
    ("umat_07", "7_posloupnosti.tex",   "Posloupnosti"),
    ("umat_08", "8_limita_fce.tex",     "Limita funkce"),
    ("umat_09", "9_derivace.tex",       "Derivace funkce"),
    # ("umat_10", "10_optimalizace.tex",  "Optimalizace"),
    ("umat_11", "11_prim_fce.tex",      "Primitivní funkce"),
]


# --- Makro expanze ----------------------------------------------------------

def expand_macros(s: str) -> str:
    """UMAT custom → standardní LaTeX + MathLive-friendly."""
    if not s:
        return s
    # \zlom{a}{b} → \frac{a}{b}
    s = re.sub(r"\\zlom\s*\{", r"\\frac{", s)
    # \lz → \langle, \pz → \rangle
    s = s.replace(r"\lz", r"\langle").replace(r"\pz", r"\rangle")
    # České trigonometrické konvence → MathLive Compute Engine standardy.
    # UMAT skriptum používá \tg i \mbox{tg} — obojí musíme mapovat.
    s = re.sub(r"\\mbox\s*\{\s*tg\s*\}",       r"\\tan",             s)
    s = re.sub(r"\\mbox\s*\{\s*cotg\s*\}",     r"\\cot",             s)
    s = re.sub(r"\\mbox\s*\{\s*arctg\s*\}",    r"\\arctan",          s)
    s = re.sub(r"\\mbox\s*\{\s*arccotg\s*\}",  r"\\text{arccot}",    s)
    s = re.sub(r"\\tg\b",       r"\\tan",     s)
    s = re.sub(r"\\cotg\b",     r"\\cot",     s)
    s = re.sub(r"\\arctg\b",    r"\\arctan",  s)
    s = re.sub(r"\\arccotg\b",  r"\\text{arccot}", s)  # KaTeX nemá arccot
    # Zbývající \mbox{...} → \text{...} (KaTeX podporuje \text)
    s = re.sub(r"\\mbox\s*\{",  r"\\text{",   s)
    # \Img → \Im (pokud tam někdy je)
    s = s.replace(r"\Img", r"\Im")
    # Odstranit sizing modifikátory kolem výsledku — jsou často
    # v odpovědích uvnitř \left[ \right]
    # \bigl[ \bigr] \Bigl[ atd. — zjednodušit na plain
    s = re.sub(r"\\[bB]igl\[", r"[", s)
    s = re.sub(r"\\[bB]igr\]", r"]", s)
    s = re.sub(r"\\biggl\[", r"[", s)
    s = re.sub(r"\\biggr\]", r"]", s)
    # \noindent, \hdef nezajímají nás v obsahu
    s = s.replace(r"\noindent", "")
    s = re.sub(r"\\hdef\{([^}]*)\}", r"\1", s)
    # Rozdělující tečka jako `1{,}5` → `1.5` — necháme, MathLive to zvládne oboje
    # Whitespace normalize
    s = re.sub(r"\s+", " ", s)
    return s.strip()


# --- Nalezení párovaných {...} argumentů ------------------------------------

def find_balanced_arg(text: str, start: int) -> tuple[str, int] | None:
    """Najdi obsah `{...}` začínající na `text[start] == '{'`.
    Vrátí (obsah_bez_ohraničujícího_{}, index_za_uzavírací_složenou závorkou)."""
    if start >= len(text) or text[start] != "{":
        return None
    depth = 0
    i = start
    while i < len(text):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return None  # nespárováno


def extract_two_arg_macro(text: str, macro_name: str) -> list[tuple[str, str, int]]:
    """Najde všechny `\\<macro_name>{arg1}{arg2}` a vrátí (arg1, arg2, pozice)."""
    out = []
    pattern = re.compile(r"\\" + re.escape(macro_name) + r"\s*\{")
    for m in pattern.finditer(text):
        r1 = find_balanced_arg(text, m.end() - 1)
        if not r1:
            continue
        arg1, next_start = r1
        # Přeskočit whitespace mezi {}{}
        while next_start < len(text) and text[next_start].isspace():
            next_start += 1
        if next_start >= len(text) or text[next_start] != "{":
            continue
        r2 = find_balanced_arg(text, next_start)
        if not r2:
            continue
        arg2, _ = r2
        out.append((arg1, arg2, m.start()))
    return out


# --- Detekce typu výsledku (heuristika) -------------------------------------

_DECIMAL_ONLY_RE = re.compile(r"^\s*-?\d+([.,]\d+)?\s*$")

# Textové odpovědi, které nejsou matematické (parser je nevyhodnotí korektně,
# uživatel by je viděl jako "chyba" i po správné odpovědi).
_TEXT_ANSWER_PATTERNS = re.compile(
    r"^(ano|ne|není|není\s+správn|neshodnou|neshodnou\s+se|čtverec|elipsa|hyperbola|parabola|"
    r"není\s+definován|neexistuje|leží|neleží|platí|neplatí|"
    r"kolmé|rovnoběžné|různoběžné|totožné)\b",
    re.IGNORECASE,
)


def looks_like_text(s: str) -> bool:
    """Heuristika: odpověď obsahuje víc než jednotlivé math tokeny → text."""
    # Očistíme sizing/text obaly
    plain = re.sub(r"\\text\{[^}]*\}", "", s)
    plain = re.sub(r"\$[^$]*\$", "", plain)  # embedovaný math sekvenční
    plain = plain.strip()
    if _TEXT_ANSWER_PATTERNS.match(plain):
        return True
    # Odpověď obsahuje čárkou-oddělený seznam čísel jako "5,7,9" (bez $)
    if re.match(r"^\s*-?\d+([.,]\d+)?\s*(,\s*-?\d+([.,]\d+)?\s*)+$", s.strip()):
        return True
    # Řetězec je delší než 6 znaků a víc než 50 % písmen z ASCII/Czech
    letters = re.findall(r"[a-zA-Zá-žÁ-Ž]", plain)
    if len(plain) > 6 and len(letters) / max(1, len(plain)) > 0.5:
        # ale ne když je to jen značka jako "x=", "F(x)", ...
        if not re.match(r"^[a-zA-Z](\(x\))?\s*=", plain):
            return True
    return False


def guess_result(expected_raw: str) -> dict:
    """Vrátí result dict {type, expected, tolerance?}. Očištěné.
    - Jen číslo → decimal
    - Jinak → mathlive
    - Poznámky, text, matematicky nekonvertovatelné → nechá jako mathlive
      (uživatel může později přepnout na multiple_choice)
    """
    # Odstranit vnější [ ... ] pokud tam jsou (z originálu `[ výsledek ]`)
    s = expected_raw.strip()
    s = re.sub(r"^\[\s*", "", s)
    s = re.sub(r"\s*\]$", "", s)
    s = expand_macros(s)
    # Odstranit `$...$` obal jestli je jenom jeden
    m = re.match(r"^\$(.*)\$$", s.strip())
    if m:
        s = m.group(1).strip()

    if _DECIMAL_ONLY_RE.match(s.replace(",", ".")):
        return {"type": "decimal", "expected": float(s.replace(",", ".")), "tolerance": 0.0}

    if looks_like_text(s):
        return None  # nezpracovatelné — skipnout úlohu

    return {"type": "mathlive", "expected": s, "tolerance": 0.0}


# --- Extraction per kapitola ------------------------------------------------

def extract_chapter(module_name: str, filename: str, chapter_title: str) -> list[dict]:
    """Vrátí seznam task dictů extrahovaných z jedné kapitoly UMAT skripta."""
    path = UMAT_DIR / filename
    raw = path.read_bytes()
    text = raw.decode("cp1250", errors="replace")

    tasks: list[dict] = []
    counter = 0

    def next_id() -> str:
        nonlocal counter
        counter += 1
        return f"{module_name}_{counter:02d}"

    # 1) \uloha{content}{result} — přímé 2-arg makro
    for content_raw, result_raw, _pos in extract_two_arg_macro(text, "uloha"):
        content = expand_macros(content_raw)
        if not content:
            continue
        result = guess_result(result_raw)
        if result is None:
            continue  # textová odpověď — nezařazujeme
        # obalit content_latex do $...$ pokud tam žádný $ není a vypadá to jako math
        clean_content = content
        tasks.append({
            "task_id": next_id(),
            "content_latex": clean_content,
            "results": [{
                "key": "vysledek",
                "label_latex": r"= ",
                **result,
            }],
            "cognitive_load": "C",
        })

    # 2) \podul{content}{result} — subitem 2-arg makro
    for content_raw, result_raw, _pos in extract_two_arg_macro(text, "podul"):
        content = expand_macros(content_raw)
        if not content:
            continue
        result = guess_result(result_raw)
        if result is None:
            continue  # textová odpověď — nezařazujeme
        tasks.append({
            "task_id": next_id(),
            "content_latex": content,
            "results": [{
                "key": "vysledek",
                "label_latex": r"= ",
                **result,
            }],
            "cognitive_load": "C",
        })

    return tasks


# --- Zápis modulu -----------------------------------------------------------

def write_module(module_name: str, chapter_title: str, filename: str, tasks: list[dict]) -> Path:
    out = OUT_DIR / f"{module_name}.py"
    lines = [
        '"""',
        f'UMAT — kapitola {module_name.split("_")[1]}: {chapter_title}.',
        '',
        f'Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/{filename}` (skriptum 2007-05-29).',
        'Automaticky vyextrahováno skriptem scripts/extract_umat.py 2026-08-03.',
        '',
        'Extrahuje jen \\\\uloha{content}{result} a \\\\podul{content}{result}.',
        'Bloky \\\\begin{ul}{...}\\\\end{ul} s oddělenou odpovědí v `Řešení:` odstavci',
        'nejsou v tomto exportu — jejich formát vyžaduje ruční extrakci.',
        '',
        'Makra rozvinutá: \\\\zlom → \\\\frac, \\\\lz/\\\\pz → \\\\langle/\\\\rangle,',
        '\\\\tg/\\\\cotg/\\\\arctg → \\\\tan/\\\\cot/\\\\arctan.',
        '"""',
        '',
        'TASKS = [',
    ]
    for t in tasks:
        lines.append('    {')
        lines.append(f'        "task_id": {t["task_id"]!r},')
        lines.append(f'        "content_latex": {t["content_latex"]!r},')
        r = t["results"][0]
        if r["type"] == "decimal":
            lines.append(f'        "results": [{{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": {r["expected"]}, "tolerance": {r["tolerance"]}}}],')
        else:
            lines.append(f'        "results": [{{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": {r["expected"]!r}, "tolerance": {r["tolerance"]}}}],')
        lines.append(f'        "cognitive_load": {t["cognitive_load"]!r},')
        lines.append('    },')
    lines.append(']')
    lines.append('')
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> int:
    if not UMAT_DIR.exists():
        print(f"Chyba: {UMAT_DIR} neexistuje.", file=sys.stderr)
        return 2

    total = 0
    generated_modules: list[str] = []
    for module_name, filename, title in CHAPTERS:
        try:
            tasks = extract_chapter(module_name, filename, title)
        except Exception as e:
            print(f"⚠ {module_name} ({filename}): parser error: {e}", file=sys.stderr)
            continue
        if not tasks:
            print(f"  {module_name}: 0 úloh (přeskočeno)")
            continue
        out = write_module(module_name, title, filename, tasks)
        print(f"  {module_name}: {len(tasks)} úloh → {out}")
        total += len(tasks)
        generated_modules.append(module_name)

    print()
    print(f"CELKEM: {total} úloh v {len(generated_modules)} modulech.")
    print()
    print("Přidej do tasks/__init__.py:")
    print(f"  from . import {', '.join(generated_modules)}")
    print(f"  # a přidej do ALL_TASKS: + {' + '.join(m + '.TASKS' for m in generated_modules)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
