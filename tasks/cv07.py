"""
Cvičení 7 — Derivace: věty o derivaci součtu, součinu, podílu a složené funkce.
"""


def _der(idx, expr, expected, cl="C", graph=None):
    """Derivace funkce — výsledek y' = ..."""
    return {
        "task_id": f"cv07_{idx}",
        "content_latex": "Vypočítejte derivaci funkce $y = " + expr + "$.",
        "results": [{"key": "y_der", "label_latex": r"y' = ", "type": "mathlive", "expected": expected}],
        "cognitive_load": cl,
        "graph_vector": graph or ["Derivace"],
    }


TASKS = [
    # --------------------- 3 negace ---------------------
    {
        "task_id": "cv07_1",
        "content_latex": (
            r"Formulujte negaci výroku: \textit{Pro každou dvojici } $x, y \in \mathbb{R}$ \textit{ platí: "
            r"je-li } $0 \le x$ \textit{ a } $0 \le y,$ \textit{ pak } $0 \le x \cdot y.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje dvojice $x, y$ taková, že $0 \le x$ a $0 \le y$ a zároveň $x \cdot y < 0.$"},
                {"key": "b", "label_latex": r"Pro každou dvojici platí: je-li $0 \le x$ a $0 \le y,$ pak $x \cdot y < 0.$"},
                {"key": "c", "label_latex": r"Existuje dvojice $x, y$ taková, že $x < 0$ nebo $y < 0$ a zároveň $x \cdot y \ge 0.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv07_2",
        "content_latex": (
            r"Formulujte negaci věty: \textit{Jestliže má } $f$ \textit{ v bodě } $a$ \textit{ konečné "
            r"obě jednostranné derivace, pak je } $f$ \textit{ v bodě } $a$ \textit{ spojitá.}"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $f$ a bod $a$ tak, že $f$ má v $a$ obě jednostranné derivace konečné a zároveň není v $a$ spojitá."},
                {"key": "b", "label_latex": r"Existuje $f$ a bod $a$ tak, že $f$ nemá konečné jednostranné derivace a je v $a$ spojitá."},
                {"key": "c", "label_latex": r"Jestliže má $f$ v $a$ konečné jednostranné derivace, pak $f$ není v $a$ spojitá."},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Derivace"],
    },
    {
        "task_id": "cv07_3",
        "content_latex": (
            r"Formulujte negaci věty: \textit{Jestliže má } $f$ \textit{ v bodě } $a$ \textit{ derivaci "
            r"a lokální extrém, pak } $f'(a) = 0.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $f$ a bod $a$ tak, že $f$ má v $a$ derivaci a lokální extrém a zároveň $f'(a) \ne 0.$"},
                {"key": "b", "label_latex": r"Existuje $f$ a bod $a$ s $f'(a) = 0$ bez lokálního extrému."},
                {"key": "c", "label_latex": r"Jestliže má $f$ v $a$ derivaci a lokální extrém, pak $f'(a) \ne 0.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Derivace"],
    },

    # --------------------- 4 derivace (polynomy, mocniny, odmocniny) ---------------------
    _der(4,  r"2 + x + x^2",                                  r"1 + 2x", "B"),
    _der(5,  r"\frac{x^3}{3} + \frac{x^2}{2} - 2x",           r"x^2 + x - 2", "B"),
    _der(6,  r"\frac{3}{x^3} + \frac{2}{x^2} + \frac{1}{x}",  r"-9 x^{-4} - 4 x^{-3} - x^{-2}", "C"),
    _der(7,  r"2\sqrt{x} + 3\sqrt[3]{x} - 4\sqrt[6]{x}",      r"x^{-1/2} + x^{-2/3} - \tfrac{2}{3} x^{-5/6}", "C"),

    # --------------------- 14 derivace (součin / produktové pravidlo) ---------------------
    _der(8,  r"(x^2 + 3x - 1)(2x + 3)",        r"6x^2 + 18x + 7", "C"),
    _der(9,  r"x \ln x",                       r"\ln x + 1", "B"),
    _der(10, r"\ln^2 x",                       r"\frac{2 \ln x}{x}", "C"),
    _der(11, r"e^x(x^2 - 2x + 2)",             r"x^2 e^x", "D"),
    _der(12, r"e^x(x^3 - 3x^2 + 6x - 6)",      r"x^3 e^x", "D"),
    _der(13, r"x(\sin x + \ln x)",             r"\sin x + x \cos x + \ln x + 1", "C"),
    _der(14, r"(x^2 + 1) \sin x",              r"2x \sin x + (x^2 + 1) \cos x", "C"),
    _der(15, r"\sin x \cos x",                 r"\cos 2x", "C"),
    _der(16, r"e^x \ln x",                     r"e^x \ln x + \frac{e^x}{x}", "C"),
    _der(17, r"\frac{x - \sin x \cos x}{2}",   r"\sin^2 x", "D"),
    _der(18, r"x \sin x + \cos x",             r"x \cos x", "C"),
    _der(19, r"x \ln x - x",                   r"\ln x", "C"),
    _der(20, r"e^x(\sin x - \cos x)",          r"2 e^x \sin x", "D"),
    _der(21, r"-\frac{x}{2} + \frac{1 + x^2}{2} \arctan x",   r"x \arctan x", "D"),

    # --------------------- 9 derivace (podíl) ---------------------
    _der(22, r"\frac{2x}{1 - x^2}",            r"\frac{2(1 + x^2)}{(1 - x^2)^2}", "C"),
    _der(23, r"\frac{x^2 - 1}{x^2 + 1}",       r"\frac{4x}{(x^2 + 1)^2}", "C"),
    _der(24, r"\frac{x^2}{x + 1}",             r"\frac{x^2 + 2x}{(x + 1)^2}", "C"),
    _der(25, r"\frac{1 + x - x^2}{1 - x + x^2}", r"\frac{2(1 - 2x)}{(1 - x + x^2)^2}", "D"),
    _der(26, r"\frac{\sin x}{1 - \cos x}",     r"\frac{1}{\cos x - 1}", "D"),
    _der(27, r"\frac{1 - \cos x}{\sin x + \cos x}", r"\frac{1 + \sin x - \cos x}{1 + \sin 2x}", "E"),
    _der(28, r"\frac{e^x + 1}{e^x - 1}",       r"\frac{-2 e^x}{(e^x - 1)^2}", "C"),
    _der(29, r"\frac{2 \sin x}{\sin x - \cos x}", r"\frac{2}{\sin 2x - 1}", "D"),
    _der(30, r"\frac{x \ln x}{1 + \ln x}",     r"\frac{\ln^2 x + \ln x + 1}{(1 + \ln x)^2}", "E"),

    # --------------------- 17 derivace (řetízkové pravidlo) ---------------------
    _der(31, r"\sqrt{x^2 + 3x + 1}",           r"\frac{2x + 3}{2\sqrt{x^2 + 3x + 1}}", "C"),
    _der(32, r"(x^2 + 5x + 7)^8",              r"8(x^2 + 5x + 7)^7 (2x + 5)", "C"),
    _der(33, r"\sqrt{\ln x}",                  r"\frac{1}{2x \sqrt{\ln x}}", "C"),
    _der(34, r"\sqrt{1 + \ln^2 x}",            r"\frac{\ln x}{x \sqrt{1 + \ln^2 x}}", "D"),
    _der(35, r"e^{\sqrt{x + 1}}",              r"\frac{e^{\sqrt{x + 1}}}{2 \sqrt{x + 1}}", "C"),
    _der(36, r"\ln(x^3 + 7x + 2)",             r"\frac{3x^2 + 7}{x^3 + 7x + 2}", "C"),
    _der(37, r"\ln \cos x",                    r"-\tan x", "C"),
    _der(38, r"\ln \frac{2 - x}{2 + x}",       r"\frac{4}{x^2 - 4}", "D"),
    _der(39, r"\ln(\tan x)",                   r"\frac{2}{\sin 2x}", "C"),
    _der(40, r"\ln(x + \sqrt{x^2 + 1})",       r"\frac{1}{\sqrt{x^2 + 1}}", "D"),
    _der(41, r"\ln(x - \sqrt{x^2 - 1})",       r"-\frac{1}{\sqrt{x^2 - 1}}", "D"),
    _der(42, r"\ln^2 x + \ln(\ln x)",          r"\frac{2 \ln^2 x + 1}{x \ln x}", "D"),
    _der(43, r"\arctan \frac{1 + x}{1 - x}",   r"\frac{1}{1 + x^2}", "D"),
    _der(44, r"\arcsin \frac{x}{\sqrt{x^2 + 1}}", r"\frac{1}{1 + x^2}", "D"),
    _der(45, r"\ln(2x + 1 + 2\sqrt{x^2 + x})", r"\frac{1}{\sqrt{x^2 + x}}", "E"),
    _der(46, r"\ln \sqrt{\frac{1 + \sin x}{1 - \sin x}}", r"\frac{1}{\cos x}", "E"),
    _der(47, r"\ln \frac{x + \sqrt{x^2 - 1}}{x}", r"\frac{x - \sqrt{x^2 - 1}}{x \sqrt{x^2 - 1}}", "F"),
]
