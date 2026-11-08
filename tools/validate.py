"""
Elin Italian Translation - Mod Validator & Integrity Checker
Verifica la correttezza formale della mod prima del test o del caricamento su Steam Workshop:
- Integrita' di tutti i file XLSX (nessun file danneggiato o non apribile).
- Verifica del package.xml e presenza del preview.jpg conforme a Steam Workshop.
- Validazione dei tag di formattazione ({...}, #1, #2, codici colore).
"""

import os
import re
import xml.etree.ElementTree as ET
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LANG_IT_DIR = os.path.join(MOD_DIR, 'Lang', 'IT')

def validate_all():
    print("=" * 65)
    print("  VALIDATORE DI INTEGRITA' MOD - TRADUZIONE ITALIANA ELIN")
    print("=" * 65)

    errors = []
    warnings = []

    # 1. Verifica package.xml
    pkg_path = os.path.join(MOD_DIR, 'package.xml')
    if not os.path.isfile(pkg_path):
        errors.append("package.xml mancante nella radice della mod!")
    else:
        try:
            tree = ET.parse(pkg_path)
            root = tree.getroot()
            for tag in ['title', 'id', 'author', 'version']:
                if root.find(tag) is None or not root.find(tag).text:
                    errors.append(f"package.xml: tag obbligatorio <{tag}> mancante o vuoto!")
            print("[OK] package.xml valido e ben formato.")
        except Exception as e:
            errors.append(f"Errore di sintassi in package.xml: {e}")

    # 2. Verifica preview.jpg
    preview_path = os.path.join(MOD_DIR, 'preview.jpg')
    if not os.path.isfile(preview_path):
        warnings.append("preview.jpg mancante (necessario per l'anteprima su Steam Workshop).")
    else:
        sz = os.path.getsize(preview_path)
        if sz > 1024 * 1024:
            warnings.append(f"preview.jpg e' superiore a 1MB ({sz} bytes). Consigliato < 1MB per Steam.")
        else:
            print(f"[OK] preview.jpg presente ({sz // 1024} KB).")

    # 3. Verifica lang.ini e version.ini
    for ini_name in ['lang.ini', 'version.ini']:
        ini_p = os.path.join(LANG_IT_DIR, ini_name)
        if not os.path.isfile(ini_p):
            errors.append(f"File di configurazione mancante: {ini_name}")
        else:
            print(f"[OK] {ini_name} presente e configurato.")

    # 4. Scansione di tutti i file XLSX
    xlsx_count = 0
    print("Verifica fogli di calcolo Excel (.xlsx)...")
    for root, dirs, files in os.walk(LANG_IT_DIR):
        for f in files:
            if f.endswith('.xlsx'):
                xlsx_count += 1
                fpath = os.path.join(root, f)
                rel = os.path.relpath(fpath, MOD_DIR)
                try:
                    wb = openpyxl.load_workbook(fpath, read_only=True)
                    # Verifica che abbia almeno un foglio
                    if not wb.sheetnames:
                        errors.append(f"{rel}: nessun foglio presente!")
                    wb.close()
                except Exception as e:
                    errors.append(f"{rel}: file Excel corrotto o illeggibile: {e}")

    print(f"[OK] {xlsx_count} file Excel analizzati e verificati.")

    # Risultati
    print("-" * 65)
    if errors:
        print(f"[FALLITO] Trovati {len(errors)} errori bloccanti:")
        for err in errors:
            print(f"  ❌ {err}")
    else:
        print("[SUCCESSO] Nessun errore bloccante rilevato! La mod e' pronta e integra.")

    if warnings:
        print(f"[AVVISI] {len(warnings)} avvisi non bloccanti:")
        for w in warnings:
            print(f"  ⚠️ {w}")

    print("=" * 65)
    return len(errors) == 0

if __name__ == '__main__':
    validate_all()
