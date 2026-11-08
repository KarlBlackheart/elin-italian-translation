"""
Elin Italian Localization - Element.xlsx Core Skills & Masteries Localizer
Localizza accuratamente tutte le abilita' di combattimento, produzione,
magia, resistenze, talenti e capacita' uniche in Element.xlsx.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ELEMENT_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Game', 'Element.xlsx')

SKILLS_MAP = {
    # -------------------------------------------------------------
    # Statistiche di Combattimento & Attributi Base
    # -------------------------------------------------------------
    "85": {"name": "Fede e Pietà", "detail": "Rappresenta la devozione verso la tua divinità e sblocca ricompense e miracoli superiori."},
    "90": {"name": "Colpo Critico", "detail": "Aumenta la probabilità di infliggere colpi devastanti che ignorano parte delle difese nemesi."},
    "91": {"name": "Tranciante Vorpal", "detail": "Capacità di sferrare colpi istantaneamente decapitanti o mortali."},
    "92": {"name": "Penetrazione Armatura", "detail": "Consente agli attacchi di oltrepassare la protezione fisica (PV) del bersaglio."},
    "93": {"name": "Resistenza Anti-Magica", "detail": "Protegge passivamente dagli effetti diretti di ogni forma di incantesimo ostile."},
    "94": {"name": "Danno Globale", "detail": "Aumenta la potenza complessiva di qualsiasi attacco o incantesimo inflitto."},

    # -------------------------------------------------------------
    # Maestrie nelle Armi (Weapon Masteries)
    # -------------------------------------------------------------
    "100": {"name": "Arti Marziali", "detail": "Aumenta l'efficacia del combattimento a mani nude e con armi da mischia orientali."},
    "101": {"name": "Spada Lunga", "detail": "Maestria nell'uso di spade ad una e due mani, sciabole e katane."},
    "102": {"name": "Ascia", "detail": "Aumenta precisione e danno letale con asce da guerra ed esecutori."},
    "103": {"name": "Bastone da Combattimento", "detail": "Migliora l'impiego di bastoni cerimoniali e armi da contusione magica."},
    "104": {"name": "Arco", "detail": "Maestria nel tiro con archi corti, lunghi e composti."},
    "105": {"name": "Arma da Fuoco", "detail": "Migliora l'uso di pistole, moschetti, fucili e armi a proiettili veloci."},
    "106": {"name": "Lancia e Asta", "detail": "Maestria nell'affondo a medio raggio con lance, alabarde e picche."},
    "107": {"name": "Spada Corta e Pugnale", "detail": "Armi rapide e leggere ideali per furtività e colpi critici alle spalle."},
    "108": {"name": "Arma da Lancio", "detail": "Aumenta gittata e letalità di shuriken, coltelli e oggetti scagliati a mano."},
    "109": {"name": "Balestra", "detail": "Migliora penetrazione e potenza con balestre pesanti e leggere."},
    "110": {"name": "Falce da Battaglia", "detail": "Maestria nel mietere le anime dei nemici con ampi fendenti di falce."},
    "111": {"name": "Mazza e Maglio", "detail": "Armi contundenti ideali per frantumare armature pesanti e stordire i nemici."},

    # -------------------------------------------------------------
    # Stili di Difesa & Combattimento
    # -------------------------------------------------------------
    "120": {"name": "Armatura Leggera", "detail": "Aumenta il valore di Schivata (DV) quando si indossano indumenti e armature poco ingombranti."},
    "122": {"name": "Armatura Pesante", "detail": "Aumenta il valore di Protezione (PV) e riduce i danni fisici, sacrificando agilità."},
    "123": {"name": "Uso dello Scudo", "detail": "Migliora la probabilità di bloccare completamente gli attacchi con lo scudo imbracciato."},
    "130": {"name": "Impugnatura a Due Mani", "detail": "Aumenta notevolmente la forza d'impatto impugnando un'arma con entrambe le mani."},
    "131": {"name": "Combattimento a Due Armi", "detail": "Consente di maneggiare con letale precisione un'arma per ciascuna mano."},
    "132": {"name": "Tattica Militare", "detail": "Conoscenza dell'arte della guerra che potenzia ogni danno inferto in mischia."},
    "133": {"name": "Tiro di Precisione", "detail": "Aumenta la precisione e la letalità con qualsiasi arma da tiro a distanza."},
    "134": {"name": "Occhio della Mente", "detail": "Intuizione sovrumana che individua i punti deboli vitali nemici, aumentando i colpi critici."},
    "135": {"name": "Strategia Bellica", "detail": "Permette di dirigere la battaglia e impartire ordini efficaci ai compagni d'arme."},
    "150": {"name": "Schivata", "detail": "Riflessi pronti per sfuggire agilmente agli attacchi in arrivo."},
    "151": {"name": "Schivata Superiore", "detail": "Capacità prodigiosa di prevedere la traiettoria dei colpi nemici e sottrarsi al danno."},
    "152": {"name": "Furtività", "detail": "Muoversi senza farsi notare né udire, cogliendo i nemici alla sprovvista."},

    # -------------------------------------------------------------
    # Sopravvivenza & Avventura
    # -------------------------------------------------------------
    "200": {"name": "Nuoto", "detail": "Capacità di muoversi in acque profonde senza affogare."},
    "207": {"name": "Sollevamento Pesi", "detail": "Aumenta drasticamente il carico massimo trasportabile nello zaino senza affaticarsi."},
    "210": {"name": "Vista Acuta / Esplorazione", "detail": "Permette di notare passaggi segreti, botole nascoste e trappole sotterranee."},
    "220": {"name": "Attività Mineraria", "detail": "Capacità di scavare pareti rocciose per estrarre metalli, minerali preziosi e gemme."},
    "225": {"name": "Disboscamento", "detail": "Abilità nell'abbattere alberi ed estrarre legname pregiato."},
    "226": {"name": "Equitazione", "detail": "Capacità di cavalcare compagni e destrieri mantenendo la stabilità in battaglia."},
    "227": {"name": "Simbiosi", "detail": "Fusione armonica con un compagno cavalcato o parassita che potenzia entrambi."},
    "230": {"name": "Scavo e Modellazione", "detail": "Capacità di scavare buche, trincee e spianare il suolo per la costruzione."},
    "235": {"name": "Mungitura", "detail": "Abilità nel mungere latte nutriente da bestiame e creature consenzienti."},
    "237": {"name": "Addomesticamento", "detail": "Capacità di calmare, strigliare e addestrare creature selvatiche per farne alleati."},
    "240": {"name": "Viaggio ed Esplorazione", "detail": "Riduce la fatica e la fame durante le lunghe traversate sulla mappa del mondo."},
    "241": {"name": "Esecuzione Musicale", "detail": "Suonare strumenti per intrattenere gli avventori nelle taverne... o scatenare lanci di sassi!"},
    "242": {"name": "Scalata", "detail": "Abilità nell'arrampicarsi su pareti scoscese, montagne e ripidi dislivelli."},
    "245": {"name": "Pesca", "detail": "Pazienza e destrezza nel pescare pesci pregiati e tesori sommersi da fiumi e mari."},
    "250": {"name": "Raccolta di Risorse", "detail": "Capacità di raccogliere erbe officinali, semi, funghi e materiali naturali intatti."},

    # -------------------------------------------------------------
    # Artigianato & Lavorazione
    # -------------------------------------------------------------
    "255": {"name": "Falegnameria", "detail": "Lavorazione del legno per costruire mobili resistenti, porte e archi."},
    "256": {"name": "Forgiatura e Fabbro", "detail": "Arte di forgiare metalli per creare armature robuste, armi letali e lingotti."},
    "257": {"name": "Alchimia", "detail": "Distillare erbe e catalizzatori per creare pozioni miracolose ed elisir rari."},
    "258": {"name": "Scultura d'Arte", "detail": "Scolpire pietra e marmo per realizzare statue, decorazioni e monumenti."},
    "259": {"name": "Oreficeria", "detail": "Tagliare gemme grezze e creare anelli, amuleti e gioielli incantati."},
    "260": {"name": "Tessitura e Sartoria", "detail": "Filare e cucire abiti leggeri, mantelli protettivi e stoffe pregiate."},
    "261": {"name": "Fabbricazione Artigianale", "detail": "Competenza generale nella creazione di arredi e strumenti di uso comune."},
    "280": {"name": "Scassinamento", "detail": "Uso dei grimaldelli per aprire forzieri blindati e porte sprangate senza chiave."},
    "281": {"name": "Borseggio", "detail": "Sottrarre monete e oggetti dalle tasche dei viandanti senza essere scoperti."},
    "285": {"name": "Alfabetizzazione e Studio", "detail": "Comprendere e decifrare tomi antichi, pergamene magiche e grimori complessi."},
    "286": {"name": "Agricoltura", "detail": "Semina, irrigazione e cura delle colture per massimizzare la resa dei campi."},
    "287": {"name": "Cucina", "detail": "Preparare piatti deliziosi che conferiscono bonus nutritivi e incrementi di attributo."},
    "288": {"name": "Edilizia e Costruzione", "detail": "Progettare e innalzare solide strutture abitative, officine e mura."},
    "289": {"name": "Perizia e Valutazione", "detail": "Riconoscere il valore e le proprietà magiche occulte degli oggetti trovati."},
    "290": {"name": "Anatomia", "detail": "Studio del corpo biologico per massimizzare il raccolto di carne e resti mostruosi."},
    "291": {"name": "Negoziazione", "detail": "Arte del commercio per ottenere sconti vantaggiosi e vendere al miglior prezzo."},
    "292": {"name": "Investimento", "detail": "Finanziare negozi e attività per migliorarne la selezione di merci in vendita."},
    "293": {"name": "Disinnesco Trappole", "detail": "Neutralizzare trappole pericolose prima che scattino sotto i piedi."},

    # -------------------------------------------------------------
    # Magia & Conoscenza Arcana
    # -------------------------------------------------------------
    "300": {"name": "Rigenerazione Naturale", "detail": "Aumenta la velocità passiva con cui il corpo recupera punti ferita (HP)."},
    "301": {"name": "Meditazione Arcana", "detail": "Concentrazione mentale che accelera il recupero naturale dei punti mana (MP)."},
    "302": {"name": "Controllo Magico", "detail": "Permette di scatenare incantesimi ad area senza colpire o ferire gli alleati."},
    "303": {"name": "Capacità di Mana", "detail": "Rafforza il canale energetico, riducendo il rischio di morte per sovraccarico di mana."},
    "304": {"name": "Incantamento", "detail": "Pronunciare formule magiche fluide e stabili, riducendo la probabilità di fallimento."},
    "305": {"name": "Dispositivi Magici", "detail": "Attivare con perizia bacchette, verghe e manufatti magici consumabili."},
    "306": {"name": "Fede e Devozione", "detail": "Profondità del legame spirituale con la propria divinità patrona."},
    "307": {"name": "Memorizzazione", "detail": "Capacità mnemonica di conservare scorte di incantesimi apprese dai grimori."},

    # -------------------------------------------------------------
    # Talenti & Proprietà Speciali
    # -------------------------------------------------------------
    "400": {"name": "Interdizione al Teletrasporto", "detail": "Impedisce il teletrasporto forzato o accidentale."},
    "401": {"name": "Levitazione", "detail": "Permette di fluttuare nell'aria, evitando trappole a pressione e pavimenti liquidi."},
    "402": {"name": "Raggio di Esplorazione", "detail": "Estende il campo visivo utile per individuare oggetti e creature attorno a sé."},
    "403": {"name": "Apprendimento Rapido", "detail": "Accelera l'acquisizione di esperienza generale e padronanza delle abilità."},
    "404": {"name": "Alleggerimento del Carico", "detail": "Riduce il peso percepito degli oggetti trasportati nello zaino."},
    "405": {"name": "Conservazione Alimenti", "detail": "Rallenta sensibilmente la decomposizione dei cibi per deperimento naturale."},
    "406": {"name": "Resistenza alle Mutazioni", "detail": "Protegge da mutazioni casuali o corruzioni corporali nocive."},
    "407": {"name": "Passo Celere nei Viaggi", "detail": "Aumenta la velocità di spostamento sulla mappa del mondo aperto."},
    "408": {"name": "Protezione dalle Intemperie", "detail": "Riduce le penalità provocate da bufere, piogge torrenziali e maltempo."},
    "409": {"name": "Acceleratore di Etere", "detail": "Accelera le trasformazioni e l'accumulo di energia da Etere."},
    "410": {"name": "Ritorno Boomerang", "detail": "Consente alle armi da lancio di ritornare magicamente nella mano dell'utilizzatore."},
    "411": {"name": "Amplificazione Magica", "detail": "Potenzia l'intensità e la durata di tutti gli incantesimi lanciati."},
    "412": {"name": "Barriera Rallenta-Etere", "detail": "Rallenta la velocità con cui il Morbo dell'Etere corrompe il corpo."},
    "414": {"name": "Onniveggenza", "detail": "Permette di scorgere la vera natura di ogni cosa celata o invisibile."},
    "415": {"name": "Invisibilità", "detail": "Rende il corpo invisibile alla vista ordinaria di nemici e guardie."},
    "416": {"name": "Vista dell'Invisibile", "detail": "Consente di vedere nitidamente mostri e creature ammantate di invisibilità."},
}

def apply():
    print(f"Caricamento di {ELEMENT_FILE}...")
    wb = openpyxl.load_workbook(ELEMENT_FILE)
    ws = wb.active

    headers = {}
    for c in range(1, ws.max_column + 1):
        v = ws.cell(row=1, column=c).value
        if v:
            headers[str(v).strip()] = c

    id_c = headers.get('id', 1)
    name_c = headers.get('name', 4)
    detail_c = headers.get('detail', 6)

    translated = 0
    for r in range(2, ws.max_row + 1):
        rid = ws.cell(row=r, column=id_c).value
        if rid:
            rid_str = str(rid).strip()
            if rid_str in SKILLS_MAP:
                entry = SKILLS_MAP[rid_str]
                ws.cell(row=r, column=name_c, value=entry['name'])
                ws.cell(row=r, column=detail_c, value=entry['detail'])
                translated += 1

    wb.save(ELEMENT_FILE)
    print(f"[OK] Applicate {translated} abilità e maestrie approfondite a Element.xlsx!")

if __name__ == '__main__':
    apply()
