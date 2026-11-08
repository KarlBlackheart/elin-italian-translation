import openpyxl
import os

def translate_religion():
    path = 'Lang/IT/Game/Religion.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    # Column mapping:
    # 9: textBenefit, 12: textType, 15: name2
    religions = {
        'eyth': {
            'textBenefit': "Eyth non concede alcuna benedizione.",
            'textType': "Vuoto",
            'name2': "Vuoto,Eyth"
        },
        'wind': {
            'textBenefit': "I fedeli di Lulwy ricevono la benedizione del vento e possono muoversi con grande rapidità.",
            'textType': "Dea",
            'name2': "Vento,Lulwy"
        },
        'earth': {
            'textBenefit': "I fedeli di Opatos ottengono una difesa straordinaria e una forza imponente.",
            'textType': "Dio",
            'name2': "Terra,Opatos"
        },
        'element': {
            'textBenefit': "I fedeli di Itzpalt sono protetti dai danni elementali e apprendono come assorbire il mana dall'ambiente circostante.",
            'textType': "Dio",
            'name2': "Elementi,Itzpalt"
        },
        'machine': {
            'textBenefit': "I fedeli di Mani acquisiscono una profonda conoscenza dei macchinari e imparano a usarli con la massima efficacia.",
            'textType': "Dio",
            'name2': "Macchine,Mani"
        },
        'harvest': {
            'textBenefit': "I fedeli di Kumiromi ricevono le copiose benedizioni della natura.",
            'textType': "Dio",
            'name2': "Raccolto,Kumiromi"
        },
        'luck': {
            'textBenefit': "I fedeli di Ehekatl sono baciati da una fortuna straordinaria.",
            'textType': "Dea",
            'name2': "Fortuna,Ehekatl"
        },
        'healing': {
            'textBenefit': "I fedeli di Jure ricevono il sacro dono di guarire le ferite.",
            'textType': "Dea",
            'name2': "Guarigione,Jure"
        },
        'oblivion': {
            'textBenefit': "Sconosciuto",
            'textType': "Dea",
            'name2': "Oblio,Yakasha"
        },
        'harmony': {
            'textBenefit': "Sconosciuto",
            'textType': "Dea",
            'name2': "Armonia,Elin"
        },
        'trickery': {
            'textBenefit': "I fedeli di Kizuami apprendono l'arte di sfruttare al massimo benedizioni e maledizioni.",
            'textType': "Dio",
            'name2': "Inganno,Kizuami"
        },
        'moonshadow': {
            'textBenefit': "I fedeli di Horome padroneggiano le arti arcane e la maestria con la spada.",
            'textType': "Dea",
            'name2': "Ombra Lunare,Horome"
        },
        'strife': {
            'textBenefit': "I fedeli di Yevan ricevono il potere della distruzione per trionfare nelle prove di battaglia.",
            'textType': "Dio",
            'name2': "Guerra,Yevan"
        }
    }

    count = 0
    for r in range(2, ws.max_row + 1):
        rid = ws.cell(row=r, column=1).value
        if rid in religions:
            data = religions[rid]
            ws.cell(row=r, column=9).value = data['textBenefit']
            ws.cell(row=r, column=12).value = data['textType']
            ws.cell(row=r, column=15).value = data['name2']
            count += 3

    wb.save(path)
    print(f"Religion.xlsx updated: {count} fields.")

def translate_tactics():
    path = 'Lang/IT/Game/Tactics.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    tactics = {
        '_': 'Disattivato',
        'archer': 'Arciere',
        'warrior': 'Guerriero',
        'tank': 'Baluardo',
        'priest': 'Guaritore',
        'wizard': 'Mago',
        'hexer': 'Fattucchiere',
        'summoner': 'Evocatore',
        'predator': 'Predatore',
        'gunner': 'Artigliere',
        'warmage': 'Guerriero Magico',
        'thief': 'Furfante',
        'paladin': 'Paladino',
        'turret': 'Torretta',
        'cocoon': 'Bozzolo',
        'runner': 'Inseguitore'
    }

    count = 0
    for r in range(2, ws.max_row + 1):
        rid = ws.cell(row=r, column=1).value
        if rid in tactics:
            ws.cell(row=r, column=3).value = tactics[rid]
            count += 1

    wb.save(path)
    print(f"Tactics.xlsx updated: {count} fields.")

def translate_zoneaffix():
    path = 'Lang/IT/Game/ZoneAffix.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    affixes = {
        '1': 'Ordinario',
        '2': 'Capriccioso',
        '3': 'Contaminato',
        '4': 'Silenzioso',
        '5': 'Montano',
        '6': 'Giocoso',
        '7': 'Spirito',
        '8': 'Malinconico',
        '9': 'Pericoloso',
        '10': 'Intricato',
        '11': 'Del Non Ritorno',
        '12': 'Bizzarro',
        '13': 'Tragico',
        '14': 'Sinistro',
        '15': 'Inquietante',
        '16': 'Terrificante',
        '17': 'Muschioso',
        '18': 'Antico',
        '19': 'Umido',
        '20': 'Storico',
        '21': 'Ignoto',
        '22': 'Tradizionale',
        '23': 'Senza Nome',
        '24': 'Distorto',
        '25': 'Proibito',
        '26': 'Silente',
        '27': 'Nebbioso',
        '28': 'Tetro',
        '29': 'Incantato',
        '30': 'Mistico',
        '31': 'Blasfemo',
        '32': 'Devastato',
        '33': 'Fatiscente',
        '34': 'Isolato',
        '35': 'Arcano',
        '36': 'Rigoglioso',
        '37': 'Rustico',
        '38': 'Della Guida',
        '39': 'Terroso',
        '40': 'Protetto'
    }

    count = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        if rid in affixes:
            ws.cell(row=r, column=3).value = affixes[rid]
            count += 1

    wb.save(path)
    print(f"ZoneAffix.xlsx updated: {count} fields.")

def translate_hobby():
    path = 'Lang/IT/Game/Hobby.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    hobbies = {
        '1': 'Giardinaggio',
        '2': 'Lettura',
        '3': 'Caccia',
        '4': 'Esercizio fisico',
        '5': 'Suonare strumenti',
        '6': 'Cucina',
        '7': 'Preghiera',
        '8': 'Scrittura',
        '9': 'Pittura',
        '10': 'Passeggiate',
        '11': 'Bagni caldi',
        '12': 'Pulizia',
        '13': 'Canto',
        '14': 'Lotteria',
        '15': 'Gacha',
        '16': 'Diario',
        '17': 'Storia',
        '18': 'Blog',
        '19': 'Pisolini',
        '20': 'Fare il tifo',
        '21': 'Romanticherie',
        '22': 'Autolesionismo',
        '23': 'Sostanze',
        '24': 'Bucato',
        '25': 'Rovistare rifiuti',
        '26': 'Dieta',
        '27': 'Artigianato',
        '28': 'Shopping',
        '29': 'Bere alcolici',
        '30': 'Fumo',
        '31': 'Cura dei malati',
        '32': 'Videogiochi',
        '33': 'Accarezzare morbidezza',
        '34': 'Piacere personale',
        '35': 'Animali da compagnia',
        '36': 'Meditazione',
        '37': 'Antiquariato',
        '38': 'Agricoltura',
        '50': 'Pioniere',
        '39': 'Ricerca',
        '40': 'Pesca',
        '41': 'Esplorazione',
        '42': 'Faccende domestiche',
        '43': 'Forgia',
        '44': 'Taglialegna',
        '45': 'Allevamento',
        '46': 'Supervisione',
        '47': 'Assassinio',
        '48': 'Spese folli',
        '49': 'Rambo',
        '51': 'Pettegolezzo',
        '52': 'Caccia al tesoro',
        '53': 'Accumulo di tesori'
    }

    details = {
        14: "Pulisce la casa",
        32: "Tasse elevate",
        33: "Rianimazione automatica dei residenti",
        41: "Crescita accelerata della Pietra del Focolare",
        45: "Pulisce la casa",
        51: "Tasse elevate",
        54: "Raccoglie automaticamente tesori (richiede una mappa del tesoro)"
    }

    count = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        if rid in hobbies:
            ws.cell(row=r, column=3).value = hobbies[rid]
            count += 1
        if r in details:
            ws.cell(row=r, column=6).value = details[r]
            count += 1

    wb.save(path)
    print(f"Hobby.xlsx updated: {count} fields.")

if __name__ == '__main__':
    translate_religion()
    translate_tactics()
    translate_zoneaffix()
    translate_hobby()
