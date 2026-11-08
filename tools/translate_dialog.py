import openpyxl

dialog_it = {
    'default': (
        "Non ho niente da fare.\n"
        "Eh? Che cosa vuoi?\n"
        "Sei un tipo dall'aspetto davvero singolare.\n"
        "Non succede mai nulla di interessante da queste parti.\n"
        "Mmm... che giornata tranquilla.\n"
        "Hai sentito le ultime voci di corridoio?\n"
        "Prenditi un momento per riposare.\n"
        "Il mondo là fuori è pieno di pericoli."
    ),
    'interest_economy': (
        "Mi appassiona molto l'economia.\n"
        "Il denaro e le valute sono la vera linfa vitale del mondo.\n"
        "Hai mai provato a investire nei negozi locali? I mercanti migliorano le loro merci se hanno fondi a disposizione!\n"
        "Il prezzo delle merci fluttua a seconda della domanda e dell'offerta delle varie città.\n"
        "Un commerciante accorto viaggia sempre con carovane ben protette per evitare i banditi lungo la via."
    ),
    'interest_science': (
        "Adoro discutere di scienza e innovazione.\n"
        "La tecnologia di Eyth Terre era incredibilmente avanzata, quasi magica per chi non la comprende.\n"
        "Gli Yerles sono riusciti a ricreare le antiche armi da fuoco studiando i rottami del Cyberdome.\n"
        "L'ingegneria e la meccanica possono risolvere problemi che nemmeno i più potenti incantesimi riescono a scalfire."
    ),
    'interest_travel': (
        "Amo viaggiare per il mondo, ho visitato tantissimi luoghi straordinari.\n"
        "La città di Lumiest è celebre per le sue fontane scintillanti e per l'accademia arcana degli artisti.\n"
        "Se ti dirigi a sud, fai molta attenzione ai ladri che infestano i dintorni di Derphy.\n"
        "I panorami di Tyris sono magnifici, ma viaggiare senza scorte di cibo può trasformare un'avventura in una tragedia."
    ),
    'interest_world': (
        "Seguo sempre con grande interesse le vicende della politica mondiale.\n"
        "Eulderna è una potenza antica e orgogliosa, ma i conflitti interni ne minano la stabilità.\n"
        "I rapporti diplomatici tra Palmia e Mysilia sono sempre sul filo del rasoio.\n"
        "Molti temono che le ombre del passato stiano per riemergere dalle rovine dimenticate."
    ),
    'interest_religion': (
        "La fede negli dei è la cosa più preziosa che abbiamo.\n"
        "Le nostre vite sarebbero vuote e insignificanti senza la guida e la grazia divina.\n"
        "Pregare con costanza e fare sacrifici graditi sull'altare è il modo migliore per ottenere il favore di un dio.\n"
        "Attento a non cambiare divinità con leggerezza: l'ira di un dio tradito può perseguitarti a lungo!"
    ),
    'interest_human': (
        "Gli Elea ci hanno abbandonati a noi stessi durante la Guerra dei Dieci Anni.\n"
        "Non mi fido affatto di chi vive isolato nelle foreste pretendendo di essere superiore agli altri.\n"
        "La cooperazione tra gli insediamenti umani è l'unica cosa che ci ha permesso di sopravvivere finora."
    ),
    'interest_elea': (
        "Gli umani dovrebbero imparare la virtù dell'umiltà e rispettare l'antico equilibrio naturale.\n"
        "Dovremmo ascoltare con maggiore attenzione il respiro della terra e i sussurri del vento.\n"
        "L'uso sconsiderato di artefatti corrotti porterà solo nuove calamità su tutta Ylva."
    ),
    'shopkeeper': (
        "Benvenuto nella mia bottega!\n"
        "Abbiamo la migliore selezione di merci di tutta la zona.\n"
        "C'è qualcosa in particolare che cattura il tuo sguardo?\n"
        "Se hai oggetti di valore da vendere, sono sempre pronto a fare affari!"
    ),
    'guard': (
        "Il nostro dovere primario è proteggere i cittadini e mantenere l'ordine.\n"
        "Fai rapporto immediatamente a me se noti criminali, mostri o attività sospette.\n"
        "Occhio a non sguainare le armi in città senza motivo, non tolleriamo risse.\n"
        "Che la giustizia e l'ordine regnino sovrani."
    ),
    'banker': (
        "La sicurezza del tuo denaro è più importante di ogni altra cosa.\n"
        "I nostri forzieri sono impenetrabili e garantiti contro qualsiasi malintenzionato.\n"
        "Vuoi depositare una somma al sicuro o effettuare un prelievo per le tue spese?"
    ),
    'bitch': (
        "Ehi tesoro... hai voglia di rilassarti un po' in dolce compagnia?\n"
        "Una pausa piacevole è proprio quello che ci vuole dopo una dura giornata di fatiche."
    ),
    'slaver': (
        "He he he... Credo di avere esattamente la merce che fa al caso tuo.\n"
        "Non fare complimenti, vieni a dare un'occhiata: braccia forti per lavorare o guardie del corpo addestrate a tutto."
    ),
    'bored': (
        "(#me ha un'aria decisamente annoiata.)\n"
        "(#me ti lancia una rapida occhiata distratta e fa un passo indietro con indifferenza.)\n"
        "(#me sospira rumorosamente guardando verso l'orizzonte.)"
    ),
    'hint': (
        "Si dice che le code di coniglio portino fortuna a chi le mangia. Non mangiarle se sono marce però!\n"
        "I grimaldelli sono costosi. Conservali con cura e impara bene i rudimenti dello scassinamento!\n"
        "I minerali estratti dalle pareti rocciose possono essere forgiati in lingotti o venduti ai mercanti.\n"
        "Dormire su un letto soffice e confortevole accelera la crescita del potenziale delle tue abilità.\n"
        "Se vieni colto dal Vento dell'Etere, rifugiati subito in un riparo solido prima che il morbo si aggravi!\n"
        "Fai attenzione a ciò che mangi: il cibo andato a male può provocare gravi intossicazioni alimentari.\n"
        "Puoi addomesticare animali e creature selvagge offrendo loro cibo e usando le abilità adatte."
    ),
    'fortune': (
        "Se veneri Kumiromi, potresti trovare semi preziosi all'interno dei frutti.\n"
        "Se possiedi un'elevata resistenza all'illusione, sarai protetto dagli attacchi di follia.\n"
        "Benedire i bastoni magici è un'ottima idea: le cariche aumenteranno e il potere sarà più stabile.\n"
        "Mentre sei bagnat#o, subisci pochissimi danni da fuoco, ma i colpi di fulmine ti faranno molto più male!\n"
        "Vomitare troppo frequentemente porta rapidamente all'anoressia. In caso di malattia, idratati con bevande nutrienti.\n"
        "Le pozioni benedette di ripristino attributi potenziano temporaneamente il corpo e la mente oltre i loro limiti normali.\n"
        "Contro i nemici più temibili, prova a lanciare addosso a loro pozioni maledette per indebolirli drasticamente!"
    ),
    'fortune_false': (
        "Si dice che esista un anello portentoso in grado di far spuntare un dito in più sulla mano.\n"
        "Lasciare i bastoni a terra per un po' li farà ricaricare magicamente da soli... o forse no!\n"
        "Non sai cosa desiderare? Prova a chiedere l'antico tesoro segreto di Milas!\n"
        "Girano voci che le guardie cittadine apprezzino molto essere caricate a testa bassa mentre sei nudo.\n"
        "C'è chi sostiene che uccidere i gatti porti una sfortuna tremenda per tutta la vita.\n"
        "Si mormora dell'esistenza di un artefatto leggendario utilizzabile esclusivamente dalla tua sorellina.\n"
        "I mercanti pagano a peso d'oro gli escrementi di mostro se sono particolarmente pesanti!\n"
        "Bere il sangue di Hermes senza prima averlo benedetto potrebbe riservare spiacevoli sorprese."
    ),
    'mayor': (
        "Per qualsiasi pratica burocratica o documento ufficiale, rivolgiti alla mia segretaria.\n"
        "Di che cosa hai bisogno? Sono un uomo estremamente occupato.\n"
        "Gli investimenti per la crescita e il prestigio della nostra cittadina sono sempre i benvenuti."
    ),
    'secretary': (
        "Desidera effettuare un investimento a beneficio dello sviluppo della città?\n"
        "Come posso esserle utile quest'oggi?"
    ),
    'bottle': (
        "Lucia|La Nave Mai Tornata|Se questa bottiglia raggiungerà le mani di qualcuno, probabilmente sarò già in fondo all'oceano. Ma il cielo oggi era così limpido e azzurro.\n"
        "Un Soldato Senza Nome|Ultima Lettera|La paura pesava molto più della mia spada. Eppure voglio che qualcuno sappia che non sono fuggito.\n"
        "Ernes|Preghiera della Risacca|O Dio, se non puoi placare il furore delle onde, concedimi almeno un sonno sereno.\n"
        "Mireille|La Riva Promessa|Se arriverò per prima sulla costa, accenderò un falò e ti aspetterò. Raggiungimi senza smarrire la via.\n"
        "Il Navigatore Daros|Il Registro delle Stelle|Le stelle avevano ragione anche stanotte. Quello che ha commesso un errore sono stato io.\n"
        "Selena|Una Modesta Confessione|Non ho mai avuto il coraggio di pronunciare il tuo nome ad alta voce. È questo il mio unico rimpianto.\n"
        "Un Vecchio Marinaio|Ai Miei Giorni di Gioventù|Il mare ti toglie molto, ma nulla va interamente sprecato. Sopravvivi.\n"
        "La Gemella Minore|Metà del Mondo|Fratello mio, metà del mondo è ancora qui ad aspettarti. Ti supplico, torna a casa sano e salvo.\n"
        "Il Medico di Bordo Renato|Appunti Medici|Non sono riuscito a richiudere le ferite, ma ho alleviato le loro sofferenze. È stato sufficiente.\n"
        "Isabelle|Continua la Melodia|Anche se io non ci sarò più, ti prego: canta questa canzone fino all'ultima nota.\n"
        "Il Contrabbandiere Kyle|Il Luogo del Bottino|L'oro è sepolto sul fondale dell'insenatura a nord. Immergiti se hai il fegato di prenderlo.\n"
        "L'Accolito Roa|Confessione di Dubbio|Le mie suppliche non hanno ricevuto risposta. Ciononostante, non smetterò mai di pregare.\n"
        "Il Pescatore Hald|L'Ultima Uscita|Oggi le reti sono rimaste vuote. Ma ho avuto modo di parlare a lungo con il mare.\n"
        "Il Viandante Cyan|Un Punto di Passaggio|Questa non è la fine del cammino. È soltanto una tappa di passaggio.\n"
        "Lo Scriba Reale|Stralcio dagli Atti Ufficiali|Il vascello è andato perduto nel cuore della tempesta. Fine del rapporto.\n"
        "Una Madre|Al Mio Bambino|Ricordati di allacciare bene il mantello quando soffia il vento freddo. Promettimelo.\n"
        "Il Bardo Fey|Poema Incompiuto|Manca l'ultima rima baciata. A chiunque troverà questo foglio: tocca a te completarla.\n"
        "Il Capitano Volk|Ordine di Ritirata|Tornate a casa tutti vivi. All'onore e alla gloria penseremo quando saremo salvi.\n"
        "Una Bambina|Il Mio Primo Viaggio|Ho un po' di paura del buio. Però è davvero un'avventura emozionante!\n"
        "Qualcuno|A Chiunque Trovi Questo Messaggio|Se stai leggendo queste righe, significa che il mondo continua ad andare avanti.\n"
        "Sconosciuto|Io...|Vojo... andà... a casuccia...!\n"
        "Sconosciuto|Non ce la faccio...|Moudamepo... non c'è più speranza..."
    )
}

file_p = 'd:/Mod/Elin/Lang/IT/Dialog/dialog.xlsx'
wb = openpyxl.load_workbook(file_p)
ws = wb.active
headers = [str(c.value) for c in ws[1]]
id_col = 1
text_col = headers.index('text') + 1

count = 0
for r in range(2, ws.max_row + 1):
    rid = str(ws.cell(row=r, column=id_col).value or '').strip()
    if rid in dialog_it:
        ws.cell(row=r, column=text_col, value=dialog_it[rid])
        count += 1

wb.save(file_p)
print(f'dialog.xlsx translated {count} active dialog entries!')
