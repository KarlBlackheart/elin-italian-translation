# coding: utf-8
"""
Elin Italian Localization - Dialog.xlsx Complete Localizer
Translates all remaining dialog lines in sheets: general, zone, unique, and asmr.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DIALOG_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'dialog.xlsx')

DIALOG_TRANSLATIONS = {
    "general": {
        "food1": "Abbiamo calde specialità del giorno che ti aspettano. Per sole #1 oren puoi riempirti la pancia con un pasto prelibato!",
        "food2": "Ecco a te, mangia con gusto e buon appetito!",
        "healer1": "Soffri per le ferite di battaglia o sei afflitto da qualche morbo? Per #1 oren posso guarirti all'istante.",
        "healer2": "Allora resta immobile per un istante. Risanerò il tuo corpo in men che non si dica.",
        "appraise1": "Porti con te oggetti misteriosi o non identificati nello zaino? Per #1 oren posso rivelarne tutti i segreti.",
        "appraise2": "Ecco a te, ora conosci la vera natura e le proprietà di ciò che possiedi.",
        "appraise3": "A quanto pare non hai nulla nello zaino che necessiti di essere periziato.",
        "expand1": "Servono #2 lingotti d'oro per espandere i confini del tuo territorio.",
        "expand2": "Perfetto! I confini del tuo territorio sono stati espansi con successo!",
        "expand3": "Sembra che il tuo territorio non possa essere ulteriormente espanso al momento.",
        "extraTax": "Attualmente il tuo versamento fiscale mensile addizionale verso Mysilia ammonta a #1 oren.",
        "extraTax2": "D'accordo, ho modificato la tua quota di tasse addizionali per Mysilia a #1 oren.",
        "banker1": "Attualmente hai #1 oren custoditi sul tuo conto bancario. Quanto desideri depositare?",
        "banker2": "Attualmente hai #1 oren custoditi sul tuo conto bancario. Quanto desideri prelevare?",
        "banker3": "Molto bene. Il denaro è stato versato e messo al sicuro sul tuo conto.",
        "banker4": "Molto bene. Ecco a te il denaro prelevato dal tuo deposito.",
        "noDrawingRoom": "Non disponi ancora di una sala di ricevimento adeguata per accogliere gli ospiti importanti.",
        "nomoney": "A quanto pare non hai abbastanza denaro per permetterti questo servizio.",
        "alreadyFull": "Sembri già completamente sazio, non riusciresti a mandare giù altro cibo.",
        "questAccept": "Accetti davvero il mio incarico? Meraviglioso, conto sul tuo aiuto!",
        "questFull": "Sembra che tu abbia già troppe incombenze e missioni in sospeso. Concludi quelle prima di accettarne altre.",
        "questInProgress": "Come procedono le cose con la missione che ti ho affidato? Tutto bene?",
        "questComplete": "Oh, vedo che hai portato a termine il mio incarico! Ti ringrazio di cuore. Ecco la tua meritata ricompensa.",
        "bird1": "Oh, adoro osservare gli uccelli librarsi nel cielo!",
        "bird2": "D'accordo, ormai non si torna più indietro! // Avanti, facciamolo!",
        "bird3": "D'accordo tesoro, mi servono #1 oren in anticipo.",
        "blooming1": "Mmh, il tuo compagno sembra decisamente pronto e maturo. Il legame che avete forgiato sprigiona un grande potenziale.",
        "blooming2": "Muwohohohohohoho, SBOCCIA!",
        "blooming3": "Muwohoho. La tua sincera devozione deciderà il mio favore. Deliziami, se ne sei capace.",
        "tail1": "Sei... davvero attraente. Ho deciso di comprarti.",
        "tail2": "D'accordo, non si torna più indietro! // Andiamo!",
        "tail3": "D'accordo tesoro, mi servono #1 oren in anticipo."
    },
    "zone": {
        "mysilia": "Umani ed Elea convivono pacificamente a Mysilia. // Dopo la devastante Guerra dei Dieci Anni, questo luogo è diventato un faro di speranza e fratellanza.",
        "olvina": "Benvenuto a Olvina, il villaggio del vino pregiato, delle sorgenti termali e dei ciliegi in fiore! // Assaggia il nostro vino locale, ha il potere di ristorare il corpo e lo spirito.",
        "lothria": "Lord Cetrus non è più stato visto sorridere da quando Lady Friaune è scomparsa... // Un velo di perpetua malinconia avvolge questo antico feudo.",
        "derphy": "Benvenuto a Derphy, un covo marcio e corrotto di feccia e malfattori. // Guarda sempre dove tieni la borsa, qui una distrazione si paga con la vita.",
        "palmia": "Palmia è una metropoli colossale. Mi perdo continuamente tra i suoi quartieri imponenti! // È la capitale del regno, dove risiedono il re e la regina.",
        "yowyn": "Questo tranquillo villaggio agricolo si chiama Yowyn. // I destrieri allevati qui sono rinomati in tutto il continente per la loro velocità e robustezza.",
        "lumiest": "Lumiest è la nobile città delle arti, della magia arcana e dell'alta cultura. Benvenuto nella capitale del sapere di Ylva.",
        "noyel": "Fa un freddo cane qui a Noyel, il gelo ti gela persino le ossa! Ma la neve che scende sulle case di legno ha un fascino fiabesco.",
        "kapul": "Ah, non c'è profumo più inebriante dell'aria salmastra e della brezza marina nel porto di Port Kapul! // Navi mercantili da ogni angolo del globo approdano qui.",
        "foxtown": "Produciamo molto più riso di quanto ce ne occorra per sfamarci, così vendiamo le eccedenze ai mercanti forestieri.",
        "foxtown_nefu": "Ho sempre una paura tremenda a uscire dal villaggio... Gli umani hanno la brutta abitudine di toccarci le orecchie pelose!",
        "specwing": "Siamo lontani dalle grandi rotte commerciali terrestri, per questo la maggior parte delle merci ci arriva per via aerea.",
        "village_exile": "Un appartenente alla razza #race in questo sperduto villaggio...? // Quale motivo spinge un #race fino a questi confini remoti?"
    },
    "unique": {
        "mimu": "…Pi? // ……Pipi // Pi……… // …Pipo……… // ……Pi……Errore……",
        "mamani": "Un giorno, le macchine domineranno la terra al posto dell'umanità.",
        "mamani2": "Un giorno, le macchine domineranno la terra al posto dell'umanità.",
        "namamani": "Che bizzarro posto è mai questo? // Dèi? Sono solo esseri un po' più potenti e capricciosi della media.",
        "namamani2": "Strano... i miei ricordi sono confusi e frammentati.",
        "keeper_garden": "Tanelorn? Ah, ho già udito qualcuno chiamare questo giardino con quel nome arcano.",
        "erishe": "Ehehe, fratellone, dove sei andato a cacciarti? // Salve, viandante. Ti prego, goditi la quiete di questo luogo.",
        "larnneire": "Oh, conosci anche tu l'antica favola del principe trasformato in bestia?",
        "lomias": "A quanto pare non hai molta familiarità con queste terre selvagge. // Segui i miei consigli se vuoi sopravvivere a lungo a Ylva.",
        "conery": "Vorrei tanto che il mio principe avesse un po' più di prudenza e moderazione...",
        "garokk": "La mia socia Miral e io ci conosciamo fin da quando eravamo due ragazzini spensierati.",
        "gilbert": "Muwahahahaha! ...E tu cosa saresti? // Per Opatos, schiaccerò ogni miserabile insetto che oserà sbarrarmi la strada!",
        "jonan": "Quali affari ti conducono al cospetto della corte di Mysilia? // Io servo la causa con assoluta rettitudine.",
        "lowell": "Cosa ci fa un avventuriero armato da queste parti, eh? // Questo asilo offre rifugio a chi ha smarrito la ragione.",
        "mapMerchant": "Mi chiamo Slan, devoto servitore di Palmia. Al momento mi occupo della vendita di mappe dettagliate delle terre emerse."
    },
    "asmr": {
        "eyth": "…bneep… // …zzzzzz… // …zshh…beep……",
        "jure": "…c-carezza…carezza… // …abbraaaccio… // …abbraaaaaccio… // …ecco qui…fai il bravo… // …shhh…ci sono io con te…",
        "opatos": "…grrr…sgretola…sgretola… // …bruuuum… // …boooom… // …schiaccia…… // …crrrk…",
        "horome": "…va tutto bene…la mamma è qui accanto a te… // …buonanotte…dolce creatura mia…",
        "demitas": "…eheheheh…… // …eheh…… // …eh……eheheh…… // …eheh……eheh…",
        "lulwy": "…oh… è questo ciò che ti piace…? // …che degenerato incurabile… // …ti concederò un po' della mia brezza…",
        "ehekatl": "@3UMIMYAA! // @3Granchio reale! // …strofina… // …fusa fusa… // …lecca… // …miao♪",
        "fox_maid": "…Buongiorno, mio signore… // …Permettetemi di servirvi una tazza di tè caldo… // …Riposate ancora un po' se siete affaticato…"
    }
}

def run():
    wb = openpyxl.load_workbook(DIALOG_FILE)
    
    total_updated = 0
    for sheet_name, trans_map in DIALOG_TRANSLATIONS.items():
        if sheet_name not in wb.sheetnames:
            continue
        ws = wb[sheet_name]
        headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
        
        text_c = headers.get('text', 2)
        id_c = headers.get('id', 1)
        
        sheet_updated = 0
        for r in range(2, ws.max_row + 1):
            id_val = str(ws.cell(r, id_c).value).strip() if ws.cell(r, id_c).value is not None else ""
            if id_val in trans_map:
                ws.cell(r, text_c).value = trans_map[id_val]
                sheet_updated += 1
                total_updated += 1
        print(f"Sheet '{sheet_name}': updated {sheet_updated} dialog entries.")
        
    wb.save(DIALOG_FILE)
    print(f"Dialog.xlsx complete! Total updated: {total_updated}")

if __name__ == "__main__":
    run()
