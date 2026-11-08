import openpyxl, json, re

def build_phase_map():
    # Load unique phase keys
    unique_phase = json.load(open('scratch/unique_phase_en.json', 'r', encoding='utf-8'))
    
    P = {}
    
    # 1. Direct explicit translations
    explicit = {
        'It is fireproof.': 'È ignifugo.',
        'It is acidproof.': 'È resistente all’acido.',
        'It increases your chance to deliver critical hits.': 'Aumenta la probabilità di mettere a segno colpi critici.',
        'It gives you a chance to throw an absolute piercing attack.': 'Conferisce una probabilità di sferrare un attacco a perforazione assoluta.',
        'It makes your attacks penetrate armors.': 'Permette ai tuoi attacchi di penetrare le armature.',
        'It is imbued with anti-magic particles.': 'È intriso di particelle antimagia.',
        'It increases the damage dealt.': 'Aumenta i danni inflitti.',
        'It makes you a better tactician.': 'Migliora le tue doti tattiche.',
        'It makes you a better marksman.': 'Ti rende un tiratore più abile.',
        'It makes it easier to spot weaknesses.': 'Rende più facile individuare i punti deboli del nemico.',
        'It makes you a better strategist.': 'Migliora la tua capacità strategica.',
        'It makes it easier to evade.': 'Rende più facile schivare gli attacchi.',
        'It makes it easier to anticipate attacks.': 'Rende più facile anticipare le mosse nemiche.',
        'It strengthens your ability to hide.': 'Migliora la tua capacità di muoverti furtivamente.',
        'It makes you a better swimmer.': 'Migliora la tua abilità nel nuoto.',
        'It makes you better at weight lifting.': 'Aumenta la tua capacità di sollevare pesi.',
        'It strengthens your ability to detect objects.': 'Aumenta la tua capacità di percepire oggetti nascosti.',
        'It enhances your mining skill.': 'Incrementa la tua abilità mineraria.',
        'It enhances your lumberjacking skill.': 'Incrementa la tua abilità di disboscamento.',
        'It enhances your ability to ride.': 'Migliora la tua abilità di equitazione.',
        'It enhances your ability to host.': 'Migliora la tua abilità di ospite simbiotico.',
        'It enhances your digging skill.': 'Incrementa la tua abilità di scavo.',
        'It makes you milk better.': 'Migliora la tua abilità nella mungitura.',
        'It makes you understand animals better.': 'Ti fa comprendere meglio gli animali.',
        'It makes you a better traveler.': 'Ti rende un viaggiatore più esperto.',
        'It makes your performance better.': 'Migliora le tue esibizioni musicali.',
        'It makes you a better climber.': 'Migliora la tua abilità di arrampicata.',
        'It makes you a better fisher.': 'Ti rende un pescatore più abile.',
        'It enhances your gathering skill.': 'Incrementa la tua abilità di raccolta.',
        'It makes you a better carpenter.': 'Migliora la tua maestria di falegname.',
        'It makes you a better blacksmith.': 'Migliora la tua maestria di fabbro.',
        'It grants you knowledge of alchemy.': 'Ti conferisce nozioni di alchimia.',
        'It makes you a better sculptor.': 'Migliora la tua abilità di scultore.',
        'It makes you a better jeweler.': 'Migliora la tua abilità di gioielliere.',
        'It makes you a better tailor.': 'Migliora la tua maestria sartoriale.',
        'It makes you a better crafter.': 'Migliora la tua abilità nella fabbricazione.',
        'It grants you the trick of lock picking.': 'Ti conferisce i trucchi dello scassinamento.',
        'It grants you the trick of pickpocketing.': 'Ti conferisce i trucchi del borseggio.',
        'It makes you literate.': 'Ti rende colto e alfabetizzato.',
        'It grants you knowledge of farming.': 'Ti conferisce nozioni di agricoltura.',
        'It enhances your cooking skill.': 'Incrementa la tua abilità culinaria.',
        'It enhances your construction skill.': 'Incrementa la tua abilità costruttiva.',
        'It makes it easier to appraise stuff.': 'Rende più facile periziare e valutare gli oggetti.',
        'It grants you knowledge of anatomy.': 'Ti conferisce nozioni di anatomia.',
        'It grants you knowledge of negotiation.': 'Ti conferisce nozioni di negoziazione.',
        'It grants you knowledge of investing.': 'Ti conferisce nozioni sugli investimenti.',
        'It grants you the trick of disarming traps.': 'Ti conferisce i trucchi per disinnescare trappole.',
        'It accelerates regeneration of body.': 'Accelera la rigenerazione naturale del corpo.',
        'It enhances your meditation.': 'Incrementa la tua meditazione arcana.',
        'It enhances your ability to control magics.': 'Migliora la tua capacità di controllare la magia.',
        'It strengthens your magic capacity.': 'Potenzia la tua capacità di riserva di mana.',
        'It enhances your casting ability.': 'Incrementa la tua capacità di incantamento.',
        'It enhances power of magical devices.': 'Incrementa la potenza dei dispositivi magici.',
        'It makes you pious.': 'Ti rende profondamente pio e devoto.',
        'It enhances your memory.': 'Potenzia la tua memoria arcana.',
        'It allows you to counter when you dodge a melee strike.': 'Ti permette di contrattaccare quando schivi un attacco in mischia.',
        'It strengthens your Shield Bash.': 'Potenzia il tuo Colpo di Scudo.',
        'It strengthens your Rush.': 'Potenzia la tua Carica.',
        'It reflects the blaster bolt back at the shooter.': 'Riflette i colpi energetici contro chi li ha sparati.',
        'It prevents teleportation.': 'Impedisce il teletrasporto.',
        'It makes you float.': 'Ti fa levitare sopra il suolo.',
        'It increases your search range.': 'Aumenta il tuo raggio di perlustrazione.',
        'It accelerates your growth.': 'Accelera la tua crescita ed esperienza.',
        'It reduces the weight of your belongings.': 'Riduce il peso degli oggetti nel tuo inventario.',
        'It slows the process of decay.': 'Rallenta il deterioramento degli alimenti.',
        'It protects you from mutation.': 'Ti protegge dalle mutazioni corporee.',
        'It speeds up your travel progress.': 'Velocizza i tuoi spostamenti durante i viaggi.',
        'It negates the effect of being stranded by bad weather.': 'Annulla gli impedimenti provocati dal maltempo.',
        'It accelerates the progression of the Ether disease.': 'Accelera la progressione della malattia dell’Etere.',
        'It returns to your hand.': 'Ritorna sempre nella tua mano come un boomerang.',
        'It protects you from vampires': 'Ti protegge dagli attacchi dei vampiri.',
        'It protects you from ranged and thrown attacks.': 'Ti protegge da proiettili e armi da lancio.',
        'It prevents lethal attacks from enemies when your health is above half.': 'Previene attacchi letali nemici quando la tua salute supera il 50%.',
        'It enables you to deflect and counter the enemy’s melee attack.': 'Permette di deflettere e contrattaccare gli assalti in mischia nemici.',
        'It intercepts attacks aimed at allies more wounded than you.': 'Intercetta gli attacchi diretti agli alleati più feriti di te.',
        'It forbids enemy retaliation.': 'Impedisce qualsiasi ritorsione nemica.',
        'It sustains your Strength.': 'Sostiene la tua Forza.',
        'It sustains your Endurance.': 'Sostiene la tua Costituzione.',
        'It sustains your Dexterity.': 'Sostiene la tua Destrezza.',
        'It sustains your Perception.': 'Sostiene la tua Percezione.',
        'It sustains your Learning.': 'Sostiene il tuo Apprendimento.',
        'It sustains your Will.': 'Sostiene la tua Volontà.',
        'It sustains your Magic.': 'Sostiene la tua Magia.',
        'It sustains your Charisma.': 'Sostiene il tuo Carisma.',
        'It sustains your body figure.': 'Mantiene inalterata la tua linea corporea.',
        'It inflicts massive damage to dragons.': 'Infligge danni colossali ai draghi.',
        'It inflicts massive damage to undeads.': 'Infligge danni colossali ai non morti.',
        'It inflicts massive damage to fairies.': 'Infligge danni colossali alle fate.',
        'It inflicts massive damage to animals.': 'Infligge danni colossali alle bestie.',
        'It inflicts massive damage to humanoids.': 'Infligge danni colossali agli umanoidi.',
        'It inflicts massive damage to machines.': 'Infligge danni colossali alle macchine.',
        'It inflicts massive damage to gods.': 'Infligge danni colossali alle divinità.',
        'It inflicts massive damage to fishes.': 'Infligge danni colossali alle creature marine.',
        'It inflicts massive damage to all beings.': 'Infligge danni colossali a tutte le creature.',
        'It lets you digest rotten things.': 'Ti consente di digerire senza problemi cibi avariati.',
        'It reveals the faith of others.': 'Rivela la fede religiosa altrui.',
        'It is wielded by the power of the Force.': 'È brandito mediante il potere della Forza.',
        'It reduces your mana consumption.': 'Riduce il consumo di mana.',
        'It can be infused with additional runes.': 'Può essere infuso con rune aggiuntive.',
        'It does not kill the target.': 'Non uccide il bersaglio (attacco non letale).',
        'It disables on-hit effects and other weapon attacks.': 'Disattiva gli effetti all’impatto e altri attacchi d’arma.',
        'It lets you cook creatively.': 'Ti consente di cucinare in modo creativo.',
        'It screams in its death throes.': 'Emette urla raccapriccianti nella sua agonia mortale.',
        'It mesmerizes the audience.': 'Ammalia e incanta il pubblico.',
        'It allows you to see farther.': 'Ti permette di vedere a distanze maggiori.',
        'It protects you from gravity.': 'Ti protegge dagli effetti della gravità opprimente.',
        'It gives you experience every time you walk.': 'Ti conferisce esperienza a ogni passo che compi.',
        'It protects you from effects that hinder movement.': 'Ti protegge da effetti che ostacolano il movimento.',
        'It prolongs the effects of sentences.': 'Prolunga la durata delle sentenze.',
        'It makes it easier to ride you.': 'Rende più facile farsi cavalcare da altri.',
        'It absorbs mana.': 'Assorbe mana.',
        'It absorbs stamina.': 'Assorbe vigore.',
        'It doubles your luck.': 'Raddoppia la tua fortuna.',
        'It upgrades machines.': 'Aggiorna e potenzia i macchinari.',
        'It replants the harvested life.': 'Ripianta la vita mietuta.',
        'It can attack distant targets.': 'Può colpire bersagli distanti.',
        'It heralds the end.': 'Preannuncia la fine dei tempi.',
        'It is burning.': 'È fiammeggiante.',
        'It is freezing.': 'È congelante.',
        'It is electrified.': 'È elettrificato.',
        'You don\'t get hurt.': 'Non subisci alcun danno.',
        'You have gigantic scissors.': 'Possiedi chele gigantesche.',
        'You are guided by fate.': 'Sei guidato dal fato.',
        'You wear thorns to protect yourself.': 'Indossi spine aguzze per proteggerti.',
        'You split.': 'Ti scindi.',
        'Your blood is acidic.': 'Il tuo sangue è altamente corrosivo.',
        'You are guarded by the spirit of ice.': 'Sei protetto dallo spirito del ghiaccio.',
        'Your loyalty is deep.': 'La tua devozione e lealtà sono profonde.',
        'You are adapted to life in the dark underworld.': 'Sei adattato alla vita nell’oscuro sottosuolo.',
        'You are servant of God.': 'Sei un servo del Signore.',
        'You are of an elder race.': 'Appartieni a una stirpe primordiale.',
        'You are demon.': 'Sei un demone.',
        'You are the leader of the pack.': 'Sei il capobranco.',
        'You interpose thick flesh to stop the strike.': 'Interponi la tua spessa carne per fermare i colpi.',
        'You carry hidden potential.': 'Custodisci un potenziale sopito.',
        'You are eternally young.': 'Sei eternamente giovane.',
        'You are watched over by Sagittarius.': 'Sei vegliato dalla costellazione del Sagittario.',
        'You hold a cosmos inside your heart.': 'Custodisci un cosmo infinito nel tuo cuore.',
        'You are watched over by Pegasus.': 'Sei vegliato dalla costellazione di Pegaso.',
        'You are watched over by Libra.': 'Sei vegliato dalla costellazione della Bilancia.',
        'You are a miscreation.': 'Sei un abominio ripugnante.',
        'You transfer your pain to your ally.': 'Trasferisci il tuo dolore al tuo alleato.',
        'You reign over the night.': 'Regni sovrano sulla notte.',
        'You turn to ash in sunlight.': 'Ti riduci in cenere alla luce del sole.',
        'You can move swiftly through water.': 'Ti muovi fulmineo attraverso l’acqua.',
        'You are watched over by Cancer.': 'Sei vegliato dalla costellazione del Cancro.',
        'You split when getting wet.': 'Ti scindi quando ti bagni d’acqua.',
        'You are good.': 'Il tuo allineamento morale è buono.',
        'You are evil.': 'Il tuo allineamento morale è malvagio.',
        'You step in when your companions fall out.': 'Intervieni per pacificare i tuoi compagni quando litigano.',
        'You are blessed by God.': 'Sei benedetto dal Dio.',
        'You are blessed by Goddess.': 'Sei benedetta dalla Dea.',
        'You are skilled in handling weapons.': 'Sei maestro nell’impugnare le armi.',
        'You have luck on your side.': 'Hai la dea bendata dalla tua parte.',
        'You have knowledge of magic.': 'Possiedi una profonda conoscenza magica.',
        'Your legs and hips are well-trained.': 'Le tue gambe e fianchi sono ben temprati.',
        'You are proficient in shooting.': 'Sei straordinariamente abile nel tiro.',
        'You have a sense of music.': 'Possiedi un innato senso musicale.',
        'You are always in a sightseeing mood.': 'Sei costantemente in vena di turismo.',
        'You are devout.': 'Sei profondamente devoto.',
        'You take pleasure in killing.': 'Provi piacere nell’uccidere.',
        'You take on a thousand forms.': 'Assumi mille forme e volti diversi.',
        'Your body passes through walls.': 'Il tuo corpo è incorporeo e oltrepassa i muri.',
        'Your presence is overwhelming.': 'La tua presenza incute timore ed è travolgente.',
        'Your skin is hard.\nYour skin is very hard.\nYour skin is as hard as iron.': 'La tua pelle è dura.\nLa tua pelle è molto dura.\nLa tua pelle è dura come il ferro.',
        'Your skin is white.\nYour skin is fragile.\nYour skin is collapsing.': 'La tua pelle è candida.\nLa tua pelle è fragile.\nLa tua pelle si sta sgretolando.',
        'You have the eyes of a cat.\nYou have the eyes of a hawk.': 'Hai gli occhi di un gatto.\nHai gli occhi di un falco.',
        'You are partially color-blind.\nYou are blind in one eye.': 'Sei parzialmente daltonico.\nSei cieco da un occhio.',
        'Your joints are flexible.\nYour joints are very flexible.\nYour joints are incredibly flexible.': 'Le tue articolazioni sono flessibili.\nLe tue articolazioni sono molto flessibili.\nLe tue articolazioni sono incredibilmente flessibili.',
        'Your joints creak.\nYou are worrying about your joint creakings.\nYou have terrible joint creakings.': 'Le tue articolazioni scricchiolano.\nTi preoccupi per gli scricchiolii articolari.\nHai terribili scricchiolii articolari.',
        'Your wounds regenerate rapidly.\nYour wounds regenerate instantly.': 'Le tue ferite guariscono rapidamente.\nLe tue ferite guariscono all’istante.',
        'You suffer from anemia.\nYou constantly have an attack of anemia.': 'Soffri di anemia.\nHai continui attacchi di anemia.',
        'You have lithe legs.\nYou have very lithe legs.\nYou have ideal legs.': 'Hai gambe scattanti.\nHai gambe molto scattanti.\nHai gambe perfette.',
        'Your legs are twisted.\nYour legs are very twisted.\nYour legs are broken.': 'Le tue gambe sono storte.\nLe tue gambe sono molto storte.\nLe tue gambe sono spezzate.',
        'You have well-knit arms.\nYou have well-muscled arms.\nYou have ideal arms.': 'Hai braccia ben formate.\nHai braccia muscolose.\nHai braccia ideali.',
        'Your arms are thin.\nYour arms are very thin.\nYour arms are just decorative.': 'Le tue braccia sono esili.\nLe tue braccia sono sottilissime.\nLe tue braccia sono puramente decorative.',
        'Your voice is sweet.\nYour voice charms everyone.': 'La tua voce è soave.\nLa tua voce ammalia chiunque.',
        'Your voice is husky.\nEveryone is frightened when you talk.': 'La tua voce è rauca.\nTutti sono spaventati quando parli.',
        'Your brain is mechanized.\nYour brain is fully mechanized.': 'Il tuo cervello è meccanizzato.\nIl tuo cervello è completamente meccanizzato.',
        'You are stupid.\nYou are really stupid.': 'Sei stupido.\nSei davvero stupido.',
        'You generate gravity.\nYou generate heavy gravity.\nYou generate massive gravity.': 'Generi gravità.\nGeneri una forte gravità.\nGeneri una gravità colossale.',
        'You have sores on your face.\nYour face is ulcerate.\nYour face is crumbling.': 'Hai piaghe sul viso.\nIl tuo volto è ulcerato.\nIl tuo volto si sta decomponendo.',
        'You have 3 eyes.\nYou have 4 eyes.': 'Hai 3 occhi.\nHai 4 occhi.',
        'You have grown a single feather.\nYou have grown dual feathers.': 'Ti è spuntata una piuma.\nTi sono spuntate due piume.',
        'Your feet transformed into hooves.': 'I tuoi piedi si sono trasformati in zoccoli.',
        'Your neck is extremely thick.': 'Il tuo collo è mostruosamente tozzo.',
        'Desire for violence arises within you.': 'Un desiderio incontrollabile di violenza sorge dentro di te.',
        'Your head has grown huge.': 'La tua testa è cresciuta a dismisura.',
        'Clouds of rain follow you.': 'Nubi temporalesche ti seguono ovunque.',
        'You are addicted to potion.': 'Sei schiavo della dipendenza da pozioni.',
        'You suffer debilitation.': 'Soffri di una debilitazione debilitante.',
        'You have dementia.': 'Sei affetto da demenza senile.',
        'You are covered with heavy carapace.': 'Sei ricoperto da un pesante carapace.',
        'A blasphemous horn grows from your head.': 'Un corno blasfemo cresce dalla tua fronte.',
        'You are a living mana battery.': 'Sei una batteria di mana vivente.',
        'Poison drips from your hands.': 'Gocce di veleno stillano continuamente dalle tue mani.'
    }
    P.update(explicit)

    # 2. General fallbacks / pattern translators for any remaining keys
    for k, info in unique_phase.items():
        if k in P: continue
        
        # Check patterns
        t = k
        # "It protects you from X"
        m = re.match(r'^It protects you from (.+)\.$', k, re.I)
        if m:
            target = m.group(1).lower()
            P[k] = f'Ti protegge da {target}.'
            continue
            
        # "It sustains your X"
        m = re.match(r'^It sustains your (.+)\.$', k, re.I)
        if m:
            stat = m.group(1)
            P[k] = f'Sostiene {stat}.'
            continue

        # "It makes you a better X"
        m = re.match(r'^It makes you a better (.+)\.$', k, re.I)
        if m:
            role = m.group(1)
            P[k] = f'Migliora la tua abilità come {role}.'
            continue

        # "It enhances your X"
        m = re.match(r'^It enhances your (.+)\.$', k, re.I)
        if m:
            sk = m.group(1)
            P[k] = f'Incrementa la tua abilità di {sk}.'
            continue

        # "It inflicts massive damage to X"
        m = re.match(r'^It inflicts massive damage to (.+)\.$', k, re.I)
        if m:
            race = m.group(1)
            P[k] = f'Infligge danni colossali a {race}.'
            continue

        # "You are X"
        m = re.match(r'^You are (.+)\.$', k, re.I)
        if m:
            desc = m.group(1)
            P[k] = f'Sei {desc}.'
            continue

        # Default fallback
        P[k] = k

    return P

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/Element.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    P = build_phase_map()
    count = 0

    for r in range(2, ws.max_row+1):
        ev = ws.cell(row=r, column=headers['textPhase_EN']).value
        if ev:
            k = str(ev).strip()
            if k in P:
                ws.cell(row=r, column=headers['textPhase']).value = P[k]
                count += 1
            elif str(ev) in P:
                ws.cell(row=r, column=headers['textPhase']).value = P[str(ev)]
                count += 1

    wb.save('Lang/IT/Game/Element.xlsx')
    print(f'Applied {count} textPhase translations to Element.xlsx')

if __name__ == '__main__':
    run()
