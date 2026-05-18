"""
Definice úloh pro task checker — rozdělené po jednotlivých cvičeních.

Každý soubor `cvNN.py` exportuje proměnnou `TASKS` = list slovníků
v formátu MathTask (viz model.py docstring).

`ALL_TASKS` agreguje úlohy ze všech cvičení v pořadí, ve kterém jsou
ve skriptech „Základy matematiky 1".
"""

from . import cv01, cv02, cv03, cv04, cv05, cv06, cv07, cv08, cv09, cv10, cv11, cv12, cv13

ALL_TASKS = (
    cv01.TASKS + cv02.TASKS + cv03.TASKS + cv04.TASKS +
    cv05.TASKS + cv06.TASKS + cv07.TASKS + cv08.TASKS +
    cv09.TASKS + cv10.TASKS + cv11.TASKS + cv12.TASKS + cv13.TASKS
)
