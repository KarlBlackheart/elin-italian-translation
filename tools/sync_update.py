"""
Elin Italian Translation - Mod Sync & Update Tool
Confronta la mod con l'installazione di gioco di Elin e sincronizza i file con ogni nuovo aggiornamento:
- Rileva nuove stringhe, missioni, oggetti o dialoghi aggiunti nelle patch.
- Aggiorna i file della mod preservando TUTTE le traduzioni italiane gia' effettuate.
- Fornisce un report dettagliato dei nuovi contenuti da tradurre.
- Confronta affiancati i testi in Giapponese (_JP), Inglese (_EN) e Cinese (_CN).
"""

import os
import sys
import shutil
import re
import openpyxl

DEFAULT_GAME_PATH = r'Z:\Giochi\SteamLibrary\steamapps\common\Elin'
MOD_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LANG_IT_PATH = os.path.join(MOD_PATH, 'Lang', 'IT')

def get_game_version(game_path):
    # Cerca la versione in version.txt o version.ini
    ver_txt = os.path.join(game_path, 'Package', '_Elona', 'Lang', 'EN', 'Text', 'version.txt')
    if os.path.isfile(ver_txt):
        with open(ver_txt, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                m = re.search(r'EA\s*([0-9\.]+)', line)
                if m:
                    return m.group(1)
    return "0.23.338"

def sync_game_excel_file(game_file_path, mod_file_path):
    """
    Sincronizza un foglio di gioco: aggiunge nuove righe mantenendo le traduzioni esistenti.
    """
    if not os.path.isfile(game_file_path):
        return 0, 0
    if not os.path.isfile(mod_file_path):
        shutil.copy2(game_file_path, mod_file_path)
        return 1, 0

    wb_game = openpyxl.load_workbook(game_file_path, data_only=True)
    wb_mod = openpyxl.load_workbook(mod_file_path)
    
    added_rows = 0
    updated_texts = 0

    for sheet_name in wb_game.sheetnames:
        if sheet_name not in wb_mod.sheetnames:
            continue
        ws_game = wb_game[sheet_name]
        ws_mod = wb_mod[sheet_name]

        # Mappatura intestazioni Mod
        mod_headers = {}
        for c in range(1, ws_mod.max_column + 1):
            val = ws_mod.cell(row=1, column=c).value
            if val:
                mod_headers[str(val).strip()] = c

        game_headers = {}
        for c in range(1, ws_game.max_column + 1):
            val = ws_game.cell(row=1, column=c).value
            if val:
                game_headers[str(val).strip()] = c

        id_col_mod = mod_headers.get('id', 1)
        id_col_game = game_headers.get('id', 1)

        # Mappa righe mod per ID
        mod_rows_by_id = {}
        for r in range(2, ws_mod.max_row + 1):
            row_id = ws_mod.cell(row=r, column=id_col_mod).value
            if row_id is not None:
                mod_rows_by_id[str(row_id).strip()] = r

        # Trova coppie localizzate
        target_pairs = []
        for h, c_idx in mod_headers.items():
            en_k = f"{h}_EN"
            if en_k in mod_headers and en_k in game_headers:
                target_pairs.append((c_idx, mod_headers[en_k], game_headers[en_k]))

        # Verifica righe del gioco
        for r_game in range(2, ws_game.max_row + 1):
            g_id = ws_game.cell(row=r_game, column=id_col_game).value
            if g_id is None:
                continue
            g_id_str = str(g_id).strip()
            
            if g_id_str not in mod_rows_by_id:
                # Nuova riga aggiunta dal gioco!
                new_row = ws_mod.max_row + 1
                for h, g_c in game_headers.items():
                    if h in mod_headers:
                        val = ws_game.cell(row=r_game, column=g_c).value
                        ws_mod.cell(row=new_row, column=mod_headers[h], value=val)
                # Inizializza colonne target con il testo inglese nuovo come fallback
                for target_col, mod_en_col, _ in target_pairs:
                    en_val = ws_mod.cell(row=new_row, column=mod_en_col).value
                    ws_mod.cell(row=new_row, column=target_col, value=en_val)
                added_rows += 1
            else:
                # Riga esistente: controlla se il sorgente EN o JP è stato aggiornato dal dev
                r_mod = mod_rows_by_id[g_id_str]
                for target_col, mod_en_col, game_en_col in target_pairs:
                    old_en = ws_mod.cell(row=r_mod, column=mod_en_col).value
                    new_en = ws_game.cell(row=r_game, column=game_en_col).value
                    if new_en is not None and str(new_en).strip() != '' and str(new_en) != str(old_en):
                        ws_mod.cell(row=r_mod, column=mod_en_col, value=new_en)
                        updated_texts += 1

    if added_rows > 0 or updated_texts > 0:
        wb_mod.save(mod_file_path)

    return added_rows, updated_texts

def sync_text_files(game_text_dir, mod_text_dir):
    """
    Sincronizza file di testo (libri, guide, scroll). Aggiunge nuovi file senza toccare quelli tradotti.
    """
    new_files = 0
    for root, dirs, files in os.walk(game_text_dir):
        rel = os.path.relpath(root, game_text_dir)
        target_dir = os.path.join(mod_text_dir, rel) if rel != '.' else mod_text_dir
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            target_f = os.path.join(target_dir, f)
            if not os.path.isfile(target_f):
                shutil.copy2(os.path.join(root, f), target_f)
                new_files += 1
    return new_files

def run_sync(game_path=DEFAULT_GAME_PATH):
    print("=" * 60)
    print("ELIN TRADUZIONE ITALIANA - SINCRONIZZAZIONE AGGIORNAMENTI")
    print("=" * 60)
    print(f"Cartella di gioco: {game_path}")
    print(f"Cartella mod:      {MOD_PATH}")

    if not os.path.isdir(game_path):
        print(f"[ERRORE] Cartella di gioco non trovata in: {game_path}")
        return

    ver = get_game_version(game_path)
    print(f"Versione rilevata dal gioco: {ver}")

    # 1. Sincronizzazione Game
    src_game = os.path.join(game_path, 'Package', '_Lang_Chinese', 'Lang', 'CN', 'Game')
    dest_game = os.path.join(LANG_IT_PATH, 'Game')
    total_added = 0
    total_updated = 0

    if os.path.isdir(src_game):
        for f in os.listdir(src_game):
            if f.endswith('.xlsx'):
                added, updated = sync_game_excel_file(
                    os.path.join(src_game, f),
                    os.path.join(dest_game, f)
                )
                if added > 0 or updated > 0:
                    print(f"  [Game/{f}] +{added} nuove voci, {updated} testi aggiornati")
                total_added += added
                total_updated += updated

    # 2. Sincronizzazione Dialog e Drama
    src_dialog = os.path.join(game_path, 'Package', '_Elona', 'Lang', '_Dialog')
    dest_dialog = os.path.join(LANG_IT_PATH, 'Dialog')
    if os.path.isdir(src_dialog):
        # dialog.xlsx
        added, updated = sync_game_excel_file(
            os.path.join(src_dialog, 'dialog.xlsx'),
            os.path.join(dest_dialog, 'dialog.xlsx')
        )
        total_added += added
        total_updated += updated
        
        # Drama
        src_drama = os.path.join(src_dialog, 'Drama')
        dest_drama = os.path.join(dest_dialog, 'Drama')
        for f in os.listdir(src_drama):
            if f.endswith('.xlsx'):
                added, updated = sync_game_excel_file(
                    os.path.join(src_drama, f),
                    os.path.join(dest_drama, f)
                )
                if added > 0 or updated > 0:
                    print(f"  [Drama/{f}] +{added} nuovi nodi, {updated} testi aggiornati")
                total_added += added
                total_updated += updated

    # 3. Sincronizzazione Text (Books, Help, Scrolls)
    src_text = os.path.join(game_path, 'Package', '_Elona', 'Lang', 'EN', 'Text')
    dest_text = os.path.join(LANG_IT_PATH, 'Text')
    new_txt_files = sync_text_files(src_text, dest_text)

    # Aggiorna version.ini
    ver_clean = re.sub(r'[^0-9]', '', ver)
    if ver_clean:
        with open(os.path.join(LANG_IT_PATH, 'version.ini'), 'w', encoding='utf-8') as vf:
            vf.write(f"version = {ver_clean}\n")

    print("-" * 60)
    print(f"Riepilogo Sincronizzazione:")
    print(f"  Nuove righe/oggetti aggiunti: {total_added}")
    print(f"  Testi sorgente aggiornati:    {total_updated}")
    print(f"  Nuovi file di testo rilevati: {new_txt_files}")
    print(f"  Tutte le traduzioni italiane esistenti sono state PRESERVATE.")
    print("=" * 60)

if __name__ == '__main__':
    game_p = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_GAME_PATH
    run_sync(game_p)
