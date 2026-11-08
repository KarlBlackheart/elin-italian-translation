import openpyxl, json

def build_extended_name_map():
    # Dictionary of translations for the remaining 886 unique items
    M = {
        # Licenses, tickets, coins
        'strange copper coin': 'moneta di rame esotica',
        'ecopo': 'ecopo',
        'skyfarer ticket': 'biglietto del viaggiatore celeste',
        'Lucky Coin': 'Moneta della Fortuna',
        'Illumination Engineer License': 'Licenza di Tecnico delle Luci',
        'Void Exploration License': 'Licenza di Esplorazione del Vuoto',
        'Advanced Adventurer License': 'Licenza di Avventuriero Veterano',
        'furniture ticket': 'buono mobilio',
        'ticket to the show': 'biglietto per lo spettacolo',
        
        # Tools, dummies, outdoor
        "witch's broom": 'scopa della strega',
        'pitchfork': 'forcone',
        'telescope': 'telescopio',
        'training dummy': 'fantoccio da addestramento',
        'armored training dummy': 'fantoccio corazzato da addestramento',
        'sand bag': 'sacco da pugilato',
        'snowman': 'pupazzo di neve',
        'signpost': 'cartello segnaletico',
        'torch stand': 'braciere su piedistallo',
        'fire pit': 'focolare da campo',
        'bonfire': 'falò',
        'street lamp': 'lampione',
        
        # Furniture, decor, fossiles
        'cat music box': 'carillon del gatto',
        'pool of stagnation': 'pozza stagnante',
        'floor mat': 'stuoia da pavimento',
        'polar bear rug': 'tappeto d’orso polare',
        'grand round table': 'grande tavola rotonda',
        'stage platform': 'pedana da palcoscenico',
        'dinosaur fossil': 'fossile di dinosauro',
        'water drain': 'grata di scarico',
        'wooden horse': 'cavallo di legno',
        'cross': 'croce di contenzione',
        'shackle': 'ceppi di prigionia',
        'iron ball': 'palla di ferro al piede',
        'generator': 'generatore',
        'speaker': 'altoparlante',
        'hamster wheel': 'ruota da criceto',
        'mail post': 'cassetta delle lettere',
        'gramophone': 'grammofono',
        'firework': 'fuoco d’artificio',
        'firework launcher': 'lanciatore di fuochi d’artificio',
        "butcher's tool": 'mannaia da macellaio',
        'bone carving tool': 'attrezzi per intaglio osseo',
        
        # Runes, stones, biology
        'rune': 'runa',
        'lawless rune': 'runa della trasgressione',
        'rune mold': 'matrice runica',
        'Destiny Stone': 'Pietra del Destino',
        'heart': 'cuore',
        'gene': 'gene',
        'brain cell': 'cellula cerebrale',
        'magic stone': 'pietra magica',
        'floor': 'pavimento',
        'floor decoration': 'decorazione da pavimento',
        'platform': 'fondamenta',
        'trap': 'trappola',
        'nuclear bomb "Cat\'s Cradle"': 'bomba atomica «Cat’s Cradle»',
        'mine': 'mina terrestre',
        'object': 'oggetto d’arredo',
        'food recipe': 'ricetta culinaria',
        'commodities': 'mucchio di merci',
        'decorative goddess': 'statua decorativa della dea',
        'weathercock pedestal': 'piedistallo della banderuola',
        'weathercock': 'banderuola segnavento',
        'weathercock pedestal arrow': 'freccia per banderuola',
        'weapon rack': 'rastrelliera per armi',
        'sturdy treasure chest': 'robusto forziere del tesoro',
        'rudder': 'timone navale',
        'vent': 'condotto di ventilazione',
        'sailing': 'albero maestro',
        'oar': 'remo',
        'Opatos bearing the earth': 'Statua di Opatos che regge la Terra',
        'ancient tomb': 'tomba antica',
        'huge tree stump': 'ceppo d’albero colossale',
        'knight': 'statua di cavaliere',
        'pendulum clock': 'orologio a pendolo',
        
        # Paintings
        '"The Younger Sister"': 'Quadro «La Sorella Minore»',
        '"Bewitching Larnneire"': 'Quadro «Larnneire Seduttrice»',
        '"Bewitching Rianna"': 'Quadro «Rianna Seducente»',
        '"The Lady"': 'Quadro «La Dama»',
        '"In the forest"': 'Quadro «Nel Bosco»',
        '"Lady In the Mirror"': 'Quadro «La Dama allo Specchio»',
        '"Strange Shadow"': 'Quadro «L’Ombra Misteriosa»',
        '"Palmia Times"': '«Il Corriere di Palmia»',
        'photo': 'fotografia',
        
        # Everyday items, kitchenware
        'bowl': 'ciotola',
        'dirty dish': 'piatto sporco',
        'broom': 'scopa',
        'sack': 'sacco di tela',
        'leaf dish': 'piatto di foglia',
        'wooden figure': 'statuetta di legno',
        'stone figure': 'statuetta di pietra',
        'spirit horse': 'cavallo degli spiriti',
        'flotsam from the north': 'relitto dal nord',
        'animal bone': 'ossa animali',
        'hungry sea lion bone': 'ossa di leone marino ghiottone',
        'empty bottle': 'bottiglia vuota',
        'dead fish': 'pesce morto',
        'float': 'ciambella salvagente',
        'stone circle': 'cerchio di pietre',
        'specimen': 'campione biologico',
        
        # Meat, crops, giant fruits
        'giant mousse': 'mousse gigante',
        'decamelon': 'decamelone',
        'giant kiwi': 'kiwi gigante',
        'giant peach': 'pesca gigante',
        'corpse': 'cadavere',
        'marbled meat': 'carne marezzata',
        'what once was life': 'resti di ciò che fu vivo',
        'fertilized egg': 'uovo fecondato',
        
        # Fish species
        'bonito': 'tonnetto',
        'tuna': 'tonno',
        'blowfish': 'pesce palla',
        'flatfish': 'pesce piatto',
        'sardine': 'sardina',
        'sea bream': 'orata',
        'salmon': 'salmone',
        'sand borer': 'triglia della sabbia',
        'mackerel': 'sgombro',
        'squid': 'calamaro',
        'octopus': 'polpo',
        'eel': 'anguilla',
        'shrimp': 'gambero',
        'lobster': 'astice',
        'crab': 'granchio',
        
        # Bakery, sweets, creams
        'whipped cream': 'panna montata',
        'chocolate cream': 'crema al cioccolato',
        'anko': 'crema anko',
        'custard cream': 'crema pasticcera',
        'matcha cream': 'crema al matcha',
        'fresh marshmallow': 'marshmallow fresco',
        'roasted marshmallow': 'marshmallow tostato',
        'candied apple': 'mela caramellata',
        'soft and fluffy bread': 'pane soffice',
        'cream puff': 'bignè alla crema',
        'pie': 'crostata',
        'meat pie': 'pasticcio di carne',
        'star gazy pie': 'stargazy pie',
        'burger': 'hamburger',
        'burnt bread': 'pane bruciato',
        'taiyaki': 'taiyaki',
        'waffle': 'waffle',
        'pancake': 'pancake',
        
        # General / Miscellaneous
        'letter_will': 'testamento',
        'will': 'testamento',
        'letter to chief editor': 'lettera al caporedattore',
        'bill': 'fattura',
        'tax bill': 'cartella esattoriale',
        'debt bill': 'ingiunzione per debiti',
        'scratch card': 'biglietto gratta e vinci',
        'old ticket': 'vecchio biglietto',
        'prize ball': 'sfera del premio',
        'treasure map': 'mappa del tesoro',
        'map': 'mappa',
        'plan': 'piano di sviluppo',
        'shared diary': 'diario condiviso',
        'old sketch': 'vecchio schizzo'
    }
    return M

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/Thing.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    M = build_extended_name_map()
    count = 0

    for r in range(2, ws.max_row+1):
        ev = ws.cell(row=r, column=headers['name_EN']).value
        tv = ws.cell(row=r, column=headers['name']).value
        if ev:
            k = str(ev).strip()
            if k in M:
                ws.cell(row=r, column=headers['name']).value = M[k]
                count += 1
            elif str(ev) in M:
                ws.cell(row=r, column=headers['name']).value = M[str(ev)]
                count += 1

    wb.save('Lang/IT/Game/Thing.xlsx')
    print(f'Applied {count} additional name translations to Thing.xlsx')

if __name__ == '__main__':
    run()
