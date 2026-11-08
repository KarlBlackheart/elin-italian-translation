import openpyxl

race_names_it = {
    'yerles': 'Yerles',
    'eulderna': 'Eulderna',
    'fairy': 'Fata',
    'dwarf': 'Nano delle Colline',
    'juere': 'Juere',
    'elea': 'Elea',
    'mutant': 'Mutante Caotico',
    'snail': 'Lumaca',
    'lich': 'Lich',
    'wraith': 'Spettro',
    'golem': 'Golem',
    'mifu': 'Mifu',
    'nefu': 'Nefu',
    'succubus': 'Succube',
    'vampire': 'Vampiro',
    'demigod': 'Semidio',
    'centaur': 'Centauro',
    'shiba': 'Shiba',
    'eldercrab': 'Granchio Antico',
    'ratkin': 'Rattoide',
    'werewolf': 'Licantropo',
    'goblin': 'Goblin',
    'kobolt': 'Coboldo',
    'orc': 'Orco',
    'troll': 'Troll',
    'lizardman': 'Uomo Lucertola',
    'minotaur': 'Minotauro',
    'norland': 'Norland',
    'asura': 'Asura',
    'slime': 'Melma',
    'wolf': 'Lupo',
    'zombie': 'Zombi',
    'rabbit': 'Coniglio',
    'rabbitkin': 'Ravian',
    'sheep': 'Pecora',
    'frog': 'Rana',
    'centipede': 'Millepiedi',
    'mandrake': 'Mandragora',
    'beetle': 'Scarabeo',
    'mushroom': 'Fungo',
    'bat': 'Pipistrello',
    'ent': 'Ent',
    'hound': 'Segugio',
    'ghost': 'Fantasma',
    'spirit': 'Spirito',
    'eye': 'Occhio Vegliante',
    'wyvern': 'Viverna',
    'wasp': 'Vespa',
    'giant': 'Gigante',
    'imp': 'Folletto',
    'hand': 'Mano Vivente',
    'snake': 'Serpente',
    'drake': 'Draco',
    'bear': 'Orso',
    'armor': 'Armatura Vivente',
    'medusa': 'Medusa',
    'cupid': 'Cupido',
    'phantom': 'Ombra Illusoria',
    'harpy': 'Arpia',
    'dragon': 'Drago',
    'dinosaur': 'Dinosauro',
    'alien': 'Alieno',
    'cerberus': 'Cerbero',
    'spider': 'Ragno',
    'rock': 'Elementale di Roccia',
    'crab': 'Granchio',
    'skeleton': 'Scheletro',
    'piece': 'Pedina',
    'cat': 'Gatto',
    'dog': 'Cane',
    'roran': 'Roran',
    'mermaid': 'Sirena',
    'rat': 'Ratto',
    'shell': 'Chiocciola Corazzata',
    'machine': 'Automa',
    'wisp': 'Fatuo',
    'chicken': 'Gallina',
    'stalker': 'Cacciatore Furtivo',
    'yeek': 'Yeek',
    'yith': 'Grande Yith',
    'octopus': 'Polpo',
    'horse': 'Cavallo',
    'quickling': 'Quickling',
    'metal': 'Creatura Metallica',
    'bike': 'Motocicletta',
    'fish': 'Pesce',
    'animal': 'Maiale',
    'catgod': 'Dio Gatto',
    'machinegod': 'Dio Macchina',
    'undeadgod': 'Dio Non-Morto',
    'catsister': 'Sorellina Gatto',
    'demon': 'Demone',
    'servant': 'Apostolo Divino',
    'god': 'Divinità',
    'god_mani': 'Mani'
}

race_details_it = {
    'yerles': 'Gli Yerles, popolo del Nuovo Regno in ascesa a Sierre Terre, vantano un lignaggio illustre ma si affidano principalmente alle armi da fuoco moderne e alla tecnologia. Possiedono elevate capacità di apprendimento e ottengono punti abilità extra a ogni aumento di livello.',
    'eulderna': 'Una delle nazioni più antiche di Sierre Terre, Eulderna possiede una vasta conoscenza della magia. Grazie alla loro grande intelligenza, gli Eulderna imparano rapidamente nuovi incantesimi e resistono naturalmente agli effetti della mente.',
    'fairy': 'Delicate, fragili e sfuggenti, le fate vantano un\'eccezionale potenza magica, straordinaria evasione e resistenza elementale naturale. Tuttavia, la loro costituzione minuta impedisce loro di equipaggiare oggetti pesanti.',
    'dwarf': 'I nani delle colline sono una stirpe tozza, robusta e instancabile. Un tempo costruttori di splendide città sotterranee, possiedono una resistenza fisica eccezionale, grande vigore e resistenza all\'oscurità.',
    'juere': 'Nomadi del Tyris Meridionale privi di una patria, i Juere scivolano spesso nel brigantaggio, diffidati dalle altre genti. Flessibili e scaltri, eccellono nelle arti furtive, nel raccogliere cibo e sopportano bene la fame prolungata.',
    'elea': 'Tra le razze più antiche e misteriose di Sierre Terre, gli Elea sono eremiti custodi della foresta. La loro naturale affinità con il mana riduce il consumo magico e mitiga gli effetti nocivi del sovraccarico arcano.',
    'mutant': 'Poco si sa sulle Forme del Caos, note anche come Deformi. Con l\'avanzare dell\'esperienza, il loro corpo muta sviluppando arti casuali in posizioni insolite, permettendo combinazioni di equipaggiamento uniche.',
    'snail': 'La lumaca è una creatura incredibilmente lenta, fragile, debole e goffa, priva di quasi ogni attributo vitale. Il sale le è letale. È la sfida estrema per ogni avventuriero.',
    'lich': 'Non-morti immortali dotati di intelligenza e potere arcano immensi, i Lich possiedono grande resistenza al freddo e all\'oscurità, oltre a un controllo magistrale sulle forze dell\'Oltretomba.',
    'wraith': 'Spettri immateriali non-morti che fluttuano tra i mondi, insensibili a molte ferite mortali e portatori di freddo sepolcrale.',
    'golem': 'I golem sono costrutti a cui è stata infusa la vita tramite antiche formule alchemiche. Fatti di solida materia, non possono essere avvelenati o storditi e godono di un\'enorme salute, a scapito della velocità.',
    'mifu': 'I Mifu sono una razza ibrida volpe-umano che vive appartata in un angolo di Tyris. Famosi per agilità, sensi acuti e grande affinità con i trucchi della natura.',
    'nefu': 'Caratterizzati da pelliccia rossa, code morbide e spiriti vivaci, i Nefu sono creature socievoli e abili nelle danze e nel canto magico.',
    'succubus': 'Conosciute come stirpe lunare, le Succubi possiedono un fascino innato in grado di ammaliare creature di ogni genere e di trarre energia vitale dagli incontri amorosi.',
    'vampire': 'I vampiri sono temuti da secoli come sovrani della notte. Dotati di rigenerazione, forza e controllo sul sangue, temono solo la luce ardente del sole.',
    'demigod': 'I semidei sono la progenie di avatar divini scesi sulla terra. Godono di attributi di base superiori e di una crescita equilibrata in ogni disciplina.',
    'centaur': 'I centauri uniscono il possente torso umano alle zampe equine, vantando una velocità naturale formidabile e grande potenza nel tiro con l\'arco.',
    'shiba': 'I fedeli e fieri Shiba sono noti per la loro lealtà incrollabile, sensi sviluppatissimi e spirito protettivo verso il proprio padrone.',
    'eldercrab': 'I Granchi Antichi sono la più vetusta specie di crostacei, con corazze impenetrabili e tenaglie capaci di stritolare la pietra.',
    'slime': 'Masse gelatinose prive di forma fissa, immuni a molte lacerazioni e capaci di assorbire impatti letali.'
}

file_p = 'd:/Mod/Elin/Lang/IT/Game/Race.xlsx'
wb = openpyxl.load_workbook(file_p)
ws = wb.active
headers = [str(c.value) for c in ws[1]]
name_col = headers.index('name') + 1
detail_col = headers.index('detail') + 1

count = 0
for r in range(2, ws.max_row + 1):
    rid = ws.cell(row=r, column=1).value
    if rid in race_names_it:
        ws.cell(row=r, column=name_col, value=race_names_it[rid])
        if rid in race_details_it:
            ws.cell(row=r, column=detail_col, value=race_details_it[rid])
        count += 1

wb.save(file_p)
print(f'Race.xlsx translated {count} races!')
