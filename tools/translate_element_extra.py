import openpyxl, json, re

def build_extra_map():
    extra_data = json.load(open('scratch/unique_extra_en.json', 'r', encoding='utf-8'))
    
    E = {}

    # Standard attributes / tags
    std = {
        'Item Quality': 'Qualità Oggetto',
        'STR': 'FOR',
        'END': 'COS',
        'DEX': 'DES',
        'PER': 'PER',
        'LER': 'APP',
        'WIL': 'VOL',
        'MAG': 'MAG',
        'CHA': 'CAR',
        'LUC': 'FOR',
        'SPD': 'VEL',
        'Swimming Exp': 'ESP Nuoto',
        'Faith Exp': 'ESP Fede',
        'STR Potency': 'Potenziale FOR',
        'END Potency': 'Potenziale COS',
        'DEX Potency': 'Potenziale DES',
        'PER Potency': 'Potenziale PER',
        'LER Potency': 'Potenziale APP',
        'WIL Potency': 'Potenziale VOL',
        'MAG Potency': 'Potenziale MAG',
        'CHA Potency': 'Potenziale CAR',
        'Lighten': 'Alleggerimento',
        'Venom': 'Veleno Letale',
        'Excitement, Not Duplicable': 'Eccitazione, Non Duplicabile',
        'Weight Gain': 'Aumento di Peso',
        'Weight Loss': 'Perdita di Peso',
        'Not fermentable': 'Non fermentabile',
        'Food effect multiplier when vampiric (x#1)': 'Moltiplicatore effetti del cibo da vampiro (x#1)',
        'END Potency, WIL Potency, Weight Loss': 'Potenziale COS, Potenziale VOL, Perdita di Peso',
        'Healing, Bed Comfort': 'Guarigione, Comfort del Letto',
        'Price, Copy Fee': 'Prezzo, Costo di Copia',
        'Price': 'Prezzo',
        'Cure Poison': 'Cura Veleno',
        'Mental Serenity': 'Serenità Mentale',
        'Cure Bleeding': 'Cura Sanguinamento',
        'Hot Spring Effect': 'Effetto Sorgente Termale',
        'Food Effect, Gift Value': 'Effetto Nutritivo, Valore del Dono',
        'All Potency, Weaken Faith, Not Duplicable': 'Tutti i Potenziali, Indebolisce la Fede, Non Duplicabile',
        'Price, Not Duplicable': 'Prezzo, Non Duplicabile',
        'Anti Sleep': 'Antisonno',
        'Stamina Recovery': 'Recupero Vigore',
        'Nutrition': 'Valore Nutritivo',
        'Air': 'Aria',
        'Not Duplicable, Not Offerable': 'Non Duplicabile, Non Offribile',
        'Increased Reading Difficulty,Reduced Memorization Effect': 'Difficoltà di Lettura Aumentata, Effetto Memorizzazione Ridotto',
        'Not Duplicable': 'Non Duplicabile',
        'Effect Range': 'Raggio d’Effetto',
        'Increased Food Effects': 'Effetti del Cibo Incrementati',
        'Greatly reduce the effect of mana overflow': 'Riduce notevolmente il contraccolpo da sovraccarico di mana',
        'Learn feats faster,Platinum coin discount when training': 'Apprendimento talenti più rapido, Sconto in monete di platino nell’addestramento',
        'Fewer body parts,Your body grows parts': 'Meno parti corporee, Nuove parti corporee crescono sul tuo corpo',
        'Cannot equip stuff weight more than 1s,Greatly increase evasion': 'Impossibile equipaggiare oggetti di peso superiore a 1s, Grande incremento della schivata',
        'Have no problem eating human flesh': 'Nessun problema a consumare carne umana',
        'Allies take less damage per blessing,Enemies take more damage per hex, Effect increases with each active copy': 'Gli alleati subiscono meno danni per ogni benedizione, I nemici subiscono più danni per ogni maledizione, L’effetto aumenta con più copie attive',
        'Increased spell learning speed,Enhanced Touch and Sword spells,To-Hit bonus when attacking with longswords': 'Velocità di apprendimento incantesimi aumentata, Incantesimi di Contatto e Spada potenziati, Bonus alla precisione con spade lunghe',
        'Your tail moves,Decreased speed when equipping waist gear': 'La tua coda si muove, Velocità ridotta quando si equipaggia una cintura',
        'Melt in salt': 'Si scioglie con il sale',
        'Reduce the chance area spells hitting friends': 'Riduce il rischio che gli incantesimi ad area colpiscano gli alleati',
        'Receive various bonuses when drunk,Walk straight when drunk,Increase the effect of temporary attribute boosts': 'Ricevi vari bonus quando sei ubriaco, Cammini dritto anche da ubriaco, Aumenta l’effetto dei potenziamenti temporanei di attributo',
        'Able to prey on sleeping creatures,Grow through pleasurable experiences': 'Capace di adescare creature addormentate, Cresci attraverso esperienze piacevoli',
        'Immune to daze,Immune to bleeding': 'Immunità allo stordimento, Immunità al sanguinamento',
        'Reduce all damage significantly': 'Riduce drasticamente tutti i danni subiti',
        'Restrain the target with scissors': 'Immobilizza il bersaglio con le chele',
        'Avoid death when stamina is more than half': 'Evita la morte quando il vigore è superiore al 50%',
        'Thorns harm those who attack': 'Le spine feriscono chiunque ti attacchi',
        'Split when hurt': 'Ti scindi quando vieni ferito',
        'Acid burns those who attack': 'L’acido ustiona chiunque ti attacchi',
        'Guard allies': 'Fa da scudo agli alleati',
        "Faster faith gain,More benefit from God's favour,Increases all attributes when faithless,Immune to divine punishment": 'Guadagno di fede più rapido, Maggiori benefici dal favore divino, Aumenta tutti gli attributi se privo di fede, Immunità alla punizione divina',
        'Gain Euphoric when insulted': 'Ottiene Euforia quando viene insultato',
        'Split when getting wet': 'Ti scindi quando ti bagni d’acqua',
        'Increased spawn rate of shrines and statues,Increased spawn rate of certain monsters,Certain monsters become friendly': 'Aumenta la frequenza di santuari e statue, Aumenta la comparsa di certi mostri, Certi mostri diventano pacifici',
        'Increased spawn rate of rare monsters,Certain monsters become hostile': 'Aumenta la comparsa di mostri rari, Certi mostri diventano ostili',
        'Party servant quarrel threshold +#1,Effective only for the player or NPC under faith of Elin of Harmony': 'Soglia di litigio dei servitori +#1, Valido solo per il giocatore o PNG devoti a Elin dell’Armonia',
        '+#1 gene slot limit,Enhanced Shared Diary effect,Boosted Exp Bonus': '+#1 limite slot genici, Effetto Diario Condiviso potenziato, Bonus ESP incrementato',
        'Apply only to the player,Evolve by consuming genes,Learn "Devour" ability,+#1 gene slot limit,Gene slot limit increases as you level': 'Si applica solo al giocatore, Ti evolvi consumando geni, Apprendi l’abilità "Divora", +#1 limite slot genici, Il limite di slot aumenta salendo di livello',
        'Always pleasurable\nAlways pleasurable,Boosted Exp Bonus,Grant "Rebirth" on sleep': 'Sempre piacevole\nSempre piacevole, Bonus ESP incrementato, Conferisce "Rinascita" durante il riposo',
        'Party love quarrel threshold +#1': 'Soglia di litigio amoroso del gruppo +#1',
        'Enhance equipment dropped as loot': 'Potenzia l’equipaggiamento rilasciato come bottino',
        'Spit out seeds after eating': 'Sputa semi dopo aver consumato il pasto',
        'Draw strength from cursed equipment': 'Trae potere dall’equipaggiamento maledetto',
        'Evolve with each tail grown': 'Ti evolvi per ogni nuova coda sviluppata',
        '"Bane" excommunicates the target': '"Flagello" scomunica e purifica il bersaglio',
        'Can brew more potions,Skilled at broom riding': 'Può distillare più pozioni, Abile nel cavalcare la scopa',
        'Increased talisman effect,Increased talisman charges': 'Effetto dei talismani aumentato, Cariche dei talismani aumentate',
        'Strengthen allies per enemy count on the same level': 'Potenzia gli alleati in base al numero di nemici sul piano attuale',
        'Animals start talking': 'Gli animali cominciano a parlare',
        'Nullifies curses occasionally': 'Annulla occasionalmente le maledizioni',
        'Increased stamina recovery when sleeping,Increased chance of learning a recipe when sleeping': 'Recupero di vigore aumentato durante il sonno, Maggiore probabilità di apprendere ricette dormendo',
        '+#1 range for searching containers when crafting': '+#1 raggio di ricerca nei contenitori durante la fabbricazione',
        '+#1 Body Parts': '+#1 Parti del Corpo',
        '+#1 Max Ally': '+#1 Massimo Alleati',
        'Boost attributes proportional to max ally vacancies': 'Potenzia gli attributi in proporzione agli slot alleato rimasti liberi',
        '+#1 Max Summon': '+#1 Massimo Evocazioni',
        "Usable only when hungry,Obtain target's gene,Obtained gene does not consume feat points,Higher chance to gain body parts when you have fewer body parts": 'Utilizzabile solo quando hai fame, Ottieni il gene del bersaglio, Il gene ottenuto non consuma punti talento, Maggiore probabilità di acquisire parti corporee se ne possiedi poche',
        "Slightly increase affinity,Consumes target's interest,Likely to fail when target's affinity is low": 'Aumenta leggermente l’affinità, Consuma l’interesse del bersaglio, Rischio di fallire se l’affinità del bersaglio è bassa',
        'The number of weapons affects stamina usage': 'Il numero di armi impugnate influenza il consumo di vigore',
        'High chance to remove a hex': 'Alta probabilità di rimuovere una maledizione',
        'Halves the power of hexes that resist purification': 'Dimezza la potenza delle maledizioni che resistono alla purificazione',
        'Remove all blessings if the target is an ally,Remove one blessing if the target is an enemy': 'Rimuove tutte le benedizioni se il bersaglio è un alleato, Rimuove una benedizione se il bersaglio è un nemico',
        'Release a #calc #ele breath': 'Rilascia un soffio di elemento #ele (#calc)',
        'Invoke a #calc #ele sphere,Damage falls off with distance from the center': 'Evoca una sfera di elemento #ele (#calc), Il danno diminuisce allontanandosi dal centro',
        'Emit a #calc #ele beam': 'Emette un raggio di elemento #ele (#calc)',
        'Touch the target with #calc #ele hand,More likely to inflict elemental damage': 'Tocca il bersaglio con una mano di elemento #ele (#calc), Maggiore probabilità di infliggere danno elementale',
        'Fire a #calc #ele arrow': 'Scaglia una freccia di elemento #ele (#calc)',
        "Slash the target with #calc #ele phantasmal sword,Penetrate the target's armor": 'Squarta il bersaglio con una lama spettrale di elemento #ele (#calc), Penetra l’armatura del bersaglio',
        '@ConWeapon,Resistance bonus scales with Charisma,Converts weapon damage to #ele': '@ConWeapon, Il bonus di resistenza scala con il Carisma, Converte il danno dell’arma in elemento #ele',
        'Summon #calc #ele meteors': 'Evoca meteore di elemento #ele (#calc)',
        'Invoke #calc #ele earthquake,Reduced damage against floating targets,Massive damage against targets affected by gravity,Damage falls off with distance from the center': 'Scatena un terremoto di elemento #ele (#calc), Danno ridotto contro bersagli fluttuanti, Danno colossale contro bersagli soggetti a gravità, Il danno cala con la distanza dal centro',
        'Unleash a #calc #ele spear,Target slain by this spear drops milk or an egg,Target slain by this spear sometimes drops a gene,Damage scales with the caster’s Charisma': 'Scaglia una lancia di elemento #ele (#calc), I nemici uccisi rilasciano latte o un uovo, I nemici uccisi rilasciano talvolta un gene, Il danno scala con il Carisma dell’incantatore',
        'Fire a #calc #ele arrow,Target slain by this arrow sometimes drops milk or an egg,Target slain by this arrow sometimes drops a gene,Damage scales with the caster’s Charisma': 'Scaglia una freccia di elemento #ele (#calc), I nemici uccisi rilasciano talvolta latte o un uovo, I nemici uccisi rilasciano talvolta un gene, Il danno scala con il Carisma dell’incantatore',
        'Release #calc #ele shards,Attack counts increase with hexes,Low chance to remove each hex on the target': 'Sprigiona frammenti di elemento #ele (#calc), Il numero di attacchi cresce con le maledizioni, Bassa probabilità di dissolvere ciascuna maledizione'
    }
    E.update(std)

    # For any remaining keys, if it starts with @, keep it as @, otherwise translate or fallback
    for k, v in extra_data.items():
        if k in E: continue
        if k.startswith('@'):
            E[k] = k
        else:
            # check patterns
            if '#calc #ele' in k:
                t = k.replace('Release a #calc #ele breath', 'Rilascia un soffio di elemento #ele (#calc)')
                t = t.replace('Invoke a #calc #ele sphere', 'Evoca una sfera di elemento #ele (#calc)')
                t = t.replace('Emit a #calc #ele beam', 'Emette un raggio di elemento #ele (#calc)')
                t = t.replace('Touch the target with #calc #ele hand', 'Tocca il bersaglio con una mano di elemento #ele (#calc)')
                t = t.replace('Fire a #calc #ele arrow', 'Scaglia una freccia di elemento #ele (#calc)')
                t = t.replace('Damage falls off with distance from the center', 'Il danno cala con la distanza dal centro')
                t = t.replace('More likely to inflict elemental damage', 'Maggiore probabilità di infliggere danno elementale')
                t = t.replace('Penetrate the target\'s armor', 'Penetra l’armatura del bersaglio')
                E[k] = t
            else:
                E[k] = k

    return E

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/Element.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    E = build_extra_map()
    count = 0

    for r in range(2, ws.max_row+1):
        ev = ws.cell(row=r, column=headers['textExtra_EN']).value
        if ev:
            k = str(ev).strip()
            if k in E and E[k] != k:
                ws.cell(row=r, column=headers['textExtra']).value = E[k]
                count += 1
            elif str(ev) in E and E[str(ev)] != str(ev):
                ws.cell(row=r, column=headers['textExtra']).value = E[str(ev)]
                count += 1

    wb.save('Lang/IT/Game/Element.xlsx')
    print(f'Applied {count} textExtra translations to Element.xlsx')

if __name__ == '__main__':
    run()
