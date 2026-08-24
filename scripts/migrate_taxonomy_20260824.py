"""
Taxonomy refactor 2026-08-24 dle nového seznamu dr. Medkové.

Rename map (properties = TASK_PROPERTIES):
    Vlasnosti - Lineární           -> Vlastnosti - Lineární
    Vlasnosti - Kvadratická        -> Vlastnosti - Kvadratická
    Vlasnosti - Mocninná           -> Vlastnosti - Mocninná
    Vlasnosti - Odmocninová        -> Vlastnosti - Odmocninová
    Vlasnosti - Logaritmická       -> Vlastnosti - Logaritmická
    Vlasnosti - Exponenciální      -> Vlastnosti - Exponenciální
    Vlasnosti - Absolutní hodnota  -> Vlastnosti - Absolutní hodnota
    Vlasnosti - Lomená lineární    -> Vlastnosti - Lomená lineární
    Vlasnosti - Racionální funkce  -> Vlastnosti - Racionální funkce
    Vlasnosti - S parametrem       -> Vlastnosti - S parametrem
    Vlastnosti - Goniometrická     -> beze změny (už s „t")

Rename map (skills = TASK_SKILLS):
    Dovednosti - Výpočet rovnic    -> Dovednosti - Řešení rovnic
    Dovednosti - Výpočet nerovnic  -> Dovednosti - Řešení nerovnic

Merge map (skills):
    Dovednosti - Vytýkání, krácení + Dovednosti - Roznásobení závorky
        -> Dovednosti - Vytýkání/roznásobení výrazu v závorce
    (úloha s jedním, druhým nebo oběma tagy dostane jeden nový, dedup.)

Cíl aplikace: list-string fieldy `properties`, `skills` a klíče v dict
`knowledge_vector` v tabulce math_tasks.

Idempotentní: druhé spuštění nic nezmění (staré názvy už neexistují).
Transakce: buď vše, nebo nic.

Použití:
    DATABASE_URL=... python scripts/migrate_taxonomy_20260824.py                # dry-run
    DATABASE_URL=... python scripts/migrate_taxonomy_20260824.py --commit
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy.orm.attributes import flag_modified

from database import init_db
from model import MathTask

# ---- Rename mapy ---------------------------------------------------------

# Vlasnosti (překlep) -> Vlastnosti (správně). Aplikuje se na properties.
VLASTNOSTI_RENAME = {
    "Vlasnosti - Lineární":          "Vlastnosti - Lineární",
    "Vlasnosti - Kvadratická":       "Vlastnosti - Kvadratická",
    "Vlasnosti - Mocninná":          "Vlastnosti - Mocninná",
    "Vlasnosti - Odmocninová":       "Vlastnosti - Odmocninová",
    "Vlasnosti - Logaritmická":      "Vlastnosti - Logaritmická",
    "Vlasnosti - Exponenciální":     "Vlastnosti - Exponenciální",
    "Vlasnosti - Absolutní hodnota": "Vlastnosti - Absolutní hodnota",
    "Vlasnosti - Lomená lineární":   "Vlastnosti - Lomená lineární",
    "Vlasnosti - Racionální funkce": "Vlastnosti - Racionální funkce",
    "Vlasnosti - S parametrem":      "Vlastnosti - S parametrem",
}

# Skills rename (Výpočet -> Řešení).
SKILLS_RENAME = {
    "Dovednosti - Výpočet rovnic":   "Dovednosti - Řešení rovnic",
    "Dovednosti - Výpočet nerovnic": "Dovednosti - Řešení nerovnic",
}

# Skills merge: obě staré -> jedna nová.
SKILLS_MERGE_INPUTS = {
    "Dovednosti - Vytýkání, krácení",
    "Dovednosti - Roznásobení závorky",
}
SKILLS_MERGE_OUTPUT = "Dovednosti - Vytýkání/roznásobení výrazu v závorce"


def rename_list(lst, rename_map):
    """Aplikuje 1:1 rename na list-stringů, zachová pořadí a dedup."""
    if not isinstance(lst, list):
        return lst, False
    changed = False
    out = []
    seen = set()
    for x in lst:
        y = rename_map.get(x, x)
        if y != x:
            changed = True
        if y not in seen:
            seen.add(y)
            out.append(y)
    return out, changed


def merge_list(lst, inputs, output):
    """Nahradí libovolné z `inputs` v listu za `output`, dedup."""
    if not isinstance(lst, list):
        return lst, False
    if not any(x in inputs for x in lst):
        return lst, False
    out = []
    seen = set()
    merged_added = False
    for x in lst:
        if x in inputs:
            if not merged_added:
                if output not in seen:
                    out.append(output); seen.add(output); merged_added = True
        else:
            if x not in seen:
                out.append(x); seen.add(x)
    # Pokud byl inputs, ale merged_added zůstal False (output už tam byl), dedup ho odstraníme
    if not merged_added and output not in seen:
        out.append(output)
    return out, True


def rename_dict_keys(d, rename_map, merge_inputs=None, merge_output=None):
    """Přepíše klíče v dictu. Při konfliktu (obě verze existují) vezme max.
    Volitelně sloučí merge_inputs -> merge_output (agregace max)."""
    if not isinstance(d, dict):
        return d, False
    changed = False
    out = {}
    for k, v in d.items():
        new_k = rename_map.get(k, k)
        if merge_inputs and k in merge_inputs:
            new_k = merge_output
        if new_k != k:
            changed = True
        if new_k in out:
            try:
                out[new_k] = max(out[new_k], v)
            except TypeError:
                out[new_k] = v
        else:
            out[new_k] = v
    return out, changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true", help="Zapiš do DB, jinak dry-run.")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"))
    args = parser.parse_args()

    if not args.db_url:
        print("Chyba: DATABASE_URL.", file=sys.stderr)
        return 2

    SessionLocal = init_db(args.db_url)
    sess = SessionLocal()

    stats = {
        "properties_renamed_rows": 0,
        "skills_renamed_rows": 0,
        "skills_merged_rows":  0,
        "kv_changed_rows":     0,
        "total_rows":          0,
    }

    all_kv_keys_map = {**VLASTNOSTI_RENAME, **SKILLS_RENAME}

    try:
        tasks = sess.query(MathTask).all()
        stats["total_rows"] = len(tasks)

        for t in tasks:
            row_touched_props = False
            row_touched_skills = False
            row_touched_kv = False

            # properties: rename Vlasnosti -> Vlastnosti
            if isinstance(t.properties, list):
                new_props, changed = rename_list(t.properties, VLASTNOSTI_RENAME)
                if changed:
                    t.properties = new_props
                    row_touched_props = True

            # skills: rename Výpočet -> Řešení
            if isinstance(t.skills, list):
                new_skills, changed = rename_list(t.skills, SKILLS_RENAME)
                if changed:
                    t.skills = new_skills
                    row_touched_skills = True

                # skills: merge Vytýkání+Roznásobení -> Vytýkání/roznásobení
                new_skills2, merged = merge_list(t.skills, SKILLS_MERGE_INPUTS, SKILLS_MERGE_OUTPUT)
                if merged:
                    t.skills = new_skills2
                    row_touched_skills = True
                    stats["skills_merged_rows"] += 1

            # knowledge_vector: rename klíčů (vlastnosti + skills) + merge
            if isinstance(t.knowledge_vector, dict):
                new_kv, changed = rename_dict_keys(
                    t.knowledge_vector,
                    all_kv_keys_map,
                    merge_inputs=SKILLS_MERGE_INPUTS,
                    merge_output=SKILLS_MERGE_OUTPUT,
                )
                if changed:
                    t.knowledge_vector = new_kv
                    row_touched_kv = True

            if row_touched_props:
                stats["properties_renamed_rows"] += 1
                if args.commit:
                    flag_modified(t, "properties")
            if row_touched_skills:
                stats["skills_renamed_rows"] += 1
                if args.commit:
                    flag_modified(t, "skills")
            if row_touched_kv:
                stats["kv_changed_rows"] += 1
                if args.commit:
                    flag_modified(t, "knowledge_vector")

        print("=" * 60)
        print(f"Celkem úloh:                     {stats['total_rows']}")
        print(f"Řádků s rename properties:        {stats['properties_renamed_rows']}")
        print(f"Řádků s rename skills (Výpočet):  {stats['skills_renamed_rows']}")
        print(f"Řádků s merge skills (Vyt+Rozn):  {stats['skills_merged_rows']}")
        print(f"Řádků s změnou knowledge_vector:  {stats['kv_changed_rows']}")
        print("=" * 60)

        if args.commit:
            sess.commit()
            print("✓ COMMIT proveden.")
        else:
            sess.rollback()
            print("(DRY-RUN — nic se nezapsalo. Pro zápis přidej --commit.)")
        return 0
    except Exception as e:
        sess.rollback()
        print(f"CHYBA: {e}", file=sys.stderr)
        raise
    finally:
        sess.close()


if __name__ == "__main__":
    sys.exit(main())
