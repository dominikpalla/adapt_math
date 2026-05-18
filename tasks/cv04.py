"""
Cvičení 4 — Limita funkce: definice a věta o aritmetice limit
Zdroj: skripta „Základy matematiky 1", Pavel Pražák a Petr Bauer (KIKM FIM UHK).
"""

TASKS = [
    # --- 4.1, 4.2, 4.3: negace výroků (multiple_choice s 3 možnostmi) ---
    {
        "task_id": "cv04_1",
        "content_latex": (
            r"Formulujte negaci výroku o tranzitivnosti uspořádání reálných čísel: "
            r"\textit{Pro libovolnou trojici } $x \in \mathbb{R},\ y \in \mathbb{R},\ z \in \mathbb{R}$ "
            r"\textit{ platí: jestliže } $x \le y$ \textit{ a } $y \le z,$ \textit{ pak } $x \le z.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje trojice $x, y, z \in \mathbb{R}$ taková, že $x \le y$ a $y \le z$ a zároveň $x > z.$"},
                {"key": "b", "label_latex": r"Pro libovolnou trojici $x, y, z \in \mathbb{R}$ platí: jestliže $x \le y$ a $y \le z,$ pak $x > z.$"},
                {"key": "c", "label_latex": r"Existuje trojice $x, y, z \in \mathbb{R}$ taková, že $x > y$ nebo $y > z$ a zároveň $x \le z.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "B",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
    },
    {
        "task_id": "cv04_2",
        "content_latex": (
            r"Formulujte negaci a obměnu výroku: "
            r"\textit{Jsou-li } $U_1(a)$ \textit{ a } $U_2(a)$ \textit{ okolí bodu } $a \in \mathbb{R}^*,$ "
            r"\textit{ potom } $U_1(a) \cap U_2(a)$ \textit{ je také okolí bodu } $a.$"
        ),
        "results": [
            {
                "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
                "options": [
                    {"key": "a", "label_latex": r"Existují okolí $U_1(a)$ a $U_2(a)$ bodu $a \in \mathbb{R}^*$ taková, že $U_1(a) \cap U_2(a)$ není okolí bodu $a.$"},
                    {"key": "b", "label_latex": r"Pro každá okolí $U_1(a)$ a $U_2(a)$ bodu $a \in \mathbb{R}^*$ platí, že $U_1(a) \cap U_2(a)$ není okolí bodu $a.$"},
                    {"key": "c", "label_latex": r"Existují okolí $U_1(a)$ a $U_2(a)$ bodu $a \in \mathbb{R}^*$ taková, že $U_1(a)$ nebo $U_2(a)$ není okolí bodu $a.$"},
                ],
                "expected": "a",
            },
            {
                "key": "obmena", "label_latex": r"\text{Obměna: }", "type": "multiple_choice",
                "options": [
                    {"key": "a", "label_latex": r"Jestliže $U_1(a) \cap U_2(a)$ není okolí bodu $a \in \mathbb{R}^*,$ potom $U_1(a)$ není okolí bodu $a$ nebo $U_2(a)$ není okolí bodu $a.$"},
                    {"key": "b", "label_latex": r"Jestliže $U_1(a) \cap U_2(a)$ není okolí bodu $a \in \mathbb{R}^*,$ potom $U_1(a)$ není okolí bodu $a$ a $U_2(a)$ není okolí bodu $a.$"},
                    {"key": "c", "label_latex": r"Jestliže $U_1(a) \cap U_2(a)$ je okolí bodu $a \in \mathbb{R}^*,$ potom $U_1(a)$ a $U_2(a)$ jsou okolí bodu $a.$"},
                ],
                "expected": "a",
            },
        ],
        "cognitive_load": "C",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
    },
    {
        "task_id": "cv04_3",
        "content_latex": (
            r"Formulujte negaci a obměnu výroku: "
            r"\textit{Jsou-li } $a, b \in \mathbb{R}^*,\ a \ne b,$ \textit{ pak existují } $U(a)$ "
            r"\textit{ a } $U(b)$ \textit{ taková, že } $U(a) \cap U(b) = \emptyset.$"
        ),
        "results": [
            {
                "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
                "options": [
                    {"key": "a", "label_latex": r"Existují $a, b \in \mathbb{R}^*,\ a \ne b,$ taková, že pro každá okolí $U(a)$ a $U(b)$ platí $U(a) \cap U(b) \ne \emptyset.$"},
                    {"key": "b", "label_latex": r"Pro každé $a, b \in \mathbb{R}^*,\ a \ne b,$ existují okolí $U(a)$ a $U(b)$ taková, že $U(a) \cap U(b) \ne \emptyset.$"},
                    {"key": "c", "label_latex": r"Existují $a, b \in \mathbb{R}^*,\ a = b,$ taková, že pro každá okolí $U(a)$ a $U(b)$ platí $U(a) \cap U(b) = \emptyset.$"},
                ],
                "expected": "a",
            },
            {
                "key": "obmena", "label_latex": r"\text{Obměna: }", "type": "multiple_choice",
                "options": [
                    {"key": "a", "label_latex": r"Jestliže pro každá okolí $U(a)$ a $U(b)$ bodů $a, b \in \mathbb{R}^*$ platí $U(a) \cap U(b) \ne \emptyset,$ pak $a = b.$"},
                    {"key": "b", "label_latex": r"Jestliže $a = b,$ pak pro nějaká okolí $U(a)$ a $U(b)$ platí $U(a) \cap U(b) \ne \emptyset.$"},
                    {"key": "c", "label_latex": r"Jestliže existují okolí $U(a)$ a $U(b)$ bodů $a, b \in \mathbb{R}^*$ taková, že $U(a) \cap U(b) \ne \emptyset,$ pak $a = b.$"},
                ],
                "expected": "a",
            },
        ],
        "cognitive_load": "C",
        "graph_vector": ["Negace výroků", "Limity funkcí"],
    },

    # --- 4.4 a)–o): aritmetika limit ---
    {"task_id": "cv04_4",
     "content_latex": r"\lim_{x \to 3} \frac{5x^2 - 8x - 13}{x^2 - 5}",
     "results": [{"key": "lim", "label_latex": "", "type": "decimal", "expected": 2.0, "tolerance": 0.001}],
     "cognitive_load": "B", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_5",
     "content_latex": r"\lim_{x \to 2} \frac{3x^2 - x - 10}{x^2 - 4}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"\frac{11}{4}"}],
     "cognitive_load": "C", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_6",
     "content_latex": r"\lim_{x \to 3} \frac{x^4 - 81}{2x^2 - 5x - 3}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"\frac{108}{7}"}],
     "cognitive_load": "C", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_7",
     "content_latex": r"\lim_{x \to -2} \frac{\frac{1}{x} + \frac{1}{2}}{x^3 + 8}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"-\frac{1}{48}"}],
     "cognitive_load": "D", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_8",
     "content_latex": r"\lim_{x \to 2} \frac{x^3 - 2x^2 - 4x + 8}{x^4 - 8x^2 + 16}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"\frac{1}{4}"}],
     "cognitive_load": "D", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_9",
     "content_latex": r"\lim_{x \to 2} \frac{x^4 - 2x^3 + 2x^2 - 5x + 2}{x - 2}",
     "results": [{"key": "lim", "label_latex": "", "type": "decimal", "expected": 11.0, "tolerance": 0.001}],
     "cognitive_load": "C", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_10",
     "content_latex": r"\lim_{x \to 4} \frac{3 - \sqrt{x + 5}}{x - 4}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"-\frac{1}{6}"}],
     "cognitive_load": "D", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_11",
     "content_latex": r"\lim_{x \to -1} \frac{x^3 + 1}{\sqrt{x^2 - 3x} + 2x}",
     "results": [{"key": "lim", "label_latex": "", "type": "decimal", "expected": 4.0, "tolerance": 0.001}],
     "cognitive_load": "D", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_12",
     "content_latex": r"\lim_{x \to 0} \frac{x^3 - 7x}{x^3}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"-\infty"}],
     "cognitive_load": "C", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_13",
     "content_latex": r"\lim_{x \to 0} \frac{x^2 - 1}{x^2}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"-\infty"}],
     "cognitive_load": "B", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_14",
     "content_latex": r"\lim_{x \to 0} \frac{x^4 + 5x - 3}{2 - \sqrt{x^2 + 4}}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"\infty"}],
     "cognitive_load": "D", "graph_vector": ["Limity funkcí"]},
    {
        # Limita zleva = -∞, zprava = +∞ → neexistuje.
        "task_id": "cv04_15",
        "content_latex": r"\lim_{x \to 1} \frac{x^3 - 1}{(x - 1)^2}",
        "results": [{
            "key": "lim", "label_latex": "", "type": "multiple_choice",
            "options": [
                {"key": "finite", "label_latex": r"\text{konečná hodnota}"},
                {"key": "plus_inf", "label_latex": r"+\infty"},
                {"key": "minus_inf", "label_latex": r"-\infty"},
                {"key": "dne", "label_latex": r"\text{limita neexistuje}"},
            ],
            "expected": "dne",
        }],
        "cognitive_load": "D", "graph_vector": ["Limity funkcí"],
    },
    {"task_id": "cv04_16",
     "content_latex": r"\lim_{x \to +\infty} \frac{x^2 + 3x - 4}{1 - 5x^2}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"-\frac{1}{5}"}],
     "cognitive_load": "B", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_17",
     "content_latex": r"\lim_{x \to +\infty} \frac{2x^2 + 7x - 2}{6x^3 - 4x + 3}",
     "results": [{"key": "lim", "label_latex": "", "type": "decimal", "expected": 0.0, "tolerance": 0.001}],
     "cognitive_load": "B", "graph_vector": ["Limity funkcí"]},
    {"task_id": "cv04_18",
     "content_latex": r"\lim_{x \to -\infty} \frac{(1 - 2x)^2 (3 - x)}{x^2 - 7x + 10}",
     "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"\infty"}],
     "cognitive_load": "C", "graph_vector": ["Limity funkcí"]},
]
