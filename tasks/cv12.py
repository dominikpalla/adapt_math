"""
Cvičení 12 — Primitivní funkce: linearita, per-partes, substituce.
"""


def _int(idx, fn, expected, cl="C", graph=None):
    """Standardní úloha „určete primitivní funkci" → mathlive výsledek bez +c
    (student doplní +c sám; my v Compute Engine porovnáme tvar bez konstanty)."""
    return {
        "task_id": f"cv12_{idx}",
        "content_latex": "Určete primitivní funkci k $f(x) = " + fn + "$.",
        "results": [{"key": "F", "label_latex": r"F(x) = ", "type": "mathlive",
                     "expected": expected, "tolerance": 0.0}],
        "cognitive_load": cl,
        "graph_vector": graph or ["Primitivní funkce"],
    }


TASKS = [
    # --------------------- 2 negace ---------------------
    {
        "task_id": "cv12_1",
        "content_latex": (
            r"Mějme funkci $f$ a k ní primitivní funkci $F$. Formulujte negaci výroku: "
            r"\textit{Je-li } $f$ \textit{ kladná na celém } $\mathbb{R},$ \textit{ potom } $F$ "
            r"\textit{ je na } $\mathbb{R}$ \textit{ rostoucí.}"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existují $f, F$ s $F' = f,$ $f > 0$ na $\mathbb{R}$ a přitom $F$ není rostoucí na $\mathbb{R}.$"},
                {"key": "b", "label_latex": r"Pokud je $f$ kladná, pak $F$ není rostoucí."},
                {"key": "c", "label_latex": r"Existují $f, F$ s $F' = f,$ $f \le 0$ na $\mathbb{R}$ a $F$ rostoucí."},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků", "Primitivní funkce"],
    },
    {
        "task_id": "cv12_2",
        "content_latex": (
            r"Formulujte negaci výroku: \textit{Je-li } $F$ \textit{ primitivní funkcí k } $f$ "
            r"\textit{ a } $G$ \textit{ k } $g,$ \textit{ pak pro všechna } $\alpha, \beta \in \mathbb{R}$ "
            r"\textit{ je } $\alpha F + \beta G$ \textit{ primitivní funkcí k } $\alpha f + \beta g.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existují $F, G, f, g$ s $F' = f,\ G' = g$ a $\alpha, \beta \in \mathbb{R}$ takové, že $\alpha F + \beta G$ není primitivní k $\alpha f + \beta g.$"},
                {"key": "b", "label_latex": r"Pro každé $\alpha, \beta$ je $\alpha F + \beta G$ neprim. k $\alpha f + \beta g.$"},
                {"key": "c", "label_latex": r"Existují $\alpha, \beta$ taková, že $\alpha F + \beta G$ je primitivní k $\alpha f - \beta g.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Negace výroků", "Primitivní funkce"],
    },

    # --------------------- 10 podul: linearita ---------------------
    _int(3,  r"2x - 3",                                 r"x^2 - 3x",                                    "B"),
    _int(4,  r"x^4 - 3x^3 + \tfrac{x^2}{2} - 4",        r"\frac{x^5}{5} - \frac{3 x^4}{4} + \frac{x^3}{6} - 4x", "C"),
    _int(5,  r"2\sqrt{x} + 6\cos x",                    r"\frac{4}{3} x^{3/2} + 6 \sin x",              "C"),
    _int(6,  r"\frac{(x - 2)^2}{x^3}",                  r"\ln|x| + \frac{4}{x} - \frac{2}{x^2}",        "D"),
    _int(7,  r"\frac{x - 2\sqrt{x} + 2}{x^2 \sqrt[3]{x}}",
            r"-3 x^{-1/3} + \frac{12}{5} x^{-5/6} - \frac{3}{2} x^{-4/3}", "E"),
    _int(8,  r"\frac{x^2 - 1}{x^2 + 1}",                r"x - 2 \arctan x",                              "C"),
    _int(9,  r"\frac{\cos 2x}{\sin^2 x}",               r"-\cot x - 2x",                                 "D"),
    _int(10, r"\frac{\sin 2x}{2 \cos x}",               r"-\cos x",                                      "C"),
    _int(11, r"\frac{1}{x}(2 - x e^x)",                 r"2 \ln|x| - e^x",                               "C"),
    _int(12, r"\frac{e^{2x} + 2 e^x}{e^x}",             r"e^x + 2x",                                     "C"),

    # --------------------- 21 podul: per-partes ---------------------
    _int(13, r"x e^x",                                  r"e^x(x - 1)",                                   "C"),
    _int(14, r"x \sin x",                               r"-x \cos x + \sin x",                           "C"),
    _int(15, r"x \ln x",                                r"\frac{1}{2} x^2 \left(\ln x - \frac{1}{2}\right)", "D"),
    _int(16, r"x^4 \ln x",                              r"\frac{x^5}{5} \left(\ln x - \frac{1}{5}\right)", "D"),
    _int(17, r"\frac{\ln x}{x^5}",                      r"-\frac{1}{4 x^4} \left(\ln x + \frac{1}{4}\right)", "E"),
    _int(18, r"\sqrt{x} \ln x",                         r"\frac{2}{3} x \sqrt{x} \left(\ln x - \frac{2}{3}\right)", "D"),
    _int(19, r"16 \sqrt[3]{x} \ln x",                   r"3 x \sqrt[3]{x} (4 \ln x - 3)",                "D"),
    _int(20, r"\ln x",                                  r"x(\ln x - 1)",                                 "C"),
    _int(21, r"\ln(x + 5)",                             r"(x + 5) \ln(x + 5) - x",                       "C"),
    _int(22, r"\arcsin x",                              r"x \arcsin x + \sqrt{1 - x^2}",                 "D"),
    _int(23, r"x^2 \sin x",                             r"-x^2 \cos x + 2x \sin x + 2 \cos x",           "D"),
    _int(24, r"2x \arctan x",                           r"(1 + x^2) \arctan x - x",                      "D"),
    _int(25, r"\ln^2 x",                                r"x(\ln^2 x - 2 \ln x + 2)",                     "D"),
    _int(26, r"\ln^3 x",                                r"x(\ln^3 x - 3 \ln^2 x + 6 \ln x - 6)",         "E"),
    _int(27, r"\cos^3 x",                               r"\sin x - \frac{\sin^3 x}{3}",                  "D"),
    _int(28, r"x \sqrt{x + 3}",                         r"\frac{2}{5} (x + 3)^{3/2} (x - 2)",            "D"),
    _int(29, r"\left(\frac{\ln x}{x}\right)^2",         r"-\frac{1}{x} (\ln^2 x + 2 \ln x + 2)",         "E"),
    _int(30, r"\sin x \cos x",                          r"\frac{1}{2} \sin^2 x",                         "C"),
    _int(31, r"\frac{\ln x}{x}",                        r"\frac{1}{2} \ln^2 x",                          "C"),
    _int(32, r"e^x \sin x",                             r"\frac{e^x}{2} (\sin x - \cos x)",              "D"),
    _int(33, r"\cos \ln x",                             r"\frac{1}{2}(x \cos \ln x + x \sin \ln x)",     "E"),

    # --------------------- 18 podul: substituce (1. blok) ---------------------
    _int(34, r"\sin^7 x \cos x",                        r"\frac{\sin^8 x}{8}",                           "C"),
    _int(35, r"\sin x \cos x",                          r"\frac{1}{2} \sin^2 x",                         "C"),
    _int(36, r"\frac{e^x}{e^x + 1}",                    r"\ln(e^x + 1)",                                 "C"),
    _int(37, r"x \sqrt{1 - x^2}",                       r"-\frac{1}{3}(1 - x^2)^{3/2}",                  "C"),
    _int(38, r"x \sin(x^2)",                            r"-\frac{1}{2} \cos x^2",                        "C"),
    _int(39, r"\tan x",                                 r"-\ln|\cos x|",                                 "C"),
    _int(40, r"\frac{\ln^2 x}{x}",                      r"\frac{\ln^3 x}{3}",                            "C"),
    _int(41, r"\frac{\cos \ln x}{x}",                   r"\sin \ln x",                                   "C"),
    _int(42, r"\frac{\cos \sqrt{x}}{\sqrt{x}}",         r"2 \sin \sqrt{x}",                              "C"),
    _int(43, r"(2x + 5)(x^2 + 5x)^7",                   r"\frac{(x^2 + 5x)^8}{8}",                       "C"),
    _int(44, r"e^x (1 + 2 e^x)^4",                      r"\frac{(1 + 2 e^x)^5}{10}",                     "D"),
    _int(45, r"\frac{3x + 6}{x^2 + 4x - 3}",            r"\frac{3}{2} \ln|x^2 + 4x - 3|",                "D"),
    _int(46, r"\frac{3}{x \ln x}",                      r"3 \ln|\ln x|",                                 "D"),
    _int(47, r"\frac{\sqrt[3]{1 + \ln x}}{x}",          r"\frac{3}{4} (1 + \ln x)^{4/3}",                "D"),
    {"task_id":"cv12_48",
     "content_latex":r"Určete primitivní funkci k $f(x) = \dfrac{1}{a^2 + x^2},\ a \in \mathbb{R} \setminus \{0\}$.",
     "results":[{"key":"F","label_latex":r"F(x) = ","type":"mathlive",
                 "expected":r"\frac{1}{a} \arctan\frac{x}{a}"}],
     "cognitive_load":"C","graph_vector":["Primitivní funkce"]},
    {"task_id":"cv12_49",
     "content_latex":r"Určete primitivní funkci k $f(x) = \dfrac{1}{\sqrt{a^2 - x^2}},\ a \in \mathbb{R} \setminus \{0\}$.",
     "results":[{"key":"F","label_latex":r"F(x) = ","type":"mathlive",
                 "expected":r"\arcsin\frac{x}{a}"}],
     "cognitive_load":"C","graph_vector":["Primitivní funkce"]},
    _int(50, r"(x + 3)(x - 1)^5",                       r"\frac{(x - 1)^7}{7} + \frac{2 (x - 1)^6}{3}",  "D"),
    _int(51, r"\frac{x + 1}{x \sqrt{x - 2}}",
        r"2 \sqrt{x - 2} + \sqrt{2} \arctan \sqrt{\frac{x - 2}{2}}",                                    "F"),

    # --------------------- 7 podul: substituce (2. blok — pokročilá) ---------------------
    _int(52, r"x \sqrt{4 - x}",
        r"\frac{2}{5} (4 - x)^{5/2} - \frac{8}{3} (4 - x)^{3/2}",                                       "E"),
    _int(53, r"\frac{1}{1 + \sqrt{x}}",                 r"2\sqrt{x} - 2 \ln(\sqrt{x} + 1)",              "D"),
    _int(54, r"\frac{2 + \sqrt{x}}{3 - \sqrt{x}}",
        r"-x - 10 \sqrt{x} - 30 \ln|3 - \sqrt{x}|",                                                     "E"),
    _int(55, r"\frac{3}{4 + \sqrt[3]{x}}",
        r"\frac{9}{2} x^{2/3} - 36 x^{1/3} + 144 \ln|x^{1/3} + 4|",                                     "F"),
    _int(56, r"\sqrt{5 + \sqrt{x}}",
        r"\frac{4}{5} (5 + \sqrt{x})^{5/2} - \frac{20}{3} (5 + \sqrt{x})^{3/2}",                        "F"),
    _int(57, r"\frac{e^x - 1}{e^x + 1}",                r"-x + 2 \ln(e^x + 1)",                          "D"),
    _int(58, r"\sqrt{e^x - 1}",
        r"2 \sqrt{e^x - 1} - 2 \arctan\sqrt{e^x - 1}",                                                  "E"),
]
