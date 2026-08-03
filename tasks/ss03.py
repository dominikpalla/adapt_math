"""
SŠ 03 — Množiny (doplněk, sjednocení, průnik, podmnožiny, zobrazení).

Zdroj: Overleaf `Andrea_příkladySŠ/Množiny.tex`.
Extrahováno 2026-08-03.
"""

TASKS = [
    # 1a) doplněk A = {x ∈ Z; |x| >= 3} v B = Z
    {
        "task_id": "ss03_01",
        "content_latex": (
            r"Určete doplněk množiny $A$ v množině $B$: "
            r"$A = \{x \in \mathbb{Z};\ |x| \ge 3\},\quad B = \mathbb{Z}$."
        ),
        "results": [{
            "key": "doplnek", "label_latex": r"A' = ", "type": "mathlive",
            "expected": r"\{-2, -1, 0, 1, 2\}", "tolerance": 0.0,
        }],
        "cognitive_load": "B",
    },
    # 1b) doplněk A = {3,4,5,6} v B = {x ∈ N; x ≤ 10}
    {
        "task_id": "ss03_02",
        "content_latex": (
            r"Určete doplněk množiny $A$ v množině $B$: "
            r"$A = \{3, 4, 5, 6\},\quad B = \{x \in \mathbb{N};\ x \le 10\}$."
        ),
        "results": [{
            "key": "doplnek", "label_latex": r"A' = ", "type": "mathlive",
            "expected": r"\{1, 2, 7, 8, 9, 10\}", "tolerance": 0.0,
        }],
        "cognitive_load": "B",
    },
    # 2a) A ∪ B, A ∩ B pro A = celá čísla nezáporná, B = celá čísla nekladná
    {
        "task_id": "ss03_03",
        "content_latex": (
            r"Určete sjednocení a průnik množin $A$, $B$: "
            r"$A = \{x \in \mathbb{Z};\ x \ge 0\},\quad B = \{x \in \mathbb{Z};\ x \le 0\}$."
        ),
        "results": [
            {"key": "sjednoceni", "label_latex": r"A \cup B = ", "type": "mathlive",
             "expected": r"\mathbb{Z}", "tolerance": 0.0},
            {"key": "prunik", "label_latex": r"A \cap B = ", "type": "mathlive",
             "expected": r"\{0\}", "tolerance": 0.0},
        ],
        "cognitive_load": "B",
    },
    # 2b) A ∪ B, A ∩ B pro A = x<-3, B = |x|>1
    {
        "task_id": "ss03_04",
        "content_latex": (
            r"Určete sjednocení a průnik množin $A$, $B$: "
            r"$A = \{x \in \mathbb{R};\ x < -3\},\quad B = \{x \in \mathbb{R};\ |x| > 1\}$."
        ),
        "results": [
            {"key": "sjednoceni", "label_latex": r"A \cup B = ", "type": "mathlive",
             "expected": r"(-\infty, -3) \cup (1, \infty)", "tolerance": 0.0},
            {"key": "prunik", "label_latex": r"A \cap B = ", "type": "mathlive",
             "expected": r"(-\infty, -3)", "tolerance": 0.0},
        ],
        "cognitive_load": "C",
    },
    # 3) všechny podmnožiny A = {x ∈ Z; x^2 < 2} — odpověď je seznam množin,
    # student by musel psát množinu množin. Přepsáno jako MC (počet podmnožin).
    {
        "task_id": "ss03_05",
        "content_latex": (
            r"Kolik má množina $A = \{x \in \mathbb{Z};\ x^2 < 2\}$ různých podmnožin "
            r"(včetně prázdné a $A$ samotné)?"
        ),
        "results": [{
            "key": "pocet", "label_latex": r"\text{Počet podmnožin: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$4$"},
                {"key": "b", "label_latex": r"$6$"},
                {"key": "c", "label_latex": r"$8$"},
                {"key": "d", "label_latex": r"$16$"},
            ],
            "expected": "c",  # A = {-1, 0, 1}, 2^3 = 8
        }],
        "cognitive_load": "C",
    },
    # 4a) A={1,2,3}, B={a,b,c}, {(1,a),(2,a),(3,c)} — zobrazení A→B?
    {
        "task_id": "ss03_06",
        "content_latex": (
            r"Jsou dány množiny $A = \{1, 2, 3\}$, $B = \{a, b, c\}$. "
            r"Rozhodněte o relaci $\{(1, a),\ (2, a),\ (3, c)\}$."
        ),
        "results": [{
            "key": "typ", "label_latex": r"\text{Charakter: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"zobrazení $A$ do $B$, není na $B$"},
                {"key": "b", "label_latex": r"zobrazení $A$ do $B$ i na $B$"},
                {"key": "c", "label_latex": r"není zobrazení"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C",
    },
    # 4b) {(1,a),(1,b),(3,a)} — 1 se zobrazuje dvakrát → není zobrazení
    {
        "task_id": "ss03_07",
        "content_latex": (
            r"Jsou dány množiny $A = \{1, 2, 3\}$, $B = \{a, b, c\}$. "
            r"Rozhodněte o relaci $\{(1, a),\ (1, b),\ (3, a)\}$."
        ),
        "results": [{
            "key": "typ", "label_latex": r"\text{Charakter: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"zobrazení $A$ do $B$, není na $B$"},
                {"key": "b", "label_latex": r"zobrazení $A$ do $B$ i na $B$"},
                {"key": "c", "label_latex": r"není zobrazení"},
            ],
            "expected": "c",
        }],
        "cognitive_load": "C",
    },
    # 4c) {(1,b),(2,b),(3,b)} — konstantní zobrazení do B, ne na B
    {
        "task_id": "ss03_08",
        "content_latex": (
            r"Jsou dány množiny $A = \{1, 2, 3\}$, $B = \{a, b, c\}$. "
            r"Rozhodněte o relaci $\{(1, b),\ (2, b),\ (3, b)\}$."
        ),
        "results": [{
            "key": "typ", "label_latex": r"\text{Charakter: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"zobrazení $A$ do $B$, není na $B$"},
                {"key": "b", "label_latex": r"zobrazení $A$ do $B$ i na $B$"},
                {"key": "c", "label_latex": r"není zobrazení"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C",
    },
    # 4d) {(1,b),(2,a),(3,c)} — bijekce
    {
        "task_id": "ss03_09",
        "content_latex": (
            r"Jsou dány množiny $A = \{1, 2, 3\}$, $B = \{a, b, c\}$. "
            r"Rozhodněte o relaci $\{(1, b),\ (2, a),\ (3, c)\}$."
        ),
        "results": [{
            "key": "typ", "label_latex": r"\text{Charakter: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"zobrazení $A$ do $B$, není na $B$"},
                {"key": "b", "label_latex": r"zobrazení $A$ do $B$ i na $B$"},
                {"key": "c", "label_latex": r"není zobrazení"},
            ],
            "expected": "b",
        }],
        "cognitive_load": "C",
    },
]
