"""
Elin Italian Translation - Translation Helper & Batch Processor
Fornisce funzioni per applicare traduzioni a singoli file o gruppi di file,
garantendo il confronto affiancato tra Giapponese (_JP), Inglese (_EN) e Italiano (IT),
e validando la conservazione di tag, placeholder (#1, #2, ecc.) e parametri speciali.
"""

import os
import re
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LANG_IT_DIR = os.path.join(MOD_DIR, 'Lang', 'IT')

def check_placeholders(src_text, trans_text):
    """
    Verifica che i segnaposto numerici (#1, #2...) e i blocchi {...}
    presenti nel testo sorgente siano preservati nella traduzione.
    """
    if not src_text or not trans_text:
        return True, []
    
    warnings = []
    # Segnaposto numerici (#1, #2, etc.)
    src_tags = set(re.findall(r'#[0-9]+', str(src_text)))
    tr_tags = set(re.findall(r'#[0-9]+', str(trans_text)))
    missing = src_tags - tr_tags
    if missing:
        warnings.append(f"Tag mancanti: {', '.join(missing)}")
    extra = tr_tags - src_tags
    if extra:
        warnings.append(f"Tag in eccesso: {', '.join(extra)}")

    # Parentesi graffe non bilanciate
    if str(trans_text).count('{') != str(trans_text).count('}'):
        warnings.append("Parentesi graffe { } sbilanciate")

    return len(warnings) == 0, warnings

def apply_translations_to_sheet(excel_path, translations_dict, id_column='id', target_column='name'):
    """
    Applica un dizionario { id: 'testo italiano' } o { id: { 'col': 'testo' } } a un file Excel.
    """
    if not os.path.isfile(excel_path):
        print(f"File non trovato: {excel_path}")
        return 0

    wb = openpyxl.load_workbook(excel_path)
    applied = 0

    for sname in wb.sheetnames:
        ws = wb[sname]
        headers = {}
        for c in range(1, ws.max_column + 1):
            val = ws.cell(row=1, column=c).value
            if val:
                headers[str(val).strip()] = c

        if id_column not in headers:
            continue

        id_c = headers[id_column]

        for r in range(2, ws.max_row + 1):
            row_id = ws.cell(row=r, column=id_c).value
            if row_id is None:
                continue
            row_id_str = str(row_id).strip()

            if row_id_str in translations_dict:
                val_data = translations_dict[row_id_str]
                if isinstance(val_data, dict):
                    # Traduzione multi-colonna, es: {'name': 'Spada', 'detail': 'Descrizione...'}
                    for col_name, it_text in val_data.items():
                        if col_name in headers:
                            target_c = headers[col_name]
                            en_k = f"{col_name}_EN"
                            src_ref = ws.cell(row=r, column=headers[en_k]).value if en_k in headers else ""
                            ok, warns = check_placeholders(src_ref, it_text)
                            if not ok:
                                print(f"  [ATTENZIONE riga {r} ID '{row_id_str}'] {', '.join(warns)}")
                            ws.cell(row=r, column=target_c, value=it_text)
                            applied += 1
                elif isinstance(val_data, str):
                    # Traduzione a singola colonna predefinita
                    if target_column in headers:
                        target_c = headers[target_column]
                        en_k = f"{target_column}_EN"
                        src_ref = ws.cell(row=r, column=headers[en_k]).value if en_k in headers else ""
                        ok, warns = check_placeholders(src_ref, val_data)
                        if not ok:
                            print(f"  [ATTENZIONE riga {r} ID '{row_id_str}'] {', '.join(warns)}")
                        ws.cell(row=r, column=target_c, value=val_data)
                        applied += 1

    if applied > 0:
        wb.save(excel_path)
    return applied

def export_multilingual_tsv(excel_path, output_tsv_path, id_column='id'):
    """
    Esporta un foglio Excel in formato TSV affiancando:
    ID \t Giapponese (_JP) \t Inglese (_EN) \t Italiano Attuale (Target)
    Ideale per revisione rapida o traduzione assistita.
    """
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    rows_out = []

    for sname in wb.sheetnames:
        ws = wb[sname]
        headers = {}
        for c in range(1, ws.max_column + 1):
            val = ws.cell(row=1, column=c).value
            if val:
                headers[str(val).strip()] = c

        # Trova colonne
        pairs = []
        for h, c_idx in headers.items():
            en_k = f"{h}_EN"
            jp_k = f"{h}_JP"
            if en_k in headers:
                jp_c = headers.get(jp_k, None)
                pairs.append((h, c_idx, headers[en_k], jp_c))

        for r in range(2, ws.max_row + 1):
            r_id = ws.cell(row=r, column=headers.get(id_column, 1)).value or f"row_{r}"
            for col_name, target_c, en_c, jp_c in pairs:
                it_val = ws.cell(row=r, column=target_c).value or ""
                en_val = ws.cell(row=r, column=en_c).value or ""
                jp_val = ws.cell(row=r, column=jp_c).value if jp_c else ""
                rows_out.append(f"{r_id}\t{col_name}\t{jp_val}\t{en_val}\t{it_val}")

    with open(output_tsv_path, 'w', encoding='utf-8') as f:
        f.write("ID\tCAMPO\tGIAPPONESE (Orig)\tINGLESE (Ref)\tITALIANO\n")
        f.write("\n".join(rows_out))
    print(f"Esportato TSV multilingue in: {output_tsv_path} ({len(rows_out)} righe)")
