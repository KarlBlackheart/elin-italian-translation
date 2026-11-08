"""
Elin Italian Localization - Game.xlsx Full Localizer
Traduzione e localizzazione completa di tutti i messaggi di log, eventi di gioco,
combattimento, sopravvivenza, divinita', dungeon crawling e interazioni di Game.xlsx.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GAME_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Game', 'Game.xlsx')

GAME_TEXTS = {
    # -------------------------------------------------------------
    # Meteo & Atmosfera
    # -------------------------------------------------------------
    "weather_Rain": "Comincia a piovere.",
    "weather_RainHeavy": "Piove a dirotto!",
    "weather_Storm": "Una tempesta si sta avvicinando!",
    "weather_Snow": "Inizia a nevicare.",
    "weather_SnowHeavy": "Si abbatte una furiosa bufera di neve!",
    "weather_Cloudy": "Il cielo si fa cupo e minaccioso.",
    "weather_Ether": "L'aria comincia a riempirsi di letale Etere!",
    "weather_Fine": "Il cielo torna sereno.",
    "welcome_intro": "Lafrontier presenta: Elin versione #1",
    "welcome": "Benvenuto, viandante! Premi '?' per aprire la guida di gioco.",
    "endDay": "Trascorre un giorno...",
    "startSiege": "L'assedio ha inizio!",
    "endSiege": "L'assedio è terminato.",
    "saved": "*Partita Salvata*",
    "tutorial_added": "Nuova voce aggiunta al Registro delle Avventure.",
    "story_added": "Un nuovo capitolo di storia è stato sbloccato.",
    "earthquake": "ROOOMBOOOO…",
    "guestArrive": "#1 è arrivato in visita.",

    # -------------------------------------------------------------
    # Azioni di Base & Abilità
    # -------------------------------------------------------------
    "stack_thing": "Unisci #1 a #2.",
    "pick_thing": "#1 raccoglie #2.",
    "pick_thing_pc": "Raccogli #2.",
    "pick_held": "#1 ripone #2 nello zaino.",
    "pick_held_pc": "Riponi #2 nel tuo zaino.",
    "backpack_full": "Non c'è più spazio nel tuo zaino!",
    "backpack_full_drop": "#1 trabocca dallo zaino e cade a terra.",
    "ding_skill": "La tua abilità in #2 è aumentata!",
    "dec_skill": "#1 avverte un declino nella propria abilità in #2.",
    "kick": "#1 sferra un calcio a #2.",
    "bash": "#1 carica con violenza #2.",
    "cooked": "#1 è stato cotto alla perfezione.",
    "massage_start": "#1 comincia a massaggiare le spalle di #2.",
    "massage_end": "#1 termina il massaggio.",
    "armpillow_start": "#1 posa delicatamente la testa sul braccio di #2.",
    "armpillow_end": "#1 si scosta dolcemente dal braccio di #2.",
    "selfHarm_start": "#1 comincia a ferirsi da solo!",
    "selfHarm_end": "#1 riprende finalmente i sensi.",
    "meditate_start": "#1 si siede e chiude gli occhi per meditare.",
    "meditate_end": "#1 conclude la meditazione e si rialza.",
    "passTime_start": "#1 comincia a sognare a occhi aperti...",

    # -------------------------------------------------------------
    # Lavoro manuale, Raccolta & Artigianato
    # -------------------------------------------------------------
    "drawWater_start": "#1 inizia ad attingere acqua in #2.",
    "pourWater_start": "#1 comincia a versare l'acqua di #2 sul terreno.",
    "chopwood_start": "#1 inizia a spaccare #2.",
    "till_start": "#1 inizia a dissodare il terreno con #2.",
    "till_invalid": "Non puoi dissodare questo tipo di pavimento.",
    "disassemble_start": "#1 inizia a smantellare #3 con #2.",
    "harvest_start": "#1 inizia a raccogliere #3 usando #2.",
    "harvestHand_start": "#1 inizia a raccogliere #2 a mani nude.",
    "harvestHand_start_pc": "Inizi a raccogliere #2 a mani nude.",

    # -------------------------------------------------------------
    # Cibo, Fame & Bisogni
    # -------------------------------------------------------------
    "not_hungry": "Non hai ancora abbastanza fame.",
    "eat_start": "#1 porta #2 alla bocca...",
    "eat_end": "#1 finisce di mangiare #2.",
    "eat_full": "Sei troppo sazio per mandare giù anche un solo boccone!",
    "eat_poison": "Era avvelenato! #1 si contorce in preda a spasmi violenti!",
    "slime_start": "#1 ingloba #2 nel proprio corpo.",
    "suck_start": "#1 affonda i denti nel collo di #2!",
    "fuck_start": "#1 inizia a togliersi gli indumenti...",
    "tame_start": "#1 comincia a strigliare #2 con una spazzola.",
    "tame_end": "#1 appare pulito e rinvigorito.",
    "brush_success": "#1 sembra molto felice delle cure.",
    "brush_fail": "#1 ti lancia un'occhiata carica di scontento.",
    "tame_success": "Hai addomesticato con successo #2!",
    "tame_fail": "Il tentativo di addomesticare #2 è fallito.",
    "tame_send": "#1 si mette in viaggio verso #2.",

    # -------------------------------------------------------------
    # Scasso, Furto & Segreti
    # -------------------------------------------------------------
    "lockpick_start": "#1 inizia a scassinare #2.",
    "lockpick_start_pick": "Inizi a scassinare #2 usando #1.",
    "lockpick_end": "#1 rinuncia a scassinare #2.",
    "lockpick_success": "#1 riesce a scassinare la serratura di #2!",
    "pry_damage": "Si ode un sinistro scricchiolio di rottura...",
    "pry_start": "#1 tenta di forzare #2 facendo leva.",
    "pry_end": "#1 rinuncia a forzare #2.",
    "pry_success": "#1 spalanca #2 con la forza bruta!",
    "drink": "#1 beve un sorso di #2.",
    "steal_chara_nothing": "Sembra che #2 non abbia nulla da rubare.",
    "steal_chara": "#1 cerca l'attimo fuggente per borseggiare #2.",
    "steal_thing": "#1 adocchia l'occasione per sottrarre #2.",
    "steal_invalid": "Non è possibile rubarlo.",
    "steal_end": "#1 ruba #2 con destrezza!",
    "steal_container": "Sottrai #2 da #1 senza farti notare!",
    "shear_start": "#1 comincia a tosare la lana di #2.",
    "shear_end": "#1 tosa #3 da #2.",
    "shear_penalty": "Non è possibile tosare lana di qualità da questa creatura.",

    # -------------------------------------------------------------
    # Gestione Oggetti, Lettura & Luce
    # -------------------------------------------------------------
    "claimRoom": "#1 rivendica il diritto di proprietà su questa stanza.",
    "getItem": "Hai ottenuto: #1.",
    "useItem": "Hai utilizzato #1.",
    "tutorialStart": "Un nuovo capitolo di guida è stato sbloccato.",
    "dropItem": "Riponi #1 a terra.",
    "read": "#1 legge #2.",
    "read_start": "#1 apre e comincia a leggere #2...",
    "read_end": "#1 termina la lettura di #2.",
    "tooDark": "È calata l'oscurità totale: non si vede un palmo dal naso!",
    "torch_start": "Accendi la fiamma di #2.",
    "torch_end": "La tua torcia si è consumata del tutto.",
    "rot": "#1 si decompone e va a male.",
    "rotInv": "#1 dentro il tuo zaino è marcito!",
    "rottingInv": "#1 nello zaino sta cominciando a marcire...",
    "diebye": "Addio, mondo crudele... Quali sono le tue ultime parole?",

    # -------------------------------------------------------------
    # Diario, Missioni & Fama
    # -------------------------------------------------------------
    "journalUpdate": "Il tuo diario è stato aggiornato.",
    "journalUpdate2": "La voce di diario \"#1\" è stata aggiornata.",
    "questExpired": "La missione \"#1\" è scaduta. Incarico fallito!",
    "questAbandon": "Hai abbandonato la missione \"#1\".",
    "gainFameLimit": "Con la tua licenza attuale non puoi accumulare ulteriore fama.",
    "gainFame": "Hai guadagnato #1 punti fama.",
    "looseFame": "Hai perso #1 punti fama.",
    "claimedZone": "Hai preso possesso di questo territorio!",
    "invalidClaimZone": "Questo territorio non può essere rivendicato.",

    # -------------------------------------------------------------
    # Religione, Altari & Divinita'
    # -------------------------------------------------------------
    "worship": "Hai giurato fedeltà a #1, diventandone seguace.",
    "worship2": "Hai rinnegato la tua fede.",
    "worship3": "#2 riceve la solenne protezione di #1.",
    "god_offer": "Deponi #2 sull'altare offrendolo in sacrificio a #1.",
    "god_offerEyth": "Non credi in alcun dio: l'altare resta inerte.",
    "god_offer1": "#1 brilla di una luce accecante e svanisce nel nulla!",
    "god_offer2": "#1 risplende un istante e sparisce, mentre piove un quadrifoglio benedetto.",
    "god_offer3": "#1 risplende per un breve momento e si dissolve.",
    "god_offer4": "#1 scompare in un soffio.",
    "god_limitPiety": "La tua divinità non mostra più interesse per le tue offerte terrene.",
    "hire": "#1 accetta la tua proposta e si unisce a te!",
    "identified": "#1 viene identificato: si tratta di #2.",
    "identified2": "#1 necessita di un'identificazione magica di livello superiore.",
    "identified3": "Intuisci che #1 nel tuo zaino potrebbe essere #3.",

    # -------------------------------------------------------------
    # Combattimento: Azioni, Incantesimi & Schivate
    # -------------------------------------------------------------
    "cast": "#1 lancia l'incantesimo #2#3.",
    "cast_hand_ally": "#1 tocca #2 con la propria #3.",
    "cast_hand": "#1 tocca #2 con la propria #3.",
    "castSpider": "#1 sputa una fitta ragnatela#3!",
    "castSpill": "#1 schizza disgustosi fluidi corporei#3!",
    "castTentacle": "#1 protende un orrido tentacolo#3!",
    "castGaze": "#1 lancia uno sguardo agghiacciante#3!",
    "castSpore": "#1 soffia via una nube di spore#3!",
    "castMachine": "#1 vibra emettendo un ronzio metallico#3.",
    "cast_silence": "La nebbia del silenzio soffoca la voce, impedendo l'incantesimo!",
    "gaze_dim": "#1 fissa minacciosamente #2 negli occhi.",
    "gaze_insane": "#2 vede orribili vermi pullulare dalle carni lacerate di #1.\n#2 scorge #1 mentre divora con foga membra putrefatte.\n#2 trema d'orrore dinanzi allo sguardo raccapricciante di #1.\n#2 viene colto dalla nausea vedendo viscere contorte tra i tentacoli di #1.",
    "gaze_insult": "#1 copre #2 di insulti sfacciati!",
    "a_drop_mine": "#1 sotterra con cura una mina esplosiva nel terreno.",
    "a_scream": "#1 lancia un grido straziante!",
    "a_drain_blood": "#1 morde e risucchia avidamente il sangue di #2!",
    "spell_sword_hit": "#1 fende #2 con una spada di #3!",
    "spell_hand_miss": "#1 agita la mano ma afferra solo aria vuota.",
    "spell_spear": "#1 scaglia una lancia di #2!",
    "spell_spear_hit": "La lancia di energia trafigge #2!",
    "spell_arrow": "#1 scocca una freccia di #2!",
    "spell_arrow_hit": "La freccia colpisce in pieno #2!",
    "spell_funnel": "#1 evoca e materializza un'arma di #2!",
    "spell_breathe": "#1 esala un tremendo soffio di #2!",
    "spell_breathe_hit": "Il soffio travolge #2 in pieno!",
    "spell_ball": "#1 scatena una sfera vorticosa di #2!",
    "spell_ball_hit": "Il vortice inghiotte ed esplode contro #2!",
    "spell_bolt": "#1 lancia un fulmineo dardo di #2!",
    "spell_bolt_hit": "Il dardo energetico perfora #2 da parte a parte!",
    "spell_earthquake": "#1 sprigiona una possente onda d'urto di #2!",
    "spell_earthquake_hit": "L'onda sismica squassa e travolge #2!",
    "suicide_hit": "#2 viene investito dalla furia dell'esplosione!",
    "evade": "#1 schiva l'attacco di #2.",
    "evade_pc": "Schivi agilmente l'attacco di #2.",
    "evadePlus": "#1 evita l'attacco di #2 con una maestosa acrobazia!",
    "evadePlus_pc": "Eviti l'attacco di #2 con straordinaria maestria!",
    "evade2": "L'attacco di #1 va a vuoto!",
    "evade2_pc": "Il tuo attacco contro #2 va a vuoto!",
    "evadePlus2": "#1 manca miseramente #2, che si fa beffe del colpo!",
    "evadePlus2_pc": "#2 elude il tuo colpo con sconcertante facilità!",
    "attackMeleeToPC": "#1 #3 contro di te e",
    "attackMelee": "#1 #3 contro #2 e",
    "attackMelee_pc": "Attacchi #2 con #3 e",
    "attack_air": "Il fendente di #1 squarcia soltanto l'aria.",
    "attack_air_range": "Il tiro di #1 vola via nel vuoto.",

    # -------------------------------------------------------------
    # Gradi di Danno Fisico & Elementale
    # -------------------------------------------------------------
    "dmgMelee0": " infligge un graffio superficiale.",
    "dmgMelee1": " ferisce lievemente #him2.",
    "dmgMelee2": " infligge una discreta ferita a #him2.",
    "dmgMelee3": " ferisce gravemente #him2!",
    "dmgMelee4": " infligge un colpo micidiale e devastante a #him2!",
    "dmgMelee5": " riduce #him2 a un passo dalla morte!",
    "dmgMelee0pc": " subisci un graffio di poco conto.",
    "dmgMelee1pc": " riporti una ferita lieve.",
    "dmgMelee2pc": " vieni ferito in modo evidente.",
    "dmgMelee3pc": " subisci una ferita profonda e dolorosa!",
    "dmgMelee4pc": " incassi un colpo critico devastante!",
    "dmgMelee5pc": " vieni ridotto a un soffio dalla tomba!",
    "dmg1": "#1 riporta una ferita lieve.",
    "dmg2": "#1 incassa un colpo doloroso.",
    "dmg3": "#1 si contorce dal dolore straziante!",
    "dmg4": "#1 caccia un urlo disperato per l'agonia!",
    "dmg5": "#1 urla disperatamente, invocando pietà!",
    "dmg_eleFire": "#1 prende fuoco e arde vivamente!",
    "dmg_eleCold": "#1 batte i denti ed è quasi congelato!",
    "dmg_eleLightning": "#1 viene attraversato da violente scariche elettriche!",
    "dmg_eleDarkness": "Le ombre corrodono la carne di #1.",
    "dmg_eleHoly": "#1 viene purificato e ustionato dalla luce radiosa!",
    "dmg_eleMind": "La mente di #1 viene invasa dalla follia!",
    "dmg_elePoison": "#1 trema, sopraffatto dal veleno nelle vene.",
    "dmg_eleNether": "Il freddo tombale degli inferi gela le ossa di #1.",
    "dmg_eleSound": "Un'onda sonica perfora i timpani di #1!",
    "dmg_eleNerve": "I nervi di #1 sono scossi da spasmi convulsi.",
    "dmg_eleChaos": "L'energia caotica sconvolge le fibre di #1!",
    "dmg_eleAcid": "L'acido sfrigola e corrode le carni di #1!",
    "dmg_eleCut": "Lame invisibili dilaniano #1 facendolo sanguinare copiosamente!",
    "dmg_eleMagic": "La pura forza magica scaraventa via #1!",
    "dmg_eleEther": "L'essenza vitale di #1 vacilla sotto l'effetto dell'Etere!",

    # -------------------------------------------------------------
    # Morti, Uccisioni & Necrologi
    # -------------------------------------------------------------
    "kill_attack": " fa a pezzi #him2!\n pone fine all'esistenza di #him2.\n riduce #him2 a un cumulo informe di carne macinata.\n distrugge senza pietà #him2.",
    "kill_eleFire": " riduce #him2 a un mucchietto di cenere.\n carbonizza #him2 all'istante!",
    "kill_eleCold": " tramuta #him2 in una scultura di ghiaccio perenne.",
    "kill_eleLightning": " folgora a morte #him2 riducendolo a un tizzone.",
    "kill_eleDarkness": " fa sprofondare #him2 nell'eterna oscurità.",
    "kill_eleHoly": " purifica l'anima di #him2 facendolo ascendere al cielo.",
    "kill_eleMind": " manda in frantumi il cervello di #him2, rendendolo un guscio vuoto.",
    "kill_elePoison": " spegne la vita di #him2 con un letale veleno.",
    "kill_eleNether": " trascina l'anima dannata di #him2 negli abissi dell'oltretomba.",
    "kill_eleSound": " polverizza #him2 con un'onda sonica d'urto inaudita.",
    "kill_eleNerve": " distrugge l'intero sistema nervoso di #him2.",
    "kill_eleChaos": " lascia che il caos primordiale divori #him2.",
    "kill_eleAcid": " scioglie completamente le carni di #him2 in un fango acido.",
    "kill_eleCut": " affetta #him2 a striscioline sottili!",
    "kill_eleMagic": " prosciuga ogni residuo di mana vitale da #him2.",
    "kill_eleEther": " dissolve la materia di #him2 nella tempesta di etere.",
    "dead_in": " a #1",
    "dead_by": "#1 è caduto per mano di #3#2.",
    "dead": "#1 è spirato#2.",
    "dead_attack": "#1 è stato trucidato#2.",
    "dead_eleFire": "#1 è stato arso fino a ridursi in cenere#2.",
    "dead_eleCold": "#1 è stato congelato diventando una statua di ghiaccio#2.",
    "dead_eleLightning": "#1 è stato folgorato da una scarica di fulmini#2.",
    "dead_eleDarkness": "#1 è stato inghiottito dall'oscurità più cupa#2.",
    "dead_eleHoly": "#1 è volato in paradiso#2.",
    "dead_eleMind": "#1 ha perso la ragione e si è tolto la vita#2.\n#1 è impazzito e si è ucciso#2.",
    "dead_elePoison": "#1 è morto tra atroci tormenti per avvelenamento#2.",
    "dead_eleNether": "#1 è precipitato negli oscuri recessi degli inferi#2.",
    "dead_eleSound": "#1 è andato in pezzi sotto la potenza delle onde sonore#2.",
    "dead_eleNerve": "#1 è morto per il collasso del sistema nervoso#2.",
    "dead_eleChaos": "#1 è stato assorbito nel vortice del caos#2.",
    "dead_eleAcid": "#1 si è sciolto come cera sotto l'azione dell'acido#2.",
    "dead_eleCut": "#1 è stato ridotto a strisce sottili#2.",
    "dead_eleMagic": "#1 è stato incenerito dal sovraccarico magico#2.",
    "dead_eleEther": "#1 è annegato nella fiumana tossica di etere#2.",
    "dead_mana": "#1 è esploso per il sovraccarico di mana incanalato#2.",
    "dead_Hunger": "#1 è morto di inedia e fame nera#2.",
    "dead_Fatigue": "#1 è crollato stecchito per lo sfinimento e la fatica estrema#2.",
    "dead_Hang": "#1 si è impiccato per porre fine ai suoi tormenti#2.",
    "dead_Wrath": "#1 è stato polverizzato dall'ira divina di #3#2.",
    "dead_Burden": "#1 è rimasto schiacciato sotto la mole del proprio bagaglio#2.",
    "dead_Fall": "#1 è precipitato nel baratro ed è morto sul colpo#2.",
    "dead_BurdenStairs": "#1 è ruzzolato giù per le scale finendo con il collo spezzato#2.",
    "dead_BurdenFallDown": "#1 è inciampato rovinosamente a terra perdendo la vita#2.",
    "vopal": "*sferzata vorpal!*",
    "curse": "#1 punta il dito contro #2 biascicando un'antica maledizione...",
    "curse_nullify": "Una fervida preghiera dissolve e annulla la maledizione!",
    "finish": "*ZAC!*",
    "finish2": "#1 mozza di netto la testa di #2!",

    # -------------------------------------------------------------
    # Trappole, Sonno, Risveglio & Dungeon
    # -------------------------------------------------------------
    "trap_trigger": "#1 fa scattare una trappola!",
    "trap_disarm": "#1 disinnesca con successo la trappola.",
    "trap_disarm_fail": "#1 fallisce il disinnesco della trappola!",
    "stairs_down": "Scendi con cautela le scale verso il livello inferiore.",
    "stairs_up": "Sali le scale tornando verso la superficie.",
    "chest_open": "Apri il forziere...",
    "chest_empty": "Il forziere è desolatamente vuoto.",
    "ether_corrupt": "L'etere muta il tuo corpo: avverti i primi sintomi del Morbo dell'Etere!",
    "fainting": "Gli occhi ti si annebbiano e perdi i sensi per lo sfinimento...",
}

def apply():
    print(f"Caricamento di {GAME_FILE}...")
    wb = openpyxl.load_workbook(GAME_FILE)
    ws = wb.active

    headers = {}
    for c in range(1, ws.max_column + 1):
        v = ws.cell(row=1, column=c).value
        if v:
            headers[str(v).strip()] = c

    id_c = headers.get('id', 1)
    text_c = headers.get('text', 4)

    translated = 0
    for r in range(2, ws.max_row + 1):
        rid = ws.cell(row=r, column=id_c).value
        if rid:
            rid_str = str(rid).strip()
            if rid_str in GAME_TEXTS:
                ws.cell(row=r, column=text_c, value=GAME_TEXTS[rid_str])
                translated += 1

    wb.save(GAME_FILE)
    print(f"[OK] Applicate {translated} localizzazioni approfondite a Game.xlsx!")

if __name__ == '__main__':
    apply()
