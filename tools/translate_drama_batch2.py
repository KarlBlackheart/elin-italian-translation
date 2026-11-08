# coding: utf-8
"""
Elin Italian Localization - Drama Batch 2 Localizer
Translates 7 rich story & quest drama files:
- _event.xlsx (Divine Sword encounter)
- _adv.xlsx (Marriage vows, proposal, priest ceremony)
- tyche.xlsx (Tyche & Vishnu - The Legendary Curry of Eyth Terre)
- fairy_nanasu.xlsx (Nanasu, Raina & Poina - Bag of Holding quest)
- _chara.xlsx (Ambient character dialogue & party interactions)
- melilith.xlsx (Melilith the Ghost Princess & the friendship ticket)
- elder_exile.xlsx (The Exile Elder, Duponne the dragon pet & Issizzle)
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DRAMA_DIR = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama')

DATA = {
    "_event.xlsx": {
        30: "\"...La spada...\", \"La mia spada...\"\nAh! Ah! Ah! Che lamenti patetici e commoventi!",
        31: "Semplici mortali,\nanzi, insignificanti insetti,\nle vostre lame serviranno in eterno la mia gloria!",
        42: "Dunque saresti tu l'arrogante stolto che osa levare la lama contro una divinità?",
        43: "Ho osservato ogni singolo istante, dall'inizio alla fine.\nLe grida strazianti delle anime liberate\nerano una melodia celestiale per le mie orecchie.",
        44: "E sia, miserabile verme, ti concederò quest'onore.\nDanza con questa lama!",
        52: "C-cosa?! Sconfitto da un branco di vermi mortali?!",
        53: "Ricorda bene le mie parole, mortale.\nTornerò un giorno a riprendermi quella lama!"
    },
    "_adv.xlsx": {
        6: "Fidanzamento",
        16: (
            "Nel #2 dell'Anno di Sierra #1, presso #3, #4 chiese la mano di #5.\n\n"
            "I due rimasero in silenzio, le mani dolcemente intrecciate, suggellando la loro promessa d'amore eterno."
        ),
        17: "Senza di te, la vita non ha alcun significato.",
        34: (
            "O stelle insonni, o luna dall'eterno peregrinare. In questa notte benedetta, vegliate sul cammino di queste due anime e consacrate questo giorno di letizia.\n\n"
            "Possa il bouquet offerto alla volta celeste e il bacio scambiato per il domani generare un tempo fulgido come l'oro.\n\n"
            "Mentre il chiarore lunare accarezza la terra, sotto un vincolo eterno, queste due vite si uniscono in una sola carne e un solo spirito."
        ),
        36: (
            "#pc_full.\n\n"
            "Giuri tu di prendere #tg come fedele compagno per tutta la vita, di non sciogliere mai la stretta della sua mano nei mattini di gioia come nelle notti di lacrime, e di dimorare al suo fianco per l'eternità?"
        ),
        37: "Lo giuro.",
        38: "Non posso farlo.",
        42: "...",
        51: (
            "#tg.\n\n"
            "Giuri tu di prendere #pc_full come tuo solo e unico compagno, di affidargli il tuo cuore nelle tempeste del fato come nella quiete del riposo, e di camminare per sempre insieme lungo il sentiero della vita?"
        ),
        53: "...Sì, lo giuro con tutto il cuore.",
        55: (
            "Dinanzi al sacro coro delle stelle, voi due siete ora uniti come una cosa sola. Possa la dea della fortuna posare il suo sguardo benevolo su di voi!\n\n"
            "E adesso... suggellate il voto con un bacio."
        ),
        56: "(Bacia #tg_him)",
        57: "(Fai l'amore con #tg_him)",
        58: "(Arrossisci e rimani in silenzio)",
        59: "(Fuggi via in preda al panico)",
        62: "(#tg sorride con timidezza e posa dolcemente le sue labbra sulle tue.)",
        66: "(#tg lascia sfuggire una risatina sommessa e unisce con tenerezza le sue labbra alle tue.)",
        85: "...Cosa?!"
    },
    "tyche.xlsx": {
        8: "Andare a caccia di androidi è uno spasso incredibile!",
        9: "Hai qualche incarico per me?",
        10: "L'incarico è compiuto.",
        16: (
            "Ehi, tu laggiù!\n\n"
            "Ho scovato un lavoro assolutamente sensazionale! Potresti diventare il salvatore dell'intera umanità!☆"
        ),
        17: "Accetto l'incarico. (Livello di Pericolo: 38)",
        18: "Magari un'altra volta.",
        26: (
            "Ottima scelta♡ Non te ne pentirai affatto!\n\n"
            "Oh, giusto, non mi sono ancora presentata! Puoi chiamarmi Tyche☆\n\n"
            "E questo qui al mio fianco è il mio fido socio, VISHNU."
        ),
        27: "...PIACERE DI CONOSCERTI.",
        29: (
            "Dunque, ascoltami con attenzione. Hai mai assaggiato un piatto di curry in vita tua?☆\n\n"
            "È una pietanza talmente squisita e travolgente che, una volta provata, non puoi più farne a meno! Abbiamo girato in lungo e in largo per il mondo alla ricerca di ogni singola ricetta di curry.\n\n"
            "Ma la delizia servita qui da 'Draghi & Spezie' mi ha fatto letteralmente perdere la testa!"
        ),
        30: (
            "La carne, le verdure, il dosaggio perfetto delle spezie... era tutto di un altro pianeta! C'è sotto qualcosa di paranormale, lo percepisci anche tu, vero?\n\n"
            "Se riuscissimo a scoprire il segreto di quel sapore, la civiltà umana farebbe un balzo evolutivo epocale! O forse no... ma hai capito cosa intendo, vero? Eh?♡\n\n"
            "Non dirmi che non muori dalla voglia di investigare!♡"
        ),
        31: (
            "Tanto per cominciare, chi mai aprirebbe una locanda in un posto sperduto come questo?\n\n"
            "E poi quelle rovine lì accanto... non ti sembra che odorino di mistero? Secondo me nelle profondità si nasconde un ingrediente leggendario!\n\n"
            "Non sembra troppo pericoloso, ma un androide arrugginito e una fanciulla delicata come me non possono farcela da soli... quindi ci darai una mano, vero? Collaborerai con noi, sì? Dì di sì!♡"
        ),
        32: (
            "Aaaah, che sollievo avere a che fare con un avventuriero così perspicace!♡\n\n"
            "Allora noi ti aspetteremo qui fuori mentre tu esplori i meandri delle rovine sotterranee☆"
        ),
        33: "...BUONA FORTUNA.",
        37: "Oh? Dici davvero?",
        42: (
            "Sei tornato tutto intero!☆\n\n"
            "Mi era sembrato di sentire la terra tremare poco fa... ma aspetta, COSA?! C'era una fabbrica sotterranea gestita da macchine pensanti e ti ha assalito un robot gigante?!"
        ),
        43: (
            "Ora capisco ogni cosa...\n\n"
            "Doveva trattarsi di una coltivazione automatizzata dell'era di Eyth Terre. Anche dopo la scomparsa degli umani, i congegni hanno continuato a produrre cibo per secoli senza mai fermarsi.\n\n"
            "E il cuoco del locale utilizzava quegli ingredienti antichissimi per sfornare il suo curry leggendario!"
        ),
        44: "...ORA È TUTTO DISTRUTTO. UNA VERA TRAGEDIA.",
        45: (
            "B-be', non fa niente! Un omaccione robusto come quel cuoco troverà il modo di tirare avanti anche senza la serra sotterranea☆\n\n"
            "Ascoltami bene, #pc: se vuoi fare l'avventuriero, ricorda sempre una cosa: non tutte le avventure si concludono con il lieto fine!"
        ),
        47: (
            "Tieni, prendi questo seme speciale, ti tirerà su il morale♡\n\n"
            "Vedila in questo modo: a quelle povere macchine, condannate a lavorare all'infinito pur avendo perso il loro scopo... noi abbiamo finalmente donato l'eterno riposo!\n\n"
            "E adesso ce la svigniamo prima che qualcuno ci chieda spiegazioni☆\n\n"
            "Ah, se dovessi finire i semi, il padrone del locale potrebbe averne ancora da venderti!"
        ),
        48: "...ADDIO. È STATO UN PIACERE."
    },
    "fairy_nanasu.xlsx": {
        8: "Sono Nanasu, la fatina delle melanzane~!",
        9: "C'è qualcosa che ti preoccupa?",
        10: "Ecco la tua Borsa Conservante.",
        19: (
            "Oh? Ma tu sei un avventuriero, vero? Eheheh, tempismo perfetto! Avrei un piccolo favore da chiederti... vorresti ascoltarmi?~\n\n"
            "Tra i viandanti che visitano Specwing gira una voce incredibile. Si dice che in un certo Nefia sia celato un tesoro oltre ogni immaginazione! Pare sia una borsa magica capace di rendere leggerissimo qualsiasi oggetto ci infili dentro!"
        ),
        20: (
            "Vedi, io non sono molto forte... Il mio zaino finisce sempre per essere troppo pesante, e a volte mi viene da piangere a metà strada. Ma con quella borsa potrei viaggiare molto più lontano! Potrei incontrare tantissima gente e ogni avventura diventerebbe uno spasso!"
        ),
        21: (
            "Però... ecco... la 'Foresta Senza Ritorno' è un posto troppo spaventoso per andarci tutto solo. Quindi, caro avventuriero... verresti con me?~\n\n"
            "Ho la sensazione che con te andrà tutto a gonfie vele! Sei forte, affidabile e... so che un'avventura insieme a te sarà emozionante!\n\n"
            "E non temere, ti ricompenserò a dovere! Che ne dici di rarissimi semi di alberi introvabili nelle terre umane?~"
        ),
        23: "Accetto la proposta. (Livello di Pericolo: 20)",
        24: "Magari un'altra volta.",
        28: "Oh, capisco... be', se dovessi cambiare idea, torna pure a parlarmi, d'accordo?~",
        34: (
            "Dici sul serio?! Evviva! Grazie infinite! Prepariamoci subito e partiamo alla volta del Nefia. La Foresta Senza Ritorno si trova a nord-ovest da qui.\n\n"
            "Spero solo che Raina e Poina non ci abbiano già battuto sul tempo... E-eh? No, niente! Non badare a me!~"
        ),
        41: (
            "Waaah, ce l'abbiamo fatta! Guarda, avventuriero, esiste davvero! La Borsa Conservante!\n\n"
            "Raina e Poina facevano davvero sul serio questa volta... da solo non ce l'avrei mai fatta. Grazie di cuore, davvero, grazie mille!~"
        ),
        43: (
            "Ed ecco la tua ricompensa pattuita! Semi di alberi rari che gli umani non troveranno mai nelle loro terre! E ci ho aggiunto un bel carico di melanzane fresche come regalo personale da parte mia!~\n\n"
            "Spero che potremo viaggiare di nuovo insieme un giorno. E quando accadrà... riempiremo questa borsa fino all'orlo di melanzane e faremo una festa epica, intesi?~"
        ),
        48: "Uh? Che strano... sento le ali formicolare... come se ci fosse elettricità nell'aria...",
        49: (
            "Ma guarda chi si rivede! Ci hai messo un secolo, Nanasu! Sei sempre la solita lumaca lenta, lentissima!\n\n"
            "Sei venuto a cercare la 'borsa misteriosa', vero? Eheheh, troppo tardi! Guarda qui! L'ho già presa io!"
        ),
        50: "Raina?! Che cosa ci fai qui?! Quella è la borsa che stavo cercando io... ridammela subito!~",
        51: (
            "Ridartela? Ma manco per sogno! No, no e poi NO! Nei Nefia i tesori appartengono a chi arriva per primo! Se la vuoi così tanto, perché non provi a strapparmela con la forza? Non è per questo che ti sei portato dietro quegli amiconi dall'aria tosta?"
        ),
        52: (
            "Oh, salute a te, piacere di fare la tua conoscenza, avventuriero! Io sono Raina, la fata del fulmine! Sta' in guardia: potresti finire tutto carbonizzato e scosso dalle scosse se osi toccarmi!"
        ),
        53: "...Che baccano insopportabile. Per colpa della tua boccaccia, Raina, abbiamo sprecato l'effetto sorpresa.",
        54: "Ma dai, Poina! Farli fuori senza neanche scambiare due parole sarebbe stato di una noia mortale! Dov'è il divertimento?",
        55: (
            "Non trovi anche tu, Nanasu? A dire il vero di questa borsa non me ne importa un fico secco! Ciò che volevo davvero... era godermi la tua faccia disperata! Guardare il piagnucolone Nanasu che supplica 'ti preeego smettila~' è la cosa più esilarante del mondo! Dunque... ridartela? MAI! Se la rivuoi, battiti con me! Fatti sotto, avanti: vediamo cosa sai fare prima che ti trasformi in una melanzana arrosto ben croccante a suon di fulmini!"
        ),
        56: "Idiota... Gioca pure quanto ti pare, Raina. Ma se ti metti tra i piedi, farò a pezzi anche te.",
        57: "Uuuh! Poina fa paura come al solito! Ma ehi, la faccenda si fa interessante! Allora, che ne dici, avventuriero? Vuoi fare una bella partita con noi?"
    },
    "_chara.xlsx": {
        13: "$sup",
        25: "(Parli tra te e te)",
        30: "$sup",
        37: "$rumor",
        39: "Unisciti a noi! (#2)",
        40: "Unisciti a noi! #1",
        41: "Ti prego di andartene.",
        45: "$hired",
        49: "$hired",
        61: "Chiamerò subito #1.",
        66: "(#self sta dormendo)",
        70: "Aiutatemi!",
        74: "(#self fissa il vuoto con sguardo perplesso)",
        79: "Mi arrendo! Te la cavi alla grande.",
        80: "Accetta questo dono in ricordo della tua vittoria.",
        85: "Finisce qui, smidollato.",
        91: "Non mi aspettavo che saresti tornato vivo! Avanti, ritira la ricompensa promessa.",
        95: "Sapevo che l'incarico era troppo gravoso per te. Che delusione.",
        100: "Scortami sano e salvo fino a destinazione.",
        104: "(#self è su di giri per la festa!)",
        108: "(#self solleva il calice per brindare a voi due!)",
        111: "(#self ti rivolge un sorriso radioso.)",
        114: "(Mette il muso imbronciato.)",
        117: "...Amore mio. (arrossisce)",
        121: "Consegnami #1, o la tua vita finisce qui!",
        123: "Fatti sotto, se ne hai il coraggio.",
        124: "Mi arrendo. (Perdi: #2)",
        135: "Una scelta saggia.",
        141: "Vorrei che tu tenessi questo.",
        145: "Ho preparato questo piatto con le mie mani... ti andrebbe di assaggiarlo?"
    },
    "melilith.xlsx": {
        14: "Tu... ti sei perso? Oppure sei venuto fin quaggiù per giocare?",
        20: "Oh, cosa c'è che non va... #brother2?",
        28: "Tu... ti sei perso? Oppure sei venuto fin quaggiù per giocare?",
        29: (
            "Benvenuto nella mia dimora! È un po' vecchia e disordinata, ma ti prego di fare come se fossi a casa tua. Il mio nome è Melilith. Suona proprio come il nome di una principessa, non trovi?\n\n"
            "Non ricevo molte visite da queste parti. C'è persino chi la chiama la magione maledetta... Dimmi, ti andrebbe di giocare un po' con me?"
        ),
        30: "Sì, volentieri.",
        31: "No, grazie.",
        34: "Capisco... sì, è naturale. Chi mai vorrebbe giocare in una tetra villa in rovina...",
        39: "Davvero?!... Che gioia immensa!",
        40: (
            "A dire il vero, giocare di tanto in tanto con i rari visitatori che passano di qui è il mio unico conforto. A cosa vorresti giocare? A nascondino? Ad acchiapparella? ...Ah, aspetta! Dato che sembri un vero avventuriero, facciamo una caccia al tesoro!"
        ),
        41: (
            "Moltissimo tempo fa ho radunato un'infinità di tesori preziosi nei sotterranei di questa magione. Tra di essi c'è persino una verga incantata capace di esaudire qualunque desiderio! Quindi, avrei una richiesta da farti... andresti a cercare il tesoro per me?"
        ),
        42: "Sì, lo farò.",
        43: "No, non mi interessa.",
        48: "Davvero?!... Oh, che meraviglia splendida!",
        49: (
            "Potrai tenere qualunque tesoro riuscirai a scovare, ma ad una sola condizione: potrai prenderne soltanto 'uno'. Fai molta attenzione! Prendi sempre e solo 'un' tesoro. Se dovessi prenderne di più, ti attende una maledizione terrificante!\n\n"
            "E adesso prepariamoci subito! Eheh, sono trascorsi secoli dall'ultima volta che ho organizzato una caccia al tesoro... non sto più nella pelle! Devo invitare tantissimi amici per darti il benvenuto! Non hai paura dei non morti, vero?"
        ),
        53: "Ebbene, il gioco sta per cominciare... Quando sarai pronto, scendi le scale verso il seminterrato. Fa' attenzione, intrepido avventuriero!",
        56: "Chissà come procede la caccia al tesoro?... Confido che saprai donarci un magnifico grido di terrore!",
        66: "Bentornato! I nostri allegri passatempi sono giunti al termine. Addio, prode viandante. Spero che tu possa vivere felice con il tesoro che hai scelto di portare con te.",
        74: "...Uh? Che cos'è quel foglietto di carta sporco e sgualcito che hai in mano?",
        75: (
            "Un 'Buono per fare amicizia con Melilith'...? No, l'avevo fabbricato centinaia di anni fa, ma nessuno lo aveva mai scelto. Me ne ero completamente dimenticata... Ma... hai davvero rinunciato a tutti gli altri tesori per questo?"
        ),
        76: "Sì, l'ho fatto per questo.",
        77: "No, ho sbagliato.",
        80: "Bugiardo...",
        82: "Capisco... è ovvio. Immaginavi che ci fosse qualche valore nascosto in quel pezzetto di carta, non è così?... Spero che tu sia maledetto!",
        90: "...Eh?",
        91: "Hai rinunciato a tutti i tesori per un misero ritaglio di carta sgualcita?",
        92: (
            "...All'inizio la caccia al tesoro non doveva essere così crudele e spaventosa. Credevo che prima o poi qualcuno avrebbe riportato su questo biglietto e mi avrebbe sorriso..."
        ),
        93: "Ma tutti sceglievano sempre i tesori luccicanti e fuggivano via da questa magione... e così io...",
        94: "...",
        95: (
            "Dimmi... che espressione dovrei fare in un momento simile? Ormai riesco a malapena a ricordare come ci si sentisse quando ero viva... anzi, persino quand'ero viva..."
        ),
        96: "...",
        97: "Grazie di cuore... mio primo, vero amico."
    },
    "elder_exile.xlsx": {
        8: (
            "Un #race che oltrepassa la barriera e mette piede in questo villaggio...?\n\n"
            "Dunque dev'essere opera di quel giovanotto. Khe keh keh... Già, il bracciale non gli serve più a nulla. Persino il nostro signore Itzpalt lo ha rinnegato.\n\n"
            "Benché questo villaggio sia lontano dai tumulti del mondo mortale, i fastidi non mancano mai. Se accetti di renderti utile ai nostri scopi, potremmo anche chiudere un occhio sulla tua intrusione."
        ),
        12: "Parlami di Issizzle.",
        13: "Cosa sai sul conto di Issizzle?",
        14: "Ho trovato Duponne, ma...",
        15: "Riguardo al Grande Corno di Minotauro...",
        16: "Ho riportato indietro Duponne.",
        17: "Ho abbattuto Duponne.",
        18: "Duponne è svanita per sempre.",
        28: (
            "L'oscura aberrazione, Issizzle. Khe keh keh... Chi mai in questo villaggio potrebbe ignorare quel nome?\n\n"
            "Prima di degradare la propria anima fondendosi con carni impure, era celebrato come il mago più vicino agli dèi.\n\n"
            "Un nemico temibile, non c'è che dire. Neppure tra noi vi è alcuno abbastanza potente da opporsi a lui. E se anche esistesse, non si abbasserebbe certo a curarsi delle beghe del mondo mortale. Un esule, dopotutto, è vincolato unicamente alla propria espiazione."
        ),
        29: (
            "Khe keh keh... Eppure attendi, avventuriero. C'è un compito che calza a pennello per uno come te. Se avrai successo, ti donerò una conoscenza proibita: un'antica formula tramandata dai tempi remoti. Un'arte segreta per forgiare una lama capace di ferire persino Issizzle."
        ),
        30: (
            "Khe keh keh... Da dove iniziare?\n\n"
            "Conosci il santuario di Lurie, a sud-est di questo villaggio? Quando gli dèi abbandonarono questo mondo, il tempio sprofondò negli abissi marini. Laggiù vivevo un tempo, nei giorni in cui ero ancora un mortale.\n\n"
            "Un piccolo cucciolo di leone marino si smarrì tra quelle navate allagate. Si affezionò a me, già. Si chiamava Duponne. Una creatura sciocca e insaziabile... khe keh keh... eppure mi affezionai morbosamente a quella bestia lenta e affettuosa."
        ),
        31: (
            "Poi venne la mia morte e, per i peccati commessi in vita, fui condannato a un'espiazione senza fine in questo villaggio d'esuli. Accadde migliaia di anni fa.\n\n"
            "Le ere sono scorse come sabbia tra le dita. Eppure, per quanto sembri inconcepibile... io lo sento ancora! Sento la presenza vitale di Duponne, ancora viva!\n\n"
            "Khe keh keh... Odo chiaramente il lamento addolorato di quella creatura, dimenticata nelle profondità degli abissi marini."
        ),
        32: (
            "Ti chiedo di riportare Duponne indietro dalla sua prigione tra i flutti.\n\n"
            "Che sia rimasta il leone marino di un tempo o sia mutata in una qualche orrenda aberrazione, non saprei dirti. Se non può essere salvata, concedi a quella povera creatura l'eterno riposo. Questo è il mio volere."
        ),
        33: "Khe keh keh... Sempre la solita sciocca creatura. Avere il potere di vivere per millenni e restarsene rintanata in simili rovine... khe keh keh...",
        41: (
            "Duponne... tramutata in un colossale drago...?!\n\n"
            "Che cosa bizzarra... la rammentavo come un semplice cucciolo ingordo. Ma i ricordi dei mortali svaniscono in fretta.\n\n"
            "In ogni caso, con una mole simile non potresti mai trascinarla fin quassù a forza."
        ),
        50: (
            "Se utilizzassi l'antico artefatto noto come Sfera del Drago, forse riusciresti a vincolare Duponne.\n\n"
            "Ma... khe keh keh... gli ingredienti per forgiare un simile arnese scarseggiano in questo villaggio. Serve un componente assai raro chiamato Grande Corno di Minotauro.\n\n"
            "...Se la memoria non mi inganna, una mandria di minotauri nidificava a sud di Yowyn, khe keh keh..."
        ),
        56: (
            "Ah! Sei in possesso del Grande Corno di Minotauro!\n\n"
            "Con questo materiale potrò forgiare la sfera per condurre Duponne fino a noi.\n\n"
            "...Come si usa? Un avventuriero del tuo calibro non ha certo bisogno di lezioni. Khe keh keh... ti basterà impugnarla e scagliarla contro la belva!"
        ),
        66: (
            "Duponne... capisco. Se tale è stato il tuo giudizio, non aggiungerò parola.\n\n"
            "Cosa mai l'abbia trattenuta tra i ruderi sommersi per incalcolabili millenni... no, cercare una risposta adesso sarebbe pura follia. Khe keh keh..."
        ),
        67: "Khe keh keh...",
        68: "...",
        70: (
            "...Non temere. Manterrò la parola data.\n\n"
            "Ti consegnerò la formula dell'antica stregoneria: la Forgiatura delle Rune, un sapere da lungo tempo perduto tra gli umani. Nel tuo scontro contro Issizzle, ti sarà senz'altro di prezioso ausilio."
        ),
        71: "Il nostro patto è suggellato. E adesso va' per la tua strada, avventuriero. Khe keh keh...",
        78: "...Duponne! Sei davvero tu?!",
        80: "GROOOOAAARRRR!!!",
        81: "Ah, che ruggito terrificante! Intendi forse divorarmi?\n\nKhe keh keh... Già, immagino che tu non possa più ricordarti di me.",
        83: "GROOOOAAAOOOONNNNN!!!",
        84: "...Eri un drago fin dal principio, dunque.\n\nEppure, vederti ancora in vita mi basta. Di questa mia vecchia carcassa rinsecchita non mi importa nulla. Fa' pure di me ciò che vuoi.",
        87: "GRRRRUUUUMMM... CHIIII...",
        88: "Duponne...?",
        89: "CHIIII... CHIIII...",
        90: (
            "Ma come, Duponne... è mai possibile che tu mi riconosca?!\n\n"
            "Ah...! Quel nastro attorno al tuo collo! È lo stesso che ti legai per gioco tantissimo tempo fa, quando ero ancora un semplice mortale...\n\n"
            "E lo hai custodito con tanta cura per tutti questi secoli...?"
        ),
        95: "CHIIII... GNAUUU...",
        96: (
            "Duponne... allora è così... era davvero così, khe keh keh...\n\n"
            "Ti ho abbandonata negli abissi oceanici per imprigionarmi in un'eterna espiazione. Eppure, dopo migliaia di anni, tu non mi hai mai dimenticato..."
        ),
        97: "GNAUUU...",
        98: "Perdonami, Duponne... perdona questa mia povera anima sciocca.",
        100: "CHIIII... WOOOONNN...!",
        101: "Oh, Duponne mia...!",
        102: "...",
        103: "...",
        105: (
            "...Khe keh keh, non temere. Non ho dimenticato la promessa fatta.\n\n"
            "Ti dono la formula dell'antica arte: la Forgiatura delle Rune, una conoscenza da millenni preclusa ai mortali. Nella tua battaglia contro Issizzle, si rivelerà di inestimabile valore."
        ),
        107: (
            "Ed ora, Duponne cara, dobbiamo presentarti a tutta la gente del villaggio!\n\n"
            "Khe keh keh... non spaventarti: hanno volti cupi e sinistri, ma non ti faranno alcun male. Sono certo che diventerai la beniamina di tutti.\n\n"
            "Vieni, Duponne, vieni qui vicino a me. Vivremo di nuovo insieme... proprio come nei bei giorni al tempio di Lurie. Khe keh keh..."
        ),
        113: (
            "Quando Issizzle calcava ancora la terra come mortale, re e condottieri si prostravano ai suoi piedi per implorare il suo aiuto. Khe keh keh... Con il potere arcano che possedeva, sottomettere i regni del mondo sarebbe stato un gioco da ragazzi.\n\n"
            "Eppure ancora oggi dimora nel suo maniero in rovina, perso nell'eterno studio delle pietre magiche. Perché ai suoi occhi, le corone e la gloria dei mortali non sono altro che polvere al vento.\n\n"
            "Non dimenticarlo mai: colui che intendi affrontare dimora in una sfera ben al di sopra delle meschine contese terrene. La tua mano si trova ora sulla soglia stessa del mito. Khe keh keh..."
        )
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
    print(f"Total rows updated across 7 files: {total_updated}")

if __name__ == "__main__":
    run()
