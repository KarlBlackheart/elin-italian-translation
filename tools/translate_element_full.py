"""
Translate remaining Element.xlsx:
- detail (9 items)
- textPhase (73 items)
- textAlt (11 items)
- textExtra (~200 items)
"""

import openpyxl

ELEMENT_FILE = 'Lang/IT/Game/Element.xlsx'

DETAIL_MAP = {
    "An ordinance allowing even duplicate exhibits to be counted as having slight tourism value.  Cannot be implemented simultaneously with Solo Exhibition.":
        "Un'ordinanza che consente anche ai reperti duplicati di avere un lieve valore turistico. Non può essere attivata contemporaneamente a Mostra Singola.",
    "An ordinance that significantly raises the prices of tagged goods at the cost of greatly decreased purchasing power.":
        "Un'ordinanza che aumenta notevolmente i prezzi delle merci etichettate, al costo di un potere d'acquisto fortemente ridotto.",
    "An ordinance that raises the prices of tagged goods at the cost of decreased purchasing power.":
        "Un'ordinanza che aumenta i prezzi delle merci etichettate, al costo di un ridotto potere d'acquisto.",
    "A license that increases the prices of tagged items other than food, beverages and furniture.":
        "Una licenza che aumenta il prezzo degli oggetti etichettati diversi da cibo, bevande e mobili.",
    "An ordinance that increases the appraisal value of the item ranked number one in the heirloom rankings.":
        "Un'ordinanza che aumenta il valore di stima dell'oggetto al primo posto nella classifica dei cimeli.",
    "An ordinance that enhances the tourism value of exhibits. Cannot be implemented simultaneously with Mass Exhibition.":
        "Un'ordinanza che migliora il valore turistico delle mostre. Non può essere attivata contemporaneamente a Mostra di Massa.",
    "License to increase the prices of tagged stolen goods. If you belong to the Thieves Guild, you will be also able to earn contribution points.":
        "Licenza per aumentare il prezzo delle merci rubate etichettate. Se appartieni alla Gilda dei Ladri, otterrai anche punti contributo.",
    "Damage your own body and inflicts various status effects. The last card to play when there is nothing you can do.":
        "Danneggia il tuo stesso corpo infliggendo vari stati alterati. L'ultima carta da giocare quando non rimane nient'altro da fare.",
    "Concentrate magical power in the caster's hand to harm any touched target.":
        "Concentra il potere magico nella mano di chi la lancia per ferire qualunque bersaglio toccato.",
}

PHASE_MAP = {
    "It slows the progression of the Ether disease.": "Rallenta la progressione della malattia dell'Etere.",
    "It enhances attack accuracy.": "Migliora la precisione degli attacchi.",
    "It makes you invisible.": "Ti rende invisibile.",
    "It lets you see invisible objects.": "Ti permette di vedere oggetti e creature invisibili.",
    "It lowers your resistance to love.": "Riduce la tua resistenza all'amore.",
    "It does not get in the way of movement.": "Non ostacola i movimenti.",
    "It negates the effect of poison.": "Annulla gli effetti del veleno.",
    "It negates the effect of blindness.": "Annulla gli effetti della cecità.",
    "It negates the effect of paralysis.": "Annulla gli effetti della paralisi.",
    "It negates the effect of fear.": "Annulla gli effetti della paura.",
    "It negates the effect of sleep.": "Annulla gli effetti del sonno.",
    "It negates the effect of confusion.": "Annulla gli effetti della confusione.",
    "It protects your neck.": "Protegge il tuo collo.",
    "It harvests life with any attack.": "Miete la vita con qualsiasi attacco.",
    "It lets you breathe underwater.": "Ti permette di respirare sott'acqua.",
    "It increases the maximum ammunition capacity.": "Aumenta la capacità massima di munizioni.",
    "It reduces the reload time for the weapon.": "Riduce il tempo di ricarica dell'arma.",
    "It makes the weapon fire multiple times.": "Permette all'arma di sparare colpi multipli.",
    "It knocks back the target when hit.": "Respinge il bersaglio quando viene colpito.",
    "It recovers ammunition upon firing.": "Recupera munizioni quando si spara.",
    "It minimizes the penalty for shooting at distance.": "Minimizza la penalità per il tiro a distanza.",
    "It drills through the target when hit.": "Trapassa il bersaglio quando viene colpito.",
    "It strikes the area around the target.": "Colpisce l'area circostante al bersaglio.",
    "It generates a shockwave at the target's location.": "Genera un'onda d'urto nel punto del bersaglio.",
    "It reduces the consumption of talismans and intonations.": "Riduce il consumo di talismani e intonazioni.",
    "It pursues the target that evades an attack.": "Insegue il bersaglio che schiva un attacco.",
    "It unleashes consecutive attacks on the target.": "Sferra attacchi consecutivi sul bersaglio.",
    "It attacks enemies adjacent to the target.": "Attacca i nemici adiacenti al bersaglio.",
    "It disrupts the target's actions.": "Interrompe le azioni del bersaglio.",
    "It delivers a decisive blow to the target that evades an attack.": "Infligge un colpo decisivo al bersaglio che schiva un attacco.",
    "It is alive.": "È vivo.",
    "It forbids you from violence.": "Ti proibisce ogni atto di violenza.",
    "It prevents you from receiving its enhancement.": "Ti impedisce di ricevere i suoi potenziamenti.",
    "It curses itself every time it is equipped.": "Si maledice ogni volta che viene equipaggiato.",
    "It absorbs life.": "Assorbe la vita.",
    "It is shining.": "Brilla di luce propria.",
    "It is vibrating.": "Sta vibrando.",
    "You eat effectively.": "Mangi in modo molto efficiente.",
    "You can supress mana overflow.": "Riesci a sopprimere il trabocco di mana.",
    "Your body is changing every moment.": "Il tuo corpo muta in ogni istante.",
    "You have no trouble eating human flesh.": "Non hai problemi a nutrirti di carne umana.",
    "Your lineage is ancient.": "Il tuo lignaggio è antichissimo.",
    "You have a fluffy tail.": "Hai una coda soffice.",
    "Your casting is precise.": "I tuoi incantesimi sono straordinariamente precisi.",
    "Mead runs in your blood.": "Nelle tue vene scorre idromele.",
    "You love things that feel good.": "Ami tutto ciò che dà piacere.",
    "You don't grow up.": "Non cresci mai.",
    "You take pleasure in being insulted.": "Provi piacere nell'essere insultato.",
    "Your existence brings terror.": "La tua semplice presenza incute terrore.",
    "Your stomach is bottomless.": "Il tuo stomaco è un pozzo senza fondo.",
    "Your stomach is small.": "Il tuo stomaco è piccolissimo.",
    "You grew up in the north.": "Sei cresciuto nelle gelide terre del nord.",
    "You can absorb other living beings": "Puoi assorbire altri esseri viventi.",
    "You embrace love in all its forms.": "Accogli l'amore in tutte le sue forme.",
    "Your voice fills the air.": "La tua voce risuona nell'aria.",
    "You want to protect your allies.": "Desideri proteggere i tuoi alleati ad ogni costo.",
    "You can reboot yourself.": "Puoi riavviarti in caso di collasso.",
    "You can purify cursed equipment.": "Riesci a purificare l'equipaggiamento maledetto.",
    "You grow tails.": "Ti crescono code.",
    "You despise heresy.": "Disprezzi profondamente l'eresia.",
    "You have knowledge of talisman.": "Possiedi la conoscenza arcana dei talismani.",
    "You boost the morale of your allies.": "Sollevi il morale dei tuoi compagni.",
    "You feel death close to you.": "Senti la morte costantemente vicina a te.",
    "You want to heal your allies.": "Desideri curare i tuoi alleati.",
    "You feel an urge to cut off heads at a visible neck.": "Senti l'impulso irrefrenabile di mozzare le teste appena scorgi un collo.",
    "You wear human skin.": "Indossi pelle umana.",
    "Your blood is boiling.": "Il tuo sangue sta ribollendo.",
    "Your skin is covered by frost.": "La tua pelle è ricoperta di brina.",
    "Your body conducts electricity well.": "Il tuo corpo conduce eccellentemente l'elettricità.",
    "Your body is purified.": "Il tuo corpo è purificato.",
    "Your body is defiled.": "Il tuo corpo è corrotto e profanato.",
    "Your hair is thick.": "I tuoi capelli sono foltissimi.",
    "Your existence provokes living things.": "La tua esistenza provoca e irrita ogni creatura vivente.",
}

TEXTALT_MAP = {
    "Swimming,Not Swimming,Swimming": "Nuoto,Non a nuoto,Nuoto",
    "Faith,Waning Faith,Rising Faith": "Fede,Fede vacillante,Fede crescente",
    "Decay,Accelerate Decay,Slightly Slow Decay,Slightly Slow Decay,Slow Decay,Slow Decay,Never Decay":
        "Deperimento,Deperimento accelerato,Deperimento lievemente rallentato,Deperimento lievemente rallentato,Deperimento lento,Deperimento lento,Incorruttibile",
    "Richness,Bland,Creamy,Mellow,Thick,Rich,Velvety":
        "Ricchezza,Insipido,Cremoso,Morbido,Denso,Ricco,Vellutato",
    "Density,Hollow,Somewhat Dense,Dense,Very Dense,Bursting,Concentrated,Ultra Concentrated":
        "Densità,Vuoto,Piuttosto compatto,Compatto,Molto compatto,Pieno zeppo,Concentrato,Ultraconcentrato",
    "Delicacy,Coarse,Rough,Slightly Rough,Delicate,Extremely Delicate,Utterly Delicate":
        "Delicatezza,Grossolano,Ruvido,Lievemente ruvido,Delicato,Estremamente delicato,Sublime",
    "Color,Dull Color,Pale Color,Colorful,Bright,Vivid,Rainbow Color":
        "Colore,Sbiadito,Pallido,Colorato,Luminoso,Vivido,Iridiscente",
    "Vitamins,Harmful Substance,Trace Vitamins,Small Vitamins,Moderate Vitamins,Large Vitamins,Abundant Vitamins,Treasure Trove Vitamins":
        "Vitamine,Sostanza nociva,Tracce vitaminiche,Poche vitamine,Discrete vitamine,Molte vitamine,Ricco di vitamine,Miniera di vitamine",
    "Mushy,Soggy,Flaky,Crispy,Very Crispy,Snappy":
        "Consistenza,Molle,Inzuppato,Friabile,Croccante,Molto croccante,Fragratissimo",
    "Spiciness,Tasteless,Somewhat Spicy,Spicy,Very Spicy,Extremely Spicy,Intensely Spicy":
        "Piccantezza,Neutro,Poco piccante,Piccante,Molto piccante,Estremamente piccante,Infernale",
    "Adam,Adam,Adam": "Adam,Adam,Adam"
}

# Single phrase map for textExtra comma-separated tokens
EXTRA_PHRASES = {
    "PER": "PER",
    "MAG": "MAG",
    "???": "???",
    "Human mimicry": "Mimetismo umano",
    "Item mimicry": "Mimetismo oggettuale",
    "Metamorphosis": "Metamorfosi",
    "Increased hunger cap": "Limite massimo di sazietà aumentato",
    "Decreased hunger cap": "Limite massimo di sazietà ridotto",
    "Grow with milk": "Cresce nutrendosi di latte",
    "Capable of imprinting": "Capace di imprinting",
    "Protected from item destruction by cold": "Oggetti protetti dalla distruzione da gelo",
    "Learn feats faster": "Apprende talenti più rapidamente",
    "Gene suitability": "Compatibilità genetica superiore",
    "Able to harness superior elements.": "Capace di dominare elementi superiori.",
    "Increased number of minions summonable at once": "Aumenta il numero di servitori evocabili contemporaneamente",
    "Take damage in place of nearby allies": "Subisce i danni al posto degli alleati vicini",
    "+#1 gene slot limit": "+#1 al limite degli slot genici",
    "Immunity to Aging": "Immunità all'invecchiamento",
    "Grants penetration to ranged weapons and magical arrows": "Le armi a distanza e le frecce magiche ottengono perforazione",
    "Attacks never miss while awakened to the Seventh Sense": "Gli attacchi non mancano mai quando risvegliato al Settimo Senso",
    "Boost attributes when mana depletes": "Aumenta gli attributi quando il mana si esaurisce",
    "Boost attributes when near death": "Aumenta gli attributi in punto di morte",
    "Grants penetration to martial arts and magical hands": "Le arti marziali e le mani magiche ottengono perforazione",
    "Grants penetration to melee weapons and magical swords": "Le armi da mischia e le lame magiche ottengono perforazione",
    "Redirects damage to your ally": "Reindirizza i danni sul tuo alleato",
    "Food provides no nutrition": "Il cibo non fornisce nutrimento",
    "Attributes rise at night": "Gli attributi aumentano durante la notte",
    "Ignite in sunlight": "Prende fuoco a contatto con la luce del sole",
    "Boosted speed in water": "Velocità aumentata in acqua",
    "Negate suffocation": "Annulla il soffocamento",
    "Grants physical attacks additional Nether damage": "Gli attacchi fisici infliggono danni aggiuntivi dall'Oltretomba",
    "Nether damage always penetrates resistances": "I danni dall'Oltretomba perforano sempre le resistenze",
    "Does not protect allies from attacks": "Non protegge gli alleati dagli attacchi",
    "Protected from impurity": "Protetto dalle impurità",
    "Ineffective if Innocence is negative": "Inefficace se l'Innocenza è negativa",
    "Hunger for love": "Fame d'amore",
    "Increased song effectiveness": "Efficacia dei canti aumentata",
    "Reduce all damage": "Riduce tutti i danni subiti",
    "Dominate machines": "Domina i macchinari",
    "Lay on Hands available when worshipping Jure": "Imposizione delle Mani disponibile se si adora Jure",
    "Learn \"Maconomy\" stance": "Apprende la postura \"Maconomia\"",
    "Improved Maconomy": "Maconomia migliorata",
    "Learn \"Taunt\" stance": "Apprende la postura \"Provocazione\"",
    "+#1 Taunt Range": "+#1 raggio di Provocazione",
    "Learn feats faster": "Apprende talenti più in fretta",
    "Mana can be used as health": "Il mana può essere usato come salute",
    "Cannot die until mana is depleted": "Impossibile morire finché il mana non è esaurito",
    "Immunity to Neck Hunt": "Immunità alla Decapitazione",
    "Halves mana usage when health is low": "Dimezza il consumo di mana quando la salute è bassa",
    "Melee attacks steal mana from enemy": "Gli attacchi in mischia assorbono mana dal nemico",
    "More benefit from God's favour": "Maggiori benefici dal favore divino",
    "Murder NPCs at random": "Assassinio casuale di PNG",
    "Neutral creatures go hostile": "Le creature neutrali diventano ostili",
    "Reduced karma penalty when killing": "Penalità al karma ridotta quando si uccide",
    "Physical attacks enhanced with each enemy defeated": "Gli attacchi fisici si potenziano a ogni nemico abbattuto",
    "Physical critical rate increases as health decreases": "La probabilità di colpo critico fisico cresce al calare della salute",
    "Poison potions": "Avvelena le pozioni",
    "Unarmed attacks convert to poison element": "Gli attacchi disarmati si convertono in elemento veleno",
    "Press and hold to identify all items in inventory": "Tieni premuto per identificare tutti gli oggetti nell'inventario",
    "Prevent damage to items": "Previene i danni agli oggetti",
    "Prevent damage to items (Entire Party)": "Previene i danni agli oggetti (Intero Gruppo)",
    "Randomize mana and stamina cost": "Casualizza il costo di mana e vigore",
    "Bonus fish shipping value": "Bonus al valore di spedizione dei pesci",
    "Reboot when dead": "Si riavvia dopo la morte",
    "Reduced heavy casting penalty when wearing heavy armor or a shield": "Penalità da incantamento pesante ridotta con armature pesanti o scudo",
    "Further reduced heavy casting penalty when wearing heavy armor or a shield": "Ulteriore riduzione della penalità da incantamento pesante",
    "Maximally reduced heavy casting penalty when wearing heavy armor or a shield": "Massima riduzione della penalità da incantamento pesante",
    "Reduced casting penalty when dimmed": "Penalità da incantamento ridotta quando stordito",
    "Reduced stamina usage": "Consumo di vigore ridotto",
    "Restore #calc and 20% of maximum mana": "Ripristina #calc e il 20% del mana massimo",
    "Restore #calc and 25% of maximum hit points": "Ripristina #calc e il 25% dei punti vita massimi",
    "Invincible on the turn used": "Invulnerabile nel turno in cui viene usata",
    "Restore #calc hit points": "Ripristina #calc punti vita",
    "See if a recipe can be learned when dismantling": "Indica se una ricetta può essere appresa smantellando",
    "Chance to discover recipes slightly increased": "Probabilità di scoprire ricette leggermente aumentata",
    "Double the chance to discover recipes": "Raddoppia la probabilità di scoprire ricette",
    "Show hidden food traits": "Mostra i tratti nascosti del cibo",
    "Add a seasoning slot to some recipes": "Aggiunge uno slot di condimento ad alcune ricette",
    "Compress the nutrition of dishes": "Comprime i nutrienti dei piatti",
    "Slash the target with #calc #ele phantasmal sword": "Squarta il bersaglio con la lama spettrale di tipo #ele pari a #calc",
    "Penetrate the target's elemental resistance": "Penetra la resistenza elementale del bersaglio",
    "Less likely to inflict elemental status effects": "Minore probabilità di infliggere stati alterati elementali",
    "Damage increases with Longsword skill": "I danni aumentano con l'abilità Spada Lunga",
    "Slightly higher item quality at gathering spots": "Qualità degli oggetti leggermente superiore nei punti di raccolta",
    "Low chance to obtain materials when dismantling traps": "Bassa probabilità di ricavare materiali smantellando trappole",
    "Higher item quality at gathering spots": "Qualità degli oggetti superiore nei punti di raccolta",
    "Moderate chance to obtain materials when dismantling traps": "Moderata probabilità di ricavare materiali smantellando trappole",
    "Failed disarm doesn't activate trap": "Il fallimento del disarmo non attiva la trappola",
    "Slightly increase affinity": "Aumenta lievemente l'affinità",
    "Consumes target's interest": "Consuma l'interesse del bersaglio",
    "Slightly enhance all allies when worshipping Horome": "Potenzia leggermente tutti gli alleati se si adora Horome",
    "Strengthen “Bladestorm” and “Swarm”": "Potenzia “Tempesta di Lame” e “Sciame”",
    "#1% parry chance (Doubled with Shield Style)": "Probabilità di parata +#1% (raddoppiata con Stile Scudo)",
    "Those who possess a Dream Larva are lured into the succubus’s bed": "Chi possiede una Larva del Sogno viene attratto nel letto della succube",
    "Those who possess a Dream Larva become more prone to Mischief": "Chi possiede una Larva del Sogno diventa più incline alle Malizie",
    "Learn \"Mischief\" at level 20": "Apprende \"Malizia\" al livello 20",
    "Upgrade the healing spell used to the next tier": "Migliora l'incantesimo di cura utilizzato al grado successivo",
    "Used party slot +#1": "Slot del gruppo utilizzati +#1",
    "Walls do not block movement": "I muri non bloccano il movimento",
    "You can steal from theft-immune targets": "Puoi rubare da bersagli immuni al furto",
    "Able to lift heavy objects": "Capace di sollevare oggetti pesanti",
    "Carry anything without complaint": "Trasporta qualunque carico senza lamentarsi",
    "Inflict gravity upon attack": "Infligge gravità quando attacca",
    "Absorb mana from rods": "Assorbe mana dalle verghe magiche",
    "Add 【Just Prepared】 trait to meal you cook": "Aggiunge il tratto 【Appena Preparato】 ai piatti cucinati",
    "Increased effect duration": "Durata dell'effetto aumentata",
    "All cocoons in the zone hatch when \"Womb of Darkness\" is activated": "Tutti i bozzoli nella zona si schiudono all'attivazione di \"Grembo dell'Oscurità\"",
    "Spiders leave no corpses": "I ragni non lasciano cadaveri",
    "Spiders use \"Acid Touch\" instead of \"Web\"": "I ragni usano \"Tocco Acido\" invece di \"Ragnatela\"",
    "Always dream of magic while sleeping": "Sogna sempre di magia durante il sonno",
    "Increased effect of magic dreams": "Effetto dei sogni magici aumentato",
    "Further increased effect of magic dreams": "Effetto dei sogni magici ulteriormente aumentato",
    "Possible to learn higher-level spells": "Possibilità di apprendere incantesimi di livello superiore",
    "Apply random hexes if the target is an enemy": "Applica maledizioni casuali se il bersaglio è un nemico",
    "Apply random blessings if the target is an ally": "Applica benedizioni casuali se il bersaglio è un alleato",
    "Attract rain clouds": "Attira nubi di pioggia",
    "Automatically pray at the end of the day if possible": "Prega automaticamente alla fine della giornata se possibile",
    "Party members also pray with you": "Anche i membri del gruppo pregano insieme a te",
    "Brand value +1": "Valore del marchio +1",
    "Can be used on creatures and items on the ground": "Utilizzabile su creature e oggetti a terra",
    "Higher power allows heavier objects to be moved": "Una potenza maggiore consente di spostare oggetti più pesanti",
    "The target is hurled away if it is adjacent to you": "Il bersaglio viene scagliato lontano se adiacente a te",
    "The target is pulled closer if it is distant from you": "Il bersaglio viene attirato a te se distante",
    "The target pushes aside any creatures along its path": "Il bersaglio spinge via ogni creatura lungo la traiettoria",
    "Invoke a #calc #ele collision": "Provoca una collisione #ele pari a #calc",
    "Collision damage increases with target weight and distance": "Il danno da collisione aumenta con il peso del bersaglio e la distanza",
    "Can eat even when full": "Può mangiare anche a stomaco pieno",
    "Grants full food effects even while full": "Fornisce i pieni effetti del cibo anche se sazio",
    "Applies only to dishes set at the party venue": "Si applica solo ai piatti disposti nel luogo del banchetto",
    "Cannot wear back gears": "Non può indossare equipaggiamento sulla schiena",
    "Cannot wear foot gears": "Non può indossare calzature",
    "Cannot wear neck gears": "Non può indossare collane o pendenti",
    "Chance to behead the target on melee attacks": "Probabilità di decapitare il bersaglio con gli attacchi in mischia",
    "Consume potions regularly": "Consuma pozioni regolarmente",
    "Damage bonus increases with distance": "Il bonus al danno aumenta con la distanza",
    "Cannot be used on adjacent targets": "Non utilizzabile su bersagli adiacenti",
    "Devour; Bloodsuck and Mischief take less time": "Divorare, Succhiare il Sangue e Malizia richiedono meno tempo",
    "Disguise does not reset hostility": "Il travestimento non resetta l'ostilità",
    "Expires after a set time": "Scade dopo un tempo prestabilito",
    "Drain blood from the target": "Drena il sangue dal bersaglio",
    "Cannot target creatures with Cut Resistance": "Non può colpire creature immuni al taglio",
    "Always reveal a food trait of blood": "Rivela sempre un tratto nutritivo del sangue",
    "Reveal an additional food trait at level 15": "Rivela un tratto nutritivo aggiuntivo al livello 15",
    "Reveal an additional food trait at level 30": "Rivela un tratto nutritivo aggiuntivo al livello 30",
    "Eating takes less time": "Mangiare richiede meno tempo",
    "Elemental status effects still trigger even without damage": "Gli effetti di stato elementali si attivano anche in assenza di danno",
    "Engage in pleasurable acts with the target": "Intrattieniti in atti piacevoli con il bersaglio",
    "Gain the potential of the target’s highest primary attribute": "Ottieni il potenziale dell'attributo primario più alto del bersaglio",
    "Enhanced performance quality": "Qualità dell'esibizione migliorata",
    "Bonus to performance reward": "Bonus alla ricompensa per l'esibizione",
    "Extract seeds from rotten foods": "Estrae semi dai cibi marci",
    "Improve seeds": "Migliora i semi",
    "Bonus crop shipping value": "Bonus al valore di spedizione dei raccolti",
    "Turn plants friendly": "Rende le piante amichevoli",
    "First 5 casts of the day have boosted high-grade fish chance": "I primi 5 lanci del giorno aumentano la possibilità di pesci rari",
    "First cast of the day guarantees high grade fish": "Il primo lancio del giorno garantisce un pesce di grado elevato",
    "Hair grows at a great pace": "I capelli crescono a vista d'occhio",
    "Hair never grows": "I capelli non crescono mai",
    "Increased effectiveness of melee weapons": "Efficacia delle armi da mischia aumentata",
    "Increased effectiveness of ranged weapons": "Efficacia delle armi a distanza aumentata",
    "Increased speed limit": "Limite massimo di velocità aumentato",
    "Reduced speed bonus when hit": "Bonus alla velocità ridotto quando colpito",
    "Increased riding dificulty": "Difficoltà di cavalcatura aumentata",
    "Greatly increased riding EXP gain": "Guadagno di ESP in cavalcatura notevolmente aumentato",
    "Increased store price": "Prezzo dei negozi aumentato",
    "Increased store inventory": "Assortimento merci dei negozi ampliato",
    "Chance to break mimicry upon taking damage": "Possibilità di interrompere il mimetismo quando si subisce danno",
    "Taking damage breaks mimicry": "Subire danno interrompe il mimetismo",
    "Taking action breaks mimicry": "Compiere un'azione interrompe il mimetismo",
    "Halves target's DV and PV": "Dimezza il VD e il VP del bersaglio",
    "Resistance bonus scales with Charisma": "Il bonus alle resistenze cresce con il Carisma",
    "Converts weapon damage to elemental damage": "Converte il danno dell'arma in danno elementale",
    "Attacking or taking elemental damage consumes a turn": "Attaccare o subire danno elementale consuma un turno",
}

def translate_extra(val):
    if not val:
        return val
    parts = val.split(',')
    res_parts = []
    for p in parts:
        p_clean = p.strip()
        if p_clean in EXTRA_PHRASES:
            res_parts.append(EXTRA_PHRASES[p_clean])
        elif p_clean.startswith('@'):
            res_parts.append(p_clean) # Engine tag intact
        else:
            res_parts.append(p_clean)
    return ','.join(res_parts)

def run():
    wb = openpyxl.load_workbook(ELEMENT_FILE)
    ws = wb['Element']
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column+1)}

    det_c = headers['detail']
    det_en_c = headers['detail_EN']
    phase_c = headers['textPhase']
    phase_en_c = headers['textPhase_EN']
    alt_c = headers['textAlt']
    alt_en_c = headers['textAlt_EN']
    extra_c = headers['textExtra']
    extra_en_c = headers['textExtra_EN']

    d_count, p_count, a_count, e_count = 0, 0, 0, 0

    for r in range(2, ws.max_row+1):
        # detail
        d_en = ws.cell(r, det_en_c).value
        if d_en and str(d_en).strip() in DETAIL_MAP:
            ws.cell(r, det_c, DETAIL_MAP[str(d_en).strip()])
            d_count += 1

        # textPhase
        p_en = ws.cell(r, phase_en_c).value
        if p_en and str(p_en).strip() in PHASE_MAP:
            ws.cell(r, phase_c, PHASE_MAP[str(p_en).strip()])
            p_count += 1

        # textAlt
        a_en = ws.cell(r, alt_en_c).value
        if a_en and str(a_en).strip() in TEXTALT_MAP:
            ws.cell(r, alt_c, TEXTALT_MAP[str(a_en).strip()])
            a_count += 1

        # textExtra
        e_en = ws.cell(r, extra_en_c).value
        if e_en and str(e_en).strip():
            new_val = translate_extra(str(e_en).strip())
            if new_val != str(e_en).strip():
                ws.cell(r, extra_c, new_val)
                e_count += 1

    wb.save(ELEMENT_FILE)
    print(f"Element updated: {d_count} details, {p_count} phases, {a_count} alts, {e_count} extras")

if __name__ == '__main__':
    run()
