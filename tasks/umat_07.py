"""
UMAT — kapitola 07: Posloupnosti.

Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/7_posloupnosti.tex` (skriptum 2007-05-29).
Automaticky vyextrahováno skriptem scripts/extract_umat.py 2026-08-03.

Extrahuje jen \\uloha{content}{result} a \\podul{content}{result}.
Bloky \\begin{ul}{...}\\end{ul} s oddělenou odpovědí v `Řešení:` odstavci
nejsou v tomto exportu — jejich formát vyžaduje ruční extrakci.

Makra rozvinutá: \\zlom → \\frac, \\lz/\\pz → \\langle/\\rangle,
\\tg/\\cotg/\\arctg → \\tan/\\cot/\\arctan.
"""

TASKS = [
    {
        "task_id": 'umat_07_01',
        "content_latex": 'Tři za sebou následující členy GP mají součet 49/2 a součin 343. Určete tato čísla.',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '7/2, 7, 14', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_02',
        "content_latex": 'První tři členy GP jsou $k-3, 2k-4, 4k-3$ v tomto pořadí. Určete hodnotu $k$ a součet prvních osmi členů této posloupnosti.',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'k=7,$ $s_8=4066,3467', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_03',
        "content_latex": 'V jisté AP je součet prvního a pátého členu 18 a pátý člen je o 6 větší než třetí člen. Určete součet prvních deseti členů.',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 165.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_04',
        "content_latex": 'V aritmetické posloupnosti \\an \\; je $a_2+a_3=9, a_2 \\cdot a_3=14.$ Určete $a_{10}.$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'a_{10}=-33$ nebo $a_{10}=42', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_05',
        "content_latex": 'Součet čtyř po sobě jdoucích členů geometrické posloupnosti je 80. Určete je, jestliže víte, že poslední je devětkrát větší než druhý.',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '2, 6, 18, 54$ nebo $-4, 12, -36, 108', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_06',
        "content_latex": 'Určete součet všech přirozených čísel, která vyhovují nerovnici $$(12x+\\frac{2}{3}) \\cdot 5-\\frac{5x-15}{3}< 50(x+10).$$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 's_{58}=1682', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_07',
        "content_latex": 'Vypočítejte součet všech přirozených dvojciferných čísel.',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 's=4905', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_08',
        "content_latex": '$a_4=0, a_6=-4, s_n=12,$ určete $n$.',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'n=3 \\lor n=4', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_09',
        "content_latex": '$a_1+a_4=26, a_2+a_5=30,$ určete $s_{10}.$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 's_{10}=190', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_10',
        "content_latex": 'aritmetické posloupnosti,',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '2;\\, 3,2;\\, \\dots;\\, 8$ nebo $8;\\, 6,8;\\, \\dots ;\\,2', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_11',
        "content_latex": 'geometrické posloupnosti.',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '2, 2\\sqrt[5]{4}, \\dots, 8$ nebo $8, 4\\sqrt[5]{4}, \\dots, 2', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_12',
        "content_latex": '$a_2= 16, a_4=1,$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'a_1=64, q=\\frac{1}{4}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_13',
        "content_latex": '$a_8-a_4=360, a_7-a_5=144$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'a_1=3, q=2 \\lor a_1=-3072, q=\\frac{1}{2}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_14',
        "content_latex": '$a_1-a_2+a_3=15, a_4-a_5+a_6=120$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": 'a_1=5, q=2', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_15',
        "content_latex": '$\\lim\\limits_{n \\to \\infty} \\frac{(n+1)}{n}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 1.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_16',
        "content_latex": '$\\lim\\limits_{n \\to \\infty} \\frac{(n+1)^{2}}{2n^{2}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1}{2}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_17',
        "content_latex": '$\\lim\\limits_{n \\to \\infty} \\frac{2n^{2}-3n+1}{3n^{2}-5}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{2}{3}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_18',
        "content_latex": '$\\lim\\limits_{n \\to \\infty} \\frac{3n^{2}+1}{n^{4}+1}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 0.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_19',
        "content_latex": '$\\lim\\limits_{n \\to \\infty} \\frac{1000n^{4}+1}{n^{4}+2n^{2}+3}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 1000.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_20',
        "content_latex": '$\\lim\\limits_{n \\to \\infty}\\frac{(n+1)^3-(n-1)^3}{(n+1)^2+(n-1)^2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 3.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_21',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty}\\frac{(n+2)^{2}+(3n-1)^{3}}{(n+1)^{2}-(2n+3)^{3}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '-\\frac{7}{8}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_22',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty}\\left(\\frac{n^{3}+1}{2n^3+14n-100}\\right)^{3}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1}{8}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_23',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty}\\left(\\frac{3n^{4}-n^{3}+166}{6n^{4}+2n-77}\\right)^{-2}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 4.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_24',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty}\\frac{(2n+1)^{4}-(n-1)^{4}}{(2n+1)^{4}+(n-1)^{4}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{15}{17}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_25',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\frac{n!}{(n+1)!-n!}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 0.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_26',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\frac{(n+2)!+(n+1)!}{(n+2)!-(n+1)!}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 1.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_27',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\frac{(n+2)!+(n+1)!}{(n+3)!}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 0.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_28',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\frac{(2n+1)!+(2n-1)!}{(2n+1)!-(2n-1)!}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 1.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_29',
        "content_latex": '$\\lim\\limits_{n \\to \\infty} \\frac{3^{-n}}{1+3^{-n}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 0.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_30',
        "content_latex": '$\\lim\\limits_{n \\to \\infty}\\frac{2^n-1}{2^n+1}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 1.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_31',
        "content_latex": '$\\lim\\limits_{n \\to \\infty}\\frac{2^{n+1}+4^{n+1}}{2^n+4^n}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 4.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_32',
        "content_latex": '$\\lim\\limits_{n \\to \\infty}\\frac{(-2)^n+3^n}{(-2)^{n+1}+3^{n+1}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1}{3}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_33',
        "content_latex": '$\\lim\\limits_{n \\to \\infty}\\frac{2^{\\frac{1}{n}}-1}{2^\\frac{1}{n}+1}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 0.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_34',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\frac{\\sqrt{n^{2}+1}}{n}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 1.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_35',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\frac{1}{\\sqrt{n^{2}+1}-\\sqrt{n}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 0.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_36',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\frac{1}{n-\\sqrt{n^2-n}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "decimal", "expected": 2.0, "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_37',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\sqrt{n}(\\sqrt{n+1}-\\sqrt{n})$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1}{2}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_38',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty}\\left(\\frac{1+2+\\ldots +n}{n+2}-\\frac{n}{2}\\right)$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '-\\frac{1}{2}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_39',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\left(\\frac{1}{n^2}+\\frac{2}{n^2}+ \\ldots + \\frac{n-1}{n^2}\\right)$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{1}{2}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_40',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\left( -\\frac{1}{10} + \\frac{1}{100} + \\ldots + \\frac{1}{(-10)^{n}}\\right)$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '-\\frac{1}{11}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'umat_07_41',
        "content_latex": '$\\lim\\limits_{n \\rightarrow \\infty} \\frac{1+\\frac{1}{2}+ \\ldots + \\frac{1}{2^{n}}} {1+\\frac{1}{3}+ \\ldots + \\frac{1}{3^{n}}}$',
        "results": [{"key": "vysledek", "label_latex": "= ", "type": "mathlive", "expected": '\\frac{4}{3}', "tolerance": 0.0}],
        "cognitive_load": 'C',
    },
]
