"""
UMAT — kapitola 09: Derivace funkce.

Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/9_derivace.tex` (skriptum 2007-05-29).
Automaticky vyextrahováno skriptem scripts/extract_umat.py 2026-08-03.

Extrahuje jen \\uloha{content}{result} a \\podul{content}{result}.
Bloky \\begin{ul}{...}\\end{ul} s oddělenou odpovědí v `Řešení:` odstavci
nejsou v tomto exportu — jejich formát vyžaduje ruční extrakci.

Makra rozvinutá: \\zlom → \\frac, \\lz/\\pz → \\langle/\\rangle,
\\tg/\\cotg/\\arctg → \\tan/\\cot/\\arctan.
"""

TASKS = [
    {
        "task_id": 'umat_09_01',
        "content_latex": '$f(x)=2x^{2} -x+5, \\,\\,x_{0}=3$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 11.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_02',
        "content_latex": '$f(x)=x^{2}-4x, \\,\\,x_{0}=1$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": -2.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_03',
        "content_latex": '$f(x)=\\sin x, \\,\\,x_{0}=0$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 1.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_04',
        "content_latex": '$f(x)=\\frac{1}{x}, \\,\\,x_{0}=4$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '-\\frac{1}{16}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_05',
        "content_latex": '$f(x)=\\sqrt x, \\,\\,x_{0}=1$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1}{2}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_06',
        "content_latex": '$y=4x^{2}-x+1$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=8x-1", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_07',
        "content_latex": '$y=2\\sin x + 3\\cos x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=2\\cos x-3\\sin x", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_08',
        "content_latex": '$y=\\sqrt x+x^{-2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{1}{2\\sqrt x}-2x^{-3}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_09',
        "content_latex": '$y=6\\sqrt[3]x-5$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=2\\sqrt[3]{x^{-2}}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_10',
        "content_latex": '$y=3\\ln x -9\\log x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{3}{x}-\\frac{9}{x\\ln 10}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_11',
        "content_latex": '$y=\\tan x+11\\cot x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{1}{\\cos^{2}x}-\\frac{11}{sin^{2}x}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_12',
        "content_latex": '$y=3^{x}+2e^{x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=3^{x}\\cdot \\ln 3+2e^{x}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_13',
        "content_latex": '$y=\\frac{(x^{2}+2)^{2}}{4}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=x^{3}+2x", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_14',
        "content_latex": '$y=\\frac{\\sqrt x \\cdot (\\sqrt[3] {x} -5\\sqrt x)}{x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=-\\frac{1}{6\\cdot \\sqrt[6]{x^{7}}}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_15',
        "content_latex": '$y=(x^{2}+1)\\cdot \\sin x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=2x\\cdot \\sin x+(x^{2}+1)\\cdot \\cos x", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_16',
        "content_latex": '$y=e^{x}\\cdot \\ln x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=e^{x}\\cdot\\ln x+\\frac{e^{x}}{x}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_17',
        "content_latex": '$y=\\frac{2x-1}{x+3}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{7}{(x+3)^{2}}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_18',
        "content_latex": '$y=\\frac{\\sin x+\\cos x}{\\sin x-\\cos x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{-2}{1-\\sin2x}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_19',
        "content_latex": '$y=\\frac{x^{2}+2x}{1-x^{3}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{x^{4}+4x^{3}+2x+2}{(1-x^{3})^{2}}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_20',
        "content_latex": '$y=\\frac{e^{x}\\cdot \\ln x}{x+1}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{1}{(x+1)^{2}}\\cdot (e^{x}\\cdot x\\cdot \\ln x+e^{x}+\\frac{e^{x}}{x})", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_21',
        "content_latex": '$y=(x^{2}+1)^{2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=4x\\cdot(x^{2}+1)", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_22',
        "content_latex": '$y=(\\sqrt{2x^{3}-1}+2)^{8}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{24x^{2}\\cdot(\\sqrt{2x^{3}-1}+2)^{7}}{\\sqrt{2x^{3}-1}}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_23',
        "content_latex": '$y=\\cos (2x+4)$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=-2\\sin (2x+1)", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_24',
        "content_latex": '$y=\\sqrt {\\cos 2x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=-\\frac{\\sin 2x}{\\sqrt {\\cos 2x}}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_25',
        "content_latex": '$y=\\frac{1}{\\cos 2x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{2\\sin 2x}{\\cos^{2}2x}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_26',
        "content_latex": '$y=\\sin^{2}x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\sin 2x", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_27',
        "content_latex": '$y=\\sin x^{2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=2x\\cdot\\cos x^{2}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_28',
        "content_latex": '$y=\\sqrt[3]{\\cos2x + 2x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{2-2\\sin 2x}{3\\cdot \\sqrt[3]{(\\cos 2x + 2x)^{2}}}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_29',
        "content_latex": '$y=\\tan (3x-\\frac{\\pi}{4})$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{3}{\\cos^{2}(3x-\\frac{\\pi}{4})}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_30',
        "content_latex": '$y=\\ln (\\cos (x^{3}-2x+1))$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_31',
        "content_latex": '$y=\\sqrt{x+\\sqrt {5x}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{2\\cdot\\sqrt {5x} +5}{4\\cdot\\sqrt{5x^{2}+5x\\cdot\\sqrt {5x}}}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_32',
        "content_latex": '$y=\\ln (3\\sin x-8)$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": "y'=\\frac{3\\cos x}{3\\sin x-8}", "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_33',
        "content_latex": '$y=2x^{4}+8x$, \\,\\,$T[-1, \\,?]$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 't:y=-6', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_34',
        "content_latex": '$y=2\\sin x $, \\,\\,$T[0, \\,?]$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 't:y=2x', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_35',
        "content_latex": '$y=\\frac{1+x^{3}}{x-1}$, \\,\\,$T[2, \\,?]$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 't:y=3x+3', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_36',
        "content_latex": 'tečna v bodě $T$ měla směrnici $k_{t}=1$;',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'T[1, \\,0]', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_37',
        "content_latex": 'tečna v bodě $T$ byla rovnoběžná s přímkou\\\\ \\> \\> $p:y=2x+3$;',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'T[e, \\,e]', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_38',
        "content_latex": 'tečna v bodě $T$ svírala s osou $o_{x}$ úhel $\\alpha=135^{o}$;',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'T[e^{-2}, \\,-2e^{-2}]', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_09_39',
        "content_latex": 'tečna v bodě $T$ byla kolmá k přímce $r:y=6-2x$.',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'T[\\frac{1}{\\sqrt{e}}, \\, -\\frac{1}{2\\sqrt e}]', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
]
