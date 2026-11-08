"""
Translate News Batch 1: faith.txt, food.txt, guild.txt, world.txt, reserved.txt
"""
import os

NEWS_DIR = 'Lang/IT/Text/News'

FAITH_TEXT = """Guarigione Miracolosa alla Chiesa di Noyel
Nella chiesa di Noyel, un abitante gravemente malato è guarito miracolosamente nel corso della notte. Intervento divino o potente incantesimo? Si dice che sul pavimento della navata sia stata rinvenuta una singola piuma candida di rara bellezza.
@snow

La Truffa delle Piume Divine
Piume fasulle della Dea della Guarigione stanno inondando i mercati neri di tutta Tyris. L'arcivescovo di Palmia ha rilasciato una dichiarazione perentoria: "Le autentiche piume di Jure non profumano affatto di pollo fritto."
@city

Sermone Eccentrico a Derphy
Ieri a Derphy, un predicatore ambulante di Kizuami ha tenuto un'omelia infuocata sostenendo che "il furto non è che una redistribuzione accelerata della grazia divina". È stato applaudito a scena aperta da mezza città prima di venire derubato del suo stesso saio.
@derphy

La Statua Piangente di Opatos
Numerosi minatori giurano che la statua del dio della terra Opatos nella miniera di Vernis abbia versato lacrime dorate. I sacerdoti invitano alla calma: potrebbe trattarsi di semplice condensa minerale o dell'imminente collasso della galleria.
@vernis

Corsa alle Offerte nel Festival del Raccolto
I fedeli di Kumiromi si contendono il primato delle offerte più ricche. Frutti dalle dimensioni titaniche e ortaggi rari si accumulano sugli altari campestri tra canti devozionali e danze della fertilità.
@yowyn

Il Mistero del Vento Sacro
Una brezza insolitamente calda e profumata ha soffiato improvvisamente attraverso le pianure, scompigliando i veli delle sacerdotesse di Lulwy. Molti avventurieri sostengono che sia il presagio di un favore divino imminente per gli arcieri di Tyris.
@field

Sussurri Meccanici nei Sotterranei
Rumori ritmici di ingranaggi e pistoni a vapore sono stati avvertiti nei pressi dell'antico santuario di Mani. Gli studiosi ritengono che l'orologio dell'apocalisse abbia appena fatto scattare un altro dente.
@dungeon

Rissa Teologica alla Locanda
Una disputa accesasi tra due mercanti riguardo alla superiorità spirituale tra la fortuna di Ehekatl e il rigore di Mani si è conclusa con il lancio reciproco di boccali di birra e l'intervento della guardia cittadina.
@inn

L'Apparizione del Gatto Bianco
Un felino dal pelo immacolato e dallo sguardo ipnotico è stato avvistato seduto sopra l'altare della dea della fortuna. I testimoni che hanno accarezzato il micio hanno riferito di aver vinto subito dopo alla lotteria di Palmia.
@palmia

Preghiere Notturne a Olvina
Le campane del tempio di Olvina hanno suonato spontaneamente a mezzanotte. I sacerdoti riferiscono di visioni celesti e raccomandano ai fedeli di rinnovare le proprie promesse d'affetto prima del prossimo plenilunio.
@olvina

Il Dono della Pioggia Purificatrice
Dopo settimane di afa asfissiante, una pioggia tiepida e cristallina è scesa sui campi assetati subito dopo la conclusione di un rito propiziatorio. I contadini festeggiano gridando al miracolo.
@farm

La Profezia dell'Etere
Un eremita sceso dai picchi montuosi ha gridato terribili moniti riguardo al prossimo Vento d'Etere, esortando tutti a fare scorta di pozioni curative e a non sfidare la furia degli elementi a cielo aperto.
@wild

Il Coro degli Angeli di Luce
Voci soavi e celestiali sono state udite risuonare tra le rovine di un antico tempio abbandonato. Chi ha ascoltato il canto riferisce una sensazione di pace assoluta e la scomparsa di ogni affanno corporeo.
@ruins

Contesa per la Reliquia Sacra
Un frammento ligneo che si narra appartenesse all'aratro primordiale del dio del raccolto è stato messo all'asta a prezzi astronomici, attirando emissari clericali e ricchi collezionisti da ogni angolo del continente.
@city

La Benedizione delle Acque Termali
I visitatori delle sorgenti calde sostengono che immergersi durante i giorni consacrati alla dea Jure raddoppi la vitalità e doni alla pelle una morbidezza soprannaturale.
@hotspring
"""

FOOD_TEXT = """Il Potage di Cabocchi e Imo Scalda Cuore e Corpo
Il semplice potage del Bistro Sierra sta spopolando. L'armonia perfetta tra dolcezza e vellutata ricchezza, unita a una consistenza morbida e aromatica, manda in estasi gli avventori di tutta la regione.
@food

Un Grande Chef Esplora il Fascino del Frutto Arcobaleno
Ricco di colori sgargianti e sfumature gustative mutevoli, la "gemma commestibile" sta conquistando i ristoranti d'alta classe. Ogni singolo boccone riserva una sorpresa inaspettata per il palato.
@gourmet

Allarme Salgemma nelle Miniere
La domanda di salgemma purissimo è alle stelle per la preparazione dei migliori prosciutti stagionati. I cuochi di corte offrono ricompense generose a qualsiasi minatore disposto a estrarre i filoni più compatti.
@mining

L'Invasione della Birra Crim di Lumiest
I barili dell'ambita Birra Crim sono giunti nei porti commerciali. Gli osti avvertono la clientela: "L'aroma è dolce e irresistibile, ma il doposbronza non perdona nessuno!"
@alcohol

La Moda dei Pasticcini Macaron
Colorati, friabili e deliziosi: le signore della nobiltà fanno la fila davanti alle migliori pasticcerie per accaparrarsi le ultime scatole di macaron glassati.
@sweets

Cucina d'Avventura: Come Arrostire Mostri con Gusto
Una guida gastronomica clandestina spiega come marinare le carni delle bestie selvatiche per renderle tenere e saporite sul falò da campo, evitando di intossicarsi con ghiandole velenose.
@wilderness

La Sagra dell'Uovo Termale
Decine di viaggiatori si radunano attorno ai vapori sulfurei per gustare le celebri uova cotte a bassa temperatura nell'acqua di sorgente, servite con un pizzico di sale e salsa di soia.
@tourist

Scandalo nei Ristoranti: Zuppe Annacquate
La gilda dei buongustai ha smascherato una bettola di periferia che allungava i brodi pregiati con semplice acqua di palude. L'oste è stato costretto a consumare l'intero pentolone per punizione.
@town
"""

GUILD_TEXT = """"Non siamo baby-sitter per Yeek!"
Gli avventurieri di Kapul, stanchi delle continue missioni di sterminio mostri di basso rango, hanno proclamato uno sciopero pubblico. Il pomo della discordia è l'abitudine della Gilda dei Guerrieri di appaltare a oltranza la caccia agli Yeek.
@city,UN_guild_doorman_fighter,UN_guild_master_fighter

Furto con Scasso al Deposito della Gilda dei Ladri
Un ladro sconosciuto è riuscito nell'impresa paradossale di svaligiare la cassaforte della stessa Gilda dei Ladri di Derphy. Il capo gilda ha promesso una taglia monumentale e un posto da ufficiale a chiunque riesca a rintracciarlo.
@derphy,thief

La Gilda dei Maghi e la Crisi della Carta da Pergamene
La carenza di cellulosa raffinata sta facendo lievitare il prezzo dei tomi magici a Lumiest. Gli incantatori apprendisti protestano per il costo esorbitante dei quaderni d'esercitazione.
@lumiest,mage

Nuovi Criteri per l'Accesso al Rango d'Oro
I maestri d'arme hanno annunciato che da questo mese non basterà più mostrare teste di goblin: per ottenere le licenze superiori sarà obbligatorio superare un duello contro un automa d'addestramento.
@guild

Taglie da Capogiro sui Banditi delle Foreste
La bacheca della Gilda dei Guerrieri si è arricchita di nuovi manifesti con taglie astronomiche sui predoni che assaltano le carovane mercantili lungo la via per Palmia.
@fighter

Esplosione Misteriosa nei Laboratori Arcani
Un esperimento di trasmutazione elementale è sfuggito di mano nella sala comune degli stregoni, tingendo di viola fosforescente la barba di tutti i presenti per i prossimi tre mesi.
@magic

Contrabbando di Oggetti Rubati a Bordo dei Carri
Le guardie cittadine hanno intensificato le perquisizioni alle porte, ma i membri della gilda furtiva continuano a far passare merci marchiate celandole sotto strati di letame e paglia.
@gate

Duello d'Onore tra Campioni
Due celebri spadaccini della Gilda dei Guerrieri si sono affrontati nell'arena municipale. Lo scontro si è concluso con la rottura simultanea di entrambe le lame e un caloroso abbraccio tra gli applausi della folla.
@arena

Sciopero dei Fabbri di Corporazione
I maniscalchi affiliati alla gilda hanno incrociato le braccia richiedendo forniture garantite di carbone e minerale di ferro di prima qualità per forgiare le armature dei veterani.
@smithy
"""

WORLD_TEXT = """Forti Raffiche di Vento d'Etere Annunciate a Nord
Gli osservatori astronomici segnalano una perturbazione eterea in avvicinamento sui rilievi montuosi settentrionali. Si raccomanda ai viaggiatori di rifugiarsi tempestivamente nei ripari al chiuso non appena l'aria assumerà la tipica sfumatura verdastra.
@weather

Crescita delle Esportazioni tra Città-Stato
I convogli commerciali registrano volumi record di scambio merci tra Vernis e Palmia. Il flusso di minerali grezzi in cambio di generi di lusso e granaglie ha rinvigorito i mercati rionali.
@economy

Riaperta la Strada per la Costa
I genieri hanno finalmente sgombrato le frane che ostruivano il valico litoraneo, consentendo il regolare transito delle diligenze e dei carri pesanti diretti verso i villaggi costieri.
@travel

Misteriosi Crolli nelle Rovine Sommersi
Pescatori locali riferiscono di aver udito boati sottomarini e di aver visto dense bolle emergere dalle profondità della baia, alimentando leggende sul risveglio di antiche creature titaniche.
@sea

Aumento della Presenza di Mostri Erranti
I guardiacaccia avvisano la popolazione che l'attività delle bestie selvatiche è insolitamente intensa ai margini delle boscaglie. Si sconsiglia vivamente ai civili disarmati di avventurarsi fuori dalle mura dopo il tramonto.
@danger

Fervono i Preparativi per le Grandi Fiere Stagionali
Mascotte, giocolieri e mercanti ambulanti stanno affluendo nelle piazze principali per allestire le bancarelle in vista dell'annuale fiera patronale, con grandi aspettative per l'indotto turistico.
@festival
"""

RESERVED_TEXT = """Spazio Riservato alla Redazione
Questo spazio è temporaneamente riservato per le comunicazioni straordinarie del Palmia Times.
@general
"""

files_data = {
    'faith.txt': FAITH_TEXT,
    'food.txt': FOOD_TEXT,
    'guild.txt': GUILD_TEXT,
    'world.txt': WORLD_TEXT,
    'reserved.txt': RESERVED_TEXT,
}

for fname, text in files_data.items():
    p = os.path.join(NEWS_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(text.strip() + '\n')

print("Applied Batch 1 translations to News")
