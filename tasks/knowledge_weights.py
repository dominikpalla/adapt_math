"""
Definice vektoru vah (skill-komponent) pro AdaptMath.

KNOWLEDGE_WEIGHTS — plochý seznam **79** všech vah znalostního vektoru
úlohy. Při editaci expert nastavuje pro každou váhu procentuální hodnotu
(0–100), která vyjadřuje, jak moc daný skill úloha trénuje. Pro IRT/BKT
engine pak ve studentově profilu existuje paralelní vektor stejných vah
s hodnotami 0–1 (úroveň znalosti studenta v daném skillu).

Aktuální seznam navazuje na verzi 260820 s revizí dr. Medkové 2026-08-24:
sjednocení pravopisu prefixu ,,Vlastnosti - `` (dřív 10× překlep
,,Vlasnosti - ''), přidány 4 nové vlastnosti (Polynomy, Lomená
kvadratická, Podíl funkcí ostatních, Cyklometrická), přidáno 7 nových
dovedností (Substituce, Práce s množinami, Dělení polynomů/Horner,
Integrování, Aritmetika funkcí, Skládání/rozklad funkcí, Ověření/využití
vlastností), přejmenováno ,,Výpočet rovnic/nerovnic'' -> ,,Řešení
rovnic/nerovnic'', sloučeno ,,Vytýkání, krácení'' + ,,Roznásobení
závorky'' -> jedna položka ,,Vytýkání/roznásobení výrazu v závorce''.

Aktuálně 14 logických skupin (Vlastnosti, Typ, Dovednosti, SŠ, Výroková
logika, Funkce, Monotonie a extrémy, Konvexnost/konkávnost, Spojitost,
Limita, Derivace, Průběh funkce, Primitivní funkce, Určitý integrál).

V UI rozlišujeme **dvě věci**:

  1) Vektor znalostí (`KNOWLEDGE_WEIGHTS`, 79) — celý mix vlastností,
     typu, dovedností i kategorií SŠ/VŠ. Edituje se sliderami.

  2) Anotace úlohy (ukládá se „bokem" pro pozdější automatické
     předvyplnění vektoru znalostí):
       - Kategorie (`TASK_CATEGORIES`, 46) — JEDNA primární kategorie
         úlohy. Jen SŠ + VŠ matematika (bez vlastností/typu/dovedností).
       - Vlastnosti (`TASK_PROPERTIES`, 15) — multi-select (checkboxy).
       - Typ (`TASK_TYPES`, 2) — multi-select (checkboxy).
       - Dovednosti (`TASK_SKILLS`, 13) — multi-select (checkboxy).

WEIGHT_GROUPS — mapping name → group key pro barevné rozlišení v UI.
"""

KNOWLEDGE_WEIGHTS = [
    # Vlastnosti (zelená) — 15 položek
    "Vlastnosti - Lineární",
    "Vlastnosti - Kvadratická",
    "Vlastnosti - Mocninná",
    "Vlastnosti - Polynomy",               # 2026-08-24: nová
    "Vlastnosti - Lomená lineární",
    "Vlastnosti - Lomená kvadratická",     # 2026-08-24: nová
    "Vlastnosti - Racionální funkce",
    "Vlastnosti - Podíl funkcí ostatních", # 2026-08-24: nová
    "Vlastnosti - Logaritmická",
    "Vlastnosti - Exponenciální",
    "Vlastnosti - Odmocninová",
    "Vlastnosti - Absolutní hodnota",
    "Vlastnosti - Goniometrická",
    "Vlastnosti - Cyklometrická",          # 2026-08-24: nová
    "Vlastnosti - S parametrem",

    # Typ (krémová) — 2 položky
    "Typ - Aplikační",
    "Typ - Extrémy funkcí",

    # Dovednosti (oranžová) — 13 položek
    "Dovednosti - Vytýkání/roznásobení výrazu v závorce",  # 2026-08-24: merge
    "Dovednosti - Úpravy zlomků",
    "Dovednosti - Substituce",             # 2026-08-24: nová
    "Dovednosti - Práce s množinami",      # 2026-08-24: nová
    "Dovednosti - Dělení polynomů/Horner", # 2026-08-24: nová
    "Dovednosti - Aplikace vzorce",
    "Dovednosti - Řešení rovnic",          # 2026-08-24: rename z Výpočet rovnic
    "Dovednosti - Řešení nerovnic",        # 2026-08-24: rename z Výpočet nerovnic
    "Dovednosti - Derivování",
    "Dovednosti - Integrování",            # 2026-08-24: nová
    "Dovednosti - Aritmetika funkcí",      # 2026-08-24: nová
    "Dovednosti - Skládání/rozklad funkcí",# 2026-08-24: nová
    "Dovednosti - Ověření/využití vlastností", # 2026-08-24: nová

    # SŠ (žlutá) — 8 položek
    "SŠ - Algebraické výrazy",
    "SŠ - Elementární funkce",
    "SŠ - Rovnice",
    "SŠ - Nerovnice",
    "SŠ - Soustavy rovnic",
    "SŠ - Posloupnosti",           # 2026-08-24: nová
    "SŠ - Množiny a relace",       # 2026-08-24: nová
    "SŠ - Analytická geometrie",   # 2026-08-24: nová

    # Výroková logika (samostatná skupina „logika") — 1 položka
    "Výroková logika",

    # Funkce — 7 položek
    "Funkce - Definiční obor",
    "Funkce - Aritmetika",
    "Funkce - Skládání/rozkládání",
    "Funkce - Sudá/lichá",
    "Funkce - Inverzní funkce",
    "Funkce - Tečna ke grafu",
    "Funkce - Asymptota",

    # Monotonie a extrémy (samostatná top-level položka, historicky
    # 2 podpoložky Monotonie sloučeny do jedné) — 1 položka
    "Monotonie a extrémy",

    # Konvexnost/konkávnost — 1 položka
    "Konvexnost/konkávnost",

    # Spojitost — 2 položky
    "Spojitost - Spojitost",
    "Spojitost - Bolzanova věta",

    # Limita — 7 položek
    "Limita - VOAL (dosazení)",
    "Limita - LVL (krácení)",
    "Limita - S odmocninou",
    "Limita - Vytknutí nejvyšší mocniny",
    "Limita - Jednostranné limity",
    "Limita - Limita složené funkce",
    "Limita - Lhopitalovo pravidlo",

    # Derivace — 8 položek
    "Derivace - Definice",         # 2026-09-03: nová
    "Derivace - Sčítání",
    "Derivace - Součin",
    "Derivace - Podíl",
    "Derivace - Složená funkce",
    "Derivace - Diferenciál",
    "Derivace - Taylorův polynom",
    "Derivace - Vyšší řády",

    # Průběh funkce — 1 položka
    "Průběh funkce",

    # Primitivní funkce — 5 položek
    "Primitivní funkce - Sčítání",
    "Primitivní funkce - Per partes",
    "Primitivní funkce - 1.věta o subustituci",
    "Primitivní funkce - 2.věta o substituci",
    "Primitivní funkce - Racionální funkce",

    # Určitý integrál — 8 položek
    "Určitý integrál - Sčítání",
    "Určitý integrál - Aditivita",
    "Určitý integrál - Per partes",
    "Určitý integrál - 1.věta o substituci",
    "Určitý integrál - 2.věta o substituci",
    "Určitý integrál - Racionální funkce",
    "Určitý integrál - Nevlastní",
    "Určitý integrál - Obsah plochy",
]

# Pořadí je zde důležité — delší prefixy musí být první, aby
# např. „Primitivní funkce -" matchovalo dřív než nic.
_GROUP_PREFIXES = [
    ("Vlastnosti - ",         "vlasnosti"),
    ("Typ - ",                "typ"),
    ("Dovednosti - ",         "dovednosti"),
    ("SŠ - ",                 "ss"),
    ("Funkce - ",             "funkce"),
    ("Monotonie - ",          "monotonie"),
    ("Spojitost - ",          "spojitost"),
    ("Limita - ",             "limita"),
    ("Derivace - ",           "derivace"),
    ("Primitivní funkce - ",  "pf"),
    ("Určitý integrál - ",    "ui"),
]
# Položky bez prefixu („Konvexnost/konkávnost", „Průběh funkce",
# „Monotonie a extrémy", „Výroková logika") mají vlastní klíče
# přidělené explicitně níže.
_NO_PREFIX_GROUPS = {
    "Konvexnost/konkávnost": "konvex",
    "Průběh funkce":         "prubeh",
    "Monotonie a extrémy":   "monotonie",   # sloučené z původních 2 „Monotonie - …"
    "Výroková logika":       "logika",      # dříve „SŠ - Výroková logika", nyní samostatná skupina
}


def weight_group(name: str) -> str:
    """Vrátí klíč skupiny pro CSS barvu (např. 'vlasnosti', 'limita')."""
    if name in _NO_PREFIX_GROUPS:
        return _NO_PREFIX_GROUPS[name]
    for prefix, group in _GROUP_PREFIXES:
        if name.startswith(prefix):
            return group
    return "default"


# Předpočítaný dict pro Jinja templaty: {name: group_key}
WEIGHT_GROUPS = {w: weight_group(w) for w in KNOWLEDGE_WEIGHTS}

# Lidsky čitelné labely skupin (pro legendu v UI).
GROUP_LABELS = {
    "vlasnosti":  "Vlastnosti",
    "typ":        "Typ",
    "dovednosti": "Dovednosti",
    "ss":         "SŠ",
    "logika":     "Výroková logika",
    "funkce":     "Funkce",
    "monotonie":  "Monotonie a extrémy",
    "konvex":     "Konvexnost/konkávnost",
    "spojitost":  "Spojitost",
    "limita":     "Limita",
    "derivace":   "Derivace",
    "prubeh":     "Průběh funkce",
    "pf":         "Primitivní funkce",
    "ui":         "Určitý integrál",
}

# --- Anotační podmnožiny (ukládají se „bokem" do tasku, viz model.py) ---
#
# TASK_CATEGORIES je primární **jedinečná** kategorie (single-select); jen
# matematické tematické skupiny (SŠ + VŠ), tedy bez Vlastností/Typu/Dovedností.
_CATEGORY_GROUPS = {
    "ss", "logika", "funkce", "monotonie", "konvex", "spojitost",
    "limita", "derivace", "prubeh", "pf", "ui",
}
TASK_CATEGORIES = [w for w in KNOWLEDGE_WEIGHTS if weight_group(w) in _CATEGORY_GROUPS]

# Multi-select checkboxy pod kategorií:
TASK_PROPERTIES = [w for w in KNOWLEDGE_WEIGHTS if weight_group(w) == "vlasnosti"]
TASK_TYPES      = [w for w in KNOWLEDGE_WEIGHTS if weight_group(w) == "typ"]
TASK_SKILLS     = [w for w in KNOWLEDGE_WEIGHTS if weight_group(w) == "dovednosti"]


# Sanity checky při importu
assert len(KNOWLEDGE_WEIGHTS) == 79, f"Očekáváno 79 vah, je {len(KNOWLEDGE_WEIGHTS)}"
assert len(set(KNOWLEDGE_WEIGHTS)) == len(KNOWLEDGE_WEIGHTS), "Duplicitní názvy vah!"
assert all(weight_group(w) != "default" for w in KNOWLEDGE_WEIGHTS), \
    f"Některá váha bez skupiny: {[w for w in KNOWLEDGE_WEIGHTS if weight_group(w) == 'default']}"
assert len(TASK_CATEGORIES) == 49, f"Očekáváno 49 kategorií, je {len(TASK_CATEGORIES)}"
assert len(TASK_PROPERTIES) == 15, f"Očekáváno 15 vlastností, je {len(TASK_PROPERTIES)}"
assert len(TASK_TYPES) == 2, f"Očekávány 2 typy, je {len(TASK_TYPES)}"
assert len(TASK_SKILLS) == 13, f"Očekáváno 13 dovedností, je {len(TASK_SKILLS)}"
assert len(TASK_CATEGORIES) + len(TASK_PROPERTIES) + len(TASK_TYPES) + len(TASK_SKILLS) \
       == len(KNOWLEDGE_WEIGHTS), "Suma anotačních podmnožin != 79"
