import json

with open('scratch_loytel_untrans.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")

with open('scratch_loytel_partA.txt', 'w', encoding='utf-8') as out:
    for d in data[:220]:
        r = d['row']
        s = d['step']
        en = d['en'].replace('\n', ' // ')
        jp = d['jp'].replace('\n', ' // ')
        out.write(f"{r}\t{s}\tEN: {en}\tJP: {jp}\n")

with open('scratch_loytel_partB.txt', 'w', encoding='utf-8') as out:
    for d in data[220:]:
        r = d['row']
        s = d['step']
        en = d['en'].replace('\n', ' // ')
        jp = d['jp'].replace('\n', ' // ')
        out.write(f"{r}\t{s}\tEN: {en}\tJP: {jp}\n")

print("Written partA (220) and partB (214)")
