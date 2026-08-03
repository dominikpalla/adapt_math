"""
Rozšířený UMAT parser — pokrývá i \\begin{ul} bloky a textové odpovědi.

Zpracovává:
  1. \\uloha{content}{result}   — 2-arg makro
  2. \\podul{content}{result}   — subitem 2-arg makro
  3. \\begin{ul}{instrukce}\\begin{tabular}...\\end{tabular}\\end{ul}
     + \\noindent{\\bf Řešení:} a) ..., b) ..., ...
  4. Textové odpovědi ("ano"/"ne"/"leží"/...) → multiple_choice
  5. Seznamy čísel ("5,7,9") → N decimal keys

Použití:
    python scripts/extract_umat_v2.py

Vyprodukuje tasks/umat_XX_extra.py — dedikované moduly s prefixem umatXXe_
(aby task_id nekolidovaly s tím, co už bylo insertnuto předchozím extractorem).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

UMAT_DIR = Path("/Users/dominikpalla/Downloads/skriptum_2007_05_29_finalni/texty")
OUT_DIR = Path(__file__).resolve().parent.parent / "tasks"

# Kapitoly, pro které chceme dělat extra extraction (nikoli 06-09 kde už DB
# má insertované úlohy — abychom nekolidovali task_id).
CHAPTERS = [
    ("umat_01e", "1_logika.tex",         "Logika (extra)",              "e01"),
    ("umat_02e", "2_dukazy.tex",         "Důkazy (extra)",              "e02"),
    ("umat_03e", "3_rovnice.tex",        "Rovnice a nerovnice (extra)", "e03"),
    ("umat_04e", "4_realnefunkce.tex",   "Reálné funkce (extra)",       "e04"),
    ("umat_05e", "5_explogfunkce.tex",   "Exp a log funkce (extra)",    "e05"),
    ("umat_10e", "10_optimalizace.tex",  "Optimalizace (extra)",        "e10"),
    ("umat_11e", "11_prim_fce.tex",      "Primitivní funkce (extra)",   "e11"),
]


# --- Makro expanze (stejná jako v v1) ---------------------------------------

def expand_macros(s: str) -> str:
    if not s:
        return s
    # \zlom{a}{b} → \frac{a}{b}
    s = re.sub(r"\\zlom\s*\{", r"\\frac{", s)
    # \zlomab (TeX shorthand — argumenty jednotlivé tokeny) → \frac{a}{b}
    # např. \zlom15 → \frac{1}{5}, \zlom23 → \frac{2}{3}
    s = re.sub(r"\\zlom(\d)(\d)", r"\\frac{\1}{\2}", s)
    s = re.sub(r"\\zlom(\d)([a-zA-Z])", r"\\frac{\1}{\2}", s)
    s = re.sub(r"\\zlom([a-zA-Z])(\d)", r"\\frac{\1}{\2}", s)
    s = re.sub(r"\\zlom([a-zA-Z])([a-zA-Z])", r"\\frac{\1}{\2}", s)
    # \velint → \int (velký integrál v UMAT stylu)
    s = re.sub(r"\\velint\b", r"\\int", s)
    s = s.replace(r"\lz", r"\langle").replace(r"\pz", r"\rangle")
    s = re.sub(r"\\mbox\s*\{\s*tg\s*\}",       r"\\tan",             s)
    s = re.sub(r"\\mbox\s*\{\s*cotg\s*\}",     r"\\cot",             s)
    s = re.sub(r"\\mbox\s*\{\s*arctg\s*\}",    r"\\arctan",          s)
    s = re.sub(r"\\mbox\s*\{\s*arccotg\s*\}",  r"\\text{arccot}",    s)
    s = re.sub(r"\\tg\b",       r"\\tan",     s)
    s = re.sub(r"\\cotg\b",     r"\\cot",     s)
    s = re.sub(r"\\arctg\b",    r"\\arctan",  s)
    s = re.sub(r"\\arccotg\b",  r"\\text{arccot}", s)
    s = re.sub(r"\\mbox\s*\{",  r"\\text{",   s)
    s = s.replace(r"\Img", r"\Im")
    s = re.sub(r"\\[bB]igl\[", r"[", s)
    s = re.sub(r"\\[bB]igr\]", r"]", s)
    s = re.sub(r"\\biggl\[", r"[", s)
    s = re.sub(r"\\biggr\]", r"]", s)
    s = s.replace(r"\noindent", "")
    s = re.sub(r"\\hdef\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


# --- Nalezení párovaných {...} argumentů ------------------------------------

def find_balanced_arg(text: str, start: int) -> tuple[str, int] | None:
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
    return None


def extract_two_arg_macro(text: str, macro_name: str) -> list[tuple[str, str, int]]:
    out = []
    pattern = re.compile(r"\\" + re.escape(macro_name) + r"\s*\{")
    for m in pattern.finditer(text):
        r1 = find_balanced_arg(text, m.end() - 1)
        if not r1:
            continue
        arg1, next_start = r1
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


# --- Text answer → MC konverze ---------------------------------------------

# Mapa známých textových odpovědí → možnosti MC.
# Klíč = normalizovaný text odpovědi (lowercase, bez interpunkce).
# Value = (options_list, correct_key)
TEXT_TO_MC = {
    # Binární výroky
    "ano":       ([("a", "ano"), ("b", "ne")], "a"),
    "ne":        ([("a", "ano"), ("b", "ne")], "b"),
    "platí":     ([("a", "platí"), ("b", "neplatí")], "a"),
    "neplatí":   ([("a", "platí"), ("b", "neplatí")], "b"),
    "je":        ([("a", "je"), ("b", "není")], "a"),
    "není":      ([("a", "je"), ("b", "není")], "b"),
    "leží":      ([("a", "leží"), ("b", "neleží")], "a"),
    "neleží":    ([("a", "leží"), ("b", "neleží")], "b"),
    "existuje":  ([("a", "existuje"), ("b", "neexistuje")], "a"),
    "neexistuje":([("a", "existuje"), ("b", "neexistuje")], "b"),
    # Vzájemná poloha přímek
    "kolmé":         ([("a", "kolmé"), ("b", "rovnoběžné"), ("c", "různoběžné"), ("d", "totožné")], "a"),
    "rovnoběžné":    ([("a", "kolmé"), ("b", "rovnoběžné"), ("c", "různoběžné"), ("d", "totožné")], "b"),
    "různoběžné":    ([("a", "kolmé"), ("b", "rovnoběžné"), ("c", "různoběžné"), ("d", "totožné")], "c"),
    "totožné":       ([("a", "kolmé"), ("b", "rovnoběžné"), ("c", "různoběžné"), ("d", "totožné")], "d"),
    # Druhy kuželoseček
    "parabola":  ([("a", "parabola"), ("b", "elipsa"), ("c", "hyperbola"), ("d", "kružnice")], "a"),
    "elipsa":    ([("a", "parabola"), ("b", "elipsa"), ("c", "hyperbola"), ("d", "kružnice")], "b"),
    "hyperbola": ([("a", "parabola"), ("b", "elipsa"), ("c", "hyperbola"), ("d", "kružnice")], "c"),
    "kružnice":  ([("a", "parabola"), ("b", "elipsa"), ("c", "hyperbola"), ("d", "kružnice")], "d"),
    # Zvláštní: neshodnou se (logika)
    "neshodnou se": ([("a", "shodnou se"), ("b", "neshodnou se")], "b"),
    "shodnou se":   ([("a", "shodnou se"), ("b", "neshodnou se")], "a"),
}

_LIST_OF_NUMBERS_RE = re.compile(
    r"^\s*(-?\d+(?:[.,]\d+)?(?:/\d+)?)\s*(?:,\s*(-?\d+(?:[.,]\d+)?(?:/\d+)?)\s*)+$"
)


def _normalize_text_answer(s: str) -> str:
    s = s.strip().rstrip(".,;:").lower()
    return s


def try_text_to_mc(expected_raw: str) -> dict | None:
    """Zkusí konvertovat text odpověď na MC. Vrátí result dict nebo None."""
    plain = re.sub(r"\$[^$]*\$", "", expected_raw)  # smazat embedovanou matematiku
    plain = _normalize_text_answer(plain)
    if plain in TEXT_TO_MC:
        options, correct = TEXT_TO_MC[plain]
        return {
            "type": "multiple_choice",
            "expected": correct,
            "options": [{"key": k, "label_latex": v} for k, v in options],
        }
    return None


def try_list_of_numbers(expected_raw: str) -> list[dict] | None:
    """`5, 7, 9` nebo `5,7,9` → seznam decimal results (max 8 hodnot)."""
    s = expected_raw.strip()
    s = re.sub(r"^\[\s*", "", s)
    s = re.sub(r"\s*\]$", "", s)
    s = re.sub(r"\$", "", s)  # smaž $
    # Přísný match — jen pro čistý seznam čísel oddělených čárkou.
    # Bez tohoto testu by parser chytal koeficienty z LaTeX výrazů
    # (např. `x^3 + x^2 - 4x + C` → mylně `[3, 2, -4]`).
    if not _LIST_OF_NUMBERS_RE.match(s):
        return None
    nums = re.findall(r"-?\d+(?:[.,]\d+)?(?:/\d+)?", s)

    results = []
    for i, num in enumerate(nums, start=1):
        num_str = num.replace(",", ".")
        # Zlomek?
        if "/" in num_str:
            try:
                a, b = num_str.split("/")
                val = float(a) / float(b)
            except (ValueError, ZeroDivisionError):
                return None
        else:
            try:
                val = float(num_str)
            except ValueError:
                return None
        results.append({
            "key": f"x_{i}",
            "label_latex": rf"x_{i} = ",
            "type": "decimal",
            "expected": val,
            "tolerance": 0.01,
        })
    return results


# --- Detekce typu výsledku --------------------------------------------------

_DECIMAL_ONLY_RE = re.compile(r"^\s*-?\d+([.,]\d+)?\s*$")


def guess_results(expected_raw: str) -> list[dict] | None:
    """Vrátí seznam result dictů (většinou 1 položka; víc pro list-of-numbers).
    Vrátí None, pokud nelze rozumně zpracovat."""
    s = expected_raw.strip()
    s = re.sub(r"^\[\s*", "", s)
    s = re.sub(r"\s*\]$", "", s)

    # Zkus text → MC ještě před expanzí maker (rychlejší)
    mc = try_text_to_mc(s)
    if mc:
        return [dict(mc, key="vysledek", label_latex="")]

    # Zkus list of numbers
    lon = try_list_of_numbers(s)
    if lon:
        return lon

    s = expand_macros(s)
    m = re.match(r"^\$(.*)\$$", s.strip())
    if m:
        s = m.group(1).strip()

    if _DECIMAL_ONLY_RE.match(s.replace(",", ".")):
        return [{"key": "vysledek", "label_latex": r"= ", "type": "decimal",
                 "expected": float(s.replace(",", ".")), "tolerance": 0.0}]

    # Cokoli jiného → mathlive
    return [{"key": "vysledek", "label_latex": r"= ", "type": "mathlive",
             "expected": s, "tolerance": 0.0}]


# --- Parser \begin{ul}...\end{ul} + \noindent{\bf Řešení:} ------------------

_UL_RE = re.compile(r"\\begin\{ul\}\s*\{", re.DOTALL)
_RESENI_RE = re.compile(
    r"\\noindent\s*\{\s*\\bf\s+(?:Řešení|�e�en�|Reseni)\s*:\s*\}(.*?)(?=\\begin\{|\\vyklad|\\ulohy|\\priklady|\\popis|\\end\{document\}|\Z)",
    re.DOTALL,
)


def parse_ul_blocks(text: str) -> list[tuple[str, list[str], list[str]]]:
    """Najde všechny \\begin{ul}{instr}...\\end{ul} bloky + jejich Řešení odstavce.
    Vrací list (instr, subitem_texts, subitem_answers).
    """
    blocks = []
    for m in _UL_RE.finditer(text):
        # Extrahuj argument (instrukce)
        arg_result = find_balanced_arg(text, m.end() - 1)
        if not arg_result:
            continue
        instr, after_arg = arg_result

        # Najdi \end{ul} za tímto argumentem
        end_match = re.search(r"\\end\{ul\}", text[after_arg:])
        if not end_match:
            continue
        end_ul_pos = after_arg + end_match.start()
        body_between = text[after_arg:end_ul_pos]  # obsah mezi arg a \end{ul}

        # Najdi Řešení: odstavec za \end{ul}
        after_end_ul = end_ul_pos + len("\\end{ul}")
        # Řešení je ve zbývajícím textu, ale jen do dalšího \begin{ul} nebo jiné struktury
        resen_match = _RESENI_RE.search(text[after_end_ul:after_end_ul + 3000])
        if not resen_match:
            continue
        resen_text = resen_match.group(1)

        # Extrahuj subitems z instrukce + body (může být tabular)
        subitems = _extract_subitems(instr + " " + body_between)
        if not subitems:
            # Není subitems v tabular → celý blok je jedna úloha (jednoduchý případ)
            answer = resen_text.strip()
            blocks.append((expand_macros(instr).strip(), [instr.strip()], [answer]))
            continue

        # Parse Řešení do subitems dle a), b), c), ...
        answers = _parse_resenice(resen_text, len(subitems))
        if not answers:
            continue

        blocks.append((expand_macros(instr).strip(), subitems, answers))
    return blocks


_SUBITEM_RE = re.compile(r"[a-l]\)\s*(.+?)(?=(?:[a-l]\))|$|\\\\|\&)", re.DOTALL)


def _extract_subitems(body: str) -> list[str]:
    """Rozloží text (např. tabular obsah) na jednotlivé subitems a), b), c), ..."""
    # Odstranit tabular boilerplate
    body = re.sub(r"\\begin\{tabular\}\{[^}]*\}", "", body)
    body = re.sub(r"\\end\{tabular\}", "", body)
    body = re.sub(r"\\hspace\{[^}]*\}", "", body)
    body = re.sub(r"\\vspace\{[^}]*\}", "", body)
    # Rozděl podle a)-l) markerů
    matches = list(re.finditer(r"([a-l])\)\s*", body))
    if not matches:
        return []
    subitems = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        text = body[start:end]
        # Vyčisti oddělovače tabular
        text = text.replace("&", "").replace("\\\\", "").strip()
        if text:
            subitems.append(text)
    return subitems


def _parse_resenice(resen_text: str, expected_count: int) -> list[str]:
    """Vyparsuje Řešení: paragraph do jednotlivých answer stringů podle a), b), c), ...
    Očekává, že bude přesně `expected_count` položek."""
    matches = list(re.finditer(r"([a-l])\)\s*", resen_text))
    if not matches:
        return []
    answers = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(resen_text)
        ans = resen_text[start:end].strip().rstrip(",;.")
        answers.append(ans)
    # Pokud počet neodpovídá, vrátíme co máme (partial match)
    return answers


# --- Extrakce per kapitola --------------------------------------------------

def extract_chapter(prefix_short: str, filename: str) -> list[dict]:
    path = UMAT_DIR / filename
    text = path.read_bytes().decode("cp1250", errors="replace")

    tasks = []
    counter = 0

    def next_id() -> str:
        nonlocal counter
        counter += 1
        return f"{prefix_short}_{counter:02d}"

    # 1) \uloha{content}{result}
    for content_raw, result_raw, _pos in extract_two_arg_macro(text, "uloha"):
        content = expand_macros(content_raw)
        if not content:
            continue
        results = guess_results(result_raw)
        if results is None:
            continue
        tasks.append({
            "task_id": next_id(),
            "content_latex": content,
            "results": results,
            "cognitive_load": "C",
        })

    # 2) \podul{content}{result}
    for content_raw, result_raw, _pos in extract_two_arg_macro(text, "podul"):
        content = expand_macros(content_raw)
        if not content:
            continue
        results = guess_results(result_raw)
        if results is None:
            continue
        tasks.append({
            "task_id": next_id(),
            "content_latex": content,
            "results": results,
            "cognitive_load": "C",
        })

    # 3) \begin{ul}{...}\end{ul} bloky s Řešením
    for instr, subitems, answers in parse_ul_blocks(text):
        for i, sub in enumerate(subitems):
            if i >= len(answers):
                break
            content = f"{instr} " + expand_macros(sub)
            results = guess_results(answers[i])
            if results is None:
                continue
            tasks.append({
                "task_id": next_id(),
                "content_latex": content,
                "results": results,
                "cognitive_load": "C",
            })

    return tasks


# --- Zápis modulu (jednodušší, používá repr) --------------------------------

def write_module(module_name: str, chapter_title: str, filename: str, tasks: list[dict]) -> Path:
    out = OUT_DIR / f"{module_name}.py"
    lines = [
        '"""',
        f'{chapter_title}.',
        '',
        f'Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/{filename}` (2007-05-29).',
        'Automaticky vyextrahováno scripts/extract_umat_v2.py 2026-08-03.',
        '',
        'Rozšířený parser oproti v1: převod textových odpovědí na multiple_choice,',
        'seznamů čísel na N decimal keys, a parsing \\\\begin{ul}...\\\\end{ul} bloků',
        's odpovědí v následujícím `Řešení:` odstavci.',
        '"""',
        '',
        'TASKS = [',
    ]
    for t in tasks:
        lines.append('    {')
        lines.append(f'        "task_id": {t["task_id"]!r},')
        lines.append(f'        "content_latex": {t["content_latex"]!r},')
        lines.append(f'        "results": {t["results"]!r},')
        lines.append(f'        "cognitive_load": {t["cognitive_load"]!r},')
        lines.append('    },')
    lines.append(']')
    lines.append('')
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> int:
    total = 0
    generated_modules: list[str] = []
    for module_name, filename, title, prefix_short in CHAPTERS:
        try:
            tasks = extract_chapter(prefix_short, filename)
        except Exception as e:
            print(f"⚠ {module_name} ({filename}): parser error: {e}", file=sys.stderr)
            import traceback; traceback.print_exc()
            continue
        if not tasks:
            print(f"  {module_name}: 0 úloh (přeskočeno)")
            continue
        out = write_module(module_name, title, filename, tasks)
        print(f"  {module_name}: {len(tasks)} úloh → {out}")
        total += len(tasks)
        generated_modules.append(module_name)

    print()
    print(f"CELKEM: {total} úloh v {len(generated_modules)} extra modulech.")
    print()
    if generated_modules:
        print("Přidej do tasks/__init__.py:")
        print(f"  from . import {', '.join(generated_modules)}")
        print(f"  + {' + '.join(m + '.TASKS' for m in generated_modules)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
