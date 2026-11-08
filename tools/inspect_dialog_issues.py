import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/placeholder_audit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

dialog_issues = [d for d in data if 'Dialog' in d['file']]
for d in dialog_issues:
    fn = d['file'].split('/')[-1]
    print(f"{fn} [{d['sheet']}] r{d['row']}:")
    print(f"  Missing: {d['missing']} | Extra: {d['extra']}")
    print(f"  EN: {repr(d['en'])}")
    print(f"  IT: {repr(d['it'])}")
    print("-" * 50)
