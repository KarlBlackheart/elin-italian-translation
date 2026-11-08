import openpyxl, json

def build_translations():
    # Translation dictionary keyed by (char_id, field)
    # field is one of 'calm', 'fov', 'aggro', 'dead', 'kill'
    T = {}

    # bell
    T[('bell', 'calm')] = '*drin*'
    T[('bell', 'aggro')] = '*drin*'
    T[('bell', 'dead')] = '*drin...*'

    # fairy
    T[('fairy', 'calm')] = '*fruscio d’ali*\n*svolazzo*\n*battito d’ali*\n*risatina*'

    # black_angel
    T[('black_angel', 'calm')] = '*fruscio d’ali*\n*battito d’ali*\n*sbattito d’ali*'
    T[('black_angel', 'dead')] = '"Aaah!"'
    T[('black_angel', 'kill')] = '"L’inferno ti attende."\n"Guardati, miserabile."'

    # bitch
    T[('bitch', 'calm')] = '"Oh cielo."\n"Ehi, bel #gender..."\n*sorrisetto*\n"Vuoi divertirti un po’ con me?"\n"Che noia..."'

    # cat
    T[('cat', 'calm')] = '"Miao."\n*fa le fusa*'
    T[('cat', 'aggro')] = '"Miao!"\n"Miao miao!"\n"Miao!"\n"Miao!"'
    T[('cat', 'dead')] = '"M...miao...."'
    T[('cat', 'kill')] = '*soffio*\n"Miaoo!"\n"Miauu!"\n"Miao!"\n"Miao miao."'

    # cat_stray
    T[('cat_stray', 'calm')] = '"Sai dov’è casa mia?"\n"Voglio andare a casa..."\n"Andiamo a casa..."'
    T[('cat_stray', 'aggro')] = '"Mi fanno la bua..."\n"Sto per morire!"'
    T[('cat_stray', 'dead')] = '"Voglio... andare... a... casa..."'
    T[('cat_stray', 'kill')] = '"Che spavento!"'

    # mogu
    T[('mogu', 'calm')] = '"Ku..."\n"...po."'
    T[('mogu', 'dead')] = '"Kupo!"'

    # cat_black
    T[('cat_black', 'calm')] = '"Miao."\n"Miao miao."\n"Miao."\n*fa le fusa*'
    T[('cat_black', 'aggro')] = '"Miao!"\n"Miao miao!"\n"Miao!"\n"Miao!"'
    T[('cat_black', 'dead')] = '"M...miao...."'
    T[('cat_black', 'kill')] = '*soffio*\n"Miaoo!"\n"Miauu!"\n"Miao!"\n"Miao miao."'

    # twintail
    T[('twintail', 'calm')] = 'Tutt’intorno a te percepisci la sacralità di un luogo venerabile.\n"Posa le tue armi e inginocchiati dinanzi a me."'

    # hardgay
    T[('hardgay', 'calm')] = '"Foooooo!"\n"Fooooo"\n"Foooooo!"'
    T[('hardgay', 'aggro')] = '"Foooooo!"\n"Fooooo"\n"Foooooo!"'
    T[('hardgay', 'dead')] = '"Foooooo!"\n"Fooooo"\n"Foooooo!"'
    T[('hardgay', 'kill')] = '"Foooooo!"\n"Fooooo"\n"Foooooo!"'

    # bunny
    T[('bunny', 'aggro')] = '"Cosa stai facendo?!"\n"Barbaro!"\n"Persino contro di me?!"'
    T[('bunny', 'dead')] = '"Ero una coniglietta così brava..."\n"Va’ all’inferno!"\n"Mi arrendo..."\n"Nooooo!"'
    T[('bunny', 'kill')] = '"Potere dei coniglietti!"'

    # conery
    T[('conery', 'calm')] = '"Vorrei che il mio giovane padrone fosse più giudizioso."\n"Sai, la disciplina è tutto."'
    T[('conery', 'aggro')] = '"Ti sottoporrò alla corte marziale, feccia."'
    T[('conery', 'dead')] = '"Maledetto sfacciato insolente!"'
    T[('conery', 'kill')] = '"Moccioso."'

    # garokk
    T[('garokk', 'calm')] = 'Senti il ritmo cadenzato del martello sull’acciaio.\nSenti il respiro pesante di un fabbro esperto.'

    # gilbert
    T[('gilbert', 'calm')] = '"Aiuta gli indifesi! Schiaccia la malvagità!"\n"Atten-TI! Saluto militare!"'
    T[('gilbert', 'aggro')] = '"Hwaaaa!"\n"Hiyah!"'
    T[('gilbert', 'dead')] = '"Cosa?!"'
    T[('gilbert', 'kill')] = '"Mwahahahahaha!"'

    # giant
    T[('giant', 'calm')] = '*bum*\n*tonfo*'
    T[('giant', 'aggro')] = '*bum*\n*tonfo*'

    # spider
    T[('spider', 'calm')] = '*scalpiccio svelto*\n*fruscio...*'
    T[('spider', 'fov')] = '*scalpiccio svelto*\n*fruscio...*'

    # horse
    T[('horse', 'calm')] = 'Senti il rumore di zoccoli.\n*clop-clop*\n*clop*'
    T[('horse', 'dead')] = '*nitrito debole*'
    T[('horse', 'kill')] = '"Hiiiiin!"'

    # janitor
    T[('janitor', 'aggro')] = '"Lumaca schifosa!"\n"Ce ne vuole di fegato per sfidarmi!"'
    T[('janitor', 'dead')] = '"Oh no, il mio cadavere inzozzerà tutta la città!"'
    T[('janitor', 'kill')] = '"Ahahahahaha!"\n"Feccia di strada!"'

    # littleOne / littleOne2 / big_sister
    for lid in ['littleOne', 'littleOne2', 'big_sister']:
        T[(lid, 'calm')] = '"#bigdaddy, ti prego alzati… Ti prego!"\nSenti il rumore di singhiozzi disperati...'
        T[(lid, 'aggro')] = '"N... no... non avvicinarti... aiuto... vi prego..."'
        T[(lid, 'dead')] = '"N... no... non voglio morire... noooo!"'
        T[(lid, 'kill')] = '"La mia bacca sarà colma del sangue di un angelo..."'

    # strange_girl
    T[('strange_girl', 'calm')] = '"Quelle bambine mi mettono i brividi."\n"Voglio tornare a casa."\n"Papà è tardi..."'
    T[('strange_girl', 'aggro')] = '"Pervertito!"'
    T[('strange_girl', 'dead')] = '"Pa... Papà..."'
    T[('strange_girl', 'kill')] = '"Che adulto patetico!"'

    # mapMerchant
    T[('mapMerchant', 'calm')] = '"Mmh.. Vediamo un po\'."\n"Dove ho messo quella mappa...?"\n"Ecco..."'
    T[('mapMerchant', 'aggro')] = '"Questo è un problema."\n"Anche questo fa parte del mio addestramento."\n"Non mi arrenderò facilmente."'
    T[('mapMerchant', 'dead')] = '"Ugh..."\n"Questo messaggio... portatelo a Palmia..."'
    T[('mapMerchant', 'kill')] = '"Bene, ce ne siamo occupati."\n"Niente rancore."\n"Questo dovrebbe bastare."'

    # adventurer_fox
    T[('adventurer_fox', 'dead')] = '"Non qui...!"\n"Hngh..."'
    T[('adventurer_fox', 'kill')] = '#self gonfia la sua coda.\n#self scodinzola vigorosamente con la coda.'

    # merc
    T[('merc', 'aggro')] = '"Che diavolo!"\n"Te ne pentirai amaramente."\n"Bene, indietro non si torna."'
    T[('merc', 'dead')] = '"Tu.... La pagherai cara un giorno..."\n"Nooo!"\n"Assassino!"'
    T[('merc', 'kill')] = '"Guardati."\n"Addio."'

    # merchant_fish
    T[('merchant_fish', 'calm')] = '"Pesce, pesce, pesce～♪"\n"Mangiamo un po’ di pesce～♪"\n"Fa bene alla salute!"'

    # merchant_festival
    T[('merchant_festival', 'calm')] = 'L’area è brulicante di festaioli allegri.\nRisate gioiose echeggiano nell’aria.'
    T[('merchant_festival', 'fov')] = '"Vieni a vedere cosa ho, #brother!"\n"È disponibile solo durante il festival!"'
    T[('merchant_festival', 'aggro')] = '"Guardie! Guardie!"\n"Un agguato!"\n"Al ladro!"'
    T[('merchant_festival', 'dead')] = '"Vi prego, risparmiate la mia vita!"\n"Ahhhh..."'
    T[('merchant_festival', 'kill')] = '"Muori, ladro!"\n"Te lo sei meritato."'

    # miral
    T[('miral', 'calm')] = '"Oh, cosa preparo per cena?"\n"Tanto lavoro e niente svago non va bene!"\n"Garokk, hai finito?"'

    # punk
    T[('punk', 'aggro')] = '"Mezza calzetta!"\n"Fatti sotto, bellezza!"\n"Urrà!"\n"Sputa l’anima, bastardo!"\n"È ora della punizione!"\n"Vieni qui!"'
    T[('punk', 'dead')] = '"Si salvi chi può!"\n"Sei completamente pazzo!"\n"Maledizione!"\n"Col cavolo!"\n"Basta, pietà!"\n"Non posso perdere!"'

    # rich
    T[('rich', 'aggro')] = '"Denaro, vuoi denaro, vero?\n"\n"Toglimi subito quelle luride mani di dosso!"\n\n"Guardie, aiuto!"\n\n"Miserabile pezzente assetato d’oro!"'
    T[('rich', 'dead')] = '"Non ti lascerò neanche una moneta..."\n"Oh, per tutti gli dei..."\n"Farabutto!"\n"Non voglio morire... gah..."\n"Meno male che ho fatto testamento..."'
    T[('rich', 'kill')] = '"Uhmf..."'

    # shojo
    T[('shojo', 'dead')] = '"No.... no...!"\n"Scusami, ho fallito..."'
    T[('shojo', 'kill')] = 'La ragazzina spolvera via la polvere dai suoi vestiti.\nLa ragazzina ti guarda con un’espressione fiera.'

    # sister
    T[('sister', 'calm')] = '"#onii"'
    T[('sister', 'dead')] = '"N... no!"'
    T[('sister', 'kill')] = 'Accarezzi la testa della tua sorellina.\nGuardi con affetto la tua sorellina.'

    # sister2
    T[('sister2', 'calm')] = '"fra…"\n"te…"\n"llo…"\n"ne…"\n"e…"'
    T[('sister2', 'aggro')] = '"fra…"\n"te…"\n"llo…"\n"ne…"\n"e…"'
    T[('sister2', 'dead')] = '"fra…"\n"te…"\n"llo…"\n"ne…"\n"e…"'
    T[('sister2', 'kill')] = '"fra…"\n"te…"\n"llo…"\n"ne…"\n"e…"'

    # olderyoungersister
    T[('olderyoungersister', 'calm')] = '"#onii"\n\n"#onii"\n\n"#onii"\n\n"#onii"\n\n"#onii"\n\n"Posso stare con te?"'
    T[('olderyoungersister', 'aggro')] = '"Spostati, #brother2!"\n"Non toccare #brother2!"\n"Attento, #brother2!"'
    T[('olderyoungersister', 'dead')] = '"Non ce la faccio più... #brother2!"'
    T[('olderyoungersister', 'kill')] = 'Accarezzi la testa della tua sorellina.\nGuardi con affetto la tua sorellina.'

    # stasha
    T[('stasha', 'calm')] = 'La quieta maestosità della stanza ti fa sentire piccolo.\nNoti lo sguardo nobile di Stasha.'
    T[('stasha', 'aggro')] = '"Fermate questo scempio!"\n"Guardie! Catturatelo!"'
    T[('stasha', 'dead')] = '"Mi dispiace tanto…"'
    T[('stasha', 'kill')] = '"Portate via questo cadavere sgradevole."'

    # strangeScientist
    T[('strangeScientist', 'calm')] = '"La retta via non è mai la più facile, vero?"\n"Non lascerò che la conoscenza vada perduta."'
    T[('strangeScientist', 'aggro')] = '"Come puoi fare una cosa simile?!"'
    T[('strangeScientist', 'dead')] = '"Non hai un cuore?!"'
    T[('strangeScientist', 'kill')] = '"Non hai un cuore?!"'

    # moyer
    T[('moyer', 'calm')] = '"Avanti, gente, venite a vedere!"\n"Accorrete tutti!"\n"Grandi affari solo per oggi!"'

    # parttimer_jure
    T[('parttimer_jure', 'calm')] = '"Cuscino da abbraccio di Santa Jure GRATIS!"\n"Avanti, fatevi sotto!"\n"Anche tu puoi essere benedetto da Santa Jure!"'

    # kuzu
    T[('kuzu', 'aggro')] = '"Eh eh eh..."\n"Ti farò fuori in un lampo."\n"Hya!"\n"Che essere patetico!"'
    T[('kuzu', 'dead')] = '"Aiutatemi..."\n"Eek... questo tizio è troppo forte..."\n"Risparmiatemi la vita!"'
    T[('kuzu', 'kill')] = '"A quanto pare la fortuna non era dalla tua parte."\n"Debole e patetico."'

    # tourist_festival
    T[('tourist_festival', 'calm')] = '"Andiamo a vedere la bancarella del cibo!"\n"No! Voglio giocare ancora un po’!"'

    # tourist_hotspring
    T[('tourist_hotspring', 'calm')] = '"Che bel bagno caldo!"\n"A quale sorgente termale dovrei andare dopo?"\n"Ah, che meraviglia rilassarsi così."'

    # mermaid_hotspring
    T[('mermaid_hotspring', 'calm')] = '"Ah, che delizia～"\n"Lalala～"\n"Lanlanlan"\n"Ufufu"\n"Cielo, che piacere l’acqua tiepida～"'
    T[('mermaid_hotspring', 'aggro')] = '"Questo non è permesso!"\n"Smettila subito!"\n"Ti schizzerò via!"'
    T[('mermaid_hotspring', 'dead')] = '"Aahn♪"'
    T[('mermaid_hotspring', 'kill')] = '"Te la sei cercata."\n"Ti sta bene, pervertito!"'

    # xabi
    T[('xabi', 'aggro')] = '"Sei impazzito?!"\n"Guardie! Catturateli!"\n"Hai perso il senno!"'
    T[('xabi', 'dead')] = '"Inutili soldati..."'
    T[('xabi', 'kill')] = '"Stupido."'

    # sad_creature
    for sfld in ['calm', 'fov', 'aggro', 'dead', 'kill']:
        T[('sad_creature', sfld)] = '"ti prego..."\n"uccidimi..."\n"di nuovo..."\n"sta crescendo..."\n"così tanto dolore..."'

    # scholar
    T[('scholar', 'fov')] = '"C’è un libro che penso ti piacerà un sacco."\n"Hai bisogno di nuove nozioni?"'

    # snail_torturer
    T[('snail_torturer', 'calm')] = '"Oh cielo, oh cielo."\n"Tutta viscida, vero?"\n"Che povera piccola creatura salata..."'

    # healer
    T[('healer', 'fov')] = '"Hai bisogno della mano di un guaritore?"\n"Stai bene?"\n"Oh, quelle ferite sembrano gravi..."'

    # informer
    T[('informer', 'calm')] = '*bisbiglia*\n"Ho una bella storiella per te."\n"Oh!"\n"Conosco ogni segreto di questa terra."'
    T[('informer', 'fov')] = '"Ho informazioni interessanti."\n"Vuoi comprare qualche notizia?"\n"Tutto ha un prezzo."'

    # dealer
    T[('dealer', 'fov')] = '"Anche tu hai l’animo corrotto, vero?"\n"Heh heh heh..."\n"Questa merce scotta parecchio."'

    # fanatic
    T[('fanatic', 'calm')] = '"O Signore."\n"Un povero agnello smarrito."\n"Tutto è per Te."\nSenti un fervore religioso nell’aria.'
    T[('fanatic', 'aggro')] = '"Miscredente!"\n"Bestemmia!"\n"Come osi!"\n"Morte agli eretici!"'
    T[('fanatic', 'dead')] = '"O Dio…!"\n"Vengo a Te, mio Signore!"\n"Possa la maledizione divina abbattersi su di te!"'
    T[('fanatic', 'kill')] = '"Pentiti!"\n"Hai avuto ciò che meritavi."\n"Una morte degna di un eretico."'

    # ashland
    T[('ashland', 'calm')] = 'Senti qualcuno che si prende cura delle proprie armi.\n"I pasticci in questa locanda sono davvero squisiti."'
    T[('ashland', 'aggro')] = '"Santo cielo."\n"Hai fretta di morire, vedo."\n"Che seccatura."'
    T[('ashland', 'dead')] = '"Fia... perdonami."'
    T[('ashland', 'kill')] = '"È già finita?"\n"Che delusione."'

    # fiama
    T[('fiama', 'calm')] = 'Rimani incantato dal volto di una fanciulla bella come una bambola preziosa.\n"C’è qualcosa che non va?"'
    T[('fiama', 'aggro')] = '"Hai bisogno di una lezione di disciplina."\n"Che stoltezza."\n"Smettila subito!"'
    T[('fiama', 'dead')] = '"Ash...!"'
    T[('fiama', 'kill')] = 'Fiama spolvera via con garbo la polvere dai suoi abiti.'

    # mayor
    T[('mayor', 'fov')] = '"Cosa vuoi?"\n"Fai in fretta."\n"Ebbene, avventuriero?"'

    # mage
    T[('mage', 'fov')] = '"Posso valutare qualsiasi cosa."\n"Hai bisogno di un perito magico?"\n"Fammi dare un’occhiata ai tuoi tomi."'

    # seeker
    T[('seeker', 'calm')] = '"Ebbene... Quando il corvo vola, la sua coda lo segue..."\n"Ora, qual è la tua meta?"'
    T[('seeker', 'aggro')] = '"È questa la tua filosofia?"\n\n"Mostrami la tua storia."\n\n"Questo era forse inevitabile."'
    T[('seeker', 'dead')] = '"Forse esplorerò l’aldilà, la prossima volta..."'
    T[('seeker', 'kill')] = '"Dunque è questa la tua storia... Una triste conclusione."'

    # ineien
    T[('ineien', 'calm')] = 'Qualcuno borbotta in un’antica lingua misteriosa.\nNote armoniose riempiono la stanza.'

    # jonan
    T[('jonan', 'calm')] = 'Qualcuno mormora debolmente tra sé.\n"Non sarò mai perdonato... mai..."'

    # lowell
    T[('lowell', 'calm')] = 'Senti una risata calorosa e gioviale.\nPercepisci occhi incuriositi su di te.\n"Oh, sei un tipo interessante!"'

    # zane
    T[('zane', 'calm')] = 'Il luogo è carico di palpabile tensione.\nQualcuno rimprovera ad alta voce una recluta.'

    # gomachan
    T[('gomachan', 'calm')] = '"Kyu."\n"Kyuu kyuu!"\n"Kyut?"\n"Kyu."\n"Kyuuu."'
    T[('gomachan', 'aggro')] = '"Kyut!"'
    T[('gomachan', 'dead')] = '"Kyu..."'
    T[('gomachan', 'kill')] = '"Kyuuu!"'

    # dog
    T[('dog', 'kill')] = '"Bau!"'

    # poppy
    T[('poppy', 'calm')] = 'Senti i guaiti squillanti di un cagnolino.\nUn uggiolio lamentoso echeggia nelle vicinanze.'
    T[('poppy', 'kill')] = '"Bau!"'

    # putty
    T[('putty', 'dead')] = '*splat*'

    # mammoth
    T[('mammoth', 'calm')] = '*bum*\n*tonfo*'
    T[('mammoth', 'aggro')] = '"Barriiiito!"'
    T[('mammoth', 'dead')] = '"Barrito debole..."'
    T[('mammoth', 'kill')] = '"Barriiiito!"'

    # snail
    T[('snail', 'calm')] = '*striscia...*'

    # pig
    T[('pig', 'calm')] = '*grugnito*\n*oink oink*'

    # rat
    T[('rat', 'calm')] = '"Squitt"\n"Squitt-squitt"\n"Squitt"'
    T[('rat', 'dead')] = '"Squitt!"'

    # performer
    T[('performer', 'calm')] = 'Senti risuonare una musica allegra.'
    T[('performer', 'dead')] = '"Torno a fare pratica..."'

    # maid
    T[('maid', 'calm')] = '"Padrone, posso aiutarvi in qualcosa?♪"\nSenti lo sguardo affettuoso della cameriera posarsi su di te...\n"Cielo, quante cose da fare!"\n"Tutto pronto!"\n"#title♪"'

    # theolucia
    T[('theolucia', 'calm')] = '"Mi chiedo quale sia la traduzione runica di questo testo..."\nSenti un mormorio sommesso di formule antiche.'
    T[('theolucia', 'aggro')] = '"Smettila, ti prego!"\n"Perché fai questo?!"'
    T[('theolucia', 'dead')] = '"Come hai potuto...."'
    T[('theolucia', 'kill')] = '"Sei inutile!"'

    # farris
    T[('farris', 'calm')] = '"O Elin, la Vedova Bianca, &il suo volto sbiadisce alla luce dell’alba..."\n"La canzone non deve finire mai."'

    # gwen
    T[('gwen', 'calm')] = '"Ah... Che bel fiorellino!"\n"Posso venire con te?"\n"Voglio giocare insieme a te!"'
    T[('gwen', 'dead')] = '"Perché mi fai questo...?"'
    T[('gwen', 'kill')] = '"Non mi piacciono le cose spaventose..."'

    # lady
    T[('lady', 'dead')] = '"Eek!"\n"Non è possibile!"'
    T[('lady', 'kill')] = 'La nobildonna spolvera via la polvere dai suoi abiti preziosi.\nLa nobildonna ti lancia uno sguardo di disprezzo.'

    # guild doormen
    T[('guild_doorman_mage', 'calm')] = '"Fermo... Lascia che verifichi se sei nei miei registri."'
    T[('guild_doorman_mage', 'fov')] = '"Oltre questa soglia comincia la giurisdizione della Gilda dei Maghi."'
    T[('guild_doorman_fighter', 'calm')] = '"Fermo… Lascia che controlli se il tuo nome è sulla lista."'
    T[('guild_doorman_fighter', 'fov')] = '"Oltre questa soglia comincia la giurisdizione della Gilda dei Guerrieri."'
    T[('guild_doorman_thief', 'calm')] = '"Fermati. Fammi controllare se sei sulla lista..."'
    T[('guild_doorman_thief', 'fov')] = '"Oltre questa soglia comincia la giurisdizione della Gilda dei Ladri..."'

    # isygarad
    T[('isygarad', 'aggro')] = '"Mostrami la tua danza."'
    T[('isygarad', 'dead')] = '"Non può essere vero…!"'
    T[('isygarad', 'kill')] = '"Che noia."'

    # mech_golems
    T[('mech_golem_a', 'aggro')] = '"Si comincia!"'
    T[('mech_golem_a', 'dead')] = '"Lascio il resto a te, Widge!"'
    T[('mech_golem_b', 'aggro')] = '"Si comincia!"'
    T[('mech_golem_b', 'dead')] = '"Lascio il resto a te, Higgs!"'

    # eluminaire
    T[('eluminaire', 'calm')] = '*pisolino*\n*sonnellino*\n"...oh!"'

    # ephrond
    T[('ephrond', 'calm')] = '"Umpf, sciocchi."\n"Dov’è finita quella donnetta?"\n"Le avevo detto di restare lì!"'

    # barrich
    T[('barrich', 'calm')] = '"Non fare il guastafeste!"\n"Oh, mi è venuta in mente una grande battuta!"'
    T[('barrich', 'fov')] = '"Ti andrebbe una canzone o due?"'

    # big_daddy
    T[('big_daddy', 'calm')] = 'Senti la terra tremare sotto i passi pesanti di un essere possente e adirato.'
    T[('big_daddy', 'aggro')] = 'Sorellina: "Uccidi! Uccidi!"\nSorellina: "Fallo a pezzi!"'
    T[('big_daddy', 'dead')] = '"ROAAARR!"'
    T[('big_daddy', 'kill')] = 'Sorellina: "Riempi la pancia col sangue dell’angelo!"'

    # melvin
    T[('melvin', 'calm')] = '"Sei ben lontano dalla perfezione!"\n"Mantieni la calma."\n"Un vero arco non mente mai."'

    # griffin
    T[('griffin', 'calm')] = '"Huu."\n"Huu-huuu."\n"Huuu!"'

    # caldorn
    T[('caldorn', 'calm')] = '"I giovani d’oggi sono inconcepibili."\n"Tirati su le maniche e lavora duro!"'

    # melilith_boss
    T[('melilith_boss', 'dead')] = '"Non lasciarmi di nuovo da sola..."'

    # demitas
    T[('demitas', 'calm')] = '"Gli antichi porteranno la calamità."\n"Heh heh heh..."\n"I miei esperimenti sono quasi completi."'
    T[('demitas', 'aggro')] = '"Heh... heh..."\n"Cerchi forse la rovina?"\n"Oserai levare la mano contro di me?"'
    T[('demitas', 'dead')] = '"Perdonami, Telessia..."\n"Ritorniamo nell’oscurità..."'
    T[('demitas', 'kill')] = '"Heh heh heh..."\n"Stolto."\n"Ritorna nelle tenebre."'

    # loytel
    T[('loytel', 'calm')] = '"La colonizzazione è una vera e propria arte."\n"Bisogna pianificare tutto con cura meticolosa."\n"I fondi scarseggiano sempre..."'
    T[('loytel', 'aggro')] = '"Ma cosa al mondo?!"\n"Cosa diavolo stai facendo?!"\n"Qual è il tuo problema?!"'
    T[('loytel', 'dead')] = '"Mi scoppia la testa..."'
    T[('loytel', 'kill')] = '"Hmph."\n"Ti sta proprio bene!"'

    # quru
    T[('quru', 'calm')] = 'Hai la sensazione che qualcuno ti stia fissando con insistenza.\nQualcuno ti scruta con occhi gelidi.'
    T[('quru', 'aggro')] = '"Stolto."\n"Desideri morire."\n"Fermati."\n"..."'
    T[('quru', 'dead')] = '"Eek!"\n"Non è possibile!"'
    T[('quru', 'kill')] = '"Muori!"'

    # kettle
    T[('kettle', 'calm')] = 'Ti senti come se il vento ti stesse stuzzicando scherzosamente.\nPercepisci una presenza amichevole accanto a te.'
    T[('kettle', 'aggro')] = '"Non mi piace affatto, ma..."\n"Se non c’è altra scelta..."\n"Non costringermi!"'
    T[('kettle', 'dead')] = '"Verrò da te adesso..."'
    T[('kettle', 'kill')] = '"È un vero peccato."\n"Riposa in pace."\n"Non dovrai più soffrire."'

    # keeper_garden
    T[('keeper_garden', 'calm')] = '"Che adorabile creatura."\n"Muwohoho."'
    T[('keeper_garden', 'aggro')] = '"Muwohohoho! Osi sfidarmi!?"'
    T[('keeper_garden', 'dead')] = '\n"Muwohohoho! Splendido!'
    T[('keeper_garden', 'kill')] = '"Muwohohoho, quanto sei debole!"'

    # namamani / namamani2
    T[('namamani', 'aggro')] = '"Bel tentativo."\n"Un altro malfunzionamento?"\n"Bene."'
    T[('namamani', 'dead')] = '"Magnifico."'
    T[('namamani', 'kill')] = '"Quanto è banale."\n"Ora hai capito?"\n"Heh."'
    T[('namamani2', 'aggro')] = '"Dunque sei mio nemico?"\n"Perché?"\n"E sia."'
    T[('namamani2', 'dead')] = '"Sto forse... per morire?"'
    T[('namamani2', 'kill')] = '"Quindi... eri mio nemico?"\n"Chi sono io?"'

    # erishe
    T[('erishe', 'calm')] = '"Mi chiedo dove sia andato..."\nSenti un calore rassicurante come essere avvolti da una coperta morbida.'
    T[('erishe', 'aggro')] = '"T-ti prego... fermati."'
    T[('erishe', 'dead')] = '"F-fratellone..."'
    T[('erishe', 'kill')] = '"Scusami..."'

    # larnneire
    T[('larnneire', 'calm')] = '"Conosci la fiaba in cui una strega malvagia &trasforma un principe in un rospo?..."'
    T[('larnneire', 'aggro')] = '"Dobbiamo davvero batterci?"\n"Scusa, ma non ho tempo da perdere."'
    T[('larnneire', 'dead')] = '"A-ah... ho fallito il mio compito... questo mondo.... questo mondo cadrà..."'
    T[('larnneire', 'kill')] = '"Mi dispiace..."'

    # lomias
    T[('lomias', 'calm')] = '"Aspetta di vedere le loro facce quando sentiranno le notizie che portiamo."\n"E poi dicono che siamo noi quelli strani..."'
    T[('lomias', 'aggro')] = '"Ripaghi la gentilezza con l’ingratitudine?"'
    T[('lomias', 'dead')] = '"Questo è assolutamente ridicolo..."'
    T[('lomias', 'kill')] = '"C’è sempre qualcuno che non riuscirò mai a capire."'

    # raphael
    T[('raphael', 'calm')] = '"Signore! La fila inizia qui!"\n"Nessuna donna può resistere al mio fascino!"'
    T[('raphael', 'aggro')] = '"Vi mostrerò cosa significa essere un vero uomo!"'
    T[('raphael', 'dead')] = '"Mammaaa!"'
    T[('raphael', 'kill')] = '"Ptu!"'

    # pursuer
    T[('pursuer', 'calm')] = 'Senti il respiro affannoso dei cani da caccia.\nPercepisci lo sguardo implacabile dell’inseguitore.'
    T[('pursuer', 'aggro')] = '"Ti ho trovato."\n"Pensavi davvero di poter fuggire?"\n"La morte ti attende."'
    T[('pursuer', 'dead')] = '"È questa la volontà degli dei?"\n"Che la maledizione ricada su di te."'
    T[('pursuer', 'kill')] = '"Affronta il giudizio."\n"Questa è la volontà degli dei."'

    # fairy_poina / fairy_raina
    T[('fairy_poina', 'aggro')] = '"Idiota..."'
    T[('fairy_poina', 'dead')] = '"Ngh..."'
    T[('fairy_poina', 'kill')] = '"Avanti il prossimo..."\n"Uff..."'
    T[('fairy_raina', 'aggro')] = '"Una melanzana arrosto in arrivo!"'
    T[('fairy_raina', 'dead')] = '"Eh? Io...!?"'
    T[('fairy_raina', 'kill')] = '"Scossa elettrica?"'

    # defender
    T[('defender', 'calm')] = 'Ti senti protetto da una solida presenza.'
    T[('defender', 'dead')] = '"Perdonami, mio signore..."'
    T[('defender', 'kill')] = 'Il difensore spolvera via la polvere dai suoi vestiti.\nIl difensore rinfodera la sua arma con solennità.'

    # adv_kiria
    T[('adv_kiria', 'calm')] = '"Un giorno troverò il mio creatore e gli darò un bel pugno in faccia."\n"Hai visto parti di ricambio in giro?"'
    T[('adv_kiria', 'dead')] = '"Devo... essermi... arrugginita..."'

    # adv_schwert
    T[('adv_schwert', 'calm')] = '"...Ancora operativo."\n"Scansione dell’area—nessuna anomalia rilevata."'
    T[('adv_schwert', 'aggro')] = '"Protocollo di combattimento—in esecuzione."\n"Dispiegamento armi."\n"Bersaglio ostile rilevato."'
    T[('adv_schwert', 'dead')] = '"Settore di memoria—errore. Ripristino impossibile."\n"Controllo mana—interrotto."'
    T[('adv_schwert', 'kill')] = '"Autodiagnosi—avviata."\n"Nucleo di mana—stabile."\n"Unità ostile neutralizzata."'

    # adv_gaki
    T[('adv_gaki', 'calm')] = '"Mezza calzetta."\n"Mezza cartuccia?"\n"Mezza-mezza-mezza cartuccia♪"\n"Mezza cartuuuccia!"'
    T[('adv_gaki', 'aggro')] = '"Mezza cartuccia!!"\n"Mezza-mezza-mezza-mezza cartuccia♪"\n"Mezza cartuccia! Solo una mezza cartuccia!"'
    T[('adv_gaki', 'dead')] = '"Mezza cartuccia…"\n"Mezza cartuuuccia!!"'
    T[('adv_gaki', 'kill')] = '"Mezza cartuuuccia♪"\n"Mezza-mezza cartuccia♥"\n"Mezza-mezza-mezza-mezza-mezza cartuccia♪"'

    # adv_verna
    T[('adv_verna', 'calm')] = '"L’ombra è il mio specchio."\n"Non temo l’oscurità. L’oscurità teme me."'
    T[('adv_verna', 'aggro')] = '"Ombre, danzate con me."\n"Metterò fine a tutto questo."\n"Che pena mi fai."'
    T[('adv_verna', 'dead')] = '"Questo mondo è troppo luminoso per me."'
    T[('adv_verna', 'kill')] = '"Addio."\n"È la fine."\n"Benvenuto nel mio mondo."\n"Possa l’oscurità inghiottirti."'

    # adv_mesherada
    T[('adv_mesherada', 'calm')] = '"I secoli passano, attraverso vite e sentieri &infiniti, eppure il mio cuore continua a cercarti..."'
    T[('adv_mesherada', 'aggro')] = '"Che insolenza!"\n"Ostacolare la mia ricerca è imperdonabile."'
    T[('adv_mesherada', 'dead')] = '"Continuerò a cercarti nella mia prossima vita..."'
    T[('adv_mesherada', 'kill')] = '"Mi dispiace..."\n"Queste catene che un tempo furono il mio desiderio &non si spezzeranno."'

    # adv_yukiimo
    T[('adv_yukiimo', 'calm')] = 'La coda soffice di #me oscilla placidamente.\nGli occhi di #me seguono con curiosità ogni tuo movimento.'
    T[('adv_yukiimo', 'aggro')] = 'Il pelo di #me si rizza per l’allerta.\nLa coda soffice di #me raddoppia di volume!'
    T[('adv_yukiimo', 'dead')] = '"No!"\n"Fai attenzione..."\n"Questo è tosto…"\n"Perché...?"'
    T[('adv_yukiimo', 'kill')] = '#me si stira beatamente.\n#me si ripulisce dal sangue degli schizzi.\n"Sei stato bravo!"'

    # exile_girl
    T[('exile_girl', 'calm')] = '"Esuli..."\n"Esuli...♥"'

    # lurie_boss
    T[('lurie_boss', 'aggro')] = '"GROOOOAAARRR!"'
    T[('lurie_boss', 'dead')] = '*guaìto debole...*'
    T[('lurie_boss', 'kill')] = '"GRROOAARR!"'

    return T

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/CharaText.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    T = build_translations()
    count = 0

    for r in range(2, ws.max_row+1):
        cid = ws.cell(row=r, column=headers['id']).value
        if not cid: continue
        for (m_id, fld), it_txt in T.items():
            if cid == m_id and fld in headers:
                ws.cell(row=r, column=headers[fld]).value = it_txt
                count += 1

    wb.save('Lang/IT/Game/CharaText.xlsx')
    print(f'Applied {count} translations to CharaText.xlsx')

if __name__ == '__main__':
    run()
