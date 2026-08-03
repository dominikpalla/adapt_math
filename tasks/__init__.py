"""
Definice úloh pro task checker — rozdělené po jednotlivých cvičeních.

Každý soubor `cvNN.py` exportuje proměnnou `TASKS` = list slovníků
v formátu MathTask (viz model.py docstring).

`ALL_TASKS` agreguje úlohy ze všech cvičení v pořadí, ve kterém jsou
ve skriptech „Základy matematiky 1".
"""

from . import cv01, cv02, cv03, cv04, cv05, cv06, cv07, cv08, cv09, cv10, cv11, cv12, cv13
# SŠ úlohy z Overleaf zdrojů (Andrea) — extrahováno 2026-08-03
from . import ss01, ss02, ss03, ss04, ss05, ss06, ss07
# UMAT — kapitoly ze skripta „Základy matematiky 1" 2007-05-29.
# Automaticky extrahováno scripts/extract_umat.py 2026-08-03.
from . import umat_06, umat_07, umat_08, umat_09
# UMAT extra — kapitoly, které v v1 dostaly 0 úloh (text answers /
# \begin{ul} bloky). V2 parser přidal MC z textových odpovědí a rozparsoval
# Řešení: odstavce. Prefix `eXX_` aby task_id nekolidovaly s v1 extraction.
from . import umat_01e, umat_03e, umat_04e, umat_10e, umat_11e

ALL_TASKS = (
    cv01.TASKS + cv02.TASKS + cv03.TASKS + cv04.TASKS +
    cv05.TASKS + cv06.TASKS + cv07.TASKS + cv08.TASKS +
    cv09.TASKS + cv10.TASKS + cv11.TASKS + cv12.TASKS + cv13.TASKS +
    ss01.TASKS + ss02.TASKS + ss03.TASKS + ss04.TASKS +
    ss05.TASKS + ss06.TASKS + ss07.TASKS +
    umat_06.TASKS + umat_07.TASKS + umat_08.TASKS + umat_09.TASKS +
    umat_01e.TASKS + umat_03e.TASKS + umat_04e.TASKS + umat_10e.TASKS + umat_11e.TASKS
)
