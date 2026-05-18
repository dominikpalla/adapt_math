"""
Cvičení 2 — Vytváření funkcí: součet, rozdíl, součin, podíl, skládání.
Vlastnosti: prostá funkce, inverzní funkce.
"""

TASKS = [
    # --------------------- 3 negace ---------------------
    {
        "task_id": "cv02_1",
        "content_latex": (
            r"Ve tvaru implikace formulujte rčení: \textit{Kdo maže, ten jede.} "
            r"Pak vyslovte jeho negaci."
        ),
        "results": [
            {
                "key": "implikace", "label_latex": r"\text{Implikace: }", "type": "multiple_choice",
                "options": [
                    {"key": "a", "label_latex": r"Jestliže maže, pak jede."},
                    {"key": "b", "label_latex": r"Jestliže jede, pak maže."},
                    {"key": "c", "label_latex": r"Maže právě tehdy, když jede."},
                ],
                "expected": "a",
            },
            {
                "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
                "options": [
                    {"key": "a", "label_latex": r"Maže a nejede."},
                    {"key": "b", "label_latex": r"Nemaže a jede."},
                    {"key": "c", "label_latex": r"Jestliže nejede, nemaže."},
                ],
                "expected": "a",
            },
        ],
        "cognitive_load": "B", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv02_2",
        "content_latex": (
            r"Nechť $\mathbf{M} \subseteq \mathbb{R}.$ Formulujte negaci výroku: "
            r"\textit{Funkce } $f: \mathbf{M} \to \mathbb{R}$ \textit{ je prostá na } $\mathbf{M}$ "
            r"\textit{ právě tehdy, když pro každé } $x_1, x_2 \in \mathbf{M}$ \textit{ platí: "
            r"je-li } $x_1 \ne x_2,$ \textit{ pak } $f(x_1) \ne f(x_2).$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$f$ není prostá nebo existují $x_1, x_2 \in \mathbf{M},\ x_1 \ne x_2,$ taková, že $f(x_1) = f(x_2),$ a opačně."},
                {"key": "b", "label_latex": r"$f$ je prostá a existují $x_1, x_2 \in \mathbf{M},\ x_1 \ne x_2,$ taková, že $f(x_1) = f(x_2).$"},
                {"key": "c", "label_latex": r"Pro každé $x_1, x_2 \in \mathbf{M}$ platí: je-li $x_1 = x_2,$ pak $f(x_1) = f(x_2).$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Prostá funkce"],
    },
    {
        "task_id": "cv02_3",
        "content_latex": (
            r"Formulujte negaci výroku: "
            r"\textit{Každá neprázdná shora omezená množina } $\mathbf{M} \subset \mathbb{R}$ "
            r"\textit{ má suprémum v množině } $\mathbb{R}.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje neprázdná shora omezená množina $\mathbf{M} \subset \mathbb{R},$ která nemá suprémum v $\mathbb{R}.$"},
                {"key": "b", "label_latex": r"Žádná shora omezená množina $\mathbf{M} \subset \mathbb{R}$ nemá suprémum v $\mathbb{R}.$"},
                {"key": "c", "label_latex": r"Každá neprázdná shora neomezená množina $\mathbf{M} \subset \mathbb{R}$ má suprémum v $\mathbb{R}.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },

    # --------------------- 4 operace s funkcemi (multi-výsledek) ---------------------
    {
        "task_id": "cv02_4",
        "content_latex": r"Určete předpisy funkcí $f+g,\ f \cdot g,\ f/g,\ f \circ g,\ g \circ f$, je-li $f: y = 2x,\ g: y = x^2 + 1$.",
        "results": [
            {"key": "fplusg",  "label_latex": r"(f+g)(x) = ",      "type": "mathlive", "expected": r"2x + x^2 + 1"},
            {"key": "ftimesg", "label_latex": r"(f \cdot g)(x) = ", "type": "mathlive", "expected": r"2x(x^2 + 1)"},
            {"key": "fdivg",   "label_latex": r"(f / g)(x) = ",     "type": "mathlive", "expected": r"\frac{2x}{x^2 + 1}"},
            {"key": "fcompg",  "label_latex": r"(f \circ g)(x) = ", "type": "mathlive", "expected": r"2(x^2 + 1)"},
            {"key": "gcompf",  "label_latex": r"(g \circ f)(x) = ", "type": "mathlive", "expected": r"4x^2 + 1"},
        ],
        "cognitive_load": "C", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_5",
        "content_latex": r"Určete předpisy funkcí $f+g,\ f \cdot g,\ f/g,\ f \circ g,\ g \circ f$, je-li $f: y = 3x - 2,\ g: y = |x|$.",
        "results": [
            {"key": "fplusg",  "label_latex": r"(f+g)(x) = ",      "type": "mathlive", "expected": r"3x + |x| - 2"},
            {"key": "ftimesg", "label_latex": r"(f \cdot g)(x) = ", "type": "mathlive", "expected": r"|x|(3x - 2)"},
            {"key": "fdivg",   "label_latex": r"(f / g)(x) = ",     "type": "mathlive", "expected": r"\frac{3x - 2}{|x|}"},
            {"key": "fcompg",  "label_latex": r"(f \circ g)(x) = ", "type": "mathlive", "expected": r"3|x| - 2"},
            {"key": "gcompf",  "label_latex": r"(g \circ f)(x) = ", "type": "mathlive", "expected": r"|3x - 2|"},
        ],
        "cognitive_load": "C", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_6",
        "content_latex": r"Určete předpisy funkcí $f+g,\ f \cdot g,\ f/g,\ f \circ g,\ g \circ f$, je-li $f: y = \sqrt{x+1},\ g: y = x - 2$.",
        "results": [
            {"key": "fplusg",  "label_latex": r"(f+g)(x) = ",      "type": "mathlive", "expected": r"\sqrt{x+1} + x - 2"},
            {"key": "ftimesg", "label_latex": r"(f \cdot g)(x) = ", "type": "mathlive", "expected": r"\sqrt{x+1}(x - 2)"},
            {"key": "fdivg",   "label_latex": r"(f / g)(x) = ",     "type": "mathlive", "expected": r"\frac{\sqrt{x+1}}{x - 2}"},
            {"key": "fcompg",  "label_latex": r"(f \circ g)(x) = ", "type": "mathlive", "expected": r"\sqrt{x - 1}"},
            {"key": "gcompf",  "label_latex": r"(g \circ f)(x) = ", "type": "mathlive", "expected": r"\sqrt{x+1} - 2"},
        ],
        "cognitive_load": "C", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_7",
        "content_latex": r"Určete předpisy funkcí $f+g,\ f \cdot g,\ f/g,\ f \circ g,\ g \circ f$, je-li $f: y = \dfrac{x}{x^2 + 1},\ g: y = \dfrac{1}{x}$.",
        "results": [
            {"key": "fplusg",  "label_latex": r"(f+g)(x) = ",      "type": "mathlive", "expected": r"\frac{2x^2 + 1}{x(x^2 + 1)}"},
            {"key": "ftimesg", "label_latex": r"(f \cdot g)(x) = ", "type": "mathlive", "expected": r"\frac{1}{x^2 + 1}"},
            {"key": "fdivg",   "label_latex": r"(f / g)(x) = ",     "type": "mathlive", "expected": r"\frac{x^2}{x^2 + 1}"},
            {"key": "fcompg",  "label_latex": r"(f \circ g)(x) = ", "type": "mathlive", "expected": r"\frac{x}{x^2 + 1}"},
            {"key": "gcompf",  "label_latex": r"(g \circ f)(x) = ", "type": "mathlive", "expected": r"\frac{x^2 + 1}{x}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Skládání funkcí"],
    },

    # --------------------- f∘f a f∘f∘f pro f(x)=1/(1-x) ---------------------
    {
        "task_id": "cv02_8",
        "content_latex": r"Je-li $f(x) = \dfrac{1}{1 - x},$ určete předpis a definiční obor funkce $f \circ f.$",
        "results": [
            {"key": "predpis", "label_latex": r"(f \circ f)(x) = ", "type": "mathlive",
             "expected": r"\frac{x - 1}{x}"},
            {"key": "D", "label_latex": r"D = ", "type": "mathlive",
             "expected": r"\mathbb{R} \setminus \{0, 1\}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_9",
        "content_latex": r"Je-li $f(x) = \dfrac{1}{1 - x},$ určete předpis a definiční obor funkce $f \circ f \circ f.$",
        "results": [
            {"key": "predpis", "label_latex": r"(f \circ f \circ f)(x) = ", "type": "mathlive",
             "expected": r"x"},
            {"key": "D", "label_latex": r"D = ", "type": "mathlive",
             "expected": r"\mathbb{R} \setminus \{0, 1\}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_10",
        "content_latex": (
            r"Pro $f(x) = \sqrt{1 - x},\ g(x) = 1 - x^2,\ h(x) = 1 + \sqrt{x}$ "
            r"určete předpis a definiční obor funkce $F = f \circ g \circ h.$"
        ),
        "results": [
            {"key": "F", "label_latex": r"F(x) = ", "type": "mathlive",
             "expected": r"1 + \sqrt{x}"},
            {"key": "D", "label_latex": r"D_F = ", "type": "mathlive",
             "expected": r"[0, \infty)"},
        ],
        "cognitive_load": "D", "graph_vector": ["Skládání funkcí"],
    },

    # --------------------- 4 podul: rozklad F na f∘g ---------------------
    {
        "task_id": "cv02_11",
        "content_latex": r"Vyjádřete funkci $F: y = (x^2 + 1)^3$ ve tvaru $f \circ g.$",
        "results": [
            {"key": "f", "label_latex": r"f(x) = ", "type": "mathlive", "expected": r"x^3"},
            {"key": "g", "label_latex": r"g(x) = ", "type": "mathlive", "expected": r"x^2 + 1"},
        ],
        "cognitive_load": "B", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_12",
        "content_latex": r"Vyjádřete funkci $F: y = \sin(\sqrt{x})$ ve tvaru $f \circ g.$",
        "results": [
            {"key": "f", "label_latex": r"f(x) = ", "type": "mathlive", "expected": r"\sin x"},
            {"key": "g", "label_latex": r"g(x) = ", "type": "mathlive", "expected": r"\sqrt{x}"},
        ],
        "cognitive_load": "B", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_13",
        "content_latex": r"Vyjádřete funkci $F: y = \sqrt{\cos x}$ ve tvaru $f \circ g.$",
        "results": [
            {"key": "f", "label_latex": r"f(x) = ", "type": "mathlive", "expected": r"\sqrt{x}"},
            {"key": "g", "label_latex": r"g(x) = ", "type": "mathlive", "expected": r"\cos x"},
        ],
        "cognitive_load": "B", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_14",
        "content_latex": r"Vyjádřete funkci $F: y = \ln^2 x + 4 \ln x + 100$ ve tvaru $f \circ g.$",
        "results": [
            {"key": "f", "label_latex": r"f(x) = ", "type": "mathlive", "expected": r"x^2 + 4x + 100"},
            {"key": "g", "label_latex": r"g(x) = ", "type": "mathlive", "expected": r"\ln x"},
        ],
        "cognitive_load": "C", "graph_vector": ["Skládání funkcí"],
    },

    # --------------------- 2 podul: F = f∘g∘h ---------------------
    {
        "task_id": "cv02_15",
        "content_latex": r"Nalezněte funkce $f, g, h$ tak, že $F = f \circ g \circ h,$ kde $F: y = \dfrac{1}{\sqrt{1 + \sqrt{x}}}$.",
        "results": [
            {"key": "f", "label_latex": r"f(x) = ", "type": "mathlive", "expected": r"\frac{1}{x}"},
            {"key": "g", "label_latex": r"g(x) = ", "type": "mathlive", "expected": r"\sqrt{1 + x}"},
            {"key": "h", "label_latex": r"h(x) = ", "type": "mathlive", "expected": r"\sqrt{x}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Skládání funkcí"],
    },
    {
        "task_id": "cv02_16",
        "content_latex": r"Nalezněte funkce $f, g, h$ tak, že $F = f \circ g \circ h,$ kde $F: y = \left|\dfrac{1}{x^2 - \sqrt{x^2 + 7}}\right|$.",
        "results": [
            {"key": "f", "label_latex": r"f(x) = ", "type": "mathlive", "expected": r"|x|"},
            {"key": "g", "label_latex": r"g(x) = ", "type": "mathlive", "expected": r"\frac{1}{x}"},
            {"key": "h", "label_latex": r"h(x) = ", "type": "mathlive", "expected": r"x^2 - \sqrt{x^2 + 7}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Skládání funkcí"],
    },

    # --------------------- 3 podul + 1 uloha: určete f(x) z transformace ---------------------
    {
        "task_id": "cv02_17",
        "content_latex": r"Určete $f(x),$ je-li $f(x + 1) = x^2 - 3x + 2.$",
        "results": [{"key": "f", "label_latex": r"f(x) = ", "type": "mathlive",
                     "expected": r"x^2 - 5x + 6"}],
        "cognitive_load": "C", "graph_vector": ["Funkce"],
    },
    {
        "task_id": "cv02_18",
        "content_latex": r"Určete $f(x),$ je-li $f\left(\dfrac{x}{x+1}\right) = x^2.$",
        "results": [{"key": "f", "label_latex": r"f(x) = ", "type": "mathlive",
                     "expected": r"\left(\frac{x}{1 - x}\right)^2"}],
        "cognitive_load": "D", "graph_vector": ["Funkce"],
    },
    {
        # Dvě větve podle znaménka — multiple_choice.
        "task_id": "cv02_19",
        "content_latex": r"Určete $f(x),$ je-li $f\left(\dfrac{1}{x}\right) = x + \sqrt{1 + x^2}.$",
        "results": [{
            "key": "f", "label_latex": r"\text{Předpis } f(x):\ ", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$x > 0:\ f(x) = \tfrac{1 + \sqrt{x^2 + 1}}{x},\quad x < 0:\ f(x) = \tfrac{1 - \sqrt{x^2 + 1}}{x}$"},
                {"key": "b", "label_latex": r"$f(x) = \tfrac{1 + \sqrt{x^2 + 1}}{x}$ pro všechna $x \ne 0$"},
                {"key": "c", "label_latex": r"$f(x) = \tfrac{x + \sqrt{1 + x^2}}{x^2}$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "E", "graph_vector": ["Funkce"],
    },
    {
        "task_id": "cv02_20",
        "content_latex": r"Určete $f(x + 1),$ je-li $f(x - 1) = 2x^2 - 3x + 1.$",
        "results": [{"key": "f", "label_latex": r"f(x+1) = ", "type": "mathlive",
                     "expected": r"2x^2 + 5x + 3"}],
        "cognitive_load": "C", "graph_vector": ["Funkce"],
    },

    # --------------------- 9 podul: inverzní funkce ---------------------
    {
        "task_id": "cv02_21",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = \sqrt[3]{x + 1}.$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"\mathbb{R}"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"\mathbb{R}"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"x^3 - 1"},
        ],
        "cognitive_load": "C", "graph_vector": ["Inverzní funkce"],
    },
    {
        "task_id": "cv02_22",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = 1 + \ln(x + 2).$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"(-2, \infty)"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"\mathbb{R}"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"e^{x - 1} - 2"},
        ],
        "cognitive_load": "C", "graph_vector": ["Inverzní funkce"],
    },
    {
        "task_id": "cv02_23",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = \dfrac{2^x}{1 + 2^x}.$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"\mathbb{R}"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"(0, 1)"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"\log_2\frac{x}{1 - x}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Inverzní funkce"],
    },
    {
        "task_id": "cv02_24",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = \dfrac{10^x - 10^{-x}}{10^x + 10^{-x}} + 1.$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"\mathbb{R}"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"(0, 2)"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"\frac{1}{2} \log\frac{x}{2 - x}"},
        ],
        "cognitive_load": "E", "graph_vector": ["Inverzní funkce"],
    },
    {
        "task_id": "cv02_25",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = \log_a(x + \sqrt{x^2 + 1}).$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"\mathbb{R}"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"\mathbb{R}"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"\frac{a^x - a^{-x}}{2}"},
        ],
        "cognitive_load": "E", "graph_vector": ["Inverzní funkce"],
    },
    {
        "task_id": "cv02_26",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = e^{1/x} - 2.$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"\mathbb{R} \setminus \{0\}"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"(-2, -1) \cup (-1, \infty)"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"\frac{1}{\ln(x + 2)}"},
        ],
        "cognitive_load": "E", "graph_vector": ["Inverzní funkce"],
    },
    {
        "task_id": "cv02_27",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = 1 + \log\dfrac{1}{1 - x}.$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"(-\infty, 1)"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"\mathbb{R}"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"1 - 10^{1 - x}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Inverzní funkce"],
    },
    {
        "task_id": "cv02_28",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = 1 + \arccos 2^x.$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"(-\infty, 0]"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"[1, 1 + \pi/2)"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"\log_2(\cos(x - 1))"},
        ],
        "cognitive_load": "E", "graph_vector": ["Inverzní funkce"],
    },
    {
        "task_id": "cv02_29",
        "content_latex": r"Určete definiční obor, obor hodnot a předpis inverzní funkce k $y = \arcsin\dfrac{x - 2}{2x}.$",
        "results": [
            {"key": "D", "label_latex": r"D_f = ", "type": "mathlive", "expected": r"(-\infty, -2] \cup [2/3, \infty)"},
            {"key": "H", "label_latex": r"H_f = ", "type": "mathlive", "expected": r"[-\pi/2, \pi/2] \setminus \{\pi/6\}"},
            {"key": "finv", "label_latex": r"f^{-1}(x) = ", "type": "mathlive", "expected": r"\frac{2}{1 - 2\sin x}"},
        ],
        "cognitive_load": "F", "graph_vector": ["Inverzní funkce"],
    },
]
