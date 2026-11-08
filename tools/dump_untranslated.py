import json

with open("scratch_game_untrans.json", encoding="utf-8") as f:
    data = json.load(f)

for chunk_idx in range(6):
    chunk = data[chunk_idx*100 : (chunk_idx+1)*100]
    with open(f"scratch_chunk_{chunk_idx}.txt", "w", encoding="utf-8") as out:
        for d in chunk:
            r = d["row"]
            i = d["id"]
            en = d["en"]
            jp = d["jp"]
            out.write(f"{r}\t{i}\tEN: {en}\tJP: {jp}\n")
    print(f"Chunk {chunk_idx}: {len(chunk)} rows written")
