"""
Translate deity lore books into Italian:
- forgotten_gods_1.txt
- deity_moonshadow.txt
- deity_strife.txt
- deity_trickery.txt
"""
import os

BOOK_DIR = 'Lang/IT/Text/Book'

FORGOTTEN_GODS_1 = """Gli Dèi Dimenticati Volume 1,Eureka - Fomentatrice della Discordia,0,5

Gli dèi dimenticati, noti anche come dèi sbiaditi o divinità del crepuscolo, erano entità celesti che si opposero ai Pilastri durante le guerre divine della terza e della sesta era di Ylva. Quei conflitti cataclismici rimodellarono la superficie del pianeta, diedero origine all'Eterno Patto e condussero Lord Yevan sul suo sentiero attuale.

Poiché comprendere il proprio nemico costituisce metà della vittoria, egli mi ha ordinato di stilare una cronaca di queste divinità, dei loro precetti e delle loro motivazioni, affinché né loro né i loro eredi possano colglierci impreparati in quest'era di tumulti. Conosci il nemico e conosci te stesso, e uscirai vittorioso da cento battaglie.

{p}
<b>Yufu</b>

Un tempo celebrato come Yufu dell'Ispirazione, questa divinità è stata quasi interamente obliata tanto nel mondo mortale quanto in quello divino. Benché si fosse schierato contro i Pilastri durante la seconda guerra divina, non prese mai parte agli scontri diretti sul campo di battaglia.

Yufu fu il dio patrono di una modesta civiltà su Ylva durante la quinta e la sesta era, e insegnava ai suoi discepoli a:

* Ricercare la perfezione in ogni cosa — nessun difetto è troppo insignificante per non essere emendato.
* Costruire sulle opere del prossimo, raggiungendo traguardi preclusi al singolo individuo.
* Trarre ispirazione da tutto ciò che esiste, nutrendo speranza per sé stessi e per le generazioni future.
* Rifuggire la violenza e il conflitto — la sopraffazione, per quanto giusta, macchia per sempre l'anima.
{p}
I fedeli più zelanti di Yufu, "illuminati" da tale ispirazione, sostenevano che togliere la vita persino per legittima difesa costituisse peccato mortale.


<b>L'Illusione</b>

Benché a un primo sguardo appaiano innocui seppur ingenui, a un esame più attento questi precetti si rivelano profondamente perniciosi e insidiosi.

La perfezione è un miraggio irraggiungibile. Non esiste un simile stato: dobbiamo costantemente lottare e crescere, oppure soccombere restando indietro rispetto agli altri. Né esiste una perfezione universale: una strategia infallibile contro un avversario può rivelarsi fallimentare contro un altro.
{p}
Una crescita lenta e graduale può apparire ragionevole, ma all'atto pratico è del tutto impraticabile; il ritmo di avanzamento è insufficiente e si riduce a una sterile stagnazione. Sebbene non neghi che la civiltà di Yufu abbia conosciuto un certo fulgore, ciò fu dovuto unicamente al suo isolamento geografico e alla protezione di un dio. Una volta rimosse tali tutele, fu rapidamente surclassata e spazzata via dalla concorrenza delle altre genti.

Il pacifismo assoluto è così alieno dalle dure realtà di Ylva da rasentare il delirio mentale. Persino qualora ammettessi che violenza e lotta corrompano l'animo — cosa che, seguendo Lord Yevan, ovviamente non condivido —, le conseguenze del <b>non</b> intervenire sarebbero infinitamente più disastrose. Questa non è pace: è un'ipocrita inerzia di fronte al male.
{p}
Per quanto suonino nobili, gli insegnamenti di Yufu sono vaneggiamenti idealistici privi di qualsiasi ancoraggio alla realtà. La nostra visione del campo di battaglia deve restare lucida, imparziale e scevra da pie illusioni.

Annoto con cupa soddisfazione che, schierandosi con gli dèi dimenticati durante la seconda guerra divina, Yufu obbedì alla lettera ma calpestò lo spirito stesso della propria dottrina.

Per queste ragioni, un dio che veniva simboleggiato dall'alba dorata viene oggi, per ironia della sorte, annoverato tra le divinità del crepuscolo.

{p}
<b>Annotazioni</b>

Raccogliere testimonianze su questo argomento è stato oltremodo estenuante, poiché quasi ogni memoria di Yufu è andata dispersa; soltanto le tribù delle volpi ne serbano il ricordo, ma rifiutano categoricamente di parlarne in dettaglio. Conclusa la mia indagine, sono convinta che qualsiasi prova dell'esistenza di Yufu non custodita dalle tribù volpine sia stata deliberatamente cancellata nel corso delle ultime ere di Ylva.

Il mio sospetto è che, in cambio della promessa che i Pilastri non avrebbero revocato il dominio di Yufu gettando pubblica vergogna sul suo casato, i suoi fratelli abbiano convenuto di risolvere la questione tra di loro, mantenendola un affare puramente privato di famiglia.

Degno di nota è anche il fatto che Yufu ebbe una sola apostola: sua figlia, una "volpe celeste a nove code". Sebbene non vi siano tracce certe di lei, alcuni viaggiatori con cui ho conferito hanno riferito dicerie sull'avvistamento di una simile creatura nei pressi dell'albero sacro. Benché io stessa non abbia trovato riscontri, l'eventualità della sua sopravvivenza non può essere scartata a priori.
"""

DEITY_MOONSHADOW = """Divinità Minori: Ombra Lunare,Theolucia - Studiosa di Storia,0,5

Dea dei nefu che predilige il canto e la danza, Horome è la sorella minore del dio dei mifu, Kizuami. L'interesse verso la stirpe dei nefu è cresciuto notevolmente di recente, e con esso la devozione a Horome per il suo portamento materno ma al contempo etereo. Non è difficile comprenderne il motivo: la dea dei nefu condivide svariati tratti superficiali con Ehekatl, e potrebbe aver beneficiato del predominio della Dea della Fortuna nell'odierno panorama religioso.
{p}
<b>La Dea dei Nefu</b>

Al pari di suo fratello, Horome è una divinità legata alla stirpe: la quasi totalità dei nefu la venera. Secondo le loro memorie, è una dea timida e riservata, che talvolta assume sembianze mortali per mescolarsi alla gente comune, senza però trattenersi a lungo poiché detesta la menzogna. La raffigurazione della danza con la spada sotto la luna di Horome rappresenta la quintessenza della dea: un quadro di bellezza struggente e tragica raramente intravisto dai fedeli, e poi immortalato in opere d'arte d'ispirazione divina.

Horome trasmette ai suoi discepoli questi precetti:

* Che la forza è inseparabile dalla grazia e la forma dalla funzione,
* Che la maternità e i bimbi felici sono doni sacri da custodire con cura,
* Que la saggezza non risiede solo nello studio solitario, ma nell'esperienza pratica del mondo,
* Che ciò che possediamo non ci appartiene per capriccio personale, ma ci è affidato in custodia per le generazioni future.
{p}
Gli insegnamenti di Horome sono modellati specificamente per il popolo nefu; per fare un esempio, la sua insistenza sui bambini appare ovvia considerando che i nefu sono longevi e generano prole con estrema lentezza. L'enfasi sull'applicazione pragmatica fa sì che ogni momento dell'esistenza dei nefu si tramuti in un atto di culto: una fede vissuta istante per istante, piuttosto che una cerimonia settimanale in un tempio. I nefu si sforzano di rendere sé stessi e l'ambiente circostante armoniosi per i sensi, rispecchiando l'incantevole bellezza di Horome.

A differenza dei mifu, il ruolo di sacerdotessa non è ereditario per via di sangue. La nuova guida viene scelta tra le giovani fanciulle che incarnano l'ideale della grazia espresso dalla loro dea: una donna che abbia padroneggiato sia le arti marziali che quelle estetiche, che abbia dato alla luce (o sia pronta a donare) molti figli, e che possieda una solida esperienza di vita con il mondo e la gente comune.
{p}
<b>Le Danze con la Spada</b>

Nel cuore pulsante del culto di Horome risiedono le danze con la spada: eseguendo le figure rituali e rievocando le storie tramandate, chi danza assume il ruolo della dea e rivive il passato attraverso i suoi occhi. Per questo motivo, ogni danza con la lama dei nefu è un sacro rito liturgico; sebbene i movimenti tradiscano radici nell'arte della scherma, le movenze hanno una valenza squisitamente scenica e devozionale.

Accompagnate dalla musica, quasi tutte le danze vedono una sola protagonista alla volta, con l'eccezione straordinaria dei festival di paese in cui l'intero villaggio prende parte all'esecuzione. Nessun dettaglio viene trascurato: dalla lunghezza della lama alle vesti cerimoniali, sino alla cura minuziosa della persona, poiché la danzatrice si fonde con la leggenda narrata dalla melodia.
{p}
Attraverso la danza con la spada, i nefu apprendono la propria storia e il folclore sperimentandoli in prima persona: un metodo perfettamente in sintonia con gli insegnamenti di Horome, assai simile alle tradizioni orali di certe tribù Juere nel South Tyris. L'attuale sacerdotessa e la sua apprendista designata hanno il dovere di padroneggiare ogni singola danza conosciuta, trasmettendone poi i passi agli altri nefu all'occorrenza.

In quanto storica, ritengo motivo di apprensione che un patrimonio culturale simile poggi sulle spalle di due sole persone e quanto facilmente possa svanire nel nulla. I nefu mi hanno replicato che ogni danza discende direttamente da Horome ed è stata loro concessa per rivelazione divina — tesi credibile, giacché le danze umane appaiono rigide e legnose al confronto. Qualora accadesse una disgrazia, la dea si limiterebbe a rivelare nuovamente la sua arte sacra.

Una devozione tanto incrollabile suscita sincera ammirazione, eppure, da accademica, una simile spiegazione non riesce a chetarmi del tutto l'animo...
"""

DEITY_STRIFE = """Divinità Minori: Discordia,Theolucia - Studiosa di Storia,0,5

Ben poco si conosce attorno al dio della discordia. Sebbene Yevan sia un'antica divinità che si narra abbia preso parte alle guerre contro gli Dèi Dimenticati, i tomi giunti fino a noi che ne riportano il nome sono incredibilmente rari. Eppure, man mano che i conflitti dilagavano sulla scia dello scontro tra Zanan ed Eulderna e con la fondazione di Yerl, la venerazione per Yevan ha progressivamente radunato proseliti tra rivoluzionari radicali e sette militariste nel corso degli ultimi secoli.

In netto contrasto con Opatos, ampiamente riverito da guerrieri e soldati d'ordinanza, coloro che inneggiano a Yevan vengono spesso trattati alla stregua di eretici o pericolosi fanatici. Il suo credo non è mai divenuto una fede di massa, eppure si distingue per un ardore feroce, insolito persino tra i più devoti.
{p}
<b>Il Dio Solitario del Conflitto</b>

A differenza di quasi tutte le altre divinità minori, Yevan non vanta una razza prediletta, non ha ordini religiosi unificati né un clero istituzionalizzato. Né il dio in persona sembra dare grande peso all'estensione della propria influenza terrena. Semmai, appare infinitamente più affascinato dalle vicissitudini e dalla tempra dei mortali.

Yevan impartisce un unico, categorico precetto a chiunque ricerchi la sua benevolenza:

<i>Supera le tue prove. Il cammino che intraprendi appartiene soltanto a te.</i>

Una tale concisione è assai insolita nel pantheon. Da questa solitaria massima, tuttavia, si può evincere il cuore della dottrina di Yevan: egli esorta i mortali a forgiare la propria natura, ad avanzare sospinti dalla ferrea convinzione e a temprare il proprio spirito attraverso la lotta incessante.
{p}
<b>Fosche Dicerie</b>

Per approfondire la questione, ho raccolto diverse testimonianze e leggende che potrebbero ricollegarsi al dio della lotta:

- Dove Riposano i Venti

Si mormora dell'esistenza di un recesso appartato nel continente di Tyris dove uno degli Dèi Dimenticati, ormai spogliato dei suoi poteri, giace confinato da catene arcane. Il luogo sarebbe sorvegliato da un misterioso custode legato a doppio filo a Yevan. Molti sostengono che questa figura valuti con occhio inflessibile i viandanti di passaggio, in cerca di un campione abbastanza possente da abbattere ciò che riposa oltre il sigillo.
{p}
- I Sacelli della Prova

Nelle profondità recondite di certi nefia sorgono santuari sinistri che evocano orrori abissali al minimo contatto. La loro foggia presenta un'inquietante somiglianza con i simulacri del culto di Yevan risalenti alla Sesta Era. Se si sposa la dottrina secondo cui la contesa con il forte è essa stessa una prova da superare, tali altari potrebbero celare un frammento tangibile del potere del dio.

- Il Gladiatore del Sogno

Un celebre campione di Karune amava vantarsi che "nessun essere vivente potesse rivaleggiare con la sua possanza". Poco tempo dopo, cominciò a sognare ogni notte un viandante incappucciato e sfregiato da una vistosa cicatrice, avvolto in abiti arcaici: un rivale che lo sfidava implacabile a ogni tramonto, sconfiggendolo immancabilmente a ogni duello. Gli scritti superstiti affermano che la superbia del guerriero fu frantumata da quegli incubi, e che da allora egli ascese a vette di maestria marziale mai toccate prima.
{p}
- I Soldati Svaniti nel Nulla

Durante il sanguinoso conflitto tra Zanan ed Eulderna, molti soldati di Zanan votati a Yevan combatterono in prima linea. Tra coloro che si distinsero per il coraggio più brutale cadendo gravemente feriti, alcuni svanirono senza lasciare alcuna traccia il mattino seguente. I commilitoni di ambo gli schieramenti mormoravano che il signore della discordia avesse accolto nel suo reame i combattenti da lui prediletti.

Non esistono prove inoppugnabili a sostegno di questi racconti. Tuttavia, se ipotizziamo che anche una sola parte corrisponda a verità, emerge una costante inequivocabile: Yevan ricerca senza sosta coloro che sfidano i propri limiti, avanzano e continuano a evolversi.

Per la massa, il dio della lotta è solo un eretico araldo di massacri. Ma per i suoi devoti egli incarna ben altro: uno spietato eppur partecipe sostenitore dei mortali, animato da una fede assoluta nel loro potenziale sconfinato.
"""

DEITY_TRICKERY = """Divinità Minori: Inganno,Theolucia - Studiosa di Storia,0,5

Sebbene i sette Pilastri siano venerati in ogni angolo di Ylva e attirino le devozioni più solenni, esistono divinità minori che operano al loro fianco, venerate da cerchie più ristrette di fedeli e preposte a domini più specifici.

In questo saggio intendo illustrare ai lettori i culti minori del nostro mondo.
{p}
<b>Il Dio dei Mifu</b>

Kizuami dell'Inganno è indiscutibilmente la divinità patrona del popolo mifu; la quasi totalità dei mifu lo venera con devozione, mentre ben pochi al di fuori delle tribù volpine ne professano la fede. Non si pensi che egli non intervenga nelle vicende terrene: la sua mano opera con discrezione e rifugge ogni plateale ostentazione di sacralità.

Agli adoratori di Kizuami viene insegnato:

* A vivere l'esistenza in ogni sua ricchezza, cercando esperienze inedite senza mai lasciarsi cogliere dal tedio,
* Ad accogliere le benedizioni così come le disgrazie, consapevoli che nessuna delle due è eterna,
* A non disprezzare le proprie imperfezioni, bensì a tramutarle nei propri punti di forza,
* A essere ingegnosi e a ridare lustro e utilità a ciò che sembra rotto o inservibile,
* A comprendere che mutando sguardo e condotta, persino dalla sventura più cupa può sbocciare una preziosa opportunità.
{p}

<i>"Non vi è estate che duri in eterno."</i> Secondo le memorie delle volpi, Kizuami pronunciò queste esatte parole mentre toglieva la vita a suo fratello Yufu; eppure i mifu d'oggi preferiscono recitare questo detto:

<i>"Non c'è vita senza morte, né paradiso senza abisso; non v'è incontro senza separazione, né gaudio senza dolore."</i>

In fondo, è la saggezza di un dio che ha dimorato in mezzo ai mortali, ne ha contemplato le nascite e i funerali, ne ha condiviso le passioni e ha abbracciato la caducità del loro respiro. Un dio che non ha tentato di strappare altro tempo per i propri beniamini, bensì ha fatto tesoro di ogni palpito trascorso insieme; una divinità che non si è rattristata nel vedere spegnersi le loro fiammelle, ma si è meravigliata di quanto intensamente sapessero brillare.
{p}
È questa — o perlomeno tale è la convinzione dei mifu — la disposizione d'animo che un dio deve possedere per comprendere appieno la ricchezza che appartiene ai mortali nella loro breve stagione. Nei nostri miti sui Pilastri, le divinità rimangono sconvolte dalla morte e dal distacco — si pensi a Itzpalt e Odina, o a Kumiromi ed Ehekatl — e, a parte le grandi guerre della terza e sesta era, perdono raramente i propri pari. Ma perché un essere celeste possa accostarsi ripetutamente a creature effimere, è indispensabile saper accettare la perdita. Dietro l'aria scanzonata e beffarda dell'Ingannatore si cela una stoica malinconia, che gli consente di sorridere anche di fronte alle tragedie di Ylva; molti miti narrano delle sue molteplici incarnazioni nel mondo mortale in cerca dell'amore.

Tematiche affini si riscontrano nel culto di Kumiromi, legate però al ciclo della vita, della morte e della rinascita della natura, laddove Kizuami abbraccia le corde più intime dello spirito e dei legami umani.
{p}
<b>Il Riso Sacro</b>

Il riso riveste un'immensa valenza sacrale per i mifu; le offerte votive per Kizuami comprendono pasta di riso, sakè e mochi freschi. Il Villaggio Mifu produce quantità sbalorditive di cereali con molteplici mietiture ogni anno, attribuendo tale abbondanza alla benevolenza celeste.

Non vi è un nesso immediato tra il cereale in sé e i dogmi teologici di Kizuami, eppure il riso è circondato da una devozione solenne ed egli viene costantemente effigiato con spighe mature tra le dita. Ho osservato i mifu prendersi cura delle risaie: ogni gesto, dalla semina al raccolto, viene eseguito con silenziosa concentrazione, come se partecipassero a un sacro rito. Anzi... vedendo la loro sacerdotessa affaticarsi nel fango e avvertendo una strana risonanza nell'aria, sono persuasa che l'intera comunità stesse tessendo una grandiosa liturgia invisibile ai miei occhi.
{p}
C'è forse un potere arcano nel riso? Nel gesto stesso di coltivarlo? O nella terra in cui affondano le radici? Non so dare risposta a ciò che ho percepito, se non che l'influsso di una divinità era all'opera. Più tardi sono stata invitata alla loro festa e ho osato porre qualche domanda alla sacerdotessa, ma ne sono uscita con dubbi ancora maggiori.

A ripensarci oggi, fatico persino a rammentare cosa mi abbia risposto di preciso...
"""

files_data = {
    'forgotten_gods_1.txt': FORGOTTEN_GODS_1,
    'deity_moonshadow.txt': DEITY_MOONSHADOW,
    'deity_strife.txt': DEITY_STRIFE,
    'deity_trickery.txt': DEITY_TRICKERY,
}

for fname, text in files_data.items():
    p = os.path.join(BOOK_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(text.strip() + '\n')

print("Applied Italian translations for deity books (4 files)")
