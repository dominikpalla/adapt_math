import pandas as pd
import numpy as np
from pyBKT.models import Model


def run_bkt_demo():
    print("🚀 Spouštím demo AdaptMath BKT Enginu...\n")

    # 1. Simulace dat z naší databáze (tabulka interaction_logs)
    # V produkci sem natáhneme data přes SQLAlchemy (např. pd.read_sql)
    # Simulujeme studenta, který se postupně učí téma "topic_1"
    data = pd.DataFrame({
        'user_id': ['student_1', 'student_1', 'student_1', 'student_1'],
        'skill_name': ['topic_1', 'topic_1', 'topic_1', 'topic_1'],
        'correct': [0, 1, 1, 1],
        'used_llm_hint': [False, True, False, False],
        'certainty_level': [0.2, 0.6, 0.9, 0.8]  # Jistota 0.0 až 1.0
    })

    print("📊 Vstupní data (logy interakcí):")
    print(data[['correct', 'used_llm_hint', 'certainty_level']])
    print("-" * 40)

    # 2. Transformace features pro pyBKT (multilearn model)
    # Knihovna pyBKT umožňuje rozdělit parametr učení (alfu) podle typu interakce.
    # Vytvoříme sloupec 'learning_state', který kombinuje vliv LLM a jistoty.
    def determine_learning_state(row):
        if row['used_llm_hint']:
            # Podle vize dr. Medkové: využití LLM nápovědy modifikuje (snižuje) alfu
            return "hint_used"
        elif row['certainty_level'] > 0.7:
            # Vysoká jistota a správná odpověď = nejvyšší alfa
            return "high_certainty"
        else:
            # Běžná interakce
            return "normal"

    data['learning_state'] = data.apply(determine_learning_state, axis=1)

    # 3. Inicializace pyBKT modelu
    # Zakomponování hranic od dr. Ševčíkové pro inicializaci EM algoritmu
    # alfa (learns) = 0.1 až 0.4
    # beta (slips/trest) = 0.03 až 0.05
    defaults = {
        'learns': np.random.uniform(0.1, 0.4),
        'slips': np.random.uniform(0.03, 0.05),
        'guesses': 0.1,  # Pravděpodobnost uhodnutí u Multiple Choice
        'priors': 0.1  # Výchozí neznalost tématu (jak jsme definovali ve Student modelu)
    }

    # Vytvoření modelu s našimi výchozími parametry
    model = Model(seed=42, defaults=defaults)

    # 4. Trénování (Fit) modelu
    print("🧠 Trénuji BKT model a hledám optimální parametry pro téma...")
    # Parametr multilearn_models říká pyBKT, ať pro každý 'learning_state'
    # vypočítá vlastní parametr učení (alfu).
    model.fit(data=data, multilearn_models=['learning_state'])

    # 5. Predikce kognitivního profilu
    print("🔮 Predikuji aktuální stav znalostí studenta...")
    predictions = model.predict(data=data)

    # Ve sloupci 'state_predictions' je průběžně počítaná pravděpodobnost P(zná).
    # Nás zajímá hodnota po poslední interakci, abychom ji uložili do DB modelu Studenta.
    current_knowledge = predictions['state_predictions'].iloc[-1]

    print("-" * 40)
    print(
        f"✅ Nová hodnota pro kognitivní profil 'topic_1': {current_knowledge:.2f} (tj. {current_knowledge * 100:.0f} %)")
    print("-" * 40)

    print("📈 Kalibrované parametry učení (alfa) pro jednotlivé typy interakcí:")
    # Zobrazení nalezených parametrů (mělo by být vidět, že hint_used má jinou alfu než high_certainty)
    learn_rates = model.params().loc['topic_1', 'learns']
    print(learn_rates)


if __name__ == "__main__":
    run_bkt_demo()