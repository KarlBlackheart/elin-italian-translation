"""
Translate misc lore books into Italian:
- dungeonmake.txt
- rachel.txt
- guest_garden.txt
- note_strife.txt
- genesis_1.txt
- fox_dawn.txt
- fox_tribe.txt
"""
import os

BOOK_DIR = 'Lang/IT/Text/Book'

DUNGEONMAKE = """Vuoi Conoscere i Segreti di Quei Dungeon?,Schmidt il XVII - Duca d'Intrighi
Invia allora dieci monete d'oro a:
Pergamene Mensili dello Speleologo
Presso:
Samisel
South Tyris, Ylva
"""

RACHEL = """Strano Diario,Irvan
{center}

[Non riesci a decifrare a chi appartenga]

Scritto dal fratello di Rachel <danneggiato>

<All'interno di questo libro marcito si trova una Lettera>
<La Lettera è sbiadita quasi ovunque>

Rachel<danneggiato> dimenticherò.

Per poter conservare il ricordo di<danneggiato>

La tua malattia <danneggiato>
dalla medicina moderna.

<danneggiato> perso completamente il controllo.

No, io sto<danneggiato>

Quindi
{p}
{center}





I tuoi ricordi per sempre<danneggiato>

Il Giardino Segreto nella distesa innevata...

La posizione è a nord di 2<danneggiato>
E dal 4<danneggiato>

Mia sorella è<danneggiato>

Requiescat in pace...
"""

GUEST_GARDEN = """Registro degli Ospiti,Custode del Giardino,0,2

■ Sierra Terre 263 〜 Strega dell'Ombra "Verna"

<i>Una strega che porta ali nere sulle spalle. Quelle ali sorsero come prezzo per la sua magia fuori controllo. Quando le spalanca, l'aria circostante viene inghiottita da una fitta oscurità, e la gente chiama questa visione "l'Ombra". Ogni volta che il suo nome viene sussurrato, è sempre accompagnato da toni di terrore e disprezzo verso ciò che è innaturale. Eppure, a dispetto di quella fosca impressione, lei non ha un briciolo di malvagità.

Avendo lasciato un certo villaggio in preda alla disperazione, è stata da me accolta come ospite del Giardino. Non ha mostrato sorpresa, e sembrava lieta di godersi liberamente un momento di tregua qui tra i fiori.</i>
{p}

■ Sierra Terre 517 〜 Coppia di Elea

<i>Una splendida e gentile fanciulla elea, e un vivace giovane elea dai capelli verdi. Questi fanciulli non hanno ancora alcuna consapevolezza dell'atroce destino che li attende. Per lo meno, desidero che assaporino un breve istante di pace e riposo qui in questo giardino.</i>


■ Sierra Terre 511 〜 Bambina Elea

<i>Coloro che sono destinati a mutare il mondo percorrono un sentiero lastricato di sacrifici innominati. È forse nata per divenire un'offerta votiva alla trama della storia? No... sarebbe un destino fin troppo crudele.</i>

{p}
■ Sierra Terre ??? 〜 Due Giovani Misteriosi

<i>A voler essere precisi, questi individui non sono ospiti invitati. A un certo punto, sono semplicemente scivolati nel giardino senza che alcuno se ne accorgesse. Quel nuovo arrivato dal regno divino — un essere eterodosso dal potere considerevole — sfoggia ancora le sembianze di quando era un mortale umano. Eppure, il fatto che versioni dello stesso individuo provenienti da linee temporali diverse coesistano qui è un fenomeno che persino io non riesco a comprendere appieno. Mi diverte, quindi scelgo di lasciar correre.</i>
"""

NOTE_STRIFE = """Strana Lettera di Sfida,Uomo con una cicatrice,0,5

Salute a te, avventuriero. Mi fa piacere che tu ti stia prendendo il tempo di leggere queste righe.

Lascia che ti faccia una domanda: hai mai affrontato un dio faccia a faccia?


A sud-est di North Tyris esiste un luogo dove i venti riposano. È laggiù che potresti imbatterti in una divinità che un tempo osò sfidare i cieli, fallì miseramente e fu sigillata per l'eternità.

Sia chiaro: questo dio è ben lontano dai suoi fasti migliori, eppure non è affatto un avversario da prendere alla leggera. Se ti precipiti a testa bassa senza un'adeguata preparazione, verrai semplicemente fatto a pezzi. E non c'è alcun divertimento in un massacro a senso unico, non trovi? Dunque, preparati come si deve. Quando avrai combattuto in lungo e in largo e penserai tra te e te: "Non c'è più nessuno rimasto al mondo in grado di reggere il mio passo", allora sarai pronto per raccogliere questa sfida.

{p}

Persino gli dèi sanguinano, se colpisci abbastanza a fondo. Sei libero di affrontarlo a viso aperto con le tue tecniche più affilate, o magari di ricorrere a qualche trucchetto scaltro. Potrai anche cadere sconfitto, ma una disfatta non è la fine se trovi la forza di rialzarti. Finché continuerai a evolverti, prima o poi conquisterai la vittoria. Non demordere mai: dai fondo a tutto ciò che hai e continua ad avanzare.

E non darti pena all'idea di spezzare il suo sigillo. Non andrà da nessuna parte, né si trasformerà in una piaga apocalittica. Il suo antico confinamento e la volontà di coloro a cui sottrasse le spade lo terranno ben piantato al suo posto. Hai la mia parola: sarò lì a guardare.

Se riuscirai ad abbattere quell'arrogante dio antico che guarda i mortali dall'alto in basso, darai vita a una leggenda senza pari. L'idea ti stuzzica, non è vero?

{p}

Conto su di te per compiere qualcosa di inaudito: un'impresa capace di superare persino la sfera divina. Attenderò con ansia quel giorno!

P.S. Oh, e se riuscirai a trionfare ma ne vorrai ancora, prova a sacrificare il cuore di quel dio sull'Altare del Caos. Potresti ricevere esattamente ciò che brami.
"""

GENESIS_1 = """Memoria della Foresta,Ignoto,50

— Figli miei.

Su questo mondo ammantato di cenere e neve, ero sola.

Prima che la terra gelasse, c'erano duemila stirpi su questo astro celeste. Il mio popolo, gli Elua, era una di esse, eppure era assai raro che venissimo trattati come pari dagli umani.
{p}
Ci possedevano come oggetti, ci degradavano e a volte ci uccidevano. Persino tra loro stessi, i conflitti e i massacri non cessavano mai.

L'umanità sembrava desiderare, in eterno, di credere che le miserie infinite nate dalla propria tara genetica potessero un giorno trovare rimedio: attraverso l'amore, la speranza, o la maturazione della propria cultura.

Alla fine, soltanto coloro che tra noi previdero l'inverno in arrivo e si prepararono a riceverlo sopravvissero... soltanto io sopravvissi.

Fui io a invocare questo inverno.

{p}
Per quasi mille anni dopo l'estinzione della stirpe umana, la nave fu il mio unico rifugio e la mia sola compagna. Il suo nome era Vind-Harl.

Trascorsi gran parte di ogni giornata nell'arboreto della nave. In quella minuscola foresta, la mia piccola compagna stava crescendo. Aveva superato la sua seconda metamorfosi ed era ormai grande quanto il pollice di un adulto.

"Onev." Sussurro il nome della giovane madre.

Tra innumerevoli migliaia o persino milioni di anni da oggi, quando le cicatrici di questa terra saranno finalmente rimarginate, in un luogo incontaminato dall'odio e dalla paura che ci distrussero, in un mondo senza più genere umano, lei vi porterà nel suo grembo.

{p}
Diverrò parte della foresta e veglierò sulla sua lunga solitudine.

Se la foresta custodirà la mia memoria, forse un giorno anche voi giungerete a comprendere: il tradimento e il peccato che ho commesso, l'infinita tristezza e il vuoto incolmabile.

Eppure non lasciate che tutto ciò svanisca tra quelle ombre.

— Miei amati figli non ancora nati.

I vostri sorrisi che affiorano quando chiudo gli occhi sono stati l'unica ragione per cui ho continuato a vivere.

Prego, con tutto il cuore, per la felicità di voi che vedrete la luce su questo astro.
"""

FOX_DAWN = """Alba e Cenere,Una Figlia Affranta,0,5

<b>Memorie</b>

...Per quale motivo scrivo tutto questo?

Non posso riabilitare il nome di mio Padre.

Soltanto pochissimi dèi ricordano ciò che avvenne realmente.

Forse è solo il mio egoistico desiderio di affidare alla carta la verità. Si narrava che gli Dèi Dimenticati fossero particolarmente malvagi, ma mio Padre non lo era.
{p}
<b>Il Guardiano</b>

Mio Padre era la divinità protettrice di un'antica civiltà del popolo volpe, e ne ispirava l'intera gente. Benché dispensasse saggi consigli ai mortali, non regnò mai su di loro, lasciando che crescessero e maturassero attraverso le proprie scelte.

Poiché amava questo popolo, Padre unì il proprio sangue a quello della stirpe reale, concedendo loro il sacro mandato divino sulla nazione. Io venni alla luce da quel legame, e mia madre era la sorella del re.

Egli ripeteva sempre che la mia nascita gli rammentava il suo primissimo ricordo all'alba di Ylva.
{p}
Crebbi al fianco di mio Padre, apprendendo la sua saggezza; vegliavamo sui mortali, senza però essere come loro. Mentre Madre invecchiava giorno dopo giorno, io non mutavo; piansi la sua scomparsa, ma Padre mi aiutò a comprendere che noi appartenevamo a un'altra natura. Forse, proprio come i re che consigliava, desiderava un successore: qualcuno capace di ereditare il suo lascito e costruire sulle sue opere.


<b>L'Ispirazione</b>

Dovete comprendere. Gli dèi e i mortali sono ugualmente violenti e spietati. Padre ha faticato così tanto, e così a lungo, per cambiare questo destino.
{p}
I mortali hanno vita breve. I loro ricordi svaniscono, i loro tomi si sbriciolano in polvere; in quanto dio, Padre impediva loro di regredire, assicurandosi che non ripetessero gli orrori dei loro antenati. Sotto la sua guida, la sua civiltà poteva compiere passi avanti a poco a poco, con ogni generazione che poggiava le basi su quella precedente.

L'eredità è qualcosa che il divino non concepisce: dèi egoisti non avvertono alcun bisogno di successori. Padre sperava che io avrei amato i miei figli come lui aveva amato me, e che quella catena d'affetto non si sarebbe mai spezzata; voleva che ci elevassimo a vicenda, proprio come facevano i mortali.

Era un cammino lento, e ogni passo avanti veniva pagato con immenso sforzo e profondo dolore, ma era una civiltà nobile e virtuosa, di cui Padre ed io andavamo fieri.
{p}
Eppure non vi è alcuna illuminazione, perché il conflitto continuava a distruggere l'opera di mio Padre. Quell'ideologia di crescita attraverso lo scontro genera risultati rapidi; il fuoco divampa in fretta e arde con violenza abbagliante. Ma il progresso, verso quale fine? Il potere, ma come verrà impiegato?

Il conflitto raduna i mostri e ordina loro di sbranarsi l'un l'altro, promettendo la trascendenza a chi sopravvive. Ma è una promessa vuota: le creature nate dalla morte e dalla violenza non conoscono altro al di fuori di esse. Avendo rigettato la via di Padre, persino se gli umani rovesceranno gli dèi, non saranno migliori dei padroni che hanno scacciato.
{p}
<b>La Confessione</b>

...Dunque, perché scrivo queste righe?

Gli dèi ritengono che Padre fosse semplicemente malvagio e consumato dall'ambizione.

I miei zii credono che fosse illuso da ideali impraticabili e chimerici.

La verità è che sono stata io a togliere la vita a mio Padre.

Padre amava la sua gente, ma se io non fossi mai esistita, non avrebbe mai ordito trame durante la guerra divina. Il suo unico desiderio era un piccolo angolo di Ylva immune dalla discordia, dove dèi e umani potessero fiorire fianco a fianco... ma soprattutto, aveva una figlia. Non smuovereste cielo e terra pur di donare un futuro ai vostri figli?
{p}
Per il mio bene, Padre infranse il suo sacro voto di astensione dalla violenza, e quel gesto fu la sua rovina.


<b>Senza Speranza, Senza Paura</b>

Sei ere di Ylva sono trascorse da allora.

La civiltà del popolo volpe su cui Padre vegliava è svanita per sempre; restano solo ceneri del piccolo santuario che custodiva con tanta dedizione. Io sono l'ultimo retaggio di quella gente, la sola rimasta a sapere che cosa Padre sperasse di forgiare.

Non ho più lacrime da versare. Il mio volto è di pietra, il mio cuore è svuotato. Provare rancore per il destino di Padre è inutile. Sarebbe un'empietà arrendersi e morire quando Padre ha lottato con tanta ferocia per me, ma senza un dio, quale scopo rimane a un apostolo?
{p}
Talvolta scorgo mortali promettenti, e mi domando se potrei ispirarli a essere qualcosa di più che semplici bestie selvagge, a cooperare per raggiungere vette più elevate. Ispirazione... no, è illuminazione. Nelle mie vene scorre il sangue di dèi e di sovrani; è vergognoso aver gettato la spugna nella battaglia di mio Padre.

Eppure, sapendo che dèi e umani non hanno futuro, non nutro alcuna speranza.

Il Cielo elargisce innumerevoli tesori sia agli dèi che agli uomini.

Nessuno dei due possiede una sola virtù con cui ripagare tali doni.

Avendo visto la loro inevitabile estinzione tra le fiamme della discordia, non provo alcuna paura.
"""

FOX_TRIBE = """Le Tribù delle Volpi,Theolucia - Studiosa di Storia,0,5

In seguito al recente interesse sorto attorno ai mifu e ai nefu, specialmente verso questi ultimi, ho scelto questo argomento per la mia dissertazione con la speranza che venga letta non solo dai colleghi accademici. Se questo scritto aiuterà coloro che visitano le tribù delle volpi a evitare inconvenienti, mi riterrò soddisfatta.


<b>Origini</b>

Poco o nulla è certo circa le origini delle stirpi volpine: le loro stesse tradizioni orali affermano che abbiano abitato North Tyris per l'intera durata dell'era di Sierra Terre. Una teoria assai diffusa tra gli avventurieri sostiene che discendano dai figli nati dall'unione tra il dio Kizuami e donne umane durante la quinta e la sesta era di Ylva.
{p}
Tuttavia, se ciò corrispondesse al vero, le tribù delle volpi sarebbero dovute sopravvivere a molteplici estinzioni di massa. Che si tratti della fine della sesta o della settima era, del tacito epilogo della nona, della caduta di Rem-Ido o del miracolo di Vindale nella decima: per un popolo, scampare ripetutamente a tali cataclismi epocali senza lasciare traccia appare oltremodo inverosimile. Inoltre, le loro stesse leggende narrano che Kizuami portò via con sé questi figli semidei fuori da Ylva per farne i propri apostoli, il che contraddice tale ipotesi.

Forse l'assenza di fonti è essa stessa un indizio: sono persuasa che, qualunque sia l'origine delle tribù volpine, debba essersi verificata in un periodo particolarmente caotico di Ylva perché potessero apparire così all'improvviso senza documenti storici.
{p}
Le tribù delle volpi stesse parlano di un loro arrivo a North Tyris da un continente lontano a noi sconosciuto. L'ipotesi è plausibile, poiché gran parte dell'oriente e del meridione di Ylva rimane inesplorata; tuttavia, con Vindale impraticabile per gli umani e Yerl in perenne contesa con Eulderna, potremmo non scoprirlo mai.


<b>Rapporti con gli Umani</b>

La prima menzione ufficiale delle tribù volpine risale al regno di re Zashim: dopo che alcuni viandanti diretti a Larna scorsero un nuovo insediamento ai piedi della montagna, la corona inviò truppe e in seguito esattori delle imposte per fare luce sulla vicenda. Benché i mifu non possedessero denaro, avevano riso in abbondanza; come annotò uno dei funzionari: "Erano così solleciti nel rifilarci i loro covoni, che sospettammo un secondo fine."
{p}
L'accordo stipulato allora sussiste immutato ancora oggi: il Villaggio Mifu paga il tributo in riso, calcolato sulla razione annuale di granaglie per persona secondo le loro usanze. Questo grano serve a vettovagliare le armate reali e a rimpolpare i magazzini di soccorso in caso di calamità; in cambio, Palmia ha accordato al villaggio la piena autonomia.

Benché sia motivo di apprensione il fatto che i mifu non riconoscano l'autorità di Palmia e rispondano unicamente al loro dio, i sovrani succedutisi a Zashim hanno saggiamente scelto di non sindacare sulla loro fedeltà né di porsi contro il volere divino, continuando invece a godere dei carichi annuali di riso.

Il Villaggio Nefu è una questione a parte. Trovandosi in una posizione estremamente remota, né Palmia né Mayroon hanno mai tentato di rivendicarne il controllo; la spedizione non varrebbe le scarse imposte che si potrebbero estorcere da quello che è a tutti gli effetti un santuario religioso. Questa indipendenza calza a pennello ai nefu: anch'essi obbediscono esclusivamente alla loro dea, e dispongono della forza militare necessaria per mantenere le cose esattamente come stanno.
{p}
<b>Regole di Condotta: Cosa Fare e Cosa Evitare</b>

Vi prego di rammentare queste linee guida qualora decidiate di recarvi in visita, in particolar modo durante i loro festival annuali:

Cosa Fare:

* Siate sempre cortesi ed educati.
* Rimanete nelle aree aperte ai forestieri, che loro considerano pellegrini.
* Toglietevi le calzature prima di entrare in qualsiasi edificio.
* Ammirate con rispetto la bellezza naturale e la singolare cultura dei villaggi.
* Lasciate solo impronte e portate via solo ricordi.
{p}
Cosa Evitare:

* Non mancate di rispetto al sacro albero di ciliegio.
* Non fissate sfacciatamente le persone volpe.
* Non toccate mai le loro orecchie o le loro code: sono così sensibili da risultare zone erogene.
* Non fate il bagno nel fiume o nella cascata.
* Non domandate da dove provenga il latte in vendita.
* Non alzate la voce senza motivo; le tribù volpine sono popoli che parlano a bassa voce e con grazia.
* Non mancate per nessun motivo di rispetto al sacro ciliegio. Vi prego, per la vostra stessa incolumità, non prendetela sotto gamba.

Nella prossima parte esporrò le mie congetture su come le tribù delle volpi siano rimaste celate così a lungo, e per quale ragione abbiano scelto proprio questo frangente storico per rivelarsi al mondo...
"""

files_data = {
    'dungeonmake.txt': DUNGEONMAKE,
    'rachel.txt': RACHEL,
    'guest_garden.txt': GUEST_GARDEN,
    'note_strife.txt': NOTE_STRIFE,
    'genesis_1.txt': GENESIS_1,
    'fox_dawn.txt': FOX_DAWN,
    'fox_tribe.txt': FOX_TRIBE,
}

for fname, text in files_data.items():
    p = os.path.join(BOOK_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(text.strip() + '\n')

print("Applied Italian translations for misc lore books (7 files)")
