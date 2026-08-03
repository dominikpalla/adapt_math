"""
SŠ 07 — Zjednodušte výraz (mocniny s racionálním exponentem, odmocniny, abs. hodnoty).

Zdroj: Overleaf `Andrea_příkladySŠ/Zjednodušte výraz.tex`.
Extrahováno 2026-08-03.
"""


def _simp(idx, expr, expected, cl="D"):
    return {
        "task_id": f"ss07_{idx:02d}",
        "content_latex": r"Zjednodušte výraz $" + expr + r"$.",
        "results": [{
            "key": "vysledek", "label_latex": r"= ", "type": "mathlive",
            "expected": expected, "tolerance": 0.0,
        }],
        "cognitive_load": cl,
    }


TASKS = [
    _simp(1,
        r"\left[\left(\frac{1}{2} \cdot \frac{1}{3}\right)^{\frac{1}{2}}\right]^{\frac{1}{3}} : "
        r"\left[\left(\frac{1}{2} \cdot 3^2\right)^{\frac{1}{3}}\right]^{\frac{1}{2}}",
        r"\frac{\sqrt{3}}{3}", "D"),
    _simp(2,
        r"\frac{\left(15^{\frac{1}{3}} \cdot 27^{-\frac{1}{2}}\right)^{-3}}"
        r"{\left(25^{\frac{1}{4}} \cdot 9^{\frac{1}{8}}\right)^{-2}} : "
        r"\frac{\sqrt[3]{9}}{\sqrt[3]{3 \cdot \sqrt[4]{27}}}",
        r"3^{\frac{47}{12}}", "E"),
    _simp(3,
        r"\sqrt[6]{\frac{5 \cdot \sqrt[3]{3}}{6}} : \sqrt[3]{\frac{6\sqrt{5}}{3\sqrt{3}}}",
        r"\frac{\sqrt[18]{3}}{\sqrt{2}}", "E"),
    _simp(4,
        r"7 \cdot 3^{\frac{2}{3}} + 6 \cdot 81^{\frac{1}{8}} - 8 \cdot 9^{\frac{1}{4}} - 5 \cdot 27^{\frac{2}{9}}",
        r"2\left(\sqrt[3]{9} - \sqrt{3}\right)", "D"),
    _simp(5,
        r"\frac{\left(10^{\frac{1}{3}} \cdot 8^{-\frac{1}{2}}\right)^{-3}}"
        r"{\left(25^{\frac{1}{4}} \cdot 4^{\frac{1}{8}}\right)^{-2}} : "
        r"\frac{\sqrt{2 \cdot \sqrt[3]{4}}}{\sqrt[3]{2 \cdot \sqrt[4]{8}}}",
        r"2^{\frac{15}{4}}", "E"),
    _simp(6,
        r"\frac{1 - \sqrt{3}}{1 + \left|2 - \sqrt{3}\right| + 2\left|1 - \sqrt{3}\right|}",
        r"-2 + \sqrt{3}", "D"),
    _simp(7,
        r"\left[\left(\frac{1}{2} \cdot \frac{1}{3}\right)^{\frac{1}{2}}\right]^{\frac{1}{3}} : "
        r"\left[\left(\frac{1}{2} \cdot 3^2\right)^{\frac{1}{3}}\right]^{\frac{1}{2}}",
        r"\frac{\sqrt{3}}{3}", "D"),
]
