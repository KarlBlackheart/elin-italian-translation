# coding: utf-8
"""
Elin Italian Localization - Drama Remainders Localizer
Brings the 14 smaller drama files to 100% completion.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DRAMA_DIR = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama')

UPDATES = {
    "guild_doorman.xlsx": {
        20: "Benvenuto alla Gilda dei Ladri, #guild_title #pc... Ti prego, entra pure.",
        21: "Benvenuto alla Gilda dei Maghi, #guild_title #pc... Ti prego, entra pure.",
        22: "Benvenuto alla Gilda dei Guerrieri, #guild_title #pc... Ti prego, entra pure.",
        28: "Parlami della Gilda dei Ladri.",
        29: "Parlami della Gilda dei Maghi.",
        30: "Parlami della Gilda dei Guerrieri.",
        41: (
            "La nostra Gilda dei Ladri, il 'Sudario Notturno', è formata da esperti consumati nelle arti delle ombre.\n\n"
            "Offriamo una vasta gamma di servizi, come la ricettazione di beni rubati, sconti esclusivi nei mercati neri e l'addestramento nelle abilità furtive. Ma per entrare nel Sudario Notturno dovrai superare una prova ardua in cui i ladruncoli comuni falliscono miseramente."
        ),
        42: (
            "La Gilda dei Maghi riunisce gli studiosi più eruditi e raffinati nelle arti arcane.\n\n"
            "Offriamo numerosi vantaggi, come sconti sui tomi di incantesimi, la prenotazione di tomi rari e l'addestramento nelle discipline magiche. L'ammissione alla Gilda dei Maghi richiede soltanto di superare un semplice esame teorico e pratico."
        ),
        43: (
            "La Gilda dei Guerrieri accoglie combattenti veterani ed esperti nell'arte delle armi.\n\n"
            "Offriamo diversi benefici, come prezzi ridotti per l'identificazione e il ripristino dell'equipaggiamento, oltre all'addestramento nelle abilità marziali. Tuttavia, per unirti ai Guerrieri dovrai superare una prova severa che scoraggia la maggior parte delle reclute."
        ),
        49: "Dunque... nutri interesse per la nostra gilda? Noi viviamo e operiamo nell'ombra della società. Prima di farti varcare la soglia, dovrai guadagnarti la nostra fiducia.",
        53: "Sì",
        54: "No",
        60: "In tal caso, ecco la tua prova di ammissione. Una delle richieste più frequenti che riceviamo è lo sterminio di quei fastidiosi Yeek. Persino i nostri guerrieri più temprati ne hanno fin sopra i capelli! Uccidine almeno una ventina, per iniziare. Torna a fare rapporto da me una volta concluso il massacro."
    },
    "corgon.xlsx": {
        8: "(mokyu?)",
        23: "(mokyuu!)",
        25: "Mokyu.",
        26: "Mo, mokyu!",
        27: "...",
        28: "...",
        29: "...",
        32: "...",
        33: "Mokyu!",
        46: "Per test",
        52: "Per test"
    },
    "felmera.xlsx": {
        23: "La perizia di un dipinto antico... be', ammetto che potrebbe stuzzicare la mia curiosità. Nelle opere del passato riesco ancora a percepire quella scintilla che ridesta la passione sopita dell'artista che è in me.",
        28: "Se dovessi scovare vecchi schizzi o bozzetti, portameli pure. Potrei esserti d'aiuto.",
        32: "D'accordo, darò un'occhiata allo schizzo che hai portato con te. Attendi qui, ci vorrà solo un istante.",
        34: "...Mmh, non è affatto male, ma... Sfortunatamente non c'è nulla di particolarmente degno di nota. Se trovi qualche altro vecchio dipinto, mostramelo.",
        39: (
            "...Ma questo è incredibile!\n\n"
            "Sembra l'opera di un pittore rimasto anonimo, eppure... che cos'è questo brivido che mi scuote l'anima?\n\n"
            "Questo... è un capolavoro speciale. Gli assegnerò una numerazione personale. Custodiscilo con cura nel diario che porti con te!"
        ),
        44: (
            "...Ma che meraviglia!\n\n"
            "Dove diavolo sei riuscito a scovare una simile collezione di dipinti così rari?! No, non importa... la mia anima freme di incontenibile emozione!\n\n"
            "Assegnerò io stesso una numerazione a ciascuna di queste opere. Custodiscile come tesori preziosi nel tuo diario."
        ),
        51: "Ti prego di accettare questo dono. Eheh, ripensando a quegli innumerevoli bozzetti anonimi che mi hai mostrato, non ho proprio resistito alla tentazione di immortalarli sulla tela!"
    },
    "guild_clerk.xlsx": {
        25: "Il 'Sudario Notturno' è un rifugio sicuro per i fuorilegge e le anime dell'oltremondo criminale. Qui nessuno verrà mai inquisito per i propri peccati passati. La nostra capogilda è conosciuta come 'Colei che Porta la Notte', e si mormora che nessun vivente abbia mai scorto il suo vero volto.",
        26: "La Gilda dei Maghi dispone di un sistema educativo d'eccellenza che le altre corporazioni possono solo invidiare. Studenti e novizi giungono da ogni angolo di Tyris in cerca di sapere arcano. Il rettore Jorg è un vanitoso snob, per sua stessa ammissione, ma quando si tratta di oro e manovre politiche è un genio senza pari.",
        27: "La Gilda dei Guerrieri è colma di avventurieri fieri della propria possanza fisica. Thorran è un comandante inflessibile, ma non esiterebbe a dichiarare guerra a un intero regno pur di difendere i propri compagni. Grazie a lui, siamo tutti uniti da un legame indissolubile, come una grande famiglia d'arme.",
        28: "La Gilda dei Mercanti tutela i carovanieri e le botteghe, garantendo traffici commerciali sicuri ed equi. Lady Marian può incutere un certo timore all'inizio, ma è una commerciante straordinaria, capace di costruire una fortuna immensa a Tyris nell'arco di una sola generazione.",
        36: "A quanto pare soddisfi tutti i requisiti per il grado successivo. Congratulazioni vivissime per la tua meritata promozione!",
        41: "Purtroppo, al momento non possiamo approvare la tua richiesta di promozione."
    },
    "guild_master_merchant.xlsx": {
        25: "Vediamo un po'... Come prova di ammissione, ti farò distribuire volantini pubblicitari. Comprane una bella scorta dalla nostra impiegata e distribuiscili tra la gente di qualche città.",
        27: (
            "Lascia che ti doni una perla di saggezza, novellino.\n\n"
            "Non distribuire quei volantini con aria timida e dimessa! Piantati con fierezza in mezzo alla calca e lanciali con tutta la passione che ti brucia in corpo!\n\n"
            "E adesso va'! Mostra al mondo intero di che pasta è fatto un vero mercante!"
        ),
        32: (
            "Ma guarda un po', hai distribuito tutti i volantini, eh? A quanto pare il tuo ardore per gli affari è sincero.\n\n"
            "Molto bene! Ti riconosco formalmente come membro della mia Gilda dei Mercanti."
        ),
        34: (
            "E togliti quel sorrisetto compiaciuto dalla faccia! Entrare nella gilda non è un lasciapassare per dormire sugli allori.\n\n"
            "Sappi che il mondo del commercio è un'arena spietata, brulicante di sciacalli pronti a pesare la tua stessa anima sulla bilancia dell'oro. Abbassa la guardia per un solo istante, e ti divoreranno vivo."
        ),
        35: "Ahah, non farti prendere dal panico adesso! Sei un mercante riconosciuto da Lady Marian in persona. Attendo con ansia il giorno in cui il tuo nome incuterà rispetto e timore tra i titani degli affari!"
    },
    "big_sister.xlsx": {
        15: "Povere creature... le Piccole Sorelle si sono smarrite nel mondo là fuori. Non conoscono il nostro Piccolo Giardino. Si sono perse nel buio, #bigdaddy...",
        17: "...Eheh, se gli angeli esistessero davvero, che meraviglia sarebbe! Gli angeli verrebbero sicuramente in nostro soccorso... perché è questo ciò che fanno gli angeli. Troverebbero le Piccole e le riporterebbero qui tra noi. Vero, #bigdaddy? Gli angeli verranno a salvarci, ne sono certa.",
        33: "...La nostra Piccola... la nostra Piccola Sorella... Gli angeli sono creature spietate, #bigdaddy... Hanno lasciato morire la nostra Piccola senza muovere un dito. Dobbiamo... dobbiamo proteggerle noi da questo mondo crudele. Qui... tutte per loro... nel nostro Piccolo... Giardino...",
        34: "Ahahah, gli angeli non esistono per niente! Ma non importa, va tutto bene... finché ci sei tu qui con me, #bigdaddy."
    },
    "demitas.xlsx": {
        29: (
            "...#pc, ho parole per te.\n\n"
            "In tempi remoti, quando ancora calcavo la terra sotto spoglie mortali, approfondii lo studio delle rune e appresi i segreti della trascrizione dei tomi arcani. Un'arte rarissima, ormai caduta nell'oblio tra le genti di superficie."
        ),
        30: (
            "Da quando ho trovato dimora in questo luogo, ho cercato di vegliare su di voi da lontano; ma se intendi davvero fronteggiare Issizzle, la mia antica conoscenza ti sarà di vitale soccorso.\n\n"
            "...Ogniqualvolta cercherai l'ausilio della magia, presentati al mio cospetto."
        )
    },
    "fiama.xlsx": {
        74: "Se dovessi avere qualsiasi dubbio o domanda sul mondo, chiedi pure ad Ash.",
        86: "..."
    },
    "keeper_garden.xlsx": {
        27: (
            "La pensi così anche tu? Fuhuhu... ma certo che sì!\n\n"
            "Quanto desidererei rilassarmi in una sorgente termale fumante insieme a una cucciolata di gatti argentati e sguazzare spensierato per ore..."
        ),
        29: "...Ops! A quanto pare ho lasciato cadere qualcosa per terra!"
    },
    "namamani.xlsx": {
        41: (
            "...Perfetto, così dovrebbe andare.\n\n"
            "Senti anche tu? Gli ingranaggi che cantano in perfetta armonia... è il battito cardiaco di un meccanismo impeccabile."
        ),
        43: "Tieni, prendi questo vecchio ingranaggio che ho rimosso dal congegno. Conservalo come ricordo d'officina!"
    },
    "parttimer_jure.xlsx": {
        27: "Grazie mille! Fiuuu, sono appena riuscito a raggiungere la mia quota giornaliera di donazioni!",
        32: "Maledizione!"
    },
    "casino_clerk.xlsx": {
        10: "È la tua prima visita di oggi, vero? Ecco qui il tuo biglietto gratta e vinci omaggio!"
    },
    "mimu.xlsx": {
        10: ".........pi!"
    },
    "poppy.xlsx": {
        15: "Wof! Wof!"
    }
}

def run():
    for fname, rows in UPDATES.items():
        fpath = os.path.join(DRAMA_DIR, fname)
        if not os.path.exists(fpath):
            print(f"File {fname} not found, skipping.")
            continue
        wb = openpyxl.load_workbook(fpath)
        ws = wb.active
        headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
        text_c = headers.get('text', 11)
        for r, val in rows.items():
            ws.cell(row=r, column=text_c, value=val)
        wb.save(fpath)
        print(f"Updated {len(rows)} rows in {fname}")

if __name__ == "__main__":
    run()
