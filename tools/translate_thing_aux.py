import openpyxl, json

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/Thing.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    room_map = {
        'Storeroom,Stockroom,Depot,Storage': 'Magazzino,Deposito,Stanza di Stoccaggio,Dispensa',
        'Hoard': 'Camera del Tesoro',
        'Bedroom': 'Camera da Letto',
        'Storeroom,Celler': 'Magazzino,Cantina',
        'Kitchen,Dining Room': 'Cucina,Sala da Pranzo',
        'Toilet,Bathroom': 'Bagno,Servizi',
        'Bathroom,Washroom': 'Stanza da Bagno,Lavatoio',
        'Cemetery,Graveyard': 'Cimitero,Sepolcro',
        'Butchery,Bloodbath,Slaughterroom': 'Macelleria,Camera di Macellazione,Mattatoio',
        'Portal Room': 'Stanza del Portale',
        'Lounge,Rest Room': 'Salotto,Area Relax',
        'Torture Room': 'Camera di Tortura'
    }

    unit_map = {
        'set': 'completo',
        'poster': 'manifesto'
    }

    unknown_map = {
        'dagger surrounded by wind': 'pugnale avvolto dal vento',
        'thin dagger': 'pugnale sottile',
        'hexed short sword': 'spada corta maledetta',
        'silver-crafted dagger': 'pugnale cesellato d’argento',
        'sharp kitchen knife': 'coltello da cucina affilato',
        'cocky wakizashi': 'wakizashi insolente',
        'sword that ends all': 'spada che pone fine a tutto',
        'white fine sword': 'spada dalla candida lama',
        'stick engraved with runes': 'bastone inciso di rune',
        'polished sword': 'katana lucente',
        'bewitched sword': 'spada stregata',
        'old sword': 'vecchia spada',
        'two-edged great sword': 'spadone a due tagli',
        'steam emitting claymore': 'claymore che sbuffa vapore',
        'giant hammer': 'martello colossale',
        'wind-worn hammer': 'martello eroso dal vento',
        'holy lance': 'lancia sacra',
        'roaring lance': 'lancia ruggente',
        'harvest scythe': 'falce del raccolto',
        'elemental staff': 'bastone elementale',
        'ivory staff': 'bastone d’avorio',
        'shivering staff': 'bastone tremante',
        'cold glinting blade': 'lama dal gelido bagliore',
        'shaking bow': 'arco vibrante',
        'bow surrounded by wind': 'arco lungo avvolto dal vento',
        'ancient shotgun': 'antico fucile a pompa',
        'tough lute': 'liuto robusto',
        'shining helm': 'elmo scintillante',
        'unusual helm': 'elmo insolito',
        'floating ring': 'anello fluttuante',
        'transparent wrap': 'velo trasparente',
        'cheerful shoes': 'scarpe allegre',
        'light shoes': 'scarpe leggere',
        'glowing blue necklace': 'collana dal bagliore azzurro',
        'strangely shaped badge': 'distintivo dalla forma bizzarra',
        'lonely piano': 'pianoforte solitario',
        'heavy piano': 'pianoforte pesante',
        'elegant string': 'elegante strumento a corda',
        'master hammer': 'martello del maestro fabbro',
        'lunch box': 'cestino del pranzo',
        'soup': 'zuppa'
    }

    name2_map = {
        'dattamono': 'ciò che un tempo era #1',
        'fish_slice': 'trancio di #1',
        'cheese': 'formaggio di #1',
        '735': 'pizza da asporto con #1b',
        'marshmallow_yaki': 'marshmallow tostato',
        'jerky': 'carne secca di #1',
        '110': '#1 con l’osso',
        '100': 'arrosto di #1',
        '511': '#1 intero arrostito',
        '106': 'crocchetta di #1',
        '678': '#1 alla griglia con foglie di shiso',
        '510': 'saltato piccante di #1',
        'bloodpack': 'sacca di sangue di #1',
        'bloodsample': 'sangue di #1',
        'lunch_dystopia': 'pasto distopico di #1',
        'lunch_love': 'pranzo al sacco preparato con amore da #1',
        '109': '#1 allo spiedo',
        '102': '#1 saltato',
        '683': 'tempura di #1',
        '684': 'sashimi di #1',
        '685': 'sashimi freschissimo di #1',
        '686': '#1 fritto',
        '737': 'banchetto festivo di #1',
        '1135': 'sushi di #1',
        'yakiimo': 'patata dolce cotta su pietra',
        '512': 'insalata di #1',
        '101': '#1 marinato',
        '108': 'stufato di #1',
        '107': 'caesar salad con #1',
        '663': 'piccola insalata di #1',
        '664': '#1 saltato in padella',
        '103': '#1 arrostito',
        '509': 'assortimento di #1',
        '680': 'gelatina di #1',
        '682': 'crêpe di #1',
        '711': 'sorbetto di #1',
        '712': 'parfait reale di #1',
        '514': 'torta paradiso con #1',
        '515': 'tiramisù con #1',
        '516': 'torta al caramello e #1',
        '105': 'mousse di #1',
        '661': 'torta gigante con #1',
        'cake_festival': 'torta deluxe del putit delle nevi con #1',
        '666': 'pane di #1',
        '660': 'pancarré di #1',
        'anpan': 'anpan di #1',
        '665': 'grissino di #1',
        '671': 'pane soffice di #1',
        '679': 'bignè di #1',
        '681': 'crostata di #1b',
        'pie_meat': 'pasticcio di carne di #1b',
        'pie_fish': 'pasticcio di pesce di #1b',
        '734': 'pizza con #1b',
        'burger': 'hamburger di #1b',
        '695': 'biscotto di #1',
        'taiyaki': 'taiyaki di #1',
        '710': 'manju di #1',
        'bun': 'paninetto al vapore di #1',
        'dorayaki': 'dorayaki di #1',
        'mancookie': 'omino di pan di zenzero con #1b',
        'oyaki': 'mochocho al forno con #1',
        'kamiyaki': '#1g arrostito su pietra',
        '513': 'ramen istantaneo di #1',
        '687': 'udon tsukimi di #1',
        '689': 'spaghetti al ragù di #1',
        '691': 'spaghetti aglio e olio con #1',
        '707': 'carbonara con #1',
        '708': 'pasta fredda con #1',
        '709': 'ramen di #1',
        'yudetamago': '#1b sodo',
        'onsentamago': '#1b termale',
        '104': '#1 all’occhio di bue',
        '662': 'frittata di #1b',
        '517': 'budino di #1b',
        '736': 'menu per bambini con #1b',
        '692': 'riso con #1',
        '693': 'curry con #1',
        '694': 'scodella di riso con #1',
        'bibimbap': 'bibimbap su pietra con #1',
        '702': 'onigiri con #1',
        'zassouni': 'stufato di erbacce',
        '703': 'cazuela di #1',
        '704': 'vellutata di #1',
        '705': 'sukiyaki di #1',
        '706': 'stufato di #1',
        'cream_stew': 'stufato cremoso di #1',
        'dish_soup': 'zuppa di #1'
    }

    count = 0
    for r in range(2, ws.max_row+1):
        tid = str(ws.cell(row=r, column=headers['id']).value)
        
        # roomName
        if 'roomName' in headers:
            ev = ws.cell(row=r, column=headers['roomName_EN']).value
            if ev and str(ev).strip() in room_map:
                ws.cell(row=r, column=headers['roomName']).value = room_map[str(ev).strip()]
                count += 1
                
        # unit
        if 'unit' in headers:
            ev = ws.cell(row=r, column=headers['unit_EN']).value
            if ev and str(ev).strip() in unit_map:
                ws.cell(row=r, column=headers['unit']).value = unit_map[str(ev).strip()]
                count += 1
                
        # unknown
        if 'unknown' in headers:
            ev = ws.cell(row=r, column=headers['unknown_EN']).value
            if ev and str(ev).strip() in unknown_map:
                ws.cell(row=r, column=headers['unknown']).value = unknown_map[str(ev).strip()]
                count += 1
                
        # name2
        if 'name2' in headers:
            ev = ws.cell(row=r, column=headers['name2_EN']).value
            if ev and tid in name2_map:
                ws.cell(row=r, column=headers['name2']).value = name2_map[tid]
                count += 1

    wb.save('Lang/IT/Game/Thing.xlsx')
    print(f'Applied {count} auxiliary translations to Thing.xlsx')

if __name__ == '__main__':
    run()
