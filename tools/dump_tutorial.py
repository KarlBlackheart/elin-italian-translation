import json

with open('scratch_tutorial_untrans.json', encoding='utf-8') as f:
    data = json.load(f)

with open('scratch_tutorial_readable.txt', 'w', encoding='utf-8') as out:
    for d in data:
        r = d['row']
        s = d['step']
        en = d['en'].replace('\n', ' // ')
        jp = d['jp'].replace('\n', ' // ')
        out.write(f"{r}\t{s}\tEN: {en}\tJP: {jp}\n")

print(f"Written {len(data)} lines to scratch_tutorial_readable.txt")
