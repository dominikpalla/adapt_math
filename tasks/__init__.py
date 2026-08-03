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

ALL_TASKS = (
    cv01.TASKS + cv02.TASKS + cv03.TASKS + cv04.TASKS +
    cv05.TASKS + cv06.TASKS + cv07.TASKS + cv08.TASKS +
    cv09.TASKS + cv10.TASKS + cv11.TASKS + cv12.TASKS + cv13.TASKS +
    ss01.TASKS + ss02.TASKS + ss03.TASKS + ss04.TASKS +
    ss05.TASKS + ss06.TASKS + ss07.TASKS
)
