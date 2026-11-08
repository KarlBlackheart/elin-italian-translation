# coding: utf-8
"""
Elin Italian Localization - _tutorial.xlsx Full Localization
Translates all fairy guide Nerun's tutorial dialogues, advice, humor, and game mechanics.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TUTORIAL_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama', '_tutorial.xlsx')

TUTORIAL_TRANSLATIONS = {
    13: "...",
    24: "...",
    30: "...",
    43: "...",
    54: "È già arrivato l'autunno...\nIl tempo vola davvero quando ci si diverte!",
    55: "Dato che Tyris Settentrionale è un continente del nord,\nanche durante le estati più assolate in cui il sole picchia forte,\nnon fa mai così caldo da impedirti di uscire all'aperto.",
    56: "Tuttavia, l'inverno si fa sentire eccome nella vita di tutti i giorni!\nFaresti bene a iniziare a prepararti fin da ora.",
    57: "Se coltivi dei campi, con l'arrivo del gelo invernale appassiranno tutti.\nQuindi assicurati di completare il raccolto prima di allora, intesi?",
    58: "E quando laghi e mari ghiacceranno del tutto,\nnaturalmente non potrai più pescare alcunché.\nSe ti guadagni da vivere con la pesca, tienilo bene a mente!",
    59: "Oh, quasi dimenticavo! A dicembre si tiene una celebre festa\nin un villaggio a est chiamato Noyel.\nVenderanno dei dolciumi squisiti alle bancarelle:\ndevi assolutamente andarci a dare un'occhiata! Capito?!",
    60: "Oltre all'inverno, in ogni stagione si tengono feste e fiere in tutto il continente.\nQuando hai un momento libero, farci un salto è sempre un'ottima idea!",

    66: "...Vuoi che ti insegni come si usa un'ascia?",
    67: "Se clicchi sull'icona della borsa sullo schermo, si apre il tuo inventario, giusto?\nDa lì trova l'ascia e cliccaci sopra col tasto destro per impugnarla.\nUna volta che la stringi in mano, fai clic destro su un albero a terra e potrai abbatterlo!",
    68: "...Eh? Sapevi già tutto?",
    69: "...Ehehe... beh, insomma...\nNon prendertela... Tutti iniziamo come principianti!",
    70: "...",
    71: "A proposito, hai notato gli slot numerati in basso a destra sullo schermo?\nSe trascini l'ascia in uno di quegli slot,\npotrai cambiare al volo gli attrezzi usando la rotellina del mouse.\nComodissimo, vero?",
    72: "...",
    73: "...S-sì... scommetto che sapevi anche questo!\nLo immaginavo, ma per sicurezza... una rinfrescata non fa mai male, no?",
    74: "Ebbene...",

    80: "Ehi, hai mai sentito parlare dell'influenza cittadina?",
    81: "Completando incarichi, investendo fondi o contribuendo al benessere di una città,\nla tua 'influenza' in quel luogo crescerà costantemente.",
    82: "Con l'aumentare dell'influenza potrai aggiornare la bacheca degli incarichi,\nchiedere ai bottegai di rifornire le scorte sul momento,\ne perfino domandare favori che altrimenti sarebbero impossibili!",
    83: "...E non finisce qui!",
    84: "Puoi perfino adoperare l'influenza come valuta di scambio!\nAd esempio, uno degli articoli più gettonati è il 'Mandato di Confisca Mobili'\nvenduto dal segretario municipale.",
    85: "Puoi usare questo tagliando per confiscare d'autorità qualsiasi mobile collocato in città!\nÈ una mano santa se cerchi arredi rari reperibili solo in determinate località.",

    90: "Guarda un po'! C'è una cassa di spedizione qui.",
    91: "Troppi oggetti nello zaino ti appesantiscono la marcia...\nMa gettarli via ti spezzerebbe il cuore...\nLa cassa di spedizione è un servizio utilissimo nato per risolvere questo dilemma!",
    92: "Se infili i tuoi oggetti in questa cassa,\nverranno automaticamente recapitati alla prossima dimora in cui metterai piede.",
    93: "Puoi usarla per spedire mobili pesanti acquistati in città,\no per traslocare comodamente merci tra una dimora e l'altra.\nUna volta presa la mano, non potrai più farne a meno!",

    99: "Buongiorno, dormiglione!",
    100: "...Tranquillo, non stai avendo le allucinazioni.\nIo sono Nerun, la tua guida fatata, e sono qui per assisterti nella tua epica avventura!",
    101: "Beh, hai ancora la faccia assonnata, quindi per oggi\nti consegnerò semplicemente questo \"Registro delle Avventure\".\nUno strumento utilissimo che ti permette di riascoltare i nostri dialoghi ogni volta che lo desideri!",
    102: "Bene, ci rivedremo molto presto...",

    106: "Aaaaaaaaargh!!",
    107: "Accidenti, il tuo equipaggiamento è stato corroso dall'acido e si è arrugginito...",
    108: "Quando un oggetto arrugginisce, le sue statistiche subiscono un malus di -1, -2 e così via,\nperdendo gran parte della sua efficacia originale.",
    109: "In questo mondo pullulano creature subdole capaci di spruzzarti addosso acido al minimo contatto,\nattaccarti malattie orribili o distruggere il tuo equipaggiamento, perciò tieni gli occhi aperti!\n...Ricorda: imparare dai propri errori è ciò che fa di te un vero avventuriero!",
    110: "...A proposito: anche se un'arma sembra inservibile per la ruggine,\npuoi sempre ripristinarla usando una mola per affilare!\nForse ti conviene tenerla da parte invece di disfartene, non trovi?",

    114: "Ecco qua l'elenco dei residenti della tua dimora.",
    115: "Vedi l'icona della valigetta accanto ai loro nomi?\nSe ci passi sopra il cursore del mouse, potrai visualizzare i loro hobby e mestieri.",
    116: "I residenti svolgono professioni assai diverse:\nalcuni aumentano la sicurezza o la fertilità della terra,\nmentre altri producono risorse e manufatti preziosi.",
    117: "Tuttavia, se l'ambiente non è idoneo, i residenti incroceranno le braccia e non lavoreranno.\nI mestieri evidenziati in giallo indicano compiti attualmente impossibili da svolgere!",
    118: "Di solito, basta collocare nella dimora il mobilio adatto a quel lavoro\nper vederli mettersi all'opera con entusiasmo!\nAd esempio, per un incarico di ricerca è fondamentale avere una libreria.",
    119: "Con la crescita dei residenti aumenterà anche la loro efficienza lavorativa.\nAnche la comodità del loro letto influisce parecchio sulle prestazioni,\nquindi è saggio procurare un bel giaciglio per ciascuno di loro!",

    122: "Un bel ciuffo d'erba da pascolo, eh?",
    123: "Quest'erba cresce un po' ovunque,\nma in realtà è un foraggio eccezionale per il bestiame!",
    124: "Se la spargi sul terreno o la riponi in un contenitore condiviso,\ngli animali della tua dimora se ne nutriranno spontaneamente ogni giorno.\nE a volte, gli animali ben pasciuti produrranno uova fresche o latte!",
    125: "Perché non raccogli qualche seme da portare con te,\ncosì da iniziare a coltivarla nella tua dimora?",

    128: "Quella è acqua.",
    129: "...",
    130: "Hai appena fatto quella faccia tipo:\n\"Ma va'? Che scoperta geniale!\", non è vero?",
    131: "...E va bene, allora scopri sulla tua pelle quanto siano terrificanti le acque profonde!\nSoffocherai e morirai prima di rendertene conto. Io ti avevo avvertito, eh!",

    134: "Povero #pc...\nCome hai potuto farti ammazzare con tanta facilità...?",
    135: "Ma come hai fatto a morire in quel modo?\nBeh, non disperare:\nti riporterò in vita tutte le volte che sarà necessario!",
    136: "Naturalmente, la morte esige sempre un suo tributo.\nPotresti perdere sul posto una parte delle tue monete d'oro,\ne le tue statistiche potrebbero subire un calo, quindi cerca di evitarla se puoi!",
    137: "Tuttavia, per i primi 90 giorni dal tuo arrivo su queste terre,\nsarai del tutto immune a qualsiasi penalità di morte!",
    138: "Perciò approfittane per lanciarti in ogni sorta di sfida\ne fare preziosa esperienza sul campo! Eheheh.",

    142: "Oh no... il tuo compagno d'avventure è caduto...",
    143: "Dai, su, non buttarti giù in questo modo!\nVedrai che il tuo alleato si rimetterà in sesto e tornerà arzillo\nnel giro di una settimana circa.",
    144: "Quando un compagno muore, lascia temporaneamente il gruppo\ne viene trasferito alla dimora a cui appartiene.\nPerciò controlla alla base dopo un po' di tempo.",
    145: "Se non hai pazienza di aspettare, puoi rivolgerti ai baristi nelle varie città:\nper qualche spicciolo, saranno felici di richiamarlo all'istante al tuo fianco!",
    146: "E se si tratta del cucciolo che ti ha affidato quella fanciulla... Fiama,\npuoi andare a parlarle in qualsiasi momento per riaverlo con te!",
    147: "Capisco che sia un momento difficile,\nma non arrenderti, tieni duro...",

    152: "Dlin-dlin!\nIl tuo periodo di apprendistato da novizio è ufficialmente concluso!",
    153: "Ma guarda un po'... non sei morto neanche una singola volta, eh?\nBravo, bravissimo! Vieni qui che ti meriti un bel grattino sulla testa!",
    155: "Il numero totale di volte in cui sei morto in questo periodo è ben #1...\nMa che cosa stavi combinando di grazia?!",
    156: "Persino io, in tutta la mia lunga vita, non ho mai visto un avventuriero simile...",
    157: "D'ora in avanti, ogni volta che morirai incorrerai nelle normali penalità della morte.\nPerciò fai molta attenzione!",

    162: "Che orrore! C'è spazzatura dappertutto!",
    163: "Non sarai mica... uno di quegli avventurieri disordinati e cialtroni?\nSe non fai un po' d'ordine, diventerà un bel problema!",
    164: "Con l'aumentare della popolazione i rifiuti si accumuleranno sempre di più,\nquindi dovrai prendere dei seri provvedimenti.",
    165: "La soluzione più rapida in assoluto\nè emanare la \"Legge Severa Contro l'Abbandono dei Rifiuti\".",
    166: "Con questo editto la spazzatura scomparirà quasi del tutto.\nTuttavia la moralità pubblica subirà un calo,\nquindi prima o poi vorrai passare a un metodo di smaltimento più decoroso.",
    167: "Piazzare cartelli di discarica e bidoni per i rifiuti\nincoraggerà i residenti a gettare l'immondizia in base al loro senso civico.",
    168: "E se hai residenti incaricati delle pulizie,\nla probabilità che differenzino correttamente i rifiuti aumenterà notevolmente!",
    169: "I rifiuti possono essere smantellati ricavandone risorse preziose,\nquindi ti conviene sfruttarli al massimo!",

    173: "Uhm, stai già esplorando una caverna?\nCominci a sembrare un vero avventuriero!",
    174: "Ma prima di addentrarti nei cunicoli oscuri, datti un'occhiata.",
    175: "...Sei proprio sicuro che quell'armatura sia sufficiente?",
    176: "Nelle caverne brulicano nemici insidiosi.\nSe ti mancano pezzi di corazza in tre o quattro slot,\nti conviene fare marcia indietro per il bene della tua pelle!",
    177: "Alla tua dimora puoi forgiare armi e corazze semplici,\noppure puoi andare a fare acquisti nelle botteghe in città.",
    178: "Il Valore di Protezione (PV) è una statistica fondamentale\nche riduce i danni subiti dai colpi nemici.\nSe gli attacchi ti fanno troppo male, corri ad alzare la difesa!",

    181: "Ottimo lavoro: la tua Pietra del Focolare sta crescendo rigogliosa.",
    182: "Ebbene sì: questa pietra arcana ha la particolarità di svilupparsi!\nE man mano che cresce, la tua dimora riceve magnifici vantaggi,\ncome un limite di residenti più alto o nuovi editti governativi.",
    183: "Certi nemici usano attacchi elementali capaci di incenerire oggetti ed equipaggiamento,\nma con la Pietra potenziata, potrai perfino scongiurare questo flagello all'interno della dimora!",
    184: "La Pietra cresce automaticamente con le spedizioni e col passare dei giorni.\n...Tieni presente, però, che con la crescita della Pietra sale anche il livello di pericolo della dimora...\nil che significa che si presenteranno mostri sempre più minacciosi!",
    185: "Puoi emanare l'editto di \"Soppressione della Crescita\" per fermare lo sviluppo della Pietra.\nSe i nemici attuali ti stanno già dando troppo filo da torcere,\nè saggia norma bloccare la crescita per un po'.",

    190: "Congratulazioni per aver conquistato un Punto Talento!",
    191: "...Eh? Non sai cosa siano i Talenti?",
    192: "I Talenti sono i tuoi tratti distintivi più speciali,\ncome essere fulmineo nei movimenti o forte come un toro!\nPuoi acquisirli spendendo Punti Talento.",
    193: "Vedi l'indicatore con la piuma azzurra in fondo allo schermo?\nCompiendo azioni e migliorando te stesso, questo indicatore si riempie.\nUna volta colmo, riceverai un prezioso Punto Talento!",
    194: "Clicca sull'indicatore per aprire l'elenco dei Talenti disponibili:\nscegli con cura quelli che ritieni più utili per il tuo stile di gioco!",
    195: "Puoi anche conservare i Punti Talento per il futuro\nse al momento non trovi nulla di indispensabile.\nÈ un'ottima strategia tenerne qualcuno di scorta!",
    196: "Ricorda che alcuni Talenti richiedono prerequisiti specifici:\nad esempio, il talento \"Buongustaio\" non comparirà\nfinché non avrai appreso l'abilità \"Cucina\"!",

    201: "Molto bene, hai recuperato un bel tronco!",
    202: "I tronchi d'albero — o meglio, il Signor Tronco — sono i materiali di base per l'artigianato,\ne sono ottimi anche come combustibile per il falò!",
    203: "Ma... non finisce qui!\nLavorando il Signor Tronco, puoi raffinarlo trasformandolo in resistenti \"Assi di Legno\"!",
    204: "Eh...? Come si lavora?\nBeh, perché non chiedi consiglio al Signor Tronco in persona?\nIl suggerimento è: 'attrezzatura di lavorazione'!",
    205: "...Oh, e ricorda che puoi sbozzare anche le pietre grezze\nper ricavarne \"Pietre Tagliate\": tienilo sempre a mente!",

    209: "Bravissimo, hai fabbricato un attrezzo!",
    210: "Ogni oggetto di questo mondo è composto da uno specifico \"materiale\".\nE ogni materiale racchiude proprietà uniche e distinte.",
    211: "Per esempio, gli oggetti di carta sono leggerissimi,\nmentre quelli di ferro sono pesanti ma assai duri da incendiare!",
    212: "Una delle caratteristiche fondamentali dei materiali è la \"durezza\",\ncruciale soprattutto per strumenti da scavo come i picconi.\nLa durezza determina quali tipi di rocce e minerali puoi estrarre!",
    213: "Se ti imbatti in vene minerarie che il tuo piccone non riesce a scalfire,\nprova a forgiarne uno nuovo impiegando un materiale più duro.",
    214: "Beh... potresti anche potenziare a dismisura l'abilità di estrazione\ne cavartela con la pura forza bruta, ma insomma... eheheh!",

    219: "Magnifico, hai costruito il banco da lavoro!",
    220: "Ora lascia che ti sveli un segreto cruciale per diventare un provetto avventuriero...\nEsatto: sto parlando del 'clic centrale' del mouse!",
    221: "Facendo clic centrale, puoi 'interagire' direttamente con gli oggetti nello zaino,\ncon le creature o con gli elementi sulla mappa.",
    222: "Ti permette di compiere una miriade di azioni speciali:\nspostare con un calcio creature fastidiose,\nazionare leve e interruttori,\nmiscelare pozioni alchemiche,\no perfino frugare nello zaino del tuo compagno!\nSblocca tutto un ventaglio di manovre che normalmente non potresti eseguire!",
    223: "Inoltre, quando sistemi mobili o innalzi pareti,\nil clic centrale ti permette di ruotarli all'istante...\nGli avventurieri che ignorano questo trucco non hanno vita lunga in questo mondo!",
    224: "Clic centrale... tutto chiaro, hai memorizzato?",
    225: "...",
    226: "Ah già, puoi usare anche il tasto 'R' sulla tastiera\ncome comodissima alternativa al clic centrale!",
    227: "Ebbene... ci si vede più tardi!",

    234: "Waaah... mi regaleresti dei funghetti?",
    235: "Certamente.",
    236: "Neanche per sogno.",
    239: "Gnam gnam gnam... che delizia!\nI funghi sono la mia passione assoluta! Ricordatelo bene, intesi?",
    240: "I funghi sono squisiti, ma non riempiono a lungo lo stomaco,\ne col tempo purtroppo marciscono: questo è il loro difetto!",
    241: "Ebbene sì: il cibo lasciato all'aria a lungo va a male.\nNon lo sapevi mica?",
    242: "Com'è ovvio, mangiare roba avariata ti farà venire un brutto mal di pancia,\nperciò non toccarla mai e poi mai!",
    243: "Pesce fresco e carni crude marciscono in fretta,\nmentre noci, semi e cibi cotti durano molto più a lungo.",
    244: "Con una mola o macina di pietra puoi perfino preparare gallette che non marciscono mai!\nPrima di un lungo viaggio, assicurati sempre di avere razioni a lunga conservazione:\nè la regola d'oro di ogni viandante!",
    247: "Taccagno e spilorcio!",

    251: "Mamma mia, guarda quanti mercanti e artigiani ambulanti!\nVendono ogni ben di dio!",
    252: "Sembra quasi un vivace angolino di città!\nGuarda: quella bacheca espone incarichi e richieste per noi avventurieri!",
    253: "Completare le missioni frutta ricche ricompense,\nquindi controlla la bacheca ogni volta che ne vedi una!\nAttento però alle missioni con molte ★: sono le più ostiche e pericolose!",
    254: "Oh, in questo accampamento c'è perfino un guaritore!\nIl guaritore risana le alterazioni di stato, mentre il mago laggiù\npuò identificare gli oggetti misteriosi... anche se ovviamente vorrà essere pagato!",
    255: "...",
    256: "Quel capocarovana laggiù...",
    257: "È... è troppo carino!\nIndossa un cappuccio a forma di gattino!\nDai, andiamo subito a salutarlo!",

    261: "Una città vera e propria!\nChe meraviglia, quanta gente e che allegra confusione!",
    262: "Compravendita, addestramento, commercio, gioco d'azzardo, missioni, cure...\nCi sono infiniti servizi qui!\nE se ti perdi, niente paura: basta chiedere a una guardia e ti indicherà la strada. Eheh!",
    263: "Naturalmente, ogni città di Tyris Settentrionale ha la sua personalità:\ndifferiscono per sviluppo, merci in vendita, botteghe e abilità da apprendere.",
    264: "Anche le richieste affisse alle bacheche variano da città a città,\nquindi esplorarle tutte è un'esperienza entusiasmante!",
    265: "Ma per ora, che ne dici se andiamo a perlustrare questa qui?",

    270: "...",
    271: "Hai combinato una marachella, vero...?",
    272: "Lo sapevo... ho sentito il tuo karma precipitare verso il basso!\nIn questo mondo, commettere malefatte fa calare il karma,\ne se scende sotto lo zero vieni marchiato come criminale!\n...E fare il fuorilegge rende la vita un inferno!",
    273: "Porta a termine incarichi leali, restituisci gli oggetti smarriti\ne cerca sempre di compiere buone azioni per accrescere il tuo karma.",
    274: "...A proposito: il crimine più imperdonabile in assoluto è l'evasione fiscale!\nSe non paghi le tasse per quattro mesi consecutivi,\nverrai dichiarato subito ricercato e ti daranno la caccia per farti la pelle!",
    275: "Perciò... occhi aperti, intesi?",

    280: "...",
    281: "No...! Stattene lontano da me, brutto depravato!",
    282: "Non riesco a credere che tu sia caduto così in basso da diventare un criminale!\nMi hai davvero spezzato il cuore...",
    283: "…Proprio così: se il tuo karma scende sotto zero, diventi un ricercato.\nLe guardie ti daranno la caccia, i mercanti si rifiuteranno di commerciare con te,\ne perfino le tue amate sorelline ti guarderanno con totale disprezzo!\nVivrai una vita miserabile da nemico pubblico della società!",
    284: "Sigh... va bene, c'è ancora speranza di redenzione per te.\nQuando il karma è in negativo, risale lentamente col passare del tempo.\nSe smetti di commettere delitti e aspetti con pazienza, prima o poi le acque si calmeranno.",
    285: "Nella malfamata città di Derphy, dove la legge non ha valore,\npotrai saldare le tue tasse arretrate e fare affari con i mercanti locali.",
    286: "Non temere, io credo ancora in te.\nFai ammenda per i tuoi peccati e torna da me a testa alta, d'accordo?",
    287: "A presto...",

    291: "Così alla fine anche tu hai contratto la terribile piaga...",
    292: "Non sgranare gli occhi: non serve agitarsi.\nAnche se non fai nulla, la corruzione dell'etere avanza inesorabile col tempo.",
    293: "I tuoi sintomi sono ancora lievi e per ora puoi ignorarli,\nma se trascuri la malattia, le deformazioni peggioreranno fino a condurti alla tomba.\n...Dobbiamo assolutamente trovare un modo per rallentare il morbo!",
    294: "Ehi, non fare quella faccia cupa!\nAbbiamo ancora parecchio tempo, troveremo una soluzione insieme, vedrai!",
    295: "Ora che ci penso...\nNel laboratorio tra le nevi a sud di Noyel c'era un nano delle colline\nche collezionava stranezze e reliquie. Forse lui sa qualcosa...",

    301: "Oh, hai iniziato a venerare una divinità?\nEhehe...",
    302: "Avanti, racconta! Chi hai scelto come tuo patrono celeste?\nChi è il tuo primo dio? Eheh!",
    303: "...#god.",
    304: "Capisco... quindi sono questi i tuoi gusti, eh?\nUhm, interessante...",
    305: "Quando veneri un dio, riceverai doni e benedizioni divine\nin base alla profondità della tua fede.\nLa fede si rinsalda offrendo tributi e col passare dei giorni.",
    306: "Una volta al giorno puoi rivolgere la preghiera alla tua divinità.\nPuò sanare le tue ferite e, se il dio è di buonumore, potresti perfino ricevere una grazia speciale!",
    307: "Pregare con costanza tempra la tua abilità di fede,\nquindi cerca di rivolgere una preghiera al cielo almeno una volta al dì!",
    308: "Bene, questo è quanto per ora.\nBada solo a non far infuriare #god!",

    311: "Oh... ti senti un po' indebolito per caso?",
    312: "Cosa intendo? Dai un'occhiata alle tue statistiche primarie per un momento!\nNoterai che sono più basse del solito, vero?",
    313: "Certi nemici possiedono attacchi malevoli in grado di fiaccare le tue capacità.\nAll'inizio sembra poca cosa, ma se i malus si accumulano possono diventare letali!",
    314: "Se possiedi una Pozione di Ristoro Corporeo o una Pozione di Ristoro Mentale,\nbevendo quelle pozioni ripristinerai all'istante le statistiche debilitate!",
    315: "Se non hai rimedi a portata di mano, puoi rivolgerti a un guaritore in città.\nTi costerà qualche oren, ma saprà rimetterti in sesto...",
    316: "Beh, l'ideale sarebbe non farsi colpire affatto!\nContro nemici insidiosi da vicino, la strategia migliore è sempre attaccarli dalla distanza!",

    321: "Caspita, hai guadagnato fama e notorietà!\nComplimenti!",
    322: "Puoi accrescere la tua fama compiendo missioni gloriose\ned espugnando le profondità delle Nefia!",
    323: "Con l'aumentare della fama ti verranno affidati incarichi via via più ardui,\ne compariranno sotterranei sempre più impervi e pericolosi!",
    324: "Accumula tanta fama e diventa presto un avventuriero leggendario!",
    325: "...",
    326: "A proposito...\nse la tua fama dovesse salire troppo e i pericoli diventassero ingestibili,\npuoi sempre vendere un po' della tua fama agli informatori in città...",
    327: "Ci vediamo...",

    333: "Hai una cera terribile, va tutto bene...?",
    334: "Il modo migliore per scuotersi di dosso la spossatezza\nè farsi una bella dormita ristoratrice in un letto soffice e comodo!",
    335: "Dormendo a sufficienza potresti avere lampi di genio per nuove ricette,\ntemprare il tuo potenziale o persino apprendere incantesimi in sogno!",
    336: "Se non hai ancora costruito un letto vero e proprio,\npuoi usare l'abilità 'Riposa' per schiacciare un pisolino.\nNon è efficace quanto un vero materasso, ma fa il suo dovere!",
    337: "Durante il riposo il recupero naturale di salute e mana subisce un'impennata,\nquindi è saggio riposarsi subito dopo una dura battaglia.\nAttento però: se sei sfinito dal lavoro o stai morendo di fame, il recupero si blocca del tutto!",
    338: "D'accordo, per ora è tutto.\nAssicurati di dormire le tue ore!",

    343: "Ehi, aspetta un attimo!\n...Non... non scappare via!",
    344: "*pant* *pant*\n...*coff coff*",
    345: "Ora ti trovi nella 'Mappa del Mondo'.\nNella mappa del mondo puoi coprire distanze immense,\nma in compenso il tempo scorre a una velocità vertiginosa!",
    346: "Se non hai abbastanza provviste nello zaino morirai di fame in men che non si dica,\ne condizioni letali come il veleno progrediscono a ritmo serrato.\nFai estrema attenzione prima di muovere un passo!",
    347: "Se ti trovi a corto di cibo, prova a cliccare sulla tua stessa figura:\nentrerai in una 'Mappa Esterna' corrispondente al terreno su cui ti trovi.\nTra boschi e pianure troverai di sicuro abbondanza di cibo selvatico da raccogliere!",
    348: "Oh, e mentre viaggi lungo la mappa del mondo\npotresti subire improvvise imboscate da parte di mostri erranti!",
    349: "Vedi quella strada maestra alla tua destra?\nLungo le strade gli agguati sono molto più rari e sicuri.\nPiù ti allontani dalla via maestra, più rischi di imbatterti in abomini letali.\nPerciò, finché sei agli inizi, cerca di viaggiare lungo la strada!",
    350: "A presto...",

    355: "Oh, ebbene sì.\nQuesto è il termine dei contenuti previsti per la versione Demo.",
    356: "Puoi comunque spingerti a visitare le città e le regioni più avanti lungo la via,\nma non te lo consiglio caldamente: vi sono molti aspetti ancora in fase di sviluppo,\ne finiresti per rovinarti la sorpresa e il divertimento più avanti!",
    357: "Dopo aver fatto un po' di sano turismo,\nchiudi pure con calma il gioco e attendi le prossime avventure!",

    360: "Dimmi pure, che c'è?",
    361: "Che tempo farà domani?",
    362: "Come sarà la mia sorte oggi?",
    363: "Nulla di particolare.",
    368: "...Chi può dirlo? Chiedilo al vento!",
    373: "Non chiamarmi se non hai nulla di serio da chiedermi!"
}

def apply():
    print(f"Loading {TUTORIAL_FILE}...")
    wb = openpyxl.load_workbook(TUTORIAL_FILE)
    ws = wb.active
    
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1)}
    col_text = headers.get('text', 4)
    
    updated = 0
    for r, it_text in TUTORIAL_TRANSLATIONS.items():
        if r <= ws.max_row:
            ws.cell(r, col_text, it_text)
            updated += 1
            
    wb.save(TUTORIAL_FILE)
    print(f"Aggiornate con successo {updated} righe in _tutorial.xlsx")

if __name__ == '__main__':
    apply()
