import time
from sqlalchemy import create_engine, Column, String, Float, Boolean, Integer, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Základní třída pro všechny naše ORM modely
Base = declarative_base()


class MathTask(Base):
    """
    ORM Model pro matematickou úlohu.
    Uchovává zadání v LaTeXu, klasifikaci a kalibrované IRT parametry.
    """
    __tablename__ = 'math_tasks'

    # Unikátní ID úlohy (ideálně UUID)
    task_id = Column(String, primary_key=True, index=True)

    # Obsah zadání, který se bude na frontendu v Moodlu renderovat pomocí KaTeXu
    content_latex = Column(String, nullable=False)
    has_image = Column(Boolean, default=False)

    # Typ výsledku ('decimal', 'fraction', 'multiple_choice') a správná odpověď
    result_type = Column(String, nullable=False)
    # Odpověď ukládáme jako JSON, aby zvládla string, číslo i pole
    correct_answer = Column(JSON, nullable=False)
    tolerance = Column(Float, default=0.0)

    # --- Metadatový a znalostní model ---
    # Klasifikace A-F určující typ a praktičnost úlohy
    cognitive_load = Column(String)
    # Vektor umístění úlohy ve znalostním grafu (uloženo jako JSON pole)
    graph_vector = Column(JSON)

    # --- IRT Parametry ---
    # Hodnota obtížnosti (typicky -3.0 až 3.0) a diskriminace (-2.5 až 2.5)
    irt_difficulty = Column(Float)
    irt_discrimination = Column(Float)

    # Relace na všechny logy, kde byla tato úloha řešena
    interactions = relationship("InteractionLog", back_populates="task")


class Student(Base):
    """
    ORM Model pro studenta.
    Uchovává statické preference a dynamicky aktualizovaný kognitivní profil (BKT).
    """
    __tablename__ = 'students'

    # Unikátní ID studenta (propojitelné s uživatelem v Moodlu)
    student_id = Column(String, primary_key=True, index=True)

    # --- Statické preference (z dotazníku) ---
    learning_style = Column(String)  # např. 'visual', 'textual'
    motivation = Column(String)  # např. 'intrinsic', 'extrinsic'
    math_anxiety = Column(String)  # úroveň matematické úzkosti
    personality_traits = Column(String)  # osobnostní rysy dle Augustina

    # --- Kognitivní profil (BKT) ---
    # Vektor zastupující pravděpodobnost zvládnutí cca 20 domén/témat.
    # Uloženo jako JSON (např. {"topic_1": 0.15, "topic_2": 0.82}).
    # Dynamicky se přepisuje po každé interakci.
    cognitive_profile = Column(JSON, nullable=False)

    # Relace na historii chování (1 student má N interakcí)
    interactions = relationship("InteractionLog", back_populates="student")


class InteractionLog(Base):
    """
    ORM Model pro behaviorální data (logy).
    Každý pokus studenta o vyřešení úlohy vytvoří jeden záznam.
    Slouží pro výpočty statistik, BKT update a analytiku.
    """
    __tablename__ = 'interaction_logs'

    log_id = Column(Integer, primary_key=True, autoincrement=True)

    # Cizí klíče propojující log se studentem a úlohou
    student_id = Column(String, ForeignKey('students.student_id'), nullable=False)
    task_id = Column(String, ForeignKey('math_tasks.task_id'), nullable=False)

    # ID sezení pro analýzu chování v čase (session tracking)
    session_id = Column(String, index=True)

    # Časová značka (UNIX timestamp)
    timestamp = Column(Float, default=time.time)
    time_spent = Column(Float, nullable=False)

    # Vyhodnocení správnosti
    is_correct = Column(Boolean, nullable=False)

    # Hodnota jistoty studenta (např. 0.0 - 1.0)
    certainty_level = Column(Float)

    # Flag určující, zda byla využita experimentální interaktivní AI nápověda
    # (pokud ano, budeme v BKT snižovat parametr učení alfa)
    used_llm_hint = Column(Boolean, default=False)

    # --- NOVÉ SLOUPCE PRO VÝZKUM A VIZUALIZACI ---
    # Uložení celého stavu profilu PO této interakci (výzkumný snapshot)
    cognitive_profile_snapshot = Column(JSON)

    # Rychlá data pro frontendovou tabulku (co se změnilo a o kolik)
    changed_topic = Column(String)
    mastery_delta = Column(Float)

    # Zpětné relace pro pohodlné dotazování
    student = relationship("Student", back_populates="interactions")
    task = relationship("MathTask", back_populates="interactions")