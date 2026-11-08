import openpyxl

def translate_celleffect():
    path = 'Lang/IT/Game/CellEffect.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    mapping = {
        '1': 'Acqua',
        '2': 'Magma',
        '3': 'Fuoco',
        '4': 'Pozione',
        '5': 'Bolle',
        '6': 'Nebbia',
        '7': 'Ragnatela'
    }
    c = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        if rid in mapping:
            ws.cell(row=r, column=3).value = mapping[rid]
            c += 1
    wb.save(path)
    print(f"CellEffect.xlsx updated: {c} rows.")

def translate_deco():
    path = 'Lang/IT/Game/Deco.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    mapping = {
        '1': 'Bordo in pietra',
        '2': 'Cordolo in pietra',
        '3': 'Cordolo in pietra',
        '4': 'Cordolo in pietra',
        '5': 'Cordolo da cantiere',
        '6': 'Cordolo di tronchi',
        '7': 'Cordolo di tronchi',
        '8': 'Cordolo di mattoni'
    }
    c = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        if rid in mapping:
            ws.cell(row=r, column=3).value = mapping[rid]
            c += 1
    wb.save(path)
    print(f"Deco.xlsx updated: {c} rows.")

def translate_globaltile():
    path = 'Lang/IT/Game/GlobalTile.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    mapping = {
        '0': '???',
        '1': 'Pianura',
        '2': 'Dirupo',
        '3': 'Foresta',
        '13': 'Foresta',
        '4': 'Mare',
        '15': 'Fondale marino',
        '5': 'Montagna',
        '6': 'Montagna rocciosa',
        '7': 'Neve',
        '8': 'Ponte',
        '9': 'Dirupo innevato',
        '10': 'Rupi scoscese',
        '11': 'Strada',
        '12': 'Neve',
        '14': 'Spiaggia'
    }
    c = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        if rid in mapping:
            ws.cell(row=r, column=3).value = mapping[rid]
            c += 1
    wb.save(path)
    print(f"GlobalTile.xlsx updated: {c} rows.")

def translate_research():
    path = 'Lang/IT/Game/Research.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    mapping = {
        'hearth_stone': 'Pietra del Focolare',
        'exploration': 'Licenza di Esplorazione',
        'home_development': 'Piano Urbanistico',
        'construction': 'Ingegneria Civile',
        'department_law': 'Dipartimento di Giustizia',
        'department_life': 'Dipartimento di Sussistenza',
        'department_economy': "Dipartimento dell'Economia",
        'test1': 'Piano di Prova A',
        'test2': 'Piano di Prova B'
    }
    c = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        if rid in mapping:
            ws.cell(row=r, column=3).value = mapping[rid]
            c += 1
    wb.save(path)
    print(f"Research.xlsx updated: {c} rows.")

def translate_note():
    path = 'Lang/IT/Game/Note.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    mapping = {
        'palmia_barrack': 'Alloggi degli Ufficiali Reali di Palmia',
        'tax': 'Paga qui le tue tasse',
        'palmia_safety': 'Commissione di Pubblica Sicurezza di Palmia',
        'wow': 'Uao!',
        'dagger_note': 'Dalla mezzanotte al crepuscolo, lui osserva.',
        'sister': '↓Sorellina  ↑L\'altra donna',
        'odina': 'In onore dei sacrifici di Odina, Dea della Compassione',
        'casino_closed': 'Il parco è temporaneamente chiuso a causa della rivolta delle lumache.',
        'vernis': 'Cercansi Pionieri',
        'farm_chest': 'Mettili pure qui.',
        'hotspring_meditation': 'Fai un "Riposo" alla sorgente termale per riscaldarti anima e corpo!',
        'pond_carp': 'Lo Stagno delle Carpe'
    }
    c = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        if rid in mapping:
            ws.cell(row=r, column=3).value = mapping[rid]
            c += 1
    wb.save(path)
    print(f"Note.xlsx updated: {c} rows.")

def translate_person():
    path = 'Lang/IT/Game/Person.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    # col 3: name, col 9: aka
    mapping = {
        'nerun': {'aka': 'La Guida'},
        'chicken': {'aka': 'Gallina'},
        'farris': {'aka': 'Cantastorie di Olvina'},
        'corgon_shadow': {'name': 'Ombra Gigantesca'},
        'jonan': {'aka': 'Il Signore di Mysilia'},
        'fan1': {'name': 'Ammiratore di Melvin'},
        'fan2': {'name': 'Ammiratore di Melvin'},
        'bunny1': {'name': 'Coniglietta'},
        'bunny2': {'name': 'Coniglietta'},
        'az': {'aka': "L'Impuro"},
        'pebble': {'name': 'Ciottolo'}
    }
    c = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        if rid in mapping:
            data = mapping[rid]
            if 'name' in data:
                ws.cell(row=r, column=3).value = data['name']
                c += 1
            if 'aka' in data:
                ws.cell(row=r, column=9).value = data['aka']
                c += 1
    wb.save(path)
    print(f"Person.xlsx updated: {c} fields.")

if __name__ == '__main__':
    translate_celleffect()
    translate_deco()
    translate_globaltile()
    translate_research()
    translate_note()
    translate_person()
