# coding: utf-8
import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ELEMENT_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Game', 'Element.xlsx')

ELEMENT_NAMES = {
    0: ('Fuoco', 'al fuoco'),
    1: ('Gelo', 'al gelo'),
    2: ('Fulmine', 'al fulmine'),
    3: ('Tenebre', 'alle tenebre'),
    4: ('Mente', 'alla mente'),
    5: ('Veleno', 'al veleno'),
    6: ('Oltretomba', 'all\'oltretomba'),
    7: ('Suono', 'al suono'),
    8: ('Nervino', 'ai danni nervini'),
    9: ('Caos', 'al caos'),
    10: ('Sacro', 'al sacro'),
    11: ('Magia', 'alla magia'),
    12: ('Etere', 'all\'etere'),
    13: ('Acido', 'all\'acido'),
    14: ('Taglio', 'al taglio'),
    15: ('Impatto', 'all\'impatto'),
    16: ('Vuoto', 'al vuoto'),
}

MATRIX_SHAPES = {
    50100: ('Sfera', 'Sfera di {elem}', 'Evoca una sfera magica di {elem} attorno a chi la lancia, investendo i nemici nell\'area.'),
    50200: ('Soffio', 'Soffio di {elem}', 'Rilascia un potente soffio di {elem} concentrato in un cono frontale.'),
    50300: ('Dardo', 'Dardo di {elem}', 'Trafigge il bersaglio e la traiettoria con un raggio magico di {elem}.'),
    50400: ('Tocco', 'Tocco di {elem}', 'Concentra pura energia di {elem} nel palmo, scatenandola a distanza ravvicinata.'),
    50500: ('Freccia', 'Freccia di {elem}', 'Scaglia una saetta perforante di {elem} contro il bersaglio.'),
    50600: ('Fuso Orbitante', 'Fuso di {elem}', 'Materializza una massa senziente di energia di {elem} che dà la caccia al bersaglio.'),
    50700: ('Miasma', 'Miasma di {elem}', 'Genera una nube persistente di {elem} che consuma gradualmente le forze del nemico.'),
    50800: ('Canto', 'Canto di {elem}', 'Infonde l\'arma dell\'esecutore con il potere di {elem}.'),
    50900: ('Marea', 'Marea di {elem}', 'Scatena una marea travolgente di energia di {elem}.'),
    51000: ('Spada Arcana', 'Lama di {elem}', 'Evoca una lama spettrale di {elem} che trafigge e squarcia le difese bersaglio.'),
    51100: ('Bit', 'Modulo Orbitante di {elem}', 'Materializza un costrutto difensivo orbitante intriso di {elem}.'),
    51200: ('Brillamento', 'Brillamento di {elem}', 'Fa detonare violentemente l\'energia di {elem} accumulata nel bersaglio.'),
    51300: ('Cometa', 'Cometa di {elem}', 'Invoca una cometa astrale intrisa di {elem} che si schianta sull\'area indicata.'),
}

FEATS_1600 = {
    '1610': {
        'name': 'Apprendista Asceta\nPraticante Asceta\nEsperto Asceta\nMaestro Asceta\nAsceta Leggendario',
        'detail': 'La pratica dell\'ascesi e della rinuncia fortifica prodigiosamente la tua forza vitale.',
        'textPhase': 'Sei un apprendista della via ascetica.\nSei un praticante della via ascetica.\nSei un esperto della via ascetica.\nSei un maestro della via ascetica.\nSei un asceta leggendario.'
    },
    '1611': {
        'name': 'Gene Magico\nCellula Magica\nSangue Magico\nCorpo Arcano\nEntità Magica',
        'detail': 'Ottieni riserve addizionali di mana manipolando la tua struttura genetica.',
        'textPhase': 'I tuoi geni racchiudono scintille magiche.\nLe tue cellule vibrano di pura magia.\nIl tuo sangue è intriso di essenza arcana.\nIl tuo corpo è forgiato nella magia.\nLa pura energia magica domina ogni fibra del tuo essere.'
    },
    '1612': {
        'name': 'Velocista\nMezzofondista\nMaratoneta',
        'detail': 'L\'allenamento costante nella corsa aumenta la tua velocità di movimento sul campo.',
        'textPhase': 'Sei un velocista sulle brevi distanze.\nSei un corridore esperto sulle medie distanze.\nSei un maratoneta instancabile sulle lunghe distanze.'
    },
    '1620': {
        'name': 'Braccio di Ferro\nMaestro di Braccio di Ferro\nCampione di Braccio di Ferro',
        'detail': 'Allenarsi nel braccio di ferro incrementa la tua Forza muscolare.',
        'textPhase': 'Hai una presa d\'acciaio nel braccio di ferro.\nSei un temuto sfidante nel braccio di ferro.\nSei l\'imbattuto campione di braccio di ferro.'
    },
    '1621': {
        'name': 'Dita Flessibili\nDita da Artigiano\nDita Prodigiose',
        'detail': 'Esercitare la manualità fine aumenta la tua Destrezza.',
        'textPhase': 'Le tue dita sono straordinariamente agili.\nHai la precisione manuale di un mastro orologiaio.\nLe tue dita compiono autentici prodigi di destrezza.'
    },
    '1622': {
        'name': 'Resistente\nMolto Resistente\nIndomito',
        'detail': 'Sopportare fatiche estreme aumenta la tua Costituzione.',
        'textPhase': 'Sei abituato a sopportare dolori e percosse.\nLa tua soglia di sopportazione fisica è straordinaria.\nPossiedi una resistenza incrollabile e indomita.'
    },
    '1623': {
        'name': 'Occhio della Vedetta\nOcchio del Ladro\nVista d\'Aquila',
        'detail': 'Affinare l\'attenzione verso l\'ambiente aumenta la tua Percezione.',
        'textPhase': 'I tuoi occhi notano anche i minimi movimenti nell\'ombra.\nScorgi immediatamente trappole, borse e oggetti nascosti.\nPossiedi una vista penetrante come quella di un\'aquila.'
    },
    '1624': {
        'name': 'Curioso\nStudioso\nTopo di Biblioteca',
        'detail': 'Coltivare la sete di sapere aumenta il tuo Apprendimento.',
        'textPhase': 'Nutri un\'insaziabile curiosità verso ogni mistero.\nDedichi ore appassionate allo studio e alla teoria.\nSei un erudito consumato che divora tomi e pergamene.'
    },
    '1625': {
        'name': 'Spirituale\nMistico\nSesto Senso',
        'detail': 'La devozione e la comunione con l\'invisibile aumentano la tua Volontà.',
        'textPhase': 'Senti la presenza sottile del regno spirituale.\nSei in profonda armonia mistica con il cosmo.\nPossiedi un autentico sesto senso che ti guida nel buio.'
    },
    '1626': {
        'name': 'Volontà Ferrea\nVolontà d\'Acciaio\nSpirito Indomabile',
        'detail': 'La determinazione granitica ti permette di resistere a ogni avversità e influenza mentale.',
        'textPhase': 'Possiedi una ferma determinazione interiore.\nLa tua forza di volontà è dura come l\'acciaio temprato.\nIl tuo spirito è fiero, indomabile e incorruttibile.'
    },
    '1627': {
        'name': 'Seduttore\nRomantico\nConquistatore Fatale',
        'detail': 'Affinare i modi galanti e la presenza scenica aumenta il tuo Carisma.',
        'textPhase': 'Emani un fascino magnetico e seducente.\nI tuoi modi romantici incantano chiunque ti ascolti.\nPossiedi una presenza scenica travolgente e irresistibile.'
    },
    '1628': {
        'name': 'Fortunato\nBaciato dalla Fortuna\nPrediletto della Dea',
        'detail': 'Il favore della sorte ti accompagna aumentando la tua Fortuna.',
        'textPhase': 'Sembri avere sempre un pizzico di fortuna dalla tua parte.\nLa buona sorte ti assiste nei momenti più critici.\nSei il prediletto assoluto della Dea bendata.'
    },
    '1629': {
        'name': 'Scattante\nFulmineo',
        'detail': 'Riflessi pronti e gambe reattive che aumentano la tua Velocità.',
        'textPhase': 'I tuoi riflessi sono reattivi e scattanti.\nTi muovi con la rapidità fulminea del lampo.'
    },
    '1630': {
        'name': 'Difesa di Pietra\nDifesa di Ferro\nDifesa d\'Acciaio',
        'detail': 'Aumenta il valore di Protezione dall\'Armatura (PV).',
        'textPhase': 'Il tuo corpo assorbe i colpi come roccia solida.\nLe tue difese sono impenetrabili come il ferro battuto.\nSei una fortezza inespugnabile protetta da piastre d\'acciaio.'
    },
    '1631': {
        'name': 'Schivata\nSchivata Migliorata\nSchivata Perfetta',
        'detail': 'Aumenta il valore di Schivata Difensiva (DV).',
        'textPhase': 'Sai disimpegnarti prontamente dalla traiettoria dei colpi.\nEludi gli attacchi avversari con consumata maestria.\nTi muovi tra i fendenti con la grazia eterea di uno spettro.'
    },
    '1632': {
        'name': 'Evasione\nEvasione Migliorata\nEvasione Superiore',
        'detail': 'Conferisce una probabilità aggiuntiva di evitare del tutto gli assalti nemici.',
        'textPhase': 'Riesci a sottrarti agli attacchi più insidiosi.\nLe probabilità di sfuggire ai colpi nemici aumentano.\nSei quasi impossibile da colpire di sorpresa.'
    },
    '1633': {
        'name': 'Ricognitore\nRicognitore Esperto\nMaestro Esploratore',
        'detail': 'Migliora la capacità di individuare trappole e dettagli celati nel terreno.',
        'textPhase': 'Noti indizi e tracce sfuggite agli altri.\nIndividui al primo sguardo passaggi segreti e meccanismi celati.\nNessun segreto del sottosuolo può sfuggire al tuo occhio.'
    },
    '1634': {
        'name': 'Negoziatore\nGrande Negoziatore',
        'detail': 'Migliora l\'abilità nella compravendita ottenendo sconti e prezzi migliori.',
        'textPhase': 'Sai contrattare abilmente con i bottegai.\nSei un maestro supremo nell\'arte della compravendita.'
    },
    '1635': {
        'name': 'Artista Marziale\nSanto della Spada',
        'detail': 'Aumenta sensibilmente il danno inflitto a mani nude o con armi marziali.',
        'textPhase': 'Padroneggi le basi delle arti marziali orientali.\nHai raggiunto l\'apice mistico della via della spada.'
    },
    '1636': {
        'name': 'Fedele\nZelota',
        'detail': 'Aumenta l\'accumulo di devozione verso la divinità prescelta.',
        'textPhase': 'La tua devozione verso gli dèi è sincera e profonda.\nLa tua fede incrollabile rasenta il fanatismo mistico.'
    },
    '1640': {
        'name': 'Amico degli Animali',
        'detail': 'Facilita l\'addomesticamento delle bestie e impedisce loro di attaccarti a vista.',
        'textPhase': 'Le bestie della foresta percepiscono la tua benevolenza.'
    },
    '1641': {
        'name': 'Esorcista',
        'detail': 'Aumenta l\'efficacia contro spiriti irrequieti, spettri e creature non-morte.',
        'textPhase': 'I tuoi colpi dissipano le ombre della non-morte.'
    },
    '1642': {
        'name': 'Sonno Ristoratore\nSonno Profondo\nMaestro del Sonno',
        'detail': 'Dormire ripristina le forze vitali, il mana e il vigore molto più rapidamente.',
        'textPhase': 'Un breve riposo basta a farti sentire rinvigorito.\nIl tuo sonno è profondo, tranquillo e immensamente ristoratore.\nPadronanza assoluta del sonno: ti risvegli sempre al massimo delle energie.'
    },
    '1643': {
        'name': 'Ordinato\nMetodico\nManiaco dell\'Ordine',
        'detail': 'Migliora l\'efficienza nell\'organizzazione dello zaino e riduce il tempo perso a cercare oggetti.',
        'textPhase': 'Ti piace mantenere le tue cose ben ordinate.\nOrganizzi meticolosamente ogni cassa e scomparto.\nOgni singolo oggetto ha il suo posto preciso e catalogato.'
    },
    '1644': {
        'name': 'Mutazione Corporea',
        'detail': 'Favorisce mutazioni corporee favorevoli durante l\'esposizione alle correnti caotiche.',
        'textPhase': 'Il tuo corpo risponde alle mutazioni con eccezionale flessibilità.'
    },
    '1645': {
        'name': 'Anima della Festa',
        'detail': 'Intrattenere il pubblico con la musica o la conversazione diverte tutti molto più in fretta.',
        'textPhase': 'Sei il centro dell\'attenzione in ogni taverna e banchetto.'
    },
    '1646': {
        'name': 'Anima Solitaria',
        'detail': 'Ottieni bonus al combattimento quando viaggi ed esplori privo di alleati o compagni.',
        'textPhase': 'La solitudine tempra il tuo spirito rendendoti più forte.'
    },
    '1647': {
        'name': 'Pastore',
        'detail': 'Migliora la resa di latte, uova e lana dagli animali da allevamento.',
        'textPhase': 'Sai prenderti cura del bestiame con mano esperta e amorevole.'
    },
    '1648': {
        'name': 'Lancio Rapido',
        'detail': 'Riduce il tempo necessario per recitare e canalizzare gli incantesimi.',
        'textPhase': 'Riesci a recitare formule arcane con straordinaria rapidità.'
    },
    '1649': {
        'name': 'Difensore',
        'detail': 'Aumenta le difese e ti permette di proteggere i compagni adiacenti dai colpi nemici.',
        'textPhase': 'Ti poni a baluardo in difesa dei tuoi compagni.'
    },
    '1650': {
        'name': 'Buongustaio',
        'detail': 'Apprendi come riconoscere le proprietà nutritive e i benefici nascosti di ogni piatto.',
        'textPhase': 'Sai discernere all\'istante il valore nutritivo e le spezie di ogni vivanda.'
    },
    '1651': {
        'name': 'Galateo Magico',
        'detail': 'Impedisce alle magie d\'area di danneggiare o infastidire gli abitanti pacifici delle città.',
        'textPhase': 'Controlli le fiamme e l\'energia arcana per non recare danno a passanti inermi.'
    },
    '1652': {
        'name': 'Raffica di Frecce',
        'detail': 'Consente di incoccare e scagliare dardi a una velocità straordinaria.',
        'textPhase': 'Scagli una tempesta ininterrotta di proiettili sul bersaglio.'
    },
    '1653': {
        'name': 'Risveglio Onirico',
        'detail': 'Conserva la lucidità mentale all\'interno dei sogni permettendo rivelazioni mistiche.',
        'textPhase': 'Padroneggi l\'onironautica e mantieni il controllo nei sogni.'
    },
    '1654': {
        'name': 'Incantatore Corazzato Base\nIncantatore Corazzato Avanzato\nMaestro Incantatore Corazzato',
        'detail': 'Riduce la penalità al successo del lancio di incantesimi causata da armature pesanti.',
        'textPhase': 'Riesci a canalizzare incantesimi indossando armature di cuoio rinforzato.\nIncanti con disinvoltura protetto da cotte di maglia e piastre parziali.\nLanci incantesimi anche avvolto da una corazza di piastre completa senza esitazione.'
    },
    '1655': {
        'name': 'Fedele Modello',
        'detail': 'Offrire doni e sacrifici all\'altare divino genera il doppio del favore celeste.',
        'textPhase': 'Le tue offerte all\'altare sono gradite e benedette dalla divinità.'
    },
    '1656': {
        'name': 'Riciclatore di Rottami',
        'detail': 'Permette di estrarre materiali utili da rottami, carcasse e rifiuti altrimenti inutilizzabili.',
        'textPhase': 'Sai ricavare risorse preziose anche dai mucchi di scarti.'
    },
    '1657': {
        'name': 'Risparmio Magico',
        'detail': 'Insegna come ottimizzare la canalizzazione dell\'energia arcana per consumare meno mana.',
        'textPhase': 'Sai come preservare il tuo mana evitando ogni dispersione energetica.'
    },
    '1658': {
        'name': 'Cuoco Itinerante',
        'detail': 'Permette di preparare manicaretti deliziosi anche all\'aperto con un semplice focolare da campo.',
        'textPhase': 'Cucini piatti squisiti anche nelle condizioni più selvagge.'
    },
    '1659': {
        'name': 'Prima Cattura',
        'detail': 'Aumenta la probabilità di pescare pesci rari e tesori sommersi con la lenza.',
        'textPhase': 'La tua lenza attira prede straordinarie fin dal primo lancio.'
    },
    '1660': {
        'name': 'Saccheggiatore',
        'detail': 'Aumenta il bottino di monete d\'oro e gemme rinvenuto dai nemici sconfitti.',
        'textPhase': 'Trovi sempre qualcosa di valore nei resti dei tuoi nemici.'
    },
    '1661': {
        'name': 'Demolitore',
        'detail': 'Migliora la capacità di abbattere strutture, pareti rocciose e porte con violenza inaudita.',
        'textPhase': 'I tuoi colpi frantumano pietre, legname e murature con facilità disarmante.'
    },
    '1662': {
        'name': 'Dita d\'Oro',
        'detail': 'La suprema abilità ladresca nel sottrarre oggetti di immenso valore senza alcun rischio.',
        'textPhase': 'Eccelli nell\'arte del borseggio e del furto con destrezza ineguagliata.'
    },
    '1663': {
        'name': 'Mangiatore Veloce',
        'detail': 'Permette di consumare cibi e bevande in un solo istante anche durante le concitate fasi di battaglia.',
        'textPhase': 'Divori provviste e pozioni con una velocità fulminea.'
    },
    '1664': {
        'name': 'Missionario dell\'Amore',
        'detail': 'Diffonde amore, gioia e concordia tra la popolazione di Ylva, pacificando gli animi inquieti.',
        'textPhase': 'La tua sola presenza irraggia calore, affetto e concordia universale.'
    }
}
