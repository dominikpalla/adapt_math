"""
Cvičení 3 — Vlastnosti funkcí: rostoucí, klesající, sudá, lichá.
Polynomy, Hornerovo schéma, racionální funkce.
"""

TASKS = [
    # --------------------- 3 negace ---------------------
    {
        "task_id": "cv03_1",
        "content_latex": (
            r"Nechť $\mathbf{M} \subseteq \mathbb{R}.$ Formulujte negaci výroku: "
            r"\textit{Funkce } $f$ \textit{ je rostoucí na } $\mathbf{M}$ \textit{ právě tehdy, "
            r"když pro každé } $x_1, x_2 \in \mathbf{M}$ \textit{ platí: je-li } $x_1 < x_2,$ "
            r"\textit{ pak } $f(x_1) < f(x_2).$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$f$ není rostoucí na $\mathbf{M}$ nebo existují $x_1, x_2 \in \mathbf{M},\ x_1 < x_2,$ taková, že $f(x_1) \ge f(x_2),$ a opačně."},
                {"key": "b", "label_latex": r"$f$ je rostoucí na $\mathbf{M}$ a existují $x_1, x_2 \in \mathbf{M},\ x_1 < x_2,$ taková, že $f(x_1) > f(x_2).$"},
                {"key": "c", "label_latex": r"Pro každé $x_1, x_2 \in \mathbf{M}$ platí: je-li $x_1 < x_2,$ pak $f(x_1) \ge f(x_2).$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Monotonie"],
    },
    {
        "task_id": "cv03_2",
        "content_latex": (
            r"Nechť $\mathbf{M} \subseteq \mathbb{R}.$ Formulujte negaci výroku: "
            r"\textit{Funkce } $f$ \textit{ je klesající na } $\mathbf{M}$ \textit{ právě tehdy, "
            r"když pro každé } $x_1, x_2 \in \mathbf{M}$ \textit{ platí: je-li } $x_1 < x_2,$ "
            r"\textit{ pak } $f(x_1) > f(x_2).$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$f$ není klesající na $\mathbf{M}$ nebo existují $x_1, x_2 \in \mathbf{M},\ x_1 < x_2,$ taková, že $f(x_1) \le f(x_2),$ a opačně."},
                {"key": "b", "label_latex": r"$f$ je klesající a existují $x_1, x_2 \in \mathbf{M},\ x_1 < x_2,$ taková, že $f(x_1) < f(x_2).$"},
                {"key": "c", "label_latex": r"Pro každé $x_1, x_2 \in \mathbf{M}$ platí: je-li $x_1 < x_2,$ pak $f(x_1) \le f(x_2).$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Monotonie"],
    },
    {
        "task_id": "cv03_3",
        "content_latex": (
            r"Formulujte negaci výroku o antisymetrii uspořádání reálných čísel: "
            r"\textit{Pro každé } $x \in \mathbb{R}$ \textit{ a pro každé } $y \in \mathbb{R}$ "
            r"\textit{ platí: jestliže } $x \le y$ \textit{ a } $y \le x,$ \textit{ pak } $x = y.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existují $x, y \in \mathbb{R}$ taková, že $x \le y$ a $y \le x$ a zároveň $x \ne y.$"},
                {"key": "b", "label_latex": r"Pro každé $x, y \in \mathbb{R}$ platí: je-li $x \le y$ a $y \le x,$ pak $x \ne y.$"},
                {"key": "c", "label_latex": r"Existují $x, y \in \mathbb{R}$ taková, že $x > y$ nebo $y > x$ a $x = y.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },

    # --------------------- 3 iterace složené funkce ---------------------
    {
        "task_id": "cv03_4",
        "content_latex": (
            r"Jestliže $f_0: y = x^2$ a $f_{n+1} = f_0 \circ f_n,$ kde $n \in \mathbb{N}_0,$ "
            r"určete předpis pro funkci $f_n.$"
        ),
        "results": [{"key": "fn", "label_latex": r"f_n(x) = ", "type": "mathlive",
                     "expected": r"x^{2^{n+1}}"}],
        "cognitive_load": "D", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv03_5",
        "content_latex": (
            r"Jestliže $f_0: y = \dfrac{x}{x+1}$ a $f_{n+1} = f_0 \circ f_n,$ kde $n \in \mathbb{N}_0,$ "
            r"určete předpis pro funkci $f_n.$"
        ),
        "results": [{"key": "fn", "label_latex": r"f_n(x) = ", "type": "mathlive",
                     "expected": r"\frac{x}{(n+1)x + 1}"}],
        "cognitive_load": "E", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv03_6",
        "content_latex": (
            r"Jestliže $f_0: y = \dfrac{1}{2 - x}$ a $f_{n+1} = f_0 \circ f_n,$ kde $n \in \mathbb{N}_0,$ "
            r"určete předpis pro funkci $f_n.$"
        ),
        "results": [{"key": "fn", "label_latex": r"f_n(x) = ", "type": "mathlive",
                     "expected": r"\frac{n + 1 - nx}{n + 2 - (n+1)x}"}],
        "cognitive_load": "F", "graph_vector": ["Skládání funkcí"],
    },

    # --------------------- 10 podul: sudá/lichá/nic ---------------------
    *[
        {
            "task_id": f"cv03_{7+i}",
            "content_latex": "Rozhodněte, zda je funkce $f$ sudá, lichá nebo nemá ani jednu z těchto vlastností: $" + expr + "$.",
            "results": [{
                "key": "parita", "label_latex": r"\text{Vlastnost: }", "type": "multiple_choice",
                "options": [
                    {"key": "suda",  "label_latex": r"\text{sudá}"},
                    {"key": "licha", "label_latex": r"\text{lichá}"},
                    {"key": "nic",   "label_latex": r"\text{ani sudá, ani lichá}"},
                ],
                "expected": expected,
            }],
            "cognitive_load": cl,
            "graph_vector": ["Sudá/lichá funkce"],
        }
        for i, (expr, expected, cl) in enumerate([
            (r"f(x) = \tfrac{1}{2}(e^x + e^{-x})",        "suda",  "B"),
            (r"f(x) = \log\tfrac{2 + x}{2 - x}",          "licha", "C"),
            (r"f(x) = \sqrt{1 + x^2} - \sqrt{1 - x^2}",   "suda",  "C"),
            (r"f(x) = \sqrt[3]{(1 - 2x)^2}",              "nic",   "C"),
            (r"f(x) = \tfrac{|x|}{x}",                    "licha", "B"),
            (r"f(x) = \tfrac{|x-1|}{x-1}",                "nic",   "C"),
            (r"f(x) = x \ln|x|",                          "licha", "C"),
            (r"f(x) = \tfrac{\sin x}{x}",                 "suda",  "B"),
            (r"f(x) = \ln(x + \sqrt{1 + x^2})",           "licha", "D"),
            (r"f(x) = x \cdot \tfrac{a^x + 1}{a^x - 1}",  "suda",  "D"),
        ])
    ],

    # --------------------- 4 podul: monotonie f∘g ---------------------
    *[
        {
            "task_id": f"cv03_{17+i}",
            "content_latex": text,
            "results": [{
                "key": "mono", "label_latex": r"f \circ g \text{ je }", "type": "multiple_choice",
                "options": [
                    {"key": "rost", "label_latex": r"\text{rostoucí}"},
                    {"key": "kles", "label_latex": r"\text{klesající}"},
                    {"key": "nic",  "label_latex": r"\text{nelze rozhodnout obecně}"},
                ],
                "expected": expected,
            }],
            "cognitive_load": "B", "graph_vector": ["Monotonie", "Skládání funkcí"],
        }
        for i, (text, expected) in enumerate([
            (r"$f$ je rostoucí na $D(f),\ g$ je rostoucí na $D(g).$ Rozhodněte o monotonii $f \circ g$.",  "rost"),
            (r"$f$ je rostoucí na $D(f),\ g$ je klesající na $D(g).$ Rozhodněte o monotonii $f \circ g$.", "kles"),
            (r"$f$ je klesající na $D(f),\ g$ je klesající na $D(g).$ Rozhodněte o monotonii $f \circ g$.","rost"),
            (r"$f$ je klesající na $D(f),\ g$ je rostoucí na $D(g).$ Rozhodněte o monotonii $f \circ g$.", "kles"),
        ])
    ],

    # --------------------- 4 podul: parita f∘g ---------------------
    *[
        {
            "task_id": f"cv03_{21+i}",
            "content_latex": text,
            "results": [{
                "key": "parita", "label_latex": r"f \circ g \text{ je }", "type": "multiple_choice",
                "options": [
                    {"key": "suda",  "label_latex": r"\text{sudá}"},
                    {"key": "licha", "label_latex": r"\text{lichá}"},
                    {"key": "nic",   "label_latex": r"\text{ani sudá, ani lichá}"},
                ],
                "expected": expected,
            }],
            "cognitive_load": "B", "graph_vector": ["Sudá/lichá funkce", "Skládání funkcí"],
        }
        for i, (text, expected) in enumerate([
            (r"$f$ je sudá na $D(f),\ g$ je sudá na $D(g).$ Rozhodněte o paritě $f \circ g$.",   "suda"),
            (r"$f$ je sudá na $D(f),\ g$ je lichá na $D(g).$ Rozhodněte o paritě $f \circ g$.",  "suda"),
            (r"$f$ je lichá na $D(f),\ g$ je lichá na $D(g).$ Rozhodněte o paritě $f \circ g$.", "licha"),
            (r"$f$ je lichá na $D(f),\ g$ je sudá na $D(g).$ Rozhodněte o paritě $f \circ g$.",  "suda"),
        ])
    ],

    # --------------------- 4 podul: parita f·g ---------------------
    *[
        {
            "task_id": f"cv03_{25+i}",
            "content_latex": text,
            "results": [{
                "key": "parita", "label_latex": r"f \cdot g \text{ je }", "type": "multiple_choice",
                "options": [
                    {"key": "suda",  "label_latex": r"\text{sudá}"},
                    {"key": "licha", "label_latex": r"\text{lichá}"},
                    {"key": "nic",   "label_latex": r"\text{ani sudá, ani lichá}"},
                ],
                "expected": expected,
            }],
            "cognitive_load": "B", "graph_vector": ["Sudá/lichá funkce"],
        }
        for i, (text, expected) in enumerate([
            (r"$f$ je sudá na $D(f),\ g$ je sudá na $D(g).$ Rozhodněte o paritě $f \cdot g$.",   "suda"),
            (r"$f$ je sudá na $D(f),\ g$ je lichá na $D(g).$ Rozhodněte o paritě $f \cdot g$.",  "licha"),
            (r"$f$ je lichá na $D(f),\ g$ je lichá na $D(g).$ Rozhodněte o paritě $f \cdot g$.", "suda"),
            (r"$f$ je lichá na $D(f),\ g$ je sudá na $D(g).$ Rozhodněte o paritě $f \cdot g$.",  "licha"),
        ])
    ],

    # --------------------- 4 podul: Hornerovo schéma — hodnota P(a) ---------------------
    {"task_id": "cv03_29",
     "content_latex": r"Pomocí Hornerova schématu určete hodnotu $P(a)$ polynomu $P(x) = 3x^5 + 5x^4 - 4x^3 + 7x + 3$ v bodě $a = -2$.",
     "results": [{"key": "P", "label_latex": r"P(a) = ", "type": "decimal", "expected": 5, "tolerance": 0.01}],
     "cognitive_load": "C", "graph_vector": ["Polynomy", "Hornerovo schéma"]},
    {"task_id": "cv03_30",
     "content_latex": r"Pomocí Hornerova schématu určete hodnotu $P(a)$ polynomu $P(x) = x^4 - 3x^3 - 13x^2 + 15x$ v bodě $a = 5$.",
     "results": [{"key": "P", "label_latex": r"P(a) = ", "type": "decimal", "expected": 0, "tolerance": 0.01}],
     "cognitive_load": "C", "graph_vector": ["Polynomy", "Hornerovo schéma"]},
    {"task_id": "cv03_31",
     "content_latex": r"Pomocí Hornerova schématu určete hodnotu $P(a)$ polynomu $P(x) = 2x^3 - 21x^2 + 9x - 200$ v bodě $a = 11$.",
     "results": [{"key": "P", "label_latex": r"P(a) = ", "type": "decimal", "expected": 20, "tolerance": 0.01}],
     "cognitive_load": "C", "graph_vector": ["Polynomy", "Hornerovo schéma"]},
    {"task_id": "cv03_32",
     "content_latex": r"Pomocí Hornerova schématu určete hodnotu $P(a)$ polynomu $P(x) = x^4 + 5x^3 + x^2 - 8$ v bodě $a = 1{,}1$.",
     "results": [{"key": "P", "label_latex": r"P(a) = ", "type": "decimal", "expected": 1.3291, "tolerance": 0.0001}],
     "cognitive_load": "C", "graph_vector": ["Polynomy", "Hornerovo schéma"]},

    # --------------------- 4 podul: Horner — podíl + zbytek při dělení (x-a) ---------------------
    {
        "task_id": "cv03_33",
        "content_latex": r"Pomocí Hornerova schématu nalezněte podíl a zbytek při dělení polynomu $P(x) = 4x^2 + 12x + 5$ výrazem $x - a,$ kde $a = -1$.",
        "results": [
            {"key": "podil", "label_latex": r"\text{Podíl: }", "type": "mathlive", "expected": r"4x + 8"},
            {"key": "zbytek", "label_latex": r"\text{Zbytek: }", "type": "decimal", "expected": -3, "tolerance": 0.01},
        ],
        "cognitive_load": "C", "graph_vector": ["Polynomy", "Hornerovo schéma"],
    },
    {
        "task_id": "cv03_34",
        "content_latex": r"Pomocí Hornerova schématu nalezněte podíl a zbytek při dělení polynomu $P(x) = x^3 + 3x^2 - 7x + 6$ výrazem $x - a,$ kde $a = 2$.",
        "results": [
            {"key": "podil", "label_latex": r"\text{Podíl: }", "type": "mathlive", "expected": r"x^2 + 5x + 3"},
            {"key": "zbytek", "label_latex": r"\text{Zbytek: }", "type": "decimal", "expected": 12, "tolerance": 0.01},
        ],
        "cognitive_load": "C", "graph_vector": ["Polynomy", "Hornerovo schéma"],
    },
    {
        "task_id": "cv03_35",
        "content_latex": r"Pomocí Hornerova schématu nalezněte podíl a zbytek při dělení polynomu $P(x) = 5x^4 + 30x^3 - 40x^2 + 36x + 14$ výrazem $x - a,$ kde $a = -7$.",
        "results": [
            {"key": "podil", "label_latex": r"\text{Podíl: }", "type": "mathlive", "expected": r"5x^3 - 5x^2 - 5x + 71"},
            {"key": "zbytek", "label_latex": r"\text{Zbytek: }", "type": "decimal", "expected": -483, "tolerance": 0.5},
        ],
        "cognitive_load": "D", "graph_vector": ["Polynomy", "Hornerovo schéma"],
    },
    {
        "task_id": "cv03_36",
        "content_latex": r"Pomocí Hornerova schématu nalezněte podíl a zbytek při dělení polynomu $P(x) = 3x^4 - x^3 - 21x^2 - 11x + 6$ výrazem $x - a,$ kde $a = -2$.",
        "results": [
            {"key": "podil", "label_latex": r"\text{Podíl: }", "type": "mathlive", "expected": r"3x^3 - 7x^2 - 7x + 3"},
            {"key": "zbytek", "label_latex": r"\text{Zbytek: }", "type": "decimal", "expected": 0, "tolerance": 0.01},
        ],
        "cognitive_load": "D", "graph_vector": ["Polynomy", "Hornerovo schéma"],
    },

    # --------------------- 6 podul: podíl polynomů ---------------------
    {"task_id": "cv03_37",
     "content_latex": r"Určete podíl polynomů: $\dfrac{x^3 + 2x^2 + 2x + 1}{x + 2}$ (uveďte celočíselný podíl plus zlomek se zbytkem).",
     "results": [{"key": "podil", "label_latex": r"= ", "type": "mathlive",
                  "expected": r"x^2 + 2 - \frac{3}{x + 2}"}],
     "cognitive_load": "D", "graph_vector": ["Polynomy", "Dělení polynomů"]},
    {"task_id": "cv03_38",
     "content_latex": r"Určete podíl polynomů: $\dfrac{x^4 - x^3 + x^2 - x + 2}{x - 2}.$",
     "results": [{"key": "podil", "label_latex": r"= ", "type": "mathlive",
                  "expected": r"x^3 + x^2 + 3x + 5 + \frac{12}{x - 2}"}],
     "cognitive_load": "D", "graph_vector": ["Polynomy", "Dělení polynomů"]},
    {"task_id": "cv03_39",
     "content_latex": r"Určete podíl polynomů: $\dfrac{x^3 + 6x + 3}{x^2 - 2x + 2}.$",
     "results": [{"key": "podil", "label_latex": r"= ", "type": "mathlive",
                  "expected": r"x + 2 + \frac{8x - 1}{x^2 - 2x + 2}"}],
     "cognitive_load": "D", "graph_vector": ["Polynomy", "Dělení polynomů"]},
    {"task_id": "cv03_40",
     "content_latex": r"Určete podíl polynomů: $\dfrac{3x^4 - 5x^3 - 20x - 5}{x^2 + x + 3}.$",
     "results": [{"key": "podil", "label_latex": r"= ", "type": "mathlive",
                  "expected": r"3x^2 - 8x - 1 + \frac{5x - 2}{x^2 + x + 3}"}],
     "cognitive_load": "E", "graph_vector": ["Polynomy", "Dělení polynomů"]},
    {"task_id": "cv03_41",
     "content_latex": r"Určete podíl polynomů: $\dfrac{x^6 + x^4 + x^2 + 1}{x^2 + 1}.$",
     "results": [{"key": "podil", "label_latex": r"= ", "type": "mathlive",
                  "expected": r"x^4 + 1"}],
     "cognitive_load": "D", "graph_vector": ["Polynomy", "Dělení polynomů"]},
    {"task_id": "cv03_42",
     "content_latex": r"Určete podíl polynomů: $\dfrac{2x^5 - 7x^4 - 13}{4x^2 - 6x + 8}.$",
     "results": [{"key": "podil", "label_latex": r"= ", "type": "mathlive",
                  "expected": r"\frac{1}{2}x^3 - x^2 - \frac{5}{2}x - \frac{7}{4} + \frac{\frac{19}{2}x + 1}{4x^2 - 6x + 8}"}],
     "cognitive_load": "F", "graph_vector": ["Polynomy", "Dělení polynomů"]},
]
