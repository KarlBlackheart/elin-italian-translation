import json, re

def generate_translations():
    unique_names = json.load(open('scratch/thing_unique_names.json', 'r', encoding='utf-8'))
    
    # Base dictionary of explicit translations
    exact_map = {
        'wakizashi': 'wakizashi',
        'Kogitsunemaru': 'Kogitsunemaru',
        'Sugaki': 'Sugaki',
        'Ragnarok': 'Ragnarok',
        'Masamune': 'Masamune',
        'Muramasa': 'Muramasa',
        'katana': 'katana',
        'naginata': 'naginata',
        'kusarigama': 'kusarigama',
        'Winchester Premium': 'Winchester Premium',
        'panzerfaust': 'panzerfaust',
        'mega flam': 'mega fiammata',
        'flam': 'fiammata',
        'boomerang': 'boomerang',
        'shuriken': 'shuriken',
        "Al'ud": "Al'ud",
        'school swimsuit': 'costume da bagno scolastico',
        'Dangerous Swimsuit': 'costume da bagno succinto',
        'snow leopard tail ': 'coda di leopardo delle nevi',
        'fox tail': 'coda di volpe',
        'cat tail': 'coda di gatto',
        'dog tail': 'coda di cane',
        'wolf tail': 'coda di lupo',
        'shiva tail': 'coda di shiva',
        'shark tail': 'coda di squalo',
        'Dal-i-thalion': 'Dal-i-thalion',
        'speed ring': 'anello della velocità',
        'aurora ring': 'anello dell’aurora',
        'armored ring': 'anello corazzato',
        'composite ring': 'anello in lega composita',
        'cyber altar': 'cyber-altare',
        'shipping chest': 'cassa di spedizione',
        'big shipping chest': 'grande cassa di spedizione',
        'storage chest': 'cassa di stoccaggio',
        'offering box': 'cassetta delle offerte',
        'bank': 'salvadanaio',
        'tax chest': 'cassa delle tasse',
        'merchant chest': 'borsa del mercante',
        'trash bin': 'cestino dei rifiuti',
        'scratch machine': 'macchina dei gratta e vinci',
        'fortune drum': 'tamburo della lotteria',
        'casino table': 'tavolo da casinò',
        'card table': 'tavolo da carte',
        'billiard table': 'tavolo da biliardo',
        'darts board': 'bersaglio per freccette',
        'pulpit': 'pulpito',
        'mirror table': 'tavolo con specchio',
        'automatic door': 'porta automatica',
        'foreign door': 'porta esotica',
        'figure': 'animale impagliato',
        'card': 'carta da collezione',
        'big furniture': 'mobile grande',
        'tall furniture': 'mobile alto',
        'huge furniture': 'mobile enorme',
        'furniture': 'mobile',
        'cage': 'gabbia',
        'dagger grave': 'tumulo della spada del vento',
        'Loytel Mart': 'Emporio di Loytel',
        'small wagon': 'piccolo carro',
        'big wagon': 'grande carro',
        'wagon': 'carro',
        'eletric guitar': 'chitarra elettrica',
        'harpsichord': 'clavicembalo',
        "Gould's piano": 'pianoforte di Gould',
        'kill kill piano': 'pianoforte massacratore',
        'panty': 'mutandine',
        'recorder': 'flauto dolce',
        'stradivarius': 'stradivari',
        'ether solvent': 'solvente d’etere',
        'Editor Light(Wall)': 'Luce Speciale (Parete)',
        'pendant light': 'lampadario a sospensione',
        'sun pendant light': 'lampadario sole',
        'hanging candle': 'candela a sospensione',
        'wall lamp': 'lampada da parete',
        'wall foreign lamp': 'lanterna esotica da parete',
        'epithets': 'pergamena degli epiteti',
        'lineage forgery': 'pergamena di falsificazione genealogica',
        'indulgence': 'lettera d’indulgenza',
        'magic': 'pergamena magica',
        'ornamental box': 'scatola ornamentale',
        'crim ale': 'birra di crim',
        'liquid': 'liquido',
        'treasure': 'tesoro',
        'gift box': 'pacco regalo',
        'sword replica': 'replica di spada',
        'axe replica': 'replica di ascia',
        'mace replica': 'replica di mazza',
        'mooring rope': 'gomena d’ormeggio',
        'anchor': 'ancora',
        'scrap': 'rottami di scarto',
        'foreign stall': 'bancarella esotica',
        'doll house': 'casa delle bambole',
        'hourglass': 'clessidra',
        'completely worthless rusted fake gold bar': 'finto lingotto d’oro arrugginito senza valore',
        'decayed Big Daddy': 'Big Daddy decomposto',
        'iron maiden': 'vergine di ferro',
        'guillotine': 'ghigliottina',
        'trolley': 'carrello da miniera',
        'wall shelf': 'mensola a muro',
        "prince's bed": 'letto principesco',
        'pipe bed': 'letto a castello',
        'poor bed': 'letto rozzo',
        'makeshift bed': 'letto di fortuna',
        'gravestone': 'lapide tombale',
        'TV': 'televisore',
        'tapestry': 'arazzo',
        'stall': 'bancarella',
        'changing room': 'spogliatoio',
        'shed': 'capanno',
        'counter': 'bancone',
        'corner counter': 'bancone angolare',
        'iron scale': 'bilancia di ferro',
        'cup': 'coppa',
        'old globe': 'antico mappamondo',
        'modern art': 'scultura d’arte moderna',
        'bucket': 'secchio',
        'exotic teapot': 'teiera esotica',
        'dish': 'piatto',
        'tea pot': 'teiera',
        'toaster': 'tostapane',
        'research equipment': 'apparecchiatura di ricerca',
        'binocular': 'binocolo',
        'alarm clock': 'sveglia',
        'evening drink set': 'set da aperitivo',
        'beach ball': 'pallone da spiaggia',
        'rubber putit': 'putit di gomma',
        'door bell': 'campanello per porta',
        'pan': 'padella',
        'rope': 'corda',
        'valve': 'valvola',
        'cooking tool': 'utensile da cucina',
        'lava curtain': 'cortina di lava',
        'lava bubble': 'bolla di lava',
        'lava pillar': 'colonna di lava',
        'Memorial Block No.1': 'Blocco Commemorativo n. 1',
        'Memorial Block No.2': 'Blocco Commemorativo n. 2',
        'Memorial Block No.3': 'Blocco Commemorativo n. 3',
        'Memorial Block No.4': 'Blocco Commemorativo n. 4',
        'cake dough': 'impasto per torte',
        'crim powder': 'polvere di crim',
        'matcha powder': 'polvere di matcha',
        'blue powder': 'polvere blu',
        'red powder': 'polvere rossa',
        'purple powder': 'polvere viola',
        'green powder': 'polvere verde',
        'bone powder': 'farina d’ossa',
        'mini salad': 'insalatina',
        'stir fried vegetable': 'verdure saltate',
        'soggy vegetable': 'verdure mollicce',
        'roasted fruit': 'frutta arrostita',
        'assorted fruit': 'macedonia di frutta',
        'jelly': 'gelatina',
        'crepe': 'crêpe',
        'sherbet': 'sorbetto'
    }

    # Noun vocabulary mapping for compounding
    noun_map = {
        'sword': 'spada',
        'great sword': 'spadone',
        'short sword': 'spada corta',
        'long sword': 'spada lunga',
        'broadsword': 'spada a lama larga',
        'claymore': 'claymore',
        'dagger': 'pugnale',
        'knife': 'coltello',
        'axe': 'ascia',
        'battle axe': 'ascia da battaglia',
        'great axe': 'grande ascia',
        'hammer': 'martello',
        'war hammer': 'martello da guerra',
        'mace': 'mazza',
        'club': 'clava',
        'spear': 'lancia',
        'lance': 'lancia da giostra',
        'halberd': 'alabarda',
        'scythe': 'falce',
        'bow': 'arco',
        'long bow': 'arco lungo',
        'short bow': 'arco corto',
        'crossbow': 'balestra',
        'gun': 'fucile',
        'pistol': 'pistola',
        'rifle': 'fucile a canna lunga',
        'shotgun': 'fucile a pompa',
        'staff': 'bastone',
        'cane': 'bastone da passeggio',
        'rod': 'verga',
        'wand': 'bacchetta',
        'shield': 'scudo',
        'large shield': 'grande scudo',
        'round shield': 'scudo rotondo',
        'kite shield': 'scudo a goccia',
        'tower shield': 'scudo a torre',
        'buckler': 'brocchiero',
        'helm': 'elmo',
        'helmet': 'elmo',
        'hat': 'cappello',
        'cap': 'berretto',
        'crown': 'corona',
        'circlet': 'diadema',
        'armor': 'armatura',
        'mail': 'cotta di maglia',
        'plate': 'corazza di piastre',
        'robe': 'veste',
        'coat': 'cappotto',
        'cloak': 'mantello',
        'boots': 'stivali',
        'shoes': 'scarpe',
        'gloves': 'guanti',
        'gauntlets': 'guanti d’arme',
        'belt': 'cintura',
        'girdle': 'cinturone',
        'ring': 'anello',
        'necklace': 'collana',
        'amulet': 'amuleto',
        'bed': 'letto',
        'table': 'tavolo',
        'chair': 'sedia',
        'bench': 'panca',
        'sofa': 'divano',
        'chest': 'baule',
        'box': 'scatola',
        'cabinet': 'armadietto',
        'shelf': 'scaffale',
        'bookshelf': 'libreria',
        'desk': 'scrivania',
        'door': 'porta',
        'window': 'finestra',
        'fence': 'staccionata',
        'wall': 'muro',
        'pillar': 'pilastro',
        'lamp': 'lampada',
        'lantern': 'lanterna',
        'candle': 'candela',
        'torch': 'torcia',
        'statue': 'statua',
        'monument': 'monumento',
        'fountain': 'fontana',
        'pot': 'vaso',
        'vase': 'vaso da fiori',
        'barrel': 'botte',
        'crate': 'cassa di legno',
        'altar': 'altare',
        'seed': 'seme',
        'potion': 'pozione',
        'scroll': 'pergamena',
        'spellbook': 'grimorio',
        'book': 'libro'
    }

    adj_map = {
        'wooden': 'di legno',
        'stone': 'di pietra',
        'iron': 'di ferro',
        'steel': 'd’acciaio',
        'golden': 'dorato',
        'silver': 'd’argento',
        'bronze': 'di bronzo',
        'copper': 'di rame',
        'glass': 'di vetro',
        'crystal': 'di cristallo',
        'bone': 'd’osso',
        'leather': 'di cuoio',
        'cloth': 'di stoffa',
        'silk': 'di seta',
        'ancient': 'antico',
        'old': 'vecchio',
        'rusty': 'arrugginito',
        'fine': 'pregiato',
        'noble': 'nobile',
        'royal': 'reale',
        'sacred': 'sacro',
        'holy': 'sacro',
        'cursed': 'maledetto',
        'blessed': 'benedetto',
        'magic': 'magico',
        'magical': 'magico',
        'small': 'piccolo',
        'big': 'grande',
        'huge': 'enorme',
        'tall': 'alto',
        'round': 'rotondo',
        'square': 'quadrato',
        'simple': 'semplice',
        'luxurious': 'lussuoso',
        'fancy': 'elegante',
        'crude': 'grezzo',
        'heavy': 'pesante',
        'light': 'leggero'
    }

    trans = {}

    for en, info in unique_names.items():
        k = en.strip()
        if k in exact_map:
            trans[en] = exact_map[k]
            continue
            
        # Check compound patterns
        # 1. "seed of X"
        if k.startswith('seed of ') or k.startswith('seed '):
            target = k.replace('seed of ', '').replace('seed ', '').strip()
            trans[en] = f'seme di {target}'
            continue
            
        # 2. "statue of X"
        if k.startswith('statue of '):
            target = k.replace('statue of ', '').strip()
            trans[en] = f'statua di {target}'
            continue

        # 3. "X tail"
        if k.endswith(' tail') or k.endswith(' tail '):
            target = k.replace(' tail', '').replace(' tail ', '').strip()
            trans[en] = f'coda di {target}'
            continue

        # 4. "[adj] [noun]"
        parts = k.split()
        if len(parts) == 2:
            a, n = parts[0].lower(), parts[1].lower()
            if a in adj_map and n in noun_map:
                trans[en] = f'{noun_map[n]} {adj_map[a]}'
                continue
            if n in noun_map:
                trans[en] = f'{noun_map[n]} ({a})'
                continue

        # Single nouns
        if k.lower() in noun_map:
            trans[en] = noun_map[k.lower()]
            continue

        # Fallback to English name if proper noun / untranslated
        trans[en] = en

    json.dump(trans, open('scratch/thing_name_map.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'Generated {len(trans)} name translations.')

if __name__ == '__main__':
    generate_translations()
