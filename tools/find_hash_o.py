import glob, openpyxl, sys
sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob('Lang/IT/**/*.xlsx', recursive=True)
total_o = []
for f in files:
    try: wb = openpyxl.load_workbook(f, data_only=True)
    except: continue
    for s in wb.sheetnames:
        ws = wb[s]
        for r in range(2, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                v = ws.cell(row=r, column=c).value
                if v and '#o' in str(v):
                    fn = f.replace('\\', '/')
                    total_o.append((fn, s, r, c, str(v)))

print(f"Total #o occurrences: {len(total_o)}")
for fn, s, r, c, v in total_o:
    print(f"{fn} [{s}] r{r} col {c}: {repr(v)}")
