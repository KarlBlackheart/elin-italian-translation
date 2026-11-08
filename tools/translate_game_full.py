# coding: utf-8
"""
Elin Italian Localization - Game.xlsx Full Localizer
Translates notifications, logs, interactions, economy, travel, and combat prompts.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GAME_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Game', 'Game.xlsx')

GAME_DICT = {
    "temp": "Messaggio temporale.",
    "passTime_end": "#1 si ridesta dalle sue fantasticherie.",
    "zoneNoEntrance": "Non puoi entrare nella zona da questo punto.",
    "materialChanged": "#1 si tramuta in #2.",
    "drinkGood": "Delizioso!",
    "drinkRamune": "*fizz*",
    "drinkMilk": "Il sapore è denso e cremoso.",
    "drinkSaltWater": "Che schifo! È acqua salata.",
    "drinkSaltWater_snail": "È sale puro! #1 comincia a sciogliersi all'istante!",
    "drinkWell": "#1 beve l'acqua da #2.",
    "drinkWater_clear": "Fiuu, quest'acqua è limpida e dissetante!",
    "drinkWater_dirty": "Che ribrezzo! Quest'acqua è putrida e contaminata!",
    "drinkWell_empty": "#2 è completamente prosciugato.",
    "drinkWell_dry": "#2 si prosciuga del tutto.",
    "mapCrumble": "#1 si sbriciola in polvere non appena lo tocchi.",
    "spellbookCrumble": "#1 si disfa completamente tra le tue dita.",
    "tooHeavy": "#1 è troppo pesante per essere sollevato.",
    "sold": "Vendi #1 per #2.",
    "bought": "Compri #1 per #2.",
    "get_quest_item": "Ricevi l'oggetto della missione.",
    "completeQuest": "Hai completato la missione \"#1\"!",
    "dropReward": "Qualcosa viene posato sul terreno.",
    "dropRewardAir": "Qualcosa piove dal cielo davanti a te!",
    "upgradeLoytelMart": "L'Emporio di Loytel è stato ampliato e migliorato.",
    "noSpellStock": "Le cariche magiche dell'incantesimo sono esaurite.",
    "deliverItem": "Consegni #1.",
    "notSleepy": "Non hai affatto sonno.",
    "notEnoughMoney": "Non hai abbastanza denaro.",
    "notEnoughTicket": "Non hai abbastanza biglietti.",
    "notEnoughInfluence": "Non hai abbastanza influenza politica.",
    "notEnoughFood": "Non hai abbastanza razioni da viaggio.",
    "payBill": "Paghi #1.",
    "depositMoney": "Depositi #1 in #2.",
    "travel": "Sono trascorsi #3 giorn#(i) e #4 or#(e) da quando hai lasciato #1.",
    "travel2": "#2 ha percorso circa #1 miglia guadagnando preziosa esperienza.",
    "regionAbortMove": "Percepisci un pericolo mortale e interrompi la marcia.",
    "noLogForTorch": "Non possiedi la risorsa richiesta.",
    "crawlup": "Riesci faticosamente a issarti verso l'alto.",
    "overWeightLimit": "#1 è troppo pesante per essere inserito.",
    "crafted": "Hai fabbricato #1.",
    "disassembled": "Hai smantellato #1.",
    "installed": "Hai posizionato #1.",
    "movedToEquip": "Prendi #1 da #2 e lo indossi.",
    "equip": "#1 equipaggia #2.",
    "book_secret": "<i>Riceverai la tua giusta ricompensa...</i>",
    "book_secret2": "<i>Sei giunto... al tuo limite estremo...</i>",
    "dingExp": "#1 guadagna punti esperienza.",
    "errorWrongType": "Questo tipo di oggetto non può essere riposto in questo contenitore.",
    "errorOverweight": "Il contenitore è sovraccarico.",
    "errorOverweightTravel": "Sei troppo appesantito per intraprendere questo viaggio!",
    "fuelFull": "Il serbatoio di combustibile è già completamente pieno.",
    "reserveLimit": "La pietra del focolare non ha più spazio per altri residenti.",
    "returnBegin": "L'aria attorno a te si comprime in una densa vibrazione arcana...",
    "returnNowhere": "Non conosci alcun rifugio verso cui fare ritorno da qui.",
    "returnAbort": "La tensione nell'aria si allenta e si dissipa.",
    "returnOverweight": "Una voce tuona dall'etere: \"Spiacente, sei troppo pesante!\"",
    "tooHeavyToMove": "Sei completamente schiacciato dal peso insostenibile!",
    "returnFail": "Senti come se una mano spettrale ti stringesse la gola, vanificando l'incanto.",
    "returnComplete": "Una prodigiosa forza di risucchio ti solleva e ti trasporta!",
    "bills": "Hai #1 cartell#(e) esattorial#(i) in sospeso non pagat#(e).",
    "getBill": "Ti è stata recapitata una cartella esattoriale di #1.",
    "bankIncome": "Sul tuo conto bancario è stato accreditato un versamento di #1.",
    "payBillBank": "Paghi #1 oren dal conto bancario (Saldo residuo: #2 oren).",
    "getSalary": "Mysilia ti invia un tributo in segno di gratitudine.",
    "getResidentTax": "Ti è stato versato un totale di #1 come tasse dei residenti.",
    "getRankIncome": "Ricevi #1 come rendita del rango del territorio.",
    "getFactionSalary": "Ricevi #1 come compenso di fazione.",
    "getIncomeInn": "#2 genera un introito di locanda pari a #1.",
    "getIncomeTourism": "#2 genera un introito turistico pari a #1.",
    "getIncomeShop": "#2 genera un introito commerciale pari a #1.",
    "becomeCriminal": "Attenzione: ora sei considerato un criminale fuorilegge!",
    "becomeNonCriminal": "Non sei più considerato un criminale davanti alla legge.",
    "claimBed": "#1 trova e reclama il proprio giaciglio.",
    "openLockFail": "Non riesci a scassinare la serratura.",
    "openLockFail2": "La serratura è troppo complicata per le tue abilità attuali!",
    "newMeeting": "Qualcuno desidera conferire urgentemente con te.",
    "noItemToThrow": "Non hai nulla da lanciare.",
    "throw": "#1 scaglia #2 contro #3.",
    "throwHit": "#1 colpisce in pieno #2!",
    "throwMiss": "#1 manca il bersaglio.",
    "trapTrigger": "#1 fa scattare una trappola: #2!",
    "trapDisarm": "#1 disinnesca abilmente la trappola.",
    "trapDisarmFail": "#1 fallisce nel disinnescare la trappola!",
    "harvest": "Raccogli #1.",
    "mine": "Estrai #1 dalla roccia.",
    "chop": "Abbatti l'albero ricavando #1.",
    "fishBite": "Qualcosa ha abboccato all'amo!",
    "fishCatch": "Pescato! Tiri fuori dall'acqua #1!",
    "fishFail": "La preda è fuggita via strappando l'esca.",
    "readFail": "Non riesci a decifrare le parole scritte su questo testo.",
    "readSpellbook": "#1 legge avidamente il tomo magico.",
    "learnSpell": "Comprendi i misteri di #1 e ne assimili l'incantesimo!",
    "forgetSpell": "I dettagli dell'incantesimo svaniscono dalla tua memoria.",
    "castSpell": "#1 canalizza il mana e lancia #2!",
    "castFail": "Il lancio dell'incantesimo fallisce miseramente!",
    "castBackfire": "Il flusso di mana si ritorce contro l'incantatore!",
    "curePoison": "Il veleno nel corpo di #1 viene neutralizzato.",
    "cureDisease": "La malattia di #1 viene debellata.",
    "buffGain": "#1 riceve l'effetto di #2.",
    "buffLose": "L'effetto di #2 su #1 svanisce.",
    "debuffGain": "#1 viene afflitto da #2!",
    "debuffLose": "#1 si riprende dagli effetti di #2.",
    "weatherRain": "Comincia a piovere.",
    "weatherHeavyRain": "Una pioggia torrenziale si abbatte sulla zona!",
    "weatherSnow": "Soffici fiocchi di neve iniziano a cadere dal cielo.",
    "weatherEther": "Il temibile Vento dell'Etere inizia a soffiare minaccioso!",
    "weatherSunny": "Il cielo si rischiara e torna a splendere il sole.",
    "sleepWakeup": "#1 si sveglia sentendosi ristorato.",
    "sleepInterrupted": "Il tuo riposo viene bruscamente interrotto!",
    "eatFood": "#1 mangia #2 con gusto.",
    "eatRotten": "Bleah! #2 è andato a male! Lo stomaco di #1 si ribella!",
    "vomit": "#1 vomita violentemente a terra.",
    "starve": "#1 sta morendo di fame!",
    "faint": "#1 sviene per la spossatezza!",
    "die": "#1 muore.",
    "revive": "#1 torna miracolosamente in vita!",
    "petLoyal": "#1 ti guarda con devozione e affetto incondizionato.",
    "petFeed": "Nutri #1 con #2.",
    "petPraise": "Accarezzi e lodi calorosamente #1.",
    "stealthEnter": "Ti dissolvi nell'ombra muovendoti furtivamente.",
    "stealthExit": "Esci dalla modalità furtiva.",
    "stealthSpotted": "Sei stato scoperto da #1!",
    "pickpocketSuccess": "Sottrai con maestria #1 a #2 senza farti notare.",
    "pickpocketFail": "Le guardie si accorgono del tuo tentativo di borseggio!"
}

def apply_game():
    wb = openpyxl.load_workbook(GAME_FILE)
    ws = wb.active
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
    
    text_c = headers.get('text', 4)
    text_en_c = headers.get('text_EN', 5)
    id_c = headers.get('id', 1)
    
    updated = 0
    for r in range(2, ws.max_row + 1):
        id_val = str(ws.cell(r, id_c).value).strip() if ws.cell(r, id_c).value is not None else ""
        cur_text = ws.cell(r, text_c).value
        en_text = ws.cell(r, text_en_c).value
        
        if id_val in GAME_DICT:
            ws.cell(r, text_c).value = GAME_DICT[id_val]
            updated += 1
            
    wb.save(GAME_FILE)
    print(f"Updated {updated} entries in Game.xlsx!")

if __name__ == "__main__":
    apply_game()
