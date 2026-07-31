"""
Cvičení 11 — Diferenciál funkce, Taylorův a Maclaurinův polynom.
"""

TASKS = [
    # --------------------- 3 negace ---------------------
    {
        "task_id": "cv11_01",
        "content_latex": (
            r"Nechť $\mathbf{M} \subseteq \mathbb{R}.$ Formulujte negaci výroku: "
            r"\textit{Funkce } $f$ \textit{ je klesající na } $\mathbf{M}$ \textit{ právě tehdy, když "
            r"pro každé } $x_1, x_2 \in \mathbf{M}$ \textit{ platí: je-li } $x_1 < x_2,$ \textit{ pak } "
            r"$f(x_1) > f(x_2).$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$f$ není klesající nebo existují $x_1, x_2 \in \mathbf{M},\ x_1 < x_2$ s $f(x_1) \le f(x_2),$ a opačně."},
                {"key": "b", "label_latex": r"Pro každé $x_1 < x_2$ platí $f(x_1) \le f(x_2).$"},
                {"key": "c", "label_latex": r"$f$ je klesající a existují $x_1 < x_2$ s $f(x_1) = f(x_2).$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Monotonie"],
    },
    {
        "task_id": "cv11_02",
        "content_latex": (
            r"Formulujte negaci distributivního zákona: "
            r"\textit{Pro každou trojici } $x, y, z \in \mathbb{R}$ \textit{ platí } "
            r"$x \cdot (y + z) = x \cdot y + x \cdot z.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje trojice $x, y, z$ taková, že $x \cdot (y + z) \ne x \cdot y + x \cdot z.$"},
                {"key": "b", "label_latex": r"Pro každou trojici platí $x \cdot (y + z) \ne x \cdot y + x \cdot z.$"},
                {"key": "c", "label_latex": r"Existuje trojice taková, že $x \cdot y \ne y \cdot x.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv11_03",
        "content_latex": (
            r"Negujte trichotomii: \textit{Pro každou dvojici } $x, y \in \mathbb{R}$ \textit{ platí: } "
            r"$x > y$ \textit{ nebo } $x < y$ \textit{ nebo } $x = y.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje dvojice $x, y$ taková, že $x \le y$ a $x \ge y$ a $x \ne y.$"},
                {"key": "b", "label_latex": r"Pro každou dvojici platí $x = y.$"},
                {"key": "c", "label_latex": r"Existuje dvojice taková, že $x \ne y$ a $x = y.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků"],
    },

    # --------------------- 3 podul: diferenciál — odvození aproximace ---------------------
    {
        "task_id": "cv11_04",
        "content_latex": (
            r"Pomocí diferenciálu ukažte, že pro $h \to 0$ platí "
            r"$(1 + h)^\alpha \approx 1 + \alpha h$, kde $\alpha \in \mathbb{R}$. "
            r"Uveďte derivaci $f'$ v bodě $1$ a hodnotu diferenciálu $df(1, h)$."
        ),
        "results": [
            {"key": "fprime", "label_latex": r"f'(1) = ",    "type": "mathlive", "expected": r"\alpha"},
            {"key": "df",     "label_latex": r"df(1, h) = ", "type": "mathlive", "expected": r"\alpha h"},
        ],
        "cognitive_load": "D", "graph_vector": ["Diferenciál"],
    },
    {
        "task_id": "cv11_05",
        "content_latex": (
            r"Pomocí diferenciálu ukažte, že pro $h \to 0$ platí "
            r"$\sqrt{a + h} \approx \sqrt{a} + \dfrac{h}{2\sqrt{a}}$, kde $a > 0$. "
            r"Uveďte derivaci v bodě $a$ a hodnotu diferenciálu $df(a, h)$."
        ),
        "results": [
            {"key": "fprime", "label_latex": r"f'(a) = ",    "type": "mathlive", "expected": r"\frac{1}{2\sqrt{a}}"},
            {"key": "df",     "label_latex": r"df(a, h) = ", "type": "mathlive", "expected": r"\frac{h}{2\sqrt{a}}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Diferenciál"],
    },
    {
        "task_id": "cv11_06",
        "content_latex": (
            r"Pomocí diferenciálu ukažte, že pro $h \to 0$ platí "
            r"$\sqrt[3]{a + h} \approx \sqrt[3]{a} + \dfrac{h}{3\sqrt[3]{a^2}}$, kde $a > 0$. "
            r"Uveďte derivaci v bodě $a$ a hodnotu diferenciálu $df(a, h)$."
        ),
        "results": [
            {"key": "fprime", "label_latex": r"f'(a) = ",    "type": "mathlive", "expected": r"\frac{1}{3 a^{2/3}}"},
            {"key": "df",     "label_latex": r"df(a, h) = ", "type": "mathlive", "expected": r"\frac{h}{3 a^{2/3}}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Diferenciál"],
    },

    # --------------------- 7 podul: přibližná hodnota pomocí diferenciálu ---------------------
    {"task_id": "cv11_07",  "content_latex":r"Pomocí diferenciálu určete přibližně $\sqrt[3]{26{,}19}$.",
     "results":[{"key":"v","label_latex":r"\approx ","type":"decimal","expected":2.97,"tolerance":0.01}],
     "cognitive_load":"C","graph_vector":["Diferenciál"]},
    {"task_id": "cv11_08",  "content_latex":r"Pomocí diferenciálu určete přibližně $\sqrt[4]{16{,}64}$.",
     "results":[{"key":"v","label_latex":r"\approx ","type":"decimal","expected":2.02,"tolerance":0.01}],
     "cognitive_load":"C","graph_vector":["Diferenciál"]},
    {"task_id": "cv11_09",  "content_latex":r"Pomocí diferenciálu určete přibližně $\sqrt{8{,}76}$.",
     "results":[{"key":"v","label_latex":r"\approx ","type":"decimal","expected":2.96,"tolerance":0.01}],
     "cognitive_load":"C","graph_vector":["Diferenciál"]},
    {"task_id":"cv11_10", "content_latex":r"Pomocí diferenciálu určete přibližně $\sqrt{99{,}8}$.",
     "results":[{"key":"v","label_latex":r"\approx ","type":"decimal","expected":9.99,"tolerance":0.01}],
     "cognitive_load":"C","graph_vector":["Diferenciál"]},
    {"task_id":"cv11_11", "content_latex":r"Pomocí diferenciálu určete přibližně $\ln 0{,}9$.",
     "results":[{"key":"v","label_latex":r"\approx ","type":"decimal","expected":-0.1,"tolerance":0.005}],
     "cognitive_load":"C","graph_vector":["Diferenciál"]},
    {"task_id":"cv11_12", "content_latex":r"Pomocí diferenciálu určete přibližně $\log 10{,}21$.",
     "results":[{"key":"v","label_latex":r"\approx ","type":"decimal","expected":1.0091,"tolerance":0.001}],
     "cognitive_load":"D","graph_vector":["Diferenciál"]},
    {"task_id":"cv11_13", "content_latex":r"Pomocí diferenciálu určete přibližně $\sqrt[5]{33}$.",
     "results":[{"key":"v","label_latex":r"\approx ","type":"decimal","expected":2.0125,"tolerance":0.001}],
     "cognitive_load":"C","graph_vector":["Diferenciál"]},

    # --------------------- 3 aplikační (chyba měření) ---------------------
    {
        "task_id": "cv11_14",
        "content_latex": (
            r"\textbf{Čtverec.} Strana čtverce má délku 21 cm s možnou chybou 0,05 cm. "
            r"Pomocí diferenciálu odhadněte chybu výpočtu plošného obsahu $S$ čtverce (cm$^2$)."
        ),
        "results": [
            {"key": "vzorec", "label_latex": r"S = ",          "type": "mathlive", "expected": r"x^2"},
            {"key": "chyba",  "label_latex": r"dS \approx ",   "type": "decimal", "expected": 2.1, "tolerance": 0.05},
        ],
        "cognitive_load": "C", "graph_vector": ["Diferenciál", "Aplikace"],
    },
    {
        "task_id": "cv11_15",
        "content_latex": (
            r"\textbf{Koule.} Poloměr koule je 10 cm s možnou chybou 0,05 cm. "
            r"Pomocí diferenciálu odhadněte relativní chybu výpočtu objemu $V$ koule (v \%)."
        ),
        "results": [
            {"key": "vzorec",        "label_latex": r"V = ",                       "type": "mathlive", "expected": r"\frac{4}{3}\pi r^3"},
            {"key": "rel_chyba_pct", "label_latex": r"\frac{dV}{V} \cdot 100\% = ", "type": "decimal",  "expected": 1.5, "tolerance": 0.05},
        ],
        "cognitive_load": "D", "graph_vector": ["Diferenciál", "Aplikace"],
    },
    {
        "task_id": "cv11_16",
        "content_latex": (
            r"\textbf{Krychle.} Hrana krychle má délku 30 cm s možnou chybou 0,1 cm. "
            r"Pomocí diferenciálu odhadněte chybu i relativní chybu výpočtu objemu $V$ krychle."
        ),
        "results": [
            {"key": "vzorec",         "label_latex": r"V = ",                        "type": "mathlive", "expected": r"x^3"},
            {"key": "chyba",          "label_latex": r"dV \approx \text{ (cm}^3)",   "type": "decimal",  "expected": 270, "tolerance": 1},
            {"key": "rel_chyba_pct",  "label_latex": r"\frac{dV}{V} \cdot 100\% = ", "type": "decimal",  "expected": 1.0, "tolerance": 0.05},
        ],
        "cognitive_load": "D", "graph_vector": ["Diferenciál", "Aplikace"],
    },

    # --------------------- 8 podul: Maclaurin ---------------------
    {"task_id":"cv11_17",
     "content_latex":r"Určete Maclaurinův polynom řádu $n = 5$ funkce $f(x) = (1 - x)^{-2}$.",
     "results":[{"key":"T","label_latex":r"T_5(x) = ","type":"mathlive",
                 "expected":r"1 + 2x + 3x^2 + 4x^3 + 5x^4 + 6x^5"}],
     "cognitive_load":"D","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_18",
     "content_latex":r"Určete Maclaurinův polynom řádu $n = 2$ funkce $f(x) = e^{-x^2}$.",
     "results":[{"key":"T","label_latex":r"T_2(x) = ","type":"mathlive",
                 "expected":r"1 - x^2"}],
     "cognitive_load":"C","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_19",
     "content_latex":r"Určete Maclaurinův polynom řádu $n = 3$ funkce $f(x) = \tan x$.",
     "results":[{"key":"T","label_latex":r"T_3(x) = ","type":"mathlive",
                 "expected":r"x + \frac{x^3}{3}"}],
     "cognitive_load":"D","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_20",
     "content_latex":r"Určete Maclaurinův polynom řádu $n = 5$ funkce $f(x) = \dfrac{1}{x + 2}$.",
     "results":[{"key":"T","label_latex":r"T_5(x) = ","type":"mathlive",
                 "expected":r"\frac{1}{2} - \frac{x}{4} + \frac{x^2}{8} - \frac{x^3}{16} + \frac{x^4}{32} - \frac{x^5}{64}"}],
     "cognitive_load":"D","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_21",
     "content_latex":r"Určete Maclaurinův polynom řádu $n = 3$ funkce $f(x) = \arctan x$.",
     "results":[{"key":"T","label_latex":r"T_3(x) = ","type":"mathlive",
                 "expected":r"x - \frac{x^3}{3}"}],
     "cognitive_load":"D","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_22",
     "content_latex":r"Určete Maclaurinův polynom řádu $n = 4$ funkce $f(x) = \ln(1 + x)$.",
     "results":[{"key":"T","label_latex":r"T_4(x) = ","type":"mathlive",
                 "expected":r"x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4}"}],
     "cognitive_load":"C","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_23",
     "content_latex":r"Určete Maclaurinův polynom řádu $n = 4$ funkce $f(x) = \ln(1 - x)$.",
     "results":[{"key":"T","label_latex":r"T_4(x) = ","type":"mathlive",
                 "expected":r"-x - \frac{x^2}{2} - \frac{x^3}{3} - \frac{x^4}{4}"}],
     "cognitive_load":"C","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_24",
     "content_latex":(r"Určete Maclaurinův polynom řádu $n = 4$ funkce $f(x) = \ln\dfrac{1 + x}{1 - x}$ "
                      r"(použijte vlastnost logaritmu a předchozí dva polynomy)."),
     "results":[{"key":"T","label_latex":r"T_4(x) = ","type":"mathlive",
                 "expected":r"2x + \frac{2x^3}{3}"}],
     "cognitive_load":"D","graph_vector":["Taylorův polynom"]},

    # --------------------- 3 podul: Taylor v bodě a ---------------------
    {"task_id":"cv11_25",
     "content_latex":r"Určete Taylorův polynom řádu $n = 3$ funkce $f(x) = \dfrac{1}{x}$ v bodě $a = 1$.",
     "results":[{"key":"T","label_latex":r"T_3(x) = ","type":"mathlive",
                 "expected":r"1 - (x - 1) + (x - 1)^2 - (x - 1)^3"}],
     "cognitive_load":"D","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_26",
     "content_latex":r"Určete Taylorův polynom řádu $n = 5$ funkce $f(x) = \ln x$ v bodě $a = 1$.",
     "results":[{"key":"T","label_latex":r"T_5(x) = ","type":"mathlive",
                 "expected":r"(x - 1) - \frac{(x - 1)^2}{2} + \frac{(x - 1)^3}{3} - \frac{(x - 1)^4}{4} + \frac{(x - 1)^5}{5}"}],
     "cognitive_load":"D","graph_vector":["Taylorův polynom"]},
    {"task_id":"cv11_27",
     "content_latex":r"Určete Taylorův polynom řádu $n = 5$ funkce $f(x) = \sqrt{x}$ v bodě $a = 1$.",
     "results":[{"key":"T","label_latex":r"T_5(x) = ","type":"mathlive",
                 "expected":r"1 + \frac{x - 1}{2} - \frac{(x - 1)^2}{8} + \frac{(x - 1)^3}{16} - \frac{5(x - 1)^4}{128} + \frac{7(x - 1)^5}{256}"}],
     "cognitive_load":"E","graph_vector":["Taylorův polynom"]},
]
