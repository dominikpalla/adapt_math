from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base


# Předpokládáme, že Base je již definován výše (Base = declarative_base())

def init_db(database_url: str):
    """
    Inicializuje připojení k databázi a vytvoří všechny potřebné tabulky
    dle našich ORM modelů (Student, MathTask, InteractionLog).

    Args:
        database_url (str): Připojovací řetězec k databázi. Pro náš Docker to bude:
                            'postgresql://adaptmath_user:supersecretpassword@localhost:5432/adaptmath'

    Returns:
        sessionmaker: Továrna pro vytváření databázových relací (sessions).
    """
    print(f"🔄 Inicializuji připojení k databázi...")

    # Vytvoření 'engine' - což je hlavní komunikační uzel mezi SQLAlchemy a databází.
    # Parametr echo=False znamená, že nebudeme logovat každý vygenerovaný SQL dotaz do konzole.
    # Pro ladění a debugování enginu si to klidně přepni na True.
    engine = create_engine(database_url, echo=False)

    try:
        # Tento příkaz zkontroluje schéma naší databáze.
        # Pokud tabulky (math_tasks, students, interaction_logs) neexistují, automaticky je vytvoří.
        # Pokud už existují, příkaz je bezpečně přeskočí a data nepřemaže.
        Base.metadata.create_all(bind=engine)
        print("✅ Databázové tabulky byly úspěšně zkontrolovány/vytvořeny.")
    except Exception as e:
        print(f"❌ Chyba při vytváření tabulek nebo připojování k DB: {e}")
        # Vyhodíme výjimku dál, protože bez databáze náš adaptivní engine nemůže fungovat
        raise

    # Vytvoření třídy SessionLocal. Každá její instance bude představovat
    # jednu izolovanou databázovou transakci (session).
    # Nastavení autocommit=False a autoflush=False nám dává plnou kontrolu nad tím,
    # kdy se data reálně zapíší (musíme explicitně zavolat session.commit()).
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal