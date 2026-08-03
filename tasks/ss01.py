"""
SŠ 01 — Analytická geometrie v rovině a v prostoru.

Zdroj: Overleaf `Andrea_příkladySŠ/Analytická geometrie v rovině a v prostoru.tex`.
Extrahováno 2026-08-03.

Poznámky:
- Ve zdrojích jsou hodnoty typu $3{,}5$ (desetinná čárka jako v české sazbě).
  V mathlive `expected` uvádíme jako desetinná tečka (Compute Engine standard).
- Vektory zadáváme jako uspořádané trojice/dvojice v `(a,b)` nebo `(a,b,c)`.
- Úloha 31 (odraz paprsku, konstruktivně-výpočetní — souřadnice bodu odrazu)
  ponechána jako dvě `decimal` (x, y).
- Úloha 37 (druh kuželosečky) → multiple_choice se 4 možnostmi.
"""

TASKS = [
    # 1) Délky těžnic ---------------------------------------------------------
    {"task_id": "ss01_01",
     "content_latex": r"Určete délky těžnic v trojúhelníku $ABC$: $A[3,5]$, $B[-2,1]$, $C[0,-3]$.",
     "results": [
         {"key": "t_a", "label_latex": r"t_a = ", "type": "mathlive", "expected": r"\sqrt{52}", "tolerance": 0.001},
         {"key": "t_b", "label_latex": r"t_b = ", "type": "decimal",  "expected": 3.5,           "tolerance": 0.01},
         {"key": "t_c", "label_latex": r"t_c = ", "type": "mathlive", "expected": r"\sqrt{36.25}", "tolerance": 0.001},
     ],
     "cognitive_load": "C"},
    {"task_id": "ss01_02",
     "content_latex": r"Určete délky těžnic v trojúhelníku $ABC$: $A[3,5,7]$, $B[-2,1,3]$, $C[0,-3,-1]$.",
     "results": [
         {"key": "t_a", "label_latex": r"t_a = ", "type": "mathlive", "expected": r"\sqrt{88}", "tolerance": 0.001},
         {"key": "t_b", "label_latex": r"t_b = ", "type": "decimal",  "expected": 3.5,           "tolerance": 0.01},
         {"key": "t_c", "label_latex": r"t_c = ", "type": "decimal",  "expected": 8.5,           "tolerance": 0.01},
     ],
     "cognitive_load": "C"},

    # 2) Obsah trojúhelníku ---------------------------------------------------
    {"task_id": "ss01_03",
     "content_latex": r"Určete obsah trojúhelníku $ABC$: $A[3,4]$, $B[7,8]$, $C[9,5]$.",
     "results": [{"key": "S", "label_latex": r"S = ", "type": "decimal", "expected": 10, "tolerance": 0}],
     "cognitive_load": "C"},
    {"task_id": "ss01_04",
     "content_latex": r"Určete obsah trojúhelníku $ABC$: $A[0,1,2]$, $B[1,2,0]$, $C[2,0,1]$.",
     "results": [{"key": "S", "label_latex": r"S = ", "type": "mathlive",
                  "expected": r"\frac{\sqrt{27}}{2}", "tolerance": 0.001}],
     "cognitive_load": "C"},

    # 3) Lineární kombinace vektorů ------------------------------------------
    {"task_id": "ss01_05",
     "content_latex": (
         r"Vyjádřete vektor $\vec{u} = (6, 3, 3)$ jako lineární kombinaci vektorů "
         r"$\vec{a} = (2, -2, 3)$, $\vec{b} = (1, -1, 2)$, $\vec{c} = (0, 4, 2)$: "
         r"$\vec{u} = k_1\vec{a} + k_2\vec{b} + k_3\vec{c}$."
     ),
     "results": [
         {"key": "k_1", "label_latex": r"k_1 = ", "type": "decimal", "expected": 13.5,  "tolerance": 0.001},
         {"key": "k_2", "label_latex": r"k_2 = ", "type": "decimal", "expected": -21,    "tolerance": 0.001},
         {"key": "k_3", "label_latex": r"k_3 = ", "type": "decimal", "expected": 2.25,  "tolerance": 0.001},
     ],
     "cognitive_load": "D"},
    {"task_id": "ss01_06",
     "content_latex": (
         r"Vyjádřete vektor $\vec{u} = (0, -2, 4)$ jako lineární kombinaci vektorů "
         r"$\vec{a} = (2, -2, 3)$, $\vec{b} = (1, -1, 2)$, $\vec{c} = (0, 4, 2)$: "
         r"$\vec{u} = k_1\vec{a} + k_2\vec{b} + k_3\vec{c}$."
     ),
     "results": [
         {"key": "k_1", "label_latex": r"k_1 = ", "type": "decimal", "expected": -5,    "tolerance": 0.001},
         {"key": "k_2", "label_latex": r"k_2 = ", "type": "decimal", "expected": 10,    "tolerance": 0.001},
         {"key": "k_3", "label_latex": r"k_3 = ", "type": "decimal", "expected": -0.5,  "tolerance": 0.001},
     ],
     "cognitive_load": "D"},
    {"task_id": "ss01_07",
     "content_latex": (
         r"Vyjádřete vektor $\vec{u} = (1, 1, 1)$ jako lineární kombinaci vektorů "
         r"$\vec{a} = (2, -2, 3)$, $\vec{b} = (1, -1, 2)$, $\vec{c} = (0, 4, 2)$: "
         r"$\vec{u} = k_1\vec{a} + k_2\vec{b} + k_3\vec{c}$."
     ),
     "results": [
         {"key": "k_1", "label_latex": r"k_1 = ", "type": "decimal", "expected": 2,    "tolerance": 0.001},
         {"key": "k_2", "label_latex": r"k_2 = ", "type": "decimal", "expected": -3,   "tolerance": 0.001},
         {"key": "k_3", "label_latex": r"k_3 = ", "type": "decimal", "expected": 0.5,  "tolerance": 0.001},
     ],
     "cognitive_load": "D"},

    # 4) Vnitřní úhly trojúhelníku (v prostoru) --------------------------------
    {"task_id": "ss01_08",
     "content_latex": r"Určete velikosti vnitřních úhlů trojúhelníku $ABC$: $A[2,-4,9]$, $B[-1,-4,5]$, $C[6,-4,6]$. Uveďte ve stupních.",
     "results": [
         {"key": "alpha", "label_latex": r"\alpha = ", "type": "decimal", "expected": 90, "tolerance": 0},
         {"key": "beta",  "label_latex": r"\beta = ",  "type": "decimal", "expected": 45, "tolerance": 0},
         {"key": "gamma", "label_latex": r"\gamma = ", "type": "decimal", "expected": 45, "tolerance": 0},
     ],
     "cognitive_load": "D"},

    # 5) Leží body v téže rovině? -> multiple_choice --------------------------
    {"task_id": "ss01_09",
     "content_latex": r"Rozhodněte, zda body $A[3,1,2]$, $B[2,-1,-2]$, $C[0,3,5]$, $D[-3,0,2]$ leží v téže rovině.",
     "results": [{"key": "lezi", "label_latex": r"\text{Odpověď: }", "type": "multiple_choice",
                  "options": [{"key":"a","label_latex":r"leží"},{"key":"b","label_latex":r"neleží"}],
                  "expected": "b"}],
     "cognitive_load": "D"},
    {"task_id": "ss01_10",
     "content_latex": r"Rozhodněte, zda body $A[1,2,-1]$, $B[0,1,5]$, $C[-1,2,1]$, $D[2,1,3]$ leží v téže rovině.",
     "results": [{"key": "lezi", "label_latex": r"\text{Odpověď: }", "type": "multiple_choice",
                  "options": [{"key":"a","label_latex":r"leží"},{"key":"b","label_latex":r"neleží"}],
                  "expected": "a"}],
     "cognitive_load": "D"},

    # 6) Vrchol C z A, B a těžiště T -------------------------------------------
    {"task_id": "ss01_11",
     "content_latex": r"Určete souřadnice vrcholu $C$ trojúhelníku $ABC$: $A[4,8]$, $B[-4,0]$, $T[1,-5]$ (těžiště).",
     "results": [
         {"key": "C_x", "label_latex": r"C_x = ", "type": "decimal", "expected": 3,   "tolerance": 0.001},
         {"key": "C_y", "label_latex": r"C_y = ", "type": "decimal", "expected": -23, "tolerance": 0.001},
     ],
     "cognitive_load": "C"},
    {"task_id": "ss01_12",
     "content_latex": r"Určete souřadnice vrcholu $C$ trojúhelníku $ABC$: $A[3,3,3]$, $B[-2,1,2]$, $T[0,-1,0]$ (těžiště).",
     "results": [
         {"key": "C_x", "label_latex": r"C_x = ", "type": "decimal", "expected": -1, "tolerance": 0.001},
         {"key": "C_y", "label_latex": r"C_y = ", "type": "decimal", "expected": -7, "tolerance": 0.001},
         {"key": "C_z", "label_latex": r"C_z = ", "type": "decimal", "expected": -5, "tolerance": 0.001},
     ],
     "cognitive_load": "C"},

    # 7) Vzdálenost rovnoběžných přímek ---------------------------------------
    {"task_id": "ss01_13",
     "content_latex": r"Přímky $p: 2x - 3y = 6$ a $q: -4x + 6y + 25 = 0$ jsou rovnoběžné. Určete jejich vzdálenost.",
     "results": [{"key": "d", "label_latex": r"d = ", "type": "mathlive",
                  "expected": r"\frac{\sqrt{13}}{2}", "tolerance": 0.001}],
     "cognitive_load": "C"},

    # 8) Rovnice přímky (kolmá + průsečík) ------------------------------------
    {"task_id": "ss01_14",
     "content_latex": (
         r"Napište rovnici přímky procházející průsečíkem přímek "
         r"$p: 5x - y + 10 = 0$, $q: 8x + 4y + 9 = 0$, která je kolmá na $r: x + 3y = 0$."
     ),
     "results": [{"key": "primka", "label_latex": r"\text{Rovnice: }", "type": "mathlive",
                  "expected": r"6x - 2y + 13 = 0", "tolerance": 0.0}],
     "cognitive_load": "D"},

    # 9) Odchylka přímek -------------------------------------------------------
    {"task_id": "ss01_15",
     "content_latex": r"Určete odchylku přímek $p: 5x - y + 7 = 0$, $q: 2x - 3y + 1 = 0$.",
     "results": [{"key": "phi", "label_latex": r"\varphi = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{4}", "tolerance": 0.001}],
     "cognitive_load": "C"},

    # 10) Vzdálenost počátku od přímky ----------------------------------------
    {"task_id": "ss01_16",
     "content_latex": r"Určete vzdálenost počátku soustavy souřadnic od přímky $p: 9x - 12y + 10 = 0$.",
     "results": [{"key": "d", "label_latex": r"d = ", "type": "mathlive",
                  "expected": r"\frac{2}{3}", "tolerance": 0.001}],
     "cognitive_load": "B"},

    # 11) Rovnice přímek přes bod P s danou vzdáleností — 2 řešení
    {"task_id": "ss01_17",
     "content_latex": (
         r"Napište rovnici přímky procházející bodem $P[-2, 5]$ a mající od bodu $Q[3, 5]$ "
         r"vzdálenost $d = \sqrt{5}$. Uveďte rovnici v obecném tvaru $Ax + By + C = 0$ (existují dvě řešení, zadejte obě)."
     ),
     "results": [
         {"key": "p_1", "label_latex": r"p_1: ", "type": "mathlive",
          "expected": r"x - 2y + 12 = 0", "tolerance": 0.0},
         {"key": "p_2", "label_latex": r"p_2: ", "type": "mathlive",
          "expected": r"x + 2y - 8 = 0", "tolerance": 0.0},
     ],
     "cognitive_load": "D"},

    # 12) Parametrické rovnice přímky AB --------------------------------------
    {"task_id": "ss01_18",
     "content_latex": r"Napište parametrické rovnice přímky $AB$: $A[2,-3]$, $B[-2,5]$ (tvar $x = x_0 + at$, $y = y_0 + bt$; napište pravé strany).",
     "results": [
         {"key": "x_t", "label_latex": r"x = ", "type": "mathlive", "expected": r"2 - 4t", "tolerance": 0.0},
         {"key": "y_t", "label_latex": r"y = ", "type": "mathlive", "expected": r"-3 + 8t", "tolerance": 0.0},
     ],
     "cognitive_load": "C"},

    # 13) Určit a, b tak, aby parametr. tvar vyjadřoval přímku AB -------------
    {"task_id": "ss01_19",
     "content_latex": (
         r"Určete čísla $a$, $b$ tak, aby soustava $x = a + 3t$, $y = 4 - bt$ vyjadřovala přímku určenou "
         r"body $A[1, 0]$, $B[3, -1]$."
     ),
     "results": [
         {"key": "a", "label_latex": r"a = ", "type": "decimal", "expected": -7,  "tolerance": 0.001},
         {"key": "b", "label_latex": r"b = ", "type": "decimal", "expected": 1.5, "tolerance": 0.001},
     ],
     "cognitive_load": "D"},

    # 14) Průsečík výšek --------------------------------------------------------
    {"task_id": "ss01_20",
     "content_latex": r"Určete souřadnice průsečíku výšek trojúhelníku $ABC$: $A[7,8]$, $B[5,-2]$, $C[-3,-6]$.",
     "results": [
         {"key": "V_x", "label_latex": r"V_x = ", "type": "mathlive", "expected": r"\frac{143}{9}",  "tolerance": 0.001},
         {"key": "V_y", "label_latex": r"V_y = ", "type": "mathlive", "expected": r"-\frac{88}{9}", "tolerance": 0.001},
     ],
     "cognitive_load": "D"},

    # 15) Bod na přímce se stejnou vzdáleností od M, N ------------------------
    {"task_id": "ss01_21",
     "content_latex": r"Určete bod přímky $5x - 4y - 28 = 0$, který má stejnou vzdálenost od bodů $M[1, 5]$ a $N[7, -3]$.",
     "results": [
         {"key": "x", "label_latex": r"x = ", "type": "decimal",  "expected": 10, "tolerance": 0.001},
         {"key": "y", "label_latex": r"y = ", "type": "mathlive", "expected": r"\frac{11}{2}", "tolerance": 0.001},
     ],
     "cognitive_load": "D"},

    # 16) Podmínky na parametry a, b, c -- 3 případy (a,b,c) → multiple_choice
    #     Obtížné pro mathlive; místo toho MC výběr správné podmínky.
    {"task_id": "ss01_22",
     "content_latex": (
         r"Rovnice $3x - 5y + 4 = 0$, $(2 - a)x - 3by + 3 - c = 0$ mají vyjadřovat \emph{tutéž} přímku. "
         r"Vyberte správnou dvojici podmínek."
     ),
     "results": [{"key": "podminky", "label_latex": r"\text{Podmínky: }", "type": "multiple_choice",
                  "options": [
                      {"key":"a","label_latex":r"$5a + 9b = 10,\ 5c + 12b = 15$"},
                      {"key":"b","label_latex":r"$3a - 5b = 4,\ c = 4$"},
                      {"key":"c","label_latex":r"$2 - a = 3,\ 3b = 5$"},
                  ],
                  "expected": "a"}],
     "cognitive_load": "D"},
    {"task_id": "ss01_23",
     "content_latex": (
         r"Rovnice $3x - 5y + 4 = 0$, $(2 - a)x - 3by + 3 - c = 0$ mají vyjadřovat \emph{dvě různé rovnoběžky}. "
         r"Vyberte správnou sadu podmínek."
     ),
     "results": [{"key": "podminky", "label_latex": r"\text{Podmínky: }", "type": "multiple_choice",
                  "options": [
                      {"key":"a","label_latex":r"$5a + 9b = 10,\ 5c + 12b = 15$"},
                      {"key":"b","label_latex":r"$5a + 9b = 10,\ 5c + 12b \neq 15,\ a \neq 2,\ b \neq 0$"},
                      {"key":"c","label_latex":r"$5a + 9b \neq 10$"},
                  ],
                  "expected": "b"}],
     "cognitive_load": "E"},
    {"task_id": "ss01_24",
     "content_latex": (
         r"Rovnice $3x - 5y + 4 = 0$, $(2 - a)x - 3by + 3 - c = 0$ mají vyjadřovat \emph{dvě různoběžky}. "
         r"Vyberte správnou podmínku."
     ),
     "results": [{"key": "podminka", "label_latex": r"\text{Podmínka: }", "type": "multiple_choice",
                  "options": [
                      {"key":"a","label_latex":r"$5a + 9b = 10,\ 5c + 12b = 15$"},
                      {"key":"b","label_latex":r"$5a + 9b = 10,\ b \neq 0$"},
                      {"key":"c","label_latex":r"$5a + 9b \neq 10$"},
                  ],
                  "expected": "c"}],
     "cognitive_load": "D"},

    # 17) Obecná a parametrická rovnice roviny ABC ----------------------------
    {"task_id": "ss01_25",
     "content_latex": r"Jsou dány body $A[0,0,6]$, $B[0,2,0]$, $C[-2,0,0]$. Určete obecnou rovnici roviny $ABC$.",
     "results": [{"key": "rov", "label_latex": r"\text{Rovina: }", "type": "mathlive",
                  "expected": r"3x - 3y - z + 6 = 0", "tolerance": 0.0}],
     "cognitive_load": "C"},
    {"task_id": "ss01_26",
     "content_latex": (
         r"Jsou dány body $A[0,0,6]$, $B[0,2,0]$, $C[-2,0,0]$. Napište parametrické vyjádření roviny $ABC$ "
         r"ve tvaru $x = ?,\ y = ?,\ z = ?$ (parametry $t, s \in \mathbb{R}$)."
     ),
     "results": [
         {"key": "x_ts", "label_latex": r"x = ", "type": "mathlive", "expected": r"t - s",       "tolerance": 0.0},
         {"key": "y_ts", "label_latex": r"y = ", "type": "mathlive", "expected": r"1 + t - 2s",  "tolerance": 0.0},
         {"key": "z_ts", "label_latex": r"z = ", "type": "mathlive", "expected": r"3 + 3s",      "tolerance": 0.0},
     ],
     "cognitive_load": "D"},

    # 18) Rovina kolmá na AB ---------------------------------------------------
    {"task_id": "ss01_27",
     "content_latex": r"Jsou dány body $A[0,-1,3]$, $B[1,3,5]$. Napište obecnou rovnici roviny, která prochází bodem $B$ a je kolmá na přímku $AB$.",
     "results": [{"key": "rov", "label_latex": r"\text{Rovina: }", "type": "mathlive",
                  "expected": r"x + 4y + 2z - 23 = 0", "tolerance": 0.0}],
     "cognitive_load": "D"},

    # 19) Rovina rovnoběžná s osou y ------------------------------------------
    {"task_id": "ss01_28",
     "content_latex": r"Napište obecnou rovnici roviny rovnoběžné s osou $y$ procházející body $A[0,1,3]$, $B[2,4,5]$.",
     "results": [{"key": "rov", "label_latex": r"\text{Rovina: }", "type": "mathlive",
                  "expected": r"x - z + 3 = 0", "tolerance": 0.0}],
     "cognitive_load": "D"},

    # 20) Rovina osou z + bod --------------------------------------------------
    {"task_id": "ss01_29",
     "content_latex": r"Napište obecnou rovnici roviny, která prochází osou $z$ a bodem $A[2, -4, 3]$.",
     "results": [{"key": "rov", "label_latex": r"\text{Rovina: }", "type": "mathlive",
                  "expected": r"2x + y = 0", "tolerance": 0.0}],
     "cognitive_load": "C"},

    # 21) Rovina rovnoběžná s danou -------------------------------------------
    {"task_id": "ss01_30",
     "content_latex": r"Určete rovnici roviny procházející bodem $M[2,2,-2]$, která je rovnoběžná s rovinou $x - 2y - 3z = 0$.",
     "results": [{"key": "rov", "label_latex": r"\text{Rovina: }", "type": "mathlive",
                  "expected": r"x - 2y - 3z - 4 = 0", "tolerance": 0.0}],
     "cognitive_load": "C"},

    # 22) Odchylka dvou rovin --------------------------------------------------
    {"task_id": "ss01_31",
     "content_latex": (
         r"Určete odchylku dvou rovin: první určena body $M[2,-2,4]$, $N[4,3,2]$, $L[0,6,6]$; "
         r"druhá má rovnici $x - 2y + 2z - 8 = 0$."
     ),
     "results": [{"key": "phi", "label_latex": r"\varphi = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{4}", "tolerance": 0.001}],
     "cognitive_load": "D"},

    # 23) Vzdálenost rovnoběžných rovin + od počátku --------------------------
    {"task_id": "ss01_32",
     "content_latex": r"Určete vzdálenost rovnoběžných rovin $x - 2y + 2z - 5 = 0$ a $x - 2y + 2z + 13 = 0$, dále vzdálenost počátku od každé z nich.",
     "results": [
         {"key": "d",   "label_latex": r"d = ",   "type": "decimal",  "expected": 6, "tolerance": 0},
         {"key": "d_1", "label_latex": r"d_1 = ", "type": "mathlive", "expected": r"\frac{5}{3}",  "tolerance": 0.001},
         {"key": "d_2", "label_latex": r"d_2 = ", "type": "mathlive", "expected": r"\frac{13}{3}", "tolerance": 0.001},
     ],
     "cognitive_load": "D"},

    # 24) Poloha roviny a přímky ----------------------------------------------
    {"task_id": "ss01_33",
     "content_latex": (
         r"Určete vzájemnou polohu roviny $2x + y + z + 8 = 0$ a přímky $PQ$: $P[0,0,0]$, $Q[1,0,2]$. "
         r"Uveďte souřadnice průsečíku."
     ),
     "results": [
         {"key": "X_x", "label_latex": r"X_x = ", "type": "decimal", "expected": -2, "tolerance": 0.001},
         {"key": "X_y", "label_latex": r"X_y = ", "type": "decimal", "expected": 0,  "tolerance": 0.001},
         {"key": "X_z", "label_latex": r"X_z = ", "type": "decimal", "expected": -4, "tolerance": 0.001},
     ],
     "cognitive_load": "D"},

    # 25) Odchylka přímek -----------------------------------------------------
    {"task_id": "ss01_34",
     "content_latex": (
         r"Určete odchylku přímek $p$ a $AB$: $A[1,0,3]$, $B[2,1,1]$; "
         r"$p$: $x = 3 - t$, $y = 1$, $z = -1 + t$, $t \in \mathbb{R}$."
     ),
     "results": [{"key": "phi", "label_latex": r"\varphi = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{6}", "tolerance": 0.001}],
     "cognitive_load": "D"},

    # 26) Průsečnice rovin (parametricky) --------------------------------------
    {"task_id": "ss01_35",
     "content_latex": r"Vyjádřete parametricky průsečnici rovin $x + y - z + 3 = 0$ a $2x - y + z - 9 = 0$ ($t \in \mathbb{R}$). Uveďte $x, y, z$ jako funkci $t$.",
     "results": [
         {"key": "x_t", "label_latex": r"x = ", "type": "mathlive", "expected": r"2",        "tolerance": 0.0},
         {"key": "y_t", "label_latex": r"y = ", "type": "mathlive", "expected": r"-5 + t",   "tolerance": 0.0},
         {"key": "z_t", "label_latex": r"z = ", "type": "mathlive", "expected": r"t",        "tolerance": 0.0},
     ],
     "cognitive_load": "E"},

    # 27) Odchylka rovin -------------------------------------------------------
    {"task_id": "ss01_36",
     "content_latex": r"Určete odchylku rovin $x - z = 0$ a $x + y = 0$.",
     "results": [{"key": "phi", "label_latex": r"\varphi = ", "type": "mathlive",
                  "expected": r"\frac{\pi}{3}", "tolerance": 0.001}],
     "cognitive_load": "C"},

    # 28) Vzdálenost bodu od přímky --------------------------------------------
    {"task_id": "ss01_37",
     "content_latex": r"Určete vzdálenost bodu $A[5, -6, 6]$ od přímky $PQ$: $P[-2, -5, 4]$, $Q[4, 1, 4]$.",
     "results": [{"key": "d", "label_latex": r"d = ", "type": "decimal", "expected": 6, "tolerance": 0}],
     "cognitive_load": "D"},

    # 29) Odchylka přímky a roviny ---------------------------------------------
    {"task_id": "ss01_38",
     "content_latex": r"Určete odchylku přímky $AB$ ($A[1, 0, 7]$, $B[3, -3, 6]$) a roviny $2x - 3y + z + 4 = 0$. Uveďte ve stupních (zaokrouhleno).",
     "results": [{"key": "alpha", "label_latex": r"\alpha \approx ", "type": "decimal",
                  "expected": 59, "tolerance": 1}],
     "cognitive_load": "D"},

    # 30) Rovina počátkem a kolmá na dvě roviny --------------------------------
    {"task_id": "ss01_39",
     "content_latex": (
         r"Napište rovnici roviny, která prochází počátkem soustavy souřadnic "
         r"a je kolmá na roviny $x + 2y + z - 12 = 0$, $2x - y - 3z = 0$."
     ),
     "results": [{"key": "rov", "label_latex": r"\text{Rovina: }", "type": "mathlive",
                  "expected": r"x - y + z = 0", "tolerance": 0.0}],
     "cognitive_load": "E"},

    # 31) Odraz paprsku — souřadnice bodu odrazu -------------------------------
    {"task_id": "ss01_40",
     "content_latex": (
         r"Světelný paprsek vychází z bodu $A[2, 3]$, odráží se od přímky $x + y = 0$ do bodu $B[1, 1]$. "
         r"Určete souřadnice bodu odrazu."
     ),
     "results": [
         {"key": "x", "label_latex": r"x = ", "type": "mathlive", "expected": r"-\frac{1}{7}", "tolerance": 0.001},
         {"key": "y", "label_latex": r"y = ", "type": "mathlive", "expected": r"\frac{1}{7}",  "tolerance": 0.001},
     ],
     "cognitive_load": "E"},

    # 32) Rovnice kružnice přes body + středový bod na přímce ------------------
    {"task_id": "ss01_41",
     "content_latex": r"Určete rovnici kružnice procházející body $A[3, 0]$, $B[-1, 2]$, jejíž střed leží na přímce $x - y + 2 = 0$.",
     "results": [{"key": "kruz", "label_latex": r"\text{Rovnice: }", "type": "mathlive",
                  "expected": r"(x - 3)^2 + (y - 5)^2 = 25", "tolerance": 0.0}],
     "cognitive_load": "D"},

    # 33) Kružnice dotykem přímky v bodě + přes počátek -----------------------
    {"task_id": "ss01_42",
     "content_latex": r"Určete rovnici kružnice, která se dotýká přímky $2x - y + 2 = 0$ v bodě $[2, 6]$ a prochází počátkem.",
     "results": [{"key": "kruz", "label_latex": r"\text{Rovnice: }", "type": "mathlive",
                  "expected": r"(x - 22)^2 + (y + 4)^2 = 500", "tolerance": 0.0}],
     "cognitive_load": "E"},

    # 34) Bod kružnice s max. vzdáleností od A ---------------------------------
    {"task_id": "ss01_43",
     "content_latex": r"Určete bod kružnice $(x - 1)^2 + (y + 2)^2 = 25$ s největší vzdáleností od bodu $A[-7, 4]$.",
     "results": [
         {"key": "x", "label_latex": r"x = ", "type": "decimal", "expected": 5,  "tolerance": 0.001},
         {"key": "y", "label_latex": r"y = ", "type": "decimal", "expected": -5, "tolerance": 0.001},
     ],
     "cognitive_load": "D"},

    # 35a) Dotyčnice kružnice rovnoběžné s přímkou (2 tečny) ------------------
    {"task_id": "ss01_44",
     "content_latex": (
         r"Kružnice $x^2 + y^2 - 6x - 4y - 3 = 0$. Určete její dotyčnice rovnoběžné s přímkou $6x + 8y - 21 = 0$ "
         r"(existují dvě, uveďte obě v obecném tvaru)."
     ),
     "results": [
         {"key": "t_1", "label_latex": r"t_1: ", "type": "mathlive", "expected": r"3x + 4y + 3 = 0",  "tolerance": 0.0},
         {"key": "t_2", "label_latex": r"t_2: ", "type": "mathlive", "expected": r"3x + 4y - 37 = 0", "tolerance": 0.0},
     ],
     "cognitive_load": "E"},
    # 35b) Dotyčnice kolmé na přímku ------------------------------------------
    {"task_id": "ss01_45",
     "content_latex": (
         r"Kružnice $x^2 + y^2 - 6x - 4y - 3 = 0$. Určete dotyčnice kolmé na přímku $4x + y - 9 = 0$ "
         r"(existují dvě, uveďte obě)."
     ),
     "results": [
         {"key": "t_1", "label_latex": r"t_1: ", "type": "mathlive",
          "expected": r"x - 4y + 5 + 4\sqrt{17} = 0", "tolerance": 0.0},
         {"key": "t_2", "label_latex": r"t_2: ", "type": "mathlive",
          "expected": r"x - 4y + 5 - 4\sqrt{17} = 0", "tolerance": 0.0},
     ],
     "cognitive_load": "E"},

    # 36) Dotyčnice kružnice z bodu P ------------------------------------------
    {"task_id": "ss01_46",
     "content_latex": (
         r"Určete rovnice dotyčnic vedených z bodu $P[2, 7]$ ke kružnici $x^2 + y^2 - 16x - 6y + 57 = 0$ "
         r"(existují dvě, uveďte obě)."
     ),
     "results": [
         {"key": "t_1", "label_latex": r"t_1: ", "type": "mathlive",
          "expected": r"y = 7", "tolerance": 0.0},
         {"key": "t_2", "label_latex": r"t_2: ", "type": "mathlive",
          "expected": r"30y + 73x - 356 = 0", "tolerance": 0.0},
     ],
     "cognitive_load": "E"},

    # 37) Druh kuželosečky — multiple_choice pro každou z a-d rovnic ----------
    {"task_id": "ss01_47",
     "content_latex": r"Rozhodněte, jaký druh kuželosečky vyjadřuje rovnice $x^2 - 12x - 6y + 57 = 0$.",
     "results": [{"key": "typ", "label_latex": r"\text{Druh: }", "type": "multiple_choice",
                  "options": [
                      {"key":"a","label_latex":r"parabola"}, {"key":"b","label_latex":r"elipsa"},
                      {"key":"c","label_latex":r"hyperbola"}, {"key":"d","label_latex":r"kružnice"}],
                  "expected": "a"}],
     "cognitive_load": "C"},
    {"task_id": "ss01_48",
     "content_latex": r"Rozhodněte, jaký druh kuželosečky vyjadřuje rovnice $x^2 + 6x - 9y = 0$.",
     "results": [{"key": "typ", "label_latex": r"\text{Druh: }", "type": "multiple_choice",
                  "options": [
                      {"key":"a","label_latex":r"parabola"}, {"key":"b","label_latex":r"elipsa"},
                      {"key":"c","label_latex":r"hyperbola"}, {"key":"d","label_latex":r"kružnice"}],
                  "expected": "a"}],
     "cognitive_load": "C"},
    {"task_id": "ss01_49",
     "content_latex": r"Rozhodněte, jaký druh kuželosečky vyjadřuje rovnice $4x^2 + 9y^2 - 8x - 36y + 4 = 0$.",
     "results": [{"key": "typ", "label_latex": r"\text{Druh: }", "type": "multiple_choice",
                  "options": [
                      {"key":"a","label_latex":r"parabola"}, {"key":"b","label_latex":r"elipsa"},
                      {"key":"c","label_latex":r"hyperbola"}, {"key":"d","label_latex":r"kružnice"}],
                  "expected": "b"}],
     "cognitive_load": "C"},
    {"task_id": "ss01_50",
     "content_latex": r"Rozhodněte, jaký druh kuželosečky vyjadřuje rovnice $2x^2 - 3y^2 - 8x + 6y - 25 = 0$.",
     "results": [{"key": "typ", "label_latex": r"\text{Druh: }", "type": "multiple_choice",
                  "options": [
                      {"key":"a","label_latex":r"parabola"}, {"key":"b","label_latex":r"elipsa"},
                      {"key":"c","label_latex":r"hyperbola"}, {"key":"d","label_latex":r"kružnice"}],
                  "expected": "c"}],
     "cognitive_load": "C"},

    # 38) Dotyčnice elipsy rovnoběžné s přímkou (2 řešení) --------------------
    {"task_id": "ss01_51",
     "content_latex": r"Určete rovnice dotyčnic elipsy $x^2 + 4y^2 - 4 = 0$ rovnoběžných s přímkou $y - x = 0$ (existují dvě, uveďte obě).",
     "results": [
         {"key": "t_1", "label_latex": r"t_1: ", "type": "mathlive", "expected": r"x - y + \sqrt{5} = 0", "tolerance": 0.0},
         {"key": "t_2", "label_latex": r"t_2: ", "type": "mathlive", "expected": r"x - y - \sqrt{5} = 0", "tolerance": 0.0},
     ],
     "cognitive_load": "E"},

    # 39a-b) Dotyčnice ke kuželosečce z daného bodu (2 řešení) ----------------
    {"task_id": "ss01_52",
     "content_latex": r"Napište rovnice dotyčnic ke kuželosečce $y^2 - x^2 = 9$ procházejících bodem $A[-6, 3]$ (dvě).",
     "results": [
         {"key": "t_1", "label_latex": r"t_1: ", "type": "mathlive", "expected": r"y - 3 = 0",           "tolerance": 0.0},
         {"key": "t_2", "label_latex": r"t_2: ", "type": "mathlive", "expected": r"4x + 5y + 9 = 0",     "tolerance": 0.0},
     ],
     "cognitive_load": "E"},
    {"task_id": "ss01_53",
     "content_latex": r"Napište rovnice dotyčnic ke kuželosečce $5x^2 + 9y^2 = 45$ procházejících bodem $A[0, -3]$ (dvě).",
     "results": [
         {"key": "t_1", "label_latex": r"t_1: ", "type": "mathlive", "expected": r"2x - 3y - 9 = 0", "tolerance": 0.0},
         {"key": "t_2", "label_latex": r"t_2: ", "type": "mathlive", "expected": r"2x + 3y + 9 = 0", "tolerance": 0.0},
     ],
     "cognitive_load": "E"},

    # 40a-b) Dotyčnice paraboly rovnoběžné s AB -------------------------------
    {"task_id": "ss01_54",
     "content_latex": r"Napište rovnici dotyčnice k parabole $4(y - 2) = (x + 1)^2$ rovnoběžné s přímkou $AB$: $A[2, 5]$, $B[-3, 1]$.",
     "results": [{"key": "t", "label_latex": r"t: ", "type": "mathlive",
                  "expected": r"20x - 25y + 54 = 0", "tolerance": 0.0}],
     "cognitive_load": "E"},
    {"task_id": "ss01_55",
     "content_latex": r"Napište rovnici dotyčnice k parabole $-(x - 3) = (y + 4)^2$ rovnoběžné s přímkou $AB$: $A[2, 5]$, $B[-3, 1]$.",
     "results": [{"key": "t", "label_latex": r"t: ", "type": "mathlive",
                  "expected": r"64x - 80y - 537 = 0", "tolerance": 0.0}],
     "cognitive_load": "E"},
]
