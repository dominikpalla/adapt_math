"""
SŠ 05 — Složené funkce (vnitřní/vnější funkce, skládání).

Zdroj: Overleaf `Andrea_příkladySŠ/Složené funkce.tex`.
Extrahováno 2026-08-03.
"""


def _rozklad(idx, y_latex, f_expected, g_expected, cl="B"):
    """Rozložení y = f(g(x)) na vnitřní/vnější funkci."""
    return {
        "task_id": f"ss05_{idx:02d}",
        "content_latex": r"Určete vnitřní a vnější funkci pro $y = " + y_latex + r"$.",
        "results": [
            {"key": "f", "label_latex": r"f(x) = ", "type": "mathlive",
             "expected": f_expected, "tolerance": 0.0},
            {"key": "g", "label_latex": r"g(x) = ", "type": "mathlive",
             "expected": g_expected, "tolerance": 0.0},
        ],
        "cognitive_load": cl,
    }


def _slozene(idx, h_def, h_expr, D_expected, cl="C"):
    """Vytvoření složené funkce podle zadaného předpisu + definiční obor."""
    return {
        "task_id": f"ss05_{idx:02d}",
        "content_latex": (
            r"Jsou dány funkce $f(x) = x - 1$, $g(x) = \sqrt{x}$, $h(x) = x + 3$. "
            r"Určete složenou funkci a její definiční obor: " + h_def + r"$."
        ),
        "results": [
            {"key": "h", "label_latex": r"h(x) = ", "type": "mathlive",
             "expected": h_expr, "tolerance": 0.0},
            {"key": "D", "label_latex": r"D(h) = ", "type": "mathlive",
             "expected": D_expected, "tolerance": 0.0},
        ],
        "cognitive_load": cl,
    }


TASKS = [
    # Úloha 1: rozklad na vnitřní/vnější
    _rozklad(1, r"6\sqrt{x - 4}",      r"6\sqrt{x}",       r"x - 4"),
    _rozklad(2, r"\sqrt{x^2 - 4x}",    r"\sqrt{x}",        r"x^2 - 4x"),
    _rozklad(3, r"\log^2 x",           r"x^2",             r"\log x"),
    _rozklad(4, r"\log x^2",           r"\log x",          r"x^2"),
    _rozklad(5, r"5^{\sqrt{x}}",        r"5^x",             r"\sqrt{x}"),
    _rozklad(6, r"\sqrt{5^x}",         r"\sqrt{x}",        r"5^x"),
    _rozklad(7, r"\log^2 x - 4\log x", r"x^2 - 4x",        r"\log x", "C"),
    _rozklad(8, r"(x^2 + 1)^3",        r"x^3",             r"x^2 + 1"),

    # Úloha 2: skládání konkrétních funkcí + definiční obor
    _slozene(9,  r"$h_1(x) = g(h(f(x)))",
             r"\sqrt{x + 2}",              r"[-2, \infty)"),
    _slozene(10, r"$h_2(x) = f(h(g(x)))",
             r"\sqrt{x} + 2",              r"[0, \infty)"),
    _slozene(11, r"$h_3(x) = f(g(h(x)))",
             r"\sqrt{x + 3} - 1",          r"[-3, \infty)"),
    _slozene(12, r"$h_4(x) = h(g(f(x)))",
             r"\sqrt{x - 1} + 3",          r"[1, \infty)"),
]
