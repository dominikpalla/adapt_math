# AdaptMath: Zjednodušený BKT (Bayesian Knowledge Tracing) Model

Tento dokument popisuje aktuální experimentální implementaci výpočtu kognitivního profilu studenta v prototypu AdaptMath. Logika je nasazena v souboru `app.py` v endpointu `/evaluate`.

Cílem tohoto zjednodušeného modelu je dynamicky upravovat pravděpodobnost, s jakou student ovládá danou doménu (např. "Limity funkcí"), na základě jeho bezprostřední interakce s úlohou.

## 1. Vstupní proměnné

Při každém odeslání odpovědi vstupují do výpočtu následující proměnné:

* **$P_{current}$**: Aktuální úroveň znalosti daného tématu. Pokud téma student řeší poprvé, je výchozí hodnota **0.1** (10 %).
* **$C$ (Jistota)**: Úroveň jistoty studenta při odpovědi, zadávaná na škále **0.0** (hádám) až **1.0** (jsem si jistý).
* **Správnost**: Vyhodnocení, zda se studentská odpověď shoduje se správnou odpovědí v rámci povolené tolerance.
* **Nápověda**: Pravdivostní hodnota (True/False) udávající, zda student využil generativní AI nápovědu.

## 2. Výpočet parametrů učení a trestu

Na základě doporučení z projektové schůzky (dr. Ševčíková) jsou parametry $\alpha$ (odměna) a $\beta$ (trest) počítány dynamicky podle jistoty studenta.

### Parametr učení ($\alpha$)
Určuje váhu odměny za správnou odpověď. Pohybuje se v teoretickém rozsahu 0.2 až 0.4 podle vzorce:

$$\alpha = 0.2 + 0.2 \cdot C$$

**Penalizace za nápovědu:** Pokud student využil AI nápovědu, je hodnota $\alpha$ snížena na polovinu (násobena **0.5**). Tím model reflektuje, že ke správnému řešení nedošel zcela samostatně.

### Parametr trestu ($\beta$)
Určuje váhu penalizace za špatnou odpověď. Pohybuje se v teoretickém rozsahu 0.03 až 0.05 podle vzorce:

$$\beta = 0.03 + 0.02 \cdot C$$

Vyšší jistota při chybné odpovědi generuje mírně vyšší penalizaci, neboť indikuje silněji zakořeněný omyl.

## 3. Aktualizace pravděpodobnosti znalosti ($P_{new}$)

Samotný přepočet kognitivního profilu závisí na správnosti odpovědi:

* **Při správné odpovědi:** Znalost asymptoticky roste k hranici 100 %.
    $$P_{new} = P_{current} + \alpha \cdot (1 - P_{current})$$

* **Při chybné odpovědi:** Znalost klesá úměrně tomu, co už student umí.
    $$P_{new} = P_{current} - \beta \cdot P_{current}$$

## 4. Ošetření extrémů a výpočet změny (Delta)

Aby se předešlo matematickým extrémům, je výsledná hodnota $P_{new}$ saturována a vždy udržována v bezpečných mezích:
* Minimální možná hodnota: **0.01**
* Maximální možná hodnota: **0.99**

Pro účely výzkumného logování a vizualizace na frontendu je následně vypočítána absolutní změna (delta):

$$\Delta = P_{new} - P_{current}$$

Tato $\Delta$, zasažené téma i kompletní snapshot profilu po interakci se ukládají do tabulky `interaction_logs` v databázi.