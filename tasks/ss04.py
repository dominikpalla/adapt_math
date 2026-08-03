"""
SŠ 04 — Rovnice s absolutní hodnotou.

Zdroj: Overleaf `Andrea_příkladySŠ/Rovnice s absolutní hodnotou.tex`.
Extrahováno 2026-08-03.
"""

TASKS = [
    {
        "task_id": "ss04_01",
        "content_latex": r"Řešte v $\mathbb{R}$ rovnici $2|x| = |4 - x| + 3$.",
        "results": [{
            "key": "x", "label_latex": r"x \in ", "type": "mathlive",
            "expected": r"\{-7,\ \frac{7}{3}\}", "tolerance": 0.0,
        }],
        "cognitive_load": "C",
    },
    {
        "task_id": "ss04_02",
        "content_latex": r"Řešte v $\mathbb{R}$ rovnici $|2x - 1| + |x + 5| = |2x + 3|$.",
        "results": [{
            "key": "x", "label_latex": r"x \in ", "type": "mathlive",
            "expected": r"\emptyset", "tolerance": 0.0,
        }],
        "cognitive_load": "C",
    },
    {
        "task_id": "ss04_03",
        "content_latex": r"Řešte v $\mathbb{R}$ rovnici $|2 - 3x| + |x - 4| = 5$.",
        "results": [{
            "key": "x", "label_latex": r"x \in ", "type": "mathlive",
            "expected": r"\{\frac{1}{4},\ \frac{3}{2}\}", "tolerance": 0.0,
        }],
        "cognitive_load": "C",
    },
    {
        "task_id": "ss04_04",
        "content_latex": r"Řešte v $\mathbb{R}$ rovnici $|x| = |2x + 3| + x - 1$.",
        "results": [{
            "key": "x", "label_latex": r"x = ", "type": "mathlive",
            "expected": r"-\frac{1}{2}", "tolerance": 0.0,
        }],
        "cognitive_load": "C",
    },
    {
        "task_id": "ss04_05",
        "content_latex": r"Řešte v $\mathbb{R}$ nerovnici $1 - |x - 3| \ge x - 2$.",
        "results": [{
            "key": "x", "label_latex": r"x \in ", "type": "mathlive",
            "expected": r"(-\infty,\ 3]", "tolerance": 0.0,
        }],
        "cognitive_load": "D",
    },
]
