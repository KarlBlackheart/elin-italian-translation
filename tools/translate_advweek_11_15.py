"""
Translate Adventurer's Weekly 11 to 15 into Italian.
"""
import os

BOOK_DIR = 'Lang/IT/Text/Book'

ADVWEEK_11 = """Settimanale dell'Avventuriero N. 11: Magia di Gruppo,L'Inviato di Lumiest Jaystar,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Questa settimana siamo alla Gilda dei Maghi per scoprire come gli incantesimi influenzino i propri alleati. Poiché gli avventurieri formano solitamente squadre per esplorare i nefia, è doveroso imparare a lavorare in team, e l'arte magica non fa eccezione.

{p}
<b>Controllo della Magia</b>

Quando si scagliano magie offensive ad area, l'ultima cosa che si desidera è incenerire i propri compagni con dardi e sfere di fuoco. È qui che entra in gioco l'abilità di Controllo della Magia: impedisce ai vostri incantesimi ad area di danneggiare gli alleati. Con un punteggio sufficiente in Controllo della Magia, potrete scatenare cataclismi come terremoto senza sfiorare i vostri amici.

{p}
<b>Incantesimi di Gruppo</b>

D'altro canto, molti incantesimi benefici possono essere estesi all'intero gruppo. Tenendo premuto il clic destro sull'icona dell'incantesimo o sul vostro personaggio, estenderete le benedizioni a tutti i membri del gruppo presenti nel vostro campo visivo.

Tuttavia, tenete a mente che il costo in Punti Mana (PM) verrà moltiplicato per ciascun alleato coinvolto! Lanciare una potente cura di gruppo quando si hanno molti compagni può prosciugare la riserva magica in un istante, scatenando un violento contraccolpo arcano se non si presta la dovuta attenzione.

Coordinazione, maestria e lucidità: ecco i veri segreti di un incantatore di squadra!

***

<i>- Nel prossimo numero prenderemo lezioni pratiche di forgiatura runica per potenziare al massimo i nostri equipaggiamenti!</i>
"""

ADVWEEK_12 = """Settimanale dell'Avventuriero N. 12: Le Rune,L'Inviato di Lumiest Jaystar,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


In questo numero abbiamo affittato un laboratorio presso la Gilda dei Maghi per fare un'esperienza pratica di forgiatura runica. Piuttosto che perderci in lunghe dissertazioni teoriche, il caporedattore ha convenuto che fosse meglio illustrare il procedimento con un esempio concreto.
{p}
In sostanza, la forgiatura runica consiste nell'estrarre un incantamento da un pezzo d'equipaggiamento per poi incastonarlo su un altro manufatto. Chiunque voglia trarre il massimo dai propri pezzi troverà quest'arte affascinante, ma sono soprattutto le classi votate alle armi pesanti come i guerrieri a trarne i benefici più sbalorditivi.

Prendiamo i miei vecchi stivali d'argento di fattura miracolosa: sono un po' logori, ma possiedono una preziosa resistenza all'oscurità che vorrei trasferire sui miei nuovi stivali di cashmere. Sembra un'operazione semplice, non è vero?
{p}
<b>La Fusione della Runa</b>

Per estrarre l'incantamento serve un apposito crogiolo per rune. Si posiziona il crogiolo, vi si inserisce il pezzo da sacrificare e si batte il martello: l'equipaggiamento originale verrà polverizzato, ma lascerà dietro di sé una pietra runica contenente il suo incantamento migliore!

Attenzione: la qualità del crogiolo deve essere all'altezza dell'oggetto sacrificato (crogioli miracolosi per oggetti miracolo, e così via).

<b>L'Incisione Runica</b>

Ottenuta la runa, basta inciderla sul nuovo manufatto, a patto che questo disponga di slot per rune liberi. Se il pezzo ha spazio, la runa si legherà permanentemente ad esso, conferendogli la tanto agognata resistenza!

Con la giusta pazienza e una fornitura costante di rune, potrete forgiare panoplie d'armi e armature perfette, su misura per ogni nefia!

***

<i>- Nel numero della prossima settimana faremo un viaggio tra i festival e le festività più spettacolari di North Tyris!</i>
"""

ADVWEEK_13 = """Settimanale dell'Avventuriero N. 13: I Festival di Tyris,Caporedattore Hans,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Nel numero di questa settimana faremo una panoramica dei festival più memorabili di North Tyris. Non è una lista esaustiva, ma raccoglie le attrazioni più famose del continente, mete imperdibili per ogni viaggiatore che si rispetti!
{p}
<b>Marzo — Olvina — Il Festival del Canto della Luna</b>
Una celebrazione per commemorare la dea Odina, il cui supremo sacrificio rappresenta un faro per tutti noi. Ammirate lo splendore delle lune nel cielo sorseggiando vino pregiato, all'ombra dei ciliegi in fiore o cullati dalle acque calde delle sorgenti termali.

<b>Agosto — Palmia — La Notte dei Fuochi d'Artificio</b>
La capitale si illumina di mille colori sfavillanti mentre spettacoli pirotecnici rischiarano il castello reale. Mercanti da ogni terra allestiscono bancarelle con dolciumi, e l'intera città balla fino all'alba.

<b>Dicembre — Noyel — Il Santo Juremas</b>
La festa dell'inverno per eccellenza: il villaggio montano di Noyel si ricopre di candida neve e addobbi festosi per celebrare la dea della guarigione Jure. Scambi di regali, pupazzi di neve giganti e banchetti succulenti scaldano il cuore di viandanti e residenti.

Non perdete l'occasione di partecipare a queste celebrazioni: tra cibi esclusivi, manufatti rari e l'atmosfera di festa, ogni festival lascerà ricordi indelebili nel vostro diario di viaggio!

***

<i>- Nel prossimo numero affronteremo un tema delicato: le visite notturne delle succubi e come proteggere il proprio riposo!</i>
"""

ADVWEEK_14 = """Settimanale dell'Avventuriero N. 14: Le Succubi,Caporedattore Hans,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


L'uscita di questa settimana è sponsorizzata dalla guardia cittadina di Palmia.
{p}
Oscure! Misteriose! Seduttive!

Le succubi sono creature demoniache che si insinuano nei sogni degli ignari avventurieri durante la notte per prosciugarne l'essenza vitale. Quello che comincia come un sogno piacevole e conturbante può trasformarsi rapidamente in un risveglio traumatico, con attributi debilitati e un'orrenda sensazione di spossatezza!

Come può difendersi un viandante solitario mentre dorme?
{p}
<b>Rimedi Notturni</b>

La prima regola aurea è non dormire mai completamente all'aperto in zone selvagge senza precauzioni. Nel vostro rifugio domestico, l'uso di un cuscino marchiato con caratteri orientali posizionato capovolto terrà lontane le visite sgradite di succubi e compagni invadenti.

Inoltre, mantenere un livello di moralità elevato e dormire sotto coperte benedette riduce enormemente il rischio di cadere vittima di queste incursioni oniriche.

Se invece decidete deliberatamente di assecondare il fascino di una succube... beh, siete stati avvisati: la vostra anima e i vostri attributi primari potrebbero non tornare mai più quelli di prima!

***

<i>- Nel prossimo numero il Sergente Kzar ci illustrerà i vari stili di equipaggiamento in combattimento: due mani, scudo o arti marziali?</i>
"""

ADVWEEK_15 = """Settimanale dell'Avventuriero N. 15: Stili di Equipaggiamento,Sergente Kzar,10,1

<i>Benvenuti al Settimanale dell'Avventuriero, la rivista che tratta i temi più cari e vicini ai vostri cuori impavidi.</i>


Salute a voi, reclute! Hans mi ha chiesto di dare qualche dritta a voi novizi su come armarsi a dovere. Sul campo di battaglia non conta solo cosa avete addosso, ma soprattutto come lo impugnate: è la postura che decide il vostro destino tra la vita e la tomba.

Nel maneggiare le armi c'è un'enorme versatilità. Potete impugnare a due mani una spada corta o brandire un martello per mano: non sempre è l'ideale, ma se proprio insistete, chi sono io per fermarvi?

Dunque, cominciamo.
{p}
<b>Arma a Due Mani</b>
Impugnare una singola arma con entrambe le mani conferisce un bonus brutale ai danni fisici e alla penetrazione dell'armatura. L'ideale per spadoni pesanti, asce da guerra e lance lunghe. La difesa ne risente, ma se spaccate in due il nemico al primo fendente, non dovrete preoccuparvi della parata!

<b>Stile Scudo (Spada e Scudo)</b>
L'assetto classico del veterano. Uno scudo solido nella mano secondaria incrementa drasticamente il Valore di Protezione (VP), il Valore di Schivata (VD) e garantisce una percentuale di parata dei colpi. La potenza offensiva è inferiore, ma la vostra sopravvivenza nei dungeon più letali raddoppierà.
{p}
<b>Combattere a Due Armi</b>
Brandire un'arma in ciascuna mano consente di sferrare raffiche di colpi a ripetizione. Richiede una grande competenza nell'abilità specifica: all'inizio la precisione della mano secondaria sarà pessima, ma con la pratica diventerete un autentico mulinello di fendenti letali.

<b>Arti Marziali (Mani Nude)</b>
Non sottovalutate mai chi combatte a mani nude. Con nocche temprate e le giuste tecniche marziali, i colpi disarmati possono infliggere danni da impatto devastanti, stordire gli avversari e penetrare le corazze senza l'ingombro di un'arma metallica.

Scegliete lo stile che meglio si adatta alle vostre inclinazioni e addestratevi fino a farlo diventare una seconda natura!

***

<i>- Nel prossimo numero parleremo di armi da tiro: archi, balestre e armi da fuoco a confronto!</i>
"""

files_data = {
    'advweek_11.txt': ADVWEEK_11,
    'advweek_12.txt': ADVWEEK_12,
    'advweek_13.txt': ADVWEEK_13,
    'advweek_14.txt': ADVWEEK_14,
    'advweek_15.txt': ADVWEEK_15,
}

for fname, text in files_data.items():
    p = os.path.join(BOOK_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(text.strip() + '\n')

print("Applied Italian translations for Adventurer's Weekly 11 to 15")
