"""
Rovnice a nerovnice (extra).

Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/3_rovnice.tex` (2007-05-29).
Automaticky vyextrahováno scripts/extract_umat_v2.py 2026-08-03.

Rozšířený parser oproti v1: převod textových odpovědí na multiple_choice,
seznamů čísel na N decimal keys, a parsing \\begin{ul}...\\end{ul} bloků
s odpovědí v následujícím `Řešení:` odstavci.
"""

TASKS = [
    {
        "task_id": 'e03_01',
        "content_latex": 'Řešte následující rovnice: $3x-1=7x+7$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x=-2', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_02',
        "content_latex": 'Řešte následující rovnice: $\\frac{x-2}{x}=\\frac{x-1}{x-1}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x \\in \\emptyset', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_03',
        "content_latex": 'Řešte následující rovnice: $ \\frac{x+3}{x}+\\frac{x+1}{x-3}=\\frac{2x-1}{x}$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x=\\frac{3}{2}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_04',
        "content_latex": 'Řešte následující rovnice: $x^3-4x=0$ e $x^2-6x+9=0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x_1=0, x_2=2,x_3=-2', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_05',
        "content_latex": 'Řešte následující rovnice: $x^2-7x+10=0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x=3', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_06',
        "content_latex": 'Řešte následující rovnice: $x^2-x-6=0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x_1=2$,\\\\ $x_2=5', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_07',
        "content_latex": 'Řešte následující rovnice: $x^2+4x-21=0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x_1=-2,x_2=3', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_08',
        "content_latex": 'Řešte následující rovnice: $x^2+2x+11=0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x_1=-7,x_2=3', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_09',
        "content_latex": 'Řešte následující rovnice: $x^2+x-7=0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in\\emptyset', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_10',
        "content_latex": 'Řešte následující rovnice: $x^2+10x-1=0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$x_1=\\frac{-1-\\sqrt{29}}{2},\\ x_2=\\frac{-1+\\sqrt{29}}{2}$,\\\\', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_11',
        "content_latex": 'Řešte následující rovnice: $ x^2+4x+1=0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x_1=-5-\\sqrt{26},\\ x_2=-5+\\sqrt{26}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_12',
        "content_latex": 'Řešte následující nerovnice: $x-7<3x-2$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-5/2,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_13',
        "content_latex": 'Řešte následující nerovnice: $x^2>5x-6$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-\\infty,2)\\cup(3,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_14',
        "content_latex": 'Řešte následující nerovnice: $x^2-x-30<0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-5,6)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_15',
        "content_latex": 'Řešte následující nerovnice: $ x^2-18x+81>0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$x\\in(-\\infty,9)\\cup(9,\\infty)$, \\\\', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_16',
        "content_latex": 'Řešte následující nerovnice: $x^2+4x+4\\leq 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$x=-2$,\\', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_17',
        "content_latex": 'Řešte následující nerovnice: $3x^2-x-3<0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in\\left(\\frac{1-\\sqrt{37}}{6}, \\frac{1+\\sqrt{37} }{6}\\right)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_18',
        "content_latex": 'Řešte následující nerovnice: $2x^2+16>0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in\\R', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_19',
        "content_latex": 'Řešte následující nerovnice: $ x^2+4x-12>0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-\\infty,-6)\\cup(2,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_20',
        "content_latex": 'Řešte následující nerovnice: $-2x^2+7x\\geq 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in\\langle0,7/2\\rangle', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_21',
        "content_latex": 'Řešte následující nerovnice: $-2x^2-2x-6>0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$x\\in\\emptyset$, \\\\', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_22',
        "content_latex": 'Řešte následující nerovnice: $ 2x^2-\\sqrt{12}\\geq 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-\\infty,-\\sqrt[4]{3}\\rangle\\cup \\langle\\sqrt[4]{3},\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_23',
        "content_latex": 'Řešte následující nerovnice: $ x^2+16<0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in \\emptyset', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_24',
        "content_latex": 'Řešte následující nerovnice: $(x+7)(x-2)x<0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in (-\\infty,-7)\\cup(0,2)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_25',
        "content_latex": 'Řešte následující nerovnice: $\\frac{(x-1)(2x+3)}{x+7}\\geq 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-7,-3/2\\rangle\\cup\\langle1,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_26',
        "content_latex": 'Řešte následující nerovnice: $\\frac{(3-x)(x-2)}{x}\\leq 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$x\\in(0,2\\rangle\\cup\\langle3,\\infty)$, \\\\', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_27',
        "content_latex": 'Řešte následující nerovnice: $(x^2-4)(x^2-x)<0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-2,0)\\cup(1,2)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_28',
        "content_latex": 'Řešte následující nerovnice: $(x+3)^2(x+5)>0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in\\langle -5,-3)\\cup(-3,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_29',
        "content_latex": 'Řešte následující nerovnice: $x^2(x-2)^2>0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-\\infty,0)\\cup(0,2)\\cup(2,\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_30',
        "content_latex": 'Řešte následující nerovnice: $(x-1)x^3\\leq 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$x\\in\\langle0,1\\rangle$, \\\\', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_31',
        "content_latex": 'Řešte následující nerovnice: $ (x-3)^{16}(x+2)^{17}> 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-2,3)\\cup(3,+\\infty)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_32',
        "content_latex": 'Řešte následující nerovnice: $(x^2-7x+10)(x^2-x-12)<0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-3,2)\\cup(4,5)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_33',
        "content_latex": 'Řešte následující nerovnice: $(x^2-2x)(x^2-4)\\leq 0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in\\langle-2,0\\rangle\\cup\\{2\\}', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_34',
        "content_latex": 'Řešte následující nerovnice: $(x^2-5)(x+\\sqrt{3})>0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$x\\in(-\\sqrt{5},-\\sqrt{3})\\cup(\\sqrt{5},\\infty)$, \\\\', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e03_35',
        "content_latex": 'Řešte následující nerovnice: $x^3-x^2\\leq 0$ m) $(x^2+x+1)(x^2-20)>0$ n) $\\frac{x^2-4}{x^2+2x}\\geq0$ o) $ \\frac{x^2+1}{1-x^2}\\geq 0$ p) $\\frac{2-x^2}{x^2+x+1}\\geq 0$ q) $\\frac{x^2-x}{x-3}\\geq x$ r) $ \\frac{x^5-4x^4}{2x^4-x^3}\\geq 1$ s) $\\frac{1-x^2}{(-x^2-4)^3}\\geq 0$ t) $(x^3-1)(x^2+1)<0$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in(-\\infty,1\\rangle$, m) $x\\in(-\\infty,-2\\sqrt{5})\\cup(2\\sqrt{5},\\infty)$, n) $x\\in(-\\infty,-2)\\cup(-2,0)\\cup(2,\\infty)$, o) $x\\in(-1,1)$, \\\\ p) $x\\in\\langle-\\sqrt{2},\\sqrt{2}\\rangle$, q) $x\\in(-\\infty,0\\rangle\\cup(3,\\infty)$, r) $x\\in(-\\infty,0)\\cup\\langle 3-2\\sqrt{2},1/2)\\cup \\langle 3+2\\sqrt{2},\\infty))$, \\\\ s) $x\\in \\langle-1,1\\rangle$, t) $x\\in(-\\infty,1)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
]
