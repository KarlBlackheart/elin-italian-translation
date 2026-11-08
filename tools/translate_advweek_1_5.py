"""
Translate Adventurer's Weekly 1 to 5 into Italian.
"""
import os

BOOK_DIR = 'Lang/IT/Text/Book'

ADVWEEK_1 = """Settimanale dell'Avventuriero N. 1: I Nefia e Voi,Caporedattore Hans,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Per il nostro numero inaugurale discuteremo della ragione primaria che spinge voi avventurieri a esplorare North Tyris: i nefia.

I "Nefia" sono le vestigia sotterranee di civiltà estinte che custodiscono ricchezze indicibili e saperi dimenticati. A North Tyris queste rovine vengono continuamente scoperte e re-inghiottite dai moti tellurici, generando un numero inesauribile di dungeon pronti a svelare i propri misteri agli esploratori più audaci.

Sebbene i nefia varino enormemente l'uno dall'altro, dopo aver intervistato numerosi veterani possiamo confermare alcune caratteristiche comuni a ciascuno di essi:
{p}
<b>Livello di Pericolo</b>
Un nefia di livello elevato cela pericoli letali, ma anche bottini di gran lunga più ricchi. Questa correlazione non è tuttavia matematica: moltissimi avventurieri sono stati colti alla sprovvista da creature feroci comparse persino in rovine di basso rango.

<b>Profondità</b>
I nefia si sviluppano generalmente su una profondità variabile tra i due e i cinque livelli. A ogni piano disceso, il livello intrinseco del nefia aumenta di un grado.

<b>Il Padrone del Dungeon</b>
Sul fondo di ogni nefia si annida il suo signore: un mostro titanico che vigila gelosamente sui propri tesori.

I veterani raccontano che, per quanto temibili, i padroni dei nefia tengono sopra ogni cosa alla sacralità della loro tana: se un avventuriero abbandona il piano più profondo, il signore del dungeon coglierà l'attimo per fuggire portando con sé il bottino, consapevole che la sua dimora non è più inviolata.
{p}
<b>Localizzare i Nefia</b>
Il continuo mutare dei nefia a North Tyris scatena una vera e propria corsa contro il tempo tra gli avventurieri per scoprire ed esplorare le rovine prima che sprofondino nuovamente nell'oblio. Le librerie locali vendono mappe tracciate in fretta e furia per i nefia vicini, mentre i mercenari si scambiano soffiate nelle locande.

Alcune regioni, come l'area a nord di Palmia, sono particolarmente soggette ai sismi che dissotterrano nuovi dungeon: gli esploratori perlustrano costantemente l'orizzonte con cannocchiali e binocoli sperando di avvistare siti degni d'essere saccheggiati.
{p}
<b>Tipologie di Nefia</b>

*Rovine Ancestrali: Sobrie e lineari, considerate il nefia per antonomasia. Grandi quantità di pietra possono essere ricavate smantellando pareti e pavimenti. Relitti frequenti e trappole disseminate ovunque.

*Praterie e Foreste: Lussureggianti e verdeggianti, brulicanti di fauna selvatica. Poche trappole, ma i predatori ricompaiono con estrema rapidità. Essendo all'aperto, il ciclo giorno-notte e le condizioni meteo restano attivi.

Vi si rinvengono legni rari e liane sulle pareti rocciose. I minerali affiorano sotto forma di massi. Gli agricoltori esperti possono scovare macchie di colture selvatiche d'altissima qualità.

*Caverne e Miniere: Ricche di vene metalliche e gemme incastonate nelle pareti. Gli speroni di roccia e le stalagmiti possono fruttare pietre pregiate. Assicuratevi di avere ampio spazio nello zaino!
{p}
*Machinarium: Resti tecnologici di antiche civiltà perdute. Curiosamente non presentano una concentrazione superiore di mostri meccanici.

Rottami di rame, ferro e cromite si ricavano smantellando pavimenti e pareti metalliche. Versamenti chimici possono essere raccolti come reagenti liquidi e frammenti di vetro fusi per la lavorazione. Certi esploratori vi trascorrono settimane intere.

*Rovine Sommerse: Si celano nei fondali oceanici e differiscono radicalmente da qualunque altro nefia. La respirazione subacquea è obbligatoria: una torcia intagliata in legno corallino basterà per cominciare, ma pozioni e artefatti offrono soluzioni di gran lunga superiori.

Il nuoto influenza la velocità tra il -50% e il +25%: nefia di livello superiore richiedono una perizia natatoria ben più affinata. I mostri marini sono perfettamente a proprio agio nell'acqua. Attenzione: chi cavalca subisce una penalità raddoppiata se sia la cavalcatura che il cavaliere sono pessimi nuotatori!
{p}
Tra le risorse degne di nota figurano corallo, alghe abissali, zolfo, pietre rare e legnami corallini. Le vongole giganti possono racchiudere perle e tesori inaspettati.


Se un nefia si rivela troppo arduo per le vostre forze, non esitate a battere in ritirata: la pelle viene prima di tutto. Finché siete vivi, vi saranno sempre mille altre avventure ad attendervi.

***

<i>- Nel numero della prossima settimana approfondiremo nei minimi dettagli il concetto di potenziale!</i>
"""

ADVWEEK_2 = """Settimanale dell'Avventuriero N. 2: Risvegliare il Tuo Potenziale,Caporedattore Hans,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


In questo numero esploreremo a fondo il concetto di potenziale e come esso influenza la vostra crescita.

Vi è mai capitato di avere la sensazione di progredire a rilento in un'abilità o in un attributo, a dispetto delle ore trascorse ad allenarvi? Con ogni probabilità la colpa è del vostro potenziale trascurato.

In parole povere, il potenziale determina la velocità con cui migliorate: un avventuriero con 200 di potenziale cresce al doppio della rapidità rispetto a uno con 100. Ciò significa dimezzare tempo e fatica!
{p}
<b>Le Forme di Potenziale</b>

Sia le abilità che gli attributi possiedono due forme di potenziale: di base e temporaneo.

Il potenziale di base è il vostro talento innato e muta unicamente in circostanze del tutto eccezionali.

Il potenziale temporaneo si somma a quello di base: ogni volta che migliorate in una competenza, il relativo potenziale temporaneo subisce un calo. Potete persino registrare un potenziale temporaneo negativo se, poniamo il caso, consumate pietanze con penalità al potenziale.

La somma algebrica del potenziale base e di quello temporaneo stabilisce la celerità di apprendimento delle vostre abilità e caratteristiche.
{p}
<b>Gestire il Potenziale</b>

Potete accrescere il potenziale delle abilità visitando gli addestratori cittadini e pagando in monete di platino: ogni sessione d'addestramento conferisce un incremento al potenziale temporaneo dell'abilità scelta. Consumare cibi con le proprietà appropriate elargirà invece potenziale temporaneo per gli attributi fisici e mentali.

Anche i vostri alleati possiedono un loro potenziale: donare loro monete d'oro da spendere in città aumenterà il loro potenziale d'abilità, e beneficeranno ugualmente del nutrimento fornito dalle pietanze.

Tenuto conto di tutto ciò, com'è possibile gestire male il proprio potenziale?
{p}
Il mantenimento del potenziale è una fune tesa tra due esigenze contrastanti: da un lato, un alto potenziale garantisce una crescita fulminea. Dall'altro, addestrarsi diventa progressivamente più costoso man mano che il potenziale temporaneo sale, e una quota maggiore ne viene bruciata a ogni avanzamento di livello.

Allo stesso modo, maggiore è il potenziale di caratteristica accumulato, più arduo risulterà incrementarlo ulteriormente. È perciò vitale bilanciare la propria progressione con il costante rinnovamento del potenziale.

<b>Cosa Allenare e con Quali Criteri</b>

Dalle nostre interviste ai veterani di Tyris è emerso un chiaro consenso:

*Le abilità belliche dovrebbero sempre essere addestrate. Persino i maghi traggono immenso giovamento dalle abilità difensive.
{p}
*Le competenze che richiedono materiali o risorse scarse, come la manifattura, meritano priorità assoluta dagli addestratori. Al contrario, abilità facilmente praticabili in autonomia, come la musica, non dovrebbero essere addestrate a pagamento.

*Le abilità che offrono vantaggi limitati, come la stima, non richiedono investimenti oltre la soglia minima d'utilità.

*Un eccellente valore di riferimento per un potenziale ben bilanciato si attesta attorno al 200%.

Queste sono linee guida generali: valutate attentamente la vostra situazione personale e spendete le vostre preziose monete di platino con giudizio!
{p}
<b>Considerazioni Conclusive</b>

Poiché i costi d'addestramento lievitano, gli avventurieri avveduti dovrebbero non solo cercare maggiori introiti di platino, ma anche sfruttare al meglio il proprio potenziale. Dato che il potenziale cala al salire dell'abilità, il momento ideale per allenarsi nuovamente è subito dopo un passaggio di livello, così da massimizzare la resa di ogni singola moneta spesa.

Attraverso un'accorta gestione del potenziale, un avventuriero intelligente ottimizzerà la propria crescita senza mai incorrere in frustranti colli di bottiglia nel proprio cammino verso la gloria!

***

<i>- Nel numero della prossima settimana faremo luce sulla sorte: cosa significa davvero essere baciati dalla fortuna e come gli avventurieri possono trarne beneficio!</i>
"""

ADVWEEK_3 = """Settimanale dell'Avventuriero N. 3: La Fortuna,L'Inviato di Palmia Kawa,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Nel numero di questa settimana vi scrivo direttamente dai saloni scintillanti del Fortune Bell, per esplorare il tema della sorte.

Un posto del genere è il tempio della buona stella, non trovate? Specialmente quando il caporedattore ha acconsentito a catalogare il mio soggiorno sotto la voce "spese aziendali"...

La fortuna è da sempre un argomento avvolto nel mistero tra i viandanti: circolano dicerie e leggende su cosa essa faccia <b>realmente</b>.
{p}
Ad esempio, ci credereste se vi dicessi che la fortuna non influenza in alcun modo i giochi del Fortune Bell? È la pura verità! Che si tratti del tiro al putit, delle slot machine o del blackjack, il vostro punteggio di fortuna non conta un bel niente!

Difatti ho imparato a calcolare il tempismo dei rulli delle slot per centrare il jackpot con sconcertante regolarità!

E sono più che certo che i croupier ai tavoli del blackjack non stiano "tramando nulla di losco"!

La sorte è davvero imprevedibile!
{p}
Per fare chiarezza è sempre meglio consultare chi se ne intende. Al bar della sala c'erano due sacerdotesse della Chiesa di Ehekatl intente a predicare con un delizioso costume da gattina: ho offerto loro da bere e ho chiesto delucidazioni sul dominio della loro dea.

<b><i>Erano adorabili, ma non divaghiamo!</i></b>

Come volevasi dimostrare, la stragrande maggioranza delle dicerie sulla fortuna è del tutto infondata. Non migliora la rarità dei tesori rinvenuti nei nefia, né aiuta a schivare i fendenti nemici. Non aumenta la probabilità di un mese fausto, né aiuta a pescare pesci più grossi. Alcuni di questi prodigi sono benedizioni esclusive di Lady Ehekatl e del tutto slegate dal punteggio di fortuna, mentre il resto è pura leggenda da taverna.
{p}
Ma allora, che cosa fa DAVVERO la fortuna?

La sua funzione primaria consiste nel consentire di ritirare i "dadi": ogni punto di fortuna garantisce l'1% di probabilità che ciò avvenga, e superando quota 100 si possono ottenere rilanci multipli, fino a un massimo di 20 volte! Ho chiesto alle sacerdotesse che cosa fossero esattamente questi "dadi", ma ammetto che potrei essere stato distratto durante la loro spiegazione... In ogni caso, ecco gli ambiti concreti in cui i "dadi" della fortuna intervengono:

*Danni inflitti e cure elargite.
*Mitigazione dei danni garantita dal VP (Protezione).

Si tenga presente che una fortuna negativa opera nello stesso identico modo, ma selezionando l'esito peggiore dei rilanci: prestate molta attenzione alle maledizioni dell'infausto!
{p}
La fortuna incide inoltre sulla probabilità che un forziere a sorpresa paghi una vincita ricca e accresce la resistenza personale contro la maledizione degli equipaggiamenti, sebbene ciò esuli dalla meccanica dei "dadi".

Potrà sembrare poco a prima vista, ma massimizzare danno, cure e difesa è vitale per la sopravvivenza, e poter contare sul migliore di due esiti è un vantaggio colossale sul filo di lana!

Dunque, come potete voi avventurieri diventare più fortunati?

Il passo fondamentale è consacrarsi a Lady Ehekatl! Le sacerdotesse al bancone erano carine, ma in fondo... <b>era solo un costume con le orecchie da gatta, no?</b>

Comunque ho comprato alcune monete della fortuna da loro!
{p}
Per chi non lo sapesse, le monete della fortuna sono pezzi a tiratura limitata coniati dalla zecca reale di Palmia nel 467 per celebrare la vittoria nella Guerra dei Dieci Anni, finemente incise con il volto sorridente di Lady Ehekatl in persona.

Basta portare quel sorriso con sé per sentirsi già baciati dalla sorte!

Potete inoltre indossare equipaggiamenti in mica per accrescere la vostra fortuna. Sapevate che gli altari di Lady Ehekatl sono intagliati nella mica? Verissimo! Anche se non ho ancora capito se la mica porti fortuna grazie alla dea, o se la dea adori la mica perché porta fortuna...
{p}
In ogni caso credo proprio che mi tratterrò al tavolo del blackjack ancora un po', perciò vi saluto qui!

***

<i>- Nel prossimo numero lasceremo la parola alla Chiesa di Jure, che ci insegnerà a prevenire e debellare gli stati alterati elementali!</i>
"""

ADVWEEK_4 = """Settimanale dell'Avventuriero N. 4: Gli Stati Alterati,Madre Therese,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.

Questa settimana abbiamo invitato Madre Therese della Chiesa di Jure per illustrarci come prevenire e guarire dalle condizioni e alterazioni elementali.</i>


Venite a me, gattini smarriti: vi condurrò verso la luce. Come parte del nostro impegno comunitario mensile, la Chiesa di Jure sta svolgendo un'opera di sensibilizzazione tra gli avventurieri. Sebbene le nostre porte siano sempre spalancate per accogliere malati e feriti, la nostra speranza più fervida è che restiate in salute e non abbiate mai bisogno dei nostri servigi.
{p}
<b>Stati Alterati e Malefici</b>

È doveroso chiarire subito questo punto, poiché moltissimi esploratori confondono le alterazioni elementali con i malefici arcani. Gli stati alterati sono effetti scatenati da determinati elementi, applicati quando il bersaglio subisce danni da quell'elemento specifico. I malefici sono invece afflizioni provocate da incantesimi peculiari. Questa distinzione è cruciale: prevenzione e cura richiedono approcci totalmente differenti.

La gravità di uno stato alterato scaturisce dalla potenza elementale dell'attacco, la quale è proporzionale al danno inferto e calibrata dalla fonte: ad esempio, gli incantesimi a contatto infliggono stati alterati con molta più facilità rispetto alle lame magiche.
{p}
Se trascurati, gli stati alterati peggioreranno sotto ulteriori attacchi elementali, provocando conseguenze catastrofiche. Troppi novizi hanno perso la vita dinanzi a bulbi oculari fluttuanti che li paralizzavano senza tregua, lasciandoli completamente inermi.

<b>La Prevenzione</b>

Un celebre insegnamento della Chiesa di Jure recita che prevenire è meglio che curare, e ciò vale doppiamente per gli stati alterati. Non contrarre un'afflizione fin dall'inizio fa risparmiare preziosi istanti durante la battaglia, quando ogni secondo può fare la differenza tra la vita e la morte, specie se l'afflizione impedisce di agire.
{p}
La prima linea difensiva è costituita dagli incantamenti degli equipaggiamenti che annullano direttamente condizioni come veleno o paralisi. Disporre di un incantamento di negazione per ciascuno stato vitale è fondamentale; possederne doppi non conferisce benefici aggiuntivi, motivo per cui gli avventurieri paragonano l'assetto della propria armatura a un intricato mosaico.

Il secondo baluardo di difesa è rappresentato dalle resistenze elementali: minore è il danno subito, più debole sarà la carica dello stato alterato. Acquisire l'immunità completa a un elemento vi proteggerà interamente anche dallo stato associato, un rimedio preziosissimo per afflizioni come lo stordimento, per le quali non esistono incantamenti di negazione diretta.

Terzo: svariati incantesimi possono prevenire stati specifici. Occhio di gatto, ad esempio, immunizza dalla cecità: usateli per colmare le falle lasciate scoperte dal vostro equipaggiamento.
{p}
Infine, quando ogni altra difesa cede, i vostri attributi possono opporre una naturale resistenza passiva a diverse afflizioni: la cecità, ad esempio, è contrastata dalla percezione. Come tutti i fedeli, gli avventurieri traggono immenso beneficio dagli insegnamenti di Lady Jure: lavorate sodo, nutritevi con cibi sani e forgerete una naturale tempra d'acciaio contro ogni male.

<b>La Guarigione</b>

Se nonostante le precauzioni siete stati colpiti da uno stato alterato, non lasciatevi prendere dal panico: vi è sempre modo di rimediare.

Lanciare un incantesimo purificatore che neutralizza quella condizione la curerà all'istante: invocare eroismo, ad esempio, dissipa immediatamente la confusione mentale.
{p}
Qualsiasi fonte di guarigione vitale ridurrà gradualmente l'intensità dello stato alterato fino a rimuoverlo. Tuttavia, se i vostri punti vita sono intatti, incantesimi come ristoro corporeo o mentale risulteranno infinitamente più efficaci nello spazzare via le alterazioni.

Alcune condizioni possono essere risolte con metodi ingegnosi: subire danni non mentali sveglia chi dorme, mentre essere bagnati estingue le fiamme. Le erbe scarlatte e blu curano rispettivamente emorragie e avvelenamenti.

Poiché molte afflizioni impediscono totalmente di muoversi o agire, avere compagni fidati al proprio fianco pronti a soccorrervi nelle situazioni critiche è sempre la miglior garanzia di salvezza.
{p}
Vi ringrazio per la vostra attenzione. Pregherò affinché ciascuno di voi possa camminare sempre sotto la graziosa benevolenza di Lady Jure.

***

<i>- Nel numero della prossima settimana scopriremo come l'applicazione pratica di un semplicissimo stato alterato possa salvare la vita agli avventurieri!</i>
"""

ADVWEEK_5 = """Settimanale dell'Avventuriero N. 5: Bagnarsi Fa Bene!,L'Inviato di Specwing Orryn,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Oggi seguiremo l'avventuriera mifu Miyuki all'interno di un nefia per carpire qualche trucco ingegnoso adatto ai principianti con pochi spiccioli in tasca. Vuoi mostrarci cosa hai portato con te, Miyuki?
<color=brown>
Ecco... Yuki-chan non ha molti soldi, quindi ha con sé solo provviste semplici...
Bende, crocchette, e il suo fidato annaffiatoio...
Non rida, signor giornalista!
L'annaffiatoio di Yuki-chan le ha salvato la pelle un sacco di volte!
</color>
{p}
Davvero curioso! Un annaffiatoio non è un arnese che si usa in giardino a casa? Vediamo come può rendersi utile in un dungeon!

***

Miyuki si addentra furtiva tra le rovine. Un segugio di fuoco selvatico balza fuori dall'ombra!

Senza scomporsi, Miyuki si rovescia addosso l'acqua dell'annaffiatoio e avanza verso la belva completamente fradicia.
<color=brown>
Rooaaar!
</color>
Una fiammata tremenda investe in pieno Miyuki.

Ma poiché era completamente bagnata, i danni da fuoco sono stati attutiti e il suo equipaggiamento non ha preso fuoco!

Niente coperta ignifuga necessaria!
{p}
Con gli attacchi resi inoffensivi, il segugio è stato abbattuto in quattro e quattr'otto.

A quanto pare l'annaffiatoio si è rivelato davvero provvidenziale!

***

Misericordia! È comparso un bellimbusto esplosivo!

Miyuki lesta gli spruzza una secchiata d'acqua gelida addosso. Il bellimbusto è zuppo fradicio.

"Fooooo!"

Essendo bagnato fradicio, il bellimbusto non può innescare l'esplosione kamikaze e viene neutralizzato in tutta sicurezza.
{p}
Sembra proprio che l'annaffiatoio abbia salvato Miyuki una seconda volta!

***

All'improvviso, una pozione sfreccia dall'oscurità!

Miyuki la schiva con una piroetta, ma il mostro nell'ombra resta invisibile.

Imbracciando l'annaffiatoio, comincia a spruzzare acqua ovunque nella stanza.

Il pavimento si riempie di pozzanghere e la creatura ci finisce dentro: zuppa d'acqua, la zucca spettrale perde l'invisibilità!
{p}
Ora che il bersaglio è palese, Miyuki affetta la zucca con il suo pugnale di rame.
<color=brown>
Hiyaaah!
</color>
L'umidità dell'acqua ha reso i danni da fulmine del pugnale incredibilmente devastanti!

La zucca finisce folgorata e stramazza al suolo!

Incredibile, è la terza volta che l'annaffiatoio toglie le castagne dal fuoco a Miyuki. Dovrei davvero riflettere su come gli oggetti della vita quotidiana possano fare la differenza per un avventuriero!

***
<color=brown>
Oh no! Yuki-chan è finita su una trappola ed è stata teletrasportata dentro una parete rocciosa!
</color>
{p}
<color=brown>Yuki-chan non si è fatta male, ma è incastrata a metà dentro questa fessura...

Signor giornalista, potrebbe prendere l'annaffiatoio dal suo zaino e aiutarla a scivolare fuori?

Ecco, bravissimo, ma... dove sta guardando, signor giornalista?

Aspetti, quello non è...

Kyaaah~♡ Che scivoloso~♡
</color>

***

<i>......Nel numero della prossima settimana saremo presenti a una delle famose aste di cavalli di Yowyn, per scoprire come l'abilità di cavalcatura possa trasformare la vostra carriera d'avventurieri!</i>
"""

files_data = {
    'advweek_1.txt': ADVWEEK_1,
    'advweek_2.txt': ADVWEEK_2,
    'advweek_3.txt': ADVWEEK_3,
    'advweek_4.txt': ADVWEEK_4,
    'advweek_5.txt': ADVWEEK_5,
}

for fname, text in files_data.items():
    p = os.path.join(BOOK_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(text.strip() + '\n')

print("Applied Italian translations for Adventurer's Weekly 1 to 5")
