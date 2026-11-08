"""
Translate Adventurer's Weekly 6 to 10 into Italian.
"""
import os

BOOK_DIR = 'Lang/IT/Text/Book'

ADVWEEK_6 = """Settimanale dell'Avventuriero N. 6: L'Arte della Cavalcata,L'Inviata di Yowyn Celia,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


In questo numero vi scrivo direttamente da una delle rare aste di cavalli che si tengono a Yowyn ogni anno! Per l'occasione ho intervistato il mastro di stalla Varis, che alleva i celebri cavalli di Yowyn da oltre vent'anni, per capire perché siano così contesi!
{p}
<color=brown>Celia: La ringrazio, Mastro Varis. C'è una folla incredibile qui oggi!</color>

Varis: Dovere, signorina. Ebbene, la corona ha diritto di prelazione sulla maggior parte dei cavalli di Yowyn, e la nobiltà sceglie subito dopo. Non abbiamo abbastanza capi perché la gente comune possa godere spesso dei benefici di un buon destriero, perciò ogni asta richiama folle di avventurieri.

<color=brown>Celia: Può illustrarci alcuni di questi benefici?</color>

Varis: Mmh. Innanzitutto ci si muove molto più in fretta, fino alla velocità massima della cavalcatura. Inoltre, gli attacchi indirizzati a voi colpiranno talvolta il vostro destriero al vostro posto. Se cavalcate una creatura alata, volerete insieme a lei.
{p}
Varis: Ma l'aspetto più cruciale è che salvaguarda la vita della cavalcatura: se la bestia cade in battaglia, rimarrà soltanto stordita per qualche tempo. Perderete i vantaggi di sella per un po', ma almeno non vi ritroverete orfani di un alleato.

<color=brown>Celia: E qualunque avventuriero sa quanto conti la velocità sul campo di battaglia.</color>

Varis: (Ride) Verissimo, signorina. Ora, montare una bestia più lenta di voi vi sarà solo d'impaccio: per fortuna i cavalli di Yowyn sono i più veloci di tutta Tyris, al punto che persino una fatina ne trarrebbe vantaggio.
{p}
Varis: Badate bene: non basta saltare in groppa per arrivare a Palmia in un giorno. Serve l'abilità di Cavalcatura per dominare la bestia, e la cavalcatura deve avere abbastanza forza fisica per reggere il vostro peso. Più veloce è l'andatura, maggiori saranno i requisiti per entrambi. Vi sono creature come i nostri cavalli selezionate appositamente per facilitare la monta; al contrario, esistono bestie che sono cavalcature pessime e non andrebbero mai montate per nessun motivo.

<color=brown>Celia: Sembra davvero complicato! So già che avrei tutti i muscoli a pezzi se dovessi cavalcare fino a Palmia adesso!</color>

Varis: Padroneggiare la cavalcatura richiede tempo, ma bisogna salire in sella e stringere i denti. All'inizio barcollerete ovunque, fallendo attacchi e pasticciando con gli incantesimi, ma queste penalità svaniranno gradualmente man mano che imparerete a coordinarvi. Un avventuriero a cavallo esperto è una forza della natura: destriero e cavaliere combattono come un'unica entità.
{p}
<color=brown>Celia: Meraviglioso! Anche la cavalcatura può attaccare?</color>

Varis: Certamente, la cavalcatura attacca finché rimanete fermi sul posto; se vi muovete, usa il suo turno per avanzare. Naturalmente soffre delle vostre stesse penalità offensive all'inizio, ma entrambi le supererete con l'esperienza.

Un altro fattore fondamentale è l'armonia magica: gli incantesimi con la dicitura "si applica anche alla cavalcatura" beneficeranno il destriero senza bisogno di lanciarli come magie di gruppo. Il rovescio della medaglia è che le frecce magiche nemiche colpiranno entrambi all'unisono, infliggendo doppio danno.
{p}
<color=brown>Celia: Se le cavalcature combattono dovrebbero essere equipaggiate: lei come vestirebbe i suoi cavalli, Mastro Varis?</color>

Varis: Mmh. La velocità prima di tutto, perciò mi assicurerei che la bestia sia benedetta da Lulwy. Dopodiché cercherei di dotarla di anelli della velocità se possibile: costano una fortuna, ma valgono ogni moneta. Ho sentito di avventurieri senza scrupoli che somministrano mutazioni d'ogni genere alle loro povere bestie per renderle ancora più scattanti, ma... preferisco davvero non pensarci troppo.
{p}
<color=brown>Celia: Capisco. Sono state informazioni preziosissime, Mastro Varis, che spiegano chiaramente perché la cavalcatura sia sempre più amata dai viandanti. Sembra che l'asta stia per cominciare, perciò chiudiamo qui l'intervista.</color>

Varis: È stato un piacere, signorina.

***

<i>- Nel numero della prossima settimana torneremo a Yowyn per una seconda intervista sul tema della simbiosi, strettamente legata alla cavalcatura!</i>
"""

ADVWEEK_7 = """Settimanale dell'Avventuriero N. 7: La Simbiosi,L'Inviata di Yowyn Celia,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


La settimana scorsa il mastro di stalla Varis ci ha introdotto all'arte della cavalcatura; oggi approfondiremo un tema affine: la simbiosi parassitaria.

<color=brown>Celia: Grazie per averci accolto di nuovo, Mastro Varis.</color>

Varis: Siete sempre la benvenuta, signorina. (Ride) Dopotutto state facendo pubblicità gratuita alle nostre attività locali!
{p}
<color=brown>Celia: Ebbene! Riprendendo il discorso dell'altra volta, cosa può dirci sulla simbiosi e su come può aiutare gli avventurieri?</color>

Varis: La simbiosi è simile alla cavalcatura: potete immaginarla come il vostro compagno che cavalca voi, invece del contrario.

<color=brown>Celia: Davvero! Significa che il compagno si muove rapido quanto noi?</color>

Varis: Purtroppo no. Il compagno ospitato sul vostro corpo mantiene la propria velocità di base. Tuttavia, riceve una frazione di tutti i vostri modificatori di velocità, positivi o negativi: incantesimi, equipaggiamenti e simili. Ma non il bonus fornito dalle cavalcature.
{p}
<color=brown>Celia: Ha appena menzionato le cavalcature: significa che si può cavalcare e ospitare un simbionte nello stesso momento?</color>

Varis: Esattamente! Voi tre potete occupare il medesimo spazio sulla mappa. Un fendente diretto a voi ha una probabilità di impattare sulla cavalcatura o sul simbionte, e lo stesso vale se il bersaglio è l'alleato ospitato. Molti vantaggi della cavalcatura sono condivisi con la simbiosi: finire storditi invece di morire, incantesimi di sella estesi a tutti voi, e via dicendo. Simili penalità a precisione e lancio magico si applicano quando si ospita un simbionte, regolate dalla specifica abilità di Simbiosi. Se cavalcate e ospitate contemporaneamente, entrambe le penalità si sommeranno, perciò fate molta attenzione!
{p}
<color=brown>Celia: Essendo due arti così simili, forse conviene concentrarsi sulle loro differenze.</color>

Varis: Ebbene, i simbionti sono più aggressivi: ospitare un compagno micidiale ma fisicamente fragile è un'ottima strategia. A differenza della cavalcatura, può continuare ad agire persino mentre vi muovete, e non dovete preoccuparvi dei divari di velocità poiché non è vincolato al vostro passo.

<color=brown>Celia: Capisco.</color>

Varis: Poiché il simbionte non può camminare autonomamente, dotarlo di attacchi a distanza è una splendida idea nel caso vogliate mantenere le distanze dai nemici.
{p}
<color=brown>Celia: Tutto ciò è illuminante, Mastro Varis. Un'ultima curiosità: quali compagni consiglierebbe come ottimi simbionti?</color>

Varis: Mmh. Non vi sono scelte ovvie e accessibili come i cavalli di Yowyn... forse una sorellina gatta. Sono agili e forti, ma inadatte alla cavalcatura e poco resistenti ai colpi pesanti. Direi che incarnano alla perfezione ciò per cui la simbiosi è stata concepita, anche se sono un po' difficili da incontrare. Un tempo le vendevamo a Yowyn, ma poi... beh, è una faccenda complicata.
{p}
<color=brown>Celia: Possiamo ben immaginarlo. La ringrazio per questa nuova intervista, Mastro Varis: combinando con astuzia cavalcatura e simbiosi, sono certa che i nostri lettori gestiranno i propri alleati con molta più disinvoltura.</color>

Varis: Il piacere è tutto mio, signorina.

***

<i>- Nel prossimo numero vi insegneremo a gestire con successo la vostra attività commerciale!</i>
"""

ADVWEEK_8 = """Settimanale dell'Avventuriero N. 8: Gestire una Bottega,Nonna Shu,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, dove rispondo ai dubbi di voi sbarbatelli sul vile denaro.</i>

La lettera di oggi arriva da un giovanotto di Mysilia che domanda: <color=blue>"Nonna Shu, i prezzi che i bottegai mi offrono per il mio bottino sono da fame! Ho pensato di aprire un negozio tutto mio: ne vale la pena?"</color>

Ebbene, ho una notizia per te: i bottegai sono dei tirchi patentati. Non è colpa loro — tutti devono campare a questo mondo — ma ti riconoscono solo una misera frazione di ciò che le tue merci valgono davvero. Poco importa cosa vendi: il prezzo d'acquisto sarà sempre una delusione.
{p}
Spedire il bottino nelle casse d'esportazione è un'opzione: i commercianti all'ingrosso pagano meglio e ti danno pure lingotti d'oro. Ma la cassa ha una capienza limitata e non c'è margine di contrattazione.

Veniamo alla tua domanda, figliolo: gestire una bottega tutta tua. Comporta del lavoro: devi allestire un banco, promulgare un paio di ordinanze comunali e tenere gli scaffali ben riforniti. Ma sarai tu a dettare legge, fisserai tu i prezzi, e l'unico limite ai tuoi incassi sarà il numero di gonzi che riuscirai ad abbindolare. Non è una vita per tutti, ma se l'idea ti stuzzica, nonna Shu ha qualche perla di saggezza per te.
{p}
<b>Le Basi del Mestiere</b>

Prima di tutto devi possedere della terra. Scegli un punto panoramico attraente: il mio emporio sorge su una distesa innevata accanto a un'antica rovina. Non serve chissà quale palazzo — puoi benissimo vendere le tue carabattole direttamente da un carro — ma a molti clienti piace una bella vetrina. Quello che ti serve <b>assolutamente</b> è un'etichetta del prezzo: fabbricane una al laboratorio delle insegne.

Con quell'etichetta, ragazzo mio, marchi le merci che intendi vendere. Apri bottega e i passanti cominceranno a entrare per comprare; se tieni un baule vicino a un'insegna di stoccaggio con altri articoli dello stesso tipo, gli scaffali si riassortiranno automaticamente. Etichettare un intero baule pieno mette in vendita tutto il suo contenuto in un colpo solo, l'ideale se sei un pigrone come mia nipote.
{p}
Non serve nemmeno che tu sia fisicamente dietro al bancone per fare affari: la gente di North Tyris è abbastanza onesta da prendere la merce e lasciare il giusto corrispettivo in monete sul tavolo. Una cosa del genere finirebbe in rapina dopo due minuti in posti come Yerl o Eulderna: non avete idea di quanto siete fortunati qui, marmocchi.

<b>Fare i Soldi Veri</b>

Ma non finisce qui. Hai aperto la bottega, ora il tuo dovere è attirare <b>tutti</b> i clienti possibili e spremere ogni singolo oren dalle loro tasche. Ciò significa, ragazzo mio, che devi muoverti su più fronti:

Prezzi: promulga ordinanze per accrescere il valore delle merci, come una licenza per emporio generale o ristorante. Personalmente detesto le botteghe truffaldine: mi sembrano miopi.
{p}
Affluenza: più gonzi entrano, più vendi. Se hai scelto un bel posto come ho fatto io sei già a metà dell'opera. Sborsa lingotti d'oro in pubblicità cittadina e attiva la sicurezza turistica così che i visitatori si sentano sereni nel venire a trovarti. E assicurati che non vengano sbranati dai mostri lungo la strada: un cliente morto non compra un bel niente!

Portafoglio: questo punto è vitale, figliolo. I clienti comprano solo ciò che possono permettersi: se tutto ciò che esponi costa un occhio della testa, non venderai uno spillo. Vuoi che siano i nobili facoltosi a varcare la tua soglia: l'ordinanza del paradiso delle celebrità li attirerà a frotte. I ricchi adorano il brivido di visitare luoghi selvaggi e pericolosi, perciò posiziona la tua tenuta lontana dalle vie battute.
{p}
E ora... ascoltami bene. Potrà suonarti folle, ragazzo mio, ma fidati: comincia a evocare demoni sulla tua terra. Ciò renderà i mostri erranti più feroci, ma attirerà magicamente i signori più danarosi. Non chiedermi perché, funziona e basta. Puoi istituire guardie di confine se l'idea ti inquieta: terranno alla larga le bestie peggiori senza infastidire i clienti.

Questi sono i consigli di Nonna Shu: semplici a sufficienza perché persino quella fannullona di mia nipote possa capirli.
{p}
Ah, un'ultima cosa: quando i clienti comprano qualcosa, spesso vogliono provare il nuovo acquisto sul posto. Non giudico chi ha un debole per il liquido anticorrosivo, ma metto un veto assoluto a chi si mette a lanciare meteoriti dentro al mio negozio! Sono certa che la pensi allo stesso modo, giovanotto, quindi occhio a cosa metti in vendita sugli scaffali!

***

<i>- Nel prossimo numero torneremo a Yowyn per dare un'occhiata alla recente mania dell'apicoltura!</i>
"""

ADVWEEK_9 = """Settimanale dell'Avventuriero N. 9: L'Apicoltura,L'Inviata di Yowyn Celia,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Questa settimana mi sono unita anch'io alla febbre dell'apicoltura che sta contagiando tutta Yowyn!

Con la gente di North Tyris sempre più attenta al benessere fisico, tutti desiderano un tocco di naturale dolcezza nella propria vita, e quale fonte migliore delle proprie api personali?
{p}
Il sapore! Il profumo! Che si tratti di zucchero o di miele dorato, è infinitamente più genuino e nutriente quando proviene dalle tue arnie piuttosto che dagli scaffali di un emporio! Non mi serviva altro per convincermi a provare l'apicoltura!

Vi incuriosisce? Continuate a leggere!

<b>I Primi Passi</b>

Ebbene, la prima cosa di cui avevo bisogno per allestire le arnie erano api regine: si possono trovare negli sciami d'api selvatiche, anche se sono piuttosto rare. Inseguire le api selvatiche nei boschi può costarvi punture dolorosissime, perciò quello che ho fatto io è stato aggirarmi attorno alle arnie della mia vicina e stuzzicare i suoi sciami finché non ho catturato un paio di regine!

Sono sicurissima che non le dispiacerà affatto, eheh!
{p}
Dopodiché servono chiodi e mattoni d'argilla, per poi assemblare le arnie al banco da falegname. Ho chiesto al mio fidanzato di farlo per me: è così abile con le mani~♡

E io? Io mi sono dedicata a piantare fiori! Una singola arnia può funzionare anche senza fiori, ma se volete ampliare l'apiario dovrete coltivare aiuole. Qualunque fiore va bene, ma io adoro il cotone perché fornisce anche morbido tessuto. Non importa dove piantate i fiori: non devono essere necessariamente attaccati alle arnie e contano persino se sono appena germogliati. Più arnie possedete, più fiori serviranno per ciascuna nuova arnia per la produzione di miele, quindi non esagerate!
{p}
<b>La Produzione del Miele</b>

Una volta preparato tutto, posizionate le arnie e attendete con pazienza! Le api lavoreranno con il sole o con la pioggia: se tutto è in ordine, ogni mattina raccoglierete un favo per ciascuna arnia. Potete aiutarle preservando la terra: se la fertilità del suolo scende sotto quota 30 la produzione di miele ne risentirà, perciò strappate via le erbacce!

La qualità dei favi che otterrete sarà la media esatta di tutti i vostri fiori piantati: fiori di qualità eccelsa significano miele da intenditori! È così gratificante vedere tutti quegli insetti laboriosi darsi da fare per voi, non trovate?
{p}
<b>La Lavorazione</b>

Potete mangiare i favi grezzi così come sono, ma sarebbe un vero spreco. Molto meglio macinarli per ricavare miele liquido, oppure tostarli nel forno per ottenere purissimo zucchero! I condimenti di alta qualità infondono un aroma straordinario a ogni piatto, specialmente a quelli più rari! Con lo zucchero fate la pasta per torte, con il miele dolcificate il caffè: fa così bene alla salute!

Dolce e profumato: una delizia del genere non si compra da nessuna parte! Eheh, non riesco proprio a resistere~♡

Ne producete più di quanto riusciate a mangiarne? Potete sempre fermentarlo per fare l'idromele, immagino... Ma non è certo un problema che riguarda la sottoscritta!

***

<i>- Nel prossimo numero torna Nonna Shu per elargire preziosi consigli sugli investimenti finanziari!</i>
"""

ADVWEEK_10 = """Settimanale dell'Avventuriero N. 10: Gli Investimenti,Nonna Shu,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, dove rispondo ai dubbi di voi sbarbatelli sul vile denaro.</i>


La lettera di oggi arriva direttamente da una ragazza di Porto Kapul: <color=blue>"Nonna Shu, adesso che ho messo da parte un bel gruzzoletto, stavo pensando di investire in qualche attività. Quali investimenti garantiscono il rendimento più alto?"</color>

Ah, beata gioventù: ingenua, fiduciosa e totalmente ignorante. Ragazzina mia, investire non ti fa guadagnare denaro liquido. Pensi davvero che basti lanciare un pugno di monete d'oro a un bottegaio perché quel poveraccio sia costretto a staccarti dividendi per l'eternità?
{p}
Magari fosse così: sarei andata in pensione cinquant'anni prima! Forse le cose funzionano a quel modo a Yerl, dove vige la legge della giungla, ma qui a North Tyris non abbiamo ancora rimpiazzato i nostri cuori con ingranaggi metallici.

<b>Botteghe contro Città</b>

La prima cosa che voi giovani dovete ficcarvi in testa è che potete investire o nei singoli negozi, oppure nell'intera città rivolgendovi al funzionario municipale. Sommando il livello della bottega a quello della città otterrete il suo livello effettivo.
{p}
La differenza potrebbe sembrarvi irrilevante, ma supponiamo che vi affezioniate a un mercante e decidiate di invitarlo a trasferirsi nel vostro insediamento: ebbene, se avevate investito nella città, quegli investimenti rimarranno lì e non saranno trasferibili. Idem investendo nella bottega: se succede qualcosa al negoziante, o se decidete di esiliarlo dalla città, non rivedrete mai più un solo soldo del vostro capitale.

Capite bene quale problema possa diventare, eh?

Altra nota fondamentale: gli investimenti nelle città non contano ai fini dei punti contributo per la Gilda dei Mercanti. Non chiedetemi il perché: le regole erano queste quando mi sono iscritta e sono rimaste tali quando sono andata in pensione.
{p}
<b>I Reali Benefici</b>

Dunque, se investire non serve a incassare rendite dirette, a cosa diavolo serve? Semplice: i negozi di livello superiore tengono un assortimento merci più vasto e di qualità nettamente superiore. Cosa significhi "superiore" dipende dalla bottega: le locande offrono piatti più nutrienti, i fabbri espongono armi e corazze più potenti, i negozi di magia tengono tomi d'incantesimi più rari. C'era un promettente panettiere a Palmia in cui Nonna Shu investì un paio di milioni: alla visita successiva sfornava il miglior pane di tutto il regno, secondo solo a quello del palazzo reale.

Badate bene: la certezza matematica non esiste. Un negozietto di basso rango può sempre esporre per miracolo un pezzo pregiatissimo, mentre un emporio di alto livello potrebbe non avere ciò che cercate; non c'è una soglia fissa in cui questa o quella merce inizia ad apparire. Nondimeno, più alto è il livello della bottega, maggiori saranno le probabilità di trovare ciò di cui avete bisogno, se non altro per la stazza del magazzino merci.
{p}
Inoltre investire vi farà guadagnare influenza politica nella comunità: come c'è da aspettarsi, girare per le strade elargendo sacchi di monete attira la benevolenza di tutti.

<b>Consigli Finanziari di Nonna Shu</b>

Ora, ragazza mia, sarò brutale: comunque la si guardi, investire richiede una quantità SPROPOSITATA di denaro, e non ne avrete mai abbastanza. Detto questo, vi sono trucchi per far rendere al meglio ogni singola moneta.

Tutti sanno che essere abili negli investimenti riduce i costi. Ciò che molti ignorano è che avere un bel faccino aiuta altrettanto. Il Carisma è efficace circa la metà, ma essere piacevoli alla vista è infinitamente più facile che comprendere il reale significato dei paroloni finanziari che vi escono dalla bocca!
{p}
Gli investimenti in una città e quelli nelle sue botteghe vengono conteggiati separatamente, quindi se il costo di uno dei due diventa esorbitante, vi converrà dirottare i fondi sull'altro per un po'.

Alcune tipologie di botteghe hanno un tetto massimo invalicabile per la qualità delle merci; altre non hanno limiti. Non continuate a gettare soldi a fondo perduto nelle prime sperando di veder apparire miracoli sugli scaffali.

Questi sono i consigli di Nonna Shu: abbastanza semplici perché persino quella fannullona di mia nipote possa comprenderli. Ora andate là fuori e diventate autentici pilastri dell'economia locale!

***

<i>- Nel prossimo numero faremo tappa alla gilda dei maghi per approfondire i retroscena del lancio d'incantesimi in gruppo!</i>
"""

files_data = {
    'advweek_6.txt': ADVWEEK_6,
    'advweek_7.txt': ADVWEEK_7,
    'advweek_8.txt': ADVWEEK_8,
    'advweek_9.txt': ADVWEEK_9,
    'advweek_10.txt': ADVWEEK_10,
}

for fname, text in files_data.items():
    p = os.path.join(BOOK_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(text.strip() + '\n')

print("Applied Italian translations for Adventurer's Weekly 6 to 10")
