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
            "type": "latex_expr",
            "expected": "(-\\infty, 0) \\cup (2, 3)"
          }
        ]

    Příklad pro úlohu „Najděte intervaly monotonie a extrémy":
        results = [
          { "key": "roste", "label_latex": "Roste na ", "type": "latex_expr",
            "expected": "(-\\infty, -1) \\cup (3, \\infty)" },
          { "key": "klesa", "label_latex": "Klesá na ", "type": "latex_expr",
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
      type:          decimal | latex_expr | multiple_choice | open_text
      expected:      podle typu:
                       decimal:         float
                       latex_expr:      string (LaTeX, porovnán přes Compute Engine)
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

    # ----- Metadata pro budoucí adaptivní engine (zatím needitujeme) -----
    cognitive_load = Column(String, nullable=True)   # A-F
    graph_vector = Column(JSON, nullable=True)       # ["Limity funkcí", ...]
    irt_difficulty = Column(Float, nullable=True)    # ±3
    irt_discrimination = Column(Float, nullable=True)  # ±2.5
