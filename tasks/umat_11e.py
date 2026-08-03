"""
Primitivní funkce (extra).

Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/11_prim_fce.tex` (2007-05-29).
Automaticky vyextrahováno scripts/extract_umat_v2.py 2026-08-03.

Rozšířený parser oproti v1: převod textových odpovědí na multiple_choice,
seznamů čísel na N decimal keys, a parsing \\begin{ul}...\\end{ul} bloků
s odpovědí v následujícím `Řešení:` odstavci.
"""

TASKS = [
    {
        "task_id": 'e11_01',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (3x^2+2x-4) \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x^3+x^2-4x+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_02',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int \\left(\\frac{1}{3x^2} - \\frac{1}{5x}\\right) \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '-\\frac{1}{3x} - \\frac{1}{5} \\ln |x|+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_03',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int \\left(\\sqrt{5x^3}- \\frac{1}{\\sqrt{x}}\\right) \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{2\\sqrt{5}x^2\\sqrt{x}}{5} - 2\\sqrt{x}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_04',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int x^2(x^2-2x+2) \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{1}{5}x^5 - \\frac{1}{2}x^4+\\frac{2}{3}x^3+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_05',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (x^2-3x+1)^2 \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{1}{5}x^5- \\frac{3}{2}x^4+\\frac{11}{3}x^3-3x^2+x+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_06',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int x(x-2)(x-3) \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{1}{4}x^4 - \\frac{5}{3}x^3+3x^2+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_07',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int \\frac{x^3-1}{x-1} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{1}{3}x^3+ \\frac{1}{2}x^2+x+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_08',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int \\left(1- \\frac{1}{x}\\right)^2 \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x-2\\ln |x| -1/x+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_09',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int \\frac{(2^x-3^x)^2}{6^x} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{(2^x3^{-x}-3^x2^{-x})}{\\ln 2 - \\ln 3}-2x+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_10',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int e^xa^x \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{e^xa^x}{1+\\ln a}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_11',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (2 \\sin (2+x) - 3 \\cos 5x) \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$-2\\cos (2+x) - 3/5 \\sin 5x+c.$ \\,$\\clubsuit$ \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_12',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (2-x)(2x-1)^2 \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '-x^4+4x^3-9/2x^2+2x+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_13',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (3\\sqrt{x}-7x^{4/3}+10x \\sqrt{x}) \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '2x^{3/2}-3x^{7/3}+4x^{5/2}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_14',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (x^2+2x)x^{1/4} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{4}{13}x^{13/4}+\\frac{8}{9}x^{9/4}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_15',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (\\sqrt{x} - x^{-1/3})^3 \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '2/5x^{5/2}-9/5x^{5/3}+\\frac{18}{5}x^{5/6}- \\ln |x|+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_16',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int \\frac{(x-1)(x^2+3)}{2x^2} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\frac{1}{4}x^2 +\\frac{3}{2} \\ln |x|-\\frac{x}{2}+\\frac{3}{2x}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_17',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int \\frac{(2x+1)^2}{x^4} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '-\\frac{4}{x}-2\\frac{1}{x^2}-\\frac{1}{3x^3}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_18',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int \\frac{1+\\sqrt{x}}{\\sqrt[3]x} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '3/2x^{2/3} + 6/7x^{7/6}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_19',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (x-\\sqrt[3]x)^2 \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '1/3x^{3}- 6/7x^{7/3}+3/5x^{5/3}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_20',
        "content_latex": 'Vypočítejte následující neurčité integrály: $\\int (e^{1-2x} - 2e^{3-x}+e^{x/5}-2^{-x}) \\,dx$ }',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$-1/2e^{1-2x} + 2e^{3-x}+5e^{x/5}+\\frac{2^{-x}}{\\ln 2}+c.$ \\,$\\clubsuit$ \\section{Metody výpočtu neurčitého integrálu: pokračování} \\vspace{2mm} \\subsection{Metoda substituce v neurčitém integrálu} \\vspace{2mm}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_21',
        "content_latex": 'Vypočítejte pomocí vhodné substituce: $\\int 2x\\sqrt{6-2x^2} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '-\\frac{(6-2x^2)^{3/2}}{3}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_22',
        "content_latex": 'Vypočítejte pomocí vhodné substituce: $\\int \\frac{2x+5}{x^2+5x-6} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\ln |x^2+5x-6|+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_23',
        "content_latex": 'Vypočítejte pomocí vhodné substituce: $\\int \\frac{1}{(4x-1)^5} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '-\\frac{1}{16(4x-1)^{4}}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_24',
        "content_latex": 'Vypočítejte pomocí vhodné substituce: $\\int \\frac{5x}{(x-3)^4} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '-\\frac{5}{2(x-3)^{2}} - \\frac{5}{(x-3)^3}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_25',
        "content_latex": 'Vypočítejte pomocí vhodné substituce: $\\int \\frac{3x^2}{1-3x^3} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '-1/3 \\ln |1-3x^3|+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_26',
        "content_latex": 'Vypočítejte pomocí vhodné substituce: $\\int \\frac{2x^4}{x^5+1} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '2/5 \\ln |x^5+1|+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_27',
        "content_latex": 'Vypočítejte pomocí vhodné substituce: $\\int \\frac{2}{x \\ln^3 x} \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '-\\frac{1}{\\ln^2 x}+c', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e11_28',
        "content_latex": 'Vypočítejte pomocí vhodné substituce: $\\int \\cos (1-2x) \\,dx$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$-1/2 \\sin (1-2x) + c.$ \\,$\\clubsuit$ \\subsection{Metoda per partes}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
]
