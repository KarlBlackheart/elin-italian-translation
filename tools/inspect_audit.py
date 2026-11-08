import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/placeholder_audit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")

# Group by category of missing/extra
for item in data[:35]:
    fn = item['file'].split('/')[-1]
    print(f"{fn} [{item['sheet']}] r{item['row']}: Missing={item['missing']} Extra={item['extra']}")
    print(f"   EN: {item['en']}")
    print(f"   IT: {item['it']}")
    print("-" * 60)
