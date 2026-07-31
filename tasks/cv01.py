"""
Cvičení 1 — Funkce, definiční obor funkce, kvadratická funkce
Zdroj: skripta „Základy matematiky 1", Pavel Pražák a Petr Bauer (KIKM FIM UHK)

Strategie kódování:
- Negace výroků → multiple_choice (3 možnosti, distraktory záměnou kvantifikátorů /
  negací nesprávné části implikace).
- Definiční obory s prostým intervalem nebo sjednocením intervalů → mathlive s
  popiskem `D = ` (student píše intervaly pomocí MathLive).
- Definiční obory se sjednoceními po k∈ℤ (cyklické) → multiple_choice
  (vstup přes MathLive by byl moc obtížný a Compute Engine ho nezvládne porovnat).
- Kvadratické extrémy → dva výsledky: bod (decimal/mathlive) + hodnota (mathlive).
- Aplikační (zisk z výroby, hotel) → více pojmenovaných výsledků.
"""

TASKS = [
    # --------------------- 3 negace výroků ---------------------
    {
        "task_id": "cv01_01",
        "content_latex": (
            r"Formulujte negaci filmového titulu: "
            r"\textit{Jestliže se rozzlobíme, budeme zlí.}"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Rozzlobíme se a nebudeme zlí."},
                {"key": "b", "label_latex": r"Nerozzlobíme se a budeme zlí."},
                {"key": "c", "label_latex": r"Jestliže nebudeme zlí, nerozzlobíme se."},
            ],
            "expected": "a",
        }],
        "cognitive_load": "A", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv01_02",
        "content_latex": (
            r"Formulujte negaci výroku: "
            r"\textit{Je-li } $\mathbf{B}$ \textit{ množina všech sudých prvočísel větších než } $2,$ "
            r"\textit{ pak } $\mathbf{B} = \emptyset.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$\mathbf{B}$ je množina všech sudých prvočísel větších než $2$ a $\mathbf{B} \ne \emptyset.$"},
                {"key": "b", "label_latex": r"Je-li $\mathbf{B}$ množina všech sudých prvočísel větších než $2,$ pak $\mathbf{B} \ne \emptyset.$"},
                {"key": "c", "label_latex": r"$\mathbf{B}$ není množina všech sudých prvočísel větších než $2$ a $\mathbf{B} = \emptyset.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "B", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv01_03",
        "content_latex": (
            r"Formulujte negaci výroku o reflexivnosti uspořádání reálných čísel: "
            r"\textit{Pro každé } $x \in \mathbb{R}$ \textit{ platí } $x \le x.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $x \in \mathbb{R}$ takové, že $x > x.$"},
                {"key": "b", "label_latex": r"Pro každé $x \in \mathbb{R}$ platí $x > x.$"},
                {"key": "c", "label_latex": r"Existuje $x \in \mathbb{R}$ takové, že $x \ge x.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "B", "graph_vector": ["Negace výroků"],
    },

    # --------------------- 25 definičních oborů ---------------------
    {
        "task_id": "cv01_04",
        "content_latex": r"Určete definiční obor funkce $y = \sqrt{x-1} + \sqrt{6-x}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"[1, 6]"}],
        "cognitive_load": "B", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_05",
        "content_latex": r"Určete definiční obor funkce $y = \sqrt{x^2 - 5x + 6}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(-\infty, 2] \cup [3, \infty)"}],
        "cognitive_load": "C", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_06",
        "content_latex": r"Určete definiční obor funkce $y = \dfrac{1}{\sqrt{6 + 7x - 3x^2}}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"\left(-\frac{2}{3}, 3\right)"}],
        "cognitive_load": "C", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_07",
        "content_latex": r"Určete definiční obor funkce $y = \log\left(5 - x - \dfrac{6}{x}\right)$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(-\infty, 0) \cup (2, 3)"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_08",
        "content_latex": r"Určete definiční obor funkce $y = \ln\left(\dfrac{x^2 - 7x + 12}{x^2 - 2x - 3}\right)$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(-\infty, -1) \cup (4, \infty)"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        # Cyklický def. obor — multiple choice (mathlive sjednocení po k∈ℤ je moc).
        "task_id": "cv01_09",
        "content_latex": r"Určete definiční obor funkce $y = \sqrt{(\sin x + \cos x)^2 - 1}$.",
        "results": [{
            "key": "D", "label_latex": r"D(f) = ", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left[k\pi,\ \tfrac{(2k+1)\pi}{2}\right]$"},
                {"key": "b", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left[\tfrac{(2k+1)\pi}{2},\ (k+1)\pi\right]$"},
                {"key": "c", "label_latex": r"$\mathbb{R}$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "E", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_10",
        "content_latex": r"Určete definiční obor funkce $y = \sqrt{\cos x - \dfrac{1}{2}}$.",
        "results": [{
            "key": "D", "label_latex": r"D(f) = ", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left[-\tfrac{\pi}{3} + 2k\pi,\ \tfrac{\pi}{3} + 2k\pi\right]$"},
                {"key": "b", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left(-\tfrac{\pi}{3} + 2k\pi,\ \tfrac{\pi}{3} + 2k\pi\right)$"},
                {"key": "c", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left[\tfrac{\pi}{3} + 2k\pi,\ \tfrac{5\pi}{3} + 2k\pi\right]$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_11",
        "content_latex": r"Určete definiční obor funkce $y = \dfrac{1}{\log(9-x)}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(-\infty, 8) \cup (8, 9)"}],
        "cognitive_load": "C", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_12",
        "content_latex": r"Určete definiční obor funkce $y = \dfrac{1}{3 - \log_3(x-3)}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(3, 30) \cup (30, \infty)"}],
        "cognitive_load": "C", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_13",
        "content_latex": r"Určete definiční obor funkce $y = \dfrac{\log_2(x^2+1)}{\sin^2 x - \sin x + \tfrac{1}{4}}$.",
        "results": [{
            "key": "D", "label_latex": r"D(f) = ", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$\mathbb{R} \setminus \bigcup_{k \in \mathbb{Z}} \left\{\tfrac{\pi}{6} + 2k\pi,\ \tfrac{5\pi}{6} + 2k\pi\right\}$"},
                {"key": "b", "label_latex": r"$\mathbb{R} \setminus \{0\}$"},
                {"key": "c", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left(\tfrac{\pi}{6} + 2k\pi,\ \tfrac{5\pi}{6} + 2k\pi\right)$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "E", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_14",
        "content_latex": r"Určete definiční obor funkce $y = \sqrt{\log(x+1)}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"[0, \infty)"}],
        "cognitive_load": "B", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_15",
        "content_latex": r"Určete definiční obor funkce $y = \sqrt{\log\dfrac{1 - 2x}{x + 3}}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"\left(-3, -\frac{2}{3}\right]"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_16",
        "content_latex": r"Určete definiční obor funkce $y = \log\dfrac{1 - 5^x}{7^{-x} - 7}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(-\infty, -1) \cup (0, \infty)"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_17",
        "content_latex": r"Určete definiční obor funkce $y = \sqrt{\log_{1/2}(x^2 - 5x + 7)}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"[2, 3]"}],
        "cognitive_load": "C", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_18",
        "content_latex": r"Určete definiční obor funkce $y = \sqrt{\,4^{\frac{3x^2 + 18x + 29}{x+3}} - 2^{6x + 17}\,}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(-\infty, -7] \cup (-3, \infty)"}],
        "cognitive_load": "E", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_19",
        "content_latex": r"Určete definiční obor funkce $y = \log(\log_{1/2}(3x - 8) - \log_{1/2}(x^2 + 4))$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"\left(\frac{8}{3}, \infty\right)"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_20",
        "content_latex": r"Určete definiční obor funkce $y = \log(\log^2 x - 5\log x + 6)$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(0, 100) \cup (1000, \infty)"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_21",
        "content_latex": r"Určete definiční obor funkce $y = \left(2 \sin\tfrac{x}{2}\right)^{1/2}$.",
        "results": [{
            "key": "D", "label_latex": r"D(f) = ", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left[4k\pi,\ (4k+2)\pi\right]$"},
                {"key": "b", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left[2k\pi,\ (2k+1)\pi\right]$"},
                {"key": "c", "label_latex": r"$\mathbb{R}$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_22",
        "content_latex": r"Určete definiční obor funkce $y = \log(|x-1| + 2x - 4)$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"\left(\frac{5}{3}, \infty\right)"}],
        "cognitive_load": "C", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_23",
        "content_latex": r"Určete definiční obor funkce $y = \dfrac{1}{\sqrt{\,5^{2+x} - x^2 \cdot 5^x\,}}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(-5, 5)"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_24",
        "content_latex": r"Určete definiční obor funkce $y = \log(\log_{1/3}(5x - 1))$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"\left(\frac{1}{5}, \frac{2}{5}\right)"}],
        "cognitive_load": "C", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_25",
        "content_latex": r"Určete definiční obor funkce $y = (6 - 2|x-1| - x^2)^{-1/2}$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"(1 - \sqrt{5}, 2)"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_26",
        "content_latex": r"Určete definiční obor funkce $y = \log_2\left(2 - \dfrac{4^x + 2x - 4}{x - 1}\right)$.",
        "results": [{"key": "D", "label_latex": r"D(f) = ", "type": "mathlive",
                     "expected": r"\left(\frac{1}{2}, 1\right)"}],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_27",
        "content_latex": r"Určete definiční obor funkce $y = \left(-\sin x \left(\cos x + \tfrac{1}{2}\right)\right)^{-1/2}$.",
        "results": [{
            "key": "D", "label_latex": r"D(f) = ", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left[\left(\tfrac{2\pi}{3} + 2k\pi,\ \pi + 2k\pi\right) \cup \left(\tfrac{4\pi}{3} + 2k\pi,\ 2\pi + 2k\pi\right)\right]$"},
                {"key": "b", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left(2k\pi,\ (2k+1)\pi\right)$"},
                {"key": "c", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left(\pi + 2k\pi,\ 2\pi + 2k\pi\right)$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "F", "graph_vector": ["Definiční obor"],
    },
    {
        "task_id": "cv01_28",
        "content_latex": r"Určete definiční obor funkce $y = \ln(2\cos^2 x + 5\cos x + 2)$.",
        "results": [{
            "key": "D", "label_latex": r"D(f) = ", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left(-\tfrac{2\pi}{3} + 2k\pi,\ \tfrac{2\pi}{3} + 2k\pi\right)$"},
                {"key": "b", "label_latex": r"$\bigcup_{k \in \mathbb{Z}} \left(\tfrac{2\pi}{3} + 2k\pi,\ \tfrac{4\pi}{3} + 2k\pi\right)$"},
                {"key": "c", "label_latex": r"$\mathbb{R}$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "D", "graph_vector": ["Definiční obor"],
    },

    # --------------------- 4 největší hodnoty kvadratické funkce ---------------------
    {
        "task_id": "cv01_29",
        "content_latex": r"Určete největší hodnotu funkce $y = -2x^2 + x - 1$ a bod, ve kterém ji nabývá.",
        "results": [
            {"key": "x", "label_latex": r"x = ", "type": "mathlive", "expected": r"\frac{1}{4}"},
            {"key": "y", "label_latex": r"y_{\max} = ", "type": "mathlive", "expected": r"-\frac{7}{8}"},
        ],
        "cognitive_load": "B", "graph_vector": ["Kvadratická funkce"],
    },
    {
        "task_id": "cv01_30",
        "content_latex": r"Určete největší hodnotu funkce $y = -x^2 - 3x + 2$ a bod, ve kterém ji nabývá.",
        "results": [
            {"key": "x", "label_latex": r"x = ", "type": "mathlive", "expected": r"-\frac{3}{2}"},
            {"key": "y", "label_latex": r"y_{\max} = ", "type": "mathlive", "expected": r"\frac{17}{4}"},
        ],
        "cognitive_load": "B", "graph_vector": ["Kvadratická funkce"],
    },
    {
        "task_id": "cv01_31",
        "content_latex": r"Určete největší hodnotu funkce $y = -2x^2 + ax - a^2,$ kde $a > 0,$ a bod, ve kterém ji nabývá.",
        "results": [{
            "key": "extremum", "label_latex": r"\text{Výsledek: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$x = \tfrac{a}{4},\ y_{\max} = -\tfrac{7a^2}{8}$"},
                {"key": "b", "label_latex": r"$x = \tfrac{a}{2},\ y_{\max} = -\tfrac{3a^2}{4}$"},
                {"key": "c", "label_latex": r"$x = a,\ y_{\max} = -2a^2$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Kvadratická funkce"],
    },
    {
        "task_id": "cv01_32",
        "content_latex": r"Určete největší hodnotu funkce $y = b^2 x - b^2 x^2,$ kde $b \ne 0,$ a bod, ve kterém ji nabývá.",
        "results": [{
            "key": "extremum", "label_latex": r"\text{Výsledek: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$x = \tfrac{1}{2},\ y_{\max} = \tfrac{b^2}{4}$"},
                {"key": "b", "label_latex": r"$x = 1,\ y_{\max} = 0$"},
                {"key": "c", "label_latex": r"$x = \tfrac{1}{2},\ y_{\max} = b^2$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Kvadratická funkce"],
    },

    # --------------------- 3 nejmenší hodnoty kvadratické funkce ---------------------
    {
        "task_id": "cv01_33",
        "content_latex": r"Určete nejmenší hodnotu funkce $y = x^2 + 4x - 2$ a bod, ve kterém ji nabývá.",
        "results": [
            {"key": "x", "label_latex": r"x = ", "type": "decimal", "expected": -2, "tolerance": 0.001},
            {"key": "y", "label_latex": r"y_{\min} = ", "type": "decimal", "expected": -6, "tolerance": 0.001},
        ],
        "cognitive_load": "B", "graph_vector": ["Kvadratická funkce"],
    },
    {
        "task_id": "cv01_34",
        "content_latex": r"Určete nejmenší hodnotu funkce $y = 1 - 3x + 6x^2$ a bod, ve kterém ji nabývá.",
        "results": [
            {"key": "x", "label_latex": r"x = ", "type": "mathlive", "expected": r"\frac{1}{4}"},
            {"key": "y", "label_latex": r"y_{\min} = ", "type": "mathlive", "expected": r"\frac{5}{8}"},
        ],
        "cognitive_load": "B", "graph_vector": ["Kvadratická funkce"],
    },
    {
        "task_id": "cv01_35",
        "content_latex": r"Určete nejmenší hodnotu funkce $y = a^2 x^2 + a^4,$ kde $a \ne 0,$ a bod, ve kterém ji nabývá.",
        "results": [{
            "key": "extremum", "label_latex": r"\text{Výsledek: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$x = 0,\ y_{\min} = a^4$"},
                {"key": "b", "label_latex": r"$x = a^2,\ y_{\min} = 2 a^4$"},
                {"key": "c", "label_latex": r"$x = -a,\ y_{\min} = 2 a^4$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Kvadratická funkce"],
    },

    # --------------------- 2 aplikační úlohy ---------------------
    {
        "task_id": "cv01_36",
        "content_latex": (
            r"\textbf{Zisk z výroby.} "
            r"Výrobce je schopen vyrábět lampy s celkovými náklady 120 korun na jeden kus. "
            r"Lampy se prodávají za cenu 150 korun za kus; při této ceně spotřebitelé nakoupí 500 lamp za měsíc. "
            r"Výrobce chce zvýšit cenu; odhaduje, že za každých 10 korun zvýšení ceny nad 150 korun budou spotřebitelé "
            r"kupovat měsíčně o 20 lamp méně. Určete: a) zisk výrobce za měsíc jako funkci ceny $c$; "
            r"b) cenu, při které je zisk maximální; c) maximální měsíční zisk."
        ),
        "results": [
            {"key": "P", "label_latex": r"P(c) = ", "type": "mathlive",
             "expected": r"(c - 120)(800 - 2c)"},
            {"key": "c_opt", "label_latex": r"c_{\text{opt}} = ", "type": "decimal",
             "expected": 260, "tolerance": 0.5},
            {"key": "P_max", "label_latex": r"P_{\max} = ", "type": "decimal",
             "expected": 39200, "tolerance": 1},
        ],
        "cognitive_load": "D", "graph_vector": ["Kvadratická funkce", "Aplikace"],
    },
    {
        "task_id": "cv01_37",
        "content_latex": (
            r"\textbf{Hotel Blue Star.} "
            r"Hotel \textit{Blue Star} v Las Vegas, který má přesně 300 pokojů, se plně obsadí každý den při ceně 80 dolarů za pokoj. "
            r"Jestliže se cena za pokoj zvedne, pak se za každý dolar přidaný k původní ceně obsadí vždy o 3 pokoje méně. "
            r"Jestliže každý obsazený pokoj znamená pro hotel výdaje 10 dolarů na úklid a služby, "
            r"jak má management stanovit cenu, aby byl zisk maximální? "
            r"Určete: a) zisk jako funkci ceny $c$; b) optimální cenu; c) maximální zisk; d) počet neobsazených pokojů."
        ),
        "results": [
            {"key": "P", "label_latex": r"P(c) = ", "type": "mathlive",
             "expected": r"3 (c - 10)(180 - c)"},
            {"key": "c_opt", "label_latex": r"c_{\text{opt}} = ", "type": "decimal",
             "expected": 95, "tolerance": 0.5},
            {"key": "P_max", "label_latex": r"P_{\max} = ", "type": "decimal",
             "expected": 21675, "tolerance": 1},
            {"key": "volne", "label_latex": r"\text{Neobsazených pokojů} = ", "type": "decimal",
             "expected": 45, "tolerance": 0.5},
        ],
        "cognitive_load": "E", "graph_vector": ["Kvadratická funkce", "Aplikace"],
    },
]
