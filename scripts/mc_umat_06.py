"""
Konverze umat_06_09..umat_06_43 (kromě _29 která už je MC) na multiple-choice.
Ručně navržené distraktory pedagogicky rozumné (typické studentské chyby:
vynechání části řešení, obrácená perioda, sousední úhel z tabulky).

Odpověď (`expected`) rozprostřena mezi a/b/c/d podle idx % 4.

Použití:
    DATABASE_URL=... python scripts/mc_umat_06.py                # dry-run
    DATABASE_URL=... python scripts/mc_umat_06.py --commit
"""
from __future__ import annotations
import argparse, os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sqlalchemy.orm.attributes import flag_modified
from database import init_db
from model import MathTask

# Pomocník: bigcup obal
def BU_set(*items):
    """\\bigcup\\limits_{k \\in \\mathbb{Z}} \\left\\{ item1, item2, ... \\right\\}"""
    inner = ",\\ ".join(items)
    return r"$\bigcup\limits_{k \in \mathbb{Z}} \left\{" + inner + r"\right\}$"

def BU_open(*items):
    """otevřený interval: \\bigcup ... \\left( ... \\right)"""
    inner = ",\\ ".join(items)
    return r"$\bigcup\limits_{k \in \mathbb{Z}} \left(" + inner + r"\right)$"

def BU_close(*items):
    inner = ",\\ ".join(items)
    return r"$\bigcup\limits_{k \in \mathbb{Z}} \left[" + inner + r"\right]$"

# Definice MC pro každou úlohu.
# Formát: task_id -> {"correct_label": "...", "distractors": ["...","...","..."]}
# `correct_label` je LaTeX-obalený zápis správné množiny řešení (přesně dle DB).
# `distractors` jsou 3 pedagogicky rozumné chybné odpovědi.
# Correct key rozdělíme cyklicky (idx % 4) pro promíchání.

MC_DATA = {
    "umat_06_09": {  # sin(2x-π/4) = -1/2
        "correct": BU_set(r"\dfrac{17\pi}{24}+k\pi", r"\dfrac{25\pi}{24}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{17\pi}{24}+2k\pi", r"\dfrac{25\pi}{24}+2k\pi"),  # špatná perioda 2π místo π
            BU_set(r"\dfrac{7\pi}{24}+k\pi", r"\dfrac{25\pi}{24}+k\pi"),      # jiný ref. úhel
            BU_set(r"\dfrac{17\pi}{24}+k\pi"),                                 # vynechané druhé řešení
        ],
    },
    "umat_06_10": {  # 2sin(x/3+π/6)=√3
        "correct": BU_set(r"\dfrac{\pi}{2}+6k\pi", r"\dfrac{3\pi}{2}+6k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{2}+2k\pi", r"\dfrac{3\pi}{2}+2k\pi"),        # zapomenutá substituce x/3
            BU_set(r"\dfrac{\pi}{6}+6k\pi", r"\dfrac{5\pi}{6}+6k\pi"),        # špatný ref. úhel
            BU_set(r"\dfrac{\pi}{2}+6k\pi"),                                    # jen jedno řešení
        ],
    },
    "umat_06_11": {  # cos(4x+π/2) = √3/2
        "correct": BU_set(r"-\dfrac{\pi}{12}+\dfrac{k\pi}{2}", r"\dfrac{\pi}{3}+\dfrac{k\pi}{2}"),
        "distractors": [
            BU_set(r"-\dfrac{\pi}{12}+2k\pi", r"\dfrac{\pi}{3}+2k\pi"),       # zapomenutá substituce 4x
            BU_set(r"\dfrac{\pi}{12}+\dfrac{k\pi}{2}", r"-\dfrac{\pi}{3}+\dfrac{k\pi}{2}"),  # špatné znaménko
            BU_set(r"\dfrac{\pi}{12}+\dfrac{k\pi}{2}"),                        # jen jedno řešení
        ],
    },
    "umat_06_12": {  # tg(2x-π/6) = √3
        "correct": BU_set(r"\dfrac{\pi}{4}+\dfrac{k\pi}{2}"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{4}+k\pi"),                                     # zapomenutá substituce 2x
            BU_set(r"\dfrac{\pi}{3}+\dfrac{k\pi}{2}"),                          # špatná substituce (bez posunu -π/6)
            BU_set(r"\dfrac{\pi}{6}+\dfrac{k\pi}{2}"),                          # jiný ref. úhel z tabulky
        ],
    },
    "umat_06_13": {  # (1/√3)cotg(x/3-π/6) = -√3/3
        "correct": BU_set(r"\dfrac{11\pi}{4}+3k\pi"),
        "distractors": [
            BU_set(r"\dfrac{11\pi}{4}+k\pi"),                                   # zapomenutá substituce x/3
            BU_set(r"\dfrac{3\pi}{4}+3k\pi"),                                   # špatný ref. úhel
            BU_set(r"-\dfrac{\pi}{4}+3k\pi"),                                   # opačné znaménko
        ],
    },
    "umat_06_14": {  # 2sin²x = √2 sinx
        "correct": BU_set(r"k\pi", r"\dfrac{\pi}{4}+2k\pi", r"\dfrac{3\pi}{4}+2k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{4}+2k\pi", r"\dfrac{3\pi}{4}+2k\pi"),         # vynechané k\pi (dělení sinx bez ošetření)
            BU_set(r"k\pi", r"\dfrac{\pi}{4}+k\pi", r"\dfrac{3\pi}{4}+k\pi"),  # špatná perioda π místo 2π
            BU_set(r"k\pi", r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),# jiný ref. úhel
        ],
    },
    "umat_06_15": {  # 2cos²x = -√2 cosx
        "correct": BU_set(r"\dfrac{\pi}{2}+k\pi", r"\dfrac{3\pi}{4}+2k\pi", r"\dfrac{5\pi}{4}+2k\pi"),
        "distractors": [
            BU_set(r"\dfrac{3\pi}{4}+2k\pi", r"\dfrac{5\pi}{4}+2k\pi"),        # vynechané π/2+kπ
            BU_set(r"\dfrac{\pi}{2}+2k\pi", r"\dfrac{3\pi}{4}+2k\pi", r"\dfrac{5\pi}{4}+2k\pi"),
            BU_set(r"\dfrac{\pi}{2}+k\pi", r"\dfrac{\pi}{4}+2k\pi", r"\dfrac{7\pi}{4}+2k\pi"),
        ],
    },
    "umat_06_16": {  # tg²x = -tgx
        "correct": BU_set(r"k\pi", r"\dfrac{3\pi}{4}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{3\pi}{4}+k\pi"),                                    # vynechané k\pi
            BU_set(r"k\pi", r"\dfrac{\pi}{4}+k\pi"),                            # špatný ref. úhel
            BU_set(r"k\pi", r"\dfrac{3\pi}{4}+2k\pi"),                          # špatná perioda
        ],
    },
    "umat_06_17": {  # √3 tg²x + 2tgx - √3 = 0
        "correct": BU_set(r"\dfrac{\pi}{6}+k\pi", r"\dfrac{2\pi}{3}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{3}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),           # záměna doplňkových úhlů
            BU_set(r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{2\pi}{3}+2k\pi"),         # špatná perioda 2π
            BU_set(r"\dfrac{\pi}{6}+k\pi"),                                     # jen jedno řešení
        ],
    },
    "umat_06_18": {  # 3tg²x + 4√3 tgx + 3 = 0
        "correct": BU_set(r"\dfrac{2\pi}{3}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{3}+k\pi", r"\dfrac{\pi}{6}+k\pi"),            # opačné úhly (bez pi/)
            BU_set(r"\dfrac{2\pi}{3}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),        # špatná perioda
            BU_set(r"\dfrac{2\pi}{3}+k\pi"),                                     # jen jedno řešení
        ],
    },
    "umat_06_19": {  # 2 - 2cos²x - √3 sinx = 0
        "correct": BU_set(r"k\pi", r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{2\pi}{3}+2k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{2\pi}{3}+2k\pi"),         # vynechané kπ (vyloučené sinx=0)
            BU_set(r"k\pi", r"\dfrac{\pi}{3}+k\pi", r"\dfrac{2\pi}{3}+k\pi"),  # špatná perioda π
            BU_set(r"k\pi", r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),# jiný ref. úhel
        ],
    },
    "umat_06_20": {  # sin2x - cosx = 0
        "correct": BU_set(r"\dfrac{\pi}{2}+k\pi", r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),         # vynechané π/2+kπ (dělení cosx)
            BU_set(r"\dfrac{\pi}{2}+2k\pi", r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),
            BU_set(r"\dfrac{\pi}{2}+k\pi", r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{2\pi}{3}+2k\pi"),
        ],
    },
    "umat_06_21": {  # 2cos²x + 4sin²x = 3
        "correct": BU_set(r"\dfrac{\pi}{4}+k\pi", r"\dfrac{3\pi}{4}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{4}+2k\pi", r"\dfrac{3\pi}{4}+2k\pi"),         # špatná perioda
            BU_set(r"\dfrac{\pi}{6}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),           # jiný ref. úhel
            BU_set(r"\dfrac{\pi}{4}+k\pi"),                                     # jen jedno
        ],
    },
    "umat_06_22": {  # sin4x = √2 cos2x
        "correct": BU_set(r"\dfrac{\pi}{4}+\dfrac{k\pi}{2}", r"\dfrac{\pi}{8}+k\pi", r"\dfrac{3\pi}{8}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{8}+k\pi", r"\dfrac{3\pi}{8}+k\pi"),           # vynechané cos2x=0 řešení
            BU_set(r"\dfrac{\pi}{4}+k\pi", r"\dfrac{\pi}{8}+k\pi", r"\dfrac{3\pi}{8}+k\pi"),
            BU_set(r"\dfrac{\pi}{4}+\dfrac{k\pi}{2}"),                          # jen jedna komponenta
        ],
    },
    "umat_06_23": {  # sin2x = (cosx - sinx)²
        "correct": BU_set(r"\dfrac{\pi}{12}+k\pi", r"\dfrac{5\pi}{12}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{12}+2k\pi", r"\dfrac{5\pi}{12}+2k\pi"),       # špatná perioda
            BU_set(r"\dfrac{\pi}{6}+k\pi", r"\dfrac{\pi}{3}+k\pi"),            # jiné úhly
            BU_set(r"\dfrac{\pi}{12}+k\pi"),                                    # jen jedno
        ],
    },
    "umat_06_24": {  # sin²x + sin²2x = 1
        "correct": BU_set(r"\dfrac{\pi}{2}+k\pi", r"\dfrac{\pi}{6}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{6}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),           # vynechané π/2+kπ
            BU_set(r"\dfrac{\pi}{2}+2k\pi", r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),
            BU_set(r"\dfrac{\pi}{2}+k\pi", r"\dfrac{\pi}{4}+k\pi", r"\dfrac{3\pi}{4}+k\pi"),
        ],
    },
    "umat_06_25": {  # sin⁴x - cos⁴x = 1/2
        "correct": BU_set(r"\dfrac{\pi}{3}+k\pi", r"\dfrac{2\pi}{3}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{2\pi}{3}+2k\pi"),         # špatná perioda
            BU_set(r"\dfrac{\pi}{6}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),           # jiné úhly
            BU_set(r"\dfrac{\pi}{3}+k\pi"),                                     # jen jedno
        ],
    },
    "umat_06_26": {  # cotg²x + (√3-1)cotgx = √3
        "correct": BU_set(r"\dfrac{\pi}{4}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{4}+k\pi", r"\dfrac{\pi}{6}+k\pi"),            # špatný doplňek k π
            BU_set(r"\dfrac{3\pi}{4}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),          # π - π/4 (záměna)
            BU_set(r"\dfrac{\pi}{4}+k\pi"),                                     # jen jedno
        ],
    },
    "umat_06_27": {  # 3^(4sin²x) = 27
        "correct": BU_set(r"\dfrac{\pi}{3}+k\pi", r"\dfrac{2\pi}{3}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{2\pi}{3}+2k\pi"),         # špatná perioda
            BU_set(r"\dfrac{\pi}{6}+k\pi", r"\dfrac{5\pi}{6}+k\pi"),           # jiný ref. úhel (sin²=1/4)
            BU_set(r"\dfrac{\pi}{4}+k\pi", r"\dfrac{3\pi}{4}+k\pi"),           # sin²=1/2 (nesprávné)
        ],
    },
    "umat_06_28": {  # cos2x - cosx = sinx - sin2x
        "correct": BU_set(r"2k\pi", r"\dfrac{\pi}{6}+\dfrac{2k\pi}{3}"),
        "distractors": [
            BU_set(r"2k\pi"),                                                   # jen jedno
            BU_set(r"k\pi", r"\dfrac{\pi}{6}+\dfrac{2k\pi}{3}"),               # špatná perioda (π místo 2π)
            BU_set(r"2k\pi", r"\dfrac{\pi}{3}+\dfrac{2k\pi}{3}"),              # jiný ref. úhel
        ],
    },
    # umat_06_29 už MC je, přeskočíme
    "umat_06_30": {  # sinx + cosx = 1 + sin2x
        "correct": BU_set(r"\dfrac{3\pi}{4}+k\pi", r"\dfrac{\pi}{2}+2k\pi", r"2k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{2}+2k\pi", r"2k\pi"),                          # vynechané 3π/4+kπ
            BU_set(r"\dfrac{3\pi}{4}+2k\pi", r"\dfrac{\pi}{2}+k\pi", r"k\pi"), # špatná perioda
            BU_set(r"\dfrac{\pi}{4}+k\pi", r"\dfrac{\pi}{2}+2k\pi", r"2k\pi"), # sousední úhel
        ],
    },
    "umat_06_31": {  # sin3x = sin2x - sinx
        "correct": BU_set(r"\dfrac{k\pi}{2}", r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{5\pi}{3}+2k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{5\pi}{3}+2k\pi"),         # vynechané kπ/2
            BU_set(r"\dfrac{k\pi}{2}", r"\dfrac{\pi}{3}+k\pi", r"\dfrac{5\pi}{3}+k\pi"),
            BU_set(r"\dfrac{k\pi}{2}", r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{11\pi}{6}+2k\pi"),
        ],
    },
    "umat_06_32": {  # √3/cos²x - 4tgx = 0
        "correct": BU_set(r"\dfrac{\pi}{6}+k\pi", r"\dfrac{\pi}{3}+k\pi"),
        "distractors": [
            BU_set(r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{\pi}{3}+2k\pi"),          # špatná perioda
            BU_set(r"\dfrac{\pi}{4}+k\pi", r"\dfrac{3\pi}{4}+k\pi"),           # jiné úhly
            BU_set(r"\dfrac{\pi}{6}+k\pi"),                                     # jen jedno
        ],
    },
    "umat_06_33": {  # sin(x+π) ≤ -√3/2 [nerovnice]
        "correct": BU_open(r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{2\pi}{3}+2k\pi"),
        "distractors": [
            BU_close(r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{2\pi}{3}+2k\pi"),        # uzavřený interval
            BU_open(r"\dfrac{\pi}{3}+k\pi", r"\dfrac{2\pi}{3}+k\pi"),           # špatná perioda
            BU_open(r"\dfrac{4\pi}{3}+2k\pi", r"\dfrac{5\pi}{3}+2k\pi"),        # jiný ref. úhel
        ],
    },
    "umat_06_34": {  # cos(x-2) < -√3/2
        "correct": BU_open(r"\dfrac{5\pi}{6}+2(1+k\pi)", r"\dfrac{7\pi}{6}+2(1+k\pi)"),
        "distractors": [
            BU_open(r"\dfrac{5\pi}{6}+2k\pi", r"\dfrac{7\pi}{6}+2k\pi"),        # vynechaný posun -2
            BU_open(r"\dfrac{5\pi}{6}+k\pi", r"\dfrac{7\pi}{6}+k\pi"),          # špatná perioda
            BU_close(r"\dfrac{5\pi}{6}+2(1+k\pi)", r"\dfrac{7\pi}{6}+2(1+k\pi)"), # uzavřený
        ],
    },
    "umat_06_35": {  # tg(2x-1) < 1
        "correct": BU_open(r"-\dfrac{\pi}{4}+\dfrac{1}{2}(1+k\pi)", r"\dfrac{\pi}{8}+\dfrac{1}{2}(1+k\pi)"),
        "distractors": [
            BU_open(r"-\dfrac{\pi}{4}+k\pi", r"\dfrac{\pi}{8}+k\pi"),           # zapomenutá substituce 2x
            BU_close(r"-\dfrac{\pi}{4}+\dfrac{1}{2}(1+k\pi)", r"\dfrac{\pi}{8}+\dfrac{1}{2}(1+k\pi)"),
            BU_open(r"\dfrac{\pi}{4}+\dfrac{1}{2}(1+k\pi)", r"\dfrac{\pi}{8}+\dfrac{1}{2}(1+k\pi)"),
        ],
    },
    "umat_06_36": {  # tg3x < -1
        "correct": BU_open(r"-\dfrac{\pi}{6}+\dfrac{k\pi}{3}", r"-\dfrac{\pi}{12}+\dfrac{k\pi}{3}"),
        "distractors": [
            BU_open(r"-\dfrac{\pi}{6}+k\pi", r"-\dfrac{\pi}{12}+k\pi"),         # zapomenutá substituce 3x
            BU_open(r"\dfrac{\pi}{6}+\dfrac{k\pi}{3}", r"\dfrac{\pi}{12}+\dfrac{k\pi}{3}"),
            BU_open(r"-\dfrac{\pi}{4}+\dfrac{k\pi}{3}", r"-\dfrac{\pi}{6}+\dfrac{k\pi}{3}"),
        ],
    },
    "umat_06_37": {  # sinx + cos2x > 1
        "correct": r"$\bigcup\limits_{k \in \mathbb{Z}} \left(2k\pi,\ \dfrac{\pi}{6}+2k\pi\right) \cup \left(\dfrac{5\pi}{6}+2k\pi,\ \pi+2k\pi\right)$",
        "distractors": [
            r"$\bigcup\limits_{k \in \mathbb{Z}} \left(\dfrac{\pi}{6}+2k\pi,\ \dfrac{5\pi}{6}+2k\pi\right)$",  # komplement
            r"$\bigcup\limits_{k \in \mathbb{Z}} \left(2k\pi,\ \pi+2k\pi\right)$",  # celá horní půlrovina
            r"$\bigcup\limits_{k \in \mathbb{Z}} \left(2k\pi,\ \dfrac{\pi}{6}+2k\pi\right)$",  # jen jedna komponenta
        ],
    },
    "umat_06_38": {  # cosx ≤ 1/cosx
        "correct": r"$\bigcup\limits_{k \in \mathbb{Z}} \left(-\dfrac{\pi}{2}+2k\pi,\ \dfrac{\pi}{2}+2k\pi\right) \cup \{\pi+2k\pi\}$",
        "distractors": [
            r"$\bigcup\limits_{k \in \mathbb{Z}} \left(-\dfrac{\pi}{2}+2k\pi,\ \dfrac{\pi}{2}+2k\pi\right)$",  # bez izolovaného bodu
            r"$\bigcup\limits_{k \in \mathbb{Z}} \left[-\dfrac{\pi}{2}+2k\pi,\ \dfrac{\pi}{2}+2k\pi\right]$",  # uzavřený, bez izol.
            r"$\bigcup\limits_{k \in \mathbb{Z}} \{\pi+2k\pi\}$",  # jen izolované body
        ],
    },
    "umat_06_39": {  # sinx > 1/sinx
        "correct": BU_open(r"\pi+2k\pi", r"2\pi+2k\pi"),
        "distractors": [
            BU_open(r"2k\pi", r"\pi+2k\pi"),  # horní půlrovina (opak)
            r"$\varnothing$",  # nemá řešení
            BU_open(r"\pi+2k\pi", r"\dfrac{3\pi}{2}+2k\pi"),  # jen půlka
        ],
    },
    "umat_06_40": {  # 2sin²x - 7sinx > -3
        "correct": BU_open(r"\dfrac{5\pi}{6}+2k\pi", r"\dfrac{13\pi}{6}+2k\pi"),
        "distractors": [
            BU_open(r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),  # komplement (sinx > 1/2)
            BU_open(r"\dfrac{5\pi}{6}+k\pi", r"\dfrac{13\pi}{6}+k\pi"),  # špatná perioda
            r"$\mathbb{R}$",  # celé R (nesprávné)
        ],
    },
    "umat_06_41": {  # cos(sinx) < 0
        "correct": r"$\varnothing$",
        "distractors": [
            r"$\mathbb{R}$",
            BU_open(r"\dfrac{\pi}{2}+2k\pi", r"\dfrac{3\pi}{2}+2k\pi"),
            BU_set(r"k\pi"),
        ],
    },
    "umat_06_42": {  # 2cos²x > 3sinx
        "correct": BU_open(r"\dfrac{5\pi}{6}+2k\pi", r"\dfrac{13\pi}{6}+2k\pi"),
        "distractors": [
            BU_open(r"\dfrac{\pi}{6}+2k\pi", r"\dfrac{5\pi}{6}+2k\pi"),  # komplement
            BU_open(r"-\dfrac{\pi}{6}+2k\pi", r"\dfrac{7\pi}{6}+2k\pi"),  # posun
            r"$\varnothing$",
        ],
    },
    "umat_06_43": {  # 2sin²x + 7cosx - 5 < 0
        "correct": BU_open(r"\dfrac{\pi}{3}+2k\pi", r"\dfrac{5\pi}{3}+2k\pi"),
        "distractors": [
            BU_open(r"-\dfrac{\pi}{3}+2k\pi", r"\dfrac{\pi}{3}+2k\pi"),  # komplement (cosx > 1/2)
            BU_open(r"\dfrac{\pi}{3}+k\pi", r"\dfrac{5\pi}{3}+k\pi"),    # špatná perioda
            r"$\mathbb{R}$",
        ],
    },
}


def build_mc_options(idx: int, correct: str, distractors: list[str]):
    """Rozprostři correct mezi a/b/c/d podle idx % 4. Zbytek jsou distractors v pořadí."""
    keys = ["a", "b", "c", "d"]
    correct_pos = idx % 4
    correct_key = keys[correct_pos]
    labels = distractors.copy()  # 3 items
    labels.insert(correct_pos, correct)  # 4 items now, correct na pozici correct_pos
    return correct_key, [{"key": k, "label_latex": lab} for k, lab in zip(keys, labels)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    args = parser.parse_args()
    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr); return 2

    SessionLocal = init_db(args.db_url)
    sess = SessionLocal()
    changed = 0
    try:
        for idx, (task_id, data) in enumerate(sorted(MC_DATA.items())):
            t = sess.query(MathTask).filter_by(task_id=task_id).first()
            if not t:
                print(f"⚠ {task_id} nenalezena, přeskakuji.")
                continue
            if isinstance(t.results, list) and len(t.results) == 1 and t.results[0].get("type") == "multiple_choice":
                print(f"⚠ {task_id} už je MC, přeskakuji.")
                continue
            correct_key, options = build_mc_options(idx, data["correct"], data["distractors"])
            new_results = [{
                "key": "vysledek",
                "label_latex": r"\text{Množina řešení: }",
                "type": "multiple_choice",
                "options": options,
                "expected": correct_key,
            }]
            t.results = new_results
            flag_modified(t, "results")
            changed += 1
            print(f"✓ {task_id}: correct={correct_key}")

        print(f"\nZměněno {changed} úloh.")
        if args.commit:
            sess.commit()
            print("✓ COMMIT proveden.")
        else:
            sess.rollback()
            print("(DRY-RUN — nic nezapsáno.)")
        return 0
    finally:
        sess.close()


if __name__ == "__main__":
    sys.exit(main())
