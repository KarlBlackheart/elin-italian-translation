"""
Translate Adventurer's Weekly 16 to 25 and _default.txt into Italian.
"""
import os

BOOK_DIR = 'Lang/IT/Text/Book'

ADVWEEK_16 = """Settimanale dell'Avventuriero N. 16: Armi da Tiro,Sergente Kzar,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Salute, reclute. Hans mi ha chiesto di istruire voi giovani avventurieri sulle armi a distanza: archi, balestre e armi da fuoco. Anche se le Forze Speciali di Palmia sono rinomate soprattutto per le loro sparatorie, ogni arma ha il suo scopo. Le armi da fuoco necessitano di ricarica, mentre archi e balestre no; durante la ricarica potete agire, ma non potete fare fuoco.

{p}
<b>Gittata Ideale</b>

La prima regola fondamentale del combattimento a distanza è che ogni arma possiede una gittata ideale. Più la distanza tra voi e il bersaglio si allontana da questo valore ottimale, minori saranno i danni inflitti. Ad esempio, i fucili a pompa danno il meglio a bruciapelo, mentre i fucili a rotaia eccellono dalla lunga distanza. Decidere continuamente se fare fuoco o riposizionarsi può sembrare tedioso, e molti avventurieri trascurano la gittata ideale, ma la cura del dettaglio ripaga sempre con gli interessi.
{p}
<b>Munizioni</b>

Parliamo di munizioni: gli archi richiedono frecce, le balestre dardi, e le armi da fuoco proiettili, razzi o celle energetiche a seconda del modello. Non confondeteli! Voi dovete avere munizioni nell'inventario per sparare, mentre i vostri alleati hanno le proprie scorte; tuttavia, useranno volentieri qualsiasi munizione speciale decidiate di consegnare loro.

Alle nostre reclute facciamo sempre addestrare la fabbricazione: le munizioni artigianali migliorano drasticamente l'efficacia in battaglia. Più alto è il vostro livello di artigianato, più letali saranno i proiettili forgiati, con potenti effetti elementali annessi. Il materiale fa la differenza: le munizioni in rubinus sono precisissime, quelle in adamantio causano danni devastanti, mentre rame, onice e simili infliggono danni elementali e alterazioni di stato. Tenete a portata di mano una varietà di munizioni — e idealmente di armi — per fronteggiare ogni evenienza.

Risparmiate le munizioni quando potete: anche se non volete montare modifiche per il risparmio colpi, chiunque può imparare a usare munizioni economiche per l'esplorazione ordinaria e conservare quelle speciali per i nemici più tosti.
{p}
<b>Modifiche e Accessori</b>

Rispetto al corpo a corpo, le armi a distanza offrono possibilità di personalizzazione infinitamente superiori. Ogni arma possiede slot di modifica in base alla sua qualità — raramente fino a 6 sulle armi divine. In questi alloggiamenti si possono installare kit di modifica per ottenere svariati effetti, come respingimento, ricarica rapida o conservazione dei colpi.

Potete acquistare i kit di modifica dagli armaioli, oppure estrarli dalle armi recuperate come bottino. Smantellare le armi con un martello recupererà i kit, ma per un'estrazione sicura e pulita è consigliabile usare polvere da scasso presso una macchina per la lavorazione delle canne.
{p}
<b>Bastoni da Tiro</b>

Dato che anche i bastoni magici rientrano nella categoria delle armi a distanza, sono tenuto a menzionarli brevemente in questa rubrica. Essi consumano PM come munizioni, il che è un vantaggio per i novizi squattrinati ma uno svantaggio per chi desidera sfruttare i bonus delle munizioni artigianali. I bastoni offrono inoltre accesso a elementi che i normali materiali metallici non possiedono.

La maggior parte dei modificatori validi per armi da fuoco e archi funziona anche sui bastoni, seppur con qualche adattamento; ad esempio, la conservazione munizioni riduce il costo in PM del bastone.
{p}
<b>Conclusione</b>

Grazie alle munizioni specializzate e ai kit di modifica, le armi da tiro traggono un beneficio diretto e immenso dalla perizia artigianale. Qualsiasi arciere o pistolero che si rispetti dovrebbe gestire con cura la propria logistica e tenere sempre a portata i materiali necessari; sconsiglio di intraprendere seriamente la via del tiratore prima di aver stabilito una solida linea di rifornimenti, ma i risultati ripagheranno ogni sforzo.

Come nel corpo a corpo, disporre di equipaggiamento variegato garantisce la flessibilità necessaria per superare ogni pericolo. Le armi a distanza non hanno stili di combattimento rigidi, quindi passare dall'una all'altra è molto più semplice.

***

<i>- Nel prossimo numero analizzeremo alcuni usi... ehm, <b>del tutto legali</b> delle abilità da ladro!</i>
"""

ADVWEEK_17 = """Settimanale dell'Avventuriero N. 17: L'Arte del Furto,Madama Persefone,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, dove vi scrivo, tesori miei, dalla pace della mia tenuta di campagna.</i>


Anche se sono abbastanza facoltosa da potermi godere la vita per il resto dei miei giorni, la pensione alla lunga diventa noiosa, e la proposta di Hans era... intrigante. È sempre stato un caro amico, perciò insegnerò a voi piccoli tesori qualche trucchetto della mia giovinezza.

Mi promettete che farete tesoro di queste nozioni solo a scopi legali, vero?
{p}
<b>Borseggiare</b>

In parole povere: il furto. Saccheggiare il tesoro di un drago non è fondamentalmente diverso dallo sfilare la borsa a un orco distratto.

Per prima cosa, vi occorrono forza e perizia sufficienti. Un punto di forza corrisponde a 0,1s di carico sfilabile, mentre un punto nell'abilità Borseggiare vale 0,2s. Finché la loro somma supera il peso dell'oggetto, riuscirete nell'intento.

In secondo luogo, dovete evitare lo sguardo di chiunque possa avere da ridire sulla vostra marachella. Finché nessuno vi osserva direttamente, siete al sicuro: non dovrete preoccuparvi di fare — hem — "troppo rumore". L'invisibilità aiuta, ma non garantisce il successo assoluto. Accecare, confondere, addormentare o paralizzare i testimoni <b>funziona</b> sempre, anche se poi vi ritroverete con altri problemi a cui badare.
{p}
Certo, potreste sempre trucidare tutti o spazzarli via con una verga di teletrasporto, ma questo è così tipico di Hans... che volgarità.

Ora, sono certa che voi dolcezze non fareste mai cose deprecabili come taccheggiare nei negozi o svaligiare le case della povera gente, vero?

Cominciate con oggetti leggeri e incustoditi, e fate pratica salendo gradualmente di livello. Quando sarete abili quanto me, sfilerete le armi dalle mani dei nemici e le corazze dalla loro schiena mentre schivate i loro fendenti! Fidatevi: i vostri amici maghi vi ringrazieranno per aver privato quell'abominio del suo anello antimagia.

{p}
<b>Scassinare</b>

A meno che non vi piaccia pagare i tariffari esorbitanti degli informatori, avrete bisogno di questa abilità per aprire i forzieri chiusi a chiave che abbondano nei nefia. Innanzitutto, servono i grimaldelli: senza di essi, potrete forzare solo serrature con un livello pari alla metà della vostra abilità. Con i grimaldelli, il limite sale alla vostra abilità + 10: un bell'incentivo, non trovate?

Gli empori vendono grimaldelli solo di rado, ma la Gilda dei Ladri ne ha sempre scorte per i membri affiliati. Ai miei tempi, mi intrufolavo furtiva nel loro covo per fare scorta ai distributori automatici...

L'ostacolo più grande per voi novizi è iniziare a fare pratica. Alcuni consigliano i forzieri d'addestramento, ma per me sono troppo lenti e noiosi. I forzieri da gioco d'azzardo offrono un briciolo di esperienza, ma non sono convenienti.
{p}
Quel che facevo io era setacciare i rigattieri in cerca di forzieri con serrature elaborate: gli informatori non possono aprirli, e sono una palestra eccezionale. Una volta avviata l'abilità, non toccherete mai più un baule d'addestramento, grazie agli dèi! Inoltre, i forzieri elaborati contengono spesso ottimo bottino, quindi otterrete ben più della sola esperienza.

Un consiglio d'oro: la perizia non è mai troppa. Tenere pronto un set di vestiario ed equipaggiamento che potenzi l'abilità Scassinare, da indossare prima di smistare il bottino dei nefia, è un'ottima abitudine per novizi ed esperti.
{p}
<b>Furtività</b>

A Hans non è mai piaciuto muoversi nell'ombra, ma persino lui ha dovuto ammettere che scegliere i propri scontri salva la pelle. Muoversi furtivamente mette alla prova la vostra abilità contro la percezione e la vista di chi vi circonda: più siete vicini a un nemico, più è arduo non farsi notare, e i bersagli già allertati dal combattimento sono doppiamente vigili.

La furtività è un'arte che rende al meglio in solitaria; basta un solo compagno maldestro per mandare all'aria l'intero piano. Se dovete muovervi in gruppo, la furtività di ciascun membro viene esaminata singolarmente: non possono esserci anelli deboli. Con la giusta maestria, potrete scivolare in un nefia ed esplorare le stanze più ricche senza che gli abitanti si accorgano nemmeno del vostro passaggio.
{p}
<b>Conclusione</b>

È affascinante come così tante abilità legate al crimine risultino indispensabili per avventurieri impeccabili e irreprensibili, non è vero? La gente ci disprezza per i nostri trucchi, ma chiude volentieri un occhio quando ha bisogno dei nostri servigi... pazienza. Ora sono una nobildonna rispettabile, e sono certissima che nessuno di voi tesorucci userà quanto appreso oggi per mettersi nei guai.

Alla prossima puntata, cari miei!

***

<i>- Nel prossimo numero scopriremo come formare e gestire una compagnia d'avventura davvero efficace!</i>
"""

ADVWEEK_18 = """Settimanale dell'Avventuriero N. 18: Formare un Gruppo,Sergente Kzar,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Salute, reclute. L'argomento di oggi è la gestione delle squadre d'avventura, quindi bando alle ciance. Formare un gruppo equilibrato moltiplica la vostra efficacia, poiché i membri si spalleggiano e coprono a vicenda le proprie debolezze; sono le stesse tattiche di plotone che adottiamo nelle forze speciali.

{p}
<b>I Ruoli della Squadra</b>

Agli avventurieri novizi basta avere numeri dalla loro parte, ma man mano che la fama e i pericoli crescono, la composizione del gruppo deve farsi selettiva. Tutti vogliono fare danno, ma nessuno vuole curare.

Il vostro gruppo deve coprire questi compiti fondamentali:

* Assorbire i colpi. Significa attirare i bersagli e incassare i colpi senza tirare le cuoia. Per attirare i nemici, all'inizio basterà l'abilità di provocazione; più avanti sbloccherete talenti ed equipaggiamenti dedicati. Per incassare, occorre incrementare protezione e resistenze, gonfiare la riserva di salute tramite vigore e costituzione, e sfoggiare armature dalle difese invidiabili.
{p}

* Curare. È fondamentale avere un curatore dedito alle ferite del gruppo. Idealmente, qualcuno dotato di potenti incantesimi curativi e dell'istinto di guarigione. Le cure nel tempo aiutano, ma non possono essere l'unica risorsa del medico: mancano della prontezza e della potenza d'impatto di una cura diretta istantanea. Inoltre, saper rianimare i caduti è un salvavita impagabile.

* Infliggere danni. Il ruolo più ambito in assoluto; vantarsi con "Ho abbattuto il drago!" attira molti più sguardi ammirati di "Ho preso mazzate mentre un altro uccideva il drago" o "Ho medicato chi ha ucciso il drago". La squadra dovrebbe bilanciare danni fisici e magici per farsi trovare pronta contro qualunque orrore spunti dal nefia; i danni elementali causano spesso alterazioni di stato, quindi fate in modo che questi compagni applichino anche penalità.
{p}
* Potenziare e indebolire (Buff e Debuff). Spesso sottovalutati dai novellini, i potenziamenti e le maledizioni possono rendere abbordabile persino il mostro più terrificante. Adattateli al vostro gruppo: guerrieri e tiratori traggono immenso beneficio da debolezze e vulnerabilità fisiche, mentre un gruppo di incantatori preferirà incubo e piaga elementale. I potenziamenti difensivi sono invece universali, poiché una corazza rinforzata fa comodo a tutti.


Un singolo membro può ricoprire più ruoli contemporaneamente: potete avere un guaritore che scaglia dardi quando nessuno sanguina. Assicuratevi di coprire ogni necessità, e andrete alla grande.
{p}
<b>Gestione del Registro</b>

Ai miei tempi, mettere assieme una squadra comportava correre a destra e a manca per mezza Tyris, ma oggi il registro d'avventura rende la formazione un gioco da ragazzi. Permette di radunare alleati anche se si trovano in città distanti e facilita lo scioglimento della banda a missione compiuta; i compagni che si trovano bene insieme possono registrarsi come formazione permanente per richiamarsi in un attimo.

Potete ottenere un registro o un libro degli alleati da qualsiasi ispettore della frontiera. Ammetto che sia comodo, ma un veterano come me non può fare a meno di sentire la mancanza del calore umano di un invito guardandosi negli occhi. Immagino sia il prezzo del progresso con l'ascesa del Nuovo Regno...

{p}
<b>Schieramento e Formazione</b>

Dato che state leggendo questo testo, darò per scontato che siate voi il caposquadra, colui che apre la strada nel nefia mentre il resto della compagnia segue a ruota. È la prassi: se combattete dalle retrovie, potrete arretrare non appena ingaggiate battaglia.

Restate uniti: un gruppo si muove alla velocità del suo membro più lento. Ordinate agli alleati di starvi vicini e usate un guinzaglio per farli tenere il vostro passo. In caso di emergenza, ad esempio se qualcuno calpesta una trappola di teletrasporto, l'incantesimo di teletrasporto di massa radunerà e riposizionerà l'intera squadra.

I nefia sono spesso cunicoli stretti e angusti, dove corridoi e strettoie ostacolano la manovra. Le piccole bande sfruttano questi colli di bottiglia per reggere l'urto delle orde nemiche, ma per i gruppi numerosi diventano una trappola mortale. Createvi spazio di manovra scavando o facendo saltare i muri con la dinamite!
{p}
Troppi combattenti in prima linea finiranno solo per intralciarsi a vicenda. Equipaggiate tutti con un'arma a distanza, così che possano fare <b>qualcosa</b> in ogni momento del combattimento. Tenete a mente la distanza d'ingaggio preferita di ciascun compagno e assegnate le mansioni di conseguenza. Chi se ne sta con le mani in mano è inutile come un cadavere.


<b>Riepilogo</b>

I compagni d'arme sono come l'equipaggiamento: non basta averli, bisogna saperli impiegare a dovere. Una squadra disciplinata e ben coordinata supererà sfide insormontabili, laddove un'orda disordinata che confida solo nel numero andrà incontro a un massacro.

***

<i>- Nel prossimo numero esamineremo un'altra famigerata minaccia della nostra società: i vampiri!</i>
"""

ADVWEEK_19 = """Settimanale dell'Avventuriero N. 19: I Vampiri,Caporedattore Hans,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Il numero di questa settimana è offerto con il patrocinio della guardia cittadina di Palmia.
{p}

Terrori che volteggiano nel cielo notturno!

Predatori in agguato nell'oscurità più profonda!

Le leggende sui vampiri affondano le radici nei secoli passati. Con i recenti avvistamenti di questi antichi non morti in tutta Tyris, è giunto il momento di separare la realtà dal mito!


<b>La Sete di Sangue</b>

La sete dei vampiri è leggendaria: tutti i racconti concordano sul fatto che non possano consumare cibo normale e debbano invece nutrirsi esclusivamente di sangue fresco. Quasi chiunque può diventare una vittima, purché abbia sangue nelle vene; i costrutti artificiali sono un'ovvia eccezione, ma in alcune cronache anche creature immuni al sanguinamento, come i ricci, sfuggono alla loro predazione.
{p}
I vampiri considerano il sangue proprio come noi apprezziamo il buon vino, descrivendo con morbosa raffinatezza gli aromi e le sfumature di ogni individuo; possono percepire le qualità del sangue altrui con una sola occhiata, e i vampiri più anziani sanno carpirne i segreti più intimi.

I vampiri traggono maggior sostentamento dalle vittime più forti e robuste, proprio come se consumassero un banchetto luculliano; questo nutrimento è amplificato dalla loro abilità di studio e risucchio vitale. Le reazioni delle vittime variano dal disgusto e dall'umiliazione fino a un'estasi perversa; ciò ha dato origine a storie d'amore tra vampiri e umani, dove questi ultimi vengono tenuti in vita come appetitosi e nutrienti spuntini da passeggio!

Personalmente non riesco a capacitarmene, ma pare che questo genere di romanzi vada a ruba tra le fanciulle, quindi...
{p}
Curiosamente, condire qualsiasi pietanza con abbondante ketchup la rende commestibile persino per i vampiri! La Gilda dei Maghi ipotizza che i vampiri non abbiano bisogno di sangue in senso strettamente materiale, bensì di una sua risonanza metafisica: un cibo che abbia l'<i>aspetto</i> e il colore del sangue è sufficiente a ingannare la loro sete. Certo, non sazia quanto un collo pulsante, ma è senza dubbio un'abitudine più discreta che girare con sacche di sangue o azzannare passanti nei vicoli.

{p}
<b>Altri Poteri e Debolezze</b>

* In quanto signori delle tenebre, i vampiri vedono i propri attributi incrementare dalle cinque del pomeriggio fino alle cinque del mattino; la mutazione è rapida ma non istantanea. Che il vampiro sia effettivamente esposto al sole o rintanato nel buio di una grotta non fa differenza: come per il trucco del ketchup, la loro sintonia con il ciclo del giorno e della notte anche nel sottosuolo dimostra che il legame è di natura puramente metafica.

* I vampiri si tramutano spesso in pipistrelli per spostarsi rapidamente: in questa forma alata non temono la luce del sole e vantano un'agilità e una schivata prodigiose, ma diventano incredibilmente fragili e deboli. Per quanto siano fulminei e silenziosi, un singolo colpo ben assestato può sbriciolarli sul colpo.

{p}
<b>Riconoscimento e Difesa</b>

Molti non morti superiori sono del tutto indistinguibili dai vivi a prima vista, perciò spetta all'occhio attento dell'avventuriero smascherarli:

* I vampiri tendono a bagnarsi costantemente per non bruciare alla luce solare. Diffidate di individui che si rovesciano addosso liquidi senza motivo, passeggiano sotto la pioggia scrosciante o nuotano nei canali in pieno giorno!

* I vampiri sono vulnerabilissimi al fuoco e tendono a bardarsi con quantità spropositate di equipaggiamenti resistenti alle fiamme; chiunque vesta da capo a piedi in scaglie di drago a mezzogiorno desta legittimi sospetti!

* Esistono incantamenti per elmi e copricapi che proteggono i non morti dal sole: trovarne uno su un viaggiatore è una prova schiacciante.
{p}
* Attenzione ai pipistrelli che trasportano arnesi, armi o zaini! La trasformazione non impedisce affatto al vampiro di compiere le sue normali azioni!

* Alcuni vampiri terrorizzati dai pasti scadenti si sono convertiti alla scienza: avvicinare sconosciuti per punzecchiarli a tradimento con siringhe da prelievo non è un comportamento da gentiluomini.

* I vampiri abbastanza sconsiderati da addormentarsi al sole senza protezione vanno incontro a sofferenze atroci. Chiunque insista nel volere un letto a forma di bara definendolo "un grazioso pezzo d'arredamento alternativo" merita un'attenta segnalazione.
{p}
La maggior parte delle credenze popolari per scacciare i vampiri è priva di fondamento: ad esempio, la vecchia fandonia secondo cui l'acqua benedetta di Jure li scioglierebbe all'istante è falsa. Tuttavia, le statuette consacrate di Jure, acquistabili durante il Festival della Notte Santa a Noyel, scoraggiano concretamente i vampiri dall'attaccarvi. Le tradizionali contromisure contro i non morti — fuoco, magie sacre e armi anatema dei non morti — restano letali ed efficacissime.

I vampiri non sono intrinsecamente malvagi, e le cronache riportano casi di autentici cittadini modello; resistere alla tentazione quotidiana di considerare ogni prossimo come una gustosa merenda richiede una nobile forza di volontà. Purtroppo, la maggior parte dei succhiasangue non fa troppe distinzioni morali; in seguito a diversi recenti decessi, la guardia cittadina di Palmia esorta la cittadinanza a segnalare tempestivamente qualunque individuo sospetto.

***

<i>- Nel prossimo numero parleremo di riciclaggio e di come fare affari mantenendo Ylva pulita e splendente!</i>
"""

ADVWEEK_20 = """Settimanale dell'Avventuriero N. 20: Il Riciclaggio,L'Inviata di Yowyn Celia,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Questa settimana scrivo per diffondere la buona novella del riciclaggio!

Vivere nella campagna di Yowyn fa un gran bene alla salute, e gran parte del merito va al nostro ambiente incontaminato; gli dèi ci hanno fatto dono di questa terra rigogliosa, ed è nostro sacro dovere custodirla! Conservare la genuinità del vivere rurale significa anche pulire e raccogliere ciò che si sporca!
{p}
E poi c'è sempre l'impiccagione del cittadino di turno sorpreso a gettare immondizia nei boschi: dare un segnale forte e chiaro è fondamentale!

I rifiuti sono inevitabili, tutti produciamo scarti. Ma riciclando, riduciamo drasticamente ciò che finisce buttato. Ed è un metodo assai migliore rispetto a una noiosa campagna contro l'abbandono dei rifiuti, perché non immusonisce la gente e ci riempie le tasche di materiali utilissimi!

Ecco il tema di oggi!


<b>La Raccolta Differenziata</b>

Ogni mattina divido scrupolosamente la mia spazzatura in tre contenitori: la cassa dei rifiuti combustibili, la cassa dei rifiuti incombustibili e la cassa del compost. Non serve che siano condivise per funzionare! Ognuno dovrebbe possederne almeno un set nella propria dimora!
{p}
Nel caso in cui le casse siano piene, ho piazzato anche un cartello della discarica per raccogliere l'eccesso, così che gli scarti non rotolino ovunque sul terreno.

Non tutti hanno il mio stesso senso civico: a bassi livelli di civiltà il vandalismo e l'abbandono di immondizia possono ancora verificarsi. Ma una rigorosa campagna di raccolta differenziata, un pizzico di morale pubblica e, naturalmente, un bel giretto sul patibolo per i trasgressori fanno miracoli garantiti!

Un giorno, l'immondizia di <b>tutti</b> sarà differenziata alla perfezione nei bidoni giusti, e allora saremo <b>tutti</b> puliti e lindi! Lavoriamo insieme per trattare la nostra Ylva con amorevole rispetto!


<b>L'Arte del Riciclo</b>

Ora che abbiamo accumulato un bel mucchio di rottami, è tempo di presentare il signor Martello!
{p}
Il signor Martello smonta ogni oggetto restituendo materiali preziosi, quindi presentategli i vostri rifiuti e rimarrete a bocca aperta! Potete ridurre qualsiasi scarto inutile in legname grezzo, lingotti, tessuti e persino ricavarne materiali rari!

Oggi ho preso a martellate tutti i miei rifiuti incombustibili e ne ho filato i frammenti ricavandone fibre tessili e corde robuste, poi ho fatto a pezzi qualche vecchio bollitore per forgiare lingotti e fabbricare bulloni! Qualcuno aveva gettato via dei piatti di foglie secche, così li ho battuti col martello per ricomporre grandi foglie e intrecciarle in funi!

Nel giro di poco tempo ho confezionato diversi zaini capienti, richiestissimi durante la stagione della mietitura! L'unico materiale che la mia spazzatura non poteva fornirmi erano le pelli conciate, che ho acquistato dal macellaio. Se solo gli avventurieri che hanno comprato i miei zaini sapessero che erano fatti di spazzatura, forse si lamenterebbero... ma a ben pensarci, perché mai? Non c'è nulla di male nel ridare splendida vita a vecchi scarti logori!
{p}
Ci sono mille altri modi per valorizzare i rifiuti: trasformarli in fertile compost, sacrificarli alla divina Dama Jure, o usarli per soddisfare le richieste dei popolani! Usate la fantasia e non dovrete mai più buttare via nulla! Riciclare i vecchi elettrodomestici per evitare la tassa di smaltimento? Quella sono proprio io!
{p}
Abbracciando il riciclaggio non solo inquiniamo di meno, ma risparmiamo anche una montagna di quattrini! E cosa fare con i rottami impossibili da riciclare? Be', potete gettarli in un bidone della spazzatura ufficiale per guadagnare preziosi ecopunti invece di lordare il suolo o buttarli nella cassa delle spedizioni! Qui a Yowyn, il mercante di ecopunti offre mercanzie magnifiche in cambio di questi gettoni!

Ora devo proprio salutarvi: me ne vado a pesca sul fiume! Le esche? Fatte con le ossa riciclate dalla mia spazzatura, naturalmente!

***

<i>- Nel numero della prossima settimana esamineremo nel dettaglio le resistenze elementali!</i>
"""

ADVWEEK_21 = """Settimanale dell'Avventuriero N. 21: Le Resistenze,L'Inviato di Lumiest Jaystar,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Questa settimana esamineremo da vicino le resistenze elementali.

Nel corso delle vostre avventure incontrerete regolarmente mostri che non si limitano a mordere o graffiare con gli artigli. Potreste ritrovarvi arsi vivi, congelati, fulminati, corrosi dall'acido, avvelenati e molto altro; gran parte delle facoltà mostruose ricade infatti in qualche dominio elementale.
{p}
I danni inferti da queste forze scavalcano completamente il Valore di Protezione (VP); l'armatura a piastre più solida e pesante di tutta Ylva non potrà nulla contro una saetta sfrigolante. È qui che la resistenza entra in gioco per mitigare i danni degli elementi.


Ma che cos'è la resistenza? In parole semplici, rappresenta la capacità di tollerare e assorbire un determinato elemento. Che derivi da equipaggiamenti, talenti, fede, incantesimi o altro, la somma finale viene confrontata con la violenza dell'attacco subito.

La resistenza si articola in scaglioni: l'effetto protettivo cambia solo quando il punteggio varia abbastanza da passare a uno scaglione diverso. Di conseguenza, piccole variazioni all'interno dello stesso intervallo potrebbero non mostrare differenze visibili.
{p}
Gli scaglioni e i relativi moltiplicatori di danno sono i seguenti:

-10 o meno — 2x danni (Vulnerabilità estrema)
da -9 a -5 — 1.5x danni (Debolezza)
da -4 a 4 — 1x danni (Neutro)
da 5 a 9 — 0.5x danni (Resistenza moderata)
da 10 a 14 — 0.33x danni (Resistenza forte)
da 15 a 19 — 0.25x danni (Resistenza eccezionale)
20 o superiore — 0x danni (Immunità totale)

Si noterà come la massima efficienza si raggiunga al livello 5 di resistenza, ma incrementarla ulteriormente garantisce sempre una protezione superiore. Inoltre, con una resistenza pari a 20 gli effetti collaterali elementali vengono del tutto annullati, a meno che l'aggressore non sia un devoto di Kizuami. Da notare che la resistenza alla magia attenua parzialmente ogni forma di danno elementale, rendendola un attributo difensivo di valore inestimabile.
{p}
Data la sterminata gamma di elementi presenti nei nefia, molti avventurieri dedicano l'intera vita a risolvere il cosiddetto "rompicapo delle resistenze": escogitare combinazioni per diventare immuni al maggior numero di elementi possibile. Grazie all'uso ingegnoso delle rune, svariati veterani ci sono andati vicini, eppure rimanere del tutto impermeabili a ogni danno elementale è semplicemente impossibile.

Per quale motivo?


In primo luogo, per alcuni domini la resistenza è strutturalmente limitata e non può raggiungere quota 20 (come nel caso dell'acido), oppure non esiste affatto, come per i danni da impatto e forza cinetica.
{p}
In secondo luogo, i mostri dispongono di contromisure formidabili contro le nostre difese: le più temibili sono maledizioni come piaga elementale e incubo. Le resistenze concesse dalla fede possono essere stracciate dalla scomunica, le difese magiche dissipate, e le lame incantate penetrano ben due scaglioni di resistenza, fino a un minimo di 0.

Infine, le razze ancestrali di Ylva come draghi e demoni sono capaci di dominare elementi superiori che perforano naturalmente le resistenze di uno scaglione; nessun avventuriero potrà mai accumulare tanta protezione da rendersi totalmente immune alle loro devastanti manifestazioni.
{p}
Risolvere il puzzle è più abbordabile per gli elementi di base: difendersi da fuoco, gelo e fulmine è alla portata persino degli avventurieri di medio livello grazie a materiali come scaglie e lana pregiata. Le resistenze più esotiche, al contrario, si presentano in porzioni assai più risicate e richiedono imprese titaniche. Benché l'ideale sia un corredo capace di offrire quante più immunità possibili, un traguardo simile è raramente praticabile sul campo: disporre di set d'equipaggiamento intercambiabili per situazioni specifiche rappresenta la strategia più saggia.

In definitiva, la conoscenza rimane la migliore corazza: sapere quali mostri si andranno ad affrontare e quali siano le loro armi costituisce la base per scegliere da quali elementi schermarsi. Dopotutto, nessuno sano di mente si aspetterebbe fiamme infernali sul fondo di una rovina sommersa!

***

<i>- Nel prossimo numero metteremo finalmente sotto i riflettori il tema del matrimonio!</i>
"""

ADVWEEK_22 = """Settimanale dell'Avventuriero N. 22: Il Matrimonio,L'Inviata di Yowyn Celia,10,1

<i>Ciao a tutti! Benvenuti al Settimanale dell'Avventuriero, dove questa settimana tratterò un argomento che mi sta immensamente a <b>cuore</b>!</i>


<b>Il Matrimonio!</b>

Il mio fidanzato mi ha fatto la fatidica proposta qualche giorno fa, e il signor Hans mi ha suggerito di condividere questa magnifica emozione con voi lettori! Gli avventurieri di tutta Ylva leggeranno delle mie nozze e scopriranno cosa significhi convolare a nozze a Tyris!

{p}
<b>La Proposta</b>

Tutto è cominciato qualche settimana fa, quando si è presentato con un anello di fidanzamento e mi ha chiesto la mano...! Io avrei preferito un amuleto di fidanzamento, ma l'anello è tradizionale e incredibilmente romantico!

Stiamo insieme da parecchio tempo, quindi naturalmente ho detto di sì! Ho sentito dire che tra avventurieri ci si sposa con una rapidità sbalorditiva — affidarsi la vita a vicenda nelle profondità di un nefia crea legami indissolubili in fretta — ma noi gente semplice di campagna preferiamo fare le cose con calma, aiutarci nei campi e imparare a conoscerci giorno dopo giorno! Non c'è una via giusta o sbagliata, l'unica cosa che conta è amarsi sul serio!

È un anello splendido: solo a guardarlo mi sento sciogliere dalla tenerezza, nessuno all'infuori di me indosserà mai questo dono del mio amato! È così che dovrei chiamarlo d'ora in poi, vero? Eheh.
{p}
<b>I Preparativi</b>

Ora che siamo ufficialmente fidanzati, oggi andremo dal notaio per acquistare il permesso di matrimonio! Costa una bella sommetta, ma la spesa include la prenotazione del luogo della cerimonia, il banchetto nuziale, gli inviti per gli ospiti e tutto il resto! Penseranno a tutto loro: a noi basterà presentarci eleganti nel grande giorno!

Certo, qualcuno preferisce risparmiare quattrini e decide di non formalizzare l'unione. Dopotutto, se vivete come se foste sposati, siete sposati a tutti gli effetti. Ma al contempo desidero rendere le cose solenni e ufficiali con il mio amato, e sono disposta a spendere ogni mia moneta!

Oh... vendono anche le pratiche per il divorzio qui. Bleah, un po' cinico proporle nello stesso ufficio, non trovate? Be', non importa. Ora che abbiamo il permesso, possiamo definire i dettagli per celebrare le nozze!
{p}
<b>Il Grande Giorno</b>

Ci siamo, è finalmente arrivato! Il giorno del nostro matrimonio!

Guarda, tesoro! Sono venuti tutti i nostri conoscenti: non è meraviglioso che tutta questa gente sia qui a festeggiare la nostra felicità? Ohh, tutti quei mazzi di fiori devono essere costati un occhio della testa!

I voti, il bacio, il taglio della torta con quella lama cerimoniale squisita... è il giorno più felice della mia vita! Ho ancora la testa che gira dall'emozione... vedo il mondo sotto una luce completamente nuova! Dicono che si impari molto di più nella vita quando c'è una persona speciale a dare un senso a ogni cosa, eheh!

E conclusa la funzione sacra, è tempo del banchetto... un momento, amore mio. Chi sono quelle donne che stanno irrompendo nella navata della chiesa?
{p}
Kyaaa! E perché ci stanno tirando delle molotov addosso?!

C-cosa?! Sarebbero le tue <i>mogli</i>?! Avevi un intero harem nascosto per tutto questo tempo?! Non me ne importa un accidente se a Eulderna è lecito, qui siamo a North Tyris!

<i>*Sberla fragorosa* *Rumore sordo di un corpo che stramazza sul pavimento*</i>

Per tutti i Pilastri, quanto è stato liberatorio. Reverendo Padre, quanto costano le carte per il divorzio?

<i>T-tutto</i> quel patrimonio?! Non potrò mai permettermele, rimarrò la moglie di un pervertito degenerato per il resto dei miei giorni...

<b><i>...E va bene!</i></b> Se stermino tutte le mie rivali, il mio amato avrà occhi soltanto per <b><i>ME!</i></b>


{p}





<b>Nota del caporedattore</b>

A causa di improvvise questioni familiari, la rubrica della signora Celia è temporaneamente sospesa per alcuni numeri.

Detto ciò, il numero della prossima settimana sarà dedicato agli slime!
"""

ADVWEEK_23 = """Settimanale dell'Avventuriero N. 23: Gli Slime,L'Inviato di Aqui Teola Dott. Mossman,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Dalla città scientifica di Aqui Teola, vi porto le ultime novità della ricerca e della tecnologia: questa settimana presenterò gli studi su una delle creature più trascurate ma straordinarie di Ylva: lo slime.

Gli slime sono considerati parassiti comuni in ogni angolo di Ylva: queste masse gelatinose prosperano nei luoghi umidi, sono spesso pericolosamente acide e proliferano a ritmi spaventosi se lasciate indisturbate. Cugini selvatici dei putit addomesticati, gli slime sono ritenuti dagli studiosi le creature più elementari e basilari del creato.
{p}
Tuttavia, è proprio questa loro natura primordiale a conferire agli slime una versatilità sbalorditiva: col tempo, possono adattarsi a qualunque habitat, consumare qualsiasi materia organica come cibo e assorbire materiale genetico manifestando una miriade di abilità. Da tre anni Aqui Teola conduce ricerche serrate sugli slime per sfruttare il potenziale medico di questa duttilità, e sono certo che siamo a un passo da una svolta rivoluzionaria!

Una creatura tanto comune quanto stupefacente: addentriamoci nel mondo dello slime!


<b>L'Evoluzione Predatoria</b>

Questo è il tratto distintivo dello slime, anche se il termine "predatoria" può trarre in inganno; benché uno slime possa assimilare i geni rilasciati dalle sue prede sconfitte, le sue facoltà non si fermano affatto qui.
{p}
Difatti, l'atto con cui uno slime "divora" materiale genetico da un'altra creatura vivente può risultare persino affettuoso e non arreca alcun danno alla "vittima", sebbene le sensazioni viscide e bizzarre spingano quasi sempre la cavia ad attaccarlo in preda al panico! Alcuni individui, nondimeno, lo trovano persino piacevole. Più uno slime ha fatto pratica nel "divorare", più solido e potente sarà il patrimonio genetico ottenuto.

Comunque sia! Che provenga da un gene inghiottito o dall'assimilazione diretta, una volta completata la fusione lo slime replica alla perfezione i talenti, le abilità e persino gli arti corporei codificati nelle memorie genetiche dell'ospite. Una sorgente di possibilità illimitate: il suo corpo primordiale si rimodella in un batter d'occhio per adattarsi a ogni avversità!
{p}
Forse l'unica ragione per cui gli slime non dominano l'intera ecologia di Ylva è che i loro corpi possono contenere solo un numero limitato di geni alla volta: se tentano di superare la propria soglia limite, perderanno il gene più vecchio assimilato in precedenza. Al contrario, ingerire un gene inferiore epura il gene acquisito più di recente, mentre consumare una cellula cerebrale rimescola l'intera struttura genetica dello slime! Non è meraviglioso?

Crescendo e maturando, la quantità di geni che uno slime può custodire simultaneamente aumenta gradualmente, dando vita a certi slime ancestrali terrificanti che hanno divorato i tratti delle creature più disparate. Gli avventurieri farebbero bene ad approcciarli con estrema prudenza!

{p}
<b>Adattabilità Estrema</b>

La vera forza dello slime risiede nella sua malleabilità biologica: combina geni di specie radicalmente diverse in modi che risulterebbero impossibili in natura, rendendo l'insieme assai più potente della somma delle singole parti. Non è vincolato a un solo ruolo, mutando forma a piacimento finché dispone di materiale genetico fresco, il che spiega la sua straordinaria diffusione su tutta Ylva.

Questa "evoluzione predatoria" è con ogni probabilità il processo attraverso cui i putit odierni sono stati addomesticati a partire dagli slime selvatici, per poi ramificarsi in una miriade di morfologie: il putit beth, il putit metallico, il putit della foresta e il putit d'acqua, per non parlare delle innumerevoli sfumature di colore del putit delle nevi, tanto amato da tutti noi.
{p}
Studiando l'umile slime, la nostra speranza è di perfezionare i metodi di ingegneria genetica applicata. Nel frattempo, raccomando a tutti gli avventurieri di non sottovalutare mai la minaccia gelatinosa!

***

<i>- Nel prossimo numero approfondiremo l'affascinante scienza dell'ingegneria genetica!</i>
"""

ADVWEEK_24 = """Settimanale dell'Avventuriero N. 24: Ingegneria Genetica,L'Inviato di Aqui Teola Dott. Mossman,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Dalla città scientifica di Aqui Teola, vi porto le ultime novità della ricerca e della tecnologia: questa settimana parleremo di una nuova moda che spopola tra gli avventurieri: l'ingegneria genetica.

Questi coraggiosi esploratori affrontano pericoli mortali ogni giorno e necessitano di ogni vantaggio possibile; sempre più spesso si rivolgono alla scienza per ottenere quel margine decisivo. La leggenda narra che la nostra conoscenza dell'ingegneria genetica sia solo una minuscola frazione sopravvissuta dell'avanzatissima biochimica posseduta dall'antica civiltà di Rem-Ido; ma questo è pane per gli storici.
{p}
Assimilando geni esogeni, gli avventurieri ampliano le proprie capacità, apprendono nuovi talenti e possono persino farsi crescere nuovi arti funzionali! Sebbene vi siano dubbi sulla sicurezza di tali pratiche, desidero rassicurare i lettori: la tecnologia messa a disposizione del pubblico è ampiamente collaudata, e quasi tutte le mutazioni sono <i>per la maggior parte</i> reversibili.


I fondamenti di questa scienza si riassumono in pochi concetti chiave:

<b>Alloggiamenti Genetici (Gene Slot): </b> indicano quanto il patrimonio genetico di un organismo possa essere alterato in sicurezza prima di incorrere nel rischio di danni irreversibili e tare genetiche. Questo valore è determinato principalmente dalla specie di appartenenza, con una certa variabilità individuale. Non tutti i geni occupano un solo slot: i geni più potenti e complessi richiedono molteplici alloggiamenti per compensare il turbamento arrecato alla struttura genetica del soggetto.
{p}
Per varie ragioni biologiche, certe specie sono particolarmente predisposte alla manipolazione genetica: possiedono una dotazione di slot superiore, oppure riescono ad accogliere geni potenti occupando meno spazio del normale.

<b>Punti Talento (PT): </b> per reggere l'innesto di geni vigorosi occorrono un corpo e una mente temprati. Ciò significa che soltanto gli avventurieri con una solida esperienza sono in grado di padroneggiare i geni più avanzati.

Inoltre, per cimentarsi nell'ingegneria genetica occorre disporre di:

<b>Un Macchinario Genetico: </b> non è un congegno facile da reperire: si tratta di una tecnologia sofisticata con un consumo energetico notevole. Tuttavia, automatizza la maggior parte delle procedure complesse, permettendo persino a un neofita di compiere innesti genetici impeccabili.
{p}
<b>Materiale Genetico: </b> gli avventurieri lo estraggono di solito abbattendo mostri, specialmente le varianti evolute. Incantesimi come lancia o dardo della notte illuminata dalla luna possono agevolare la raccolta, ma il metodo più affidabile in assoluto consiste nel lanciare una pozione genetica direttamente sul bersaglio designato. Esistono altri metodi per estrarre geni, ma li considero troppo aleatori per meritare menzione.

I geni si suddividono in tre gradi qualitativi: superiore, che garantisce sempre almeno un talento, un'abilità o un arto corporeo; normale, che ne possiede al massimo uno; e inferiore, impiegato per annullare le alterazioni pregresse. I geni inferiori possono essere ottenuti anche macinando due geni qualunque in una macina di pietra.

Esistono inoltre i geni cellulari cerebrali, che obbediscono a regole distinte: non consumano alloggiamenti genetici e servono a rimodellare la condotta e i pattern comportamentali dell'organismo. Non si trovano in natura e vanno sintetizzati artificialmente.

{p}
All'atto pratico, applicare questa scienza è un gioco da ragazzi: assicuratevi che il soggetto possieda PT e slot a sufficienza, inserite il soggetto e il gene prescelto nel macchinario, e quest'ultimo farà tutto da solo. La durata del processo di sintesi dipende dal costo in PT del gene; i tempi possono essere abbreviati mediante iniezioni di siringhe di solvente d'etere. Purtroppo, poiché i macchinari aperti al pubblico richiedono un avvio manuale dall'esterno, per ora non è possibile operare l'editing genetico su sé stessi.

Verificate che la macchina genetica sia costantemente alimentata e che nessuno la urti durante la procedura: qualsiasi interruzione vanificherà ogni progresso. Il soggetto verrà espulso automaticamente dal vano non appena il ciclo sarà terminato.

L'uso di un gene inferiore segue una prassi identica. Al termine, occorrerà selezionare il gene da eradicare: i punti talento spesi verranno rimborsati, ma il gene rimosso andrà perduto per sempre.
{p}
Gli avventurieri forgiano le loro abilità, il loro equipaggiamento e le loro armi: il passo successivo e naturale consiste nel perfezionare sé stessi al livello biologico più profondo. L'ingegneria genetica spalanca una nuova era di prodigi scientifici al servizio di chi esplora l'ignoto!

***

<i>- Nel prossimo numero scopriremo alcune tecniche agricole avanzate per coltivatori ambiziosi!</i>
"""

ADVWEEK_25 = """Settimanale dell'Avventuriero N. 25: Agricoltura Avanzata,L'Inviata di Yowyn Celia,10,1

<i>Ciao a tutti! Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi. Prima di cominciare, ci tengo a ringraziare tutti i lettori per la premurosa solidarietà riguardo ai miei piccoli guai matrimoniali... abbiamo trovato un'intesa amichevole, ma se prova a prendersi un'altra moglie giuro che lo <i>sgozzo</i> nel sonno.</i>


Questa settimana vi porto la saggezza millenaria di Yowyn, tramandata da generazioni di instancabili contadini! Non è emozionante? Ogni avventuriero dovrebbe saper apprezzare il buon cibo, e tutto comincia con il coltivare la terra! Seminare, innaffiare, guardare i germogli crescere: è giusto, ma c'è ben altro sotto la zolla!

{p}
<b>Irrigazione, Raccolto e Fertilizzanti</b>

So bene che voi avventurieri siete sempre in viaggio attraverso North Tyris; non potete rientrare a casa ogni santo giorno e temete che le piante muoiano di sete. Niente paura: innaffiare le coltivazioni è l'ideale, ma i vegetali non moriranno se li trascurate, si limiteranno a crescere più lentamente. In realtà è una gran comodità per le spedizioni prolungate, dato che non rischierete di trovare il raccolto marcito nei campi al vostro ritorno!

Inoltre, è fondamentale ricordare che una semina produce un unico raccolto! I viaggiatori in visita a Yowyn rimangono a bocca aperta quando vedono sradicare alberi da frutto o piante di pomodori dopo la mietitura: sono convinti che continuino a fruttificare all'infinito! Ingenui cittadini che credono che il cibo nasca magicamente sui banchi del mercato, eheh~
{p}
Il concime spesso disorienta i giovani fattori perché il suo effetto non salta subito all'occhio. Dona alla piantina una spinta vitale che ne accelera la maturazione di circa il 10%. L'effetto non è retroattivo e non si accumula con dosi multiple, quindi concimate presto!

{p}
<b>Miglioramento delle Colture e Varietà</b>

Più diventerete esperti nell'agricoltura, più le piante risponderanno al vostro amore e alle vostre cure, diventando più nutrienti, sazianti e preziose al mercato! Potrebbero persino sviluppare qualità particolari che noi chiamiamo "varietà": potreste scoprire che i vostri imo hanno un sapore piccante, o che i pomodori sono diventati straordinariamente croccanti!

Io? Personalmente adoro il collagene abbondante in tutti i miei ortaggi: fa miracoli assoluti per la pelle! Una volta che una varietà compare nella stirpe dei semi, vi rimarrà per sempre! Potete alterarla mescolando le sementi con misture alchemiche come mercurio e sangue di angelo caduto in un mortaio di legno, ma si tratta di ingredienti rarissimi!
{p}
Perfezionare i raccolti richiede dedizione e perizia. Mietere le piante con la falce di persona vi consente di selezionare le sementi migliori a ogni raccolto, velocizzando il miglioramento genetico rispetto a quando delegate il lavoro ai garzoni!

I nefia boschivi e prativi sono incredibilmente fertili: capita che avventurieri con l'occhio lungo scovino macchie di vegetali di qualità sublime che crescono selvatici! Se volete risparmiare tempo per avviare una nuova coltivazione d'eccellenza, perché non cercate qualche buon seme selvatico da cui partire?

Ricordate: le colture raggiungono a un certo punto il vertice della squisitezza, ma anche dopo continueranno ad aumentare di valore e a riempire lo stomaco con porzioni sempre più sazianti! Pensate che una sola mela del mio vicino basta a <i>farcire</i> un'intera torta gigante!

{p}
<b>Alberi e Idroponica</b>

Gli alberi richiedono tempi di crescita più lunghi: gli alberi da frutto necessitano di 40 giorni, gli altri di 30 giorni, a fronte dei 20 giorni tipici della maggior parte delle verdure. Fatto ancor più rilevante, gli alberi adulti piantati su terreno arato rilasciano sempre sementi quando vengono abbattuti. Non avrete bisogno di falciare metà del vostro frutteto per riseminare, il che significa che la resa effettiva pareggia quella delle altre colture! Il doppio del tempo, ma anche il doppio del legname e dei frutti: non è fantastico?

Tuttavia, i lunghi tempi di crescita impongono cautela con l'avvicinarsi dell'inverno se non disponete di lampade solari. Certi sprovveduti di città credono che agli alberi non importi svernare sotto le tempeste di neve. A <i>voi</i> piacerebbe essere lasciati nudi al gelo polare? Certo che no! Raccogliete i semi prima che il gelo ve li porti via!
{p}
L'idroponica viene impiegata solitamente per i cereali come frumento e riso, piantando le sementi direttamente nell'acqua. La coltivazione di alghe profonde sulla terraferma funziona in modo simile: versare tre volte l'acqua da una giara senza fondo creerà la profondità ideale per farle prosperare.

Le colture adatte all'idroponica sono considerate perennemente irrigate. Le altre piante cresceranno comunque, ma senza trarre alcun beneficio da quel regime!

L'agricoltura è una di quelle arti facili da intraprendere, ma difficilissime da padroneggiare appieno. Spero di cuore che la gente non dimentichi mai il legame sacro con la terra, ovunque decidiate di vivere!

***

<i>- Nel nostro prossimo numero parleremo della gestione delegata delle fattorie!</i>
"""

DEFAULT_TXT = """Diario

Da oggi inizierò a scrivere il mio diario!
"""

files_data = {
    'advweek_16.txt': ADVWEEK_16,
    'advweek_17.txt': ADVWEEK_17,
    'advweek_18.txt': ADVWEEK_18,
    'advweek_19.txt': ADVWEEK_19,
    'advweek_20.txt': ADVWEEK_20,
    'advweek_21.txt': ADVWEEK_21,
    'advweek_22.txt': ADVWEEK_22,
    'advweek_23.txt': ADVWEEK_23,
    'advweek_24.txt': ADVWEEK_24,
    'advweek_25.txt': ADVWEEK_25,
    '_default.txt': DEFAULT_TXT,
}

for fname, text in files_data.items():
    p = os.path.join(BOOK_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(text.strip() + '\n')

print("Applied Italian translations for Adventurer's Weekly 16 to 25 and _default.txt")
