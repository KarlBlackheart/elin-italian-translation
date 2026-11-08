import openpyxl

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/List.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    list_map = {
        'skillDiff': 'Facile,Normale,Difficile,Impossibile',
        'temper': 'Infuriato,Scontento,Imbronciato,Calmo,Contento,Deliziato,Al settimo cielo',
        'zone_R_Plain': 'Campi',
        'zone_R_Forest': 'Foresta',
        'zone_R_Forest_cherry': 'Foresta di ciliegi',
        'zone_R_Shore': 'Riva',
        'zone_R_Mountain': 'Montagna',
        'zone_R_Snow': 'Distesa innevata',
        'zone_R_Water': 'Oceano',
        'zone_R_Undersea': 'Fondali marini',
        'rooms': 'Stanza',
        'onii2': 'Fratellone',
        'onee2': 'Sorellona',
        'onii': 'Fratellone♪,Fratellone!,Fratellino mio♪,Fratellone,Fratellone?,Fratellone!?',
        'onee': 'Sorellona♪,Sorellona!,Sorellina mia♪,Sorellona,Sorellona?,Sorellona!?',
        'qFriendHome': 'conoscente,vicino,amico,gatto,cane,leone marino ghiottone,putit,collega,pollo,animale domestico',
        'qFriend': 'amico,genitore,amante,sorella,fratello,moglie,capo,fidanzata,tesoro,mamma,papà,gatto,figlio',
        'qClient': 'amico,magnate,nobile,mercante,studioso,avventuriero,trafficante del mercato nero,ricettatore',
        'resist': 'Nessuna,Normale,Forte,Eccellente,Immunità,Immunità+',
        'resistNeg': 'Nessuna,Debolezza,Vulnerabilità estrema',
        'wGender': 'Scegli un sesso,,,Elenco dei sessi',
        'wClass': 'Scegli una classe,,,Elenco delle classi',
        'wRace': 'Scegli una razza,,,Elenco delle razze',
        'wAlias': 'Scegli un epiteto,,,Elenco degli epiteti',
        'wAge': 'Scegli una fascia di età,,,Elenco delle età',
        'wStartMode': 'Scegli un prologo,,,Elenco dei prologhi',
        'wMoongate': 'Scegli una destinazione per il portale,,,Nome Luogo',
        'wReturn': 'Scegli una destinazione di ritorno,,,Nome Luogo,Livello di ritorno',
        'wRuneMold': 'Scegli un incantamento da estrarre,,,Nome Incantamento,Livello',
        'wTrain': 'Scegli un’abilità da addestrare,,,Nome Abilità,Costo in Monete di Platino',
        'wSkyTravel': 'Scegli una coordinata per spostarti,,,Coordinate,Costo Biglietto',
        'wCraft': 'Scegli una ricetta,,,Nome Ricetta,Posseduto,Abilità Artigianato',
        'ListPeopleBuySlave': 'Scegli uno schiavo,,,Nome Creatura,Prezzo,Occupazione',
        'ListPeopleRevive': 'Scegli un alleato da resuscitare,,,Nome Alleato,Prezzo,Classe',
        'ListPeopleCallReserve': 'Scegli un alleato da richiamare,,,Nome Alleato,Interazione,Classe',
        'ListPeople': ',,,Nome Alleato,Interazione,Info',
        'ListPeopleSelect': ',,,Nome Alleato,Nota',
        'ListPeopleBed': ',,,Nome Alleato,Nota',
        'ListPeopleParty': ',,,Nome Alleato,Preferito',
        'wBGMLot': 'Scegli un brano,,,Nome Brano,Interazione',
        'wPlaylist': 'Playlist Attuale,,,Nome Brano,Interazione',
        'wPlaylist2': 'Brani in memoria,,,Nome Brano,Interazione',
        'wTravel': 'Scegli una meta per il viaggio rapido,,,Nome Destinazione,Giorni,Razioni Richieste',
        'dayLuck': 'Granchio reale,Tonno rosso,Aragosta spinosa,Vongola orientale comune,Riccio di mare,Cetriolo di mare',
        'dayLuck2': 'Miao miao miao!,Miao miao!,Miao...,Che noia.,Fai attenzione!,(Pssss...)',
        'daggerTalk': 'Liberatele...!,Le nostre spade...!,La mia spada...!,Amico mio...,La mia anima...,Il mio orgoglio...,Ti prego... la spada...,Abbiamo atteso così a lungo...,La mia spada che fu vincolata da lui...,La mia spada che fu rubata da lui...,La mia spada...,La spada...,Tu...hai liberato la mia spada...?,Chi va là...?',
        'quality_furniture': "stupido,sciatto,figo,prediletto da madame,stregato,eccentrico,stimato,magnifico,regale,capolavoro,celestiale,divino",
        'ancientbook': "Manoscritto Voynich,Canti di Dhol,Scritture di Ponape,Rivelazioni di Glaaki,Frammenti di G'harne,Liber Damnatus,Libro di Dzyan,Libro di Eibon,Grande Grimorio,Frammenti di Celaeno,Necronomicon,Testo di R'lyeh,Frammenti di Eltdown,Il Ramo d'Oro,Apocalisse",
        'music_result': "È una perdita di tempo.,Quasi tutti ti ignorano.,Devi fare molta più pratica.,Termini l'esibizione.,Non un granché.,Alla gente sembra piacere la tua esibizione.,La tua esibizione è un successo.,Meraviglioso!,Grande esibizione.,Un'esibizione Leggendaria!",
        'buff_STR': 'Poderoso,Indebolito',
        'buff_END': 'Fortificato,Fragile',
        'buff_DEX': 'Agile,Maldestro',
        'buff_PER': 'Sensi Acuti,Sensi Offuscati',
        'buff_LER': 'Illuminato,Ostacolato',
        'buff_WIL': 'Inflessibile,Soggiogato',
        'buff_MAG': 'Magia Amplificata,Magia Prosciugata',
        'buff_CHA': 'Radioso,Tetro',
        'buff_LUC': 'Baciato dalla Fortuna,Iellato',
        'buff_SPD': 'Celerità,Lentezza',
        'quality': 'grezzo,normale,buono,miracoloso,divino,speciale',
        'quality_food': 'Avariato,Qualità Comune,Discreta Qualità,Pregiata Qualità,Qualità Superiore,Qualità Regale',
        'quality_general': ',di qualità,puro,leggendario ',
        'quality_fish': ',fresco ,favoloso ,leggendario ',
        'work_lv': '-,Dilettante,Novizio,Apprendista,Artigiano,Esperto,Adepto,Maestro,Gran Maestro',
        'civility': 'Infima,Bassa,Normale,Alta,Massima',
        'startMode': 'Una notte nel Prato,Una notte nel Prato (Inverno),In una caverna,Un Singolo Blocco (Test)',
        'exhint_AM_Terrain': 'Altezza Immediata: <b>Shift + Clic</b>',
        'guild_title': 'Novizio,Apprendista,Giramondo,Adepto,Esperto,Maestro,Gran Maestro',
        'plant_size': 'estremamente minuscolo ,piccolo ,maneggevole ,piuttosto grande ,enorme ,colossale ,di taglia mostruosa ,più grande di un uomo ,di dimensioni leggendarie ,più pesante di un elefante ',
        'num_rank': '°,°,°,°',
        'fur': 'Appena spuntata,Leggermente soffice,Quasi soffice,Soffice,*Sofficiosissima*',
        'search_words': 'tassa,imposta,istruttore,guardia',
        'fortuneroll': 'Niente da fare,3° Premio,2° Premio,1° Premio',
        'pp_templates': 'Avventuriero Novizio,Avventuriero,Avventuriero Veterano,Personalizzato',
        'pp_titles': 'Avventuriero d’Epoca,Avventuriero Novizio,Avventuriero,Avventuriero Veterano,Avventuriero Leggendario,Avventuriero Mitico',
        'barrel': 'Bo～tte♪,Botte!,Bo～tte!,Botte.'
    }

    count = 0
    for r in range(2, ws.max_row+1):
        id_val = str(ws.cell(row=r, column=headers['id']).value)
        if id_val in list_map:
            ws.cell(row=r, column=headers['text']).value = list_map[id_val]
            count += 1

    wb.save('Lang/IT/Game/List.xlsx')
    print(f'Updated {count} entries in List.xlsx')

if __name__ == '__main__':
    run()
