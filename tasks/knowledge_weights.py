"""
Definice vektoru vah (skill-komponent) pro AdaptMath.

KNOWLEDGE_WEIGHTS — plochý seznam **64** všech vah znalostního vektoru
úlohy. Při editaci expert nastavuje pro každou váhu procentuální hodnotu
(0–100), která vyjadřuje, jak moc daný skill úloha trénuje. Pro IRT/BKT
engine pak ve studentově profilu existuje paralelní vektor stejných vah
s hodnotami 0–1 (úroveň znalosti studenta v daném skillu).

Aktuální seznam pochází z konzultace s dr. Medkovou (verze 260601_v2):
13 logických skupin (Vlasnosti, Typ, Dovednosti, SŠ, Funkce, Monotonie,
Konvexnost/konkávnost, Spojitost, Limita, Derivace, Průběh funkce,
Primitivní funkce, Určitý integrál).

V UI rozlišujeme **dvě věci**:

  1) Vektor znalostí (`KNOWLEDGE_WEIGHTS`, 61) — celý mix vlastností,
     typu, dovedností i kategorií SŠ/VŠ. Edituje se sliderami.

  2) Anotace úlohy (ukládá se „bokem" pro pozdější automatické
     předvyplnění vektoru znalostí):
       - Kategorie (`TASK_CATEGORIES`, 46) — JEDNA primární kategorie
         úlohy. Jen SŠ + VŠ matematika (bez vlastností/typu/dovedností).
       - Vlastnosti (`TASK_PROPERTIES`, 11) — multi-select (checkboxy).
       - Typ (`TASK_TYPES`, 1) — multi-select (checkboxy).
       - Dovednosti (`TASK_SKILLS`, 6) — multi-select (checkboxy).

WEIGHT_GROUPS — mapping name → group key pro barevné rozlišení v UI.
"""

KNOWLEDGE_WEIGHTS = [
    # Vlastnosti (zelená) — 9 položek
    "Vlasnosti - Lineární",
    "Vlasnosti - Kvadratická",
    "Vlasnosti - Mocninná",
    "Vlasnosti - Odmocninové",
    "Vlasnosti - Logaritmická",
    "Vlasnosti - Exponenciální",
    "Vlastnosti - Goniometrická",  # zachováváme dle zdroje (varianta „Vlastnosti")
    "Vlasnosti - Absolutní hodnota",
    "Vlasnosti - Lomená lineární",
    "Vlasnosti - Zlomky",
    "Vlasnosti - S parametrem",

    # Typ (krémová) — 1 položka
    "Typ - Aplikační",

    # Dovednosti (oranžová) — 6 položek
    "Dovednosti - Aplikace vzorce",
    "Dovednosti - Vytýkání, krácení",
    "Dovednosti - Roznásobení závorky",
    "Dovednosti - Výpočet rovnic",
    "Dovednosti - Výpočet nerovnic",
    "Dovednosti - Derivování",

    # SŠ (žlutá) — 6 položek
    "SŠ - Algebraické výrazy",
    "SŠ - Elementární funkce",
    "SŠ - Rovnice",
    "SŠ - Nerovnice",
    "SŠ - Soustavy rovnic",
    "SŠ - Výroková logika",

    # Funkce — 7 položek
    "Funkce - Definiční obor",
    "Funkce - Aritmetika",
    "Funkce - Skládání/rozkládání",
    "Funkce - Sudá/lichá",
    "Funkce - Inverzní funkce",
    "Funkce - Tečna ke grafu",
    "Funkce - Asymptota",

    # Monotonie — 2 položky
    "Monotonie - Absolutní extrémy na intervalu",
    "Monotonie - Určování lokálních extrémů",

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
    "Limita - Typová limita",
    "Limita - Lhopitalovo pravidlo",

    # Derivace — 7 položek
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
    "Primitivní funkce - Parciální zlomky",

    # Určitý integrál — 8 položek
    "Určitý integrál - Sčítání",
    "Určitý integrál - Aditivita",
    "Určitý integrál - Per partes",
    "Určitý integrál - 1.věta o substituci",
    "Určitý integrál - 2.věta o substituci",
    "Určitý integrál - Parciální zlomky",
    "Určitý integrál - Nevlastní",
    "Určitý integrál - Obsah plochy",
]

# Pořadí je zde důležité — delší prefixy musí být první, aby
# např. „Primitivní funkce -" matchovalo dřív než nic.
_GROUP_PREFIXES = [
    ("Vlasnosti - ",          "vlasnosti"),
    ("Vlastnosti - ",         "vlasnosti"),   # alias pro „Vlastnosti" (zdrojová odlišnost)
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
# Položky bez prefixu („Konvexnost/konkávnost", „Průběh funkce") mají vlastní
# klíče přidělené explicitně níže.
_NO_PREFIX_GROUPS = {
    "Konvexnost/konkávnost": "konvex",
    "Průběh funkce":         "prubeh",
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
    "funkce":     "Funkce",
    "monotonie":  "Monotonie",
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
    "ss", "funkce", "monotonie", "konvex", "spojitost",
    "limita", "derivace", "prubeh", "pf", "ui",
}
TASK_CATEGORIES = [w for w in KNOWLEDGE_WEIGHTS if weight_group(w) in _CATEGORY_GROUPS]

# Multi-select checkboxy pod kategorií:
TASK_PROPERTIES = [w for w in KNOWLEDGE_WEIGHTS if weight_group(w) == "vlasnosti"]
TASK_TYPES      = [w for w in KNOWLEDGE_WEIGHTS if weight_group(w) == "typ"]
TASK_SKILLS     = [w for w in KNOWLEDGE_WEIGHTS if weight_group(w) == "dovednosti"]


# Sanity checky při importu
assert len(KNOWLEDGE_WEIGHTS) == 64, f"Očekáváno 64 vah, je {len(KNOWLEDGE_WEIGHTS)}"
assert len(set(KNOWLEDGE_WEIGHTS)) == len(KNOWLEDGE_WEIGHTS), "Duplicitní názvy vah!"
assert all(weight_group(w) != "default" for w in KNOWLEDGE_WEIGHTS), \
    f"Některá váha bez skupiny: {[w for w in KNOWLEDGE_WEIGHTS if weight_group(w) == 'default']}"
assert len(TASK_CATEGORIES) == 46, f"Očekáváno 46 kategorií, je {len(TASK_CATEGORIES)}"
assert len(TASK_PROPERTIES) == 11, f"Očekáváno 11 vlastností, je {len(TASK_PROPERTIES)}"
assert len(TASK_TYPES) == 1, f"Očekáván 1 typ, je {len(TASK_TYPES)}"
assert len(TASK_SKILLS) == 6, f"Očekáváno 6 dovedností, je {len(TASK_SKILLS)}"
assert len(TASK_CATEGORIES) + len(TASK_PROPERTIES) + len(TASK_TYPES) + len(TASK_SKILLS) \
       == len(KNOWLEDGE_WEIGHTS), "Suma anotačních podmnožin != 64"
