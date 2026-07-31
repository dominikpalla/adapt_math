"""
Cvičení 5 — Limita funkce: věta o limitě složené funkce, typové limity.
"""


def _lim(idx, content, expected, cl="C"):
    """Jednoduchá limita s mathlive výsledkem."""
    return {
        "task_id": f"cv05_{idx:02d}",
        "content_latex": content,
        "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": expected}],
        "cognitive_load": cl, "graph_vector": ["Limity funkcí"],
    }


def _lim_dec(idx, content, value, tol=0.001, cl="B"):
    """Limita s číselnou hodnotou (decimal)."""
    return {
        "task_id": f"cv05_{idx:02d}",
        "content_latex": content,
        "results": [{"key": "lim", "label_latex": "", "type": "decimal", "expected": value, "tolerance": tol}],
        "cognitive_load": cl, "graph_vector": ["Limity funkcí"],
    }


TASKS = [
    # --------------------- 3 negace ---------------------
    {
        "task_id": "cv05_01",
        "content_latex": (
            r"Formulujte negaci výroku: \textit{Je-li } $x = $ Karel IV. \textit{ a } "
            r"$\mathbf{C}$ \textit{ množina všech současných politiků, pak } $x \notin \mathbf{C}.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$x = $ Karel IV. a $\mathbf{C}$ je množina všech současných politiků a $x \in \mathbf{C}.$"},
                {"key": "b", "label_latex": r"Je-li $x = $ Karel IV. a $\mathbf{C}$ je množina všech současných politiků, pak $x \in \mathbf{C}.$"},
                {"key": "c", "label_latex": r"$x \ne $ Karel IV. nebo $\mathbf{C}$ není množina všech současných politiků nebo $x \in \mathbf{C}.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "B", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv05_02",
        "content_latex": (
            r"Formulujte negaci výroku o slučitelnosti sčítání s uspořádáním: "
            r"\textit{Pro libovolnou trojici } $x, y, z \in \mathbb{R}$ \textit{ platí: "
            r"je-li } $x \le y,$ \textit{ pak } $x + z \le y + z.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje trojice $x, y, z \in \mathbb{R}$ taková, že $x \le y$ a zároveň $x + z > y + z.$"},
                {"key": "b", "label_latex": r"Pro libovolnou trojici $x, y, z \in \mathbb{R}$ platí: je-li $x \le y,$ pak $x + z > y + z.$"},
                {"key": "c", "label_latex": r"Existuje trojice $x, y, z \in \mathbb{R}$ taková, že $x > y$ a zároveň $x + z \le y + z.$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků"],
    },
    {
        "task_id": "cv05_03",
        "content_latex": (
            r"Formulujte negaci existenčního výroku: \textit{Pro každou } $f: \mathbb{R} \to \mathbb{R}$ "
            r"\textit{ a každý bod } $a \in \mathbb{R}^*$ \textit{ existuje nejvýše jedna limita } "
            r"$f$ \textit{ v bodě } $a.$"
        ),
        "results": [{
            "key": "negace", "label_latex": r"\text{Negace: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"Existuje $f: \mathbb{R} \to \mathbb{R}$ a $a \in \mathbb{R}^*$ taková, že $f$ má v $a$ aspoň dvě různé limity."},
                {"key": "b", "label_latex": r"Pro každou $f$ a každý $a$ existují aspoň dvě limity $f$ v $a.$"},
                {"key": "c", "label_latex": r"Existuje $f$ a $a$ takové, že $f$ nemá v $a$ žádnou limitu."},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C", "graph_vector": ["Negace výroků", "Limity funkcí"],
    },

    # --------------------- 7 limit (sin/cos kolem π/4, π/2, π) ---------------------
    _lim(4,  r"\lim_{x \to \frac{\pi}{4}} \frac{\sin x - \cos x}{1 - \tan x}", r"-\frac{\sqrt{2}}{2}", "C"),
    _lim(5,  r"\lim_{x \to \frac{\pi}{4}} \frac{\sin x - \cos x}{\cos 2x}",    r"-\frac{\sqrt{2}}{2}", "C"),
    _lim_dec(6,  r"\lim_{x \to \frac{\pi}{2}} \frac{\sin 2x \cdot \cos x}{1 + \cos 2x}", 1, 0.001, "C"),
    _lim_dec(7,  r"\lim_{x \to 0} \frac{\sin^2 2x}{1 - \cos 2x}", 2, 0.001, "B"),
    _lim_dec(8,  r"\lim_{x \to \pi} \frac{\sin^2 x}{1 + \cos x}", 2, 0.001, "B"),
    _lim_dec(9,  r"\lim_{x \to 0} \frac{1 - \cos x}{\sin x}",      0, 0.001, "B"),
    _lim_dec(10, r"\lim_{x \to \frac{\pi}{4}} \frac{\tan x - 1}{\cot x - 1}", -1, 0.001, "C"),

    # --------------------- 8 limit s odmocninami v jmenovateli ---------------------
    _lim_dec(11, r"\lim_{x \to 0} \frac{\tan^2 x}{1 - \sqrt{\cos 2x}}", 1, 0.001, "D"),
    _lim(12, r"\lim_{x \to 0} \frac{\sin^2 x}{\sqrt{3} - \sqrt{2 + \cos x}}", r"4\sqrt{3}", "D"),
    _lim_dec(13, r"\lim_{x \to 0} \frac{\tan x}{\sqrt{1 - \sin x} - \sqrt{1 + \sin x}}", -1, 0.001, "D"),
    _lim(14, r"\lim_{x \to \frac{\pi}{4}} \frac{\cos 2x}{\sqrt{\sin x} - \sqrt{\cos x}}", r"-2\sqrt[4]{2}", "E"),
    _lim(15, r"\lim_{x \to \pi} \frac{1 - \sqrt{\cos x + 2}}{\sin^2 2x}", r"-\frac{1}{16}", "E"),
    _lim_dec(16, r"\lim_{x \to \frac{\pi}{6}} \frac{2 \sin^2 x - \cos 2x}{\sqrt{2 \sin x} - 1}", 4, 0.001, "E"),
    {
        "task_id": "cv05_17",
        "content_latex": r"\lim_{x \to 0} \frac{1}{\cos x - 1}",
        "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"-\infty"}],
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
    },
    {
        "task_id": "cv05_18",
        "content_latex": r"\lim_{x \to \frac{\pi}{2}} \frac{x}{1 - \sin x}",
        "results": [{"key": "lim", "label_latex": "", "type": "mathlive", "expected": r"\infty"}],
        "cognitive_load": "C", "graph_vector": ["Limity funkcí"],
    },

    # --------------------- 13 typových limit (sin/x, 1-cos x/x², …) ---------------------
    _lim_dec(19, r"\lim_{x \to 0} \frac{\sin 2x}{x}",        2, 0.001, "B"),
    _lim(20, r"\lim_{x \to 0} \frac{\sin^2 x}{4x^2}",        r"\frac{1}{4}", "B"),
    _lim_dec(21, r"\lim_{x \to 0} \frac{\sin x + \sin 3x}{x}", 4, 0.001, "C"),
    _lim_dec(22, r"\lim_{x \to 0} \frac{4x + \sin 8x}{4x}",   3, 0.001, "C"),
    _lim(23, r"\lim_{x \to 0} \frac{\sin^2 x + x}{10x}",     r"\frac{1}{10}", "C"),
    _lim_dec(24, r"\lim_{x \to 0} \frac{\cos^2 x - 1 + \sin 2x}{x}", 2, 0.001, "D"),
    _lim_dec(25, r"\lim_{x \to 0} \frac{1 - \cos 2x}{x \sin x}",     2, 0.001, "C"),
    _lim_dec(26, r"\lim_{x \to 0} \frac{\tan x - \sin 2x}{x}", -1, 0.001, "C"),
    _lim(27, r"\lim_{x \to 0} \frac{1 - \cos x}{x^2}",       r"\frac{1}{2}", "C"),
    _lim_dec(28, r"\lim_{x \to 0} \frac{\sin 4x}{\sqrt{x+1} - 1}", 8, 0.001, "D"),
    _lim_dec(29, r"\lim_{x \to 0} \frac{1 - \sqrt{\cos 2x}}{x^2}", 1, 0.001, "D"),
    _lim_dec(30, r"\lim_{x \to 0^+} \frac{1 - \sqrt{\cos x}}{1 - \cos\sqrt{x}}", 0, 0.001, "D"),
    _lim(31, r"\lim_{x \to 0} \frac{1 - \cos^3 x}{x \sin 2x}", r"\frac{3}{4}", "D"),

    # --------------------- 13 e-typových limit ---------------------
    _lim(32, r"\lim_{x \to \infty}\left(1 + \frac{1}{x}\right)^x", r"e", "B"),
    _lim(33, r"\lim_{x \to \infty}\left(\frac{x+1}{x-1}\right)^x", r"e^2", "C"),
    _lim(34, r"\lim_{x \to 0}\left(1 + 2x^2\right)^{\frac{1}{2x^2}}", r"e", "C"),
    _lim(35, r"\lim_{x \to \infty}\left(\frac{2x}{2x-3}\right)^{3x}", r"e^{9/2}", "D"),
    _lim(36, r"\lim_{x \to \infty}\left(\frac{2x+3}{2x+1}\right)^{x+1}", r"e", "D"),
    _lim(37, r"\lim_{x \to \infty}\left(\frac{x^2+2}{x^2+1}\right)^{x^2}", r"e", "C"),
    _lim_dec(38, r"\lim_{x \to \infty} \frac{\ln(1 + e^x)}{x}", 1, 0.001, "C"),
    _lim_dec(39, r"\lim_{x \to \infty}\left(\cos\frac{1}{x}\right)^x", 1, 0.001, "D"),
    _lim(40, r"\lim_{x \to 0} \frac{\ln \cos x}{x^2}", r"-\frac{1}{2}", "C"),
    _lim(41, r"\lim_{x \to 1} \frac{e^x - e}{x - 1}", r"e", "C"),
    _lim_dec(42, r"\lim_{x \to 0} \frac{1 - e^{-x}}{\sin x}", 1, 0.001, "B"),
    _lim(43, r"\lim_{x \to 0} (\cos x)^{\frac{1}{x^2}}", r"\frac{1}{\sqrt{e}}", "D"),
    _lim_dec(44, r"\lim_{x \to 0} \frac{\ln(1 + 5\sin x)}{\sin x}", 5, 0.001, "C"),
]
