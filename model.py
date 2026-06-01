from sqlalchemy import Column, String, Float, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class MathTask(Base):
    """
    Matematická úloha.

    Každá úloha má jedno zadání v LaTeXu a **kolekci pojmenovaných výsledků**
    (`results`). Každý výsledek je sám o sobě jeden očekávaný vstup studenta
    (číslo, LaTeX výraz, výběr možnosti, otevřený text) a má svůj typ.

    Příklad pro úlohu „Určete definiční obor"  vypadá takto:
        results = [
          {
            "key": "Df",
            "label_latex": "D(f) = ",
            "type": "mathlive",
            "expected": "(-\\infty, 0) \\cup (2, 3)"
          }
        ]

    Příklad pro úlohu „Najděte intervaly monotonie a extrémy":
        results = [
          { "key": "roste", "label_latex": "Roste na ", "type": "mathlive",
            "expected": "(-\\infty, -1) \\cup (3, \\infty)" },
          { "key": "klesa", "label_latex": "Klesá na ", "type": "mathlive",
            "expected": "(-1, 3)" },
          { "key": "lokmax", "label_latex": "Lokální max v ", "type": "decimal",
            "expected": -1, "tolerance": 0.001 },
          { "key": "lokmin", "label_latex": "Lokální min v ", "type": "decimal",
            "expected": 3, "tolerance": 0.001 },
        ]

    Struktura jednoho výsledku:
      key:           interní identifikátor (pro logging / vyhodnocení)
      label_latex:   prefix zobrazený před vstupním polem (LaTeX),
                     např. "D(f) = " nebo "Inflexní bod x_1 = " (může být prázdný)
      type:          decimal | mathlive | multiple_choice | open_text
      expected:      podle typu:
                       decimal:         float
                       mathlive:      string (LaTeX, porovnán přes Compute Engine)
                       multiple_choice: klíč správné možnosti (string)
                       open_text:       vzorové řešení (string, vyhodnocuje LLM/expert)
      tolerance:     pro decimal numerická tolerance (default 0)
      options:       pro multiple_choice — pole {key, label_latex} (label může obsahovat LaTeX)
    """
    __tablename__ = 'math_tasks'

    # Identifikátor stylu "cv04_1", "cv01_3" atd. (cvičení_index)
    task_id = Column(String, primary_key=True, index=True)

    # Zadání v LaTeXu (renderuje KaTeX; pure-math wrapneme automaticky do $$...$$ ve frontendu)
    content_latex = Column(String, nullable=False)

    # Kolekce pojmenovaných výsledků (viz docstring výše)
    results = Column(JSON, nullable=False)

    # ----- Klasifikace / metadata pro adaptivní engine -----
    # Kognitivní zátěž (A–F) — typ / praktičnost úlohy, edituje expert.
    cognitive_load = Column(String, nullable=True)

    # Primární kategorie úlohy — jeden řetězec ze seznamu TASK_CATEGORIES
    # v tasks/knowledge_weights.py (45 položek; jen SŠ + VŠ matematika,
    # bez vlastností/typu/dovedností). Slouží k pozdější automatické
    # generaci defaultního knowledge_vector dle kategorie.
    category = Column(String, nullable=True)

    # Multi-select anotace (ukládají se „bokem" — orthogonální ke kategorii):
    #   properties → list ze TASK_PROPERTIES (9 vlastností),
    #   task_type  → list ze TASK_TYPES (zatím 1: Aplikační),
    #   skills     → list ze TASK_SKILLS (6 dovedností).
    properties = Column(JSON, nullable=True)
    task_type = Column(JSON, nullable=True)
    skills = Column(JSON, nullable=True)

    # Vektor vah znalostního grafu — dict {weight_name: int 0..100}.
    # 61 možných vah definuje KNOWLEDGE_WEIGHTS v tasks/knowledge_weights.py.
    # Při řešení úlohy se přírůstek / úbytek znalosti distribuuje mezi
    # skill-komponenty v poměru těchto vah. Suma vah by se měla blížit 100 %.
    knowledge_vector = Column(JSON, nullable=True)

    # Starší tag-vektor (volné textové tagy) — nadále jen pro kompatibilitu,
    # v UI editoru se už nezobrazuje. Plánujeme migrovat do knowledge_vector.
    graph_vector = Column(JSON, nullable=True)

    # IRT parametry (zatím needitujeme přes UI, doplní expert / py-irt pilot).
    irt_difficulty = Column(Float, nullable=True)    # ±3
    irt_discrimination = Column(Float, nullable=True)  # ±2.5
