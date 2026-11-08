import openpyxl, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

cn_pattern = re.compile(r'[\u4e00-\u9fff]')

files_to_check = [
    'Lang/IT/Game/Chara.xlsx',
    'Lang/IT/Game/Block.xlsx',
    'Lang/IT/Game/Word.xlsx',
    'Lang/IT/Game/CharaText.xlsx',
    'Lang/IT/Dialog/Drama/casino_clerk.xlsx',
    'Lang/IT/Dialog/Drama/farris.xlsx'
]

for fpath in files_to_check:
    wb = openpyxl.load_workbook(fpath, data_only=True)
    for s in wb.sheetnames:
        ws = wb[s]
        headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column + 1)}
        for r in range(2, ws.max_row + 1):
            for h, c in headers.items():
                if not h: continue
                # ONLY target columns, NOT _EN or _JP
                if h.endswith('_EN') or h.endswith('_JP'):
                    continue
                val = ws.cell(row=r, column=c).value
                if val and cn_pattern.search(str(val)):
                    en_val = ws.cell(row=r, column=headers.get(f"{h}_EN", c)).value
                    print(f"{fpath} [{s}] r{r} col '{h}':")
                    print(f"  VAL: {repr(val)}")
                    print(f"  EN : {repr(en_val)}")
                    print("-" * 50)
