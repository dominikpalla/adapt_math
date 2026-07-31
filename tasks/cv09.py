"""
Cvičení 9 — Vyšetřování první derivace, lokální extrémy.

Pro úlohy „určete intervaly monotonie a lokální extrémy" používám
multiple_choice — vyšetření průběhu má textovou strukturu, kterou
MathLive Compute Engine neporovná. Studentovi nabídnu 3 varianty
se správnou + 2 typickými chybami (prohození roste/klesá, posun bodů).
"""


def _mono(idx, fn, correct, distr_b, distr_c, cl="C"):
    return {
        "task_id": f"cv09_{idx:02d}",
        "content_latex": (
            r"Určete intervaly, na kterých je funkce $f$ ryze monotonní, "
            r"a určete lokální extrémy: $f(x) = " + fn + "$."
        ),
        "results": [{
            "key": "vysetreni", "label_latex": r"\text{Průběh: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": correct},
                {"key": "b", "label_latex": distr_b},
                {"key": "c", "label_latex": distr_c},
            ],
            "expected": "a",
        }],
        "cognitive_load": cl, "graph_vector": ["Monotonie", "Lokální extrémy"],
    }


TASKS = [
    # --------------------- 3 negace ---------------------
    {
        "task_id": "cv09_01",
        "content_latex": (
            r"Nechť $f$ je spojitá na $\mathbf{I}$ a má v každém bodě derivaci. "
            r"Formulujte negaci výroku: \textit{Je-li } $f'(x) > 0$ \textit{ pro každý vnitřní bod "
            r"intervalu } $\mathbf{I},$ \textit{ je } $f$ \textit{ rostoucí na } $\mathbf{I}.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $f$ spojitá na $\mathbf{I}$ s derivací, $f'(x) > 0$ uvnitř, a přitom $f$ není rostoucí na $\mathbf{I}.$"},
                {"key": "b", "label_latex": r"Existuje $f$ taková, že $f'(x) \le 0$ pro nějaký vnitřní bod a přesto $f$ je rostoucí."},
                {"key": "c", "label_latex": r"Pokud $f'(x) > 0$ uvnitř $\mathbf{I},$ pak $f$ není rostoucí na $\mathbf{I}.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Derivace"],
    },
    {
        "task_id": "cv09_02",
        "content_latex": (
            r"Formulujte negaci výroku: \textit{Je-li } $f'(x) < 0$ \textit{ pro každý vnitřní bod "
            r"intervalu } $\mathbf{I},$ \textit{ je } $f$ \textit{ klesající na } $\mathbf{I}.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $f$ s $f'(x) < 0$ uvnitř $\mathbf{I},$ ale $f$ není klesající na $\mathbf{I}.$"},
                {"key": "b", "label_latex": r"Existuje $f$ s $f'(x) \ge 0$ pro nějaký vnitřní bod, přesto $f$ je klesající."},
                {"key": "c", "label_latex": r"Pokud $f'(x) < 0,$ pak $f$ není klesající."},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Derivace"],
    },
    {
        "task_id": "cv09_03",
        "content_latex": (
            r"Formulujte negaci výroku: \textit{Je-li } $f'(x) = 0$ \textit{ pro každý vnitřní bod "
            r"intervalu } $\mathbf{I},$ \textit{ je } $f$ \textit{ konstantní na } $\mathbf{I}.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $f$ s $f'(x) = 0$ uvnitř $\mathbf{I},$ ale $f$ není konstantní na $\mathbf{I}.$"},
                {"key": "b", "label_latex": r"Existuje $f$ s $f'(x) \ne 0$ pro některý bod a přesto $f$ konstantní."},
                {"key": "c", "label_latex": r"Pokud $f'(x) = 0,$ pak $f$ je rostoucí na $\mathbf{I}.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Derivace"],
    },

    # --------------------- 18 podul: monotonie + extrémy ---------------------
    _mono(4, r"2x^2 - \ln x",
          r"Klesá v $(0, \tfrac{1}{2}),$ roste v $(\tfrac{1}{2}, \infty);$ lokmin v $x = \tfrac{1}{2}.$",
          r"Roste v $(0, \tfrac{1}{2}),$ klesá v $(\tfrac{1}{2}, \infty);$ lokmax v $x = \tfrac{1}{2}.$",
          r"Roste v celém $D = (0, \infty);$ žádný extrém.", "C"),
    _mono(5, r"2x^3 - 6x^2 - 18x + 7",
          r"Roste v $(-\infty, -1) \cup (3, \infty),$ klesá v $(-1, 3);$ lokmax v $x = -1,$ lokmin v $x = 3.$",
          r"Klesá v $(-\infty, -1) \cup (3, \infty),$ roste v $(-1, 3);$ lokmin v $x = -1,$ lokmax v $x = 3.$",
          r"Roste v $(-\infty, 0) \cup (2, \infty),$ klesá v $(0, 2);$ lokmax v $x = 0,$ lokmin v $x = 2.$", "C"),
    _mono(6, r"\frac{x^2 - 2x + 1}{x^2 + 1}",
          r"Roste v $(-\infty, -1) \cup (1, \infty),$ klesá v $(-1, 1);$ lokmax v $x = -1,$ lokmin v $x = 1.$",
          r"Klesá v $(-\infty, -1) \cup (1, \infty),$ roste v $(-1, 1);$ lokmin v $x = -1,$ lokmax v $x = 1.$",
          r"Roste na celém $\mathbb{R};$ žádné extrémy.", "D"),
    _mono(7, r"x^2 e^x",
          r"Roste v $(-\infty, -2) \cup (0, \infty),$ klesá v $(-2, 0);$ lokmax v $x = -2,$ lokmin v $x = 0.$",
          r"Klesá v $(-\infty, -2) \cup (0, \infty),$ roste v $(-2, 0);$ lokmin v $x = -2,$ lokmax v $x = 0.$",
          r"Roste na celém $\mathbb{R};$ žádné extrémy.", "C"),
    _mono(8, r"x^2 e^{-x}",
          r"Klesá v $(-\infty, 0) \cup (2, \infty),$ roste v $(0, 2);$ lokmin v $x = 0,$ lokmax v $x = 2.$",
          r"Roste v $(-\infty, 0) \cup (2, \infty),$ klesá v $(0, 2);$ lokmax v $x = 0,$ lokmin v $x = 2.$",
          r"Klesá v $(-\infty, 1),$ roste v $(1, \infty);$ lokmin v $x = 1.$", "C"),
    _mono(9, r"x e^{-x^2}",
          r"Klesá v $(-\infty, -\tfrac{1}{\sqrt{2}}) \cup (\tfrac{1}{\sqrt{2}}, \infty),$ roste v $(-\tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}});$ lokmin v $x = -\tfrac{1}{\sqrt{2}},$ lokmax v $x = \tfrac{1}{\sqrt{2}}.$",
          r"Roste v $(-\infty, -\tfrac{1}{\sqrt{2}}) \cup (\tfrac{1}{\sqrt{2}}, \infty),$ klesá uvnitř.",
          r"Roste na celém $\mathbb{R};$ žádné extrémy.", "D"),
    _mono(10, r"\frac{x}{\ln x}",
          r"Klesá v $(0, 1) \cup (1, e),$ roste v $(e, \infty);$ lokmin v $x = e.$",
          r"Roste v $(0, 1) \cup (1, e),$ klesá v $(e, \infty);$ lokmax v $x = e.$",
          r"Klesá v $(0, 1),$ roste v $(1, \infty);$ lokmin v $x = 1.$", "D"),
    _mono(11, r"\frac{\ln x}{\sqrt{x}}",
          r"Roste v $(0, e^2),$ klesá v $(e^2, \infty);$ lokmax v $x = e^2.$",
          r"Klesá v $(0, e^2),$ roste v $(e^2, \infty);$ lokmin v $x = e^2.$",
          r"Roste v celém $(0, \infty);$ žádný extrém.", "C"),
    _mono(12, r"x^2 \ln x",
          r"Klesá v $(0, 1/\sqrt{e}),$ roste v $(1/\sqrt{e}, \infty);$ lokmin v $x = 1/\sqrt{e}.$",
          r"Roste v $(0, 1/\sqrt{e}),$ klesá v $(1/\sqrt{e}, \infty);$ lokmax v $x = 1/\sqrt{e}.$",
          r"Roste v celém $(0, \infty);$ žádný extrém.", "C"),
    _mono(13, r"x e^{1/x}",
          r"Roste v $(-\infty, 0) \cup (1, \infty),$ klesá v $(0, 1);$ lokmin v $x = 1.$",
          r"Klesá v $(-\infty, 0) \cup (1, \infty),$ roste v $(0, 1);$ lokmax v $x = 1.$",
          r"Roste na celém $\mathbb{R} \setminus \{0\};$ žádný extrém.", "D"),
    _mono(14, r"x^2 e^{x + 2}",
          r"Roste v $(-\infty, -2) \cup (0, \infty),$ klesá v $(-2, 0);$ lokmax v $x = -2,$ lokmin v $x = 0.$",
          r"Klesá v $(-\infty, -2) \cup (0, \infty),$ roste v $(-2, 0);$ lokmin v $x = -2,$ lokmax v $x = 0.$",
          r"Roste na celém $\mathbb{R};$ žádné extrémy.", "C"),
    _mono(15, r"x - \arctan x",
          r"Roste na celém $\mathbb{R};$ žádné lokální extrémy.",
          r"Klesá na celém $\mathbb{R};$ žádné extrémy.",
          r"Roste v $(-\infty, 0),$ klesá v $(0, \infty);$ lokmax v $x = 0.$", "C"),
    _mono(16, r"(x - 4)\sqrt[3]{x}",
          r"Klesá v $(-\infty, 1),$ roste v $(1, \infty);$ lokmin v $x = 1.$",
          r"Roste v $(-\infty, 1),$ klesá v $(1, \infty);$ lokmax v $x = 1.$",
          r"Roste na celém $\mathbb{R};$ žádný extrém.", "D"),
    _mono(17, r"(x - 2)^{2/3}(2x + 1)",
          r"Roste v $(-\infty, 1) \cup (2, \infty),$ klesá v $(1, 2);$ lokmax v $x = 1,$ lokmin v $x = 2.$",
          r"Klesá v $(-\infty, 1) \cup (2, \infty),$ roste v $(1, 2);$ lokmin v $x = 1,$ lokmax v $x = 2.$",
          r"Roste na celém $\mathbb{R};$ žádné extrémy.", "E"),
    _mono(18, r"\frac{x}{\ln^2 x}",
          r"Roste v $(0, 1) \cup (e^2, \infty),$ klesá v $(1, e^2);$ lokmin v $x = e^2.$",
          r"Klesá v $(0, 1) \cup (e^2, \infty),$ roste v $(1, e^2);$ lokmax v $x = e^2.$",
          r"Roste v celém $(0, \infty) \setminus \{1\};$ žádný extrém.", "D"),
    _mono(19, r"x(1 - \ln x)^2",
          r"Roste v $(0, 1/e) \cup (e, \infty),$ klesá v $(1/e, e);$ lokmax v $x = 1/e,$ lokmin v $x = e.$",
          r"Klesá v $(0, 1/e) \cup (e, \infty),$ roste v $(1/e, e);$ lokmin v $x = 1/e,$ lokmax v $x = e.$",
          r"Roste v celém $(0, \infty);$ žádný extrém.", "E"),
    _mono(20, r"x^3 e^{-x}",
          r"Roste v $(-\infty, 3),$ klesá v $(3, \infty);$ lokmax v $x = 3.$",
          r"Klesá v $(-\infty, 3),$ roste v $(3, \infty);$ lokmin v $x = 3.$",
          r"Roste na celém $\mathbb{R};$ žádný extrém.", "D"),
    _mono(21, r"(x + 2)^{2/3} + (x - 2)^{2/3}",
          r"Klesá v $(-\infty, -2) \cup (0, 2),$ roste v $(-2, 0) \cup (2, \infty);$ lokmin v $x = \pm 2,$ lokmax v $x = 0.$",
          r"Roste v $(-\infty, -2) \cup (0, 2),$ klesá v $(-2, 0) \cup (2, \infty);$ lokmax v $x = \pm 2,$ lokmin v $x = 0.$",
          r"Klesá na celém $\mathbb{R};$ žádný extrém.", "E"),

    # --------------------- 5 aplikačních úloh ---------------------
    {
        "task_id": "cv09_22",
        "content_latex": (
            r"\textbf{Ropovod.} "
            r"Na severním břehu řeky široké 2 km je rafinérie. Ropná nádrž je na jižním břehu, 6 km východně. "
            r"Náklady: 400 000 \$/km na severním břehu, 800 000 \$/km na dně řeky. "
            r"V kterém místě na severním břehu má být stanice, aby byly náklady minimální? "
            r"Uveďte vzdálenost (km) východně od rafinérie."
        ),
        "results": [{"key": "x", "label_latex": r"x \approx ", "type": "decimal",
                     "expected": 4.85, "tolerance": 0.05}],
        "cognitive_load": "E", "graph_vector": ["Aplikace", "Optimalizace"],
    },
    {
        "task_id": "cv09_23",
        "content_latex": (
            r"\textbf{Hajný do restaurace.} "
            r"Lesem prochází přímá cesta. 3 km jižně leží hájovna; 5 km východně (na cestě) restaurace. "
            r"Hajný jde lesem rychlostí 2 km/h, po cestě 4 km/h. Určete minimální dobu cesty."
        ),
        "results": [{
            "key": "t", "label_latex": r"t_{\min} = ", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$2\ \text{h}\ 32\ \text{min}$"},
                {"key": "b", "label_latex": r"$2\ \text{h}\ 15\ \text{min}$"},
                {"key": "c", "label_latex": r"$3\ \text{h}$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "E", "graph_vector": ["Aplikace", "Optimalizace"],
    },
    {
        "task_id": "cv09_24",
        "content_latex": (
            r"\textbf{Kruhové jezero.} Poloměr 3 km; po břehu rychlost 6 km/h, na pramici 3 km/h. "
            "Bod $A,$ cíl $C$ naproti. Určete maximální dobu cesty z $A$ do $C$ (strategie „co nejdéle spolu\") "
            r"a minimální dobu zpětné cesty chlapce."
        ),
        "results": [
            {"key": "t_max", "label_latex": r"t_{\max} = ", "type": "multiple_choice",
             "options": [
                 {"key": "a", "label_latex": r"$2\ \text{h}\ 15\ \text{min}$ (jen po břehu)"},
                 {"key": "b", "label_latex": r"$2\ \text{h}$"},
                 {"key": "c", "label_latex": r"$3\ \text{h}\ 14\ \text{min}$"},
             ], "expected": "a"},
            {"key": "t_min", "label_latex": r"t_{\min} = ", "type": "multiple_choice",
             "options": [
                 {"key": "a", "label_latex": r"$1\ \text{h}\ 34\ \text{min}$ (kombinace břeh + pramice)"},
                 {"key": "b", "label_latex": r"$2\ \text{h}$ (jen pramice přes střed)"},
                 {"key": "c", "label_latex": r"$1\ \text{h}\ 30\ \text{min}$"},
             ], "expected": "a"},
        ],
        "cognitive_load": "F", "graph_vector": ["Aplikace", "Optimalizace"],
    },
    {
        "task_id": "cv09_25",
        "content_latex": (
            r"\textbf{Plavba lodi.} Při rychlosti 10 km/h jsou náklady na plavbu 300 Kč/h a rostou úměrně třetí "
            r"mocnině rychlosti. Ostatní náklady 4 800 Kč/h. Při jaké rychlosti je 1 km plavby nejlevnější?"
        ),
        "results": [{"key": "v", "label_latex": r"v_{\min} = ", "type": "decimal",
                     "expected": 20, "tolerance": 0.5}],
        "cognitive_load": "E", "graph_vector": ["Aplikace", "Optimalizace"],
    },
    {
        "task_id": "cv09_26",
        "content_latex": (
            r"\textbf{Regulátory.} Roční spotřeba 120 ks, cena 1 800 Kč/ks, jízda do závodu 2 700 Kč. "
            r"Skladovací náklady 10\% z ceny uskladněných regulátorů. "
            r"Určete optimální počet ks na jízdu, počet jízd a minimální celkové roční náklady."
        ),
        "results": [
            {"key": "n",      "label_latex": r"\text{Počet ks na jízdu} = ", "type": "decimal", "expected": 60, "tolerance": 0.5},
            {"key": "jizdy",  "label_latex": r"\text{Počet jízd ročně} = ",  "type": "decimal", "expected": 2,  "tolerance": 0.1},
            {"key": "R",      "label_latex": r"R_{\min} = ",                 "type": "decimal", "expected": 226800, "tolerance": 50},
        ],
        "cognitive_load": "F", "graph_vector": ["Aplikace", "Optimalizace"],
    },
]
