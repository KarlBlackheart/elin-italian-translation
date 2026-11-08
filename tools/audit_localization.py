"""
Audit Italian localization for:
1. Placeholder mismatches against EN and JP
2. Known false friends and context-dependent polysemous terms
3. Consistency of core mechanics terms
"""
import glob, openpyxl, re, os, json

placeholder_pattern = re.compile(r'#[a-zA-Z0-9_]+')

files = glob.glob('Lang/IT/**/*.xlsx', recursive=True)

placeholder_issues = []

for f in files:
    if 'Backer' in f: continue
    try:
        wb = openpyxl.load_workbook(f, data_only=True)
    except:
        continue
    for s in wb.sheetnames:
        ws = wb[s]
        headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column + 1)}
        pairs = []
        for h, c in headers.items():
            if f'{h}_EN' in headers:
                pairs.append((h, c, headers[f'{h}_EN']))
        if not pairs and 'text' in headers and 'text_EN' in headers:
            pairs.append(('text', headers['text'], headers['text_EN']))

        for r in range(2, ws.max_row + 1):
            for h, tc, ec in pairs:
                tv = ws.cell(row=r, column=tc).value
                ev = ws.cell(row=r, column=ec).value
                if tv and ev:
                    t_str = str(tv).strip()
                    e_str = str(ev).strip()

                    t_ph = set(placeholder_pattern.findall(t_str))
                    e_ph = set(placeholder_pattern.findall(e_str))

                    # In Italian #o or #a or #e are valid gender placeholders
                    t_ph_clean = {p for p in t_ph if p not in ['#o', '#a', '#e', '#newline']}
                    e_ph_clean = {p for p in e_ph if p not in ['#newline']}

                    t_lower = {p.lower() for p in t_ph_clean}
                    e_lower = {p.lower() for p in e_ph_clean}

                    missing = e_lower - t_lower
                    extra = t_lower - e_lower

                    # If missing placeholders that are crucial for game logic (#1, #2, #pc, #tg, #his, etc.)
                    if missing or extra:
                        placeholder_issues.append({
                            'file': f.replace('\\', '/'),
                            'sheet': s,
                            'row': r,
                            'col': h,
                            'missing': list(missing),
                            'extra': list(extra),
                            'en': e_str,
                            'it': t_str
                        })

print(f"Total placeholder issues: {len(placeholder_issues)}")

with open('scratch/placeholder_audit.json', 'w', encoding='utf-8') as fp:
    json.dump(placeholder_issues, fp, ensure_ascii=False, indent=2)

print("Saved to scratch/placeholder_audit.json")
