"""
Cvičení 8 — Použití derivace: tečny a normály, absolutní extrémy, L'Hospital.
"""


def _lim(idx, content, expected, cl="C"):
    return {
        "task_id": f"cv08_{idx}",
        "content_latex": content,
        "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": expected}],
        "cognitive_load": cl, "graph_vector": ["Limity funkcí", "L'Hospital"],
    }


def _lim_dec(idx, content, value, tol=0.001, cl="C"):
    return {
        "task_id": f"cv08_{idx}",
        "content_latex": content,
        "results": [{"key": "lim", "label_latex": "", "type": "decimal", "expected": value, "tolerance": tol}],
        "cognitive_load": cl, "graph_vector": ["Limity funkcí", "L'Hospital"],
    }


TASKS = [
    # --------------------- 3 negace ---------------------
    {
        "task_id": "cv08_1",
        "content_latex": (
            r"Formulujte negaci výroku o neutrálním prvku pro sčítání: "
            r"\textit{Existuje } $0 \in \mathbb{R}$ \textit{ takové, že pro každé } $x \in \mathbb{R}$ "
            r"\textit{ platí } $x + 0 = x.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Pro každé $0 \in \mathbb{R}$ existuje $x \in \mathbb{R}$ takové, že $x + 0 \ne x.$"},
                {"key": "b", "label_latex": r"Pro každé $0 \in \mathbb{R}$ a každé $x \in \mathbb{R}$ platí $x + 0 \ne x.$"},
                {"key": "c", "label_latex": r"Existuje $0 \in \mathbb{R}$ takové, že pro každé $x \in \mathbb{R}$ platí $x + 0 \ne x.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv08_2",
        "content_latex": (
            r"Formulujte negaci výroku o opačném prvku: "
            r"\textit{Pro každé } $x \in \mathbb{R}$ \textit{ existuje } $y \in \mathbb{R}$ "
            r"\textit{ takové, že } $x + y = 0.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $x \in \mathbb{R}$ takové, že pro každé $y \in \mathbb{R}$ platí $x + y \ne 0.$"},
                {"key": "b", "label_latex": r"Pro každé $x \in \mathbb{R}$ existuje $y \in \mathbb{R}$ takové, že $x + y \ne 0.$"},
                {"key": "c", "label_latex": r"Pro každé $x, y$ platí $x + y \ne 0.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv08_3",
        "content_latex": (
            r"Formulujte negaci výroku o komutativitě násobení: "
            r"\textit{Pro každou dvojici } $x, y \in \mathbb{R}$ \textit{ platí } $x \cdot y = y \cdot x.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje dvojice $x, y \in \mathbb{R}$ taková, že $x \cdot y \ne y \cdot x.$"},
                {"key": "b", "label_latex": r"Pro každou dvojici platí $x \cdot y \ne y \cdot x.$"},
                {"key": "c", "label_latex": r"Existuje dvojice $x, y$ taková, že $x \cdot y = y \cdot x.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },

    # --------------------- 7 podul: tečna + normála ---------------------
    {
        "task_id": "cv08_4",
        "content_latex": r"Napište rovnice tečny $t$ a normály $n$ ke grafu funkce $y = x^2 \ln x$ v bodě $A = [1, 0]$.",
        "results": [
            {"key": "t", "label_latex": r"t:\ ", "type": "mathlive", "expected": r"y = x - 1"},
            {"key": "n", "label_latex": r"n:\ ", "type": "mathlive", "expected": r"y = -x + 1"},
        ],
        "cognitive_load": "C", "graph_vector": ["Tečna a normála"],
    },
    {
        "task_id": "cv08_5",
        "content_latex": r"Napište rovnice tečny $t$ a normály $n$ ke grafu funkce $y = x + \sqrt{1 - x}$ v bodě $A = [0, ?]$.",
        "results": [
            {"key": "t", "label_latex": r"t:\ ", "type": "mathlive", "expected": r"x - 2y + 2 = 0"},
            {"key": "n", "label_latex": r"n:\ ", "type": "mathlive", "expected": r"2x + y - 1 = 0"},
        ],
        "cognitive_load": "D", "graph_vector": ["Tečna a normála"],
    },
    {
        "task_id": "cv08_6",
        "content_latex": r"Napište rovnice tečny $t$ a normály $n$ ke grafu funkce $y = 2 + \tan^2 x$ v bodě $A = [0, ?]$.",
        "results": [
            {"key": "t", "label_latex": r"t:\ ", "type": "mathlive", "expected": r"y = 2"},
            {"key": "n", "label_latex": r"n:\ ", "type": "mathlive", "expected": r"x = 0"},
        ],
        "cognitive_load": "C", "graph_vector": ["Tečna a normála"],
    },
    {
        "task_id": "cv08_7",
        "content_latex": r"Napište rovnice tečny $t$ a normály $n$ ke grafu funkce $y = \dfrac{2x + 1}{x^2}$ v bodě $A = [-2, ?]$.",
        "results": [
            {"key": "t", "label_latex": r"t:\ ", "type": "mathlive", "expected": r"x + 4y + 5 = 0"},
            {"key": "n", "label_latex": r"n:\ ", "type": "mathlive", "expected": r"16x - 4y + 29 = 0"},
        ],
        "cognitive_load": "D", "graph_vector": ["Tečna a normála"],
    },
    {
        "task_id": "cv08_8",
        "content_latex": r"Napište rovnice tečny $t$ a normály $n$ ke grafu funkce $y = \arctan\dfrac{2x - 3}{3x + 2}$ v bodě $A = \left[\tfrac{3}{2}, ?\right]$.",
        "results": [
            {"key": "t", "label_latex": r"t:\ ", "type": "mathlive", "expected": r"4x - 13y - 6 = 0"},
            {"key": "n", "label_latex": r"n:\ ", "type": "mathlive", "expected": r"26x + 8y - 39 = 0"},
        ],
        "cognitive_load": "E", "graph_vector": ["Tečna a normála"],
    },
    {
        "task_id": "cv08_9",
        "content_latex": r"Napište rovnice tečny $t$ a normály $n$ ke grafu funkce $y = 3 e^{2x} + 4x^2 + 6$ v bodě $A = [0, ?]$.",
        "results": [
            {"key": "t", "label_latex": r"t:\ ", "type": "mathlive", "expected": r"6x - y + 9 = 0"},
            {"key": "n", "label_latex": r"n:\ ", "type": "mathlive", "expected": r"x + 6y - 54 = 0"},
        ],
        "cognitive_load": "C", "graph_vector": ["Tečna a normála"],
    },
    {
        "task_id": "cv08_10",
        "content_latex": r"Napište rovnice tečny $t$ a normály $n$ ke grafu funkce $y = x^2 \sqrt{x^3 - 7}$ v bodě $A = [2, ?]$.",
        "results": [
            {"key": "t", "label_latex": r"t:\ ", "type": "mathlive", "expected": r"28x - y - 52 = 0"},
            {"key": "n", "label_latex": r"n:\ ", "type": "mathlive", "expected": r"x + 28y - 114 = 0"},
        ],
        "cognitive_load": "D", "graph_vector": ["Tečna a normála"],
    },

    # --------------------- 2 úlohy: tečna rovnoběžná / kolmá ---------------------
    {
        "task_id": "cv08_11",
        "content_latex": r"Napište rovnici tečny ke grafu funkce $y = \arccos(1 - 2x)$ rovnoběžné s přímkou $2x - y = 4$.",
        "results": [{"key": "t", "label_latex": r"t:\ ", "type": "mathlive",
                     "expected": r"4x - 2y + \pi - 2 = 0"}],
        "cognitive_load": "E", "graph_vector": ["Tečna a normála"],
    },
    {
        "task_id": "cv08_12",
        "content_latex": r"Napište rovnici tečny ke grafu funkce $y = x^3 + 3x^2 - 5$ kolmé k přímce $2x - 6y + 1 = 0$.",
        "results": [{"key": "t", "label_latex": r"t:\ ", "type": "mathlive",
                     "expected": r"3x + y + 6 = 0"}],
        "cognitive_load": "D", "graph_vector": ["Tečna a normála"],
    },

    # --------------------- 7 podul: absolutní extrémy ---------------------
    {
        "task_id": "cv08_13",
        "content_latex": r"Najděte absolutní extrémy funkce $y = \dfrac{x}{x^2 + 2}$ na intervalu $[-1, 4]$.",
        "results": [
            {"key": "max_x", "label_latex": r"x_{\max} = ", "type": "mathlive", "expected": r"\sqrt{2}"},
            {"key": "max_y", "label_latex": r"f_{\max} = ", "type": "mathlive", "expected": r"\frac{\sqrt{2}}{4}"},
            {"key": "min_x", "label_latex": r"x_{\min} = ", "type": "decimal", "expected": -1, "tolerance": 0.001},
            {"key": "min_y", "label_latex": r"f_{\min} = ", "type": "mathlive", "expected": r"-\frac{1}{3}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Absolutní extrémy"],
    },
    {
        "task_id": "cv08_14",
        "content_latex": r"Najděte absolutní extrémy funkce $y = x^{2/3}(x - 20)$ na intervalu $[-1, 20]$.",
        "results": [
            {"key": "max", "label_latex": r"f_{\max} = ", "type": "decimal", "expected": 0, "tolerance": 0.001},
            {"key": "min_x", "label_latex": r"x_{\min} = ", "type": "decimal", "expected": 8, "tolerance": 0.001},
            {"key": "min_y", "label_latex": r"f_{\min} = ", "type": "decimal", "expected": -48, "tolerance": 0.01},
        ],
        "cognitive_load": "D", "graph_vector": ["Absolutní extrémy"],
    },
    {
        "task_id": "cv08_15",
        "content_latex": r"Najděte absolutní extrémy funkce $y = \dfrac{x + 1}{x^2 + 2x + 2}$ na intervalu $[-7, 0]$.",
        "results": [
            {"key": "max_x", "label_latex": r"x_{\max} = ", "type": "decimal", "expected": 0, "tolerance": 0.001},
            {"key": "max_y", "label_latex": r"f_{\max} = ", "type": "mathlive", "expected": r"\frac{1}{2}"},
            {"key": "min_x", "label_latex": r"x_{\min} = ", "type": "decimal", "expected": -2, "tolerance": 0.001},
            {"key": "min_y", "label_latex": r"f_{\min} = ", "type": "mathlive", "expected": r"-\frac{1}{2}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Absolutní extrémy"],
    },
    {
        "task_id": "cv08_16",
        "content_latex": r"Najděte absolutní extrémy funkce $y = x\sqrt{4 - x^2}$ na intervalu $[-1, 2]$.",
        "results": [
            {"key": "max_x", "label_latex": r"x_{\max} = ", "type": "mathlive", "expected": r"\sqrt{2}"},
            {"key": "max_y", "label_latex": r"f_{\max} = ", "type": "decimal", "expected": 2, "tolerance": 0.001},
            {"key": "min_x", "label_latex": r"x_{\min} = ", "type": "decimal", "expected": -1, "tolerance": 0.001},
            {"key": "min_y", "label_latex": r"f_{\min} = ", "type": "mathlive", "expected": r"-\sqrt{3}"},
        ],
        "cognitive_load": "D", "graph_vector": ["Absolutní extrémy"],
    },
    {
        "task_id": "cv08_17",
        "content_latex": r"Najděte absolutní extrémy funkce $y = \dfrac{\ln x}{x^3}$ na intervalu $[e^{-1}, e]$.",
        "results": [
            {"key": "max", "label_latex": r"f_{\max} = ", "type": "mathlive", "expected": r"\frac{1}{3e}"},
            {"key": "min", "label_latex": r"f_{\min} = ", "type": "mathlive", "expected": r"-e^3"},
        ],
        "cognitive_load": "E", "graph_vector": ["Absolutní extrémy"],
    },
    {
        "task_id": "cv08_18",
        "content_latex": r"Najděte absolutní extrémy funkce $y = x^2 e^{-x^2}$ na intervalu $[-2, 2]$.",
        "results": [
            {"key": "max", "label_latex": r"f_{\max} = ", "type": "mathlive", "expected": r"\frac{1}{e}"},
            {"key": "min", "label_latex": r"f_{\min} = ", "type": "decimal", "expected": 0, "tolerance": 0.001},
        ],
        "cognitive_load": "D", "graph_vector": ["Absolutní extrémy"],
    },
    {
        "task_id": "cv08_19",
        "content_latex": r"Najděte absolutní extrémy funkce $y = (x^2 + x)^{2/3}$ na intervalu $[-2, 3]$.",
        "results": [
            {"key": "max", "label_latex": r"f_{\max} = ", "type": "mathlive", "expected": r"\sqrt[3]{144}"},
            {"key": "min", "label_latex": r"f_{\min} = ", "type": "decimal", "expected": 0, "tolerance": 0.001},
        ],
        "cognitive_load": "D", "graph_vector": ["Absolutní extrémy"],
    },

    # --------------------- 17 podul: L'Hospital ---------------------
    _lim_dec(20, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 1}\dfrac{x^3 - x^2 + x - 1}{x + \ln x - 1}.$", 1, 0.001, "C"),
    _lim(21, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}\dfrac{x + \sin 2x}{x - \sin x}.$", r"\infty", "C"),
    _lim_dec(22, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}\dfrac{x + \sin 2x}{x - \sin x^2}.$", 3, 0.001, "D"),
    _lim_dec(23, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0^+} x^x.$", 1, 0.001, "C"),
    _lim(24, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}\left(\dfrac{1}{\ln(x + 1)} - \dfrac{1}{x}\right).$", r"\frac{1}{2}", "D"),
    _lim_dec(25, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to \infty}\dfrac{\ln x + 2x}{x - 3}.$", 2, 0.001, "C"),
    _lim_dec(26, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to -\infty} x e^x.$", 0, 0.001, "C"),
    _lim_dec(27, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0^+}(\sin x \cdot \ln x).$", 0, 0.001, "C"),
    _lim_dec(28, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}\dfrac{x e^x}{e^x - \cos x}.$", 1, 0.001, "C"),
    _lim(29, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0^+}\left(\dfrac{1}{x} + \ln x\right).$", r"\infty", "D"),
    _lim(30, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}\dfrac{\sin x - x \cos x}{\sin^3 x}.$", r"\frac{1}{3}", "D"),
    _lim(31, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to \infty}(\ln x - \sqrt{x}).$", r"-\infty", "D"),
    _lim_dec(32, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 1^+}(\ln x \cdot \ln(x - 1)).$", 0, 0.001, "D"),
    _lim(33, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}\dfrac{1 + x - e^x}{x^2}.$", r"-\frac{1}{2}", "C"),
    _lim_dec(34, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}\dfrac{1 - \cos x}{3^x - 2^x}.$", 0, 0.001, "D"),
    _lim(35, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}(1 + \sin 2x)^{\frac{1}{x}}.$", r"e^2", "D"),
    _lim_dec(36, r"Pomocí L'Hospitalova pravidla určete $\lim_{x \to 0}\left(\dfrac{1}{\sin x} - \dfrac{1}{x}\right).$", 0, 0.001, "D"),
]
