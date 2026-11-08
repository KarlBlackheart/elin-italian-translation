# coding: utf-8
"""
Elin Italian Localization - Drama ashland.xlsx Localizer
Translates all 117 dialogue rows of Ashland:
- Greeting & recovery at the meadow camp
- Handing over the Land Deed, hatchet, 10 gold bars
- Tutorials: gathering, fatigue, crafting, combat, shared containers
- Lore of Mysilia: Lord Cetrus, Vindale, Elea vs Humans, House Torres, brother Ephrond
- Taxes and Mysilia court bills (mailbox reward)
- The Council of Tyris Union
- Exploring Nymelle & reporting on the mysterious ether crystal and Onev
- Introducing Loytel, the First-Class Frontier Inspector
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ASHLAND_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama', 'ashland.xlsx')

ASHLAND_DATA = {
    16: "È un piacere rivederti in piedi. Come procedono i lavori di bonifica del tuo feudo?",
    17: "Ti stai abituando alla vita qui a Tyris? Ogni tanto fa bene spezzare la routine e mettersi in viaggio per visitare le città delle altre regioni.",
    18: (
        "Vedo che sei tornato tutto intero.\n\n"
        "Io sono Ashland. Sono in viaggio verso la capitale reale di Palmia assieme alla mia compagna. Non sei pratico di queste contrade, vero? Prima di congedarci, potrei dedicare un po' del mio tempo a insegnarti le basi della sopravvivenza in queste terre. Se lo desideri, s'intende."
    ),
    21: "Cos'è l'atto di proprietà della terra?",
    22: "Qual è il mio obiettivo di bonifica?",
    23: "Insegnami le basi per vivere e sopravvivere.",
    24: "Avrei alcune domande da farti.",
    31: (
        "Ti senti un po' meglio?\n\n"
        "Prima di tutto, prendi questo: te lo sei meritato.\n"
        "(L'uomo ti lancia con noncuranza un foglio di pergamena sigillato.)\n\n"
        "Non farti troppi scrupoli: è solo una quota di concessione governativa. Anche se 'atto di proprietà fondiaria' suona altisonante, al giorno d'oggi dubito che a qualcuno importi granché di una simile terra selvaggia. Se preferisci, puoi sempre gettarlo nel fuoco del falò per quanto mi riguarda!"
    ),
    37: (
        "Congratulazioni, d'ora in poi questa terra appartiene a te!\n\n"
        "Per celebrare questo tuo nuovo inizio, ti faccio dono di un'accetta. Ti sarà di vitale utilità mentre ti farai strada tra la boscaglia e gli alberi incolti."
    ),
    39: (
        "E questi sono 10 lingotti d'oro: le scorte di sussistenza e soccorso fornite dal regno di Mysilia.\n\n"
        "I lingotti d'oro sono una risorsa preziosissima: possono essere usati per assoldare nuovi coloni e residenti, oppure barattati per manufatti essenziali allo sviluppo del tuo feudo.\n\n"
        "Fiama tiene in custodia alcuni arredi basilari per la casa, quindi non dimenticare di acquistarli prima che partiamo."
    ),
    41: (
        "Ci tratterremo qui ancora per un po' ad osservare come evolverà la situazione. Ehi, mi sento in parte responsabile per aver ridestato il tuo ardore di pioniere!"
    ),
    43: "Ho affisso alcuni incarichi e annunci sulla bacheca. Dagli un'occhiata quando hai un attimo di respiro.",
    49: (
        "Oh, quel pezzo di carta?\n\n"
        "È un 'atto di proprietà fondiaria'. Mysilia è alla disperata ricerca di pionieri volenterosi, perciò concediamo terreni a titolo gratuito ad avventurieri promettenti.\n\n"
        "...Be', naturalmente case accoglienti e coloni laboriosi non spuntano dal nulla per magia. Dovrai aprirti un varco a colpi di lama tra i rovi, e non ci sarà nessuno a difendere il tuo confine da predoni e belve feroci. E prima o poi, dovrai anche pagare le tasse regie."
    ),
    50: (
        "Non ho intenzione di mentirti: io e Fiama siamo al servizio di Mysilia, e Mysilia ha un disperato bisogno di alleati fidati e forzieri colmi d'oro.\n\n"
        "Dunque il mio calcolo segreto è farti pesare il favore di averti salvato la pelle, nella speranza che tu decida di fondare un paio di fiorenti borghi commerciali per nostro conto! (Ti rivolge un ghigno beffardo)"
    ),
    51: (
        "A dire il vero, questa radura non sembra affatto male per un nuovo insediamento. Perché non cerchi un bel punto panoramico e provi a leggere l'atto di proprietà?"
    ),
    55: (
        "Cosa desideri costruire su queste terre?\n\n"
        "Una locanda accogliente dove i viaggiatori possano riposare le membra stanche, una bottega artigiana dove mastri forgiatori mostrino il loro talento, oppure un quieto villaggio agreste circondato da spighe dorate di grano... Se hai un sogno nel cuore, quello è il tuo 'obiettivo'.\n\n"
        "Finché riuscirai a versare nelle casse della corona le entrate pattuite, non verremo a dirti cosa devi o non devi fare. Be', se non sai da dove cominciare, dai un'occhiata alla bacheca: vi ho affisso alcuni incarichi per farti muovere i primi passi."
    ),
    60: "Cosa desideri sapere?",
    61: "Chi era la fanciulla Elea che ho scorto?",
    62: "Cos'è esattamente un Nefia?",
    63: "Parlami dell'attuale situazione politica di Mysilia.",
    64: "Parlami di messer Cetrus.",
    65: "Parlami dei rapporti tra Umani ed Elea.",
    66: "Parlami del casato dei Torres.",
    67: "(Torna indietro)",
    74: "Quale argomento desideri approfondire?",
    75: "Raccogliere e utilizzare oggetti.",
    76: "Raccolta risorse e affaticamento.",
    77: "Fabbricazione e artigianato.",
    78: "Combattimento e tattiche.",
    79: "Abilità speciali e incantesimi.",
    80: "Nutrimento, sonno e vita quotidiana.",
    81: "Campo visivo e fonti di luce.",
    82: "(Torna indietro)",
    84: "Campo visivo e fonti di luce.",
    87: (
        "Per prima cosa, lascia che ti spieghi come raccogliere e impiegare gli oggetti.\n\n"
        "Gli oggetti sparsi al suolo possono essere raccolti automaticamente camminandovi sopra, mentre gli elementi posizionati, come i mobili, devono prima essere presi in mano facendo clic destro su di essi.\n\n"
        "Quando impugni un oggetto, puoi fare clic destro sul terreno per posizionarlo di nuovo, oppure cliccare sul tuo personaggio per riporlo nello zaino.\n\n"
        "Raccogliere oggetti collocati all'interno delle città è considerato furto e richiede l'arte del borseggio, ma per ora non c'è alcun bisogno di imparare simili nefandezze."
    ),
    88: (
        "Fai clic sull'icona dell'inventario in basso a destra dello schermo per aprire il tuo zaino. Gli oggetti al suo interno possono essere spostati liberamente trascinandoli col mouse.\n\n"
        "Risorse come cibo e tomi possono essere consumati o letti direttamente con un clic destro. Puoi anche premere il tasto centrale del mouse (o il tasto R) per visualizzare l'elenco completo delle azioni possibili.\n\n"
        "Gli slot della barra degli strumenti inferiore possono essere scambiati rapidamente con la rotella del mouse, così da alternare all'istante utensili e consumabili di uso frequente."
    ),
    93: (
        "Per i primi tempi, le risorse naturali saranno la linfa vitale della tua esistenza. Funghi selvatici e bacche rappresentano una preziosa fonte di sostentamento. Puoi abbattere alberi e spaccare pietre per ricavare legname e blocchi con cui costruire arredi ed edifici.\n\n"
        "Puoi tentare di raccogliere le risorse presenti sulla mappa cliccandovi sopra con il tasto destro. Tieni presente, tuttavia, che alcune di esse richiedono attrezzi specifici, come un'accetta o un piccone."
    ),
    94: (
        "Determinate mansioni, come la raccolta o lo scavo, consumano la tua resistenza fisica. Se la fatica si accumula eccessivamente, la rigenerazione naturale della salute si arresta, e continuare a sforzarsi comporta il rischio concreto di svenire sul colpo.\n\n"
        "Esistono pochissimi modi per riprendersi dal collasso da fatica, quindi finché il tuo fisico non sarà temprato ti consiglio la massima cautela.\n\n"
        "Se ti senti troppo sfinito persino per camminare, una bella notte di sonno in un letto ti rimetterà al mondo. E se non hai un giaciglio a portata di mano, prova a fare ricorso all'abilità 'Riposa'."
    ),
    99: (
        "Strutture come falò e banchi da lavoro possono essere impiegate per fabbricare oggetti, a patto di possedere le materie prime richieste.\n\n"
        "All'inizio la gamma di oggetti che sarai in grado di forgiare sarà piuttosto modesta; tuttavia, man mano che rinvieni nuove formule e ricette durante i tuoi viaggi, potrai dare vita a manufatti sempre più raffinati e complessi."
    ),
    100: (
        "Durante la fabbricazione puoi attingere sia ai materiali presenti nel tuo zaino, sia a quelli stipati nei contenitori circostanti, purché ti appartengano legittimamente.\n\n"
        "Se il tuo livello nelle abilità artigianali necessarie è insufficiente, la creazione richiederà un dispendio spropositato di energia. Ti suggerisco pertanto di impratichirti assemblando articoli semplici prima di cimentarti con ricette di alto rango."
    ),
    106: "(In arrivo!)",
    111: "(In arrivo!)",
    117: "(In arrivo!)",
    123: "(In arrivo!)",
    134: (
        "Come dici? Hai scorto una fanciulla Elea nei meandri della boscaglia?\n\n"
        "Ah! Devi aver intravisto Fiama attraverso il velo del tuo delirio. Dovrebbe essere ancora da queste parti. È stata proprio lei a trovarti quando giacevi privo di sensi sul terreno."
    ),
    135: (
        "Fia è una comune umana, ma non sei certo il primo a prendere un simile abbaglio.\n\n"
        "Lei... possiede il dono di udire la voce delle foreste. Ricordo che poco fa farfugliava frasi insolite... sosteneva che una bambina apparsa nei suoi sogni ci avesse guidato fin qui. Chissà cosa intendesse dire davvero."
    ),
    139: (
        "In tutta Tyris si contano innumerevoli rovine inviolate e sotterranei dimenticati, che noi chiamiamo 'Nefia'. Le leggende narrano di tesori d'inestimabile valore sepolti nei recessi più oscuri, ma sarebbe una pazzia precipitarsi laggiù a meno che tu non sia un avventuriero di straordinaria perizia."
    ),
    143: (
        "Mysilia è un principato retto dal vecchio duca Jonan, incastonato sul confine che separa Tyris Settentrionale dalle catene montuose a sud. Per lunghi secoli, le genti umane e gli Elea vi hanno prosperato fianco a fianco in fraterna armonia.\n\n"
        "Si racconta che circa un secolo fa il mio venerabile signore, messer Cetrus, giunse in queste terre quale messaggero di Vindale assieme alla sua compagna, madonna Frine. Entrambi scelsero di rimanere nel nostro mondo mortale e furono a lungo venerati dal popolo quale simbolo vivente della concordia tra le due razze.\n\n"
        "Mysilia non è mai stata una terra opulenta, ma era un regno ricolmo di quiete e di speranza."
    ),
    144: (
        "Ma l'ultimo conflitto, conclusosi quindici anni or sono, ha inferto ferite sanguinanti a Mysilia e ha spezzato i legami di fiducia tra le due stirpi.\n\n"
        "Vindale scelse di rimanere sorda ai nostri disperati appelli, lasciando che Tyris venisse calpestata e razziata dall'Impero. Il veleno del risentimento germogliato tra gli umani ha proiettato una cupa ombra di astio su Mysilia, la nazione che più di ogni altra incarnava l'unione dei due popoli.\n\n"
        "La voce di messer Cetrus non trova più ascolto tra la plebe. E mentre i nostri connazionali si scannano per contendersi le ultime spighe di grano su terre desolate, gli sciacalli degli stati confinanti e i burocrati della Dieta assistono con sorrisi di scherno alle nostre sventure.\n\n"
        "Questa è la tragica realtà del nostro paese."
    ),
    145: (
        "Forse per Mysilia non v'è più speranza alcuna, e i giorni in cui umani ed Elea si stringevano la mano non torneranno mai più.\n\n"
        "Eppure messer Cetrus non si è ancora arreso. E anch'io farò la mia parte fino all'ultimo respiro per la mia terra natia... o meglio, per il mio nobile signore Cetrus."
    ),
    149: (
        "Avrai sicuramente udito le sue gesta nei racconti dei viandanti. Signore di Willow, Marchese delle Terre di Confine, Figlio dell'Antica Foresta ed Eroe di Nymelle... i titoli non si contano.\n\n"
        "Messer Cetrus e la nobile Frine giunsero qui da Vindale. Hanno dimorato a Mysilia sostenendo il Casato dei Torres e l'intera nazione per generazioni. È un saggio dotato di un carisma e di una benevolenza rari a trovarsi."
    ),
    150: (
        "I prodigi da lui compiuti durante la Guerra dei Dieci Anni sono ancora scolpiti a fuoco nella memoria della gente. Quel giorno fatale... quello spettacolo... è ancora impresso dinanzi agli occhi di ogni cittadino di Mysilia.\n\n"
        "Mi trovavo sui bastioni di Forte Willow, con lo sguardo rivolto al cielo cupo, a maledire la colossale aeronave da guerra Cyran che avanzava inesorabile su Mysilia, nell'assoluta impotenza di fare alcunché. Messer Cetrus si era chiuso in un cupo silenzio dopo la scomparsa di madonna Frine; eppure uscì dalle sue stanze proprio mentre i difensori della fortezza cominciavano a radunarsi. Sollevò lo sguardo verso le nubi con infinita mestizia e pronunciò antiche parole nell'arcana lingua degli Elea.\n\n"
        "D'improvviso, un fascio di luce azzurrina squarciò i cieli di Nymelle. E allora..."
    ),
    151: (
        "Non possiedo parole umane sufficienti a descrivere ciò che accadde. Una tempesta azzurra infuriò attraverso il firmamento e l'aeronave Cyran venne inghiottita da un turbine furioso. Quando la burrasca si placò, nessuno tra i presenti riusciva ad articolare verbo: fissavamo tutti attoniti la scia di fuoco scarlatto che precipitava lentamente verso il suolo. E quando posai lo sguardo su messer Cetrus, vidi che stava piangendo.\n\n"
        "...Con l'annientamento dell'ammiraglia Cyran, ritenuta fino ad allora inespugnabile, l'Impero diede inizio alla ritirata generale da Tyris e dal resto del continente. Fu così che la Guerra dei Dieci Anni giunse al termine."
    ),
    157: (
        "Gli Elea camminavano su questa terra molto prima che l'umanità erigesse la sua prima dimora. Nelle epoche arcaiche, gli uomini contemplavano con sacro terrore la loro sapienza millenaria e i loro poteri arcani, giungendo a chiamarli Madri o a venerarli come veri e propri dèi.\n\n"
        "Gli Elea sono creature magnifiche, pacifiche e riservate. Condivisero con i mortali molti segreti del cosmo, ma senza mai immischiarsi troppo nei loro affari. Dimoravano nelle profondità delle foreste cerulee e raramente si mostravano all'occhio umano. Le fronde dei loro boschi primordiali esalavano un miasma tossico che respingeva caparbiamente ogni intruso mortale..."
    ),
    158: (
        "Come ben saprai, al giorno d'oggi i rapporti tra le due razze sono ai minimi storici. La gente cova un profondo rancore per il silenzio serbato dagli Elea durante la Guerra dei Dieci Anni. C'è persino chi sostiene che la loro stessa presenza abbia tarpato le ali all'indipendenza e all'ingegno degli umani.\n\n"
        "Ma quando mai gli Elea hanno giurato alleanza all'umanità, o hanno preteso di farci da tutori? Siamo stati noi a battezzarli arbitrariamente 'madri', e ora pretendiamo di fare le vittime perché ci sentiamo trascurati! Non è altro che ipocrisia urlata a gran voce per mascherare un vile senso d'inferiorità e una dipendenza egoistica.\n\n"
        "E dietro ogni coro d'odio della plebe, si cela invariabilmente la bieca brama di potere di qualche tiranno. Già... benvenuto nel meraviglioso mondo degli uomini!"
    ),
    163: (
        "Messer Cetrus e madonna Frine sono figure sacre per chiunque appartenga al Casato dei Torres. Per noi sono stati come genitori che hanno vegliato sui nostri primi passi, sacerdoti al capezzale dei moribondi, custodi della storia di Mysilia e amici fidati con cui condividere dolori e gioie.\n\n"
        "Il duca Jonan... mio padre sorride ancora come un fanciullo quando si trova al suo cospetto. Un sorriso luminoso che non ha mai riservato né a me né a mio fratello."
    ),
    164: (
        "Nelle fredde e austere sale di pietra della corte di Mysilia, persino fratelli dello stesso sangue finiscono per guardarsi con distacco e diffidenza. Da ragazzino ero immensamente affascinato da loro due: erano così uniti, così pronti a sostenersi l'un l'altro in ogni frangente.\n\n"
        "Ridi pure di me, se credi; ma dovunque si trovassero messer Cetrus e madonna Frine, vi regnava sempre una perfetta, celestiale armonia."
    ),
    209: (
        "Mi rincresce spegnere il tuo entusiasmo mentre sei così indaffarato a bonificare la tua nuova dimora, ma è una verità con cui dovrai fare i conti prima o poi.\n\n"
        "Questa terra ti appartiene, ed è tuo pieno diritto gestirla come meglio credi. Tuttavia, trovandosi entro i confini del principato di Mysilia, qualunque bene o capo di bestiame presente su di essa deve essere registrato nei registri del catasto regio.\n\n"
        "Riceverai periodicamente cartelle esattoriali per il pagamento dei tributi. E ti avverto: una sorte assai cupa attende coloro che osano rendersi morosi col fisco!"
    ),
    210: "...Be', mancano ancora diverse settimane. Per il momento non angustiarti troppo e pensa solo a far prosperare il tuo insediamento.",
    216: (
        "A quanto vedo la prima cartella esattoriale è infine stata recapitata!\n\n"
        "Lascia che ti spieghi la procedura per adempiere al pagamento. La modalità in sé è elementare, non serve agitarsi. La vera incognita consiste nell'avere i fondi a disposizione!"
    ),
    217: (
        "Prendi la cartella che hai ricevuto e recati nella capitale di Mysilia. All'interno del palazzo municipale troverai la cassetta tributaria: ti basterà depositare la cartella assieme alla somma richiesta.\n\n"
        "Liberarsi di un simile fardello è sempre una boccata d'ossigeno. Perché, una volta saldato il debito, non fai un giro al mercato cittadino per concederti qualche souvenir?"
    ),
    218: (
        "In futuro riceverai fatture e richieste di pagamento per svariate ragioni, non solo per le tasse fondiarie. La modalità di riscossione è identica per tutte, perciò non temere. L'unica raccomandazione è non sforare le scadenze: oltre a rovinare la tua reputazione, i funzionari imperiali non esitano a ricorrere alle maniere forti!"
    ),
    219: (
        "Ah già, stavo per dimenticare il dettaglio più importante: per raggiungere la capitale di Mysilia, ti basta seguire la strada maestra verso sud-est. Il tragitto è un po' lungo, ma è impossibile perdersi."
    ),
    223: (
        "Allora, eri agitato per il tuo primo versamento di tasse?\n\n"
        "Non è stato affatto complicato, vero? Come ti accennavo, l'unico vero scoglio è avere il portafoglio abbastanza gonfio!\n\n"
        "E ora che hai adempiuto al tuo dovere civico, ho un regalo straordinario per te. La 'cassetta postale' è un comodo arredo che raccoglie in automatico tutte le missive e le fatture in arrivo al feudo. Così facendo, eviterai di smarrire comunicazioni vitali in mezzo alla confusione!"
    ),
    227: (
        "Prima di trattare della Dieta, lascia che ti impartisca una tediosa ma doverosa lezione di storia.\n\n"
        "Rispetto alle lande orientali di Asseria, dilaniate da guerre perenni, Tyris Settentrionale è sempre stato un continente relativamente pacifico. Separato dal vasto Mare di Asseria, persino l'Impero con le sue temibili flotte di aeronavi Cyran vi si spingeva raramente."
    ),
    228: (
        "Tuttavia, con l'inasprirsi dell'odio tra il Nuovo Regno di Yerl e l'Impero, le fiamme della guerra raggiunsero ogni angolo del mondo conosciuto, costringendo i principati di Tyris a fare fronte comune. Fu così che nacque l'Unione di Tyris, sotto lo stendardo della concordia e della prosperità collettiva.\n\n"
        "Durante le sedute della Dieta vengono dibattute tutte le proposte presentate all'Unione: dalle grandi dispute internazionali agli aiuti economici per i piccoli villaggi rurali. I potenti senatori sono coloro che detengono il diritto di voto per approvare o respingere ciascuna mozione."
    ),
    229: (
        "Nel corso delle tue peripezie ti capiterà certamente di imbatterti in qualche membro della Dieta. Stringere relazioni con loro e ottenerne l'appoggio politico sarà cruciale per il futuro del tuo feudo.\n\n"
        "Dunque, se mai dovessi incontrare un senatore, rivolgigli un saluto cordiale e cerca di ingraziartelo."
    ),
    240: (
        "Tyris è un continente sconfinato. Una volta presa dimestichezza con la vita campestre, faresti bene a esplorare i territori limitrofi.\n\n"
        "Dirigendoti a sud-est troverai una caverna nota come Nymelle. Nelle gallerie superficiali i mostri non dovrebbero rappresentare una minaccia letale. E laggiù... c'è qualcosa che mi insospettisce parecchio. Saresti disposto a esplorarla per conto mio?"
    ),
    242: (
        "Prima che tu ti metta in marcia, desidero affidarti queste pergamene magiche.\n\n"
        "La 'Pergamena dell'Evacuazione' consente di fuggire all'istante da qualsiasi Nefia e tornare in superficie. La 'Pergamena del Ritorno' ti teletrasporta al piano più profondo che hai esplorato in un Nefia, oppure direttamente al tuo feudo.\n\n"
        "Entrambe sono strumenti salvavita imprescindibili per ogni avventuriero. Fannegli il miglior uso possibile."
    ),
    249: (
        "Sei tornato! Ero in pensiero quando Fiama è svanita all'improvviso... anche se è la sua solita abitudine.\n\n"
        "Ebbene, sentiamo cosa hai scoperto laggiù."
    ),
    254: (
        "Una falena... titanica...?! Ma che ti sei fumato, per caso i fumi del crim?!\n\n"
        "No, scusami... stento a crederci, ma se entrambi l'avete vista con i vostri occhi, non può trattarsi di una semplice allucinazione."
    ),
    255: (
        "Un cristallo d'etere sepolto nelle viscere del mondo... Dunque era questa la vera identità del potere arcano che stavamo cercando. E se la Dama della Foresta dice il vero, un secondo cristallo giace dimenticato tra le rovine sud-orientali di Lysanas."
    ),
    256: (
        "Non dovremmo mai fidarci ciecamente delle parole di un'entità ancestrale come quella falena, ma dobbiamo ammettere di non avere altra scelta.\n\n"
        "Lysanas, dunque. Vale senz'altro la pena investigare a fondo."
    ),
    257: (
        "...E c'è un altro particolare che non mi dà pace.\n\n"
        "Hai detto di aver visto un individuo con un orrendo tatuaggio sul collo? Se la mia intuizione è esatta... no, ne sono certo, non esiste un altro damerino simile in tutta Tyris.\n\n"
        "Ephrond Torres. Figlio del duca Jonan Torres di Mysilia. Il mio viziatissimo fratellastro."
    ),
    258: (
        "Non guardarmi con quegli occhi sgranati! Ho rescisso ogni legame con il Casato dei Torres molto tempo fa. Oggi non sono altro che un modesto servitore di messer Cetrus.\n\n"
        "Ad ogni modo... perché mai Ephrond, l'erede di Mysilia, tratterebbe in segreto con l'Impero nemico?!\n\n"
        "Ho un pessimo presentimento, ma questa è una faccenda che spetta a me risolvere. Indagherò su questo tradimento assieme alle notizie su Lysanas."
    ),
    259: (
        "...Quando ti abbiamo raccolto privo di sensi credevo che soccorrerti fosse una perdita di tempo colossale; e invece guarda un po'! Grazie alle tue scoperte, mi ritrovo con una montagna di informazioni preziose su cui lavorare.\n\n"
        "Ora faremo ritorno a Forte Willow per fare rapporto a messer Cetrus. È stato un vero onore condividere con te la nascita del tuo insediamento."
    ),
    261: (
        "Se... se ti andasse di prendere parte alla spedizione verso Lysanas, saresti disposto a venirci a trovare a Forte Willow?\n\n"
        "Nessuna costrizione, sia chiaro: sei liberissimo di dedicarti unicamente a espandere il tuo villaggio, o di viaggiare per il mondo per scoprire nuove terre. Sta solo a te decidere cosa vedere e quale impronta lasciare in questo universo.\n\n"
        "Addio per ora, e possa il soffio del vento vegliare sui tuoi passi."
    ),
    272: "L'arte della forgiatura e della falegnameria è una competenza fondamentale per la vita e l'avventura. Non sono un mastro artigiano, ma condividerò con te quel poco che so.",
    273: (
        "Dunque, cominciamo con il costruire un banco da lavoro. È la struttura portante di qualsiasi laboratorio: con esso potrai fabbricare pavimentazioni improvvisate e mura per la tua prima casetta.\n\n"
        "Puoi creare un banco di lavoro ovunque ti trovi sfruttando l'abilità 'Fabbricazione Rapida' che già conosci. Abbatti qualche albero circostante per procurarti dei tronchi, e poi usa l'abilità per assemblarlo."
    ),
    274: "Assicurati di piazzare il banco completato su una porzione di terreno pianeggiante.",
    280: (
        "Niente male davvero!\n\n"
        "Hai già provato a utilizzarlo? All'inizio i manufatti realizzabili saranno pochi, ma non appena entrerai in possesso di nuovi schemi potrai sbizzarrirti con ogni sorta di arredo."
    ),
    281: (
        "Bene, siamo pronti a erigere le pareti domestiche; ma prima di farlo, faremmo meglio a fabbricare una sorgente di luce per affrontare l'oscurità notturna.\n\n"
        "Portare con sé una fonte luminosa permette di orientarsi anche nelle notti più buie. Puoi costruire una 'Torcia' direttamente al banco di lavoro: raccogli i materiali nei dintorni e mettiti alla prova."
    ),
    282: (
        "Lo spago necessario alla torcia può essere intrecciato al banco usando le liane selvatiche. E una volta forgiata la torcia, ricordati di equipaggiarla nell'apposito slot per le fonti di luce!"
    ),
    287: "Ottimo! Hai compiuto il tuo primo passo come artigiano. C'è ancora molto da apprendere, ma adesso voglio assegnarti una vera missione.",
    288: (
        "Il tuo traguardo è: 'Costruire da cima a fondo una casa con le tue sole forze'.\n\n"
        "Potrà sembrarti un'opera titanica, ma in fin dei conti basta delimitare uno spazio con quattro mura e munirlo di una porta per poterlo chiamare casa! Nel frattempo preparerò un dono per la nuova dimora. Avanti, mettiti all'opera!"
    ),
    292: "Vedo che la casa è ultimata! Congratulazioni vivissime! Adesso non dovrai più temere di dormire all'addiaccio in balia di acquazzoni e bufere.",
    293: (
        "Ora spendiamo due parole sul funzionamento delle abitazioni.\n\n"
        "L'aspetto esteriore e la destinazione d'uso della casa possono essere personalizzati interagendo con il registro edilizio. Inoltre, quando suddividi lo spazio interno con tramezzi e porte, crei delle stanze distinte: ciascuna di esse può essere configurata tramite l'apposita targa della camera.\n\n"
        "Non è un granché, ma voglio regalarti una targa della casa e una della stanza. Personalizza il tuo nuovo nido a tuo piacimento!"
    ),
    299: (
        "In tempi turbolenti come questi, imparare a brandire un'arma non fa mai male.\n\n"
        "Molte delle creature selvatiche che popolano le terre aperte ti attaccheranno a vista. Puoi valutare la pericolosità di un avversario passando il cursore del mouse sul bersaglio. È sempre saggio evitare lo scontro con nemici soverchianti finché non sarai ben corazzato."
    ),
    300: (
        "Cominciamo con una rapida sessione di addestramento pratico. Ho legato un teppistello di passaggio dietro la bacheca degli annunci. Una creatura immobilizzata non può muoversi: se ti trovi alle strette, allontanati e attendi che la tua energia si rigeneri.\n\n"
        "Non fare complimenti: va' e gonfialo di botte a tuo piacimento!"
    ),
    306: (
        "Ottimo lavoro!\n\n"
        "Avversari stupidi come quei teppisti non incutono timore perché si limitano ad attacchi prevedibili. Tuttavia, esistono creature che colpiscono a distanza o possiedono abilità insidiose qualora tu le affronti corpo a corpo."
    ),
    307: (
        "Il prossimo bersaglio della tua leva è un cinghiale selvatico. Ne ho fatto legare uno sempre dietro la bacheca.\n\n"
        "Come il teppista, anche il cinghiale è una bestia semplice, ma la possanza degli animali selvaggi non va mai sottovalutata: affrontarlo a mani nude rischierebbe solo di farti incornare per bene!\n\n"
        "Contro simili avversari, gli attacchi a distanza sono la scelta più saggia. Ti affido alcuni arnesi da getto: usa l'astuzia per abbatterlo. E ricorda sempre: molti oggetti possono essere 'lanciati'!"
    ),
    312: (
        "Magistrale! Ora non avrai più problemi ad avere la meglio su avversari che fanno leva solo sulla forza bruta.\n\n"
        "Belve come i cinghiali sono facili da gestire, ma possono circondarti, tagliarti la ritirata o metterti all'angolo. La regola d'oro è non peccare mai di superbia e disporre sempre di una via di fuga per sganciarsi dalla mischia."
    ),
    313: (
        "Come prova finale del tuo addestramento, ti pongo un traguardo ambizioso.\n\n"
        "L'obiettivo è: 'Sconfiggi cento nemici, qualunque essi siano'.\n\n"
        "Tyris Settentrionale pullula di mostri pericolosi e briganti da strapazzo: non farai alcuna fatica a trovarne un centinaio o due! Il conteggio delle tue prede è annotato nel diario d'avventura, consultalo per tenere il conto."
    ),
    318: (
        "Congratulazioni vivissime! Ora sei perfettamente in grado di difendere la tua pelle.\n\n"
        "Ci sarebbero ancora innumerevoli nozioni da illustrarti, ma per ora concentrati sul fare esperienza sul campo. Eccoti alcune monete di platino come ricompensa.\n\n"
        "Puoi consegnarle ai maestri d'arme nelle città per farti addestrare o apprendere nuove e potenti abilità."
    ),
    324: (
        "Ora che hai iniziato a gettare le basi del tuo feudo, devi assolutamente comprendere il funzionamento dei 'contenitori condivisi'.\n\n"
        "Un contenitore condiviso è un'infrastruttura fondamentale per la vita e il lavoro dei tuoi abitanti. Ascoltami con la massima attenzione: te lo spiegherò una sola volta!"
    ),
    325: (
        "Casse, bauli e barili possiedono un sistema di 'autorizzazioni'. In condizioni ordinarie solo tu puoi depositare e prelevare oggetti, ma puoi convertire qualunque cassa in un contenitore condiviso cliccando sull'icona del 'Lucchetto' a destra.\n\n"
        "I contenitori condivisi sono accessibili a tutti i residenti e compagni del feudo. Coloro che hanno fame cercheranno provviste al loro interno; se trovano armi o armature migliori, le indosseranno; e se necessitano di materie prime per lavorare, le consumeranno in autonomia."
    ),
    326: (
        "Inoltre, tieni sempre d'occhio lo spazio residuo nei bauli condivisi, poiché i residenti vi depositeranno il frutto del loro lavoro e i tesori rinvenuti in giro.\n\n"
        "Ti consegno questa cassa come premio anticipato: posizionala al suolo e prova a convertirla in un 'contenitore condiviso'."
    ),
    335: (
        "Vedo che hai configurato con successo la cassa condivisa!\n\n"
        "Modificando le impostazioni dei contenitori, puoi persino creare bauli con priorità di stoccaggio o adibiti esclusivamente a determinate categorie di merci. Ti tornerà utilissimo più avanti per organizzare i magazzini del feudo."
    ),
    342: (
        "Capiti al momento giusto!\n\n"
        "Non te l'avevo ancora detto, ma la legge di Mysilia prevede che ogni nuova colonia sia affiancata da un ispettore fondiario. 'Ispettore' suonerà burocratico e severo, ma non temere: sono veri e propri assistenti che agevolano lo sviluppo delle terre."
    ),
    343: (
        "Se invece preferisci vivere da pioniere libero e solitario, senza alcun tipo di intromissione tra i piedi, posso sistemare io la faccenda con la burocrazia di Mysilia.\n\n"
        "A te la scelta: cosa preferisci fare?"
    ),
    344: "Desidero l'aiuto di un ispettore fondiario.",
    345: "Preferisco vivere in piena libertà.",
    349: (
        "Immaginavo che avresti risposto così! In realtà ho già mandato a chiamare un eccellente ispettore di mia conoscenza: ha un carattere un po' spigoloso, ma sul lavoro è una garanzia assoluta.\n\n"
        "Consentimi di presentarti un mio fidato compagno, nonché il miglior ispettore fondiario di Mysilia: Loytel!"
    ),
    350: "...",
    351: "...Ma che diavolo significa tutto questo?!",
    352: (
        "'C'è una terra oltremodo promettente dove l'oro scorrerà a fiumi!', mi avevi detto per convincermi a venire fin qui... Ma ho forse inteso male io?!\n\n"
        "Questa non è altro che una desolata, fangosa, maledetta pietraia dimenticata da dio e dagli uomini!"
    ),
    353: (
        "Pretendo una spiegazione convincente, Ashland! Sono un uomo indaffarato, io! Che razza di scherzo è questo?! Per quale motivo mi hai trascinato in questa landa brulla piena solo di sterpaglie e sassi?!"
    ),
    354: (
        "Ah, Loytel mio! A quanto pare la polvere del viaggio ti ha annebbiato la vista. Una miniera d'oro non si trova certo già scavata e tirata a lucido sul ciglio del sentiero!\n\n"
        "Certo, questo posto è rustico come dici tu; ma hai dato un'occhiata all'avventuriero che sta al mio fianco? È #he la vera ragione per cui ti ho fatto venire fin qui!"
    ),
    355: "...",
    356: "...",
    357: "...",
    358: "Vorresti forse darmi a bere che questa specie di sprovveduto spaesato sarebbe la 'miniera d'oro'?!",
    359: "...Esattamente, proprio così!",
    360: (
        "Uff... Se proprio insisti a questo modo, suppongo di poter accettare l'incarico. Non ne sono per nulla entusiasta, ma riconosco di avere un debito d'onore nei confronti tuoi e di Fiama.\n\n"
        "Ma santo cielo, qui intorno c'è solo una distesa sterminata di erbacce! Di norma, prima di fondare una colonia ci si attrezza con un minimo di decenza, non trovi?!"
    ),
    361: (
        "Ehm... Ehi, tu, avventuriero! Ci sei? Hai afferrato il concetto?\n\n"
        "Permettimi di presentarmi: sono Loytel, ispettore fondiario di prima classe del principato di Mysilia, nonché consigliere di corte e tesoriere finanziario. Apprezzo i vini d'annata di Olvina e i piani di bonifica efficienti; detesto con tutto il cuore i coloni incompetenti.\n\n"
        "Con la mia sapienza ed esperienza questa terra è destinata a trionfare, anche se quasi tutto dipenderà dal tuo sudore. Dunque vedi di dare il massimo!"
    ),
    362: (
        "Loytel ha modi bruschi, ma è un uomo fidato e scrupoloso: sarà di immenso ausilio alla crescita del tuo feudo.\n\n"
        "Per qualsiasi dubbio circa la gestione dell'insediamento o la vita a Tyris, è a lui che devi fare riferimento."
    ),
    371: "D'accordo. Se questa è la tua volontà, fai pure come meglio credi. Se dovessi cambiare idea, vieni pure a parlarmi in qualsiasi momento."
}

def run():
    wb = openpyxl.load_workbook(ASHLAND_FILE)
    ws = wb.active
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
    text_c = headers.get('text', 11)
    
    count = 0
    for row, it_text in ASHLAND_DATA.items():
        ws.cell(row=row, column=text_c, value=it_text)
        count += 1
        
    wb.save(ASHLAND_FILE)
    print(f"Successfully translated {count} dialogue rows in ashland.xlsx!")

if __name__ == "__main__":
    run()
