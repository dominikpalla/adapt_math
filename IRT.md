# AdaptMath: BKT Model a Adaptivní Selekce Úloh (IRT)

Tento dokument popisuje aktuální experimentální implementaci výpočtu kognitivního profilu studenta (BKT) a návrh enginu pro adaptivní výběr dalších úloh na základě expertních IRT parametrů.

## 1. Aktualizace znalostí: Zjednodušený BKT Model

BKT (Bayesian Knowledge Tracing) v našem systému dynamicky upravuje pravděpodobnost ($P_{current}$), s jakou student ovládá danou doménu (např. "Limity funkcí"), na základě jeho bezprostřední interakce s úlohou.

* **Parametr učení ($\alpha$):** Váha odměny za správnou odpověď. Počítá se dynamicky z jistoty studenta ($C \in [0, 1]$):
    $$\alpha = 0.2 + 0.2 \cdot C$$
    *(Pokud student využil AI nápovědu, je $\alpha$ sníženo na polovinu: $\alpha = \alpha \cdot 0.5$)*
* **Parametr trestu ($\beta$):** Váha penalizace za chybu:
    $$\beta = 0.03 + 0.02 \cdot C$$

**Přepočet kognitivního profilu ($P_{new}$):**
* Při správné odpovědi: $P_{new} = P_{current} + \alpha \cdot (1 - P_{current})$
* Při chybné odpovědi: $P_{new} = P_{current} - \beta \cdot P_{current}$
*(Hodnoty jsou saturovány do mantinelů 0.01 až 0.99).*

---

## 2. Parametry úloh: Item Response Theory (IRT)

Zatímco BKT modeluje studenta, IRT modeluje kvalitu a náročnost samotných úloh. V databázi (tabulka `math_tasks`) aktuálně uchováváme dvě expertně odhadnuté hodnoty pro každou úlohu:
* **`irt_difficulty` ($b$):** Obtížnost úlohy (typicky v rozsahu -3.0 až +3.0).
* **`irt_discrimination` ($a$):** Jak dobře úloha rozlišuje silné a slabé studenty (v adaptivních systémech kladná hodnota, typicky 0.5 až 2.5).

### Pilotní seed (od 2026-08-24)

V počáteční pilotní fázi jsou hodnoty zjednodušené:

* **`irt_difficulty`** nastavuje **lektor v editoru úlohy** pomocí selectu se třemi předdefinovanými hodnotami:
    * **Lehká** → $b = -2$
    * **Střední** → $b = 0$ (výchozí)
    * **Těžká** → $b = +2$
* **`irt_discrimination`** je pro všechny úlohy fixně **1.0** (standardní 2PL default, „úloha rozlišuje neutrálně"). V UI ji lektor nevidí ani nemění. Ruční nastavení `a = 0` by celý model degradovalo — pravděpodobnost správné odpovědi by pak byla vždy $0.5$ nezávisle na obtížnosti i schopnosti studenta.

Backfill provedený 2026-08-24: všech 923 úloh v DB s dříve `NULL` hodnotami dostalo `b = 0`, `a = 1.0`. Backend validuje, že POST na `/api/tasks/<id>` přijímá `irt_difficulty` jen z množiny `{-2.0, 0.0, 2.0}`.

---

## 3. Adaptivní engine: Selekce další úlohy

Abychom vybrali studentovi ideální další úlohu, musíme propojit jeho aktuální BKT skóre ($P \in [0.01, 0.99]$) s IRT škálou úloh ($-3$ až $+3$). 

**Krok 1: Převod BKT na úroveň schopností ($\theta$)**
Využijeme logitovou transformaci k převodu pravděpodobnosti na logistickou škálu:
$$\theta = \ln\left(\frac{P_{new}}{1 - P_{new}}\right)$$
*Příklad: Pokud BKT profil studenta v Limitech stoupl na $P = 0.88$, jeho odhadovaná schopnost $\theta$ je cca $+1.99$. Pokud je $P = 0.12$, jeho $\theta$ je cca $-1.99$.*

**Krok 2: Výběr úlohy (Targeting)**
Algoritmus následně v databázi vyhledá úlohy ze zvolené domény a seřadí je podle toho, jak moc se jejich obtížnost ($b$) blíží studentově schopnosti ($\theta$). 

Hledáme úlohu, která minimalizuje rozdíl:
$$|b - (\theta + \Delta_{Vygotsky})|$$

*Poznámka: Můžeme aplikovat mírný posun (např. $\Delta_{Vygotsky} = 0.2$), abychom cílili do zóny nejbližšího vývoje – úloha by měla být o malý kousek těžší, než je aktuální komfortní zóna studenta, čímž maximalizujeme efektivitu učení.*

---

## 4. Budoucí vývoj: Empirická rekalibrace (Fáze 2)

Problém expertního odhadu spočívá v tom, že učitelé často vnímají obtížnost úloh jinak než samotní studenti. Proto jakmile systém nasbírá dostatečné množství behaviorálních dat (záznamy v `interaction_logs` o úspěšnosti a časech řešení), bude spuštěna analytická pipeline pomocí knihovny `py-irt`.

Tato knihovna zpětně zanalyzuje matici odpovědí od stovek studentů a vypočítá **skutečné, empiricky podložené hodnoty** `irt_difficulty` a `irt_discrimination`. Tyto přesné statistické hodnoty následně v databázi trvale nahradí naše počáteční expertní odhady, čímž se adaptivní selekce zásadně zpřesní.