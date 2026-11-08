import openpyxl

def translate_floor():
    path = 'Lang/IT/Game/Floor.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    mapping = {
        'Editor Floor(Exterior)': 'Pavimento editor (esterno)',
        'Editor Floor(Interior)': 'Pavimento editor (interno)',
        'Editor Floor(Sky)': 'Pavimento editor (cielo)',
        'Editor Floor(Transparent)': 'Pavimento editor (trasparente)',
        'Tatami': 'Tatami',
        'alien floor': 'Pavimento alieno',
        'ash floor': 'Pavimento carbonizzato',
        'barren soil floor': 'Pavimento di terra brulla',
        'biscuit floor': 'Pavimento di biscotto',
        'brick floor': 'Pavimento di mattoni',
        'bridge': 'Ponte',
        'bush floor': 'Pavimento di cespugli',
        'carpet': 'Tappeto',
        'cave floor': 'Pavimento di caverna',
        'chocolate floor': 'Pavimento di cioccolato',
        'cloud floor': 'Pavimento di nuvole',
        'crystal floor': 'Pavimento di cristallo',
        'cute floor': 'Pavimento grazioso',
        'deep grass floor': 'Pavimento di erba fitta',
        'deep water': 'Acqua profonda',
        'dried soil floor': 'Pavimento di terra arida',
        'field': 'Terreno coltivato',
        'glass floor': 'Pavimento di vetro',
        'grass floor': 'Pavimento erboso',
        'ice floor': 'Pavimento di ghiaccio',
        'lawn floor': 'Pavimento a prato',
        'log floor': 'Pavimento di tronchi',
        'magma': 'Magma',
        'metal floor': 'Pavimento di metallo',
        'metal grille floor': 'Pavimento a grata metallica',
        'mirror floor': 'Pavimento a specchio',
        'modern carpet': 'Tappeto moderno',
        'modern floor': 'Pavimento moderno',
        'mushroom floor': 'Pavimento di funghi',
        'pedestal': 'Piedistallo',
        'plain floor': 'Pavimento semplice',
        'plank floor': 'Pavimento di assi',
        'plank pattern floor': 'Pavimento a trama lignea',
        'quality plank floor': 'Pavimento di assi pregiate',
        'red algae floor': 'Pavimento di alghe rosse',
        'ruin floor': 'Pavimento di rovine',
        'rusty metal floor': 'Pavimento di metallo arrugginito',
        'sand floor': 'Pavimento di sabbia',
        'seabed floor': 'Pavimento di fondale marino',
        'shallow water': 'Acqua bassa',
        'smooth soil floor': 'Pavimento di terra battuta',
        'snow floor': 'Pavimento innevato',
        'soil floor': 'Pavimento di terra',
        'solid soil floor': 'Pavimento di terra compatta',
        'stage floor': 'Pavimento da palcoscenico',
        'stone floor': 'Pavimento di pietra',
        'straw floor': 'Pavimento di paglia',
        'support floor': 'Pavimento di impalcatura',
        'thick grass floor': 'Pavimento di erba alta',
        'tile floor': 'Pavimento di piastrelle',
        'tricky floor': 'Pavimento ingannevole',
        'very shallow water': 'Acqua molto bassa',
        'water': 'Acqua',
        'wooden grille floor': 'Pavimento a graticcio di legno'
    }

    c = 0
    for r in range(2, ws.max_row + 1):
        rid = str(ws.cell(row=r, column=1).value)
        en = ws.cell(row=r, column=4).value
        if not en:
            continue
        if en == 'wooden floor':
            if rid == '41':
                ws.cell(row=r, column=3).value = 'Pavimento in legno massiccio'
            else:
                ws.cell(row=r, column=3).value = 'Pavimento a zattera'
            c += 1
        elif en in mapping:
            ws.cell(row=r, column=3).value = mapping[en]
            c += 1

    wb.save(path)
    print(f"Floor.xlsx updated: {c} items.")

def translate_obj():
    path = 'Lang/IT/Game/Obj.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    mapping = {
        'For Test': 'Oggetto di prova',
        'acacia tree': 'Acacia',
        'api': 'Pianta di api',
        'apple tree': 'Melo',
        'bamboo': 'Bambù',
        'banana tree': 'Banano',
        'berry': 'Cespuglio di bacche',
        'big fossil tree': 'Grande albero fossile',
        'big rock': 'Grande roccia',
        'birch tree': 'Betulla',
        'bird\'s nest': 'Nido d\'uccello',
        'blue flower': 'Fiore blu',
        'blue grass': 'Erba blu',
        'bollard': 'Bitta d\'ormeggio',
        'bone': 'Ossa di drago',
        'bone mound': 'Cumulo d\'ossa',
        'border': 'Bordo',
        'burnt tree': 'Albero bruciato',
        'cabbage': 'Cavolo',
        'cabocchi': 'Cabocchi',
        'cactus': 'Cactus',
        'carrot': 'Carota',
        'cattail': 'Tifa',
        'cedar tree': 'Cedro',
        'chasm': 'Voragine',
        'chemicals': 'Sostanze chimiche',
        'cherry blossom tree': 'Ciliegio in fiore',
        'christmas tree': 'Albero di Natale',
        'chunk': 'Blocco di minerale',
        'coffee': 'Pianta di caffè',
        'conveyor belt': 'Nastro trasportatore',
        'coral': 'Corallo',
        'coral reef': 'Barriera corallina',
        'coralwood tree': 'Albero di legnocorallo',
        'corn': 'Mais',
        'cotton': 'Pianta di cotone',
        'cracked floor': 'Pavimento crepato',
        'crim': 'Frutto di crim',
        'crystal': 'Cristallo',
        'debris': 'Detriti',
        'decayed fossil': 'Fossile deteriorato',
        'decayed fossil tree': 'Albero fossile deteriorato',
        'decayed tree': 'Tronco marcio',
        'decayed wall': 'Muro crollato',
        'deep seaweed': 'Alga abissale',
        'egg': 'Uovo',
        'fern': 'Felce',
        'feywood tree': 'Albero fatato',
        'fir tree': 'Abete',
        'fish silhouette': 'Sagoma di pesce',
        'flower': 'Fiore',
        'fossil tree': 'Albero fossile',
        'fragments': 'Frammenti',
        'gem ore': 'Filone di gemme',
        'grape': 'Vite d\'uva',
        'green grass': 'Erba verde',
        'huge rock': 'Roccia colossale',
        'hydrangea': 'Ortensia',
        'imo': 'Imo',
        'mahogany tree': 'Mogano',
        'metal frame': 'Telaio metallico',
        'momiji': 'Acero momiji',
        'moss': 'Muschio',
        'mound': 'Monticello di terra',
        'mushroom': 'Fungo',
        'mushroom tree': 'Albero fungo',
        'narrow road': 'Sentiero stretto',
        'neon line': 'Striscia al neon',
        'oak tree': 'Quercia',
        'orange tree': 'Arancio',
        'ore': 'Filone minerario',
        'palulu tree': 'Albero di palulu',
        'pasture': 'Erba da pascolo',
        'pear tree': 'Pero',
        'pebble': 'Ciottolo',
        'pile of fallen leaves': 'Mucchio di foglie secche',
        'pine tree': 'Pino',
        'purple grass': 'Erba viola',
        'radish': 'Daikon',
        'rafflesia': 'Rafflesia',
        'rainbow fruit': 'Frutto multicolore',
        'red grass': 'Erba rossa',
        'red pepper': 'Peperoncino',
        'remain': 'Resti mortali',
        'rice': 'Riso',
        'road': 'Sentiero',
        'roof': 'Tetto',
        'rose': 'Rosa',
        'rosewood tree': 'Palissandro',
        'salt rock': 'Salgemma',
        'seaweed': 'Alga marina',
        'shell': 'Conchiglia',
        'silver grass': 'Erba argentea',
        'stalagmite': 'Stalagmite',
        'stepping stone': 'Pietra da guado',
        'stone': 'Pietra',
        'stone road': 'Sentiero lastricato',
        'stump': 'Ceppo',
        'sulfur rock': 'Roccia di zolfo',
        'sunflower': 'Girasole',
        'sweet imo': 'Imo dolce',
        'tea': 'Pianta del tè',
        'test': 'Pianta di prova',
        'tobacc': 'Pianta di tabacco',
        'tomato': 'Pomodoro',
        'track': 'Binario ferroviario',
        'tulip': 'Tulipano',
        'vine bush': 'Cespuglio rampicante',
        'wall support': 'Puntello di legno',
        'water lily': 'Ninfea',
        'weed': 'Erbaccia',
        'wheat': 'Grano',
        'white flower': 'Fiore bianco',
        'white line': 'Linea bianca',
        'willow tree': 'Salice',
        'window': 'Finestra',
        'wooden frame': 'Telaio di legno',
        'wreck': 'Relitto',
        'yellow flower': 'Fiore giallo'
    }
    # Roofs: roof2..roof17
    for i in range(2, 18):
        mapping[f'roof{i}'] = f'Tetto {i}'

    c = 0
    for r in range(2, ws.max_row + 1):
        en = ws.cell(row=r, column=4).value
        if en and en in mapping:
            ws.cell(row=r, column=3).value = mapping[en]
            c += 1

    wb.save(path)
    print(f"Obj.xlsx updated: {c} items.")

def translate_block():
    path = 'Lang/IT/Game/Block.xlsx'
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    mapping = {
        'Editor Block(Exterior)': 'Blocco editor (esterno)',
        'Editor Block(Interior)': 'Blocco editor (interno)',
        'Editor Block(Invisiblel)': 'Blocco editor (invisibile)',
        'alien block': 'Blocco alieno',
        'alien pillar': 'Pilastro alieno',
        'alien wall': 'Parete aliena',
        'arch pillar': 'Pilastro ad arco',
        'arch wall': 'Parete ad arco',
        'ash block': 'Blocco carbonizzato',
        'ash wall': 'Parete carbonizzata',
        'atrium wall': 'Parete da atrio',
        'barbed wire fence': 'Recinzione di filo spinato',
        'biscuit block': 'Blocco di biscotto',
        'biscuit pillar': 'Pilastro di biscotto',
        'biscuit wall': 'Parete di biscotto',
        'brick block': 'Blocco di mattoni',
        'brick pillar': 'Pilastro di mattoni',
        'brick wall': 'Parete di mattoni',
        'casino wall': 'Parete da casinò',
        'chocolate block': 'Blocco di cioccolato',
        'chocolate pillar': 'Pilastro di cioccolato',
        'chocolate wall': 'Parete di cioccolato',
        'cloud block': 'Blocco di nuvola',
        'cookie block': 'Blocco di cookie',
        'coral block': 'Blocco di corallo',
        'crystal pillar': 'Pilastro di cristallo',
        'crystal wall': 'Parete di cristallo',
        'deco block': 'Blocco decorativo',
        'fake wall(experimental)': 'Parete illusoria (sperimentale)',
        'fluffy block': 'Blocco soffice',
        'gear fence': 'Recinzione a ingranaggi',
        'glass block': 'Blocco di vetro',
        'glass wall': 'Parete di vetro',
        'grass block': 'Blocco erboso',
        'grass fence': 'Recinzione d\'erba',
        'grass wall': 'Parete d\'erba',
        'ice block': 'Blocco di ghiaccio',
        'jail wall': 'Parete di prigione',
        'ladder': 'Scala a pioli',
        'lattice wall': 'Parete a graticcio',
        'log block': 'Blocco di tronchi',
        'log wall': 'Parete di tronchi',
        'lumiest wall': 'Parete di Lumiest',
        'magma block': 'Blocco di magma',
        'metal block': 'Blocco di metallo',
        'metal fence': 'Recinzione di metallo',
        'mirror block': 'Blocco a specchio',
        'mirror wall': 'Parete a specchio',
        'modern pillar': 'Pilastro moderno',
        'modern wall': 'Parete moderna',
        'mushroom pillar': 'Pilastro di funghi',
        'natural half-stairs': 'Mezza scala naturale',
        'natural ramp': 'Pendenza naturale',
        'natural step': 'Gradino naturale',
        'organ block': 'Blocco d\'organi',
        'palmian block': 'Blocco di Palmia',
        'palmian pillar': 'Pilastro di Palmia',
        'palmian wall': 'Parete di Palmia',
        'paper wall': 'Parete di carta shoji',
        'plain block': 'Blocco d\'intonaco',
        'plain pillar': 'Pilastro d\'intonaco',
        'plain wall': 'Parete d\'intonaco',
        'plank block': 'Blocco di assi',
        'plank half-stairs': 'Mezza scala di assi',
        'plank ramp': 'Pendenza di assi',
        'plank stairs': 'Scala di assi',
        'plank wall': 'Parete di assi',
        'quality plank block': 'Blocco di assi pregiate',
        'quality plank wall': 'Parete di assi pregiate',
        'reinforced plank block': 'Blocco di assi rinforzate',
        'rooftop': 'Colmo del tetto',
        'rope pillar': 'Pilastro di corda',
        'sand block': 'Blocco di sabbia',
        'sandbag fence': 'Barricata di sacchi di sabbia',
        'sandbag pillar': 'Pilastro di sacchi di sabbia',
        'sandbag wall': 'Parete di sacchi di sabbia',
        'scaffold': 'Impalcatura',
        'shelf stairs': 'Scala a cassettiera',
        'ship block': 'Blocco navale',
        'skeleton stairs': 'Scala a giorno',
        'snow block': 'Blocco di neve',
        'soil block': 'Blocco di terra',
        'soil block covered with roots': 'Blocco di terra con radici',
        'soil block covered with vines': 'Blocco di terra con rampicanti',
        'sponage block': 'Blocco di spugna',
        'stake fence': 'Palizzata di pali',
        'stone block': 'Blocco di pietra',
        'stone fence': 'Recinzione di pietra',
        'stone half-stairs': 'Mezza scala di pietra',
        'stone pillar': 'Pilastro di pietra',
        'stone ramp': 'Pendenza di pietra',
        'stone stairs': 'Scala di pietra',
        'stone step': 'Gradino di pietra',
        'stone wall': 'Parete di pietra',
        'straw block': 'Blocco di paglia',
        'straw wall': 'Parete di paglia',
        'tent pillar': 'Pilastro da tenda',
        'tent wall': 'Parete di tenda',
        'thick plank wall': 'Parete di assi spesse',
        'undersea block': 'Blocco sottomarino',
        'unknown block': 'Blocco misterioso',
        'water block': 'Blocco d\'acqua',
        'waterfall': 'Cascata',
        'wire mesh fence': 'Recinzione a rete metallica',
        'wood block': 'Blocco di legno massiccio',
        'wooden fence': 'Recinzione di legno',
        'wooden pillar': 'Pilastro di legno'
    }

    c = 0
    for r in range(2, ws.max_row + 1):
        en = ws.cell(row=r, column=4).value
        if en and en in mapping:
            ws.cell(row=r, column=3).value = mapping[en]
            c += 1

    wb.save(path)
    print(f"Block.xlsx updated: {c} items.")

if __name__ == '__main__':
    translate_floor()
    translate_obj()
    translate_block()
