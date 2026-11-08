import glob, openpyxl, re, sys
sys.stdout.reconfigure(encoding='utf-8')

print("Scanning for potential false friends...")

false_friends = [
    (r'\battualmente\b', 'attualmente (check if meant actually)'),
    (r'\beventualmente\b', 'eventualmente (check if meant eventually)'),
    (r'\bmagazzino\b', 'magazzino (check if meant magazine/journal)'),
    (r'\bparente\b', 'parente (check if meant parent/genitore)'),
    (r'\bfabbrica\b', 'fabbrica (check if meant fabric/tessuto)'),
    (r'\blibreria\b', 'libreria (check if meant library/biblioteca)'),
    (r'\blitigio\b', 'litigio (check if meant crossbow quarrel/dardo)')
]

hits = []

# Check text files
for txt in glob.glob('Lang/IT/**/*.txt', recursive=True):
    with open(txt, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        for pat, desc in false_friends:
            if re.search(pat, line, re.IGNORECASE):
                hits.append((txt, idx+1, desc, line.strip()))

# Check excel files
for x in glob.glob('Lang/IT/**/*.xlsx', recursive=True):
    if 'Backer' in x: continue
    try: wb = openpyxl.load_workbook(x, data_only=True)
    except: continue
    for s in wb.sheetnames:
        ws = wb[s]
        for r in range(2, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                val = ws.cell(row=r, column=c).value
                if val:
                    s_val = str(val)
                    for pat, desc in false_friends:
                        if re.search(pat, s_val, re.IGNORECASE):
                            hits.append((f"{x} [{s}] r{r}", c, desc, s_val))

print(f"Total potential false friend matches: {len(hits)}")
for h in hits:
    print(f"{h[0]}: {h[2]}")
    print(f"   Context: {repr(h[3][:100])}")
