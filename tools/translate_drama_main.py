# coding: utf-8
"""
Elin Italian Localization - Drama _main.xlsx Localizer
Translates the entire main storyline prologue and cutscenes:
- Opening cinematic (11th era of Ylva, Rem-Ido, Ancient Desert Empire)
- Awakening at the bonfire with Ash and Fiama
- The Court of Mysilia council (Barrich, Melvin, Caldorn, Ephrond, Eluminaire)
- Royal Gardens: Duke Jonan and Ephrond (Dreaming Child secret)
- Royal Gardens: Barrich, Melvin and the ladies (lyra origin, Cetrus, Zanan)
- Depths of Nymelle: General Isygarad, imperial golems and Ephrond's conspiracy
- Vindale Lore: Rise and fall of Rem-Ido, Ether, Unyielding Tree
- Encounter with Onev, the Lady of the Forest
- Epilogue on the Road: Fiama's nightmares, Ash's cynicism, Willow's pies
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MAIN_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama', '_main.xlsx')

MAIN_TRANSLATIONS = {
    35: (
        "In un'epoca remota, ormai dimenticata...\n"
        "Le vestigia di innumerevoli civiltà giacciono sepolte nelle viscere della terra,\n"
        "e l'Undicesima Era di Ylva ebbe inizio\n"
        "mentre le profonde ferite del Rehm-Ido tardavano ancora a rimarginarsi.\n"
        "Questa è la storia di Sieraterre."
    ),
    37: (
        "I fuochi di guerra accesi dall'antico impero del deserto\n"
        "si propagarono ben presto nel resto del mondo, gettando Ylva\n"
        "in un lungo e tenebroso periodo di scompiglio.\n\n"
        "Dopo aver perduto la leggendaria aeronave Cyran sul continente occidentale,\n"
        "le truppe dell'impero iniziarono una ritirata graduale da ogni regione,\n"
        "ponendo fine a dieci lunghi anni di ostilità.\n\n"
        "I popoli umani celebrarono la loro prima grande vittoria e la pace riconquistata,\n"
        "e la gente tornò a condurre una vita serena e laboriosa.\n\n"
        "Tuttavia, nessuno riuscì mai a dimenticare il tradimento degli Elea,\n"
        "rimasti impassibili a osservare in silenzio durante il conflitto."
    ),
    39: "E così trascorsero quindici anni...",
    41: (
        "Il tempo continuò a scorrere inesorabile.\n\n"
        "Ti eri unito a una carovana di mercanti diretta verso Mysilia.\n"
        "Voci inquietanti e sinistri presagi echeggiavano ovunque facessi sosta,\n"
        "facendoti percepire un'ombra minacciosa calare nuovamente sulle terre d'occidente.\n\n"
        "Una notte inoltrata, mentre il lungo viaggio volgeva ormai al termine,\n"
        "una strana luce danzante tra le fronde ti attirò nelle profondità della boscaglia.\n"
        "E mentre il denso miasma azzurro esalato dagli alberi dell'Antica Foresta ti avvolgeva,\n"
        "i tuoi sensi si spensero a poco a poco..."
    ),
    54: (
        "Ti sei svegliato, finalmente.\n\n"
        "No, resta disteso. Sei rimasto privo di sensi per un bel pezzo."
    ),
    56: (
        "È una fortuna che ti abbiamo trovato prima che fosse troppo tardi. Non è mai saggio per un umano addentrarsi nella foresta degli Elea, specialmente nel cuore della notte come questa, con il vento che infuria e le fronde in continuo tumulto."
    ),
    57: (
        "...Ora ti abbiamo portato fin qui, ma a quanto pare abbiamo perso un'intera notte del nostro urgente viaggio. Non che me ne lamenti... be', non troppo. Almeno la mia compagna sembra gradire questa sosta imprevista.\n\n"
        "Sei un viaggiatore? Cosa ti porta a Mysilia?\n\n"
        "...Ma forse sto ficcando il naso un po' troppo, eh?"
    ),
    58: (
        "Dormi sodo per adesso. La vera quiete giunge sempre nel momento in cui ne abbiamo più bisogno."
    ),
    65: "Così... è da questo istante che ha inizio la nostra storia.",
    66: (
        "Ash non perdeva occasione per fare del sarcasmo, come sempre,\n"
        "ma in fondo sembrava persino più lieto di me\n"
        "per quella piccola tregua che tu, inconsapevolmente, ci avevi donato."
    ),
    68: (
        "Il destino che attendeva la terra di Mysilia,\n"
        "la verità nascosta del mondo e le scelte che avremmo compiuto,\n"
        "e le profonde cicatrici che tutto ciò avrebbe lasciato su Ylva..."
    ),
    69: (
        "Ancora ignari di quanto sarebbe accaduto,\n"
        "fissavamo in silenzio le fiamme del focolare,\n"
        "attendendo con pazienza che la luce dell'alba rischiarasse il cielo."
    ),
    80: (
        "Ah, finalmente il nostro misterioso ospite ha deciso di destarsi.\n\n"
        "C'è della zuppa d'avena vicino al falò, anche se ormai si è raffreddata del tutto.\n\n"
        "Vieni da me quando ti sarai sfamato. Dobbiamo fare due chiacchiere."
    ),
    95: "- La corte di Mysilia -",
    96: "Ehi, quanto durerà ancora questo consiglio? Di cosa stiamo discutendo, esattamente?",
    97: "Fammi indovinare, Barrich. Eri occupato a comporre un altro dei tuoi nuovi poemi?",
    98: (
        "...Dalla guerra di quindici anni fa, Mysilia continua a brancolare nella tormenta. Una misteriosa epidemia ha flagellato le nostre terre già devastate dal conflitto, prosciugando riserve alimentari e forzieri. I tumulti interni sono all'ordine del giorno, per non parlare dei dissidi tra i nobili... e il promettente erede del duca Jonan è stato persino esiliato all'improvviso.\n\n"
        "Inoltre, il risentimento verso gli Elea germogliato tra gli umani dopo la guerra ha minato pesantemente i rapporti tra Mysilia e le altre nazioni, poiché noi continuiamo a sostenere la riconciliazione tra i due popoli."
    ),
    99: (
        "Oh, e ho già menzionato che l'Impero sta allestendo nuove aeronavi da guerra per consumare la propria vendetta contro Mysilia?\n\n"
        "Cosa facciamo adesso? Nessuna conclusione. Ognuno dei presenti ha già le mani legate fino al collo con i problemi dei propri feudi."
    ),
    100: (
        "Sei sempre il solito musone diligente, Melvin.\n\n"
        "In soldoni, ci troviamo su una barca che fa acqua da tutte le parti peggio di una forma di formaggio bucherellata, e noi passiamo le giornate a discutere su quale falla tappare per prima."
    ),
    101: (
        "Che diavolo continuate a confabulare voi due ragazzini?!\n\n"
        "E tu, Barrich, che accidenti ti è saltato in mente di portare quella dannata lira in mezzo a una seduta di corte?!"
    ),
    102: "Posso sempre dedicarvi una ballata, se preferite. Magari vi ammorbidirà quel cervello un tantino arrugginito.",
    103: "Barrich, tu piccolo insolente...!",
    104: (
        "Non irritatevi così, Caldorn. In fondo Barrich non ha tutti i torti: da un consesso simile non verrà mai fuori nulla di utile.\n\n"
        "Ora, se volete scusarmi, ho questioni urgenti da sbrigare. Svegliati, Eluminaire. Ce ne andiamo."
    ),
    105: "...Ah, sì, signor Ephrond! Chiedo umilmente perdono.",
    107: (
        "...Ma chi è quella ragazzina? Stava forse dormendo in piedi?!\n\n"
        "Che mancanza di rispetto imperdonabile, appisolarsi in questo luogo sacro, per quanto sia la protetta del nostro giovane signore.\n\n"
        "E quel damerino... mostrarsi così disinteressato alle sorti di Mysilia!\n\n"
        "Che cosa diavolo sta succedendo a questo regno?!"
    ),
    118: "- I giardini reali di Mysilia -",
    119: "Cosa aspetti ancora, Eluminaire? Non ho tutta la giornata a disposizione.",
    120: "Un momento, Ephrond. Devo parlarti.",
    121: "Ma guarda un po', padre. Siete sceso ad ammirare le aiuole in fiore? Non dovreste trovarvi a quella noiosissima adunanza?",
    122: (
        "Risparmiami le tue arie, Ephrond. Dunque è lei la fanciulla...\n\n"
        "Puoi dirmi come ti chiami, bambina? Ti trovi bene qui a corte?"
    ),
    123: "Il mio nome è Eluminaire, Vostra Grazia. La vita di corte o quella dell'orfanotrofio non fanno molta differenza per me. Io desidero soltanto seguire il mio signore Ephrond.",
    124: "Deve essere... gravoso. Forse ogni tanto desidereresti trascorrere un momento di quiete da sola.",
    125: (
        "Ahahah! Che battuta spassosa, padre!\n\n"
        "Ricorderete sicuramente l'incidente in cui un intero villaggio svanì nel nulla per via di un folle che cercò di spaventare un Bambino Sognante. Non posso distogliere lo sguardo da Eluminaire neppure per un secondo: è una creatura così incredibilmente timorosa.\n\n"
        "Ah, se solo possedesse anche solo la metà del fascino della compianta nobildonna Friaune, tutto questo sarebbe infinitamente più piacevole."
    ),
    126: (
        "Il potere celato nei Bambini Sognanti... Dunque la ricerca è andata a buon fine?\n\n"
        "...Ne dubitavo fortemente. E pur sapendo che un simile sacrilegio non mi sarebbe mai perdonato, ho gettato tutto il fardello sulle tue spalle.\n\n"
        "Questo potere salverà Mysilia, non è vero? Un potere mai concesso prima d'ora alle mani dei mortali... uno strumento forgiato a vantaggio degli uomini."
    ),
    127: (
        "Uno strumento per gli uomini? Vi sbagliate di grosso, padre.\n\n"
        "Questa ricerca non è condotta per l'umanità, né tantomeno per la gloria di Mysilia. È destinata unicamente a Eluminaire e alla sua stirpe, affinché possano sopravvivere alle catastrofi imminenti."
    ),
    128: (
        "Voi ci avete imposto questa 'maledizione' con cieco egoismo, e il mio codardo fratello è fuggito a gambe levate. Ma io... io trasformerò questa maledizione in una benedizione eterna.\n\n"
        "E ora vogliate scusarmi, ho un appuntamento a cui non posso mancare. Abbiate cura di voi, padre."
    ),
    129: "...",
    139: "- I giardini reali di Mysilia -",
    140: "Oh cielo, mio splendido Lord Melvin!",
    141: "Aaaah! È così affascinante!",
    142: (
        "Signore, vi prego, mantenete la calma! Radunandovi in questo modo state bloccando il passaggio nel viale.\n\n"
        "Oh, gentildonne, non spingete, è pericoloso! Fate largo, vi scongiuro!\n\n"
        "...Oh, Barrich! Arrivi proprio a fagiolo!"
    ),
    143: "Melvin, intorno a te c'è sempre un gran fermento teatrale! Oggi ho composto una nuova melodia apposta per te. Mie signore, accomodatevi e prestatemi orecchio!",
    144: "Aaaaah!",
    150: "...Così tante dame sparite in un battito d'ali! Ehi Melvin, il mio canto fa davvero così schifo?",
    151: (
        "Be'... no, in realtà mi sei sempre... di grande aiuto in queste situazioni.\n\n"
        "Non credo che il tuo tocco con lo strumento sia sgradevole. Mia sorella mi raccontava che la tua bimba appena nata smette di piangere e si addormenta appena sente le note della tua lira. Dice persino che, finché non apri bocca per cantare, la tua musica è leggiadra come quella degli Elea."
    ),
    152: (
        "...Ehi, e questo sarebbe un complimento?!\n\n"
        "È stato messer Cetrus in persona a insegnarmi a suonare la lira, comunque. A quanto pare la mia adorata mogliettina ha un gusto sopraffino per la vera arte musicale."
    ),
    153: "Messer Cetrus ti ha fatto da maestro? E com'è accaduta una cosa simile?",
    154: (
        "Non è chissà quale grande epopea.\n\n"
        "Dieci anni fa, dopo aver fatto un disastro a Zanan ed essere fuggito esule qui a Mysilia, passavo le giornate a spezzarmi la schiena con la spada. Non avevo nient'altro da fare: non conoscevo questo paese e la mia lama era l'unica cosa su cui potessi contare."
    ),
    155: (
        "Un giorno, ebbi da ridire con un tipo dall'aria raffinata che suonava la lira con grazia impeccabile in una bettola malfamata. Ovviamente non avevo la minima idea che si trattasse di messer Cetrus! Gli risi in faccia dicendo: 'La musica è un passatempo per donne e mocciosi'. Lui non mi fulminò con lo sguardo né ribatté parola... si limitò a pizzicare le corde, intonando le antiche ballate di Zanan.\n\n"
        "Io... be', lascio il resto alla tua immaginazione."
    ),
    156: (
        "...Per noi di Mysilia, messer Cetrus è un padre venerabile e un mentore verso cui non oseremmo mai alzare lo sguardo con alterigia. Dopotutto, veglia su queste terre da più di un secolo. Persino un testardo come te non è altro che un bimbo capriccioso al suo cospetto.\n\n"
        "Quando smettesti di farti vedere agli allenamenti e si sparse la voce che passavi le ore a strimpellare la lira da solo su una collina, pensavamo tutti che fossi caduto vittima delle febbri d'amore! Ma ultimamente devo ammettere che andare in giro con quello strumento a tracolla comincia a donarti."
    ),
    157: (
        "Ad ogni modo, da quando hai la testa persa tra gli spartiti non trovo più nessuno con cui incrociare le spade degnamente. Cominciavo a temere che il tuo braccio si stesse arrugginendo."
    ),
    158: (
        "È stata una scoperta sconvolgente persino per me, ma a quanto pare comporre melodie si addice al mio spirito molto più che squarciare gole.\n\n"
        "Ma hai ragione a preoccuparti. Con i foschi nembi che si addensano sul cielo di Mysilia, forse è giunto il momento di riporre la lira nel vecchio armadio e lucidare la lama."
    ),
    159: "...",
    160: (
        "Amo Mysilia.\n\n"
        "Ha saputo accogliere persino un bastardo diffidente e burbero come me. Certo, all'inizio mi ridevano dietro, ma a nessuno importa sul serio se un omone rude va in giro portando una lira. E adesso mi ritrovo con un fratello per la vita, una sposa incantevole e quel vecchio rompiscatole calvo a inveirmi contro!\n\n"
        "Al diavolo Zanan! Sono pronto a donare il mio cuore per l'unica vera casa che abbia mai trovato."
    ),
    161: (
        "...È una nobile risoluzione, anche se un po' gonfiata dai fumi dell'alcol che hai tracannato!\n\n"
        "Su, credo sia meglio che ti rimandi a casa. Mia sorella mi farebbe la pelle se tornassi da lei ubriaco fradicio a cantare a squarciagola davanti alla culla!"
    ),
    174: "Le radici pietrificate delle piante primordiali si estendono fin quaggiù... Non c'è dubbio, in queste profondità devono trovarsi cristalli d'etere.",
    175: "La vista soddisfa il vostro nobile palato, mio signore Isygarad?",
    176: "È valsa la pena scendere in questi meandri. Certo, è una riserva piuttosto modesta se paragonata agli immensi giacimenti che brillano sotto le sabbie del nostro deserto.",
    177: "...Stando a quanto ho appreso, per la fabbricazione delle aeronavi Cyran è richiesta una quantità esorbitante di cristalli. Forse avete intrapreso questo lungo viaggio fin qui perché le immense risorse delle vostre terre d'origine non bastano più a saziare la vostra fame?",
    178: (
        "Mettere le mani su questi cristalli è senz'altro uno dei miei scopi, sì. Ma non è l'unica ragione che ci ha condotti in una terra remota e funestata dalla sventura come questa.\n\n"
        "Quella tempesta di luce impetuosa e indimenticabile... Se aprite la mappa, noterete che questo 'Cimitero dei Venti' coincide esattamente con il punto in cui la luce apparve per la prima volta. Una coincidenza assai ben orchestrata, non trovate?"
    ),
    179: "...Quella tempesta. State forse insinuando che la burrasca che abbatté l'invincibile aeronave Cyran sia legata al cristallo sigillato a Nymelle...?",
    180: (
        "Ma guarda un po'... Questa sì che è una teoria affascinante. Sarei ben lieto di approfondire le vostre deduzioni a riguardo.\n\n"
        "Tuttavia, sembra proprio che abbiamo una visita sgradita."
    ),
    183: (
        "Mmh, a giudicare dalle vesti sembrerebbe feccia d'avventuriero da quattro soldi.\n\n"
        "Non preoccupatevi. I golem imperiali sapranno come sbarazzarsene in fretta."
    ),
    184: "In tal caso, avendo assolto al mio compito di farvi da guida, toglierò il disturbo. Lord Isygarad, confido che terrete fede alla promessa pattuita.",
    185: "Eluminaire... oh, Eluminaire, ti sei addormentata di nuovo?! Muovi quelle gambe, stupida creatura!",
    186: "...S-sì, perdonatemi, padron Ephrond!",
    187: "...",
    191: (
        "Ora, ammetto di essere piuttosto curioso di scoprire cosa cercasse un miserabile avventuriero nelle viscere del 'Cimitero dei Venti', ma purtroppo ho una certa fretta.\n\n"
        "Non fate complimenti: danzate con i miei golem!"
    ),
    201: (
        "Fin da quando ero bambina, la 'voce' della foresta ha sempre trovato la via per raggiungermi.\n\n"
        "Ero solita rannicchiarmi contro il tronco di un imponente albero dell'Antica Foresta, ascoltando rapita il sussurro dei rami. Il canto dei boschi mi ricordava la mia defunta madre.\n\n"
        "Ed è stata proprio quella voce a condurmi fin qui."
    ),
    202: (
        "...Non immaginavo minimamente che nelle viscere di Nymelle si celasse un luogo simile.\n\n"
        "Eppure lo sento... La linfa vitale di questo 'bosco' è ormai prosciugata, destinata soltanto a un lento appassire.\n\n"
        "Qualunque cosa fosse, il potere in cui sperava Ash non si trova più qui."
    ),
    236: (
        "In un'epoca remota, ormai dimenticata.\n\n"
        "Venne alla luce grazie all'antica civiltà di Rehm-Ido.\n\n"
        "Fu battezzata 'la luce che mai sbiadisce',\n"
        "lo splendore che accoglie i ricordi dei defunti, la lacrima che colma il pianeta, oppure mana,\n"
        "oppure etere.\n\n"
        "Era una sorgente di anime che ricordava, generava e fondeva ogni cosa\n"
        "con l'essenza ideale dell'esistenza.\n\n"
        "Si diffuse con fulminea rapidità tra le genti\n"
        "e trasformò radicalmente l'intera civiltà di Rehm-Ido."
    ),
    238: (
        "Irretita e sedotta dall'etere, Rehm-Ido imboccò lentamente\n"
        "il sentiero della rovina trascinando con sé l'intero pianeta.\n\n"
        "Le guerre sanguinose per il dominio dell'etere non ebbero tregua.\n"
        "La terra fu squarciata nel profondo e tetre nubi soffocarono la volta celeste.\n\n"
        "Quando l'etere fu infine consumato, il pianeta si trasformò\n"
        "in una landa inospitale, priva di vita.\n\n"
        "E così calò l'inverno eterno."
    ),
    240: (
        "Soltanto 'l'Albero Indomito' riuscì a sopravvivere a quel rigido gelo.\n\n"
        "Il colossale albero divenne foresta, e la foresta cullò e rigenerò la vita.\n"
        "Quella foresta prese il nome di Vindale.\n\n"
        "I bagliori cerulei sprigionati dagli alberi di Vindale\n"
        "volarono alti nel cielo, danzando nei venti.\n\n"
        "Fu l'inizio della sacra purificazione\n"
        "e della rinascita del pianeta."
    ),
    255: "...L'era di Sierra Terre ebbe dunque inizio con la promessa della rinascita di questo mondo. Eppure, sono già trascorsi secoli da quando i venti di Vindale sono cessati.",
    256: "Una falena... gigantesca?\n...Sto forse sognando?",
    257: (
        "O figlia della foresta, fragile creatura mortale che tuttavia ode la mia voce. Il mio nome è Onev, compagna del grande Albero Indomito, prima tra i viventi e madre di ogni essere animato su Ylva.\n\n"
        "Il cristallo che contempli dinanzi a te è la forma pietrificata di un antico albero permeato d'etere. È un nucleo che racchiude un potere immenso.\n\n"
        "...Ma l'arte per liberarne la potenza è andata smarrita nell'inesorabile scorrere dei millenni."
    ),
    258: "Eppure, vent'anni or sono, un Elea dischiuse il potere di questo cristallo di Nymelle e ridestò il vento.",
    259: "...La Tempesta di Nymelle. Il cristallo deve aver risposto alla preghiera di messer Cetrus!",
    260: "Quel vento è l'araldo del Vento d'Etere che Ylva attendeva da tempi immemori. La 'Stagione della Quiete' è giunta al termine, e la purificazione del pianeta sta per iniziare nuovamente.",
    261: (
        "La purificazione del pianeta... Aspettate, cosa state cercando di dirci?!\n\n"
        "Siamo giunti fin qui alla ricerca di una speranza per respingere l'avanzata dell'Impero. Ma il cristallo di questa foresta sotterranea è spento. Non abbiamo più alcun modo per fermare le aeronavi Cyran..."
    ),
    262: (
        "Esistono altri cristalli. Se bramate il potere, dirigetevi verso i ruderi di Lysanas tra i monti a sud-est.\n\n"
        "E rammenta: soltanto colui che 'Ode la Voce del Vento' possiede la grazia di liberare il cristallo e richiamare i venti sopiti. Trova 'Colui che Ode la Voce del Vento'."
    ),
    263: "...",
    264: "Non posso credere ciecamente a tutto ciò che dite! Colui che ode la voce del vento... non è forse messer Cetrus? Perché cercate di aiutarci?",
    265: (
        "O figlia dei boschi, mortale dalle ali effimere e dalla vita fugace, non potrai mai comprendere il fardello del mio ruolo. Ora debbo congedarmi.\n\n"
        "Custodisci questa verità nel cuore: quand'anche usaste il potere dei cristalli per spazzare via l'impero invasore, se il vento andrà perduto, ciò che attende Sierra Terre non sarà altro che la disfatta totale.\n\n"
        "Che la brezza ti benedica, o figlia mia che porgi l'orecchio al sussurro della foresta."
    ),
    266: "Aspettate!",
    271: (
        "Onev, la Dama della Foresta... Ma che cosa sarà mai quell'essere...?\n\n"
        "No, dobbiamo affrettarci a tornare all'accampamento e fare rapporto ad Ash.\n\n"
        "Su, andiamo!"
    ),
    291: "- Sulla via di Mysilia -",
    293: "È stata una permanenza davvero prolungata. Non avrei mai scommesso che il nostro stimato pioniere si dedicasse alla bonifica con tanto ardore!",
    294: "...",
    295: (
        "Ti trovo alquanto abbattuta, Fia. Non sei più la stessa da quando siamo tornati dalle viscere di Nymelle.\n\n"
        "...Va tutto bene?"
    ),
    296: "Sto bene, suppongo. È solo che... da allora, ogni notte sono perseguitata da sogni su Rehm-Ido.",
    297: "Sogni su Rehm-Ido? E di che si tratta?",
    298: (
        "Antichi ricordi che il cristallo esausto di Nymelle mi ha trasmesso. Gli ultimi capitoli di quella fiorente civiltà chiamata Rehm-Ido, che un tempo dominava Ylva.\n\n"
        "Possedevano una conoscenza e una grandezza di gran lunga superiori alle nostre. Eppure, ammaliati dal potere dell'etere, imboccarono il sentiero dell'autodistruzione. I massacri tra umani per il controllo dell'etere non avevano mai fine, la terra avvizziva e i deboli venivano schiacciati..."
    ),
    299: (
        "E questo ti coglie di sorpresa? Per quanto risalga la memoria, gli esseri umani sono sempre stati fatti a questo modo.\n\n"
        "Siamo eternamente governati da due sole pulsioni primordiali: la paura e l'avidità. E dove albergano entrambe, non può che scaturire il conflitto. La storia tenta di insegnarci a domare i nostri istinti attraverso le tragedie del passato, ma non ho mai visto un solo mortale riuscirci davvero.\n\n"
        "Non cambieremo mai. Quegli antichi abitanti di Rehm-Ido, dopotutto, erano pur sempre uomini."
    ),
    300: "Sei il solito cinico... ma hai ragione, la gente non cambia. Ed è proprio questo a gettarmi nello sconforto. Per quanto possiamo lottare o costruire qualcosa di buono nel mondo, la crudeltà e l'egoismo umani rimarranno sempre gli stessi.",
    301: (
        "Desidero aiutare messer Cetrus con tutte le mie forze. Forse Mysilia può ancora essere salvata... ma prima o poi gli umani ricominceranno a tormentare gli Elea.\n\n"
        "Ho il terribile presentimento che per lui si stia preparando una disgrazia ancora più straziante."
    ),
    302: "Oh, Fia...",
    303: (
        "...Non possiedo risposte a tutto questo.\n\n"
        "Vorrei tanto rincuorarti con qualche bella parola di circostanza, ma ho rinunciato ad avere fiducia nel genere umano, compreso me stesso, parecchio tempo fa. Non nutro illusioni sul mondo, e così non corro il rischio di rimanerne deluso. Il mio solo proposito è restare al fianco di messer Cetrus fino alla fine, qualunque cosa accada.\n\n"
        "Anche se... un modo per modellare il mondo secondo i tuoi desideri ci sarebbe."
    ),
    304: "Un modo?",
    305: "Basterebbe che la razza umana si estinguesse del tutto, lasciando la terra unicamente agli Elea. Sarebbe un mondo sereno, privo di guerre e persecuzioni. O forse sarebbe stato ancor meglio se non fossimo mai venuti al mondo fin dal principio.",
    306: "...",
    307: "Stavo solo scherzando, Fia! Non guardarmi con quegli occhi spiritati.",
    308: "...Non sono arrabbiata. C'era solo qualcosa che mi suonava strano. Forse perché la tua 'soluzione' assomigliava fin troppo a un piano infallibile...",
    309: "...",
    310: (
        "Accidenti, questo viaggio infinito ci ha sfiniti entrambi.\n\n"
        "Su, mettiamoci in marcia. Abbiamo un disperato bisogno di un comodo giaciglio per riposare le nostre povere teste. E se riusciamo ad arrivare alle cucine di Willow prima del tramonto, potremmo persino trovare qualche torta ancora calda!"
    )
}

def run():
    wb = openpyxl.load_workbook(MAIN_FILE)
    ws = wb.active
    
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
    text_c = headers.get('text', 11)
    
    count = 0
    for row, it_text in MAIN_TRANSLATIONS.items():
        ws.cell(row=row, column=text_c, value=it_text)
        count += 1
        
    wb.save(MAIN_FILE)
    print(f"Successfully translated {count} story rows in _main.xlsx!")

if __name__ == "__main__":
    run()
