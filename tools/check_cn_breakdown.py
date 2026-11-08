import glob, openpyxl, re, json

files = glob.glob('Lang/IT/**/*.xlsx', recursive=True)
cn_pattern = re.compile(r'[\u4e00-\u9fff]')

found_cn = {}

for f in files:
    if 'Backer' in f: continue
    try: wb = openpyxl.load_workbook(f, data_only=True)
    except: continue
    for s in wb.sheetnames:
        ws = wb[s]
        headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column + 1)}
        pairs = []
        for h, c in headers.items():
            if f'{h}_EN' in headers: pairs.append((h, c))
        if not pairs and 'text' in headers: pairs.append(('text', headers['text']))
        for r in range(2, ws.max_row + 1):
            for h, tc in pairs:
                tv = ws.cell(row=r, column=tc).value
                if tv and cn_pattern.search(str(tv)):
                    fn = f.replace('\\', '/')
                    key = f"{fn} [{s}] (col {h})"
                    found_cn[key] = found_cn.get(key, 0) + 1

with open('scratch/cn_breakdown.json', 'w', encoding='utf-8') as fp:
    json.dump(found_cn, fp, indent=2, ensure_ascii=False)

print("Breakdown:")
for k, v in sorted(found_cn.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
