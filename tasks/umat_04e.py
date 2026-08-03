"""
Reálné funkce (extra).

Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/4_realnefunkce.tex` (2007-05-29).
Automaticky vyextrahováno scripts/extract_umat_v2.py 2026-08-03.

Rozšířený parser oproti v1: převod textových odpovědí na multiple_choice,
seznamů čísel na N decimal keys, a parsing \\begin{ul}...\\end{ul} bloků
s odpovědí v následujícím `Řešení:` odstavci.
"""

TASKS = [
    {
        "task_id": 'e04_01',
        "content_latex": 'Určete maximální definiční obor $Df$ daného zobrazení $f$: $f: y = \\sqrt{x+3} + \\sqrt{5-x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Df = \\langle -3, \\,5\\rangle', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_02',
        "content_latex": 'Určete maximální definiční obor $Df$ daného zobrazení $f$: $f: y = \\sqrt{x^3 -8}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Df = \\langle 2, \\,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_03',
        "content_latex": 'Určete maximální definiční obor $Df$ daného zobrazení $f$: $f: y = \\frac{1}{x+1} + \\frac{1}{x^2-4}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Df = \\{x \\in {\\Bbb R}: x \\neq -1 \\,\\,\\text{a současně} \\,\\, x \\neq \\pm 2\\}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_04',
        "content_latex": 'Určete maximální definiční obor $Df$ daného zobrazení $f$: $f: y = \\sqrt{x^2-1} + \\sqrt{4-x^2}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Df = \\langle -2, \\,-1\\rangle \\cup \\langle 1, \\,2\\rangle', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_05',
        "content_latex": 'Určete maximální definiční obor $Df$ daného zobrazení $f$: $f: y = \\sqrt{\\frac{x}{1+x}}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Df = (-\\infty, \\,-1) \\cup \\langle 0, \\,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_06',
        "content_latex": 'Určete maximální definiční obor $Df$ daného zobrazení $f$: $f: y = \\sqrt{x^3-9x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$Df = \\langle -3, \\,0\\rangle \\cup \\langle 3, \\,\\infty)$ $\\clubsuit$ \\pagebreak \\section{Prosté zobrazení}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_07',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = x^3-5$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'prostá, důkaz sporem', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_08',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = x^3 + x^2-1$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'není prostá: např. $f(0) = f(-1) = -1$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_09',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = \\sqrt{1+5x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'prostá, důkaz sporem', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_10',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = x^4 -2x^2$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'není prostá: např. $f(\\sqrt2) = f(\\sqrt{-2}) = 0$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_11',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = \\frac{1}{1-x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'prostá, důkaz sporem', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_12',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = \\frac{2+2x}{1-x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'prostá, důkaz sporem', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_13',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = \\frac{1}{1+x^3}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'prostá, důkaz sporem', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_14',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = x^3 - 4x + 5$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'není prostá: např. $f(\\pm\\sqrt2) = f(0) = 5$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_15',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = \\sqrt{4+5x^2}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'není prostá, např. $f(1) = f(-1) = 3$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_16',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = \\frac{x}{x^2-4}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'není prostá, např. $f(1) = f(-4) = -1/3$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_17',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = \\frac{x^3-1}{x^3+1}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'prostá, důkaz sporem', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_18',
        "content_latex": 'Zkoumejte, zda dané funkce jsou nebo nejsou prosté na svých maximálních definičních oborech; zdůvodněte: $f: y = \\sqrt{x - x^2}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'není prostá, např. $f(0) = f(1) = 0$. $\\clubsuit$ \\pagebreak \\section{Složené zobrazení}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_19',
        "content_latex": 'Nechť $f: y = 3x-5$, $g: y = 2-x^2$. Určete následující hodnoty příslušných složených funkcí: $f(g(0))$, \\quad $g(f(0))$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '1, $-23$; \\quad', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_20',
        "content_latex": 'Nechť $f: y = 3x-5$, $g: y = 2-x^2$. Určete následující hodnoty příslušných složených funkcí: $f(f(4))$, \\quad $g(g(3))$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '16, $-47$; \\quad', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_21',
        "content_latex": 'Nechť $f: y = 3x-5$, $g: y = 2-x^2$. Určete následující hodnoty příslušných složených funkcí: $f(f(f(-1)))$, \\quad $g(-g(3))$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$-92$, $-47$; \\quad', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_22',
        "content_latex": 'Nechť $f: y = 3x-5$, $g: y = 2-x^2$. Určete následující hodnoty příslušných složených funkcí: $f(1+g(0))$, \\quad $g(f(2)-1)$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '4, 2; \\quad', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_23',
        "content_latex": 'Nechť $f: y = 3x-5$, $g: y = 2-x^2$. Určete následující hodnoty příslušných složených funkcí: $f(3g(1))$, \\quad $g(f(0)+g(1))$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '4, $-14$; \\quad', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_24',
        "content_latex": 'Nechť $f: y = 3x-5$, $g: y = 2-x^2$. Určete následující hodnoty příslušných složených funkcí: $f(g(2)-g(-2))$, \\quad $g(f(1) + f(-1))$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$-5$, $-98$. $\\clubsuit$ \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_25',
        "content_latex": 'Z daných zobrazení utvořte složená zobrazení $F_1 = f \\circ g$, $F_2 = g \\circ f$, $F_3 = f \\circ f$, $F_4 = g \\circ g$. Určete definiční obory těchto složených zobrazení: $f: y = 6x-5$, \\quad $g: y = \\frac{x}{2}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$F_1 = 3x-5$, $F_2 = 3x-5/2$, $F_3 = 36x-35$, $F_4 = x/4$, $DF_1 = DF_2 = DF_3 = DF_4 = {\\Bbb R}$; \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_26',
        "content_latex": 'Z daných zobrazení utvořte složená zobrazení $F_1 = f \\circ g$, $F_2 = g \\circ f$, $F_3 = f \\circ f$, $F_4 = g \\circ g$. Určete definiční obory těchto složených zobrazení: $f: y = x^3 + 2$, \\quad $g: y = \\sqrt[3]{2x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$F_1 = 2x+2$, $F_2 = \\sqrt[3]{2x^3+4}$, $F_3 = (x^3+2)^3+2$, $F_4 = \\sqrt[3]{2}\\sqrt[9]{2x}$, $DF_1 = DF_2 = DF_3 = DF_4 = {\\Bbb R}$; \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_27',
        "content_latex": 'Z daných zobrazení utvořte složená zobrazení $F_1 = f \\circ g$, $F_2 = g \\circ f$, $F_3 = f \\circ f$, $F_4 = g \\circ g$. Určete definiční obory těchto složených zobrazení: $f: y = \\frac{1}{x}$, \\quad $g: y = 2x+4$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$F_1 = \\frac{1}{2x+4}$, $F_2 = \\frac{2}{x} +4$, $F_3 = x$, $F_4 = 4x+12$, $DF_1 = \\{x \\in {\\Bbb R}: x \\neq -2\\}$, $DF_2 = \\{x \\in {\\Bbb R}: x \\neq 0\\}$, $DF_3 = DF_4 = {\\Bbb R}$; \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_28',
        "content_latex": 'Z daných zobrazení utvořte složená zobrazení $F_1 = f \\circ g$, $F_2 = g \\circ f$, $F_3 = f \\circ f$, $F_4 = g \\circ g$. Určete definiční obory těchto složených zobrazení: $f: y = \\frac{x}{x+1}$, \\quad $g: y = 1-2x$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$F_1 = \\frac{1-2x}{2-2x}$, $F_2 = \\frac{1-x}{1+x}$, $F_3 = \\frac{x}{2x+1}$, $F_4 = 4x-1$, $DF_1 = \\{x \\in {\\Bbb R}: x \\neq 1\\}$, $DF_2 = \\{x \\in {\\Bbb R}: x \\neq -1\\}$, $DF_3 = \\{x \\in {\\Bbb R}: x \\neq -1/2\\}$, $DF_4 = {\\Bbb R}$; \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_29',
        "content_latex": 'Z daných zobrazení utvořte složená zobrazení $F_1 = f \\circ g$, $F_2 = g \\circ f$, $F_3 = f \\circ f$, $F_4 = g \\circ g$. Určete definiční obory těchto složených zobrazení: $f: y = \\sqrt[3]{x}$, \\quad $g: y = \\sqrt[4]{x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$F_1 = F_2 = \\sqrt[12]{x}$, $F_3 = \\sqrt[9]{x}$, $F_4 = \\sqrt[16]{x}$, $DF_3 = {\\Bbb R}$, $DF_1 = DF_2 = DF_4 = \\{x \\in {\\Bbb R}: x > 0\\}$; \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_30',
        "content_latex": 'Z daných zobrazení utvořte složená zobrazení $F_1 = f \\circ g$, $F_2 = g \\circ f$, $F_3 = f \\circ f$, $F_4 = g \\circ g$. Určete definiční obory těchto složených zobrazení: $f: y = \\frac{1}{x+2}$, \\quad $g: y = \\sqrt[3]{x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$F_1 = \\frac{1}{\\sqrt[3]{x}+2}$, $F_2 = \\frac{1}{\\sqrt[3]{x+2}}$, $F_3 = \\frac{x+2}{2x+5}$, $F_4 = \\sqrt[9]{x}$, $DF_1 = \\{x \\in {\\Bbb R}: x \\neq -8\\}$, $DF_2 = \\{x \\in {\\Bbb R}: x \\neq -2\\}$, $DF_3 = DF_4 = {\\Bbb R}$. $\\clubsuit$ \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_31',
        "content_latex": 'Určete inverzní zobrazení $f^{-1}$ k daným zobrazením $f$, najděte $Df^{-1}$, $Hf^{-1}$ a dokažte, že platí vztahy $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id:$ $f: y = 5-4x^3$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$f: y = \\sqrt[3]{\\frac{5-x}{4}}$; $Df^{-1} = Hf^{-1} = {\\Bbb R}$, důkaz $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id$ provedeme vytvořením příslušných složených zobrazení (také pro další zobrazení)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_32',
        "content_latex": 'Určete inverzní zobrazení $f^{-1}$ k daným zobrazením $f$, najděte $Df^{-1}$, $Hf^{-1}$ a dokažte, že platí vztahy $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id:$ $f: y = 4- x^2$ pro $x \\geq 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'f: y = \\sqrt{4-x}$; $Df^{-1} = (-\\infty, \\,4\\rangle$, $Hf^{-1} = Df = \\langle 0, \\,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_33',
        "content_latex": 'Určete inverzní zobrazení $f^{-1}$ k daným zobrazením $f$, najděte $Df^{-1}$, $Hf^{-1}$ a dokažte, že platí vztahy $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id:$ $f: y = \\sqrt{2+5x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'f: y = \\frac{x^2-2}{5}$; $Df^{-1} = \\langle 0, \\,\\infty)$, $Hf^{-1} = Df = \\langle -2/5, \\,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_34',
        "content_latex": 'Určete inverzní zobrazení $f^{-1}$ k daným zobrazením $f$, najděte $Df^{-1}$, $Hf^{-1}$ a dokažte, že platí vztahy $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id:$ $f: y = x^2 +x$ pro $x \\geq -1/2$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'f: y = \\frac{-1+\\sqrt{1+4x}}{2}$; $Df^{-1} = \\langle -1/4, \\,\\infty)$, $Hf^{-1} = Df = \\langle -1/2, \\,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_35',
        "content_latex": 'Určete inverzní zobrazení $f^{-1}$ k daným zobrazením $f$, najděte $Df^{-1}$, $Hf^{-1}$ a dokažte, že platí vztahy $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id:$ $f: y = 4+ \\sqrt[3]{x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'f: y = (x-4)^3$; $Df^{-1} = Hf^{-1} = {\\Bbb R}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_36',
        "content_latex": 'Určete inverzní zobrazení $f^{-1}$ k daným zobrazením $f$, najděte $Df^{-1}$, $Hf^{-1}$ a dokažte, že platí vztahy $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id:$ $f: y = (2-x^3)^5$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'f: y = \\sqrt[3]{2-\\sqrt[5]{x}}$; $Df^{-1} = Hf^{-1} = {\\Bbb R}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_37',
        "content_latex": 'Určete inverzní zobrazení $f^{-1}$ k daným zobrazením $f$, najděte $Df^{-1}$, $Hf^{-1}$ a dokažte, že platí vztahy $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id:$ $f: y = \\frac{x^3-1}{x^3+1}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'f: y = \\sqrt[3]{\\frac{1+x}{1-x}}$; $Df^{-1} = {\\Bbb R} - \\{1\\}$, $Hf^{-1} = {\\Bbb R} - \\{-1\\}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_38',
        "content_latex": 'Určete inverzní zobrazení $f^{-1}$ k daným zobrazením $f$, najděte $Df^{-1}$, $Hf^{-1}$ a dokažte, že platí vztahy $f^{-1} \\circ f = id, \\,\\,f \\circ f^{-1} = id:$ $f: y = 1+\\sqrt{1+x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$f: y = x^2-2x$; $Df^{-1} = \\langle 1, \\,\\infty)$, $Hf^{-1} = Df = \\langle -1, \\,\\infty)$. $\\clubsuit$ \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_39',
        "content_latex": 'Určete osu a vrchol $V$ paraboly dané předpisem $y = ax^2+bx+c$: $y = x^2+4x+4$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'osa: $x = -2$, $V[-2, \\,0]$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_40',
        "content_latex": 'Určete osu a vrchol $V$ paraboly dané předpisem $y = ax^2+bx+c$: $y = -x^2+2x$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'osa: $x = 1$, $V[1, \\,1]$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_41',
        "content_latex": 'Určete osu a vrchol $V$ paraboly dané předpisem $y = ax^2+bx+c$: $y = x^2+5x+3$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'osa: $x = -5/2$, $V[-5/2, \\,-13/4]$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_42',
        "content_latex": 'Určete osu a vrchol $V$ paraboly dané předpisem $y = ax^2+bx+c$: $y = x^2+6x+8$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'osa: $x = -3$, $V[-3, \\,-1]$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_43',
        "content_latex": 'Určete osu a vrchol $V$ paraboly dané předpisem $y = ax^2+bx+c$: $y = x^2+8x+6$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'osa: $x = -4$, $V[-4, \\,-10]$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e04_44',
        "content_latex": 'Určete osu a vrchol $V$ paraboly dané předpisem $y = ax^2+bx+c$: $y = x^2+7x+4$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'osa: $x = -7/2$, $V[-7/2, \\,-33/4]$. $\\clubsuit$ \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
]
