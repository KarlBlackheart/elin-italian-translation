import openpyxl, json, re

def build_details_map():
    details_data = json.load(open('scratch/thing_unique_details.json', 'r', encoding='utf-8'))
    
    D = {
        'A portable lamp used to illuminate the surroundings. Much favored by adventurers.': 'Una lampada portatile usata per illuminare i dintorni. Molto apprezzata dagli avventurieri.',
        'A bottle containing brewed liquid.': 'Una bottiglia contenente liquido distillato o alchemico.',
        'Made by Cyber Dome Inc,': 'Fabbricato dalla Cyber Dome Inc.',
        'An ornamental mask worn over the face.': 'Una maschera ornamentale indossata sul volto.',
        'A fine tail.': 'Una splendida coda.',
        'A scroll written in runes.': 'Una pergamena vergata in caratteri runici.',
        'A book written in runes.': 'Un libro scritto in caratteri runici.',
        'A note containing instructions for item crafting. Reading it teaches the recipe.': 'Un appunto contenente istruzioni di fabbricazione. Leggendolo si apprende la ricetta.',
        'A wooden door. Can be placed on top of a wall.': 'Una porta di legno. Può essere posizionata sopra un muro.',
        'A foreign door. Can be placed on top of a wall.': 'Una porta esotica. Può essere posizionata sopra un muro.',
        'A small leather bag.': 'Una piccola sacca di cuoio.',
        'A bulletin board where you can view requests from residents and immigrants.': 'Una bacheca dove consultare le richieste dei residenti e degli immigrati.',
        'A coin with exotic symbol engraved.': 'Una moneta con inciso un simbolo esotico.',
        'A music box filled with memories.': 'Un carillon colmo di ricordi.',
        'A fabric door. Can be placed on top of a wall.': 'Una porta in tessuto. Può essere posizionata sopra un muro.',
        'A sheet of paper for drawing. Place it on the ground to freely draw pictures.': 'Un foglio di carta da disegno. Posizionalo a terra per dipingere liberamente.',
        'A tool that can change various settings in a room when installed and used.': 'Uno strumento che permette di modificare varie impostazioni della stanza una volta installato.',
        'A blunt weapon with a round end that is sometimes spiked.': 'Un’arma contundente ricavata lavorando il materiale grezzo.',
        'A weapon employed in close hand-to-hand fighting.': 'Un’arma impiegata nel combattimento corpo a corpo ravvicinato.',
        "A decorative clothing that doesn't offer much protection.": 'Un abito decorativo che non offre una grande protezione come armatura.',
        'A container that can hold orens inside. To retrieve the orens, it must be broken.': 'Un salvadanaio per conservare oren. Per prelevare il denaro deve essere rotto.',
        'A signpost indicating the destination. Spawn location of the map changes when placed at the edge of the map.': 'Un cartello segnaletico che indica la direzione. Il punto di spawn cambia se posizionato al margine della mappa.',
        'A pillow for hugging tightly while sleeping, which can be shared with a companion when placed on a bed.': 'Un cuscino da abbracciare durante il sonno, condivisibile con un compagno se posizionato su un letto.',
        'A stone door. Can be placed on top of a wall.': 'Una porta di pietra. Può essere posizionata sopra un muro.',
        'A door often used in jails. Can be placed on top of a wall.': 'Una robusta porta carceraria. Può essere posizionata sopra un muro.',
        'A mysterious light source that emits sunlight.': 'Una misteriosa fonte di luce che emana luce solare.',
        'A short wand filled with magic.': 'Una corta verga intrisa di energia magica.',
        'A wooden weapon used for combat practice.': 'Un’arma di legno usata per l’addestramento al combattimento.',
        'A double-edged sword': 'Una spada a doppio taglio dalla lama sottile.',
        'A single-bladed axe resembling a polearm.': 'Un’ascia a lama larga simile a un’arma in asta.',
        'A versatile hammer useful for both construction and combat.': 'Un martello versatile utile sia per la costruzione che per il combattimento.',
        'A stick useful for poking or prodding.': 'Un bastone utile per punzecchiare o colpire.',
        'An agile weapon requiring both strength and agility to wield effectively.': 'Un’arma agile che richiede forza e destrezza per essere maneggiata con efficacia.',
        'A curved single-edged blade used in slashing and thrusting attacks.': 'Una lama curva a filo singolo adatta a fendenti e affondi.',
        'A large, heavy, single-edged knife with a broad blade.': 'Un grosso e pesante coltello da caccia a lama larga.',
        'A polearm consisting of a shaft with a pointed blade.': 'Un’arma in asta formata da un manico con punta acuminata.',
        'A large, two-handed polearm with an axe-like blade.': 'Una grande alabarda a due mani con lama a scure.',
        'A defensive weapon made of wood or metal used to absorb the impact of blows.': 'Un dispositivo difensivo in legno o metallo usato per assorbire i colpi nemici.',
        'A defensive weapon made of wood or metal used to intercept attacks.': 'Uno scudo in legno o metallo usato per intercettare gli attacchi.',
        'A piece of armor used to protect the torso.': 'Un’armatura impiegata per proteggere il busto.',
        'A piece of armor used to protect the head.': 'Un copricapo o elmo usato per proteggere la testa.',
        'A piece of armor used to protect the hands.': 'Protezioni corazzate per salvaguardare le mani.',
        'A piece of armor used to protect the feet.': 'Calzature corazzate per proteggere i piedi.',
        'A long piece of cloth used as an accessory.': 'Una lunga fascia di stoffa indossata come accessorio.',
        'A ring worn on the finger.': 'Un anello da portare al dito.',
        'An ornament worn around the neck.': 'Un ornamento prezioso portato intorno al collo.',
        'A ranged weapon used to shoot arrows.': 'Un’arma a distanza usata per scoccare frecce.',
        'A ranged weapon that fires projectiles.': 'Un’arma a distanza che spara proiettili.',
        'A ranged weapon consisting of a bow mounted on a stock.': 'Un’arma a distanza costituita da un arco montato su affusto.',
        'An explosive device used to cause damage over an area.': 'Un dispositivo esplosivo che infligge danni ad area.',
        'A projectile designed to be thrown by hand.': 'Un’arma da lancio progettata per essere scagliata a mano.',
        'A tool used for digging.': 'Uno strumento da scavo per modellare il terreno.',
        'A tool used for cutting wood.': 'Uno strumento usato per tagliare legname.',
        'A tool used for catching fish.': 'Uno strumento adoperato per pescare.',
        'A container used to hold liquids or small items.': 'Un contenitore per conservare liquidi o piccoli oggetti.',
        'A musical instrument that produces sound when played.': 'Uno strumento musicale che emette note melodiose quando suonato.',
        'A delicious food that restores stamina and provides nutrition.': 'Una pietanza prelibata che ripristina il vigore e nutre il corpo.',
        'A seed that can be planted in soil to grow crops.': 'Un seme che può essere piantato nel terreno per far crescere colture.'
    }

    for k, info in details_data.items():
        if k in D: continue
        
        # Check patterns
        if k.startswith('A note containing instructions for'):
            D[k] = 'Un foglio contenente istruzioni di fabbricazione. Leggendolo si apprende la ricetta.'
        elif k.startswith('A portable lamp used to'):
            D[k] = 'Una lampada portatile per illuminare i dintorni. Molto amata dagli avventurieri.'
        elif k.startswith('A wooden door.'):
            D[k] = 'Una porta di legno. Può essere posizionata sopra un muro.'
        elif k.startswith('A stone door.'):
            D[k] = 'Una porta di pietra. Può essere posizionata sopra un muro.'
        elif k.startswith('A foreign door.'):
            D[k] = 'Una porta esotica. Può essere posizionata sopra un muro.'
        elif k.startswith('A fabric door.'):
            D[k] = 'Una porta in tessuto. Può essere posizionata sopra un muro.'
        elif k.startswith('A scroll written in'):
            D[k] = 'Una pergamena vergata in caratteri runici.'
        elif k.startswith('A book written in'):
            D[k] = 'Un libro scritto in caratteri runici.'
        elif k.startswith('A seed of'):
            item_name = k.replace('A seed of', '').replace('.', '').strip()
            D[k] = f'Un seme di {item_name}. Piantalo in un campo arato.'
        elif 'Can be placed on top of a wall.' in k:
            base = k.replace('Can be placed on top of a wall.', '').strip()
            D[k] = f'{base}. Può essere posizionato sopra un muro.'
        else:
            D[k] = k

    return D

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/Thing.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    D = build_details_map()
    count = 0

    for r in range(2, ws.max_row+1):
        ev = ws.cell(row=r, column=headers['detail_EN']).value
        if ev:
            k = str(ev).strip()
            if k in D and D[k] != k:
                ws.cell(row=r, column=headers['detail']).value = D[k]
                count += 1
            elif str(ev) in D and D[str(ev)] != str(ev):
                ws.cell(row=r, column=headers['detail']).value = D[str(ev)]
                count += 1

    wb.save('Lang/IT/Game/Thing.xlsx')
    print(f'Applied {count} detail translations to Thing.xlsx')

if __name__ == '__main__':
    run()
