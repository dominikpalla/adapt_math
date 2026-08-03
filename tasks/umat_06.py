"""
UMAT — kapitola 06: Goniometrické rovnice a nerovnice.

Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/6_gon_rce_nrce.tex` (skriptum 2007-05-29).
Automaticky vyextrahováno skriptem scripts/extract_umat.py 2026-08-03.

Extrahuje jen \\uloha{content}{result} a \\podul{content}{result}.
Bloky \\begin{ul}{...}\\end{ul} s oddělenou odpovědí v `Řešení:` odstavci
nejsou v tomto exportu — jejich formát vyžaduje ruční extrakci.

Makra rozvinutá: \\zlom → \\frac, \\lz/\\pz → \\langle/\\rangle,
\\tg/\\cotg/\\arctg → \\tan/\\cot/\\arctan.
"""

TASKS = [
    {
        "task_id": 'umat_06_01',
        "content_latex": '$\\sin\\left( \\frac{\\pi}{6} +x\\right)+\\sin\\left( \\frac{\\pi}{6}-x\\right)$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\cos x', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_02',
        "content_latex": '$\\frac{1-\\cos^{2}x}{1+\\tan^{2}x} -\\frac{\\cos^{2}x}{1+\\cot^{2}x}+ \\frac{1}{\\cos^{2}x}-1$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\tan^2 x', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_03',
        "content_latex": '$\\frac{1-\\tan^{2}x}{\\cos 2x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1}{\\cos^2 x}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_04',
        "content_latex": '$\\frac{\\sin^{2}x}{1+\\cos x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '{$1-\\cos x$}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_05',
        "content_latex": '$\\frac{2 \\sin x - \\sin 2x}{2 \\sin x + \\sin 2x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1-\\cos x}{1+\\cos x}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_06',
        "content_latex": '$\\frac{(\\sin x + \\cos x)^{2}}{1+\\sin 2x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 1.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_07',
        "content_latex": '$\\frac{\\cos 2x + \\sin^2 x}{1 + \\cos 2x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1}{2}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_08',
        "content_latex": '$\\frac{2\\sin^2x - \\sin 2x}{2\\cos^2 x - \\sin 2x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '-\\tanx', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_09',
        "content_latex": '$ \\sin(2x-\\frac{\\pi}{4})=-\\frac{1}{2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{17}{24}\\pi+k\\pi, \\frac{25}{24}\\pi +k \\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_10',
        "content_latex": '$2\\sin(\\frac{x}{3}+\\frac{\\pi}{6})=\\sqrt{3}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{2}\\pi+6k\\pi, \\frac{3}{2}\\pi+6k \\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_11',
        "content_latex": '$\\cos(4x+\\frac{\\pi}{2})=\\frac{\\sqrt{3}}{2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ -\\frac{1}{12}\\pi+k\\frac{1}{2}\\pi, \\frac{1}{3}\\pi + k \\frac{1}{2}\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_12',
        "content_latex": '$\\tan(2x-\\frac{\\pi}{6})=\\sqrt{3}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{4}\\pi+k\\frac{1}{2}\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_13',
        "content_latex": '$\\frac{1}{\\sqrt{3}}\\cot(\\frac{x}{3}-\\frac{\\pi}{6})=-\\frac{\\sqrt{3}}{3}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{11}{4}\\pi+3k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_14',
        "content_latex": '$2\\sin^{2}x=\\sqrt{2} \\sin x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ k \\pi, \\frac{1}{4}\\pi+2k\\pi, \\frac{3}{4}\\pi +2k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_15',
        "content_latex": '$2\\cos^{2}x=-\\sqrt{2}\\cos x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{2}\\pi+k \\pi, \\frac{3}{4}\\pi+2k\\pi, \\frac{5}{4}\\pi +2k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_16',
        "content_latex": '$ \\tan^{2}x=-\\tanx$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ k \\pi, \\frac{3}{4} \\pi+ k \\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_17',
        "content_latex": '$\\sqrt{3}\\tan^{2}x+2\\tanx-\\sqrt{3}=0$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{6}\\pi+k\\pi, \\frac{2}{3}\\pi + k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_18',
        "content_latex": '$3\\tan^{2}x+4\\sqrt{3}\\tanx+3=0$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{2}{3}\\pi+k\\pi, \\frac{5}{6}\\pi+k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_19',
        "content_latex": '$ 2-2\\cos^{2}x-\\sqrt{3} \\sin x =0$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ k\\pi, \\frac{1}{3}\\pi+2k\\pi, \\frac{2}{3}\\pi + 2k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_20',
        "content_latex": '$\\sin 2x -\\cos x =0$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{2}\\pi+k\\pi, \\frac{1}{6}\\pi+2k\\pi, \\frac{5}{6}\\pi + 2k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_21',
        "content_latex": '$2\\cos^{2} x+4\\sin^{2} x =3$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{4}\\pi+k\\pi, \\frac{3}{4}\\pi+k\\pi, \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_22',
        "content_latex": '$\\sin 4x= \\sqrt{2} \\cos 2x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{4}\\pi+k\\frac{\\pi}{2}, \\frac{1}{8}\\pi+k\\pi, \\frac{3}{8}\\pi+k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_23',
        "content_latex": '$\\sin 2x=(\\cos x - \\sin x)^{2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{12}\\pi+k\\pi, \\frac{5}{12}\\pi+k\\pi, \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_24',
        "content_latex": '$\\sin^{2} x + \\sin^{2} 2x =1$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{2}\\pi+k\\pi, \\frac{1}{6}\\pi+k\\pi, \\frac{5}{6}\\pi+k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_25',
        "content_latex": '$\\sin^{4} x - \\cos^{4} x = \\frac{1}{2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{3}\\pi+k\\pi, \\frac{2}{3}\\pi+k\\pi, \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_26',
        "content_latex": '$\\cot^{2} x +(\\sqrt{3}-1)\\cot x =\\sqrt{3}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{4}\\pi+k\\pi, \\frac{5}{6}\\pi+k\\pi, \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_27',
        "content_latex": '$3^{4 \\sin^{2} x}=27$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{3}\\pi+k\\pi, \\frac{2}{3}\\pi+k\\pi, \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_28',
        "content_latex": '$\\cos 2x -\\cos x= \\sin x - \\sin 2x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ 2k\\pi, \\frac{1}{6}\\pi+\\frac{2}{3}k\\pi, \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_29',
        "content_latex": '$ 2\\sin^{2} x +\\sin^{2} 2x =2$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{2}\\pi+k\\pi, \\, \\frac{1}{6}\\pi+k\\pi, \\, \\frac{5}{6}\\pi+k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_30',
        "content_latex": '$\\sin x +\\cos x = 1 +\\sin 2x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{3}{4}\\pi+k\\pi, \\frac{1}{2}\\pi+2k\\pi,2k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_31',
        "content_latex": '$\\sin 3x= \\sin 2x - \\sin x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ k\\frac{\\pi}{2}, \\frac{1}{3}\\pi+2k\\pi, \\frac{5}{3}\\pi+2k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_32',
        "content_latex": '$\\frac{\\sqrt{3}}{\\cos^{2}x}-4\\tanx=0$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left \\{ \\frac{1}{6}\\pi+k\\pi, \\frac{1}{3}\\pi+k\\pi \\right \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_33',
        "content_latex": '$ \\sin(x+\\pi) \\le -\\frac{\\sqrt{3}}{2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left ( \\frac{1}{3} \\pi + 2k\\pi, \\frac{2}{3} \\pi+2k\\pi \\right )', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_34',
        "content_latex": '$ \\cos(x-2) < -\\frac{\\sqrt{3}}{2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left ( \\frac{5}{6}\\pi+2(1+k\\pi), \\frac{7}{6}\\pi+2(1+k\\pi) \\right )', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_35',
        "content_latex": '$ \\tan(2x-1)<1$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left ( -\\frac{1}{4}\\pi+\\frac{1}{2}(1+k\\pi), \\frac{1}{8}\\pi+\\frac{1}{2}(1+k\\pi) \\right )', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_36',
        "content_latex": '$ \\tan3x<-1$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left (-\\frac{1}{6}\\pi+\\frac{1}{3}k\\pi, -\\frac{1}{12}\\pi+\\frac{1}{3}k\\pi \\right)', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_37',
        "content_latex": '$ \\sin x +\\cos 2x >1$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left ( 2k\\pi,\\frac{1}{6}\\pi+2k\\pi \\right ) \\cup \\left( \\frac{5}{6}\\pi + 2k\\pi, \\pi+ 2k\\pi \\right)', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_38',
        "content_latex": '$ \\cos x \\le \\frac{1}{\\cos x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left (-\\frac{1}{2}\\pi+2k\\pi, \\frac{1}{2}\\pi+2k\\pi \\right) \\cup \\{\\pi+2k\\pi \\}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_39',
        "content_latex": '$ \\sin x > \\frac{1}{ \\sin x}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in \\Bbb Z} (\\pi+2k\\pi, 2\\pi+2k\\pi)', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_40',
        "content_latex": '$ 2\\sin^{2}x -7 \\sin x >-3$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in \\Bbb Z}(\\frac{5}{6}\\pi+2k\\pi, \\frac{13}{6}\\pi+2k\\pi)', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_41',
        "content_latex": '$ \\cos(\\sin x)<0$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\O', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_42',
        "content_latex": '$ 2 \\cos^{2} x > 3 \\sin x$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in \\Bbb Z} (\\frac{5}{6}\\pi+2k\\pi, \\frac{13}{6}\\pi+2k\\pi)', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_06_43',
        "content_latex": '$ 2 \\sin^{2} x + 7 \\cos x -5<0$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\bigcup_{k \\in {\\mathbf Z}} \\left ( \\frac{1}{3} \\pi + 2k\\pi, \\frac{5}{3} \\pi+2k\\pi \\right )', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
]
