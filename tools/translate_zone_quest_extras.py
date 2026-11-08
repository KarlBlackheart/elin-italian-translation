import openpyxl

def translate_block_extra():
    path = 'Lang/IT/Game/Block.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    ws.cell(row=131, column=6).value = 'Un blocco invisibile utilizzato per delimitare le stanze.'
    wb.save(path)
    print("Block.xlsx extra detail updated.")

def translate_quest_extras():
    path = 'Lang/IT/Game/Quest.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    # r89 (into_darkness3): detail col 6
    # r93 (into_darkness7): detail col 6
    for r in range(2, ws.max_row + 1):
        rid = ws.cell(row=r, column=1).value
        if rid == 'into_darkness3':
            ws.cell(row=r, column=6).value = '|Aspettiamo che Kettle faccia ritorno.'
        elif rid == 'into_darkness7':
            ws.cell(row=r, column=6).value = '|Il tuo compito nella Cripta dei Dannati è terminato. È ora di attendere notizie da Issizzle alla base.'

    wb.save(path)
    print("Quest.xlsx extras updated.")

def translate_zone_flavors():
    path = 'Lang/IT/Game/Zone.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    # col 3: name, col 6: detail, col 9: textFlavor
    flavors = {
        'kapul': 'Vedi Port Kapul. Il porto brulica di navi e mercanti.',
        'nymelle': 'Vedi la caverna di Nymelle. Il fischio del vento riecheggia nelle profondità.',
        'lysanas': 'Vedi le rovine di Lysanas. Senti che qualcosa di fondamentale giace sepolto qui.',
        'void': 'Cosa diavolo è questo posto...?',
        'tinkerCamp': "Vedi l'accampamento dei mercanti itineranti. È vivace come il quartiere di una città!",
        'olvina': 'Vedi il villaggio di Olvina. Si percepisce il profumo di vino e di sorgenti termali.',
        'embassy_palmia': "Vedi l'ambasciata di Palmia. L'edificio è sorvegliato a vista.",
        'aquli': 'Vedi un edificio davvero bizzarro.',
        'yowyn': 'Vedi il villaggio di Yowyn. Ti torna in mente con nostalgia il dolce profumo della terra.',
        'specwing': "Vedi un albero mastodontico. Le fate volteggiano leggiadre nell'aria.",
        'village_exile': 'Vedi un villaggio abbandonato nel cuore della foresta oscura.',
        'foxtown': "Vedi un placido villaggio esotico. L'aria profuma di risaie.",
        'foxtown_nefu': 'Vedi un grande tempio esotico. Lo scroscio di una cascata risuona solenne.',
        'casino': "Vedi un'enorme aeronave che fluttua nel cielo.",
        'palmia': 'Vedi la grandiosa capitale di Palmia. La città è cinta da possenti mura.',
        'lothria': 'Vedi la fortezza di Willow. I rami dei salici ondeggiano dolcemente al vento.',
        'mysilia': "Vedi la città di Mysilia. Immersa nella natura, regna un'atmosfera pacifica e serena.",
        'derphy': 'Vedi la famigerata città di Derphy. Si respira un\'aria decisamente pericolosa.',
        'lesimas': 'Vedi i sotterranei di Lesimas. Percepisci il palpito inesorabile del destino.',
        'jail': "Vedi una prigione. L'ingresso è sbarrato con estrema cura.",
        'cave_dead': "Un brivido gelido ti attraversa, congelandoti fin nel profondo dell'anima.",
        'little_garden': 'Vedi un giardino curato con amorevole grazia. Ti trasmette un senso di calore al cuore.',
        'chaos_castle': 'Vedi una fortezza spettrale. Il tuo istinto ti implora di non entrare mai.',
        'cave_mino': "È la tana di un minotauro. L'apertura della caverna è mastodontica.",
        'cave_yeek': "Vedi una caverna abitata dagli yeek. L'accesso è davvero minuscolo.",
        'temple_undersea': 'Vedi un passaggio che conduce a rovine sommerse negli abissi marini.',
        'lumiest': 'Vedi la magnifica Lumiest. Il gorgoglio armonioso dell\'acqua echeggia dolcemente.',
        'truce_ground': 'Vedi antichi santuari. Un\'aura sacra avvolge l\'intero suolo.',
        'miral_garok': 'Vedi un caratteristico laboratorio artigianale. Si odono miagolii di gatti.',
        'guild_merchant': 'Vedi la gilda dei mercanti. Numerosi carri e carretti sono parcheggiati all\'esterno.',
        'cursed_manor': 'Vedi una sontuosa villa. L\'aria nei dintorni è incredibilmente gelida.',
        'noyel': 'Vedi il villaggio innevato di Noyel. Le risate argentine dei bambini echeggiano nella piazza.',
        'windrest': 'Vedi una foresta insolita e immobile, dove non spira nemmeno un alito di vento.',
        'snowgrave': 'È forse questa... la fine del mondo?',
        'lumiest_graveyard': 'Vedi il cimitero di Lumiest. Il silenzio circostante è totale, quasi irreale...',
        'asylum': 'Vedi un orfanotrofio. Le risate serene dei bambini risuonano nel cortile.'
    }

    details = {
        'asseria': 'Il continente a est del Mare di Asseria.',
        'wilds': 'Un luogo sconosciuto dove vagano creature ignote e persone disperse.'
    }

    names = {
        'tent_snow': 'Iglu',
        'snowgrave': 'Gelo Perenne'
    }

    c = 0
    for r in range(2, ws.max_row + 1):
        rid = ws.cell(row=r, column=1).value
        if rid in flavors:
            ws.cell(row=r, column=9).value = flavors[rid]
            c += 1
        if rid in details:
            ws.cell(row=r, column=6).value = details[rid]
            c += 1
        if rid in names:
            ws.cell(row=r, column=3).value = names[rid]
            c += 1

    wb.save(path)
    print(f"Zone.xlsx updated: {c} fields.")

if __name__ == '__main__':
    translate_block_extra()
    translate_quest_extras()
    translate_zone_flavors()
