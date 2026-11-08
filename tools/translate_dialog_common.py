import openpyxl

def translate_dialogs():
    path = 'Lang/IT/Dialog/dialog.xlsx'
    wb = openpyxl.load_workbook(path)

    # 1. SHEET GENERAL
    ws_gen = wb['general']
    t_gen = {
        'tail4': "Che c'è che non va, #pc? Perché mi fissi così?",
        'lockpick_purse': "Sembra un oggetto smarrito da qualcuno... beh, che me ne importa?",
        'invite': "Vorresti che mi trasferissi a vivere nella tua colonia?",
        'invite2': "Purtroppo ho delle faccende importanti di cui occuparmi in questo momento.",
        'invite3': "Se tu avessi un briciolo di fascino in più, forse accetterei.#newline(Richiede carisma #1)",
        'inviteReq1': "Potresti portarmi #1?",
        'talk_hobby': "Il mio passatempo preferito è #1.",
        'talk_fav': "Cosa mi piace? Diciamo che ho un debole per #1, ma la mia vera passione è #2.",
        'slave_buy': "Vuoi comprare #2? Oh, vedo che hai buongusto! Ti costerà #1 oren.",
        'slave_buy2': "Da oggi #1 è tutto tuo. Abbine cura, mi raccomando.",
        'goto': "#1? Certo, ti mostro subito dove si trova.",
        'goto2': "Ti sembra il momento di scherzare?",
        'upgrade_heath1': "Ci servirà #1 per potenziare la Pietra del Focolare al livello #2.#3",
        'upgrade_heath2': "Fantastico! Questo aiuterà la nostra dimora a prosperare ancora di più!",
        'invest1': "Ti interessa investire del denaro? Finora hai investito un totale di #2 oren, e #zone è attualmente alla ricerca di #1 oren di finanziamenti.",
        'invest2': "Grazie di cuore! Il tuo investimento renderà #zone un luogo molto più florido.",
        'invest_shop1': "Oh, desideri investire nella mia bottega? Per espandere l'attività serviranno #1 oren. Spero che tu abbia con te il denaro.",
        'invest_shop2': "Mi hai rallegrato la giornata! Grazie, faremo ottimi affari!",
        'questCompleteDeliver': "Oh, mi hai portato #1! Grazie mille. Ecco a te la ricompensa pattuita.",
        'questCompleteDeliverExtra': "Oh, questo è senz'altro l'oggetto che ti avevo commissionato! Ti darò una ricompensa degna del valore di #1. Grazie!",
        'miral_medal': "Ohohoh! Hai con te delle piccole medaglie! Fammi dare un'occhiata, fammi vedere! Ti andrebbe di scambiarle con uno dei miei capolavori di cui vado tanto fiero?",
        'miral_medal2': "Umpf!",
        'shop_criminal': "Non concludo affari con i criminali della tua risma.",
        'shop_blackmarket_noaccess': "Ahaha, e cosa ci fa un avventuriero perbene come te in un posto losco come questo?",
        'guide': "Stai cercando qualcuno in particolare?",
        'shutup': "(#tg ammutolisce con aria mesta...)",
        'shutup2': "(#tg ti stringe forte a sé.)",
        'insult': "Sei un pervertito senza alcuna speranza.",
        'insult2': "A quanto pare sei finalmente tornato in te.",
        'ok': "(#tg annuisce dolcemente con il capo.)",
        'refuse': "(#tg declina cortesemente la tua proposta.)",
        'deliver_purse': "Che gentilezza riconsegnarmi un oggetto smarrito. Sei davvero un cittadino modello! Grazie di cuore.",
        'news1': "C'è un luogo chiamato #1 da queste parti. Se la cosa ti incuriosisce, potrebbe valere la pena esplorarlo.",
        'news2': "Purtroppo non ci sono novità degne di nota al momento.",
        'bout1': "Vuoi mettere alla prova la tua forza?\nSei davvero serio?\nStai forse cercando di attaccare briga con me?",
        'bout2': "Bene, vedo che hai fegato!\nCosì ti voglio!\nD'accordo, mostrami di che pasta sei fatto!",
        'what': "Cosa c'è?",
        'becomeMaid': "D'accordo, da oggi sarò la tua cameriera personale.",
        'sellFame1': "Ahaha, #brother, sei davvero così a corto di quattrini? D'accordo, comprerò la tua fama per #1 oren.",
        'sellFame2': "Grazie, saprò sfruttare la tua reputazione a dovere.",
        'blessing': "Desideri ricevere una benedizione? Molto bene, china il capo e prega!",
        'lockTooHard': "Questa serratura sembra decisamente troppo complessa per le mie capacità. Mi dispiace, ma dovrai vedertela da te.",
        'loytel_bill_give1': "Ti ringrazio sinceramente per aver deciso di aiutarmi con i debiti... D'accordo, iniziamo sbrigando questa fattura di piccolo importo. Depositala nella cassa delle tasse e vieni a riferirmi non appena avrai saldato tutto.",
        'loytel_bill_give2': "Capisco... Mi si stringe il cuore a dovertelo dare, ma ecco a te la prossima cartella. Torna a parlarmi quando avrai effettuato il versamento.",
        'loytel_bill_give_given': "Dovresti avere già con te la cartella del debito. È un documento importante, cerca di non perderlo per nessun motivo.",
        'loytel_bill_give_wait': "Ecco... non mi sento ancora pronto per la prossima fattura. Ti dispiacerebbe pazientare ancora un momento?",
        'loytel_bill_give_lost': "...Ti ricordi quando ti dissi: 'Cerca di non perderla'? Tieni, te ne do un'altra copia, ma stavolta prestaci la massima attenzione.",
        'marry': "Sì... con tutto il cuore.",
        'wedding_deed': "Mi riempie di gioia sentirtelo dire! Ma prima ci servirà un Permesso di Matrimonio ufficiale.",
        'wedding_zone': "Mi fai così felice! Ma parliamone con calma una volta tornati alla base.",
        'wedding_confirm': "Ne sei davvero sicuro? (Il tuo gruppo attuale verrà sciolto e ne verrà formato uno nuovo con voi due soli).",
        'wedding_accept': "Sono così felice, #pc! È il giorno più bello della mia vita!",
        'rob1': "Mi sbagliavo sul tuo conto!\nTi prego, fermati!\nTi pentirai amaramente di avermi sfidato.\nCosa crede di fare un volgare brigante contro di me?\nTi prego, fermati. Te ne pentirai.\nMercenari, scacciate via questo villano!\nUmpf. Non vedi quante guardie del corpo mi circondano?",
        'mama_yes': "La mamma è qui!\nSì, sono la tua mamma!\nLa mamma non ti lascerà mai solo.",
        'mama_no': "Pussa via!\nNon sono affatto tua madre!\nMa che cosa stai blaterando...?\nPoveretto... hai per caso battuto la testa?\nChe cosa raccapricciante...\nEh...?",
        'baby_yes': "Mammaaa!\n...Sei davvero... la mia mamma?\nMa... mamma...?",
        'baby_no': "Tu non sei la mia mamma!\nMa che cosa stai blaterando...?\nPoveretto... hai per caso battuto la testa?\nEh...?"
    }

    c_gen = 0
    headers_gen = {ws_gen.cell(row=1, column=c).value: c for c in range(1, ws_gen.max_column + 1)}
    for r in range(2, ws_gen.max_row + 1):
        rid = ws_gen.cell(row=r, column=1).value
        if rid in t_gen:
            ws_gen.cell(row=r, column=headers_gen['text']).value = t_gen[rid]
            c_gen += 1

    print(f"general sheet updated: {c_gen} rows.")

    # 2. SHEET UNIQUE
    ws_uni = wb['unique']
    headers_uni = {ws_uni.cell(row=1, column=c).value: c for c in range(1, ws_uni.max_column + 1)}
    t_uni = {
        'miral': "Oh, un visitatore! Non fare complimenti, vieni pure a coccolare i miei gatti.\nUn tempo io e il mio socio litigavamo spesso sul nome della bottega. Se solo avesse avuto un briciolo di senso estetico, non gli sarebbe mai venuto in mente un nome ridicolo come \"Garok Miral\".\nCosa prepareremo per il pranzo di oggi? Negli ultimi tempi mi diverto molto più a pensare al menu per i miei gatti che a forgiare metalli sull'incudine.",
        'nino': "La vita della carovana è libera e spensierata, ma non mi dispiacerebbe stabilirmi in una cittadina accogliente, prima o poi. Magari proprio dalle parti di Port Kapul.\nTrovi insolito un mercante uomo-bestia? In effetti a Tyris non siamo molti.\nAndiamo fieri delle innumerevoli merci raccolte viaggiando da Verizzia, il regno degli oceani a ovest, fino a Nieca, la terra dorata delle sabbie orientali. Fai con calma e guarda pure ciò che ti aggrada.\nNo... ti assicuro che questo non è un costume.",
        'nola': "Sono Nola, facente funzioni di Sindaco. Come posso esservi d'aiuto?",
        'stasha': "Oh, avete bisogno di qualcosa?\nPalmia è un regno che vanta una grandiosa storia in tutta Tyris. Per me è un sommo onore essere accolta a corte in questo sontuoso palazzo reale.\nIdolo...? ...È forse un termine di qualche lingua straniera?\nI fan... ah, cioè... i gentiluomini di corte sono sempre straordinariamente premurosi con me.",
        'theolucia': "Mi appassionano profondamente la storia antica e il folclore popolare.\nTi do un consiglio: evita di far arrabbiare mia sorella Farris, sa essere davvero terrificante.\nLa Biblioteca Reale di Palmia è un posto meraviglioso, custodisce una quantità infinita di tomi e volumi preziosi.",
        'xabi': "Sei un avventuriero? Mi piacerebbe tantissimo ascoltare i tuoi racconti di viaggio.\nMio padre è davvero troppo severo. Trova da ridire su qualsiasi cosa io faccia, non ne posso più! Sono sicuro che Connelly eserciti una pessima influenza su di lui.",
        'zane': "Chi sei? E cosa cerchi?\nQuesto non è un luogo accessibile a qualsiasi avventuriero di passaggio. Allontanati immediatamente.\n...",
        'ephrond': "Chi sei tu? Tieni le distanze.\nAh, che splendida e pacifica giornata nella magnifica Mysilia. Gli abitanti sembrano tutti tenere gli occhi ben chiusi, oppure li hanno smarriti chissà dove...",
        'eluminaire': "Ti prego, allontanati... Lord Efrond andrà su tutte le furie se mi vede parlare con te.\nLa Foresta delle Aberrazioni? ...Non ci ho mai messo piede. Gli elea che abitano a Mysilia sono tutti elea 'esterni alla foresta'...",
        'barrich': "Ti andrebbe di ascoltare una canzone?\nUn tempo servivo alla corte reale di Zanan ma, ecco, ho combinato un pasticcio memorabile...\nOrmai considero Mysilia la mia vera casa.\nI fedeli ammiratori di Melvin? Ahaha, che tipi pittoreschi!",
        'melvin': "Sono già passati otto anni da quando mia sorella è andata in sposa a Barrich. Il tempo vola davvero in fretta.\nLa mia stirpe custodisce da generazioni il ruolo di protettrice delle genti della foresta. Per gli elea, gli alberi e la natura sono beni infinitamente preziosi.",
        'caldorn': "Cosa sei venuto a fare?\nLa parola 'avventuriero' suonerà anche romantica, ma in fin dei conti siete solo vagabondi senza alcuna intenzione di svolgere un lavoro onesto.\nLa minaccia dell'Impero è evidente, ma anche le vere intenzioni di Zanan restano del tutto imperscrutabili.",
        'melilith': "Secondo te fanno più paura le sorelline o i cubi? Io trovo che le sorelline siano molto più carine!",
        'seeker': "Ah, un corvo pellegrino. Sei in cerca di qualcosa?\nGradiresti una tazza di tè, corvo?\nGli uomini mi chiamano 'Il Cercatore'... oppure 'Il Viaggiatore dei Mondi'. Sono un uomo che ha visto la nascita e la fine di innumerevoli dimensioni.",
        'quru': "Cosa vuoi?",
        'kettle': "Riesci a percepire le antiche parole che il vento sussurra nell'aria? Vago per questo mondo proprio per apprendere i segreti e le storie che il vento porta con sé.",
        'strange_girl': "Non sopporto quelle Little Sister. Dicono sempre cose bizzarre e fanno davvero paura!\nNon osare paragonarmi a quei mostriciattoli, intesi?\nQuando tornerà papà, gli chiederò di portarmi a fare un giro sui gatti.",
        'moyer': "Ehi tu! Sei qui per tentare la sorte alla ruota della fortuna?",
        'miko_mifu': "Noi siamo al contempo una benedizione e una maledizione. Mutando prospettiva, perfino la debolezza può tramutarsi in forza.\nNon v'è vita senza morte, né cielo senza inferno, né incontro che non rechi in sé l'addio.",
        'miko_nefu': "Yufu era una divinità empia e distruttiva che tentò di manipolare la guerra tra gli dei per dominare su tutta Ylva.\nNoi offriamo danze sacre nella radura dell'Albero Divino.\nNostra signora Horome protegge con affetto ogni singola creatura vivente.",
        'eureka': "Un viaggiatore? Che evento straordinario.\nIl mio dovere è vegliare su questo luogo sacro. È un sommo onore, anche se... alle volte la solitudine si fa un po' noiosa...",
        'merchant_inn_fox': "Questo ciondolo che porto al collo? Naturalmente è ricolmo di chicchi di riso. Nel nostro villaggio non coltiviamo il grano.",
        'merchant_inn_fox2': "Questa locanda era stata originariamente costruita per accogliere i devoti pellegrini, ma ultimamente si vedono sempre più turisti curiosi.\nBenvenuto! Desideri mangiare qualcosa di caldo o preferisci fare un bagno rilassante nelle sorgenti?",
        'adv_kiria': "Sai per quale scopo sono stata creata? No? Immaginavo.\nContinuo a sognare un posto che sento come casa, ma non riesco a ricordare come tornarci.\nI miei occhi? Già... sembrano quasi due gemme preziose, vero?",
        'adv_gaki': "Un tulipano azzurro spettrale? Ho girato in lungo e in largo per il mondo, ma non ne ho mai visto uno.\nSi dice che stia girando una strana e nuova malattia... chissà, magari mi spuntano le corna!\nSe la fai arrabbiare, Farris diventa spaventosa.",
        'adv_mesherada': "Mi chiedo... se le nostre anime siano destinate a intrecciarsi di nuovo, in attesa del compimento della promessa solenne.\nSe tu fossi davvero la persona che cerco... sono certa che il destino ce lo sussurrerebbe al cuore.",
        'olderyoungersister': "Ti domandi quando sia nata, #brother2? È accaduto tanto, tanto tempo fa, mio caro #brother2...\nHo vagato per il mondo intero cercando te e soltanto te, #brother2.",
        'fairy_nanasu': "Io sono Nanasu, la fata delle melanzane!\nQual è il mio cibo preferito? Le melanzane, ovvio!\nSpecwing è un posto meraviglioso, tutti si divertono un mondo qui.",
        'fairy_raina': "Io sono Raina! Se mi tocchi senza permesso ti farò prendere una bella scossa!\nOh, avventuriero! Hai bisogno di me?\nIl mio rapporto con Poina? Beh, diciamo che siamo compagne di marachelle!",
        'fairy_poina': "Io sono Poina. Se dici una sola parola di troppo ti avveleno seduta stante.\n...Cosa c'è? Vuoi qualcosa da me?\nRaina a volte prende le battaglie troppo alla leggera. Gliel'ho ripetuto mille volte che l'avventura non è un gioco da ragazzi.",
        'girl_blue': "Il Putty delle nevi è così incredibilmente carino... eheheh.\nVorrei tanto essere libera e spensierata come un gatto.\nSe esistesse una divinità dei gatti, incarnerebbe la libertà assoluta.",
        'rodwyn': "Per le mie preparazioni utilizzo esclusivamente ingredienti di primissima qualità.\nTi andrebbe di dare un'occhiata alla mia collezione di scope magiche?\nDunque vediamo... lingua di tritone... occhi d'ape... Oh, scusami! Non mi sono ancora presentata!"
    }

    c_uni = 0
    for r in range(2, ws_uni.max_row + 1):
        rid = ws_uni.cell(row=r, column=1).value
        if rid in t_uni:
            ws_uni.cell(row=r, column=headers_uni['text']).value = t_uni[rid]
            c_uni += 1

    print(f"unique sheet updated: {c_uni} rows.")

    wb.save(path)
    print("dialog.xlsx fully updated!")

if __name__ == '__main__':
    translate_dialogs()
