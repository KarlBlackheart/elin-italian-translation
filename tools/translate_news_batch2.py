"""
Translate News Batch 2: mysilia.txt and palmia.txt to Italian
"""
import os

NEWS_DIR = 'Lang/IT/Text/News'

MYSILIA_TEXT = """【Tragedia】Il Fanciullo Sognante Colpisce Ancora
Una cittadina di Mysilia è stata rasa al suolo senza lasciare traccia a causa della furia cieca scatenata da un Fanciullo Sognante. I sopravvissuti, disorientati e sotto shock, continuano a fissare sgomenti le rovine fumanti della loro città.
@ruin,UN_ephrond

Nuova Varietà d'Uva Rivoluziona l'Industria Vinicola
I viticoltori di Olvina sono riusciti a coltivare con successo una nuova varietà d'uva sfruttando le acque sorgive minerali. L'aroma fruttato e la fragranza inebriante promettono di dare vita a vini d'eccellenza assoluta.
@farm,UN_sio

Cerimonia Commemorativa per i Caduti
A Mysilia, terra profondamente segnata dai dieci anni di guerra, si è tenuta una solenne cerimonia di suffragio. La cittadinanza si è raccolta presso il sacrario civico per onorare la memoria degli eroi e dei propri cari scomparsi.
@city

L'Uscita sulle "Batterie Fiscali" Scatena la Polemica
"Un caloroso saluto a voi, mie care e patriottiche batterie fiscali di Palmia", ha esordito con sarcasmo il principe Efrond di Mysilia durante un'assemblea. Le sue parole caustiche hanno innescato una veemente ondata di sdegno tra i contribuenti.
@city,UN_ephrond

Rapporti Umani-Elea: Cresce la Discordia
I legami fraterni tra umani ed elea si fanno di giorno in giorno più gelidi. L'annuale festival congiunto della fioritura è stato bruscamente annullato a causa di insanabili attriti politici.
@city,UN_jonan

Miracolo al Cuore dell'Orfanotrofio di Mysilia
Una cassa ricolma di giocattoli intagliati e dolciumi prelibati è stata recapitata in forma anonima all'Orfanotrofio di Mysilia, asilo sicuro per i piccoli orfani di guerra. I fanciulli non hanno trattenuto le lacrime di gioia.
@farm,UN_lowell

L'Orfanotrofio Semina le Basi del Futuro
Accogliendo decine di bimbi provati dalle brutture del conflitto, l'Orfanotrofio di Mysilia ha avviato un programma agricolo comunitario per educarli all'autosufficienza e al lavoro della terra.
@farm,UN_lowell

Il Signore degli Elea Chiuso nel Dolore
Lord Cetrus, emblema dell'unità tra umani ed elea ed eroe leggendario della Guerra dei Dieci Anni, si è ritirato a vita privata dalla prematura scomparsa della sua consorte umana. Nessuno lo vede più in pubblico.
@ruin,UN_ineien

Zanan Protesta Ufficialmente Contro Mysilia
Il regno militare di Zanan ha indirizzato una dura nota diplomatica a Mysilia per aver concesso asilo politico al cavaliere esule Barrich. L'accaduto rischia di riaccendere pericolose tensioni internazionali.
@royal,UN_barrich

'Griffin' il Gufo Sventa il Colpo Notturno
Griffin, il fidato gufo reale di Lord Melvin, ha messo in fuga un ladro che tentava di forzare una finestra nel cuore della notte. Il malvivente è stato costretto alla ritirata tra sonore beccate e graffi.
@city,UN_melvin

Sconti Esclusivi alle Terme per gli Avventurieri
Olvina ha istituito una tariffa agevolata speciale per tutti gli avventurieri erranti. Sono già tantissimi i guerrieri che affollano le rinomate sorgenti termali per ristorare le membra doloranti dopo le battaglie.
@farm

Putit Randagio Vaga Cercando Famiglia
Un piccolo putit randagio continua a essere avvistato nei pressi dei casolari alla periferia di Mysilia. Chi lo ha visto sostiene che emetta pigolii malinconici, come se stesse cercando il suo padrone avventuriero mai tornato.
@farm
"""

PALMIA_TEXT = """Vascello Misterioso Attracca al Porto di Kapul
Questa mattina una nave non identificata, battente bandiera sconosciuta e con equipaggio misterioso, ha gettato l'ancora nel porto di Kapul. A bordo si scorgono macchinari sconosciuti: la milizia portuale ha aperto un'indagine formale.
@port,guard_m-1

Completato il Restauro delle Mura di Palmia
I lavori di riparazione dei bastioni del Regno di Palmia, gravemente danneggiati durante l'ultimo assedio, sono stati finalmente ultimati. La capitale può ora vantare una cinta muraria possente e rinnovata.
@gate,UN_nola

Preoccupazione per la Scarsità del Raccolto
Il tranquillo borgo contadino di Yowyn teme una significativa flessione nella resa delle colture stagionali. I sindaci dei comuni vicini invitano a razionalizzare le scorte di farina e cereali.
@farm

Valanga Travolge la Valle di Noyel
Il borgo montano di Noyel è stato investito da una violenta valanga che ha isolato decine di abitazioni. Le squadre di soccorso sono già al lavoro per liberare i sentieri sepolti dalla neve.
@snow,UN_zane

Scomparsa una Celebre Compagnia Musicale a Lumiest
Un'acclamata orchestra interamente composta da bardi elea è svanita nel nulla dall'oggi al domani nella città delle arti. Gli appassionati temono un rapimento o un ritiro spirituale improvviso.
@city

Il Bizzarro Fenomeno del Raduno dei Gatti
Nelle campagne di Yowyn si sta registrando uno strano fenomeno: centinaia di gatti randagi si radunano in cerchio nei fienili durante la notte, fissando il cielo stellato in assoluto silenzio.
@farm

Possiamo Ancora Sperare?
Il Regno di Palmia ha presentato un ambizioso piano di riforma integrale del sistema tributario. La cittadinanza oscilla tra il timore di nuovi balzelli e la speranza di un alleggerimento delle imposte.
@royal,UN_zane

I Cittadini Sognano Quotidiani Commestibili?
Una singolare proposta di stampare il Palmia Times su fogli d'amido commestibili per usarli come rancio d'emergenza in tempo di carestia è approdata nell'aula del Parlamento reale, scatenando risate e perplessità.
@royal,UN_xabi

Nuovo Aroma Esotico per la Birra Crim!
La Birra Crim ha lanciato la sua ultima creazione: la variante 'Spezie d'Oriente'. L'inedito equilibrio tra aromi speziati e note vellutate sta già spopolando nelle locande più rinomate.
@tavern

La Principessa Stasha Detta la Nuova Moda di Corte
La principessa Stasha, originaria di Mayroon, ha incantato la corte di Palmia sfoggiando il suo nuovo guardaroba. I sarti del regno hanno fatto a gara per replicare le sue elegantissime linee principesche.
@royal,UN_stasha

Sfida ai Fornelli Vinta dalla Principessa Stasha
La principessa Stasha ha dato prova delle sue eccezionali abilità culinarie preparando personalmente le portate di un banchetto a palazzo. I nobili sono rimasti estasiati dalle sue raffinate ricette.
@royal,UN_stasha

Cavallo di Yowyn Salva Viandante dai Mostri!
Un mercante rimasto intrappolato tra i predatori è stato tratto in salvo dal tempestivo intervento di uno stallone di Yowyn, che ha travolto le fiere permettendogli di fuggire. L'uomo ha promesso di prendersene cura a vita.
@farm

Esplode la Mania del Putit delle Nevi!
Il Putit delle Nevi, docile creatura tipica delle nevi di Noyel, è diventato il compagno domestico più ricercato del momento grazie alla sua irresistibile morbidezza e indole affettuosa.
@snow

La Travolgente Popolarità della Principessa Stasha
La grazia autentica e la spiccata affabilità della principessa di Mayroon hanno conquistato il cuore della nobiltà e del popolo, accrescendone enormemente il prestigio e l'influenza a corte.
@royal,UN_stasha

Caos a Corte: Nuovo Scandalo per il Principe
Il principe Xabi, visibilmente brillo durante un ricevimento a Kapul, ha lasciato cadere una compromettente lettera d'amore non indirizzata alla sua promessa sposa, la principessa Stasha. La corte attende spiegazioni ufficiali.
@royal,UN_xabi

Il Principe Agita Nuovamente le Acque
Il principe Xabi è stato colto in incontri riservati con la sua futura consorte Stasha. Pare tuttavia che il principe stesse unicamente consolando la nobildonna, sopraffatta dalla nostalgia per la propria terra natale.
@royal,UN_xabi

L'Eroe del Festival della Neve
Durante la festa della neve di Noyel, un'avventuriera di passaggio ha scolpito una magnifica scultura di ghiaccio che ha incantato grandi e piccini. Gli abitanti l'hanno acclamata a gran voce come paladina del festival.
@snow

Incubo Leoni Marini Ingordi: Scorte Sparite nella Notte
Porto Kapul fa i conti con un'insolita emergenza: i magazzini ittici sono stati ripuliti da una famelica colonia di leoni marini. La capitaneria recluta con urgenza avventurieri per allontanare le bestie.
@port

Lumiest Chiama gli Avventurieri al Festival Musicale
Lumiest, la splendida capitale della musica e delle arti, invita tutti i cantori e i viandanti a partecipare alla rassegna concertistica. Le gesta più epiche verranno immortalate in ballate immortali.
@tavern

Nuove Avventure Hanno Inizio!
La casa dei piaceri di Derphy sta registrando un'affluenza senza precedenti. La città senza legge, dove il brivido e la tentazione si intrecciano, è divenuta il nuovo teatro d'azione preferito da mercenari ed esploratori.
@tavern

La 'Fortune' Solca i Cieli Sopra Palmia
Fortune Bell, la prima nave-casinò volante di Palmia, solca i cieli per esibire la grandezza tecnologica del Nuovo Regno. In sinergia con la storica casa da gioco 'Fortune Cookie', l'aeronave promette emozioni sfrenate per tutti gli scommettitori.
@casino

Preoccupazione tra i Cittadini per il Casinò Volante
L'aeronave da gioco 'Fortune Bell' suscita non pochi timori tra la popolazione di Palmia. Il terrore che un simile colosso d'acciaio possa precipitare sulle case ha portato molti a ribattezzarla 'la bomba celeste'.
@casino

La Sorte Chiama gli Ex-Armigeri tra le Nubi
La società "Fortune Cookie", che gestisce il casinò volante del Nuovo Regno, sta reclutando massicciamente ex guardie cittadine per il servizio di sicurezza di bordo. Re Zane ha espresso viva soddisfazione per la crescita dell'occupazione.
@casino,UN_zane,guard_m-1
"""

files_data = {
    'mysilia.txt': MYSILIA_TEXT,
    'palmia.txt': PALMIA_TEXT,
}

for fname, text in files_data.items():
    p = os.path.join(NEWS_DIR, fname)
    with open(p, 'w', encoding='utf-8') as fp:
        fp.write(text.strip() + '\n')

print("Applied Batch 2 translations to News (mysilia.txt and palmia.txt)")
