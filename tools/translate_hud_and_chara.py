import openpyxl

# 1. Update General.xlsx
print("Updating General.xlsx...")
gen_p = 'd:/Mod/Elin/Lang/IT/Game/General.xlsx'
wb_gen = openpyxl.load_workbook(gen_p)
ws_gen = wb_gen.active
h_gen = [str(c.value) for c in ws_gen[1]]
id_c = h_gen.index('id') + 1
txt_c = h_gen.index('text') + 1

gen_fixes = {
    'client': 'Committente',
    'reward': 'Ricompensa',
    'qReward': '#1 oren',
    'qRewardDefense': '#1 oren + Bonus Ondata',
    'qRewardSupply': '#1 oren + Bonus Qualità',
    'qRewardSupplyCost': '#1 oren + Bonus Qualità + Rimborso Oggetto',
    'qRewardHunt': '#1 oren',
    'qRewardMusic': '#1 oren',
    'qRewardHarvest': '#1 oren',
    'days1': 'giorni rimasti ',
    'days2': ' giorni rimasti',
    'daysLeft': '#1 g',
    'reroll': 'Rinnova',
    'rerollQuest': 'Rinnova Missioni\n(-#1 Influenza)',
    'rerollShop': 'Rinnova Negozio\n(-#1 Influenza)',
    'tReroll': 'Rinnova',
    'progressHuntRace': 'Caccia "#3": #1 di #2',
    'progressDebt': 'Debito: #1 rimanenti',
    'faction_contribution': 'Contributo: #1 / #2',
    'progressHunt': 'Caccia creature ostili: #1 di #2',
    'progressVernis': 'Enormi rocce rimanenti: #1',
    'progressEscort': 'Scorta #1\nA: #2',
    'progressDeliver': 'Consegna #1\n#3\nA: #2',
    'progressFlyer': 'Distribuzione Volantini: #1 di #2',
    'progressKarma': 'Accumula Karma: #1 di #2',
    'progressRecruit': 'Recluta Residenti: #1 di #2',
    'progressShowSupply': 'Mostra #1',
    'progressSupply': 'Consegna #1\n#2',
    'progressDefenseGame': 'Sopravvivi',
    'progressHarvest': 'Consegna Raccolto: #1 di #2',
    'progressMusic': 'Punteggio Musicale: #1 di #2',
    'progressWedding': 'Festeggiamo questo giorno fausto!',
    'rank_contribution': 'Classifica Contributi',
    'foundTreasure': 'Tesori Trovati: #1',
    'supplyInInv': '(Posseduto) ',
    'supplyNotInInv': '(Non posseduto) ',
    'target_huntRace': 'Bersagli Possibili:',
    'weatherCloudy': 'Nuvoloso',
    'weatherEther': 'Vento dell\'Etere',
    'weatherFine': 'Sereno',
    'weatherBlossom': 'Petali al Vento',
    'weatherRain': 'Pioggia',
    'weatherRainHeavy': 'Nubifragio',
    'weatherSnow': 'Neve',
    'weatherSnowHeavy': 'Tormenta di Neve'
}

count_gen = 0
for r in range(2, ws_gen.max_row + 1):
    rid = str(ws_gen.cell(row=r, column=id_c).value or '').strip()
    if rid in gen_fixes:
        ws_gen.cell(row=r, column=txt_c, value=gen_fixes[rid])
        count_gen += 1
wb_gen.save(gen_p)
print(f"General.xlsx updated with {count_gen} strings.")

# 2. Update Chara.xlsx (akas and common creatures)
print("Updating Chara.xlsx...")
chara_p = 'd:/Mod/Elin/Lang/IT/Game/Chara.xlsx'
wb_ch = openpyxl.load_workbook(chara_p)
ws_ch = wb_ch.active
h_ch = [str(c.value) for c in ws_ch[1]]
name_c = h_ch.index('name') + 1
name_en_c = h_ch.index('name_EN') + 1
aka_c = h_ch.index('aka') + 1
aka_en_c = h_ch.index('aka_EN') + 1

aka_it = {
    'trainer': 'addestratore',
    'goods shopkeeper': 'mercante di merci',
    'general shopkeeper': 'droghiere',
    'book shopkeeper': 'libraio',
    'junk shopkeeper': 'rigattiere',
    'furniture shopkeeper': 'mercante di mobili',
    'fruit shopkeeper': 'fruttivendolo',
    'magic shopkeeper': 'mercante arcano',
    'blackmarket shopkeeper': 'ricettatore del mercato nero',
    'guard': 'guardia',
    'security guard': 'guardia di sicurezza',
    'innkeeper': 'locandiere',
    'bartender': 'barista',
    'blacksmith': 'fabbro',
    'legendary smith': 'fabbro leggendario',
    'gunsmith': 'armaiolo',
    'baker': 'fornaio',
    'butcher': 'macellaio',
    'patissier': 'pasticciere',
    'fishmonger': 'pescivendolo',
    'healer': 'guaritore',
    'mayor': 'sindaco',
    'acting mayor': 'sindaco facente funzioni',
    'adventurer': 'avventuriero',
    'little adventurer': 'giovane avventuriero',
    'beggar': 'mendicante',
    'citizen': 'cittadino',
    'child': 'bambino',
    'little girl': 'bambina',
    'innocent girl': 'fanciulla innocente',
    'farmer': 'contadino',
    'fisher': 'pescatore',
    'miner': 'minatore',
    'sailor': 'marinaio',
    'captain': 'capitano',
    'priest': 'sacerdote',
    'nun': 'suora',
    'noble': 'nobile',
    'maid': 'cameriera',
    'fox maid': 'cameriera volpe',
    'wandering alchemist': 'alchimista girovago',
    'wandering merchant': 'mercante girovago',
    'frontier inspector': 'ispettore della frontiera',
    'casino clerk': 'impiegato del casinò',
    'arena master': 'maestro dell\'arena',
    'caravan master': 'capocarovana',
    'slave master': 'schiavista',
    'Fighters guild clerk': 'impiegato della Gilda dei Guerrieri',
    'Mages guild clerk': 'impiegato della Gilda dei Maghi',
    'Merchants guild clerk': 'impiegato della Gilda dei Mercanti',
    'watchman of the Fighters Guild': 'guardiano della Gilda dei Guerrieri',
    'watchman of the Mages Guild': 'guardiano della Gilda dei Maghi',
    'maiden of the Night': 'fanciulla della Notte',
    'younger sister': 'sorellina',
    'younger cat sister': 'sorellina gatto',
    'younger penguin sister': 'sorellina pinguino',
    'younger shark sister': 'sorellina squalo',
    'young lady': 'giovane dama',
    'artist': 'artista',
    'bard': 'bardo',
    'dancer': 'danzatrice',
    'gambler': 'giocatore d\'azzardo',
    'banker': 'banchiere',
    'informer': 'informatore',
    'hitman': 'sicario',
    'thief': 'ladro',
    'rogue': 'fuorilegge',
    'fighter': 'combattente',
    'defender': 'difensore',
    'mage': 'mago',
    'apprentice mage': 'apprendista mago',
    'apprentice thief': 'apprendista ladro',
    'apprentice trader': 'apprendista commerciante',
    'silver cat': 'gatto argentato',
    'black cat': 'gatto nero',
    'little dog': 'cagnolino',
    'flower girl': 'fioraia',
    'talesinger of Olvina': 'cantrice di Olvina',
    'king of Palmia': 'Re di Palmia',
    'prince of Palmia': 'Principe di Palmia',
    'duke of Mysilia': 'Duca di Mysilia',
    'prince of Mysilia': 'Principe di Mysilia',
    'Goddess of Luck': 'Dea della Fortuna',
    'Goddess of Healing': 'Dea della Guarigione',
    'Goddess of Wind': 'Dea del Vento',
    'Goddess of Harmony': 'Dea dell\'Armonia',
    'Goddess of Moonshadow': 'Dea dell\'Ombra Lunare',
    'God of Earth': 'Dio della Terra',
    'God of Element': 'Dio degli Elementi',
    'God of Harvest': 'Dio del Raccolto',
    'God of Machine': 'Dio delle Macchine',
    'God of Infidel': 'Dio degli Infedeli'
}

creature_names_it = {
    'snow putit': 'putit delle nevi',
    'forest putit': 'putit della foresta',
    'putit': 'putit',
    'beth putit': 'putit rosso',
    'water putit': 'putit d\'acqua',
    'metal putit': 'putit metallico',
    'stray cat': 'gatto randagio',
    'cat': 'gatto',
    'big cat': 'gatto gigante',
    'dog': 'cane',
    'hunting dog': 'segugio da caccia',
    'shiba dog': 'cane shiba',
    'mine dog': 'cane della miniera',
    'caterpillar': 'bruco',
    'alien dog': 'cane alieno'
}

count_aka = 0
count_name = 0
for r in range(2, ws_ch.max_row + 1):
    a_en = str(ws_ch.cell(row=r, column=aka_en_c).value or '').strip()
    if a_en in aka_it:
        ws_ch.cell(row=r, column=aka_c, value=aka_it[a_en])
        count_aka += 1
    
    n_en = str(ws_ch.cell(row=r, column=name_en_c).value or '').strip()
    if n_en in creature_names_it:
        ws_ch.cell(row=r, column=name_c, value=creature_names_it[n_en])
        count_name += 1

wb_ch.save(chara_p)
print(f"Chara.xlsx updated: {count_aka} akas/titles, {count_name} creature names.")

# 3. Update Thing.xlsx (meat on the bone, cone, and common foods/junk)
print("Updating Thing.xlsx...")
thing_p = 'd:/Mod/Elin/Lang/IT/Game/Thing.xlsx'
wb_th = openpyxl.load_workbook(thing_p)
ws_th = wb_th.active
h_th = [str(c.value) for c in ws_th[1]]
name_c = h_th.index('name') + 1

item_fixes = {
    '110': 'carne con osso',
    '525': 'pigna',
    '1101': 'pigna',
    'meat_bone': 'carne con osso',
    'cone': 'pigna',
    'apple': 'mela',
    'bread': 'pane fragrante',
    'ration': 'razione da viaggio',
    'egg': 'uovo fresco',
    'raw_meat': 'carne cruda',
    'raw_fish': 'pesce crudo',
    'roasted_meat': 'arrosto',
    'steamed_meat': 'carne al vapore',
    'fried_meat': 'frittura di carne',
    'soup_meat': 'zuppa di carne',
    'jerky': 'carne essiccata',
    'stew': 'stufato sostanzioso',
    'salad': 'insalata mista',
    'cake': 'torta deliziosa',
    'cookie': 'biscotto croccante',
    'candy': 'caramella dolce',
    'pasta': 'piatto di pasta',
    'ramen': 'ciotola di ramen',
    'cheese': 'formaggio stagionato',
    'milk': 'latte fresco',
    'beer': 'birra schiumosa',
    'wine': 'vino pregiato',
    'whiskey': 'whisky forte',
    'juice': 'succo di frutta',
    'coffee': 'caffè bollente',
    'tea': 'tè aromatico'
}

count_th = 0
for r in range(2, ws_th.max_row + 1):
    rid = str(ws_th.cell(row=r, column=1).value or '').strip()
    if rid in item_fixes:
        ws_th.cell(row=r, column=name_c, value=item_fixes[rid])
        count_th += 1

wb_th.save(thing_p)
print(f"Thing.xlsx updated with {count_th} items.")

# 4. Update CharaText.xlsx & god_talk.xlsx
print("Updating CharaText.xlsx & god_talk.xlsx...")
ct_p = 'd:/Mod/Elin/Lang/IT/Game/CharaText.xlsx'
wb_ct = openpyxl.load_workbook(ct_p)
ws_ct = wb_ct.active
h_ct = [str(c.value) for c in ws_ct[1]]
fov_c = h_ct.index('fov') + 1

for r in range(2, ws_ct.max_row + 1):
    rid = str(ws_ct.cell(row=r, column=1).value or '').strip()
    if rid == 'merchant':
        ws_ct.cell(row=r, column=fov_c, value='"Benvenuto nel mio negozio!"\n"Dai un\'occhiata alla mia merce!"\n"Piacere di averti qui."\n#self ti guarda e annuisce.\n#self ti fa un cenno con la mano.')
    elif rid == 'banker':
        ws_ct.cell(row=r, column=fov_c, value='"Benvenuto."\n"Non è saggio portarsi dietro tutto questo denaro."\n"È tutta una questione di fiducia."')
wb_ct.save(ct_p)

gt_p = 'd:/Mod/Elin/Lang/IT/Data/god_talk.xlsx'
wb_gt = openpyxl.load_workbook(gt_p)
ws_gt = wb_gt.active
h_gt = [str(c.value) for c in ws_gt[1]]
luck_c = h_gt.index('luck') + 1

for r in range(2, ws_gt.max_row + 1):
    rid = str(ws_gt.cell(row=r, column=1).value or '').strip()
    if rid == 'welcome':
        ws_gt.cell(row=r, column=luck_c, value='Ueee♪ Sei tornat#o? Sei tornat#o!')
wb_gt.save(gt_p)

print("All updates applied successfully!")
