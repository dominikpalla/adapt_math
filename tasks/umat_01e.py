"""
Logika (extra).

Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/1_logika.tex` (2007-05-29).
Automaticky vyextrahováno scripts/extract_umat_v2.py 2026-08-03.

Rozšířený parser oproti v1: převod textových odpovědí na multiple_choice,
seznamů čísel na N decimal keys, a parsing \\begin{ul}...\\end{ul} bloků
s odpovědí v následujícím `Řešení:` odstavci.
"""

TASKS = [
    {
        "task_id": 'e01_01',
        "content_latex": 'Tři politické strany na magistrátu města se rozhodují o investicích. Strany zastávají následující stanoviska: \\begin{itemize} \\item {\\it strana A:} Jestliže se postaví silnice, pak se musí postavit nemocnice. \\item {\\it strana B:} Postaví se nemocnice a ne továrna. \\item {\\it strana C:} Postaví se továrna a silnice. \\end{itemize}Určete, zda se při takovýchto stanoviscích mohou shodnout a v případě, že ano, jaké investice proběhnou.',
        "results": [{'type': 'multiple_choice', 'expected': 'b', 'options': [{'key': 'a', 'label_latex': 'shodnou se'}, {'key': 'b', 'label_latex': 'neshodnou se'}], 'key': 'vysledek', 'label_latex': ''}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_02',
        "content_latex": 'Mějme pravdivý výrok "Jestliže A podpoří B, pak B nepodpoří C". Nastala situace, ve které B nepodpořil C. Lze z toho usuzovat, že A podpořil B?',
        "results": [{'type': 'multiple_choice', 'expected': 'b', 'options': [{'key': 'a', 'label_latex': 'ano'}, {'key': 'b', 'label_latex': 'ne'}], 'key': 'vysledek', 'label_latex': ''}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_03',
        "content_latex": 'Nechť platí: $x>4\\Ra |x-3|>1$. Víme, že $|x-3|=1.99$. Můžeme z toho usoudit, že $x>4$?',
        "results": [{'type': 'multiple_choice', 'expected': 'b', 'options': [{'key': 'a', 'label_latex': 'ano'}, {'key': 'b', 'label_latex': 'ne'}], 'key': 'vysledek', 'label_latex': ''}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_04',
        "content_latex": 'Platí: $|x+1|<1\\Ra x^2<4$. Víme, že $x^2=5,6$. Můžeme z toho usoudit, že $|x+1|\\geq 1$?',
        "results": [{'type': 'multiple_choice', 'expected': 'a', 'options': [{'key': 'a', 'label_latex': 'ano'}, {'key': 'b', 'label_latex': 'ne'}], 'key': 'vysledek', 'label_latex': ''}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_05',
        "content_latex": '$x$ leží v množině $A$ a současně v množině $B$.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '(x\\in A)\\wedge (x\\in B)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_06',
        "content_latex": '$x$ leží v $A$ a v $B$ ale neleží v $C$.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '(x\\in A \\wedge x\\in B)\\wedge x \\not \\in C', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_07',
        "content_latex": 'Jestliže je $x>0$, pak číslo $x$ leží v $A$.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x>0\\Ra x \\in A', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_08',
        "content_latex": 'Pro každé reálné číslo $x$ platí, že $x^2$ je kladné.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\forall x\\in \\R:\\quad x^2>0', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_09',
        "content_latex": 'Pro každé reálné číslo $x$ existuje přirozené číslo $y$ \\\\ \\> \\> takové, že $x+y>1000$.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\forall x\\in \\R\\ \\exists y\\in \\N:\\quad x+y>1000', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_10',
        "content_latex": 'Existuje reálné číslo $a$ takové, že pro všechna $x$ větší než $a$\\\\ \\> \\> platí, že $x^2+10$ je menší než $6x+5$.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '\\exists a\\in \\R\\ \\forall x>a:\\quad x^2+10<6x+5', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_11',
        "content_latex": 'Na oslavu přijde Karel nebo Eliška.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Na oslavu nepřijde ni Karel ani Eliška.', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_12',
        "content_latex": 'Když máme chuť, jdeme na pivo.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Máme chuť a nejdeme na pivo.', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_13',
        "content_latex": 'Každý Edudand má (alespoň) jednoho Francimora.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Existuje Edudand, který nemá Francimora.', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_14',
        "content_latex": '$\\forall x>0:\\quad x^2-x<x^3$.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$\\exists x>0:\\quad x^2-x\\geq x^3$.', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_15',
        "content_latex": 'Každé tři body v rovině leží na jedné přímce.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'Existují tři body v rovině které neleží na jedné přímce.', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_16',
        "content_latex": '$\\forall x>0\\exists y\\geq x:\\quad x^2y-y^2x=0$.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$\\exists x>0\\ \\forall y\\geq x:\\quad x^2y-xy^2\\not = 0$.', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_17',
        "content_latex": '$x\\geq 0 \\wedge x<5$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in \\langle 0, 5)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_18',
        "content_latex": '$(x\\geq 0 \\wedge x<5)\\vee x<-5$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in (-\\infty,-5)\\cup \\langle 0, 5)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_19',
        "content_latex": '$(x\\geq 0 \\wedge x<5)\\vee x<3$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in (-\\infty,5)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_20',
        "content_latex": '$(x\\geq 0 \\wedge x<5)\\wedge x>1$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in (1,5)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_21',
        "content_latex": '$(x\\geq 0 \\wedge x<5)\\vee (x\\leq 3\\wedge x\\geq -1)$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in \\langle -1, 5)', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_22',
        "content_latex": '$(x\\geq 0 \\wedge x<5)\\wedge (x\\leq 3\\wedge x\\geq -1)$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x\\in \\langle 0,3\\rangle', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_23',
        "content_latex": '$(x\\in A\\wedge x\\not \\in B)\\vee x\\in C$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '(A\\cap\\overline{B})\\cup C,\\quad \\langle -3,-2)\\cup\\langle -1,17 \\rangle', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_24',
        "content_latex": '$x\\in A\\wedge (x\\not \\in B \\vee x \\in C)$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'A\\cap (\\overline{B}\\cup C),\\quad \\langle-3,-2)\\cup \\langle-1,0\\rangle', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e01_25',
        "content_latex": '$x\\in C \\wedge (x\\not \\in B \\vee x \\not \\in A)$',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'C\\cap(\\overline{A}\\cup \\overline{B}),\\quad (0,17\\rangle', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
]
