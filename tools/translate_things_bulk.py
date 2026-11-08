import openpyxl
import re

# Comprehensive dictionary of item translations for Thing.xlsx
item_dict = {
    # Crafting Stations & Workbenches
    'workbench': 'banco da lavoro',
    'workbench_carpenter': 'banco da carpentiere',
    'workbench_mason': 'banco da scalpellino',
    'workbench_tailor': 'telaio da sarto',
    'workbench_tinker': 'banco dell\'inventore',
    'workbench_alchemy': 'alambicco alchemico',
    'workbench_jeweler': 'banco da gioielliere',
    'furnace': 'fornace di fusione',
    'anvil': 'incudine',
    'sawmill': 'segheria',
    'loom': 'telaio per tessitura',
    'spinning_wheel': 'arcolaio',
    'pottery_wheel': 'tornio da vasaio',
    'stove': 'fornello da cucina',
    'cauldron': 'calderone',
    'kitchen': 'cucina completa',
    'cutting board': 'tagliere da cucina',
    'chopper': 'tagliere',
    'mixer': 'miscelatore',
    'microwave oven': 'forno a microonde',
    'oven': 'forno in muratura',
    'pot': 'pentola',
    'frying pan': 'padella',
    'millstone': 'macina di pietra',
    'grindstone': 'mola per affilare',
    'fermenter': 'botte di fermentazione',
    'distiller': 'distillatore',
    'campfire': 'falò da campo',
    'bonfire': 'grande falò',

    # Containers & Storage
    'backpack': 'zaino da viaggio',
    'backpack_holding': 'zaino conservante',
    'quiver': 'faretra per frecce',
    'pouch': 'borsello da cintura',
    'cooler box': 'borsa termica',
    'cooler': 'ghiacciaia',
    'chest': 'baule di legno',
    'chest_iron': 'forziere di ferro',
    'chest_treasure': 'forziere del tesoro',
    'chest_modern': 'contenitore moderno',
    'closet': 'armadio',
    'wardrobe': 'guardaroba',
    'dresser': 'cassettiera',
    'cupboard': 'credenza',
    'cabinet': 'armadietto',
    'bookshelf': 'libreria',
    'shelf': 'scaffale',
    'rack': 'rastrelliera',
    'safe': 'cassaforte blindata',
    'wallet': 'portamonete',
    'trash can': 'cestino dei rifiuti',
    'waste basket': 'cestino',
    'barrel': 'barile di legno',
    'cask': 'botte',
    'crate': 'cassa da imballaggio',
    'basket': 'cesto di vimini',
    'urn': 'urna cineraria',
    'vase': 'vaso decorativo',

    # Furniture & Household
    'chair': 'sedia',
    'wooden chair': 'sedia di legno',
    'armchair': 'poltrona',
    'sofa': 'divano',
    'couch': 'divano imbottito',
    'stool': 'sgabello',
    'bench': 'panca',
    'table': 'tavolo',
    'wooden table': 'tavolo di legno',
    'dining table': 'tavolo da pranzo',
    'desk': 'scrivania',
    'bed': 'letto',
    'double bed': 'letto matrimoniale',
    'bunk bed': 'letto a castello',
    'coffin': 'bara di legno',
    'pillow': 'cuscino',
    'blanket': 'coperta',
    'carpet': 'tappeto',
    'rug': 'tappetino',
    'curtain': 'tenda per finestra',
    'mirror': 'specchio',
    'clock': 'orologio a pendolo',
    'bathtub': 'vasca da bagno',
    'toilet': 'servizio igienico',
    'chamber pot': 'pitale',
    'sink': 'lavello',
    'shower': 'doccia',

    # Lighting & Architecture
    'candle': 'candela di cera',
    'candlestick': 'candelabro',
    'candelabra': 'grande candelabro',
    'lantern': 'lanterna portatile',
    'lamp': 'lampada',
    'street lamp': 'lampione stradale',
    'old street lamp': 'lampione antico',
    'chandelier': 'lampadario di cristallo',
    'door': 'porta di legno',
    'iron door': 'porta di ferro',
    'jail door': 'porta a sbarre',
    'window': 'finestra di vetro',
    'fence': 'staccionata di legno',
    'gate': 'cancello d\'ingresso',
    'wall': 'parete in muratura',
    'brick': 'mattone da costruzione',
    'pillar': 'pilastro di pietra',
    'column': 'colonna di marmo',
    'stairs': 'scala di legno',
    'stairway': 'scalinata di pietra',
    'ladder': 'scala a pioli',
    'bridge': 'ponte pedonale',
    'fountain': 'fontana ornamentale',
    'chimney': 'comignolo',
    'well': 'pozzo d\'acqua',

    # Plants, Trees & Agriculture
    'plant': 'pianta ornamentale',
    'small plant': 'piantina',
    'potted plant': 'pianta in vaso',
    'flower': 'fiore profumato',
    'sunflower': 'girasole',
    'rose': 'rosa rossa',
    'tulip': 'tulipano',
    'lily': 'giglio',
    'tree': 'albero',
    'sapling': 'arbusto giovane',
    'bush': 'cespuglio',
    'grass': 'ciuffo d\'erba',
    'weed': 'erbaccia',
    'mushroom': 'fungo',
    'spore': 'spora fungina',
    'bamboo': 'canna di bambù',
    'cactus': 'cactus del deserto',
    'vine': 'rampicante',
    'seed': 'sacchetto di semi',

    # Food & Ingredients
    'apple': 'mela croccante',
    'orange': 'arancia succosa',
    'grape': 'grappolo d\'uva',
    'strawberry': 'fragola dolce',
    'cherry': 'ciliegia',
    'banana': 'banana',
    'lemon': 'limone aspro',
    'melon': 'melone',
    'watermelon': 'anguria fresca',
    'tomato': 'pomodoro maturo',
    'carrot': 'carota',
    'radish': 'ravanello',
    'onion': 'cipolla',
    'garlic': 'spicchio d\'aglio',
    'potato': 'patata',
    'corn': 'pannocchia di mais',
    'wheat': 'spiga di grano',
    'rice': 'chicchi di riso',
    'cabbage': 'cavolo',
    'lettuce': 'foglia di lattuga',
    'meat': 'pezzo di carne',
    'raw meat': 'carne cruda',
    'cooked meat': 'carne cotta',
    'meat on the bone': 'carne con osso',
    'steak': 'bistecca alla brace',
    'fish': 'pesce pescato',
    'raw fish': 'pesce crudo',
    'sashimi': 'sashimi di pesce fresco',
    'bread': 'pane fragrante',
    'loaf of bread': 'pagnotta di pane',
    'sandwich': 'panino imbottito',
    'hamburger': 'hamburger succoso',
    'pizza': 'fetta di pizza',
    'cheese': 'forma di formaggio',
    'egg': 'uovo fresco',
    'fried egg': 'uovo al tegamino',
    'milk': 'bottiglia di latte fresco',
    'soup': 'zuppa calda',
    'stew': 'stufato saporito',
    'curry': 'piatto di curry speziato',
    'pasta': 'piatto di pasta al dente',
    'noodle': 'ciotola di tagliolini',
    'ramen': 'ciotola di ramen caldo',
    'cake': 'torta squisita',
    'pancake': 'pancake dorato',
    'cookie': 'biscotto friabile',
    'candy': 'caramella dolce',
    'chocolate': 'tavoletta di cioccolato',
    'honey': 'vasetto di miele',
    'jam': 'barattolo di marmellata',
    'water': 'fiala d\'acqua pura',
    'potion of water': 'pozione d\'acqua pura',
    'holy water': 'acqua santa benedetta',
    'wine': 'bottiglia di vino pregiato',
    'beer': 'boccale di birra fresca',
    'ale': 'boccale di birra scura',
    'whiskey': 'bicchiere di whisky',
    'tea': 'tazza di tè caldo',
    'coffee': 'tazza di caffè fumante',
    'juice': 'bicchiere di succo',
    'ration': 'razione da viaggio',
    'fortune cookie': 'biscotto della fortuna',
    'cone': 'pigna',

    # Tools, Instruments & Everyday Items
    'pickaxe': 'piccone da scavo',
    'shovel': 'pala da giardiniere',
    'axe': 'scure da boscaiolo',
    'fishing rod': 'canna da pesca',
    'fishingpole': 'canna da pesca',
    'hoe': 'zappa agricola',
    'hammer': 'martello da lavoro',
    'sickle': 'falcetto da mietitura',
    'watering can': 'annaffiatoio',
    'torch': 'braciere da terra',
    'torch_held': 'torcia da esplorazione',
    'lockpick': 'grimaldello di ferro',
    'wrench': 'chiave inglese',
    'stethoscope': 'stetoscopio medico',
    'leash': 'guinzaglio da bestie',
    'whistle': 'fischietto d\'ottone',
    'bell': 'campanella',
    'guitar': 'chitarra a corde',
    'lute': 'liuto melodioso',
    'piano': 'pianoforte a coda',
    'violin': 'violino di legno',
    'trumpet': 'tromba d\'ottone',
    'flute': 'flauto traverso',
    'drum': 'tamburo da parata',
    'harp': 'arpa celtica',
    'dice': 'dado da gioco',
    'cards': 'mazzo di carte da gioco',
    'plushie': 'peluche morbido',
    'doll': 'bambola di pezza',
    'painting': 'quadro d\'autore',
    'poster': 'poster illustrato',
    'banner': 'stendardo araldico',
    'flag': 'bandiera al vento',
    'statue': 'statua scolpita',
    'trophy': 'trofeo celebrativo',
    'book': 'libro rilegato',
    'grimoire': 'tomo arcano',
    'blank paper': 'foglio di carta bianca',
    'scroll': 'pergamena arrotolata',
    'letter': 'lettera sigillata',
    'diary': 'diario personale',
    'gold bar': 'lingotto d\'oro massiccio',
    'gold coin': 'moneta d\'oro',
    'platinum coin': 'moneta di platino',
    'small medal': 'piccola medaglia',
    'token': 'gettone di scambio'
}

file_p = 'd:/Mod/Elin/Lang/IT/Game/Thing.xlsx'
wb = openpyxl.load_workbook(file_p)
ws = wb.active
headers = [str(c.value) for c in ws[1]]
name_col = headers.index('name') + 1
name_en_col = headers.index('name_EN') + 1

count = 0
for r in range(2, ws.max_row + 1):
    curr_name = ws.cell(row=r, column=name_col).value
    en_name = ws.cell(row=r, column=name_en_col).value
    
    if en_name:
        en_str = str(en_name).strip().lower()
        
        # 1. Exact match in item_dict
        if en_str in item_dict:
            ws.cell(row=r, column=name_col, value=item_dict[en_str])
            count += 1
            continue
            
        # 2. Pattern matching for common combinations
        if en_str.startswith('small ') and en_str[6:] in item_dict:
            ws.cell(row=r, column=name_col, value=item_dict[en_str[6:]] + ' piccol#o')
            count += 1
            continue
            
        if en_str.startswith('wooden ') and en_str[7:] in item_dict:
            ws.cell(row=r, column=name_col, value=item_dict[en_str[7:]] + ' di legno')
            count += 1
            continue

        if en_str.startswith('stone ') and en_str[6:] in item_dict:
            ws.cell(row=r, column=name_col, value=item_dict[en_str[6:]] + ' di pietra')
            count += 1
            continue

        if en_str.startswith('iron ') and en_str[5:] in item_dict:
            ws.cell(row=r, column=name_col, value=item_dict[en_str[5:]] + ' di ferro')
            count += 1
            continue

        if en_str.startswith('ancient ') and en_str[8:] in item_dict:
            ws.cell(row=r, column=name_col, value=item_dict[en_str[8:]] + ' antic#o')
            count += 1
            continue

        if en_str.startswith('giant ') and en_str[6:] in item_dict:
            ws.cell(row=r, column=name_col, value=item_dict[en_str[6:]] + ' gigante')
            count += 1
            continue

        if en_str.endswith(' seed') and en_str[:-5] in item_dict:
            ws.cell(row=r, column=name_col, value='seme di ' + item_dict[en_str[:-5]])
            count += 1
            continue

        if en_str.endswith(' poster'):
            base = en_str[:-7]
            ws.cell(row=r, column=name_col, value='poster di ' + base)
            count += 1
            continue

        if en_str.endswith(' statue') and en_str[:-7] in item_dict:
            ws.cell(row=r, column=name_col, value='statua di ' + item_dict[en_str[:-7]])
            count += 1
            continue

wb.save(file_p)
print(f'Thing.xlsx translated {count} additional items!')
