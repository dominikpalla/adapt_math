"""
Cvičení 13 — Integrace racionálních funkcí (parciální zlomky).
"""


def _int(idx, fn, expected, cl="D"):
    return {
        "task_id": f"cv13_{idx:02d}",
        "content_latex": "Určete primitivní funkci k racionální funkci $f(x) = " + fn + "$.",
        "results": [{"key": "F", "label_latex": r"F(x) = ", "type": "mathlive",
                     "expected": expected, "tolerance": 0.0}],
        "cognitive_load": cl,
        "graph_vector": ["Primitivní funkce", "Racionální funkce", "Parciální zlomky"],
    }


TASKS = [
    _int(1,  r"\frac{x^3}{x - 2}",
        r"\frac{x^3}{3} + x^2 + 4x + 8 \ln|x - 2|", "C"),
    _int(2,  r"\frac{x - 4}{(x - 2)(x - 3)}",
        r"\ln\frac{(x - 2)^2}{|x - 3|}", "D"),
    _int(3,  r"\frac{2x + 7}{x^2 + x - 2}",
        r"\ln\left|\frac{(x - 1)^3}{x + 2}\right|", "D"),
    _int(4,  r"\frac{(x + 1)^3}{x^2 - x}",
        r"\frac{1}{2} x^2 + 4x - \ln|x| + 8 \ln|x - 1|", "E"),
    _int(5,  r"\frac{3x + 2}{x (x + 1)^2}",
        r"2 \ln\left|\frac{x}{x + 1}\right| - \frac{1}{x + 1}", "E"),
    _int(6,  r"\frac{x^2 + x - 1}{x^3 + x^2 - 6x}",
        r"\frac{1}{6} \ln|x| + \frac{1}{2} \ln|x - 2| + \frac{1}{3} \ln|x + 3|", "E"),
    _int(7,  r"\frac{3x^3 + 5x^2 - 25x - 1}{(x + 2)(x - 1)^2}",
        r"3x + \frac{6}{x - 1} + 5 \ln|x + 2|", "E"),
    _int(8,  r"\frac{2x^2 - 3x + 3}{x^3 - 2x^2 + x}",
        r"3 \ln|x| - \frac{2}{x - 1} - \ln|x - 1|", "E"),
    _int(9,  r"\frac{1}{(x^2 + 1)(x^2 + 4)}",
        r"\frac{1}{3} \arctan x - \frac{1}{6} \arctan\frac{x}{2}", "F"),
    _int(10, r"\frac{1}{x^3 - 2x^2 + x}",
        r"\ln|x| - \ln|x - 1| - \frac{1}{x - 1}", "E"),
]
