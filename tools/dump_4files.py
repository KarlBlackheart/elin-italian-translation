import openpyxl, os, json

MOD_DIR = 'd:/Mod/Elin/Lang/IT/Game'

files = ['Religion.xlsx', 'ZoneAffix.xlsx', 'Tactics.xlsx', 'Hobby.xlsx']
out_data = {}

for f in files:
    wb = openpyxl.load_workbook(os.path.join(MOD_DIR, f), data_only=True)
    ws = wb.active
    headers = {str(ws.cell(1, c).value).strip(): c for c in range(1, ws.max_column + 1)}
    
    rows = []
    for r in range(2, ws.max_row + 1):
        item = {'row': r, 'id': ws.cell(r, headers['id']).value}
        for k in ['name', 'name_EN', 'name_JP', 'detail', 'detail_EN', 'detail_JP', 'textBenefit', 'textBenefit_EN', 'textBenefit_JP', 'textType', 'textType_EN', 'textType_JP']:
            if k in headers:
                item[k] = ws.cell(r, headers[k]).value
        rows.append(item)
    out_data[f] = rows

with open('scratch_4files.json', 'w', encoding='utf-8') as out:
    json.dump(out_data, out, ensure_ascii=False, indent=2)

print("Dumped 4 files into scratch_4files.json")
