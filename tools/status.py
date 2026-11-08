"""
Elin Italian Translation - Status & Progress Reporter
Calcola le statistiche dettagliate di avanzamento della traduzione italiana:
- Totale voci traducibili
- Voci tradotte in italiano vs voci in fallback inglese
- Avanzamento per categoria (UI/Sistema, Gameplay, Dialoghi, Testi/Libri, Dati)
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LANG_IT_DIR = os.path.join(MOD_DIR, 'Lang', 'IT')

def analyze_excel_file(path):
    try:
        wb = openpyxl.load_workbook(path, data_only=True)
    except Exception as e:
        return 0, 0

    total = 0
    translated = 0

    for sname in wb.sheetnames:
        ws = wb[sname]
        headers = {}
        for c in range(1, ws.max_column + 1):
            val = ws.cell(row=1, column=c).value
            if val:
                headers[str(val).strip()] = c

        # Trova colonne target e _EN
        pairs = []
        for h, c_idx in headers.items():
            en_k = f"{h}_EN"
            if en_k in headers:
                pairs.append((c_idx, headers[en_k]))
        
        # Se non ci sono coppie col/col_EN ma c'e' 'text' e 'text_EN'
        if not pairs and 'text' in headers and 'text_EN' in headers:
            pairs.append((headers['text'], headers['text_EN']))

        if not pairs:
            continue

        for r in range(2, ws.max_row + 1):
            for target_col, en_col in pairs:
                target_val = ws.cell(row=r, column=target_col).value
                en_val = ws.cell(row=r, column=en_col).value

                if en_val is not None and str(en_val).strip() != '':
                    total += 1
                    if target_val is not None:
                        t_str = str(target_val).strip()
                        en_str = str(en_val).strip()
                        # Considerato tradotto se diverso dall'inglese e non vuoto
                        if t_str != '' and t_str != en_str:
                            translated += 1

    return total, translated

def run_status():
    print("=" * 65)
    print("  STATO AVANZAMENTO TRADUZIONE ITALIANA - ELIN")
    print("=" * 65)

    categories = {
        "UI & Sistema (General, Game, Calc)": [
            os.path.join(LANG_IT_DIR, 'Game', 'General.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Game.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Calc.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'HomeResource.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'List.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Word.xlsx'),
        ],
        "Personaggi, Razze & Classi": [
            os.path.join(LANG_IT_DIR, 'Game', 'Chara.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Race.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Job.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Hobby.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Person.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'CharaText.xlsx'),
        ],
        "Statistiche, Abilita' & Elementi": [
            os.path.join(LANG_IT_DIR, 'Game', 'Stat.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Element.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Tactics.xlsx'),
        ],
        "Oggetti, Materiali & Equipaggiamento": [
            os.path.join(LANG_IT_DIR, 'Game', 'Thing.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'ThingV.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Category.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Material.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Food.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Collectible.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'KeyItem.xlsx'),
        ],
        "Mondo, Zone & Costruzione": [
            os.path.join(LANG_IT_DIR, 'Game', 'Area.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Zone.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'ZoneAffix.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Quest.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Faction.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Religion.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Block.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Floor.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Obj.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Deco.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'GlobalTile.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'CellEffect.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Note.xlsx'),
            os.path.join(LANG_IT_DIR, 'Game', 'Research.xlsx'),
        ],
        "Dialoghi Comuni (Dialog)": [
            os.path.join(LANG_IT_DIR, 'Dialog', 'dialog.xlsx')
        ],
    }

    grand_total = 0
    grand_trans = 0

    for cat_name, file_list in categories.items():
        cat_total = 0
        cat_trans = 0
        for f in file_list:
            if os.path.isfile(f):
                tot, tr = analyze_excel_file(f)
                cat_total += tot
                cat_trans += tr

        grand_total += cat_total
        grand_trans += cat_trans
        pct = (cat_trans / cat_total * 100) if cat_total > 0 else 0.0
        print(f"• {cat_name:<42} : {cat_trans:>5} / {cat_total:>5} ({pct:>5.1f}%)")

    # Drama files (tutti i 36 file insieme)
    drama_dir = os.path.join(LANG_IT_DIR, 'Dialog', 'Drama')
    if os.path.isdir(drama_dir):
        drama_total = 0
        drama_trans = 0
        for f in os.listdir(drama_dir):
            if f.endswith('.xlsx'):
                tot, tr = analyze_excel_file(os.path.join(drama_dir, f))
                drama_total += tot
                drama_trans += tr
        grand_total += drama_total
        grand_trans += drama_trans
        pct_drama = (drama_trans / drama_total * 100) if drama_total > 0 else 0.0
        print(f"• {'Dialoghi di Trama (Drama - 36 file)':<42} : {drama_trans:>5} / {drama_total:>5} ({pct_drama:>5.1f}%)")

    # File di testo
    text_dir = os.path.join(LANG_IT_DIR, 'Text')
    text_count = 0
    for r, d, files in os.walk(text_dir):
        for f in files:
            if f.endswith('.txt'):
                text_count += 1
    print(f"• {'File di Testo (Guide, Libri, Pergamene)':<42} : {text_count} file (.txt)")

    print("-" * 65)
    overall_pct = (grand_trans / grand_total * 100) if grand_total > 0 else 0.0
    print(f"TOTALE COMPLESSIVO STRINGHE: {grand_trans:,} / {grand_total:,} ({overall_pct:.2f}%)")
    print("=" * 65)

if __name__ == '__main__':
    run_status()
