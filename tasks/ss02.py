"""
SŠ 02 — Goniometrie a trigonometrie.

Zdroj: Overleaf `Andrea_příkladySŠ/Goniometrie a trigoniometrie.tex`.
Extrahováno 2026-08-03.

Poznámka: úloha 10 (důkazy identit) vynechána — vyžadovala by open_text.
"""


TASKS = [
    # --- 1. sin/cos/tg/cotg pro speciální úhly ------------------------------
    {
        "task_id": "ss02_01",
        "content_latex": r"Vypočítejte $\sin\alpha$, $\cos\alpha$, $\tan\alpha$, $\cot\alpha$ pro $\alpha = 30^\circ$.",
        "results": [
            {"key": "sin",  "label_latex": r"\sin\alpha = ",  "type": "mathlive", "expected": r"\frac{1}{2}",       "tolerance": 0.0},
            {"key": "cos",  "label_latex": r"\cos\alpha = ",  "type": "mathlive", "expected": r"\frac{\sqrt{3}}{2}", "tolerance": 0.0},
            {"key": "tan",  "label_latex": r"\tan\alpha = ",  "type": "mathlive", "expected": r"\frac{\sqrt{3}}{3}", "tolerance": 0.0},
            {"key": "cot",  "label_latex": r"\cot\alpha = ",  "type": "mathlive", "expected": r"\sqrt{3}",           "tolerance": 0.0},
        ],
        "cognitive_load": "B",
    },
    {
        "task_id": "ss02_02",
        "content_latex": r"Vypočítejte $\sin\alpha$, $\cos\alpha$, $\tan\alpha$, $\cot\alpha$ pro $\alpha = 45^\circ$.",
        "results": [
            {"key": "sin",  "label_latex": r"\sin\alpha = ",  "type": "mathlive", "expected": r"\frac{\sqrt{2}}{2}", "tolerance": 0.0},
            {"key": "cos",  "label_latex": r"\cos\alpha = ",  "type": "mathlive", "expected": r"\frac{\sqrt{2}}{2}", "tolerance": 0.0},
            {"key": "tan",  "label_latex": r"\tan\alpha = ",  "type": "mathlive", "expected": r"1",                  "tolerance": 0.0},
            {"key": "cot",  "label_latex": r"\cot\alpha = ",  "type": "mathlive", "expected": r"1",                  "tolerance": 0.0},
        ],
        "cognitive_load": "B",
    },
    {
        "task_id": "ss02_03",
        "content_latex": r"Vypočítejte $\sin\alpha$, $\cos\alpha$, $\tan\alpha$, $\cot\alpha$ pro $\alpha = 60^\circ$.",
        "results": [
            {"key": "sin",  "label_latex": r"\sin\alpha = ",  "type": "mathlive", "expected": r"\frac{\sqrt{3}}{2}", "tolerance": 0.0},
            {"key": "cos",  "label_latex": r"\cos\alpha = ",  "type": "mathlive", "expected": r"\frac{1}{2}",        "tolerance": 0.0},
            {"key": "tan",  "label_latex": r"\tan\alpha = ",  "type": "mathlive", "expected": r"\sqrt{3}",           "tolerance": 0.0},
            {"key": "cot",  "label_latex": r"\cot\alpha = ",  "type": "mathlive", "expected": r"\frac{\sqrt{3}}{3}", "tolerance": 0.0},
        ],
        "cognitive_load": "B",
    },

    # --- 2. Převod stupně → radiány -----------------------------------------
    {"task_id": "ss02_04", "content_latex": r"Vyjádřete v radiánech: $\alpha = 22{,}5^\circ$.",
     "results": [{"key": "alpha", "label_latex": r"\alpha = ", "type": "mathlive", "expected": r"\frac{\pi}{8}", "tolerance": 0.0}],
     "cognitive_load": "B"},
    {"task_id": "ss02_05", "content_latex": r"Vyjádřete v radiánech: $\alpha = 300^\circ$.",
     "results": [{"key": "alpha", "label_latex": r"\alpha = ", "type": "mathlive", "expected": r"\frac{5\pi}{3}", "tolerance": 0.0}],
     "cognitive_load": "B"},
    {"task_id": "ss02_06", "content_latex": r"Vyjádřete v radiánech: $\alpha = 720^\circ$.",
     "results": [{"key": "alpha", "label_latex": r"\alpha = ", "type": "mathlive", "expected": r"4\pi", "tolerance": 0.0}],
     "cognitive_load": "B"},
    {"task_id": "ss02_07", "content_latex": r"Vyjádřete v radiánech: $\alpha = 1^\circ$.",
     "results": [{"key": "alpha", "label_latex": r"\alpha = ", "type": "mathlive", "expected": r"\frac{\pi}{180}", "tolerance": 0.0}],
     "cognitive_load": "B"},

    # --- 3. Převod radiány → stupně -----------------------------------------
    {"task_id": "ss02_08", "content_latex": r"Vyjádřete ve stupních: $\alpha = \dfrac{7\pi}{6}$.",
     "results": [{"key": "alpha", "label_latex": r"\alpha = ", "type": "decimal", "expected": 210, "tolerance": 0}],
     "cognitive_load": "B"},
    # 3b) 1 rad ≈ 57°18' — nutnost decimal (přibližný výsledek); tolerance ±1'
    {"task_id": "ss02_09", "content_latex": r"Vyjádřete ve stupních: $\alpha = 1\ \text{rad}$ (zaokrouhleno na minuty; zadejte hodnotu ve stupních jako desetinné číslo).",
     "results": [{"key": "alpha", "label_latex": r"\alpha \approx ", "type": "decimal", "expected": 57.3, "tolerance": 0.05}],
     "cognitive_load": "C"},
    {"task_id": "ss02_10", "content_latex": r"Vyjádřete ve stupních: $\alpha = \dfrac{\pi}{18}$.",
     "results": [{"key": "alpha", "label_latex": r"\alpha = ", "type": "decimal", "expected": 10, "tolerance": 0}],
     "cognitive_load": "B"},
    {"task_id": "ss02_11", "content_latex": r"Vyjádřete ve stupních: $\alpha = \dfrac{\pi}{12}$.",
     "results": [{"key": "alpha", "label_latex": r"\alpha = ", "type": "decimal", "expected": 15, "tolerance": 0}],
     "cognitive_load": "B"},

    # --- 4. Uspořádání sin 1, sin 2, sin 3, sin 4 --> multiple_choice --------
    {
        "task_id": "ss02_12",
        "content_latex": r"Uspořádejte podle velikosti čísla $\sin 1$, $\sin 2$, $\sin 3$, $\sin 4$.",
        "results": [{
            "key": "poradi", "label_latex": r"\text{Správné pořadí: }", "type": "multiple_choice",
            "options": [
                {"key": "a", "label_latex": r"$\sin 4 < \sin 3 < \sin 1 < \sin 2$"},
                {"key": "b", "label_latex": r"$\sin 1 < \sin 2 < \sin 3 < \sin 4$"},
                {"key": "c", "label_latex": r"$\sin 4 < \sin 1 < \sin 2 < \sin 3$"},
                {"key": "d", "label_latex": r"$\sin 3 < \sin 4 < \sin 1 < \sin 2$"},
            ],
            "expected": "a",
        }],
        "cognitive_load": "C",
    },

    # --- 5. tg x = -5/2 v (3π/2, 2π) → určit sin x, cos x --------------------
    {
        "task_id": "ss02_13",
        "content_latex": r"Určete hodnoty $\sin x$, $\cos x$, jestliže $\tan x = -\dfrac{5}{2}$ a $x \in \left(\dfrac{3\pi}{2}, 2\pi\right)$.",
        "results": [
            {"key": "sin", "label_latex": r"\sin x = ", "type": "mathlive",
             "expected": r"-\frac{5}{\sqrt{29}}", "tolerance": 0.0},
            {"key": "cos", "label_latex": r"\cos x = ", "type": "mathlive",
             "expected": r"\frac{2}{\sqrt{29}}", "tolerance": 0.0},
        ],
        "cognitive_load": "D",
    },

    # --- 6. cos x = -1/8 v (π, 3π/2) → sin, tg, cotg --------------------------
    {
        "task_id": "ss02_14",
        "content_latex": r"Určete hodnoty $\sin x$, $\tan x$, $\cot x$, jestliže $\cos x = -\dfrac{1}{8}$ a $x \in \left(\pi, \dfrac{3\pi}{2}\right)$.",
        "results": [
            {"key": "sin", "label_latex": r"\sin x = ", "type": "mathlive",
             "expected": r"-\frac{\sqrt{63}}{8}", "tolerance": 0.0},
            {"key": "tan", "label_latex": r"\tan x = ", "type": "mathlive",
             "expected": r"\sqrt{63}", "tolerance": 0.0},
            {"key": "cot", "label_latex": r"\cot x = ", "type": "mathlive",
             "expected": r"\frac{\sqrt{63}}{63}", "tolerance": 0.0},
        ],
        "cognitive_load": "D",
    },

    # --- 7. Zjednodušte -------------------------------------------------------
    {"task_id": "ss02_15",
     "content_latex": r"Zjednodušte výraz $\dfrac{(\sin\alpha + \cos\alpha)^2}{1 + \sin 2\alpha}$.",
     "results": [{"key": "v", "label_latex": r"= ", "type": "mathlive", "expected": r"1", "tolerance": 0.0}],
     "cognitive_load": "C"},
    {"task_id": "ss02_16",
     "content_latex": r"Zjednodušte výraz $\sqrt{\sin^2\alpha(1 + \cot\alpha)^2 + \cos^2\alpha(1 + \tan\alpha)^2}$.",
     "results": [{"key": "v", "label_latex": r"= ", "type": "mathlive",
                  "expected": r"|\sin\alpha + \cos\alpha|", "tolerance": 0.0}],
     "cognitive_load": "D"},
    {"task_id": "ss02_17",
     "content_latex": r"Zjednodušte výraz $\dfrac{1 - \cos 2\alpha + \sin 2\alpha}{1 + \cos 2\alpha + \sin 2\alpha}$.",
     "results": [{"key": "v", "label_latex": r"= ", "type": "mathlive",
                  "expected": r"\tan\alpha", "tolerance": 0.0}],
     "cognitive_load": "D"},
    {"task_id": "ss02_18",
     "content_latex": (r"Zjednodušte výraz "
                       r"$\dfrac{\sin^2\left(\dfrac{3\pi}{2} + \alpha\right)}{\cot^2(\alpha - 2\pi)} "
                       r"+ \dfrac{\sin^2(-\alpha)}{\cot^2\left(\alpha - \dfrac{3\pi}{2}\right)}$."),
     "results": [{"key": "v", "label_latex": r"= ", "type": "mathlive", "expected": r"1", "tolerance": 0.0}],
     "cognitive_load": "D"},

    # --- 8. cos α, když sin(α/2) = 1/2·√(2-√3) --------------------------------
    {
        "task_id": "ss02_19",
        "content_latex": r"Vypočítejte $\cos\alpha$, jestliže $\sin\dfrac{\alpha}{2} = \dfrac{1}{2}\sqrt{2 - \sqrt{3}}$.",
        "results": [{"key": "cos", "label_latex": r"\cos\alpha = ", "type": "mathlive",
                     "expected": r"\frac{\sqrt{3}}{2}", "tolerance": 0.0}],
        "cognitive_load": "D",
    },

    # --- 9. Vypočítej výraz když tg x = -7 -----------------------------------
    {
        "task_id": "ss02_20",
        "content_latex": r"Vypočítejte $\dfrac{3\sin x + \cos x}{\cos x - 3\sin x}$, jestliže $\tan x = -7$.",
        "results": [{"key": "v", "label_latex": r"= ", "type": "mathlive",
                     "expected": r"-\frac{10}{11}", "tolerance": 0.0}],
        "cognitive_load": "C",
    },

    # --- 10 (důkazy identit) — SKIP (open_text zakázán) ----------------------

    # --- 11. Řešení rovnic v R (množina řešení) ------------------------------
    {"task_id": "ss02_21",
     "content_latex": r"Řešte v $\mathbb{R}$ rovnici $\sin^4 x - \cos^4 x = \dfrac{1}{2}$. Zapište obecné řešení pro $k \in \mathbb{Z}$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{3} + k\pi \lor x = \frac{2\pi}{3} + k\pi", "tolerance": 0.0}],
     "cognitive_load": "E"},
    {"task_id": "ss02_22",
     "content_latex": r"Řešte v $\mathbb{R}$ rovnici $\cot^2 x + (\sqrt{3} - 1)\cot x = \sqrt{3}$. Zapište obecné řešení pro $k \in \mathbb{Z}$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"\frac{5\pi}{6} + k\pi \lor x = \frac{\pi}{4} + k\pi", "tolerance": 0.0}],
     "cognitive_load": "E"},
    {"task_id": "ss02_23",
     "content_latex": r"Řešte v $\mathbb{R}$ rovnici $\cos^2 x + \sqrt{3}(\cos x + 1) = \sin^2 x - 2\cos x - 1$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"(2k+1)\pi \lor x = \frac{5\pi}{6} + 2k\pi \lor x = \frac{7\pi}{6} + 2k\pi", "tolerance": 0.0}],
     "cognitive_load": "E"},
    {"task_id": "ss02_24",
     "content_latex": r"Řešte v $\mathbb{R}$ rovnici $\cos x + \sin 2x = 0$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{2} + k\pi \lor x = \frac{7\pi}{6} + 2k\pi \lor x = \frac{11\pi}{6} + 2k\pi", "tolerance": 0.0}],
     "cognitive_load": "E"},

    # --- 12. Rovnice v <0, 2π) — konkrétní hodnoty ----------------------------
    {"task_id": "ss02_25",
     "content_latex": r"Řešte v intervalu $\langle 0, 2\pi)$ rovnici $\sin^6 x + \cos^6 x = \dfrac{1}{4}$.",
     "results": [{"key": "x", "label_latex": r"x \in ", "type": "mathlive",
                  "expected": r"\{\frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}\}", "tolerance": 0.0}],
     "cognitive_load": "E"},

    # --- 13. Další rovnice v R -----------------------------------------------
    {"task_id": "ss02_26",
     "content_latex": r"Řešte v $\mathbb{R}$ rovnici $\sin^2 2x = (\cos x - \sin x)^2$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{12} + k\pi \lor x = \frac{5\pi}{12} + k\pi", "tolerance": 0.0}],
     "cognitive_load": "E"},
    {"task_id": "ss02_27",
     "content_latex": r"Řešte v $\mathbb{R}$ rovnici $\sin^2 x + \sin^2 2x = 1$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"\frac{(2k+1)\pi}{2} \lor x = \frac{\pi}{6} + k\pi \lor x = \frac{11\pi}{6} + k\pi", "tolerance": 0.0}],
     "cognitive_load": "E"},
    {"task_id": "ss02_28",
     "content_latex": r"Řešte v $\mathbb{R}$ rovnici $4\sin^3 x + 4\sin^2 x - 3\sin x = 3$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"\frac{3\pi}{2} + 2k\pi \lor x = \frac{\pi}{3} + k\pi \lor x = \frac{2\pi}{3} + k\pi", "tolerance": 0.0}],
     "cognitive_load": "E"},
    {"task_id": "ss02_29",
     "content_latex": r"Řešte v $\mathbb{R}$ rovnici $\tan x + \dfrac{\cos x}{1 + \sin x} = 2$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{3} + 2k\pi \lor x = \frac{2\pi}{3} + 2k\pi", "tolerance": 0.0}],
     "cognitive_load": "E"},

    # --- 14. Řešení v (-π, 2π] — konkrétní hodnoty ---------------------------
    {"task_id": "ss02_30",
     "content_latex": r"Určete všechna $x \in (-\pi, 2\pi]$, pro která platí $\sin\left(x + \dfrac{\pi}{6}\right) = 1$.",
     "results": [{"key": "x", "label_latex": r"x = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{3}", "tolerance": 0.0}],
     "cognitive_load": "C"},
    {"task_id": "ss02_31",
     "content_latex": r"Určete všechna $x \in (-\pi, 2\pi]$, pro která platí $\cot\left(2x - \dfrac{\pi}{4}\right) = -1$.",
     "results": [{"key": "x", "label_latex": r"x \in ", "type": "mathlive",
                  "expected": r"\{-\frac{\pi}{2}, 0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi\}", "tolerance": 0.0}],
     "cognitive_load": "D"},
    {"task_id": "ss02_32",
     "content_latex": r"Určete všechna $x \in (-\pi, 2\pi]$, pro která platí $\cos\left(x + \dfrac{\pi}{4}\right) = 1$.",
     "results": [{"key": "x", "label_latex": r"x \in ", "type": "mathlive",
                  "expected": r"\{-\frac{\pi}{4}, \frac{7\pi}{4}\}", "tolerance": 0.0}],
     "cognitive_load": "C"},
    {"task_id": "ss02_33",
     "content_latex": r"Určete všechna $x \in (-\pi, 2\pi]$, pro která platí $\tan\left(-x + \dfrac{\pi}{6}\right) = \sqrt{3}$.",
     "results": [{"key": "x", "label_latex": r"x \in ", "type": "mathlive",
                  "expected": r"\{-\frac{\pi}{6}, \frac{5\pi}{6}, \frac{11\pi}{6}\}", "tolerance": 0.0}],
     "cognitive_load": "D"},

    # --- 15. Cosinová věta — určit úhel γ v trojúhelníku ---------------------
    {"task_id": "ss02_34",
     "content_latex": r"Určete velikost úhlu $\gamma$ v trojúhelníku $ABC$, jestliže platí $c^2 = a^2 + b^2 + ab$.",
     "results": [{"key": "gamma", "label_latex": r"\gamma = ", "type": "decimal", "expected": 120, "tolerance": 0}],
     "cognitive_load": "C"},
    {"task_id": "ss02_35",
     "content_latex": r"Určete velikost úhlu $\gamma$ v trojúhelníku $ABC$, jestliže platí $c^2 = a^2 + b^2 - ab$.",
     "results": [{"key": "gamma", "label_latex": r"\gamma = ", "type": "decimal", "expected": 60, "tolerance": 0}],
     "cognitive_load": "C"},

    # --- 16. Cosinová věta — třetí strana -----------------------------------
    {"task_id": "ss02_36",
     "content_latex": r"Určete velikost třetí strany trojúhelníku $ABC$: dáno $a$, $c$, $\beta = 30^\circ$.",
     "results": [{"key": "b", "label_latex": r"b = ", "type": "mathlive",
                  "expected": r"\sqrt{a^2 + c^2 - ac\sqrt{3}}", "tolerance": 0.0}],
     "cognitive_load": "C"},
    {"task_id": "ss02_37",
     "content_latex": r"Určete velikost třetí strany trojúhelníku $ABC$: dáno $b$, $c$, $\alpha = 45^\circ$.",
     "results": [{"key": "a", "label_latex": r"a = ", "type": "mathlive",
                  "expected": r"\sqrt{b^2 + c^2 - bc\sqrt{2}}", "tolerance": 0.0}],
     "cognitive_load": "C"},

    # --- 17. Slovní úlohy ----------------------------------------------------
    {"task_id": "ss02_38",
     "content_latex": r"Vnitřní úhly rovnoramenného trojúhelníku, jehož obsah je $8\ \text{cm}^2$ a rameno má délku $4\ \text{cm}$. Určete největší úhel ve stupních.",
     "results": [{"key": "uhel", "label_latex": r"= ", "type": "decimal", "expected": 90, "tolerance": 0}],
     "cognitive_load": "D"},
    {"task_id": "ss02_39",
     "content_latex": (
         r"Z věže vysoké $15\ \text{m}$ a vzdálené od řeky $30\ \text{m}$ se jeví šířka řeky v úhlu $15^\circ$. "
         r"Určete šířku řeky v tomto místě (v metrech, zaokrouhleno na desetinu)."
     ),
     "results": [{"key": "sirka", "label_latex": r"\approx ", "type": "decimal",
                  "expected": 43.5, "tolerance": 0.5}],
     "cognitive_load": "D"},
    {"task_id": "ss02_40",
     "content_latex": (
         r"Na vrcholu hory stojí rozhledna vysoká $30\ \text{m}$. Její patu a vrchol je z daného místa v údolí "
         r"vidět pod výškovými úhly $\alpha = 28^\circ 30'$ a $\beta = 30^\circ 40'$. "
         r"Určete výšku hory vzhledem k rovině pozorování (v metrech, zaokrouhleno na desetiny)."
     ),
     "results": [{"key": "vyska", "label_latex": r"\approx ", "type": "decimal",
                  "expected": 325.7, "tolerance": 0.5}],
     "cognitive_load": "E"},
    {"task_id": "ss02_41",
     "content_latex": (
         r"Určete velikost zorného úhlu, pod kterým vidí pozorovatel tyč délky $7\ \text{m}$, "
         r"je-li od jednoho jejího konce vzdálen $5\ \text{m}$ a od druhého $8\ \text{m}$. "
         r"Zadejte ve stupních (zaokrouhleno)."
     ),
     "results": [{"key": "uhel", "label_latex": r"\approx ", "type": "decimal",
                  "expected": 60, "tolerance": 1}],
     "cognitive_load": "D"},
]
