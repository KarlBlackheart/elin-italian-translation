"""
Translate all scrolls in Lang/IT/Text/Scroll/ to Italian.
"""
import os

SCROLL_DIR = 'Lang/IT/Text/Scroll'

SCROLLS = {
    'dontread.txt': """Non leggere questo
{center}

<i>Ti avevo avvertito.</i>
""",

    'farthest_sea.txt': """Il Mare Più Remoto,,0
{center}

Il faro si ergeva sul promontorio solitario, guidando le anime smarrite.
""",

    'goround.txt': """Girotondo,,0
{center}

Gira, gira in tondo, finché il mondo non crolla ai tuoi piedi.
""",

    'letter_crimale.txt': """Ringraziamento e Dono di Birra Crim,Loytel,0

Ti scrivo questa lettera nella speranza che ti trovi in ottima salute.

Desidero rinnovare la mia più profonda gratitudine per il tuo continuo supporto nel saldare quello che all'inizio era soltanto il mio personale debito finanziario. La tua generosità rappresenta un debito di ben altra natura... uno che non si ripaga facilmente.

Sebbene la nostra conoscenza sia ormai profonda, come recita l'adagio, anche la vera amicizia deve osservare le dovute cortesie. Ho voluto cogliere questa occasione per manifestarti formalmente la mia riconoscenza, accludendo una bottiglia di pregiata Birra Crim distillata a Lumiest.

Sarei sommamente onorato se dovesse incontrare il tuo gradimento.

Con l'augurio di una salute radiosa e di continui successi in ogni tua impresa.

Con sincera stima,
Loytel
Ex Ispettore di Frontiera di Mysilia
""",

    'letter_ether.txt': """Una Malattia Ignota,,0
{center}

Se dovessi contrarre la Malattia dell'Etere, bevi questa pozione.

Si sa ancora pochissimo di questo morbo. Sembra manifestarsi quando una sostanza misteriosa chiamata etere si accumula nel corpo.

Purtroppo pare che persino l'aria che respiriamo ne contenga tracce microscopiche. La fine dell'umanità potrebbe essere vicina.
""",

    'letter_juremas.txt': """[pubblicità] Buon Juremas!,Chiesa di Jure,0
{center}

Nel nome della nostra splendida dea della guarigione, Jure,
ti elargiamo questi sacri doni in occasione della santa notte.

Questi sontuosi articoli, naturalmente, non sono che una minuscola goccia nell'oceano infinito della grandezza di Jure.

Rendiamo grazie per la sconfinata compassione della dea
e ricorda di nominarla ogni giorno nelle tue preghiere!
""",

    'letter_love.txt': """Ti ricordi?,,0

{center}

Questo fu il giorno in cui stringesti la mia mano.
""",

    'letter_magic_chest.txt': """Un Dono di Commiato,Ashland,0

È passato un po' di tempo, vero, #pc? Come te la passi?

Io e Fiama stiamo attualmente soggiornando al Forte del Salice, sotto la reggenza di Lord Cetrus. La nostra partenza è stata un po' affrettata e non abbiamo avuto modo di congedarci come si deve, ma permettimi di cogliere questa occasione per esprimerti la mia gratitudine per tutto l'aiuto e le informazioni che ci hai fornito.

A proposito, il tuo fidato forziere non sta forse diventando un po' troppo stretto con tutti gli oggetti e i materiali che raccogli durante le esplorazioni?

Mi è capitato di trovare qualcosa di molto interessante al Forte del Salice, e ho pensato di mandartelo. Si chiama "Baule di Stoccaggio" — un nome semplice, ma è un capolavoro forgiato dai mastri artigiani degli Uomini delle Colline. Spero possa rivelarsi utile nelle tue future avventure.

P.S.
Sembra che questo baule possa essere ulteriormente potenziato. Se durante i tuoi viaggi avrai la fortuna di incontrare un artigiano delle Colline, non esitare a chiedergli informazioni.
""",

    'letter_trial.txt': """Lettera di Raccomandazione per l'Accademia,un mago mercante,0
{center}

Con la presente si certifica che
il possessore di questa missiva
è un degno membro della Gilda dei Maghi.

Con tutto il mio affetto,
""",

    'letter_vampire.txt': """Caro Amico,,0
{center}

Fuggi la luce del sole...
L'ombra dei tetti e delle fronde ti scherma dalla sua furia bruciante...

Quando la strada si fa lunga, assumi la forma di un pipistrello...
Questo dono già ribolle nel tuo sangue...

Il cibo dei mortali non può più sostenerti...
Cerca il sangue: il tuo unico vero nutrimento...

Non dimenticare la tua sete...
La fame è la bussola che ti guiderà...

Seconda il tuo desiderio...
La notte appartiene solo a te...
""",

    'lutz_1.txt': """Diario di Lutz - Volume 1,Lutz l'Ex Eroe,0

Forse quel titolo di "ex eroe" non è mai stato altro che una beffa. Tutto ciò in cui credevo poggiava su una menzogna. Quando ho sentito il fragore del crollo, ho pensato di dire addio a questo mondo per sempre.

Poi, per qualche misterioso motivo, sono rimasto incantato dagli occhi tondi e innocenti di Mii-Chan, la foca ingorda. Nel suo sguardo ho scorto un minuscolo barlume di speranza, la promessa di un paradiso. Così ho deciso: partiremo alla ricerca della terra promessa, soltanto noi due.

Ora vivo di ciò che offre la terra in una foresta remota, preparandomi per il grande viaggio che ci attende.

Chissà a chi giungerà questa lettera, scritta nel cuore di una notte insonne... Non vedo l'ora di scoprirlo.

- Lutz, l'Ex Eroe nella Foresta Remota
""",

    'lutz_2.txt': """Diario di Lutz - Volume 2,Lutz l'Ex Eroe,0

La vita nella foresta non è affatto male. Le noci degli arbusti di Api <color=green>si conservano a lungo</color>, e ci sono <color=green>funghi</color> e <color=green>germogli di bambù</color> in abbondanza per riempire la pancia di Mii-Chan.

Ciò che mi affascina di più sono i <color=green>nidi di animali</color>. Di tanto in tanto vi trovo uova feconde, tanto ambite dai mercanti itineranti. Una mattina, un uovo che avevo lasciato sul mio giaciglio di paglia <color=green>si è schiuso</color>, dando alla luce un cucciolo di scoiattolo gigante. Sono un po' preoccupato per la gelosia di Mii-Chan, ma sono sicuro che diventerà un compagno fedele.

Circondato da Ris-Chan e Mii-Chan, ho trovato un frammento di serenità.

Alla prossima lettera.

- Lutz, l'Ex Eroe nella Foresta Remota
""",

    'lutz_3.txt': """Diario di Lutz - Volume 3,Lutz l'Ex Eroe,0

Il sole estivo scalda la spiaggia dorata, e Mii-Chan e Ris-Chan stanno schiacciando un pisolino tranquilli accanto a me. Io dondolo dolcemente sull'amaca con un bicchiere di succo di Palulu in mano.

È semplicemente perfetto. Credo proprio che venire qui sia stata la scelta giusta. Trovare questo luogo appartato dopo aver lasciato la foresta ed essermi spinto un po' oltre... deve essere stato un disegno del destino.

La prossima volta ti racconterò qualcosa di più su questa spiaggia.

- Lutz, l'Ex Eroe nella Foresta Remota
""",

    'lutz_4.txt': """Diario di Lutz - Volume 4,Lutz l'Ex Eroe,0

La vita in riva al mare ha un fascino tutto suo. Disponendo un po' di <color=green>polpa di cactus</color> e qualche <color=green>alga</color> su un piatto, sembra quasi di trovarsi in una stazione balneare di lusso. Con le <color=green>grandi foglie</color> degli alberi di Palulu posso ricavare piatti improvvisati, e le <color=green>spine di cactus</color> sono ottimi stuzzicadenti.

C'è anche del <color=green salgemma</color>, ma estrarlo è un'impresa disperata. Il mio vecchio piccone non riesce nemmeno a scalfirlo. Ma non ho alcuna intenzione di usare l'impossibile come scusa. Troverò una soluzione.

Alla prossima lettera.

- Lutz, l'Ex Eroe nella Foresta Remota
""",

    'lutz_5.txt': """Diario di Lutz - Volume 5,Lutz l'Ex Eroe,0

A volte mi domando se queste lettere giungeranno mai nelle mani di qualcuno, o se siano destinate a dissolversi nell'oblio, ignorate e dimenticate per sempre.

In ogni caso non importa. Che cosa lascio dietro di me in questo mondo, chi mai potrà trovarlo o che cosa penserà... non ha alcuna reale importanza.

- Lutz, l'Ex Eroe nella Foresta Remota
""",

    'lutz_6.txt': """Diario di Lutz - Volume 6,Lutz l'Ex Eroe,0

Gli attrezzi come i picconi possiedono una proprietà fondamentale chiamata durezza. Un piccone forgiato con un materiale resistente può frantumare persino i filoni di ferro, ma con un piccone di legno, a meno che tu non sia un minatore leggendario, non riuscirai a scalfire nemmeno la roccia comune.

È giunto il momento di fare ritorno al mio accampamento nella foresta. Se userò quel blocco di basalto nero che conservavo per le grandi occasioni, dovrei riuscire a fabbricare un piccone capace di scavare quel blocco di salgemma.

- Lutz, l'Ex Eroe nella Foresta Remota
""",

    'lutz_7.txt': """Diario di Lutz - Volume 7,Lutz l'Ex Eroe,0

Esplorando la spiaggia ho scoperto un antico congegno sepolto nella sabbia. Uno strano apparecchio che, inserendovi una scatoletta chiamata "<color=green>cassetta</color>", diffonde nell'aria una melodia bizzarra. Mii-Chan, dapprima spaventata, ora ascolta rapita e silenziosa.

Ho anche costruito un barbecue di pietra. Questa spiaggia è diventata la nostra seconda casa. Seduto accanto al fuoco, ascoltando musiche d'altri tempi, ho desiderato che il tempo si fermasse, anche solo per un istante. Ma un'inquietudine profonda dentro di me non lo concede. Devo trovare la terra promessa. Dove potrà mai essere?

- Lutz, l'Ex Eroe nella Foresta Remota
""",

    'lutz_8.txt': """Diario di Lutz - Volume 8,Lutz l'Ex Eroe,0

Chissà se qualcuno sta davvero leggendo le mie lettere. Se "tu" stai leggendo queste righe, per quale ragione lo fai? Semplice passatempo? O speravi di trovarvi una qualche rivelazione?

Se hai a cuore i miei diari, fammi un favore: buttali via. Anzi, c'è un modo ancora migliore.

Quando hai bisogno di sbarazzarti di ciarpame o scartoffie accumulate, un <color=green>martello</color> è l'attrezzo ideale. Riducendo le cose in frantumi, puoi trasformarle in qualcosa di completamente nuovo. Quindi impugna un <color=green>martello</color> e distruggi i miei diari. Frantumali con tutte le tue forze. Forse così queste pagine avranno avuto un briciolo di senso.

- Lutz, l'Ex Eroe nella Foresta Remota
""",
}

for fname, content in SCROLLS.items():
    p = os.path.join(SCROLL_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(content.strip() + '\n')

print(f"Translated all {len(SCROLLS)} scrolls in {SCROLL_DIR}")
