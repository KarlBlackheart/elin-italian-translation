"""
Translate guide and lore books in Lang/IT/Text/Book/ to Italian:
- welcome.txt
- manual_home.txt
- cave_note.txt
- crimberry.txt
- herbs.txt
- guide_cook.txt
- guide_faith.txt
- guide_fish.txt
- guide_magic.txt
- guide_quest.txt
- guide_ranch.txt
"""
import os

BOOK_DIR = 'Lang/IT/Text/Book'

BOOKS = {
    'welcome.txt': """Benvenuto,Uno strano avventuriero
{center}
Benvenuto, avventuriero, nel vasto mondo di Ylva!

Puoi accedere alla "Guida" in qualsiasi momento dal menu di sistema o premendo il tasto "?".

Il nostro mondo è scosso da tumulti e le cicatrici della guerra oscurano ancora le terre in cui muoverai i tuoi primi passi.
La vita per un viandante è aspra e insidiosa, ma lungo il cammino incontrerai anime gentili pronte a guidarti e sostenerti.

Possa il vento misericordioso accompagnare sempre i tuoi passi.
""",

    'manual_home.txt': """Manuale di Sviluppo della Tenuta
Ti insegnerò tutto ciò che serve per fondare e far prosperare un insediamento fiorente.
""",

    'cave_note.txt': """Appunto Sbiadito,,0
{center}

[Il testo antico è cancellato in più punti]

...lasciando la foresta... verso il mondo esterno...

...questa caverna... noi...

Un emissario dei Torres... umani ed Elea...

...verso Mysilia...

...è giunto il momento... per noi di partire... questo luogo rimarrà...

...a chiunque visiterà questo rifugio... per caso... o forse per disegno del destino...

Possa il... vento...
""",

    'crimberry.txt': """La Dipendenza da Bacche Crim e Tu

Ogni anno sempre più persone cadono vittime della dipendenza dalle apparentemente innocue Bacche Crim.

Conosciute nell'antico dialetto nefiano come Kur-amu-beri — a riprova della loro lunga e torbida storia nelle nostre terre — le Bacche Crim sono un potente allucinogeno dai molteplici utilizzi.

Il semplice consumo di una bacca può scatenare i seguenti sintomi entro 15-60 minuti:

- Allucinazioni visive e uditive
- Alterazione psicomotoria simile a grave ebbrezza
- Deliri sconnessi
- Perdita del controllo motorio ed episodi febbrili.
{p}
Le Bacche Crim creano un'assuefazione devastante: se il tossicodipendente non riceve la sua dose quotidiana di "Crim", ripiegherà su altri narcotici o diverrà una minaccia pubblica per l'intera comunità.

E naturalmente nessuno pensa ai poveri fanciulli coinvolti in queste pratiche da "adulti". I giovani hanno persino inventato un nuovo modo per "gustare" questi frutti diabolici:

Imitando gli yeek selvatici, essiccano le bacche e se le infilano direttamente nelle narici. Questo "sniffare" Bacche Crim provoca attacchi d'aggressività incontrollata e spinge individui disperati a improvvisarsi "avventurieri", compiendo gesta sconsiderate pur di procurarsi la dose successiva.
{p}
Mentre alcuni vecchi maghi dai capelli lunghi pretendono che le Bacche Crim restino legali per i loro presunti "rituali sacri", questa follia deve cessare una volta per tutte!
""",

    'herbs.txt': """Erbe Benedette,Dott. Schmidt

<b>Curaria</b> [KYURARIA AQUIFOLIUM]
I suoi effetti terapeutici sono ampiamente documentati. Tuttavia, la reale efficacia curativa dipende strettamente dal suo stato di "consacrazione", clinicamente testato come un autentico principio attivo e non come un mero placebo.

Proprietà: Rigenerante Vitale

<b>Morgia</b> [MOJIA DIPSACUS PILOSUS]
Potente stimolante ormonale. Accresce la massa muscolare, la forza fisica e la costituzione. I soggetti sottoposti a test in doppio cieco hanno ricevuto erbe con diversi gradi di consacrazione, ottenendo riscontri differenti. Ciò dimostra inconfutabilmente l'esistenza degli Dei, dinanzi alla cui potenza ogni nostra scienza impallidisce.

Proprietà: Potenziamento di Forza e Costituzione
{p}
<b>Mareilon</b> [MAREIRON DIPSACUS FEROX]
Stimolante neurochimico d'eccezione. Accresce le facoltà cognitive e l'intelletto. Il grado d'efficacia dipende interamente dalla benedizione ricevuta.

Proprietà: Potenziamento Mentale e Cognitivo

<b>Erbaspense</b> [SUPENSUUIDO LONGIFOLIA]
L'esatto spettro dei suoi principi attivi resta parzialmente sconosciuto, ma chi la assume manifesta riflessi fulminei e una sensibilità percettiva straordinaria. Ulteriori sperimentazioni sono necessarie per catalogarne ogni effetto collaterale.

Proprietà: Amplificazione della Percezione

<b>Alraunia</b> [ARURONIA MARTYNIA LUTEA]
Attivazione ormonale. Potentissimo afrodisiaco naturale, popolarissimo tra gli abitanti del luogo. Curiosamente sembra stimolare anche le facoltà mnemoniche. Le ricerche sono in attesa di ulteriori sovvenzioni universitarie.

Proprietà: Stimolazione della Memoria e del Desiderio

{p}
<b>Stomafilla</b> [SUTOMAFIRIA HYPOGAEA]
A contatto con i succhi gastrici, questa pianta si espande a dismisura riempiendo l'intera cavità stomacale e inducendo un immediato senso di profonda sazietà. L'apporto nutrizionale sul lungo periodo resta ancora da verificare.

Proprietà: Estremamente Saziante

Man mano che nuovi campioni botanici perverranno ai nostri laboratori, provvederemo ad aggiornare questo compendio.

Con ossequio,

<i>Dott. Schmidt
	Philosophiae Doctor Magus</i>
""",

    'guide_cook.txt': """Tutti Possono Cucinare!,Lo Chef d'Acciaio

Hai mai ammirato i piatti nei ristoranti di lusso pensando: "Vorrei poter mangiare così ogni santo giorno"?

Ebbene, puoi farlo... se impari a cucinare da te!

<b>Gli Utensili Fondamentali</b>

Innanzitutto ti serve un posto dove cucinare. Falò e paioli vanno bene per pasti frugali, ma per impiattare da veri professionisti avrai bisogno di una cucina attrezzata.

{p}

Uno chef che si rispetti dovrebbe possedere:

* Tagliere da cucina
* Tavolo da barbecue
* Calderone
* Fornello
* Frullatore
* Forno
* Microonde

I seguenti macchinari sono preziosissimi per la preparazione delle basi:

* Macina a pietra
* Scaffale di stagionatura
* Macchina da caffè espresso

Consiglio d'oro: tieni sempre a portata di mano un annaffiatoio pieno, per spegnere le fiamme nel caso tentassi ricette troppo difficili scatenando un incendio!

{p}
<b>Le Ricette</b>

Ora devi imparare l'arte culinaria. Purtroppo i grandi cuochi custodiscono le ricette con la stessa gelosia con cui i draghi difendono i loro tesori: la concorrenza è spietata, perciò dovrai farti venire le idee da solo. Cucinando spesso avrai intuizioni per piatti simili, oppure potrai sempre smantellare il piatto forte di un rivale con un martello per carpirne gli ingredienti!

Ovviamente ciò presuppone che la tua abilità in Cucina sia sufficiente per comprendere la preparazione. Sei ancora a secco d'idee? Cerca i Santuari della Ruota, noti per infondere illuminazioni creative.

<b>Ingredienti e Preparazione</b>

I grandi piatti nascono da grandi ingredienti: raccolti e pesci di qualità superiore ottenuti da contadini e pescatori veterani, carni marezzate di mostri rari, condimenti caserecci e molto altro.
{p}
Nello scegliere gli ingredienti, presta attenzione alla qualità e ai tratti: basta un solo ingrediente di qualità eccelsa per elevare il piatto, e tutti i tratti degli ingredienti si sommano durante la cottura.

Sei ciò che mangi, perciò pianifica i pasti in base al tuo stile di vita. I guerrieri prediligono cibi ricchi e grassi per accrescere la forza, mentre i maghi adorano dessert dolci e speziati per potenziare l'energia arcana.

Ora tocca alla preparazione. I cuochi novelli dovrebbero iniziare con piatti semplici, osando ricette complesse solo con il crescere dell'esperienza: un principiante non sfornerà mai un banchetto stellato, non importa quanti sforzi faccia. Più perfezioni abilità e ricette, più renderanno i tuoi ingredienti: con la giusta pratica, sfornerai capolavori culinari capaci di oscurare i bistrot più rinomati di Palmia!

{p}
<b>L'Arte della Tavola</b>

A proposito di ristoranti di classe: l'esperienza culinaria non finisce quando il piatto è pronto. Quei raffinati bistrot sanno bene che un'atmosfera conviviale esalta ogni sapore: puoi fare lo stesso allestendo una sala da pranzo con l'apposita insegna. Inoltre il cibo è infinitamente più delizioso a stomaco vuoto: l'appetito è il miglior condimento.

Servi porzioni ragionevoli e cerca di non strafogarti. Credimi, non c'è nulla di più amaro che dover gettare via mezzo piatto nutriente e squisito solo perché non riesci a mandar giù un boccone in più.

<i>Buon appetito!</i>
""",

    'guide_faith.txt': """Vita Devozionale,Madre Superiora

Avvicinatevi, gattini smarriti: vi condurrò verso la luce. Oggi è l'ultimo giorno del vostro catechismo, dopodiché voi giovani sarete grandi abbastanza per consacrarvi a una divinità. Poiché questa decisione influenzerà il resto della vostra esistenza, ripasseremo tutto ciò che abbiamo appreso in questa lezione conclusiva.

<b>I Pilastri Divini e Voi</b>

Venerare una divinità significa riservarle un posto speciale nel proprio cuore. Attraverso il vincolo della fede riceverete benedizioni celesti e consentirete al vostro dio di agire attraverso le vostre opere.
{p}
Per iniziare, meditate sul vostro futuro e scegliete una divinità le cui grazie rispecchino le vostre aspirazioni:

* Studiosi, maghi: Itzpalt degli Elementi
* Contadini, tessitori: Kumiromi del Raccolto
* Cacciatori, allevatori: Lulwy del Vento
* Guerrieri, fabbri: Opatos della Terra

Vi sono innumerevoli motivi per adorare un determinato dio, ma considerazioni pratiche e inclinazioni personali devono sempre essere bilanciate con saggezza.

Fatta la vostra scelta, dovrete raggiungere un altare consacrato al dio prescelto — i pellegrini viaggiano fino alle Terre della Tregua a nord di Palmia a tale scopo. Giunti dinanzi all'altare, potrete essere accolti nell'abbraccio divino.
{p}
<b>I Doveri del Fedele</b>

La semplice devozione consoliderà il vostro legame con il trascorrere dei giorni. Tuttavia, potete fare molto per coltivare attivamente un rapporto intimo con il divino:

* Pregate ogni giorno. È il dovere cardine di ogni credente: la preghiera quotidiana vi ritemprerà e approfondirà la vostra fede.

* Presentate offerte. Ogni divinità predilige tributi specifici: deponeteli con devozione sull'altare del vostro dio.

* Leggete le pergamene della fede. Questi rari manoscritti vi renderanno autentici fari di potere sacro.
{p}
La fede rappresenta il vostro potenziale spirituale, ma è una coppa vuota che spetta alle vostre azioni colmare. I Pilastri non necessitano materialmente dei nostri doni, ma l'atto del sacrificio e della devozione funge da canale mistico tra noi e loro. Ricordate sempre: fede <b>e</b> opere sono entrambe necessarie per accogliere la pienezza delle grazie divine.

{p}
<b>Gli Altari</b>

Oltre alla preghiera e al sacrificio, gli altari assolvono altre funzioni cruciali. Innanzitutto, è possibile offrire una fiala d'acqua pura per farla benedire dal proprio dio — attenzione: l'acqua comune non regge la santificazione. Inoltre, non deponete mai per errore l'acqua pura sull'altare di un'altra divinità, altrimenti verrà inesorabilmente maledetta!

Se vi imbattete nell'altare di un dio rivale, potete tentare di consacrarlo al vostro culto. Per farlo, preparate un'offerta imponente — più è pesante, meglio è — e sacrificatela sull'altare avverso. Migliore è il tributo, maggiori saranno le probabilità di successo: se il vostro dio reclamerà l'altare, il vostro sforzo sarà ricompensato immensamente. Se fallite, subirete la tremenda punizione divina.

Alcuni altari, come quelli protetti delle Terre della Tregua, sono inviolabili e non possono essere contesi.

{p}
<b>Cambiare Divinità</b>

Abbandonare il proprio dio non è una scelta da compiere alla leggera: il tradimento viene invariabilmente punito dall'ira celeste. Se siete irremovibili, trovate l'altare del nuovo nume e iniziate il culto come fatto in precedenza. Siate consapevoli che sarete gravati dal peso dei vostri peccati in proporzione a quanta fiducia il dio precedente aveva riposto in voi... e subire un'ulteriore punizione divina mentre si è già marchiati dalla censura celeste significa morte certa e ineluttabile.

La lezione è conclusa: pregate con fervore, vi è sempre speranza di salvezza. Domani avrà inizio il nostro pellegrinaggio verso le Terre della Tregua.
""",

    'guide_fish.txt': """Abboccato!,Il Re dei Pescatori

Dunque, ti interessa la pesca? Ottima idea, miao! Le terre di North Tyris pullulano di pesci d'ogni razza; nei quarant'anni in cui ho servito Lady Ehekatl non ho mai patito la fame nemmeno per un giorno.

<b>I Preparativi</b>

Per cominciare devi imparare le basi della pesca; puoi apprendere l'abilità nel borgo di Yowyn. Una volta compreso per bene come muoverti, avrai bisogno di lenza, canna ed esca, miao.

L'esca è semplicissima da preparare: sminuzza ossa, interiora e scarti di mostro fino a creare bocconi irresistibili per i pesci. Molti funghi che crescono a North Tyris hanno una consistenza carnosa e fungono da discreta esca se sei di stomaco delicato.

{p}
Riguardo alle canne da pesca: per i principianti andrà benissimo un ramo flessibile legato a una cordicella, ma un professionista esige ben altro, miao! Una canna forgiata in materiali duri affatica molto meno durante le battute di pesca, quindi potenziala non appena ne hai l'occasione.

<b>I Luoghi di Pesca</b>

Puoi gettare la lenza ovunque a North Tyris: non esiste specchio d'acqua tanto sterile da non ospitare forme di vita. Tuttavia, per ottimizzare tempo ed esche conviene recarsi dove i pesci abbondano, e questo significa l'oceano, miao! Porto Kapul è il posto perfetto per iniziare: non ci sono mostri minacciosi e la locanda offre vitto e alloggio dopo una dura giornata di pesca. Dopodiché potrai vendere il pescato al mercato o spedirlo a casa tramite la cassa delle spedizioni.

Detto ciò, la città è troppo rumorosa. Se ne hai la possibilità, acquista un lotto sul lungomare per crearti una riserva di pesca tutta tua!

{p}
La ricompensa per tutta questa fatica è un pescato strabiliante: la probabilità di una pesca miracolosa, in cui Lady Ehekatl benedice la tua lenza riempiendola di tutti i pesci che può reggere, è dieci volte superiore sulle spiagge e nell'oceano rispetto a un modesto stagno! Risparmierai esche e tempo, e diventerai un maestro pescatore in un batter d'occhio, miao!

<b>Il Brivido della Cattura</b>

Una volta lanciata la lenza, il resto è nelle zampe di Lady Ehekatl. All'inizio tirerai su solo cianfrusaglie e pesciolini, ma col tempo pesci sempre più grossi e prelibati abboccheranno al tuo amo, miao. Negli anni ho pescato dall'acqua persino scrigni del tesoro sommersi!

Ah, quasi dimenticavo! Il pesce fresco va a male rapidissimamente: porta sempre con te una borsa frigo per conservare il pescato!

{p}
Talvolta abboccherà una preda così colossale da risultare intrasportabile: è in quei momenti che consiglio di avere un tagliere con sé. Con un buon coltello potrai sfilettare uno squalo o una balena direttamente a riva senza rischiare di finire schiacciato dal peso, miao.

<b>E Dopo la Pesca?</b>

Ora che hai il tuo pesce, che cosa ne fai?

Se adori Lady Ehekatl come me, i commercianti d'esportazione ti pagheranno il cinquanta percento in più per il pesce fresco: un affare d'oro, miao! I giovani d'oggi vanno matti per il "vino aromatizzato al bonito"... sembra quasi un sacrilegio verso i doni di Lady Ehekatl, ma la gente paga profumatamente per assaporare il sapore del mare.

{p}
Se vuoi il mio modesto parere: mangiati il pesce! Con quarant'anni d'esperienza alle spalle, i miei piatti a base di pesce sono leggendari: sashimi con salsa di soia, tranci marinati o bonito essiccato, sono tutti sublimi, miao! Il pesce giova enormemente alla destrezza e all'apprendimento, ma chiunque può deliziarsene!

Dunque va' e getta la lenza! Che la benedizione di Lady Ehekatl vegli sempre su di te, miao!
""",

    'guide_magic.txt': """Introduzione alla Magia

(Appunti di uno studente della Gilda dei Maghi)

Molto bene, ragazzi. Il maestro di gilda mi ha riferito che siete allievi pratici, perciò ho strutturato questa lezione introduttiva appositamente per voi. Niente noiose dissertazioni teoriche: so bene che fremete dalla voglia di sperimentare un po' di vera magia. Non siate timidi: la gilda ha disperato bisogno di incantatori operativi sul campo, e voi verrete addestrati per questo.

Oggi vi guiderò passo dopo passo nell'arte del lancio degli incantesimi.
{p}
<b>Apprendere gli Incantesimi</b>

La magia inizia con lo studio delle formule. Ora, decifrare tomi magici non è come sfogliare il Palmia Times: la vostra alfabetizzazione verrà messa a dura prova, e le conseguenze di una svista nella lettura delle rune arcane sono ben più severe di un errore di stampa scandalistico. Ho portato con me uno dei tomi più accessibili: dardo magico. Fatelo girare tra i banchi, desidero che ciascuno provi a leggerlo. Man mano che la vostra cultura crescerà, potrete cimentarvi con formule ben più complesse.

Fatto? Una volta memorizzate le rune, sarete pronti per scagliare il vostro primo incantesimo. Tenete a mente che lo sforzo mentale della magia brucerà gradualmente l'incantesimo dalla vostra memoria: non all'istante, ma se non rinfrescherete lo studio dei tomi, finirete per dimenticare le formule per intero.
{p}
È ciò che noi maghi definiamo "scorte d'uso": quante volte possiamo invocare una magia prima che la formula sfumi dalla mente. La memorizzazione è un'abilità che si allena: più tomi magici studierete, maggiore sarà la vostra capacità di ritenere il sapere arcano, garantendovi più scorte a ogni sessione di lettura.

Il ciclo è elementare: leggi i tomi, accumuli scorte d'uso. Lanci incantesimi, consumi scorte. Persino dei novizi possono comprenderlo!

Prima che me lo chiediate: sì, i tomi magici costano un occhio della testa. Se avete esaurito le scorte, potreste attingere alla sorgente primordiale della magia durante il sonno, ricaricando un po' di scorte degli incantesimi basilari del vostro dominio. I maghi addestrati riescono a farlo persino con le scorte piene, ottenendo formule avanzate: questo talento è ritenuto indispensabile per qualunque incantatore e farà risparmiare un patrimonio di monete d'oro ai novizi.

Sì, la sorgente della magia assume la forma di un regale uomo dai capelli scarlatti. Nessun'altra domanda al riguardo, per cortesia.
{p}
<b>Scagliare Incantesimi</b>

Ora che avete appreso la formula, è tempo di canalizzarla. Tu laggiù in fondo! Fatti avanti e prova a scagliare un dardo magico contro il manichino d'addestramento.

...Oh, l'incantesimo è fallito. Non abbatterti: più ti eserciti, più diventerai abile. Oltre alla competenza generale nel lancio, utilizzare un incantesimo vi sintonizzerà con esso — ciò che chiamiamo "livello dell'incantesimo", che ne accresce la potenza e la probabilità di successo. Ogni magia è legata a un attributo: più questo è alto rispetto al livello della formula, più rapidamente guadagnerete livelli in quell'arte. Persino i lanci falliti fanno avanzare la competenza: la pratica rende perfetti.
{p}
L'arte magica si esprime al meglio liberi da impacci; i seguenti fattori penalizzeranno gravemente il vostro lancio:

* Corazze pesanti
* Scudi
* Combattere a due armi
* Cavalcare bestie
* Ospitare parassiti sul corpo

Armature pesanti e scudi impongono inoltre un tetto massimo alla percentuale di riuscita del lancio, sebbene esistano talenti specifici per azzerare tali svantaggi. Infine, stati alterati come stordimento o confusione comprometteranno pesantemente la vostra concentrazione.

Ricordate: con sufficiente dedizione e i giusti talenti potrete superare qualsiasi penalità d'incantamento. Inteso? Ora disponetevi in fila davanti ai manichini e alternatevi nel lanciare dardi magici fino all'esaurimento delle vostre scorte!
{p}
<b>I Punti Mana (PM)</b>

Tu laggiù! Sei pallido come un cencio, siediti e bevi questo tonico! Va meglio?

...Capisco, hai preteso troppo dalle tue forze. Oltre alle scorte mnemoniche, la magia attinge ai Punti Mana: lanciare incantesimi a mana esaurito provocherà laceranti danni da reazione arcana sul vostro corpo. Persino i principianti possono sopravvivere a un singolo sovrasforzo senza aver allenato la capacità magica, ma più il mana scende in negativo, più il contraccolpo sarà devastante.

Non abbiate timore di ricorrere al sovrasforzo se è questione di vita o di morte, ma rammentate che l'imprudenza può uccidervi con altrettanta rapidità.

{p}
Riepilogando la lezione odierna:

* Leggete tomi o sognate durante il sonno per accumulare scorte d'uso.
* Lanciate magie consumando scorte e Punti Mana.
* Equipaggiamento ingombrante, posture e stati alterati penalizzano il lancio.
* Gli incantesimi salgono di livello con l'uso, aumentando potenza e successo.
* Potete lanciare a mana zero, ma il contraccolpo danneggerà le vostre carni.

Confido che abbiate apprezzato questa introduzione alle arti arcane. La vostra classe terrà regolarmente queste sessioni pratiche, perciò preparatevi a dovere!
""",

    'guide_quest.txt': """Linee Guida per le Missioni,Il Consiglio di Tyris

A causa del vertiginoso incremento nel numero di avventurieri registrato negli ultimi anni, nonché delle frequenti controversie legali approdate nei nostri tribunali, i governi di Mysilia, Palmia e Mayroon hanno concordato la standardizzazione ufficiale delle richieste affisse sulle bacheche di tutta North Tyris.

Sebbene non sia formalmente vietato ingaggiare mercenari al di fuori di tali canali, sia il committente che l'avventuriero troveranno arduo ottenere tutela giuridica in caso di inadempimento o controversie contrattuali.

Le tipologie di richieste omologate sono le seguenti:

{p}
<b>Approvvigionamento</b>

L'avventuriero è tenuto a procurare l'articolo o gli articoli specificati. Si noti che la denominazione dell'oggetto deve coincidere rigorosamente con quella indicata nell'annuncio. Qualora sia richiesto un "utensile", dovrà essere consegnato un "utensile", non una "zappa" o un'"ascia".

Ove sia richiesta un'intera classe di articoli, l'annuncio recherà la dicitura "categoria" nell'angolo in basso a destra. Una richiesta per la categoria "pane" potrà essere soddisfatta consegnando un "panino imbottito" o una "focaccia".

Alla consegna verrà corrisposto un compenso aggiuntivo in oren proporzionale al valore stimato dell'oggetto.

{p}
<b>Esibizione Artistica</b>

L'avventuriero dovrà esibirsi presso la sede designata entro il limite di tempo stabilito. Gli spettatori soddisfatti o delusi aggiungeranno o sottrarranno punti al punteggio complessivo. Non sono previsti compensi supplementari per il superamento della quota minima richiesta.

* Per ottenere i migliori risultati, si raccomanda di suonare dinanzi a vaste platee.
* Gli avventurieri con un'alta competenza nell'abilità Musicale possono assumersi incarichi di maggior prestigio.

{p}
<b>Raccolta Agricola</b>

L'avventuriero è tenuto a mietere e raccogliere prodotti agricoli presso la tenuta indicata entro il tempo limite. Solo i raccolti depositati nell'apposita cassa delle spedizioni saranno conteggiati ai fini della quota. La ricompensa è calcolata in base al peso complessivo conferito. I prodotti ancora in possesso dell'avventuriero al termine dell'incarico potranno essere confiscati.

* È opportuno dare priorità alla raccolta di ortaggi e frutti di peso elevato.
* Una volta raggiunta la quota pattuita, lasciare la tenuta non comporterà il fallimento della missione.
* Gli avventurieri esperti nell'abilità Raccolta possono intraprendere incarichi a resa superiore.

{p}
<b>Consegna Merci</b>

L'avventuriero dovrà recapitare l'articolo affidatogli al destinatario entro l'orario concordato. Una volta accettato l'incarico, la mancata consegna sarà perseguita a norma di legge come frode postale.

* Il committente declina ogni responsabilità circa l'effettiva capacità di carico dell'avventuriero o la congruità del tempo concesso.
* In caso di smarrimento dell'articolo, l'avventuriero può procurare a proprie spese un rimpiazzo identico e consegnarlo al destinatario.
* L'impiego di dispositivi di teletrasporto è severamente vietato durante le consegne.

{p}
<b>Scorta di Viandanti</b>

L'avventuriero dovrà scortare il cliente fino alla destinazione pattuita entro il termine prefissato. Una volta accettato il contratto, la morte dell'assistito comporterà il fallimento immediato dell'incarico con imputazione di responsabilità diretta a carico della scorta.

* Nelle aree pericolose, l'assistito deve trovarsi nelle immediate vicinanze dell'avventuriero prima di abbandonare la mappa, onde evitare l'accusa di abbandono e la conseguente rescissione contrattuale.
* L'impiego di dispositivi di teletrasporto è severamente vietato.

{p}
<b>Sterminio Mostri</b>

L'avventuriero ha il mandato di abbattere tutte le mostruosità presenti nel luogo designato. Allontanarsi anzitempo costituisce rinuncia e fallimento della missione.

* Gli avventurieri di grande fama possono accedere a contratti di disinfestazione più ardui e lautamente retribuiti.

<b>Caccia Selettiva</b>

L'avventuriero dovrà abbattere il numero prestabilito di creature entro il tempo concesso. L'ubicazione geografica degli abbattimenti è libera. Le ricompense sono commisurate al numero e alla pericolosità delle belve eliminate.

* Quando la richiesta specifica una determinata tipologia di fiera, le specie idonee verranno evidenziate nel diario di viaggio.

{p}
<b>Guerra e Resistenza</b>

L'avventuriero è chiamato a resistere per un intervallo di tempo prestabilito sotto l'incessante assalto di ondate di mostruosità belliche. Scaduto il tempo limite, l'avventuriero dovrà suonare la ritirata al corno da guerra ed evacuare la zona d'operazioni. Le ricompense sono corrisposte in funzione delle uccisioni confermate e delle ondate superate.

* Il corno da guerra può essere liberamente imbracciato e spostato sul campo. Può essere suonato per richiamare anticipatamente l'ondata successiva, ma posticiperà l'ordine di ritirata. Richiamare un'ondata immediatamente dopo l'inizio della precedente incrementerà la ricompensa finale.
* A intervalli regolari potranno giungere rinforzi alleati in supporto dell'avventuriero.

{p}
<i>- Post Scriptum -</i>

Tutte le missioni andate a buon fine riconosceranno un compenso in monete di platino commisurato al grado di difficoltà affrontato.

Le richieste riflettono i bisogni delle comunità locali: gli avventurieri sono esortati a muoversi laddove vi sia domanda di lavoro. Si raccomanda prudenza nell'accettare gli incarichi, poiché la fattibilità dell'impresa non è in alcun modo garantita dai committenti.

Sebbene una missione possa essere annullata tramite il diario o abbandonando l'area, tale inadempienza comporterà la perdita di karma e prestigio personale. A seconda della natura dell'incarico potranno applicarsi ulteriori sanzioni pecuniarie.

Per qualsiasi controversia contrattuale si invita a rivolgersi al tribunale mandamentale competente, astenendosi da atti di giustizia sommaria.
""",

    'guide_ranch.txt': """Vita da Fattore,Autore Ignoto

<i>(Sembra una circolare aziendale interna a uso del personale)</i>

La mia rete di allevamenti si è espansa in tutta Zanan a tal punto che trovo più pratico redigere questo manuale piuttosto che istruire singolarmente ogni nuovo amministratore: leggete con la massima attenzione. Se la vostra filiale non genererà profitti adeguati, ne risponderete direttamente al sottoscritto!

{p}
<b>Infrastruttura del Pascolo</b>

Prima di cominciare dovrete predisporre i terreni. Edificate una stalla ben illuminata e piantate un cartello del pascolo affinché il bestiame rimanga al coperto: i muri spessi proteggeranno gli animali dalle bestie feroci erranti. Se preferite tenere le vostre creature all'aperto, recintatele a debita distanza dai confini della tenuta e assicurate loro un riparo sicuro per la notte.

Se disponete di sufficienti punti amministrazione, incaricate i dipendenti di organizzare ronde di sorveglianza perimetrale. Ricordate: il bestiame morto o stressato non produce un bel niente, perciò preservare la vita delle vostre bestie è una priorità assoluta.

Se vi sentite particolarmente generosi potete concedere balle di fieno su cui far dormire gli animali, sebbene non sia strettamente necessario.

{p}
<b>Alimentazione</b>

Ogni capo d'allevamento necessita di una porzione di foraggio al giorno: niente foraggio, niente prodotti. Potete mietere foraggio selvatico, ma la soluzione migliore è seminarlo e coltivarlo in proprio: un foraggio di alto livello aumenta la resa del raccolto, consentendovi di mantenere un numero maggiore di animali.

Il bestiame non bruca il foraggio direttamente dalla pianta: deve essere raccolto e riposto in una cassa condivisa. La bacheca della tenuta riporta il riepilogo delle scorte di foraggio accumulate e il fabbisogno giornaliero stimato.

Potete viziare i vostri animali con pietanze cucinate come premio, ma ciò non eliminerà il loro fabbisogno quotidiano di foraggio fresco.

{p}
<b>Acquisto e Scelta del Bestiame</b>

Dovete ora determinare quale tipologia di allevamento avviare. I prodotti zootecnici includono: uova, latte, carne e vello. Selezionate specie compatibili con gli obiettivi produttivi della vostra azienda: per i novizi raccomando caldamente i putit delle nevi, capaci di fornire tutte e quattro le risorse.

La produzione di latte e uova è vincolata alla specie d'appartenenza: gli allevamenti di dinosauri suonano altisonanti, ma sono del tutto inefficienti. Come regola generale, più un animale occupa i gradini bassi della catena alimentare, più è prolifico — da qui l'inestimabile valore del modesto putit delle nevi. Sebbene esistano tenute a Zanan che producono beni d'eccellenza come scaglie di drago e bestie da guerra per l'esercito, si tratta di strutture rare e massicciamente sovvenzionate dalla corona.
{p}
I primi esemplari possono essere acquistati dagli addestratori di bestiame, oppure potete cimentarvi nella cattura di creature selvatiche con sfere per mostri o ammansirle con una spazzola morbida. In entrambi i casi, registrate la bestia addomesticata come bestiame nella lista dei residenti e il gioco è fatto.

{p}
<b>Operazioni Quotidiane</b>

Il bestiame produce uova e latte puntualmente alle 5:00 del mattino; assegnate a un lavoratore la mansione delle corvée per raccogliere le merci e riporle nei bauli condivisi. Le uova necessitano di refrigerazione per evitare il deperimento, mentre il latte si conserva egregiamente a temperatura ambiente.

Le creature da vello vanno tosate quando il manto è folto: potete farlo anche prima, ma attendere la muta completa garantisce una resa superiore. Cesoie forgiate in leghe dure velocizzeranno l'opera, e l'impiego di lozioni rinfoltenti benedette incrementerà la produttività.

Spazzolature regolari manterranno gli animali sereni e mansueti, soprattutto se nell'area si aggirano predatori fastidiosi.

{p}
<b>Espansione dell'Allevamento</b>

Una volta avviata la produzione, sarà il momento di espandere l'attività. Ogni uovo deposto possiede una modesta probabilità di risultare fecondo, schiudendosi e dando vita a un nuovo cucciolo. Gli allevamenti moderni impiegano incubatrici elettriche per velocizzare la covata, ma adagiare (senza gettarlo) l'uovo su un letto rappresenta una valida alternativa economica, benché più lenta. Se nei paraggi è presente una sorgente termale, immergervi l'uovo fecondato garantirà i medesimi risultati di un'incubatrice dopo una breve attesa.

Potete allattare i cuccioli di bestiame con latte fresco per favorirne la crescita e far maturare ai vostri lavoranti preziosa esperienza nell'addomesticamento.
{p}
Detto questo, evitate di espandervi oltre le vostre reali capacità gestionali. I capi in eccesso possono essere macellati con una mannaia per ricavare ingenti quantità di carne e vello (ove previsto) — un'alta competenza in Anatomia produrrà i tagli migliori. In alternativa, gli animali possono essere venduti direttamente ai visitatori della tenuta etichettandoli per la vendita.

Esigo di trovare il vostro rendiconto finanziario annuale sulla mia scrivania all'indomani del prossimo Juremas.

{p}
<i>Appendice: Esempi di Bestiame e Tipologie di Vello</i>

Coniglio, putit delle nevi: cashmere
Putit delle nevi dorato: filamenti d'oro
Pesce: scaglie
Dinosauro: pelle dura
Maiale, Pecora: lana
Coleottero: seta grezza
Ragno: seta di ragno
Drago, viverna: scaglie di drago
Scheletro: frammenti ossei
Ent: legname pregiato
""",
}

for fname, content in BOOKS.items():
    p = os.path.join(BOOK_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(content.strip() + '\n')

print(f"Translated {len(BOOKS)} guide and lore books in {BOOK_DIR}")
