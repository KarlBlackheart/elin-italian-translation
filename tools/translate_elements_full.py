# coding: utf-8
"""
Elin Italian Localization - Element.xlsx Full Localizer
Translates all attributes, elements, skills, spells, matrix spells, feats,
mutations, ether diseases, town policies, and enchantments into authentic Italian.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ELEMENT_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Game', 'Element.xlsx')

ELEMENT_NAMES = {
    0: ("Fuoco", "al fuoco"),
    1: ("Gelo", "al gelo"),
    2: ("Fulmine", "al fulmine"),
    3: ("Tenebre", "alle tenebre"),
    4: ("Mente", "alla mente"),
    5: ("Veleno", "al veleno"),
    6: ("Oltretomba", "all'oltretomba"),
    7: ("Suono", "al suono"),
    8: ("Nervino", "ai danni nervini"),
    9: ("Caos", "al caos"),
    10: ("Sacro", "al sacro"),
    11: ("Magia", "alla magia"),
    12: ("Etere", "all'etere"),
    13: ("Acido", "all'acido"),
    14: ("Taglio", "al taglio"),
    15: ("Impatto", "all'impatto"),
    16: ("Vuoto", "al vuoto"),
}

MATRIX_SHAPES = {
    50100: ("Sfera", "Sfera di {elem}", "Evoca una sfera magica di {elem} attorno a chi la lancia, investendo i nemici nell'area."),
    50200: ("Soffio", "Soffio di {elem}", "Rilascia un potente soffio di {elem} concentrato in un cono frontale."),
    50300: ("Dardo", "Dardo di {elem}", "Trafigge il bersaglio e la traiettoria con un raggio magico di {elem}."),
    50400: ("Tocco", "Tocco di {elem}", "Concentra pura energia di {elem} nel palmo, scatenandola a distanza ravvicinata."),
    50500: ("Freccia", "Freccia di {elem}", "Scaglia una saetta perforante di {elem} contro il bersaglio."),
    50600: ("Fuso Orbitante", "Fuso di {elem}", "Materializza una massa senziente di energia di {elem} che dà la caccia al bersaglio."),
    50700: ("Miasma", "Miasma di {elem}", "Genera una nube persistente di {elem} che consuma gradualmente le forze del nemico."),
    50800: ("Canto", "Canto di {elem}", "Infonde l'arma dell'esecutore con il potere di {elem}."),
    50900: ("Marea", "Marea di {elem}", "Scatena una marea travolgente di energia di {elem}."),
    51000: ("Spada Arcana", "Lama di {elem}", "Evoca una lama spettrale di {elem} che trafigge e squarcia le difese bersaglio."),
    51100: ("Bit", "Modulo Orbitante di {elem}", "Materializza un costrutto difensivo orbitante intriso di {elem}."),
    51200: ("Brillamento", "Brillamento di {elem}", "Fa detonare violentemente l'energia di {elem} accumulata nel bersaglio."),
    51300: ("Cometa", "Cometa di {elem}", "Invoca una cometa astrale intrisa di {elem} che si schianta sull'area indicata."),
}

FEATS_1600 = {
    "1610": {
        "name": "Apprendista Asceta\nPraticante Asceta\nEsperto Asceta\nMaestro Asceta\nAsceta Leggendario",
        "detail": "La pratica dell'ascesi e della rinuncia fortifica prodigiosamente la tua forza vitale.",
        "textPhase": "Sei un apprendista della via ascetica.\nSei un praticante della via ascetica.\nSei un esperto della via ascetica.\nSei un maestro della via ascetica.\nSei un asceta leggendario."
    },
    "1611": {
        "name": "Gene Magico\nCellula Magica\nSangue Magico\nCorpo Arcano\nEntità Magica",
        "detail": "Ottieni riserve addizionali di mana manipolando la tua struttura genetica.",
        "textPhase": "I tuoi geni racchiudono scintille magiche.\nLe tue cellule vibrano di pura magia.\nIl tuo sangue è intriso di essenza arcana.\nIl tuo corpo è forgiato nella magia.\nLa pura energia magica domina ogni fibra del tuo essere."
    },
    "1612": {
        "name": "Velocista\nMezzofondista\nMaratoneta",
        "detail": "L'allenamento costante nella corsa aumenta la tua velocità di movimento sul campo.",
        "textPhase": "Sei un velocista sulle brevi distanze.\nSei un corridore esperto sulle medie distanze.\nSei un maratoneta instancabile sulle lunghe distanze."
    },
    "1620": {
        "name": "Braccio di Ferro\nMaestro di Braccio di Ferro\nCampione di Braccio di Ferro",
        "detail": "Allenarsi nel braccio di ferro incrementa la tua Forza muscolare.",
        "textPhase": "Hai una presa d'acciaio nel braccio di ferro.\nSei un temuto sfidante nel braccio di ferro.\nSei l'imbattuto campione di braccio di ferro."
    },
    "1621": {
        "name": "Dita Flessibili\nDita da Artigiano\nDita Prodigiose",
        "detail": "Esercitare la manualità fine aumenta la tua Destrezza.",
        "textPhase": "Le tue dita sono straordinariamente agili.\nHai la precisione manuale di un mastro orologiaio.\nLe tue dita compiono autentici prodigi di destrezza."
    },
    "1622": {
        "name": "Resistente\nMolto Resistente\nIndomito",
        "detail": "Sopportare fatiche estreme aumenta la tua Costituzione.",
        "textPhase": "Sei abituato a sopportare dolori e percosse.\nLa tua soglia di sopportazione fisica è straordinaria.\nPossiedi una resistenza incrollabile e indomita."
    },
    "1623": {
        "name": "Occhio della Vedetta\nOcchio del Ladro\nVista d'Aquila",
        "detail": "Affinare l'attenzione verso l'ambiente aumenta la tua Percezione.",
        "textPhase": "I tuoi occhi notano anche i minimi movimenti nell'ombra.\nScorgi immediatamente trappole, borse e oggetti nascosti.\nPossiedi una vista penetrante come quella di un'aquila."
    },
    "1624": {
        "name": "Curioso\nStudioso\nTopo di Biblioteca",
        "detail": "Coltivare la sete di sapere aumenta il tuo Apprendimento.",
        "textPhase": "Nutri un'insaziabile curiosità verso ogni mistero.\nDedichi ore appassionate allo studio e alla teoria.\nSei un erudito consumato che divora tomi e pergamene."
    },
    "1625": {
        "name": "Spirituale\nMistico\nSesto Senso",
        "detail": "La devozione e la comunione con l'invisibile aumentano la tua Volontà.",
        "textPhase": "Senti la presenza sottile del regno spirituale.\nSei in profonda armonia mistica con il cosmo.\nPossiedi un autentico sesto senso che ti guida nel buio."
    },
    "1626": {
        "name": "Volontà Ferrea\nVolontà d'Acciaio\nSpirito Indomabile",
        "detail": "La determinazione granitica ti permette di resistere a ogni avversità e influenza mentale.",
        "textPhase": "Possiedi una ferma determinazione interiore.\nLa tua forza di volontà è dura come l'acciaio temprato.\nIl tuo spirito è fiero, indomabile e incorruttibile."
    },
    "1627": {
        "name": "Seduttore\nRomantico\nConquistatore Fatale",
        "detail": "Affinare i modi galanti e la presenza scenica aumenta il tuo Carisma.",
        "textPhase": "Emani un fascino magnetico e seducente.\nI tuoi modi romantici incantano chiunque ti ascolti.\nPossiedi una presenza scenica travolgente e irresistibile."
    },
    "1628": {
        "name": "Fortunato\nBaciato dalla Fortuna\nPrediletto della Dea",
        "detail": "Il favore della sorte ti accompagna aumentando la tua Fortuna.",
        "textPhase": "Sembri avere sempre un pizzico di fortuna dalla tua parte.\nLa buona sorte ti assiste nei momenti più critici.\nSei il prediletto assoluto della Dea bendata."
    },
    "1629": {
        "name": "Scattante\nFulmineo",
        "detail": "Riflessi pronti e gambe reattive che aumentano la tua Velocità.",
        "textPhase": "I tuoi riflessi sono reattivi e scattanti.\nTi muovi con la rapidità fulminea del lampo."
    },
    "1630": {
        "name": "Difesa di Pietra\nDifesa di Ferro\nDifesa d'Acciaio",
        "detail": "Aumenta il valore di Protezione dall'Armatura (PV).",
        "textPhase": "Il tuo corpo assorbe i colpi come roccia solida.\nLe tue difese sono impenetrabili come il ferro battuto.\nSei una fortezza inespugnabile protetta da piastre d'acciaio."
    },
    "1631": {
        "name": "Schivata\nSchivata Migliorata\nSchivata Perfetta",
        "detail": "Aumenta il valore di Schivata Difensiva (DV).",
        "textPhase": "Sai disimpegnarti prontamente dalla traiettoria dei colpi.\nEludi gli attacchi avversari con consumata maestria.\nTi muovi tra i fendenti con la grazia eterea di uno spettro."
    },
    "1632": {
        "name": "Evasione\nEvasione Migliorata\nEvasione Superiore",
        "detail": "Conferisce una probabilità aggiuntiva di evitare del tutto gli assalti nemici.",
        "textPhase": "Riesci a sottrarti agli attacchi più insidiosi.\nLe probabilità di sfuggire ai colpi nemici aumentano.\nSei quasi impossibile da colpire di sorpresa."
    },
    "1633": {
        "name": "Ricognitore\nRicognitore Esperto\nMaestro Esploratore",
        "detail": "Migliora la capacità di individuare trappole e dettagli celati nel terreno.",
        "textPhase": "Noti indizi e tracce sfuggite agli altri.\nIndividui al primo sguardo passaggi segreti e meccanismi celati.\nNessun segreto del sottosuolo può sfuggire al tuo occhio."
    },
    "1634": {
        "name": "Negoziatore\nGrande Negoziatore",
        "detail": "Migliora l'abilità nella compravendita ottenendo sconti e prezzi migliori.",
        "textPhase": "Sai contrattare abilmente con i bottegai.\nSei un maestro supremo nell'arte della compravendita."
    },
    "1635": {
        "name": "Artista Marziale\nSanto della Spada",
        "detail": "Aumenta sensibilmente il danno inflitto a mani nude o con armi marziali.",
        "textPhase": "Padroneggi le basi delle arti marziali orientali.\nHai raggiunto l'apice mistico della via della spada."
    },
    "1636": {
        "name": "Fedele\nZelota",
        "detail": "Aumenta l'accumulo di devozione verso la divinità prescelta.",
        "textPhase": "La tua devozione verso gli dèi è sincera e profonda.\nLa tua fede incrollabile rasenta il fanatismo mistico."
    },
    "1640": {
        "name": "Amico degli Animali",
        "detail": "Facilita l'addomesticamento delle bestie e impedisce loro di attaccarti a vista.",
        "textPhase": "Le bestie della foresta percepiscono la tua benevolenza."
    },
    "1641": {
        "name": "Esorcista",
        "detail": "Aumenta l'efficacia contro spiriti irrequieti, spettri e creature non-morte.",
        "textPhase": "I tuoi colpi dissipano le ombre della non-morte."
    },
    "1642": {
        "name": "Sonno Ristoratore\nSonno Profondo\nMaestro del Sonno",
        "detail": "Dormire ripristina le forze vitali, il mana e il vigore molto più rapidamente.",
        "textPhase": "Un breve riposo basta a farti sentire rinvigorito.\nIl tuo sonno è profondo, tranquillo e immensamente ristoratore.\nPadronanza assoluta del sonno: ti risvegli sempre al massimo delle energie."
    },
    "1643": {
        "name": "Ordinato\nMetodico\nManiaco dell'Ordine",
        "detail": "Migliora l'efficienza nell'organizzazione dello zaino e riduce il tempo perso a cercare oggetti.",
        "textPhase": "Ti piace mantenere le tue cose ben ordinate.\nOrganizzi meticolosamente ogni cassa e scomparto.\nOgni singolo oggetto ha il suo posto preciso e catalogato."
    },
    "1644": {
        "name": "Mutazione Corporea",
        "detail": "Favorisce mutazioni corporee favorevoli durante l'esposizione alle correnti caotiche.",
        "textPhase": "Il tuo corpo risponde alle mutazioni con eccezionale flessibilità."
    },
    "1645": {
        "name": "Anima della Festa",
        "detail": "Intrattenere il pubblico con la musica o la conversazione diverte tutti molto più in fretta.",
        "textPhase": "Sei il centro dell'attenzione in ogni taverna e banchetto."
    },
    "1646": {
        "name": "Anima Solitaria",
        "detail": "Ottieni bonus al combattimento quando viaggi ed esplori privo di alleati o compagni.",
        "textPhase": "La solitudine tempra il tuo spirito rendendoti più forte."
    },
    "1647": {
        "name": "Pastore",
        "detail": "Migliora la resa di latte, uova e lana dagli animali da allevamento.",
        "textPhase": "Sai prenderti cura del bestiame con mano esperta e amorevole."
    },
    "1648": {
        "name": "Lancio Rapido",
        "detail": "Riduce il tempo necessario per recitare e canalizzare gli incantesimi.",
        "textPhase": "Riesci a recitare formule arcane con straordinaria rapidità."
    },
    "1649": {
        "name": "Difensore",
        "detail": "Aumenta le difese e ti permette di proteggere i compagni adiacenti dai colpi nemici.",
        "textPhase": "Ti poni a baluardo in difesa dei tuoi compagni."
    },
    "1650": {
        "name": "Buongustaio",
        "detail": "Apprendi come riconoscere le proprietà nutritive e i benefici nascosti di ogni piatto.",
        "textPhase": "Sai discernere all'istante il valore nutritivo e le spezie di ogni vivanda."
    },
    "1651": {
        "name": "Galateo Magico",
        "detail": "Impedisce alle magie d'area di danneggiare o infastidire gli abitanti pacifici delle città.",
        "textPhase": "Controlli le fiamme e l'energia arcana per non recare danno a passanti inermi."
    },
    "1652": {
        "name": "Raffica di Frecce",
        "detail": "Consente di incoccare e scagliare dardi a una velocità straordinaria.",
        "textPhase": "Scagli una tempesta ininterrotta di proiettili sul bersaglio."
    },
    "1653": {
        "name": "Risveglio Onirico",
        "detail": "Conserva la lucidità mentale all'interno dei sogni permettendo rivelazioni mistiche.",
        "textPhase": "Padroneggi l'onironautica e mantieni il controllo nei sogni."
    },
    "1654": {
        "name": "Incantatore Corazzato Base\nIncantatore Corazzato Avanzato\nMaestro Incantatore Corazzato",
        "detail": "Riduce la penalità al successo del lancio di incantesimi causata da armature pesanti.",
        "textPhase": "Riesci a canalizzare incantesimi indossando armature di cuoio rinforzato.\nIncanti con disinvoltura protetto da cotte di maglia e piastre parziali.\nLanci incantesimi anche avvolto da una corazza di piastre completa senza esitazione."
    },
    "1655": {
        "name": "Fedele Modello",
        "detail": "Offrire doni e sacrifici all'altare divino genera il doppio del favore celeste.",
        "textPhase": "Le tue offerte all'altare sono gradite e benedette dalla divinità."
    },
    "1656": {
        "name": "Riciclatore di Rottami",
        "detail": "Permette di estrarre materiali utili da rottami, carcasse e rifiuti altrimenti inutilizzabili.",
        "textPhase": "Sai ricavare risorse preziose anche dai mucchi di scarti."
    },
    "1657": {
        "name": "Risparmio Magico",
        "detail": "Insegna come ottimizzare la canalizzazione dell'energia arcana per consumare meno mana.",
        "textPhase": "Sai come preservare il tuo mana evitando ogni dispersione energetica."
    },
    "1658": {
        "name": "Cuoco Itinerante",
        "detail": "Permette di preparare manicaretti deliziosi anche all'aperto con un semplice focolare da campo.",
        "textPhase": "Cucini piatti squisiti anche nelle condizioni più selvagge."
    },
    "1659": {
        "name": "Prima Cattura",
        "detail": "Aumenta la probabilità di pescare pesci rari e tesori sommersi con la lenza.",
        "textPhase": "La tua lenza attira prede straordinarie fin dal primo lancio."
    },
    "1660": {
        "name": "Saccheggiatore",
        "detail": "Aumenta il bottino di monete d'oro e gemme rinvenuto dai nemici sconfitti.",
        "textPhase": "Trovi sempre qualcosa di valore nei resti dei tuoi nemici."
    },
    "1661": {
        "name": "Demolitore",
        "detail": "Migliora la capacità di abbattere strutture, pareti rocciose e porte con violenza inaudita.",
        "textPhase": "I tuoi colpi frantumano pietre, legname e murature con facilità disarmante."
    },
    "1662": {
        "name": "Dita d'Oro",
        "detail": "La suprema abilità ladresca nel sottrarre oggetti di immenso valore senza alcun rischio.",
        "textPhase": "Eccelli nell'arte del borseggio e del furto con destrezza ineguagliata."
    },
    "1663": {
        "name": "Mangiatore Veloce",
        "detail": "Permette di consumare cibi e bevande in un solo istante anche durante le concitate fasi di battaglia.",
        "textPhase": "Divori provviste e pozioni con una velocità fulminea."
    },
    "1664": {
        "name": "Missionario dell'Amore",
        "detail": "Diffonde amore, gioia e concordia tra la popolazione di Ylva, pacificando gli animi inquieti.",
        "textPhase": "La tua sola presenza irraggia calore, affetto e concordia universale."
    }
}

NAME_MAP = {
    "0": ("Vuoto", "Elemento primordiale del nulla assoluto."),
    "1": ("Livello", "Il livello di competenza o potere."),
    "2": ("Qualità", "Il grado di fattura o purezza."),
    "3": ("d", ""),
    "5": ("Incavo", "Alloggiamento per rune o gemme di potenziamento."),
    "10": ("Nutrizione", "Valore nutritivo fornito."),
    "11": ("Peso", "Massa complessiva dell'oggetto."),
    "12": ("Dimensione", "Grandezza fisica o ingombro."),
    "13": ("Durezza", "Resistenza meccanica e solidità."),
    "14": ("Crescita", "Tasso di sviluppo o maturazione."),
    "15": ("Acqua", "Contenuto d'acqua o idratazione."),
    "16": ("Calore", "Temperatura interna o calore accumulato."),
    "17": ("Deperimento", "Grado di deperibilità o freschezza."),
    "18": ("Gusto", "Sapore o appetibilità."),
    "20": ("Veleno", "Tossicità o presenza di veleno."),
    "21": ("Fuoco", "Proprietà termica o incendiaria."),
    "22": ("Freddo", "Proprietà congelante o criogenica."),
    "23": ("Antidoto", "Efficacia nel neutralizzare veleni."),
    "24": ("Guarigione", "Capacità curativa e rigenerativa."),
    "25": ("Antidoto", "Effetto disintossicante."),
    "26": ("Cura", "Ripristino delle condizioni di salute."),
    "29": ("Tratti Razziali", "Tratti innati ereditati dalla propria stirpe nel mondo di Ylva."),
    "30": ("Testa", "Slot per copricapi, elmi e cappelli."),
    "31": ("Collo", "Slot per amuleti, collane e pendenti."),
    "32": ("Busto", "Slot per armature, tuniche e corazze."),
    "33": ("Schiena", "Slot per mantelli, zaini e ali."),
    "34": ("Braccio", "Slot per scudi, bracciali e protezioni avambraccio."),
    "35": ("Mano", "Slot per armi da mischia, bacchette e attrezzi impugnati."),
    "36": ("Dito", "Slot per anelli e sigilli."),
    "37": ("Vita", "Slot per cinture, fasce e cinturoni."),
    "38": ("Gamba", "Slot per gambali, pantaloni e calzoni."),
    "39": ("Piedi", "Slot per stivali, calzari e scarpe."),
    "40": ("Strumento", "Slot per strumenti da lavoro o equipaggiamento speciale."),
    "41": ("A Distanza", "Slot per archi, balestre, fucili e fionde."),
    "42": ("Munizioni", "Slot per frecce, dardi e proiettili."),
    "43": ("Gettone", "Slot per gettoni, talismani e reliquie minori."),
    "44": ("Cintura Attrezzi", "Slot di accesso rapido per attrezzi e utensili."),
    "45": ("Fonte di Luce", "Slot per lanterne, torce e pietre luminescenti."),
    "50": ("Ignifugo", "Protegge l'oggetto dalla distruzione da fiamme."),
    "51": ("Antiacido", "Protegge l'oggetto dalla corrosione da acido."),
    "55": ("Riduzione Danni Fisici", "Riduce passivamente l'entità dei danni fisici subiti."),
    "56": ("Riduzione Danni Elementali", "Riduce passivamente l'entità dei danni di origine elementale."),
    "57": ("Schivata Perfetta", "Conferisce una probabilità di eludere totalmente gli attacchi fisici."),
    "60": ("Punti Vita", "Energia vitale del corpo. Se si azzera, sopraggiunge la morte."),
    "61": ("Mana", "Riserva di energia arcana necessaria per lanciare incantesimi."),
    "62": ("Vigore", "Resistenza fisica impiegata nelle fatiche, nell'artigianato e nelle abilità speciali."),
    "68": ("Protezione Letale", "Mitiga i colpi fatali permettendo di sopravvivere a un soffio dalla morte."),
    "70": ("Forza", "Influenza il danno in mischia, il carico trasportabile e la potenza muscolare."),
    "71": ("Costituzione", "Determina i punti vita massimi, la resistenza alla fatica e il vigore fisico."),
    "72": ("Destrezza", "Determina la precisione degli attacchi, l'agilità manuale e la schivata."),
    "73": ("Percezione", "Migliora la mira a distanza, la vista e l'individuazione di trappole e segreti."),
    "74": ("Apprendimento", "Governa la rapidità di acquisizione di abilità e l'accumulo di esperienza."),
    "75": ("Volontà", "Rafforza la riserva di mana, la fede verso le divinità e la tenacia spirituale."),
    "76": ("Magia", "Potenzia l'intensità di tutti gli incantesimi e la comprensione dei tomi."),
    "77": ("Carisma", "Migliora le relazioni con gli NPC, i prezzi mercantili e la fedeltà dei compagni."),
    "78": ("Fortuna", "Un tocco benevolo del fato che influenza eventi casuali e colpi critici."),
    "79": ("Velocità", "Determina la frequenza dei turni d'azione in combattimento e nell'esplorazione."),
    "80": ("Intelligenza", "Capacità logica e comprensione teorica delle scienze e dei misteri."),
    "85": ("Fede e Pietà", "Rappresenta la devozione verso la tua divinità e sblocca ricompense e miracoli superiori."),
    "90": ("Colpo Critico", "Aumenta la probabilità di infliggere colpi devastanti."),
    "91": ("Tranciante Vorpal", "Capacità di sferrare colpi istantaneamente decapitanti o mortali."),
    "92": ("Penetrazione Armatura", "Consente agli attacchi di oltrepassare la protezione fisica (PV) del bersaglio."),
    "93": ("Resistenza Anti-Magica", "Protegge passivamente dagli effetti diretti di ogni forma di incantesimo ostile."),
    "94": ("Danno Globale", "Aumenta la potenza complessiva di qualsiasi attacco o incantesimo inflitto."),
    "132": ("Tattica", "Aumenta l'efficacia del combattimento corpo a corpo ravvicinato."),
    "133": ("Mira", "Incrementa la precisione e il danno delle armi a distanza."),
    "134": ("Occhio della Mente", "Consente di individuare i punti deboli avversari."),
    "135": ("Strategia", "Migliora la coordinazione sul campo di battaglia e i bonus di squadra."),
    "150": ("Schivata", "Capacità di evitare agilmente i colpi in arrivo."),
    "151": ("Schivata Superiore", "Perfezione nel movimento per anticipare e neutralizzare ogni attacco."),
    "152": ("Furtività", "Abilità nel muoversi senza farsi notare né udire da creature ostili."),
    "200": ("Nuoto", "Capacità di muoversi in acque profonde senza affogare."),
    "207": ("Sollevamento Pesi", "Aumenta la capacità di carico trasportabile senza subire penalità da ingombro."),
    "210": ("Esplorazione", "Capacità di individuare trappole nascoste, porte segrete e scorciatoie sotterranee."),
    "300": ("Rigenerazione Naturale", "Accelera il recupero naturale dei punti vita nel tempo."),
    "301": ("Meditazione", "Aumenta la velocità di rigenerazione passiva della riserva di mana."),
    "302": ("Controllo Magico", "Evita di danneggiare compagni e alleati quando si lanciano incantesimi ad area."),
    "310": ("Igiene", "Mantenimento della pulizia personale per prevenire malattie e parassiti."),
    "311": ("Vescica", "Capacità di gestire i bisogni corporali fisiologici."),
    "312": ("Svago", "Necessità di divertimento e passatempi per mantenere alto l'umore."),
    "313": ("Ambiente", "Sensibilità alla bellezza e al decoro del luogo circostante."),
    "380": ("Contrattacco", "Risponde istantaneamente a un attacco nemico parato o schivato."),
    "381": ("Tiranno dello Scudo", "Schiaccia gli avversari usando lo scudo come arma d'impatto devastante."),
    "382": ("Carica Furiosa", "Scatta a capofitto contro il nemico per spezzarne la guardia."),
    "383": ("Riflessione Energetica", "Devia parte dell'energia magica ricevuta contro l'attaccante."),
    "400": ("Anti-Teletrasporto", "Impedisce il teletrasporto involontario o forzato."),
    "401": ("Levitazione", "Fa galleggiare il corpo a mezz'aria, evitando trappole e terreni insidiosi."),
    "402": ("Raggio di Rilevamento", "Estende la distanza a cui percepisci nemici e oggetti."),
    "417": ("Affetto Espanso", "Promuove sentimenti di calore e amicizia profonda."),
    "418": ("Innocenza", "Purezza di spirito che attenua le ostilità."),
    "419": ("Coda Mobile", "Una coda agile che aiuta a mantenere l'equilibrio."),
    "420": ("Immunità al Veleno", "Rende completamente immune agli effetti del veleno."),
    "421": ("Immunità alla Cecità", "Rende immune alla perdita temporanea o permanente della vista."),
    "422": ("Immunità alla Paralisi", "Rende immune agli effetti paralizzanti."),
    "423": ("Immunità alla Paura", "Rende immune al terrore e al panico in battaglia."),
    "424": ("Immunità al Sonno", "Impedisce di essere addormentati da incantesimi o sonniferi."),
    "425": ("Immunità alla Confusione", "Protegge la mente da ogni forma di confusione o disorientamento."),
    "426": ("Protezione Borseggi", "Rende impossibile essere borseggiati dai ladri."),
    "427": ("Protezione Decapitazione", "Impedisce di subire colpi vorpal decapitanti istantanei."),
    "428": ("Mietitore di Vita", "Assorbe una frazione dell'essenza vitale dei nemici abbattuti."),
    "429": ("Respirazione Subacquea", "Permette di respirare normalmente sott'acqua."),
    "430": ("Immunità Onde d'Urto", "Rende immuni agli spostamenti e agli stordimenti da esplosione."),
    "431": ("Immunità alle Scottature", "Protegge la pelle dai danni delle radiazioni solari e del caldo estremo."),
    "432": ("Santificato", "Consacrato con benedizioni celesti che allontanano il male."),
    "435": ("Difesa a Distanza", "Riduce l'impatto e i danni ricevuti dai proiettili a distanza."),
    "440": ("Sostegno Forza", "Impedisce il deterioramento o la riduzione della Forza."),
    "441": ("Sostegno Costituzione", "Impedisce la riduzione della Costituzione."),
    "442": ("Sostegno Destrezza", "Impedisce la riduzione della Destrezza."),
    "443": ("Sostegno Percezione", "Impedisce la riduzione della Percezione."),
    "444": ("Sostegno Apprendimento", "Impedisce la riduzione dell'Apprendimento."),
    "445": ("Sostegno Volontà", "Impedisce la riduzione della Volontà."),
    "446": ("Sostegno Magia", "Impedisce la riduzione della Magia."),
    "447": ("Sostegno Carisma", "Impedisce la riduzione del Carisma."),
    "488": ("Rantolo di Morte", "Emette un grido straziante nel momento della caduta, disorientando i nemici."),
    "489": ("Melodia dell'Anima", "Una melodia eterea che armonizza l'essenza spirituale."),
    "490": ("Chiaroveggenza", "Permette di scrutare oltre le barriere fisiche e le pareti sotterranee."),
    "491": ("Immunità alla Gravità", "Protegge dagli effetti schiaccianti dei pozzi di gravità."),
    "492": ("Passi Allegri", "Movimenti spensierati che riducono la stanchezza durante il viaggio."),
    "493": ("Libertà di Movimento", "Impedisce di essere rallentati, intrappolati o bloccati da ragnatele."),
    "494": ("Sentenza Prolungata", "Estende la durata delle condanne inflitte ai bersagli."),
    "495": ("Amico delle Cavalcature", "Rende le cavalcature eccezionalmente mansuete e docili."),
    "600": ("Caricatore Espanso", "Aumenta il numero di munizioni che l'arma può contenere."),
    "601": ("Ricarica Rapida", "Riduce il tempo necessario per ricaricare le armi a distanza."),
    "602": ("Fuoco Rapido", "Aumenta la cadenza di tiro e il numero di colpi esplosi."),
    "603": ("Respingimento", "Gli attacchi scagliano indietro il bersaglio all'impatto."),
    "604": ("Recupero Munizioni", "Aumenta la probabilità di recuperare frecce o proiettili intatti."),
    "605": ("Tiratore Scelto", "Incrementa la precisione estrema dei tiri a lunga distanza."),
    "606": ("Perforazione", "I colpi penetrano attraverso i corpi dei nemici in fila."),
    "607": ("Rosa Dispersa", "Allarga l'arco di dispersione dei proiettili per colpire più bersagli."),
    "608": ("Onda d'Urto", "Genera una violenta onda sonica al punto d'impatto del colpo."),
    "609": ("Risparmio Amuleti", "Riduce il consumo delle cariche degli amuleti magici."),
    "620": ("Inseguimento", "Consente di inseguire prontamente i bersagli in fuga."),
    "621": ("Raffica di Fendenti", "Scatena una combinazione serrata di colpi d'arma in rapida successione."),
    "622": ("Fendente Circolare", "Spazza l'arma in cerchio colpendo tutti i nemici adiacenti."),
    "623": ("Finta di Spada", "Inganna le difese avversarie aprendo un varco letale per l'assalto."),
    "624": ("Contrattacco della Frustrazione", "Canalizza la rabbia dei colpi subiti in un devastante fendente di risposta."),
    "640": ("Moltiplicatore Vita", "Aumenta proporzionalmente il totale dei punti vita massimi."),
    "641": ("Moltiplicatore Mana", "Aumenta proporzionalmente il totale del mana massimo."),
    "650": ("Moltiplicatore DV", "Incrementa proporzionalmente il valore di Schivata Difensiva (DV)."),
    "651": ("Moltiplicatore PV", "Incrementa proporzionalmente il valore di Protezione dall'Armatura (PV)."),
    "652": ("Ecologico", "Riduce l'impatto e il consumo energetico dell'oggetto."),
    "653": ("Vivente", "L'arma possiede un'anima propria e si nutre delle esperienze di battaglia per crescere."),
    "654": ("Divieto di Violenza", "Impedisce categoricamente ogni azione violenta o aggressiva."),
    "700": ("Ricco di Collagene", "Nutre la pelle e favorisce l'elasticità dei tessuti corporei."),
    "701": ("Gatto", "Carne di felino domestico."),
    "702": ("Veleno Letale", "Una dose concentrata di veleno organico letale."),
    "756": ("Aroma Termale", "Emana il caratteristico profumo di zolfo e acque calde."),
    "758": ("Carne Divina", "L'essenza nutritiva strappata a una divinità."),
    "800": ("Dominio", "Sfera di influenza arcana o territoriale."),
    "801": ("Sopravvivenza", "Capacità di resistere alle asperità della natura selvaggia."),
    "802": ("Fede", "Il legame mistico con la divinità patrona."),
    "910": ("Fuoco", "Elemento delle fiamme e del calore rovente."),
    "911": ("Gelo", "Elemento del ghiaccio e del freddo glaciale."),
    "912": ("Fulmine", "Elemento delle tempeste e delle scariche elettriche."),
    "913": ("Tenebre", "Elemento dell'oscurità primordiale e dell'oblio."),
    "914": ("Mente", "Elemento del pensiero, delle illusioni e del controllo psichico."),
    "915": ("Veleno", "Elemento delle tossine mortali e della corruzione vitale."),
    "916": ("Oltretomba", "Elemento delle energie spettrali e della non-morte."),
    "917": ("Suono", "Elemento delle vibrazioni acustiche e degli urli sonici."),
    "918": ("Nervino", "Elemento delle tossine neurali e della paralisi motoria."),
    "919": ("Sacro", "Elemento della grazia divina e della purificazione celestiale."),
    "920": ("Caos", "Elemento dell'entropia incontrollata e della mutazione pura."),
    "921": ("Magia", "Elemento dell'energia arcana pura non vincolata."),
    "922": ("Etere", "Elemento del vento etereo, fonte di mutazioni e follia cosmica."),
    "923": ("Acido", "Elemento corrosivo capace di sciogliere metalli e carni."),
    "924": ("Taglio", "Danno inferto da lame affilate che causano emorragie."),
    "925": ("Impatto", "Danno inferto da corpi contundenti e colpi dirompenti."),
    "926": ("Vuoto", "Il nulla che consuma e annulla l'esistenza stessa."),
    "927": ("Gatto", "Elemento dell'essenza felina e delle sue bizzarre manifestazioni."),
    "950": ("Resistenza al Fuoco", "Protezione passiva contro bruciature e incantesimi di fuoco."),
    "951": ("Resistenza al Gelo", "Protezione passiva contro assideramento e incantesimi di ghiaccio."),
    "952": ("Resistenza al Fulmine", "Protezione passiva contro scariche elettriche e temporali."),
    "953": ("Resistenza alle Tenebre", "Protezione passiva contro incantesimi oscuri e cecità."),
    "954": ("Resistenza alla Mente", "Protezione passiva contro attacchi psichici, panico e follia."),
    "955": ("Resistenza al Veleno", "Protezione passiva contro tossine, veleni e morbi."),
    "956": ("Resistenza all'Oltretomba", "Protezione passiva contro danni necrotici e risucchio vitale."),
    "957": ("Resistenza al Suono", "Protezione passiva contro esplosioni soniche e sordità."),
    "958": ("Resistenza Nervina", "Protezione passiva contro tossine nervine e paralisi."),
    "959": ("Resistenza al Caos", "Protezione passiva contro effetti caotici imprevedibili."),
    "960": ("Resistenza al Sacro", "Protezione passiva contro punizioni divine e luce sacra."),
    "961": ("Resistenza alla Magia", "Protezione passiva contro incantesimi arcanici generici."),
    "962": ("Resistenza all'Etere", "Protezione passiva contro la progressione della Malattia dell'Etere."),
    "963": ("Resistenza all'Acido", "Protezione passiva contro acidi corrosivi e ruggine."),
    "964": ("Resistenza al Taglio", "Protezione passiva contro lacerazioni ed emorragie."),
    "965": ("Resistenza all'Impatto", "Protezione passiva contro traumi da schiacciamento e percussione."),
    "1200": ("Nutrizione Efficiente", "Estrae il massimo sostentamento da ogni porzione di cibo ingerita."),
    "1201": ("Sintonia col Mana", "Armonizza il corpo con i flussi del mana riducendo il costo degli incantesimi."),
    "1202": ("Apprendimento Rapido", "Permette di assimilare nozioni ed esperienza a una velocità prodigiosa."),
    "1205": ("Gusto per la Carne Umana", "Sviluppa una predilezione culinaria per le carni dei propri simili."),
    "1206": ("Maledizione del Maniero", "Un antico maleficio incombe sinistramente sul destino."),
    "1231": ("Illuminazione Spirituale", "Uno stato di chiarezza mistica trascendente."),
    "1270": ("Condotta Virtuosa", "Rappresenta una vita retta e colma di nobiltà d'animo."),
    "1271": ("Fardello del Karma", "Il pesante fardello spirituale accumulato compiendo nefandezze."),
    "1300": ("Favore degli Elementi", "Benedizione degli spiriti elementali della natura."),
    "1305": ("Favore della Terra", "Benedizione delle rocce profonde e della stabilità tellurica."),
    "1310": ("Favore del Vento", "Benedizione delle brezze veloci e delle correnti aeree."),
    "1400": ("Maestria nelle Armi", "Padronanza assoluta nell'uso di lame, asce e strumenti di guerra."),
    "1401": ("Fortuna del Ladro", "Una predisposizione innata a scappare dalle guardie e scassinare serrature."),
    "1402": ("Sapienza Arcana", "Conoscenza approfondita dei circoli magici e delle formule antiche."),
    "1415": ("Crescita della Coda", "Spunta una coda addizionale che vibra di energia."),
    "1510": ("Pelle di Ferro", "Alterazione fisica causata da mutazione corporea."),
    "1511": ("Albino", "Depigmentazione genetica della cute e dei capelli."),
    "1512": ("Occhio di Falco", "Una mutazione che acuisce straordinariamente la vista."),
    "1513": ("Vista Indebolita", "La retina fatica a mettere a fuoco i dettagli."),
    "1514": ("Articolazioni Flessibili", "Legamenti straordinariamente elastici."),
    "1515": ("Articolazioni Rigide", "Le cartilagini si induriscono limitando l'agilità."),
    "1516": ("Sangue di Troll", "La rigenerazione tissutale è prodigiosa."),
    "1517": ("Anemia", "Carenza di emoglobina che causa affanno costante."),
    "1518": ("Gambe Scattanti", "Gambe lunghe e toniche modellate per la corsa."),
    "1519": ("Gambe Deformi", "Le ossa degli arti inferiori sono arcuate o contorte."),
    "1520": ("Braccia Taurine", "Bicipiti possenti capaci di sforzi titanici."),
    "1521": ("Braccia Esili", "Arti superiori deboli e privi di tono muscolare."),
    "1522": ("Voce Suadente", "Timbro melodioso che ammalia chiunque lo ascolti."),
    "1523": ("Voce Terrificante", "Un ringhio gutturale che incute timore istintivo."),
    "1524": ("Cervello Cibernetico", "La mente elabora dati con la precisione di un computer."),
    "1525": ("Ottusità Mentale", "Difficoltà nel formulare pensieri astratti complessi."),
    "1526": ("Sangue Bollente", "La temperatura corporea sale costantemente."),
    "1527": ("Gelo Interiore", "Un brivido perenne avvolge il sistema circolatorio."),
    "1528": ("Isolante Corporeo", "Il corpo disperde innocuamente le scariche elettriche."),
    "1529": ("Conduttore Naturale", "La pelle assorbe avidamente le cariche elettriche."),
    "1530": ("Corpo Purificato", "I tessuti sono incorrotti e respingono le impurità."),
    "1531": ("Corpo Contaminato", "La carne ospita tossine e scorie malsane."),
    "1532": ("Chioma Folta", "Capelli robusti e setosi che crescono con vigore."),
    "1533": ("Calvizie Totale", "Cute completamente liscia e priva di follicoli."),
    "1550": ("Vortice Gravitazionale", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1551": ("Volto Piagato", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1552": ("Trasformazione in Zoccoli", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1553": ("Occhio Etereo Aggiuntivo", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1554": ("Ali dell'Etere", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1555": ("Collo Taurino Spesso", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1556": ("Sete di Strage", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1557": ("Testa Ipertrofica", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1558": ("Umidificatore Vivente", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1559": ("Dipendenza da Pozioni", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1560": ("Debilitazione Progressiva", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1561": ("Demenza dell'Etere", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1562": ("Corazza di Chitina Pesante", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1563": ("Nemico di Ogni Vivente", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1564": ("Batteria di Mana Vivente", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "1565": ("Mani di Veleno", "Sintomo fisico scatenato dall'accumulo di Etere nei tessuti."),
    "2003": ("Edilizia", "Consente l'espansione urbanistica e la costruzione di nuovi edifici."),
    "2115": ("Amministrazione Civica", "Gestione centralizzata delle risorse del feudo e della burocrazia."),
    "2116": ("Dedizione allo Studio", "Incoraggia la popolazione a frequentare biblioteche e accademie."),
    "2117": ("Patriottismo Locale", "Rafforza l'orgoglio degli abitanti e il senso di appartenenza al territorio."),
    "2200": ("Qualità del Suolo", "Fertilità e ricchezza di minerali della terra coltivabile."),
    "2201": ("Generazione Elettrica Naturale", "Sfrutta cascate, venti e calore sotterraneo per alimentare il feudo."),
    "2202": ("Promozione Turistica", "Diffonde la fama del territorio per attrarre mercanti e viandanti facoltosi."),
    "2500": ("Tassa sui Patrimoni", "Imposta proporzionale sui possedimenti e sui tesori dei residenti più agiati."),
    "2501": ("Tributo al Tempio", "Destina una quota delle entrate locali al culto degli dèi protettori."),
    "2502": ("Distribuzione Alimentare", "Garantisce razioni di pane e viveri gratuiti alle famiglie bisognose."),
    "2700": ("Risparmio Energetico", "Regola l'uso di torce, lampade e generatori magici nelle ore notturne."),
    "2701": ("Raccolta Differenziata", "Ordinanza che impone di smistare scarti organici, rottami e vetro."),
    "2702": ("Bando sul Decoro Urbano", "Sanzioni severe per chi abbandona rifiuti per strada o danneggia il verde."),
    "2800": ("Sconto Fedeltà al Feudo", "Agevolazioni commerciali per chi risiede stabilmente nel territorio."),
    "2810": ("Apertura Commerciale", "Incentivi per l'apertura di nuovi banchi di vendita e botteghe artigiane."),
    "2811": ("Tutela dei Viandanti", "Rafforza le ronde di guardie a difesa di carovane e forestieri."),
    "3500": ("Grotta Sotterranea", "Ambiente sotterraneo umido e ricco di vene rocciose."),
    "3600": ("Pianura", "Ampie distese erbose ideali per pascoli e accampamenti."),
    "3601": ("Foresta Rigogliosa", "Bosco denso ricco di legname pregiato e fauna selvatica."),
    "3602": ("Distesa Innevata", "Terreno perennemente ghiacciato e battuto da bufere artiche."),
    "3700": ("Suolo Fertile", "Terreno ricco di humus che velocizza la maturazione dei raccolti."),
    "3701": ("Geyser Naturale", "Sorgente idrotermale che zampilla vapori benefici dal sottosuolo."),
    "3702": ("Rovine Antiche", "Vestigia di civiltà dimenticate celanti segreti e reperti preziosi."),
    "3800": ("Vena di Carbone", "Deposito minerario di combustibile fossile per forge e caldaie."),
    "3801": ("Funghi Rari del Bosco", "Colonie di funghi autoctoni dagli svariati impieghi alchemici e culinari."),
    "3802": ("Perla di Silice", "Minerale splendente formatosi dalla cristallizzazione delle sabbie."),
    "3900": ("Grazia di Elin", "La protezione mistica e benevola che veglia sulle terre di Ylva."),
    "4000": ("Modalità Disboscamento", "Configurazione di lavoro ottimizzata per abbattere alberi e raccogliere tronchi."),
    "4001": ("Modalità Scavo", "Configurazione di lavoro per sbancare pareti rocciose ed estrarre minerali."),
    "4002": ("Modalità Modellazione Terreno", "Permette di innalzare, spianare o modificare il rilievo del suolo."),
    "5000": ("Attendi", "Lascia trascorrere il turno osservando i movimenti circostanti."),
    "5001": ("Attacca", "Sferra un assalto di base con l'arma impugnata."),
    "5002": ("Attacca", "Sferra un assalto di base con l'arma impugnata."),
    "6001": ("Suona Musica", "Esegui un brano musicale con lo strumento impugnato per allietare o intrattenere."),
    "6003": ("Riposa", "Prenditi un momento di quiete per recuperare gradualmente energie e vigore."),
    "6011": ("Mano Lesta", "Abilità nel sottrarre oggetti o monete dalle tasche altrui senza essere notati."),
    "6400": ("Fuga Disperata", "Scatta a perdifiato per allontanarti dalle minacce più letali."),
    "6410": ("Autodistruzione", "Fa detonare il proprio corpo provocando un'esplosione catastrofica."),
    "6420": ("Moltiplicazione", "Crea una copia biologica identica di se stesso sul campo."),
    "6500": ("Soffio di Bolle", "Espelle una raffica di bolle d'acqua schiumose che disorientano i nemici."),
    "6600": ("Maledizione", "Lancia una sventura debilitante che affligge il destino del bersaglio."),
    "6601": ("Intralcio", "Avvolge gli arti del bersaglio impedendogli la fuga o la marcia rapida."),
    "6602": ("Trazione Forzata", "Aggancia e trascina a forza il nemico verso la propria posizione."),
    "6700": ("Provocazione", "Deride e insulta i nemici per attirare la loro attenzione su di sé."),
    "6701": ("Regressione della Volpe", "Ritorna alla primordiale e scattante forma di cucciolo di volpe."),
    "6720": ("Economia Magica", "Ottimizza il consumo di mana per preservare le riserve arcane."),
    "6800": ("Adunata", "Chiama a raccolta i compagni e i servi nelle immediate vicinanze."),
    "6801": ("Grembo delle Tenebre", "Crea una sfera di oscurità viva che consuma le forze vitali."),
    "6802": ("Sentenza di Morte", "Condanna il bersaglio a morte certa al termine di un conto alla rovescia."),
    "6900": ("Risucchio di Mana", "Estrae il flusso magico direttamente dall'avversario per rifornirsi."),
    "6901": ("Preghiera di 《Jure》", "Invoca la pietosa e commovente intercessione della Dea della Guarigione 《Jure》."),
    "6902": ("Possessione di 《Lulwy》", "Canalizza nel corpo l'impetuosa e tempestosa agilità della Dea del Vento 《Lulwy》."),
    "7000": ("Soffio", "Forma di incantesimo che scaturisce a cono frontale."),
    "7001": ("Sfera Esplosiva", "Forma di incantesimo che si espande in una sfera devastante."),
    "7002": ("Dardo Perforante", "Forma di incantesimo che saetta in linea retta perforando i bersagli."),
    "7800": ("Marea Marina", "Onda d'acqua travolgente che spazza il campo di battaglia."),
    "8200": ("Teletrasporto", "Smaterializza e ricompone il lanciatore in una posizione casuale della mappa."),
    "8201": ("Teletrasporto Breve", "Sposta istantaneamente il lanciatore di poche caselle verso una zona sicura."),
    "8202": ("Teletrasporto di Massa", "Trasporta simultaneamente compagni e nemici circostanti in luoghi remoti."),
    "8300": ("Levitazione Magica", "Solleva temporaneamente il corpo in aria per sorvolare trappole e abissi."),
    "8380": ("Mutazione Spontanea", "Scatena un'alterazione corporea incontrollata donando tratti o anomalie."),
    "8390": ("Desiderio", "La forma più alta di magia. Invoca una preghiera all'universo per ottenere qualsiasi bene."),
    "8400": ("Cura Ferite Leggere", "Canalizza energia vitale per risanare graffi, contusioni e piccole lacerazioni."),
    "8401": ("Cura Ferite Gravi", "Ricompone tessuti muscolari profondi e ferite sanguinanti di seria entità."),
    "8402": ("Cura Ferite Critiche", "Sana fratture esposte e lacerazioni mortali strappando il bersaglio alla morte."),
    "8500": ("Velo Sacro", "Avvolge il lanciatore in un sudario benedetto che deflette le malefatte oscure."),
    "8501": ("Occhio del Gatto", "Amplifica la vista notturna e la percezione sensoriale di ombre e contorni."),
    "8502": ("Scudo Sacro", "Erige una barriera protettiva celestiale che assorbe parte dei danni ricevuti."),
    "8700": ("Silenzio", "Soffoca la voce del bersaglio impedendogli di recitare formule e incantesimi."),
    "8702": ("Debolezza", "Indebolisce la fibra muscolare e le difese fisiche del bersaglio."),
    "8704": ("Cicatrice Elementale", "Dilacera le difese del bersaglio rendendolo vulnerabile a ogni elemento."),
    "8800": ("Nube di Tenebra", "Evoca una cortina di fumo nero impenetrabile che acceca chiunque vi entri."),
    "8801": ("Ragnatela Vischiosa", "Tesse fili appiccicosi sul terreno per intrappolare e immobilizzare i nemici."),
    "9000": ("Evocazione Bestie", "Chiama in soccorso animali selvatici della foresta a difesa del lanciatore."),
    "9001": ("Evocazione Sorellina Non-Morta", "Richiama dal regno delle ombre una devota (e inquietante) sorellina non-morta."),
    "9002": ("Evocazione Fiamme", "Genera spiriti ardenti di fuoco elementale pronti a incenerire i nemici."),
    "9150": ("Meteora", "Fa piovere una devastante roccia fusa dallo spazio che annienta l'intera area."),
    "9151": ("Terremoto", "Fa tremare violentemente la terra distruggendo mura e schiacciando i nemici."),
    "9155": ("Lancia del Chiaro di Luna", "Incalza il nemico con una saetta di purissima luce lunare trafiggente."),
    "9200": ("Spezzare Maledizioni", "Rimuove le afflizioni maledette dagli oggetti o dall'equipaggiamento."),
    "9210": ("Dissacrazione", "Infrange le protezioni sacre e i sigilli divini che schermano il bersaglio."),
    "9500": ("Scaccia Mostri", "Emana un'aura respingente che tiene lontane le creature aggressive."),
    "9501": ("Attira Mostri", "Diffonde un profumo che richiama frotte di mostri desiderosi di lottare."),
    "9502": ("Attira Metallo", "Richiama nelle vicinanze i rari e sfuggenti mostri metallici porta-tesori."),
    "10000": ("Tomba dei Fili Pallidi", "Una cripta avvolta da ragnatele eteree e segreti sopiti."),
    "10001": ("Banchetto Senza Fondo", "Una tavola imbandita di delizie la cui abbondanza non si esaurisce mai."),
    "10002": ("Stato di Allerta", "Mantiene i sensi tesi e l'arma pronta a sferrare il primo colpo."),
}

# Element conversions (850-866)
for elem_id, (elem_name, elem_prep) in ELEMENT_NAMES.items():
    conv_id = str(850 + elem_id)
    NAME_MAP[conv_id] = (
        f"Conversione {elem_name}",
        f"Converte una porzione del danno inflitto in danno da {elem_name.lower()}."
    )

# Matrix spells (50100 - 51399)
for shape_base, (shape_name, shape_template, shape_desc_template) in MATRIX_SHAPES.items():
    for elem_id, (elem_name, elem_prep) in ELEMENT_NAMES.items():
        spell_id = str(shape_base + elem_id)
        s_name = shape_template.format(elem=elem_name)
        s_desc = shape_desc_template.format(elem=elem_prep)
        NAME_MAP[spell_id] = (s_name, s_desc)

def run():
    wb = openpyxl.load_workbook(ELEMENT_FILE)
    ws = wb.active
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}

    updated_names = 0
    updated_details = 0
    updated_phases = 0

    for r in range(2, ws.max_row + 1):
        id_val = str(ws.cell(r, 1).value).strip() if ws.cell(r, 1).value is not None else ""
        if not id_val:
            continue

        # Check multi-tier feats first
        if id_val in FEATS_1600:
            f = FEATS_1600[id_val]
            ws.cell(r, headers['name']).value = f['name']
            if 'detail' in headers and f.get('detail'):
                ws.cell(r, headers['detail']).value = f['detail']
            if 'textPhase' in headers and f.get('textPhase'):
                ws.cell(r, headers['textPhase']).value = f['textPhase']
            updated_names += 1
            updated_details += 1
            updated_phases += 1
            continue

        # Check explicit NAME_MAP
        if id_val in NAME_MAP:
            it_name, it_detail = NAME_MAP[id_val]
            current_name = ws.cell(r, headers['name']).value
            name_en = ws.cell(r, headers['name_EN']).value
            if it_name and (current_name is None or str(current_name).strip() == "" or str(current_name).strip() == str(name_en).strip()):
                ws.cell(r, headers['name']).value = it_name
                updated_names += 1

            if it_detail and 'detail' in headers:
                current_detail = ws.cell(r, headers['detail']).value
                detail_en = ws.cell(r, headers['detail_EN']).value
                if current_detail is None or str(current_detail).strip() == "" or str(current_detail).strip() == str(detail_en).strip():
                    ws.cell(r, headers['detail']).value = it_detail
                    updated_details += 1

        # Check generic patterns
        name_en_col = headers.get('name_EN')
        name_it_col = headers.get('name')
        name_en = str(ws.cell(r, name_en_col).value).strip() if name_en_col and ws.cell(r, name_en_col).value else ""
        name_it = str(ws.cell(r, name_it_col).value).strip() if name_it_col and ws.cell(r, name_it_col).value else ""

        if (not name_it or name_it == name_en) and name_en:
            # Pattern: X Resistance
            if name_en.endswith(" Resistance"):
                base_elem = name_en[:-11]
                elem_trans = {
                    "Fire": "al Fuoco", "Cold": "al Gelo", "Lightning": "al Fulmine",
                    "Darkness": "alle Tenebre", "Mind": "alla Mente", "Poison": "al Veleno",
                    "Nether": "all'Oltretomba", "Sound": "al Suono", "Nerve": "ai Danni Nervini",
                    "Chaos": "al Caos", "Holy": "al Sacro", "Magic": "alla Magia",
                    "Ether": "all'Etere", "Acid": "all'Acido", "Cut": "al Taglio", "Impact": "all'Impatto",
                    "Cat": "ai Gatti"
                }.get(base_elem, f"a {base_elem}")
                ws.cell(r, name_it_col).value = f"Resistenza {elem_trans}"
                if 'detail' in headers and (not ws.cell(r, headers['detail']).value or ws.cell(r, headers['detail']).value == ws.cell(r, headers['detail_EN']).value):
                    ws.cell(r, headers['detail']).value = f"Protezione passiva e riduzione danni {elem_trans}."
                if 'textPhase' in headers and (not ws.cell(r, headers['textPhase']).value or ws.cell(r, headers['textPhase']).value == ws.cell(r, headers['textPhase_EN']).value):
                    ws.cell(r, headers['textPhase']).value = f"Aumenta la tua resistenza {elem_trans}."
                updated_names += 1

            # Pattern: Immunity to X
            elif name_en.startswith("Immunity to "):
                aff = name_en[12:].lower()
                aff_map = {
                    "poison": "al veleno", "blind": "alla cecità", "paralysis": "alla paralisi",
                    "fear": "alla paura", "sleep": "al sonno", "confusion": "alla confusione",
                    "pickpocket": "ai borseggi", "neck hunt": "alla decapitazione",
                    "shockwave": "alle onde d'urto", "sunburn": "alle scottature", "gravity": "alla gravità"
                }
                it_aff = aff_map.get(aff, f"a {aff}")
                ws.cell(r, name_it_col).value = f"Immunità {it_aff}"
                if 'textPhase' in headers and (not ws.cell(r, headers['textPhase']).value or ws.cell(r, headers['textPhase']).value == ws.cell(r, headers['textPhase_EN']).value):
                    ws.cell(r, headers['textPhase']).value = f"Conferisce totale immunità {it_aff}."
                updated_names += 1

            # Pattern: Favor of X
            elif name_en.startswith("Favor of the "):
                f_name = name_en[13:]
                f_map = {
                    "Element": "Favore degli Elementi", "Earth": "Favore della Terra",
                    "Wind": "Favore del Vento", "Strife": "Favore della Lotta",
                    "Harvest": "Favore del Raccolto", "Healing": "Favore della Guarigione",
                    "Trickery": "Favore dell'Inganno", "Knowledge": "Favore della Conoscenza",
                    "Machine": "Favore delle Macchine", "Fortune": "Favore della Fortuna"
                }
                if f_name in f_map:
                    ws.cell(r, name_it_col).value = f_map[f_name]
                    updated_names += 1

            # Pattern: Sustain X
            elif name_en.startswith("Sustain "):
                s_stat = name_en[8:]
                s_map = {
                    "Strength": "Sostegno Forza", "Endurance": "Sostegno Costituzione",
                    "Dexterity": "Sostegno Destrezza", "Perception": "Sostegno Percezione",
                    "Learning": "Sostegno Apprendimento", "Will": "Sostegno Volontà",
                    "Magic": "Sostegno Magia", "Charisma": "Sostegno Carisma",
                    "Speed": "Sostegno Velocità", "Luck": "Sostegno Fortuna"
                }
                if s_stat in s_map:
                    ws.cell(r, name_it_col).value = s_map[s_stat]
                    if 'textPhase' in headers:
                        ws.cell(r, headers['textPhase']).value = f"Preserva il valore di {s_stat}."
                    updated_names += 1

            # Pattern: Summon X
            elif name_en.startswith("Summon "):
                s_target = name_en[7:]
                s_map = {
                    "Animal": "Evoca Animali", "Fire": "Evoca Fiamme", "Metal": "Evoca Creatura Metallica",
                    "Undead Younger Sister": "Evoca Sorellina Non-Morta",
                    "Younger Sisteroid": "Evoca Sorellina Meccanica"
                }
                ws.cell(r, name_it_col).value = s_map.get(s_target, f"Evoca {s_target}")
                updated_names += 1

    wb.save(ELEMENT_FILE)
    print(f"Element.xlsx updated successfully! Names: {updated_names}, Details: {updated_details}, Phases: {updated_phases}")

if __name__ == "__main__":
    run()
