"""
Optimalizace (extra).

Zdroj: `~/Downloads/skriptum_2007_05_29_finalni/texty/10_optimalizace.tex` (2007-05-29).
Automaticky vyextrahováno scripts/extract_umat_v2.py 2026-08-03.

Rozšířený parser oproti v1: převod textových odpovědí na multiple_choice,
seznamů čísel na N decimal keys, a parsing \\begin{ul}...\\end{ul} bloků
s odpovědí v následujícím `Řešení:` odstavci.
"""

TASKS = [
    {
        "task_id": 'e10_01',
        "content_latex": 'Najděte takové kladné číslo, aby součet tohoto čísla a jeho převrácené hodnoty byl minimální.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x=1', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e10_02',
        "content_latex": 'Určete rozměry $a$, $b$ obdélníku tak, aby při daném obsahu $16 \\,cm^{2}$ měl minimální obvod.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'čtverec se stranou $a=4 cm$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e10_03',
        "content_latex": 'Tvrdý papír obdelníkového tvaru má rozměry $60 \\,cm$ a $28 \\,cm$. V rozích se vystřihnou stejné čtverce a zbytek se ohne do tvaru otevřené krabice. Jak dlouhá musí být strana $x$ odstřižených čtverců, aby objem krabice byl maximální?',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x=12 \\,cm', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e10_04',
        "content_latex": 'Obchod prodává skateboardy za 40 dolarů za kus a při této ceně prodá měsíčně 50 skateboardů. Majitel obchodu chce zvýšit cenu a očekává, že každý dolar zvýšení ceny přinese snížení prodeje skateboardů o 2 kusy za měsíc. Jestliže majitel nakupuje skateboardy za cenu 25 dolarů, při jaké prodejní ceně bude jeho měsíční zisk maximální?',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'x=45 \\, \\$', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e10_05',
        "content_latex": 'Město Bory je 10 km východně od města Akáty a město Cédry je 3 km jižně od města Bory. Z A do C se má postavit silnice, a to tak, že se využije dálnice z A do B, přičemž se do C odbočí v nějakém bodě P na trase A-B. Náklady na přestavbu dálnice jsou 4 miliony Kč na 1 km, zatímco cena na stavbu silnice kdekoliv jinde je 5 milionu Kč na 1 km. Jak daleko od města A se má umístit bod P tak, aby stavba byla co nejlevnější a jaká bude tato cena?',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': '$6 \\,km$ od města Akáty, stavba bude stát $49 \\cdot 10^{6}$ Kč', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e10_06',
        "content_latex": 'Zjistěte rozměry otevřeného bazénu o daném objemu $32 \\,m^3$ se čtvercovým dnem tak, aby na vyzdění jeho stěn a dna bylo použito co nejmenší množství materiálu.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'a = 4 \\,m$, $v = 2 \\,m', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e10_07',
        "content_latex": 'Najděte rovnoramenný trojúhelník, který má při daném obvodu minimální obsah.',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'rovnostranný trojúhelník se stranou $a=\\frac{o}{3}$, $o$ je jeho obvod', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
    {
        "task_id": 'e10_08',
        "content_latex": 'Roh v 1. kvadrantu potřebujeme uzavřít závorou délky 20 metrů přes body $[a, \\,0]$, $[0, \\,b]$ tak, aby uzavřený segment tvaru trojúhelníku měl maximální plošný obsah. Pro jaké hodnoty $a$, $b$ to nastane?',
        "results": [{'key': 'vysledek', 'label_latex': '= ', 'type': 'mathlive', 'expected': 'a = b = 10 \\cdot \\sqrt 2 \\,m', 'tolerance': 0.0}],
        "cognitive_load": 'C',
    },
]
