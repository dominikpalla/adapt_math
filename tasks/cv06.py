"""
Cvičení 6 — Spojitost funkce.
"""


def _neg(idx, content, opts, cl="C"):
    """Negace s 3 MC možnostmi (první je správná = klíč 'a')."""
    return {
        "task_id": f"cv06_{idx}",
        "content_latex": content,
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [{"key": k, "label_latex": v} for k, v in opts],
            "expected": "a",
        }],
        "cognitive_load": cl, "graph_vector": ["Negace výroků", "Spojitost"],
    }


TASKS = [
    # --------------------- 3 negace ---------------------
    _neg(1,
        r"Formulujte negaci výroku: \textit{Je-li } $f: \mathbb{R} \to \mathbb{R}$ \textit{ spojitá "
        r"na intervalu } $\mathbf{I},$ \textit{ pak } $f(\mathbf{I})$ \textit{ je interval nebo "
        r"jednoprvková množina.}",
        [("a", r"Existuje spojitá $f: \mathbb{R} \to \mathbb{R}$ a interval $\mathbf{I}$ takové, že $f(\mathbf{I})$ není interval ani jednoprvková množina."),
         ("b", r"Existuje spojitá $f$ a interval $\mathbf{I}$ takové, že $f(\mathbf{I})$ je dvouprvková množina."),
         ("c", r"Je-li $f$ spojitá na $\mathbf{I},$ pak $f(\mathbf{I})$ není interval ani jednoprvková množina.")],
        "D"),
    _neg(2,
        r"Formulujte negaci výroku: \textit{Je-li } $f: \mathbb{R} \to \mathbb{R}$ \textit{ spojitá "
        r"na } $[a, b]$ \textit{ taková, že } $f(a) \cdot f(b) < 0,$ \textit{ pak existuje } "
        r"$c \in (a, b)$ \textit{ takové, že } $f(c) = 0.$",
        [("a", r"Existuje spojitá $f$ na $[a, b]$ taková, že $f(a) \cdot f(b) < 0,$ a pro každé $c \in (a, b)$ je $f(c) \ne 0.$"),
         ("b", r"Existuje spojitá $f$ na $[a, b]$ taková, že $f(a) \cdot f(b) > 0,$ a existuje $c \in (a, b)$ s $f(c) = 0.$"),
         ("c", r"Pro každou spojitou $f$ na $[a, b]$ a každý bod $c \in (a, b)$ platí $f(c) \ne 0.$")],
        "D"),
    _neg(3,
        r"Formulujte negaci výroku: \textit{Je-li } $f$ \textit{ spojitá na } $(a, b),$ "
        r"\textit{ nemá v něm nulový bod a pro nějaké } $c \in (a, b)$ \textit{ je } $f(c) > 0,$ "
        r"\textit{ pak pro každé } $x \in (a, b)$ \textit{ je } $f(x) > 0.$",
        [("a", r"Existuje spojitá $f$ na $(a, b)$ bez nulového bodu, pro některé $c \in (a, b)$ je $f(c) > 0$ a existuje $x \in (a, b)$ s $f(x) \le 0.$"),
         ("b", r"Existuje spojitá $f$ na $(a, b)$ s nulovým bodem a $f(c) > 0,$ ale $f(x) \le 0$ pro jiné $x.$"),
         ("c", r"Pro každou spojitou $f$ bez nulového bodu platí: pokud $f(c) > 0,$ pak $f(x) < 0$ pro některé $x.$")],
        "E"),

    # --------------------- 7 podul: spojitost po částech ---------------------
    {
        "task_id": "cv06_4",
        "content_latex": (
            r"Rozhodněte, zda je funkce $f(x) = \begin{cases} x^2 & x < 1 \\ \sqrt{x} & x \ge 1 \end{cases}$ "
            r"spojitá na $\mathbb{R}$ a uveďte hodnotu limity v bodě nespojitosti (pokud existuje)."
        ),
        "results": [
            {"key": "spojita", "label_latex": r"\text{Spojitá na }\mathbb{R}:\ ", "type": "multiple_choice",
             "options": [{"key":"ano","label_latex":r"\text{ano}"},{"key":"ne","label_latex":r"\text{ne}"}],
             "expected": "ano"},
            {"key": "limita", "label_latex": r"\lim_{x \to 1} f(x) = ", "type": "decimal",
             "expected": 1, "tolerance": 0.001},
        ],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_5",
        "content_latex": (
            r"Rozhodněte, zda je funkce $f(x) = \begin{cases} \sin x & x < \pi/4 \\ \cos x & x \ge \pi/4 \end{cases}$ "
            r"spojitá v bodě $\pi/4$."
        ),
        "results": [
            {"key": "spojita", "label_latex": r"\text{Spojitá v }\pi/4:\ ", "type": "multiple_choice",
             "options": [{"key":"ano","label_latex":r"\text{ano}"},{"key":"ne","label_latex":r"\text{ne}"}],
             "expected": "ano"},
            {"key": "limita", "label_latex": r"\lim_{x \to \pi/4} f(x) = ", "type": "mathlive",
             "expected": r"\frac{\sqrt{2}}{2}"},
        ],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_6",
        "content_latex": (
            r"Je funkce $f(x) = \begin{cases} x^4 \sin(1/x) & x \ne 0 \\ 0 & x = 0 \end{cases}$ "
            r"spojitá v bodě $0$? Uveďte limitu."
        ),
        "results": [
            {"key": "spojita", "label_latex": r"\text{Spojitá v }0:\ ", "type": "multiple_choice",
             "options": [{"key":"ano","label_latex":r"\text{ano}"},{"key":"ne","label_latex":r"\text{ne}"}],
             "expected": "ano"},
            {"key": "limita", "label_latex": r"\lim_{x \to 0} f(x) = ", "type": "decimal",
             "expected": 0, "tolerance": 0.001},
        ],
        "cognitive_load": "D", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_7",
        "content_latex": (
            r"Funkce $f(x) = \begin{cases} \dfrac{x^2 - 4}{x - 2} & x \ne 2 \\ A & x = 2 \end{cases}$. "
            r"Pro jakou hodnotu $A$ je $f$ spojitá v bodě $2$?"
        ),
        "results": [{"key": "A", "label_latex": r"A = ", "type": "decimal",
                     "expected": 4, "tolerance": 0.001}],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_8",
        "content_latex": (
            r"Funkce $f(x) = \begin{cases} \dfrac{1}{(1+x)^2} & x \ne -1 \\ A & x = -1 \end{cases}$. "
            r"Pro kterou hodnotu $A$ je $f$ spojitá v bodě $-1$?"
        ),
        "results": [{
            "key": "A", "label_latex": r"\text{Hodnota }A:\ ", "type": "multiple_choice",
            "options": [
                {"key": "ne_inf", "label_latex": r"\text{Žádná — limita je } +\infty"},
                {"key": "ne_neg", "label_latex": r"\text{Žádná — limita je } -\infty"},
                {"key": "nula",   "label_latex": r"A = 0"},
            ],
            "expected": "ne_inf",
        }],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_9",
        "content_latex": (
            r"Je funkce $f(x) = \begin{cases} e^{-1/x^2} & x \ne 0 \\ 0 & x = 0 \end{cases}$ "
            r"spojitá v bodě $0$? Uveďte limitu."
        ),
        "results": [
            {"key": "spojita", "label_latex": r"\text{Spojitá v }0:\ ", "type": "multiple_choice",
             "options": [{"key":"ano","label_latex":r"\text{ano}"},{"key":"ne","label_latex":r"\text{ne}"}],
             "expected": "ano"},
            {"key": "limita", "label_latex": r"\lim_{x \to 0} f(x) = ", "type": "decimal",
             "expected": 0, "tolerance": 0.001},
        ],
        "cognitive_load": "D", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_10",
        "content_latex": (
            r"Funkce $f(x) = \begin{cases} x \ln x^2 & x \ne 0 \\ A & x = 0 \end{cases}$. "
            r"Pro jakou hodnotu $A$ je $f$ spojitá v bodě $0$?"
        ),
        "results": [{"key": "A", "label_latex": r"A = ", "type": "decimal",
                     "expected": 0, "tolerance": 0.001}],
        "cognitive_load": "D", "graph_vector": ["Spojitost"],
    },

    # --------------------- 4 podul: nespojitost speciálních funkcí ---------------------
    {
        "task_id": "cv06_11",
        "content_latex": r"Kde je funkce $y = \operatorname{sign}(\sin x)$ nespojitá?",
        "results": [{
            "key": "nespoj", "label_latex": r"\text{Nespojitost: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"V bodech $x = k\pi,\ k \in \mathbb{Z}$ (skoková)."},
                {"key": "b", "label_latex": r"Pouze v bodě $x = 0.$"},
                {"key": "c", "label_latex": r"Funkce je spojitá na celém $\mathbb{R}.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_12",
        "content_latex": r"Kde je funkce $y = x - [x]$ (zlomková část) nespojitá?",
        "results": [{
            "key": "nespoj", "label_latex": r"\text{Nespojitost: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Pro $x \in \mathbb{Z}$ je nespojitá zleva."},
                {"key": "b", "label_latex": r"Pro $x \in \mathbb{Z}$ je nespojitá zprava."},
                {"key": "c", "label_latex": r"Funkce je spojitá všude."},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_13",
        "content_latex": r"Kde je funkce $y = x \cdot [x]$ nespojitá?",
        "results": [{
            "key": "nespoj", "label_latex": r"\text{Nespojitost: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Pro $x \in \mathbb{Z} \setminus \{0\}$ je nespojitá zleva."},
                {"key": "b", "label_latex": r"Pro $x \in \mathbb{Z}$ je nespojitá zprava."},
                {"key": "c", "label_latex": r"Funkce je spojitá všude."},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_14",
        "content_latex": r"Kde je funkce $y = \left[\dfrac{1}{x}\right]$ nespojitá?",
        "results": [{
            "key": "nespoj", "label_latex": r"\text{Nespojitost: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"V bodech $x = 1/k,\ k \in \mathbb{Z} \setminus \{0\}$ (nespojitá zprava)."},
                {"key": "b", "label_latex": r"V bodech $x = 1/k$ je nespojitá zleva."},
                {"key": "c", "label_latex": r"Pouze v $x = 0.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Spojitost"],
    },

    # --------------------- 3 podul: dodefinujte aby byla spojitá ---------------------
    {
        "task_id": "cv06_15",
        "content_latex": r"Funkci $f(x) = \dfrac{x^2 - x}{x - 1}$ dodefinujte tak, aby byla spojitá v bodě $a = 1$.",
        "results": [{"key": "f1", "label_latex": r"f(1) = ", "type": "decimal",
                     "expected": 1, "tolerance": 0.001}],
        "cognitive_load": "B", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_16",
        "content_latex": r"Funkci $f(x) = \dfrac{x^2 - 9}{x^2 + 2x - 3}$ dodefinujte tak, aby byla spojitá v bodě $a = -3$.",
        "results": [{"key": "fm3", "label_latex": r"f(-3) = ", "type": "mathlive",
                     "expected": r"\frac{3}{2}"}],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_17",
        "content_latex": r"Funkci $f(x) = \dfrac{1 - \sqrt{1 - x^2}}{x}$ dodefinujte tak, aby byla spojitá v bodě $a = 0$.",
        "results": [{"key": "f0", "label_latex": r"f(0) = ", "type": "decimal",
                     "expected": 0, "tolerance": 0.001}],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },

    # --------------------- 2 úlohy s parametrem ---------------------
    {
        "task_id": "cv06_18",
        "content_latex": (
            r"Pro které hodnoty parametru $c \in \mathbb{R}$ je funkce "
            r"$f(x) = \begin{cases} cx^2 + 2x & x < 2 \\ x^3 - cx & x \ge 2 \end{cases}$ spojitá na $\mathbb{R}$?"
        ),
        "results": [{"key": "c", "label_latex": r"c = ", "type": "mathlive",
                     "expected": r"\frac{2}{3}"}],
        "cognitive_load": "C", "graph_vector": ["Spojitost"],
    },
    {
        "task_id": "cv06_19",
        "content_latex": (
            r"Pro které hodnoty $a, b \in \mathbb{R}$ je funkce "
            r"$f(x) = \begin{cases} \dfrac{x^2 - 4}{x - 2} & x < 2 \\ ax^2 - bx + 3 & 2 < x < 3 \\ 2x - a + b & x \ge 3 \end{cases}$ spojitá na $\mathbb{R}$?"
        ),
        "results": [
            {"key": "a", "label_latex": r"a = ", "type": "mathlive", "expected": r"\frac{1}{2}"},
            {"key": "b", "label_latex": r"b = ", "type": "mathlive", "expected": r"\frac{1}{2}"},
        ],
        "cognitive_load": "E", "graph_vector": ["Spojitost"],
    },

    # --------------------- 4 podul: Bolzano (kořen v intervalu) ---------------------
    *[
        {
            "task_id": f"cv06_{20+i}",
            "content_latex": text,
            "results": [{
                "key": "exist", "label_latex": r"\text{Kořen v intervalu: }", "type": "multiple_choice",
                "options": [
                    {"key": "ano", "label_latex": r"\text{ano (existuje)}"},
                    {"key": "ne",  "label_latex": r"\text{ne}"},
                    {"key": "neoblastní", "label_latex": r"\text{nelze rozhodnout z Bolzanovy věty}"},
                ],
                "expected": "ano",
            }],
            "cognitive_load": cl, "graph_vector": ["Spojitost", "Bolzano"],
        }
        for i, (text, cl) in enumerate([
            (r"Pomocí Bolzanovy věty rozhodněte, zda rovnice $x = \cos x$ má kořen v intervalu $[0, \pi/2]$.", "C"),
            (r"Pomocí Bolzanovy věty rozhodněte, zda rovnice $x^4 + x - 3 = 0$ má kořen v intervalu $[1, 2]$.", "B"),
            (r"Pomocí Bolzanovy věty rozhodněte, zda rovnice $\sqrt[3]{x} = 1 - x$ má kořen v intervalu $[0, 1]$.", "B"),
            (r"Pomocí Bolzanovy věty rozhodněte, zda rovnice $\tan x = 2x$ má netriviální kořen v intervalu $(0, \pi/2)$.", "C"),
        ])
    ],
]
