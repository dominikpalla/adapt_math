"""
Definice vektoru vah (skill-komponent) pro AdaptMath.

KNOWLEDGE_WEIGHTS — plochý seznam všech vah znalostního vektoru úlohy.
Při editaci úlohy expert nastavuje pro každou váhu procentuální hodnotu
(0–100), která vyjadřuje, jak moc daný skill úloha trénuje. Při úspěšném
vyřešení úlohy se přírůstek znalosti rozdělí mezi její skill-komponenty
v poměru daném těmito vahami; při nesplnění se obdobně rozdělí úbytek.

Pro IRT/BKT engine pak ve studentově profilu existuje paralelní vektor
stejných vah s hodnotami 0–1 (úroveň znalosti studenta v daném skillu).

Duplicitní názvy „Sčítání" rozlišujeme prefixem:
    „Derivace — Sčítání"   vs   „Prim. funkce — Sčítání"
Variantu pro určitý integrál pak nese prefix „UI - ".

TASK_CATEGORIES — podmnožina vah, kterou lze přiřadit jedné úloze
jako její primární téma (kategorie ze selectu v editoru úlohy).
Začíná od „Algebraické výrazy" — tj. odřezává úvodních 16 čistě
skill-komponentových vah, které nejsou samostatnými „kategoriemi úloh".
"""

KNOWLEDGE_WEIGHTS = [
    # --- Algebraické a aritmetické skill-komponenty (1–16) ---
    "lineární",
    "kvadratická",
    "mocninná",
    "log",
    "exponenciální",
    "goniometrická",
    "Absolutní hodnota",
    "lomená lineární",
    "zlomky",
    "Aplikační",
    "vzorec",
    "vytýkání, krácení",
    "Roznásobení závorky - distributivní zákon",
    "výpočet rovnic",
    "výpočet nerovnic",
    "Derivování",

    # --- Kategorie úloh (17–67) ---
    "Algebraické výrazy",
    "Elementární funce",
    "Rovnice",
    "Nerovnice",
    "Soustavy rovnic - dosazovací a sčítací metoda",
    "Funkce",
    "Definiční obor",
    "Aritmetika funkcí",
    "Skládání/rozkládání funkcí",
    "Sudá/lichá",
    "Inverzní funkce",
    "Tečna ke grafu",
    "Asymptota",
    "Monotónie, Určování Extrémů",
    "Absolutní extrémy na intervalu",
    "Určování lokálních extrémů",
    "Konvexnost/konkávnost",
    "Spojitost",
    "Bolzanova věta",
    "Limita",
    "VOAL (dosazení)",
    "LVL (krácení)",
    "S odmocninou",
    "Vytknutí nejvyšší mocniny",
    "Jednostranné limity",
    "Typová limita",
    "Lhopitalovo pravidlo",
    "Derivace",
    "Derivace — Sčítání",
    "Součin",
    "Podíl",
    "Složená funkce",
    "Diferenciál",
    "Taylorův polynom",
    "Derivace vyšších rádu",
    "Průběh funkce",
    "Primitivní funkce",
    "Prim. funkce — Sčítání",
    "Per partes",
    "1.věta o sub",
    "2.věta o sub",
    "Parciální zlomky",
    "Určitý integrál",
    "UI - Sčítání",
    "Roztrhnutí integrálu na dva",
    "UI - Per partes",
    "UI - 1.věta o sub",
    "UI - 2.věta o sub",
    "UI - Parciální zlomky",
    "Nevlastní integrál",
    "Obsah plochy",
]

# Subset začínající od indexu 16 (= „Algebraické výrazy") — kategorie úloh.
TASK_CATEGORIES = KNOWLEDGE_WEIGHTS[16:]


# Sanity check při importu (rozdíl mezi 67 vahami a 51 kategoriemi).
assert len(KNOWLEDGE_WEIGHTS) == 67, f"Očekáváno 67 vah, je {len(KNOWLEDGE_WEIGHTS)}"
assert len(TASK_CATEGORIES) == 51, f"Očekáváno 51 kategorií, je {len(TASK_CATEGORIES)}"
assert len(set(KNOWLEDGE_WEIGHTS)) == len(KNOWLEDGE_WEIGHTS), "Duplicitní názvy vah!"
