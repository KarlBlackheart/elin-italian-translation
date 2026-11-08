# coding: utf-8
"""
Elin Italian Localization - Drama Batch 3 Localizer
Translates 3 major companion & quest drama files:
- olderyoungersister.xlsx (The "Older Younger Sister" test & allowance)
- farris.xlsx (Farris of Olvina - Nymelle key, Ten Years War lore, Loytel's debt chase)
- quru.xlsx (Quruitzia - Azure tulips, Corgon, Demitas and the truth of the calamity eyes)
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DRAMA_DIR = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama')

DATA = {
    "olderyoungersister.xlsx": {
        16: "Cosa c'è, #brother2?",
        18: "Vorrei che cambiassi la tua acconciatura.",
        26: "Sì♪ Mi dona questa pettinatura, #brother2?",
        30: "#brother2? Ma sei davvero il mio #brother2?",
        32: "Sì, certo.",
        38: "Bzzzt! Risposta sbagliata!",
        39: "Tu non sei affatto il mio vero #brother2!!!",
        45: (
            "C-cosa, sul serio...!?\n\n"
            "E va bene, se sei davvero il mio #brother2, ti farò dei quiz facilissimi a cui saprai certamente rispondere!"
        ),
        46: "Domanda: Cosa significa esattamente 'sorellina maggiore'?",
        47: "Una sorella biologica più giovane separata alla nascita.",
        48: "Una sorella biologica più anziana separata alla nascita.",
        49: "Una sorella non di sangue più giovane separata alla nascita.",
        50: "Una sorella non di sangue più anziana separata alla nascita.",
        51: "Nessuna delle precedenti è corretta.",
        56: "Ding-dong! Esatto! Come ci si aspetta dal mio #brother2! Ed ora, la prossima domanda!",
        57: "Domanda: Cosa nascondo di nascosto nella stanza del mio #brother2?",
        58: "Dolcetti e provviste d'emergenza.",
        59: "Un cestino da pranzo preparato con tanto amore per il mio #brother2.",
        60: "Una lettera colma d'affetto infinito per il mio #brother2.",
        61: "Una capsula del tempo con tutti i nostri ricordi.",
        62: "Un grosso coltello da cucina.",
        63: "Non nascondo assolutamente nulla.",
        64: "Tutto quanto elencato sopra!",
        69: "Ding-dong! Esatto! Come ci si aspetta dal mio #brother2! Ed ora, la prossima domanda!",
        70: "Domanda: Qual è lo scudo più resistente e impenetrabile di tutti?",
        71: "Uno scudo d'acciaio temprato.",
        72: "Uno scudo incantato dalla magia.",
        73: "Uno scudo in rubynus.",
        74: "Uno scudo d'etere purissimo.",
        75: "Uno scudo assolutamente invincibile.",
        76: "Il dolce sorriso della tua sorellina.",
        80: "Ding-dong! Esatto! Come ci si aspetta dal mio #brother2! Ed ora, la prossima domanda!",
        81: "Domanda: Qual è la mia varietà di Putit preferita?",
        82: "Il Putit comune.",
        83: "Il Putit rosso.",
        84: "Il Putit delle nevi.",
        85: "Il Putit metallico.",
        86: "Il Re Putit.",
        87: "L'Angelo Putit.",
        88: "Il Putit lumaca.",
        89: "Il Putit vagabondo.",
        94: "Ding-dong! Esatto! Come ci si aspetta dal mio #brother2! Ed ora, l'ultima domanda decisiva!",
        95: "Domanda: Cosa desidero più di ogni altra cosa al mondo dal mio #brother2?",
        96: "Condividere tantissimo tempo insieme a te.",
        97: "Rimanere per sempre uniti l'uno all'altra.",
        98: "Che tu non mi tradisca mai e poi mai.",
        99: "Che mi accarezzi la testolina.",
        100: "Che mi rimproveri con affetto.",
        101: "Paghetta illimitata e senza fondo!",
        102: "Tutto ciò che hai appena elencato!",
        103: "Nessuna delle risposte è corretta.",
        108: "Ding-dong! Esatto! Come ci si aspetta dal mio splendido #brother2!",
        109: "Congratulazioni per aver risposto esattamente a tutte le domande! E adesso sgancia la paghetta, #brother2♪",
        110: "Consegna 10.000 Oren.",
        111: "Al momento non ho abbastanza denaro con me.",
        114: "Uau, ho trovato il mio vero #brother2!",
        120: "Capisco... allora non eri davvero il mio #brother2 dopotutto..."
    },
    "farris.xlsx": {
        12: "Dite pure, nobile #player.",
        20: "Uuh... uugh... qualcuno mi aiuti...",
        23: "Uuh... c'è... c'è qualcuno lì fuori?",
        24: (
            "Oh... sia resa grazia alla misericordiosa Ehekatl per questo fausto incontro!\n\n"
            "Io sono Farris, bardo e cantastorie di Olvina. Avendo percepito sinistri presagi a Nymelle, mi sono avventurato in questa caverna assieme a una scorta di mercenari. Ma ahimè, siamo stati colti da un feroce assalto di mostri inferociti."
        ),
        26: (
            "In qualità di custode e cantore delle tradizioni di Mysilia, è mio solenne dovere scoprire cosa stia accadendo in questa terra. Eppure, con la mia scorta dispersa, non ho altra scelta se non ritirarmi...\n\n"
            "Se intendete proseguire oltre, vi farò dono della chiave di questo passaggio. Vi supplico: avanzate e scoprite quali oscuri prodigi si celano nelle viscere di Nymelle."
        ),
        27: (
            "Oh... il vostro accampamento non dista molto da qui?\n\n"
            "Allora mi rifugerò laggiù ad attendere vostre notizie. Cercatemi non appena avrete concluso l'esplorazione: vi sono rivelazioni importanti di cui devo mettervi a parte.\n\n"
            "Che la fortuna sia con voi, nobile avventuriero. Pregherò per il vostro ritorno incolume."
        ),
        31: (
            "Vedo con sommo sollievo che siete tornato sano e salvo!\n\n"
            "Consentitemi di presentarmi degnamente: sono Farris di Olvina, cantore e tessitore di antiche memorie. Come debito di riconoscenza per avermi salvato la vita, vi rivelerò ciò che so sul conto di Nymelle."
        ),
        32: (
            "Nymelle... la caverna altrimenti nota come il Cimitero dei Venti, nonché una delle tante enigmatiche rovine sparse per Tyris. Come il nome suggerisce, un tempo era una grotta pacifica in cui l'eco del vento risuonava con malinconica dolcezza dal nulla... o per meglio dire, lo era un tempo. Perché dopo la Guerra dei Dieci Anni, Nymelle è mutata radicalmente.\n\n"
            "Il canto del vento è cessato d'improvviso, le foreste circostanti sono avvizzite e mostri grotteschi hanno iniziato a infestare le terre di superficie."
        ),
        33: (
            "Quale sia la vera origine di queste anomalie... cosa stia accadendo laggiù nelle viscere della terra?\n\n"
            "Stando alle antiche cronache, nei recessi più profondi della grotta giacciono le sacre reliquie di divinità dimenticate. Che forse abbiamo scatenato l'ira degli antichi d—"
        ),
        35: (
            "—No, non c'è alcuna reliquia sacra custodita nel ventre di Nymelle. Né l'origine di questa corruzione è riconducibile alla maledizione di un dio.\n\n"
            "Scusate l'intrusione, ma sembra proprio che quella caverna sia, dopotutto, ciò che avevamo sempre sospettato..."
        ),
        36: "Ash!",
        37: "Va tutto bene, Fia. Lascia che continui io.",
        39: (
            "...La Guerra dei Dieci Anni e le anomalie che sconvolgono Nymelle non sono affatto slegate tra loro.\n\n"
            "Avrete sicuramente udito i racconti dell'ultimo grande conflitto. La guerra divampata sul continente orientale tra il Nuovo Regno di Yerl e l'Impero del Deserto si propagò rapidamente nel resto del mondo, gettando Ylva nel caos più buio.\n\n"
            "I regni di Tyris formarono una coalizione per arginare l'invasione, ma non erano che infanti al cospetto dell'Impero, armato delle terrificanti aeronavi Cyran."
        ),
        40: (
            "Proprio quando le nostre terre stavano per essere calpestate e rase al suolo, il mio signore Cetrus parlò al vento. Una raffica di vento fulgido e luminescente squarciò i cieli di Nymelle e si abbatté contro le armate nemiche. E l'aeronave Cyran, decantata fino ad allora come invincibile, precipitò in fiamme sul suolo di Mysilia.\n\n"
            "...Fu la fine della Guerra dei Dieci Anni."
        ),
        41: (
            "È indubbio che sia stato messer Cetrus a invocare la leggendaria 'Tempesta di Nymelle'. Ma è stato solo merito suo?\n\n"
            "Quel vento di luce che danzò su tutta Mysilia e le strane mutazioni di Nymelle... Qualcosa, laggiù nel Cimitero dei Venti, deve aver risposto alla disperata preghiera di messer Cetrus. Ho ragione di credere che la chiave di questo arcano sia sepolta proprio nelle profondità della grotta."
        ),
        42: (
            "Tetri nembi si stanno addensando ancora una volta sui cieli di Tyris.\n\n"
            "L'Impero ha affilato i propri artigli spezzati e ricostruire la flotta delle aeronavi Cyran è solo questione di tempo. E questa volta attaccheranno con ferocia implacabile per consumare la loro tremenda vendetta.\n\n"
            "Messer Cetrus nutre ancora la speranza di riconciliare umani ed Elea, ma non servirà a nulla se Mysilia verrà cancellata dalla faccia della terra. Per sopravvivere dobbiamo impadronirci del 'potere' che giace a Nymelle."
        ),
        43: (
            "Non possiamo rivelarvi ogni dettaglio, né noi stessi sappiamo ancora tutto. Sì, starete sicuramente pensando di esservi cacciato in un bel pasticcio.\n\n"
            "Ma ora che vi siete stabilito qui e fate parte a tutti gli effetti di Tyris, la cosa vi riguarda da vicino.\n\n"
            "Dunque rassegnatevi e collaborate alle nostre indagini! Chissà, magari nelle viscere della grotta salterà fuori anche qualche tesoro di vostro gradimento."
        ),
        47: (
            "...Sì, ho compreso la gravità della situazione.\n\n"
            "È anche mio solenne dovere fare luce sulle cause di questa calamità a Nymelle."
        ),
        48: (
            "Rimarrò qui per assistere agli sviluppi della vicenda fino alla fine.\n\n"
            "Possa la fortuna arridervi, prode avventuriero. E che il soffio del vento benedica il vostro cammino."
        ),
        74: "(sussurra)",
        75: "(sussurra)",
        76: "Proprio così... (sussurra)",
        77: "(sussurra)",
        78: "Santo cielo...! (sussurra)",
        79: "Salute a voi, dama Farris.",
        80: "Oh, messer Loytel! Stavamo parlando giusto di voi.",
        81: "...",
        82: "I-iik...!",
        83: "...!",
        84: "A-ah, no... Quruitzia, dove stai andando... a-aspetta!",
        85: "...",
        86: "...",
        87: "Messer Loytel, gridare 'Iik!' non appena incrociate lo sguardo di una fanciulla...",
        88: (
            "No, non volevo! Non era mia intenzione!\n\n"
            "Ma... mi è tornata alla mente la diceria sui suoi occhi. L'avrete sentita anche voi da Kettle, vero? So che non le vado a genio... ho il terrore che un giorno o l'altro possa farmi cadere stecchito sul colpo..."
        ),
        89: "Messer Loytel, sono sinceramente deluso dal vostro comportamento.",
        90: "Temere quella povera ragazza come una 'calamità' senza neppure comprendere la natura del suo dono... Non vi rendete conto che è proprio questo atteggiamento a ferirla più di ogni altra cosa?",
        91: "Ma...",
        92: "Non ci sono 'ma' che tengano! Prima di paventare maledizioni e anatemi, dovreste considerare l'immensa solitudine con cui ha dovuto combattere finora. Qualunque sia il colore dei suoi occhi o il suo passato, è pur sempre una ragazza. Ha un cuore e dei sentimenti, messer Loytel.",
        93: (
            "Dama Farris... avete perfettamente ragione.\n\n"
            "A dire il vero, desidero anch'io andare d'accordo con lei. Ma è come se non parlassimo la stessa lingua, o qualcosa del genere..."
        ),
        95: "Quruitzia è una ragazza introversa e sensibile. Forse vi trattenete troppo nel timore di offenderla, finendo per rendere ogni scambio goffo e forzato.",
        96: (
            "...Nelle narrazioni esistono regole e armonie ben precise. Gli eroi delle storie superano contrasti laceranti prima di forgiare un legame di vera fratellanza.\n\n"
            "Comprendete, messer Loytel? Se desiderate schiudere il suo cuore, dovete affrontarla a viso aperto, con totale sincerità, per far emergere i suoi veri sentimenti. Dovete accogliere il grido della sua anima con tutta la vostra forza!"
        ),
        97: (
            "Uhm... be', suona un tantino melodrammatico, ma ho compreso il vostro punto, dama Farris.\n\n"
            "Far emergere i veri sentimenti di Quruitzia... Santo cielo, sarà un'impresa titanica!"
        ),
        109: (
            "#pc, arrivate giusto in tempo!\n\n"
            "Ebbene sì... stavamo affrontando a muso duro messer Loytel, che non mostra la minima intenzione di rimborsare il suo debito colossale."
        ),
        110: "Messer Loytel... avanti, mostrateci il vostro mirabolante piano per estinguere il debito!",
        111: "...",
        112: (
            "Non esiste alcun piano, dama Farris...!\n\n"
            "Ma come potrei mai ripagare una cifra astronomica come venti milioni di Oren?! Io... io...!"
        ),
        114: "Ah! Messer Loytel?!",
        115: "Presto, si sta dando alla fuga...! Acciuffatelo, non lasciatelo scappare! Su, Kettle, anche tu, inseguilo!",
        116: "A-ar件ivo...",
        117: "Anf... anf... maledizione! Non mi farete catturare!",
        118: "Ah! Con i muscoli temprati dal duro lavoro nei campi, non mi farò mai acciuffare da quattro donne e mocciosi!",
        121: "Mokyuuu!",
        123: "...Aaargh!",
        124: "Bravo Corgon, tienilo bloccato a terra così!",
        125: "Pant... pant...",
        126: "E adesso arrenditi, Loytel!",
        127: "Voi... coalizzarvi tutti contro di me in questo modo sleale...",
        128: (
            "D'accordo, d'accordo! In realtà ho abbozzato una bozza di piano di rimborso!\n\n"
            "Vado a prenderlo... aspettatemi qui un istante!"
        ),
        129: "...",
        131: "Ah! Messer Loytel è fuggito di nuovo!",
        135: "...È scappato a gambe levate... non è vero?",
        136: "Conoscendo messer Loytel, non credo che commetterà gesti sconsiderati per la disperazione, ma...",
        137: "Sono comunque in pensiero. #pc, se avete qualche idea su dove possa essersi rintanato messer Loytel, potreste andare a cercarlo?",
        148: "(sussurra)",
        149: "Mmmh... (sussurra)",
        150: "Proprio così, vedete... (sussurra)",
        151: "Mio dio, sul serio...",
        152: (
            "Da quando quel tale Demitas ha messo piede qui, l'aria è diventata irrespirabile. Anche Quruitzia è tornata a chiudersi a riccio.\n\n"
            "Non fa altro che pronunciare frasi sinistre per seminare angoscia... che individuo fastidioso."
        ),
        153: "Eppure, messer Loytel, non credo che sia un uomo malvagio nel profondo. Secondo me, Demitas porta una ferita inguaribile nel cuore.",
        154: "Mmh, una ferita nel cuore?",
        155: (
            "Non posso affermarlo con certezza. Ma c'è qualcosa di profondamente tormentato dentro di lui...\n\n"
            "Dietro quell'aspetto spettrale e quel modo di esprimersi arcaico, chissà quale indicibile dolore e rimorso si celano. È una persona incredibilmente affascinante."
        ),
        156: (
            "...A pensarci bene, dama Farris, i vostri occhi si illuminano ogni volta che posate lo sguardo su Demitas.\n\n"
            "Be', è un tipo lugubre, ma ammetto che non sembra incarnare il male assoluto."
        ),
        157: (
            "Demitas, l'Esule... Chissà com'era prima di ridursi in questo stato...\n\n"
            "E cosa mai avrà scatenato il suo esilio? Prima o poi mi piacerebbe ascoltare la sua storia dalla sua stessa voce."
        )
    },
    "quru.xlsx": {
        8: "Cosa c'è?",
        18: "Mmh-mmh♪",
        19: "Mmh, da dove proviene questo allegro canticchiare...",
        20: "Mmh-mmh♪",
        21: "Eheh, sei di ottimo umore oggi, Quruitzia. Che melodia è mai questa?",
        22: "(ti ignora) Mmh-mmh♪ Il fiore d'oltremare～♪",
        23: "(sussulta)",
        24: "Mmh-mmh♪",
        25: "Quruitzia, quella canzone... te l'ha insegnata per caso Farris?",
        26: "Mmh-mmh♪ Il tulipano fantasma azzurro～♪",
        27: "No, ti scongiuro, fermati...!",
        28: "...",
        29: "Ah, no, volevo dire... Non che tu canti male, anzi! È solo che quella canzone, ecco...",
        30: (
            "...Se quella ballata si diffondesse in giro, nascerebbero grossi guai... Sì, insomma, è una fiaba inventata! Un tulipano azzurro fantasma, andiamo, è assurdo, non trovi? Persino i bambini sanno che non esiste! È una canzonaccia orribile, ahaha!"
        ),
        31: "...",
        32: "...Eh?",
        33: "...Loytel, sei un emerito idiota!",
        34: "A-aspetta, Quruitzia, non guardarmi con quegli occhi infuriati... aspetta, ti prego...!",
        35: "...",
        36: "Ma non sarà che... crede davvero all'esistenza del tulipano azzurro fantasma? Non è possibile...",
        53: "Carezzina, carezzina♪",
        54: "Mokyu!",
        55: "Eheh, ti fa il solletico, Corgon?",
        56: "Mokyu.",
        57: "...",
        58: "...",
        59: "Carezzine, tante carezzine♪",
        60: "Mokyu... Mokyu!",
        61: "Eheh, soffri il solletico, vero Corgon?",
        63: "Mmh...?",
        64: "Sento dei passi... Qualcuno si sta avvicinando da quella parte.",
        67: "Chi mai può essere a quest'ora di notte?",
        69: "Dunque è questo il luogo...",
        70: "Mokyu...?",
        71: "...La prole di un drago e una fanciulla dallo sguardo funesto... Qual è il significato di tutto ciò...?",
        72: (
            "Quest'uomo... quegli occhi spettrali sotto il cappuccio... Non è un essere umano... È una creatura empia...\n\n"
            "Corgon, allontanati da lui! Corri ad avvisare tutti gli altri!"
        ),
        73: "Heh heh heh... Una creatura empia, dici?",
        74: "Cosa c'è di tanto divertente?!",
        75: (
            "Non appartieni forse alla medesima genia, o Quruitzia dagli occhi di calamità? Non te ne avvedi? Un potere arcano e ancestrale alberga dentro di te: una forza rovinosa portatrice di sciagura."
        ),
        76: "Tu... come fai a sapere il mio nome...?!",
        77: "Ahi! D'accordo, d'accordo, piccoletto, sto arrivando, smettila di tirarmi per la giacca... Ma... chi diavolo è costui?!",
        78: "Amici miei!",
        79: "Quest'uomo...",
        81: (
            "Oh... Un drago della leggenda, una strega dagli occhi funesti e il 'Primo Alchimista'. Invero, questo luogo sembra scaturito direttamente dal mito antico."
        ),
        82: "Un momento, tu conosci questo tizio, Kettle?!",
        83: "'Kettle'... È dunque questo il tuo nuovo nome?",
        84: (
            "...Non c'è motivo di allarmarsi, amici miei. Il nome di quest'uomo è Demitas, l'Esule. Non ha alcuna intenzione di farci del male."
        ),
        85: "L'Esule...?",
        86: (
            "Un'anima pietosa che, avendo osato infrangere i tabù del cosmo, è stata condannata a servire gli dèi per espiare le proprie colpe. Benché, nel suo caso, persino la divinità a cui era devoto lo abbia infine abbandonato."
        ),
        87: (
            "...Non sei mutato affatto, vedo. Invero, ora vago per le terre mortali senza meta né proposito, spogliato di ogni significato.\n\n"
            "Eppure, dimmi... l'hai forse trovato tu, quel senso o quello scopo? Temo di essere ancora troppo giovane per comprendere l'eterno patimento, 'Kettle'."
        ),
        88: (
            "Io sono un semplice alchimista errante, che si lascia trasportare dalla brezza. Forse lungo il cammino troverò un senso, o forse no.\n\n"
            "Demitas, posso domandarti per quale ragione sei giunto in queste lande?"
        ),
        89: (
            "...Un demone che dimorava qui da tempi immemori è svanito nel nulla. Tephra, mi pare fosse il suo nome.\n\n"
            "Sono passato unicamente per sincerarmi di cosa fosse accaduto."
        ),
        90: (
            "...O forse sono stato attirato dal nauseabondo sentore del fato che permea questa terra. Fanciulli derelitti, stolti e ripugnanti, abbandonati dagli dèi, stanno per dare inizio a un nuovo vortice di follia.\n\n"
            "Molto interessante. Rimarrò qui per qualche tempo ad osservare in silenzio lo svolgersi degli eventi."
        ),
        108: "Le parole pronunciate da quell'uomo...",
        109: "...",
        110: "Ugh, mi rimbombano nella testa senza lasciarmi pace.",
        112: "Il potere che dorme assopito dentro di me...",
        113: "Un potere antico e rovinoso, portatore di sciagura.",
        114: "Mokyu...",
        115: (
            "Da quando ho incontrato Kettle... no, da quando vivo con Loytel e tutti gli altri, gli incubi sono diminuiti. Avevo smesso di tormentarmi su chi fossi realmente."
        ),
        116: "Eppure...",
        117: "Corgon, io...",
        118: "Non riesci a prender sonno, vero, fanciulla?",
        119: "Demitas...",
        120: "Il potere che arde nel tuo sguardo... a quanto pare non sei ancora in grado di dominarlo.",
        121: "Cosa vorresti insinuare sui miei occhi...?!",
        122: (
            "Heh heh heh... Quel bagliore... Ogniqualvolta la luce purpurea della calamità rifulge nelle tue iridi, il caos piomba sul mondo terreno. Ragazza dagli occhi funesti, non conosci ancora il tuo destino; eppure, l'istante fatidico giungerà. Proprio come in quel tragico giorno."
        ),
        123: "...Quel giorno?",
        124: "Non rammenti? Di certo non avrai cancellato la memoria del massacro che rase al suolo il tuo villaggio natale.",
        125: "Il mio villaggio... Come puoi saperlo?! Io e te non ci siamo mai incontrati prima d'ora!",
        126: (
            "Heh heh heh... Ne sei davvero convinta?\n\n"
            "Una simile maledizione non l'avevo mai scorta in tutta la mia esistenza. Il bagliore scarlatto che brillava nelle tue pupille... era forse la fiamma dell'odio o un'estatica luce primordiale?\n\n"
            "Nell'arco di una sola notte, il tuo intero villaggio fu..."
        ),
        127: "Basta! Taci!",
        129: "Basta! Ti prego!",
        130: (
            "...Quella voce... No... che leggerezza imperdonabile evocare il passato...\n\n"
            "Il tuo potere... Già, noi tutti abbiamo vegliato con estrema attenzione su di te, che erediti quell'antico lignaggio di sangue.\n\n"
            "Dimmi, ragazza: credi davvero che quel giorno il soccorso di 'Kettle' sia stato una fortuita coincidenza?"
        ),
        131: "Lasciami in pace! Non voglio ascoltare un'altra sola delle tue menzogne!",
        132: (
            "Heh heh heh... Non sai assolutamente nulla.\n\n"
            "Quell'uomo vi sta unicamente manipolando per i propri fini. Salvarvi la vita, farvi incontrare con il drago... ogni cosa è stata orchestrata per saziare le sue ambizioni."
        ),
        133: "Non ti credo! Tutto ciò che esce dalla tua bocca è solo veleno e menzogna!",
        134: "Mokyuu!!",
        135: (
            "Oh... Il drago risponde alla tua collera? È sbalorditivo come un essere umano possa legarsi così visceralmente a un drago. Eppure questa creatura, benché ancora tenera d'età...\n\n"
            "La prole del Drago d'Acciaio... Una pietra magica... Un ricettacolo di pietra...\n\n"
            "Hehehe, capisco... dunque stanno così le cose."
        ),
        136: (
            "La notte volge al termine. Prima che io mi dilegui, ti svelerò un'ultima verità, fanciulla dallo sguardo funesto.\n\n"
            "Quel cucciolo di drago è 'troppo piccolo'. Per sua stessa volontà, o forse per volere di una forza esterna, la sua naturale crescita viene soffocata.\n\n"
            "E purtroppo, di questo passo, non vivrà ancora a lungo."
        ),
        137: "Corgon... Aspetta! Spiegati! Che cosa significa?!",
        138: "Domandalo a 'Kettle'. Sembra proprio che vi stia celando una moltitudine di segreti... Heh heh heh..."
    }
}

def run():
    total_updated = 0
    for fname, rows in DATA.items():
        fpath = os.path.join(DRAMA_DIR, fname)
        if not os.path.exists(fpath):
            print(f"Skipping {fname}, not found.")
            continue
        wb = openpyxl.load_workbook(fpath)
        ws = wb.active
        headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
        text_c = headers.get('text', 11)
        for r, val in rows.items():
            ws.cell(row=r, column=text_c, value=val)
        wb.save(fpath)
        print(f"Updated {len(rows)} rows in {fname}")
        total_updated += len(rows)
    print(f"Total rows updated across 3 files: {total_updated}")

if __name__ == "__main__":
    run()
