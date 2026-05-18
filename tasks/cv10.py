"""
Cvičení 10 — Vyšetřování druhé derivace (konvexita / konkávita / inflexe),
hledání asymptot.
"""


def _conv(idx, fn, correct, distr_b, distr_c, cl="D"):
    return {
        "task_id": f"cv10_{idx}",
        "content_latex": (
            r"Určete intervaly, na kterých je funkce $f$ ryze konvexní nebo ryze konkávní, "
            r"a inflexní body: $f(x) = " + fn + "$."
        ),
        "results": [{
            "key": "konvexita", "label_latex": r"\text{Vyšetření: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": correct},
                {"key": "b", "label_latex": distr_b},
                {"key": "c", "label_latex": distr_c},
            ],
            "expected": "a",
        }],
        "cognitive_load": cl, "graph_vector": ["Konvexita", "Inflexní bod"],
    }


TASKS = [
    # --------------------- 3 negace ---------------------
    {
        "task_id": "cv10_1",
        "content_latex": (
            r"Formulujte negaci výroku o asociativnosti násobení: "
            r"\textit{Pro každou trojici } $x, y, z \in \mathbb{R}$ \textit{ platí } "
            r"$x \cdot (y \cdot z) = (x \cdot y) \cdot z.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje trojice $x, y, z \in \mathbb{R}$ taková, že $x \cdot (y \cdot z) \ne (x \cdot y) \cdot z.$"},
                {"key": "b", "label_latex": r"Pro každou trojici platí $x \cdot (y \cdot z) \ne (x \cdot y) \cdot z.$"},
                {"key": "c", "label_latex": r"Existuje trojice taková, že $x \cdot y \ne y \cdot x.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv10_2",
        "content_latex": (
            r"Formulujte negaci výroku o neutrálním prvku pro součin: "
            r"\textit{Existuje } $\nu \in \mathbb{R} \setminus \{0\}$ \textit{ takové, že pro každé } "
            r"$x \in \mathbb{R}$ \textit{ platí } $x \cdot \nu = x.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Pro každé $\nu \in \mathbb{R} \setminus \{0\}$ existuje $x \in \mathbb{R}$ takové, že $x \cdot \nu \ne x.$"},
                {"key": "b", "label_latex": r"Existuje $\nu \ne 0$ takové, že pro každé $x$ platí $x \cdot \nu \ne x.$"},
                {"key": "c", "label_latex": r"Pro každé $\nu$ a každé $x$ platí $x \cdot \nu \ne x.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv10_3",
        "content_latex": (
            r"Formulujte negaci výroku o inverzním prvku pro součin: "
            r"\textit{Pro každé } $x \in \mathbb{R} \setminus \{0\}$ \textit{ existuje } $y \in \mathbb{R}$ "
            r"\textit{ takové, že } $x \cdot y = 1.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $x \in \mathbb{R} \setminus \{0\}$ takové, že pro každé $y \in \mathbb{R}$ platí $x \cdot y \ne 1.$"},
                {"key": "b", "label_latex": r"Pro každé $x$ existuje $y$ takové, že $x \cdot y \ne 1.$"},
                {"key": "c", "label_latex": r"Pro každé $x \ne 0$ a každé $y$ platí $x \cdot y \ne 1.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků"],
    },

    # --------------------- 10 podul: konvexita / konkávita / inflexe ---------------------
    _conv(4, r"x^6 - 6x^5 + \tfrac{15}{2}x^4 + 3x",
          r"Konvexní v $(-\infty, 0) \cup (0, 1) \cup (3, \infty),$ konkávní v $(1, 3);$ inflexe v $x = 1, x = 3.$",
          r"Konkávní v $(-\infty, 0) \cup (0, 1) \cup (3, \infty),$ konvexní v $(1, 3);$ inflexe v $x = 1, x = 3.$",
          r"Konvexní na celém $\mathbb{R};$ žádná inflexe.", "E"),
    _conv(5, r"x^4 - 2x^2 + 3",
          r"Konvexní v $(-\infty, -\tfrac{1}{\sqrt{3}}) \cup (\tfrac{1}{\sqrt{3}}, \infty),$ konkávní v $(-\tfrac{1}{\sqrt{3}}, \tfrac{1}{\sqrt{3}});$ inflexe v $x = \pm \tfrac{1}{\sqrt{3}}.$",
          r"Konkávní v $(-\infty, -\tfrac{1}{\sqrt{3}}) \cup (\tfrac{1}{\sqrt{3}}, \infty),$ konvexní uvnitř.",
          r"Konvexní na celém $\mathbb{R};$ žádná inflexe.", "D"),
    _conv(6, r"x^5 - 5x^4 + \tfrac{20}{3}x^3 + 3x + 1",
          r"Konkávní v $(-\infty, 0) \cup (1, 2),$ konvexní v $(0, 1) \cup (2, \infty);$ inflexe v $x = 0, 1, 2.$",
          r"Konvexní v $(-\infty, 0) \cup (1, 2),$ konkávní v $(0, 1) \cup (2, \infty);$ inflexe v $x = 0, 1, 2.$",
          r"Konvexní na celém $\mathbb{R};$ žádná inflexe.", "E"),
    _conv(7, r"e^{-x^2} + 2x",
          r"Konvexní v $(-\infty, -\tfrac{1}{\sqrt{2}}) \cup (\tfrac{1}{\sqrt{2}}, \infty),$ konkávní v $(-\tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}});$ inflexe v $x = \pm \tfrac{1}{\sqrt{2}}.$",
          r"Konkávní v $(-\infty, -\tfrac{1}{\sqrt{2}}) \cup (\tfrac{1}{\sqrt{2}}, \infty),$ konvexní uvnitř.",
          r"Konvexní na celém $\mathbb{R};$ žádná inflexe.", "D"),
    _conv(8, r"\left(\frac{1 + x}{1 - x}\right)^4",
          r"Konkávní v $(-\infty, -4),$ konvexní v $(-4, 1) \cup (1, \infty);$ inflexe v $x = -4.$",
          r"Konvexní v $(-\infty, -4),$ konkávní v $(-4, 1) \cup (1, \infty);$ inflexe v $x = -4.$",
          r"Konvexní na celém $D;$ žádná inflexe.", "E"),
    _conv(9, r"3x e^x",
          r"Konkávní v $(-\infty, -2),$ konvexní v $(-2, \infty);$ inflexe v $x = -2.$",
          r"Konvexní v $(-\infty, -2),$ konkávní v $(-2, \infty);$ inflexe v $x = -2.$",
          r"Konvexní na celém $\mathbb{R};$ žádná inflexe.", "D"),
    _conv(10, r"\frac{3 \ln x}{\sqrt{x}}",
          r"Konkávní v $(0, e^{8/3}),$ konvexní v $(e^{8/3}, \infty);$ inflexe v $x = e^{8/3}.$",
          r"Konvexní v $(0, e^{8/3}),$ konkávní v $(e^{8/3}, \infty);$ inflexe v $x = e^{8/3}.$",
          r"Konvexní v celém $(0, \infty);$ žádná inflexe.", "E"),
    _conv(11, r"x^4 e^{-3x}",
          r"Konkávní v $(\tfrac{2}{3}, 2),$ konvexní v $(-\infty, \tfrac{2}{3}) \cup (2, \infty);$ inflexe v $x = \tfrac{2}{3}, x = 2.$",
          r"Konvexní v $(\tfrac{2}{3}, 2),$ konkávní jinde; inflexe v $x = \tfrac{2}{3}, x = 2.$",
          r"Konvexní na celém $\mathbb{R};$ žádná inflexe.", "E"),
    _conv(12, r"x^2 \ln x",
          r"Konkávní v $(0, e^{-3/2}),$ konvexní v $(e^{-3/2}, \infty);$ inflexe v $x = e^{-3/2}.$",
          r"Konvexní v $(0, e^{-3/2}),$ konkávní v $(e^{-3/2}, \infty);$ inflexe v $x = e^{-3/2}.$",
          r"Konvexní v celém $(0, \infty);$ žádná inflexe.", "D"),
    _conv(13, r"\frac{\ln(x + 2)}{\sqrt{x + 2}}",
          r"Konkávní v $(-2, -2 + e^{8/3}),$ konvexní v $(-2 + e^{8/3}, \infty);$ inflexe v $x = -2 + e^{8/3}.$",
          r"Konvexní v $(-2, -2 + e^{8/3}),$ konkávní v $(-2 + e^{8/3}, \infty);$ inflexe v $x = -2 + e^{8/3}.$",
          r"Konvexní v celém $(-2, \infty);$ žádná inflexe.", "E"),

    # --------------------- 5 podul: rovnice asymptot ---------------------
    {
        "task_id": "cv10_14",
        "content_latex": r"Napište rovnice asymptot grafu funkce $y = \dfrac{x^3 + 3}{x^2 - 9}$.",
        "results": [
            {"key": "vert1", "label_latex": r"\text{Vertikální 1: }", "type": "mathlive", "expected": r"x = 3"},
            {"key": "vert2", "label_latex": r"\text{Vertikální 2: }", "type": "mathlive", "expected": r"x = -3"},
            {"key": "sikma", "label_latex": r"\text{Šikmá: }",        "type": "mathlive", "expected": r"y = x"},
        ],
        "cognitive_load": "D", "graph_vector": ["Asymptoty"],
    },
    {
        "task_id": "cv10_15",
        "content_latex": r"Napište rovnice asymptot grafu funkce $y = \dfrac{\ln x}{x} - x$.",
        "results": [
            {"key": "vert",  "label_latex": r"\text{Vertikální: }", "type": "mathlive", "expected": r"x = 0"},
            {"key": "sikma", "label_latex": r"\text{Šikmá: }",      "type": "mathlive", "expected": r"y = -x"},
        ],
        "cognitive_load": "D", "graph_vector": ["Asymptoty"],
    },
    {
        "task_id": "cv10_16",
        "content_latex": r"Napište rovnice asymptot grafu funkce $y = \dfrac{x^2 + 3x + 7}{x + 1}$.",
        "results": [
            {"key": "vert",  "label_latex": r"\text{Vertikální: }", "type": "mathlive", "expected": r"x = -1"},
            {"key": "sikma", "label_latex": r"\text{Šikmá: }",      "type": "mathlive", "expected": r"y = x + 2"},
        ],
        "cognitive_load": "C", "graph_vector": ["Asymptoty"],
    },
    {
        "task_id": "cv10_17",
        "content_latex": r"Napište rovnice asymptot grafu funkce $y = 2 - e^{-x^2}$.",
        "results": [
            {"key": "h", "label_latex": r"\text{Vodorovná: }", "type": "mathlive", "expected": r"y = 2"},
        ],
        "cognitive_load": "C", "graph_vector": ["Asymptoty"],
    },
    {
        "task_id": "cv10_18",
        "content_latex": r"Napište rovnice asymptot grafu funkce $y = \dfrac{x^2}{x - 2}$.",
        "results": [
            {"key": "vert",  "label_latex": r"\text{Vertikální: }", "type": "mathlive", "expected": r"x = 2"},
            {"key": "sikma", "label_latex": r"\text{Šikmá: }",      "type": "mathlive", "expected": r"y = x + 2"},
        ],
        "cognitive_load": "C", "graph_vector": ["Asymptoty"],
    },
]
