# coding: utf-8
"""
Elin Italian Localization - Game.xlsx Batch 2
Translates the next batch of immersion, crafting, recipes, expedition, and home logs.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GAME_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Game', 'Game.xlsx')

GAME_BATCH_2 = {
    "dingExp_pc": "Hai guadagnato sufficiente esperienza per acquisire un talento!",
    "wishFail": "Qualcosa nell'oscurità ride con scherno beffardo.",
    "wishNet": "(#1 ti è stato concesso per grazia divina.)",
    "wish": "#1 grida con gioia sfrenata: \"#2!!\"",
    "wishHappen": "Cosa desideri invocare dall'universo?",
    "affinityPlus": "#1 apprezza #2.",
    "affinityMinus": "#1 disapprova #2.",
    "affinityNone": "#1 fa spallucce davanti a #2.",
    "craft_fail": "#1 fallisce nella fabbricazione di #2.",
    "disassemble_fail": "#1 non riesce a smantellare #2.",
    "lostResource": "#1 è andato irrimediabilmente perduto.",
    "tooHardToDig": "#2 è troppo duro da scavare!",
    "tooHardToMine": "#2 è troppo duro da estrarre!",
    "tooHardToHarvest": "#2 è troppo difficile da raccogliere.",
    "tooHardToDisassemble": "#2 è troppo resistente per essere smantellato.",
    "karmaUp": "Karma (+#1)",
    "karmaDown": "Karma (#1)",
    "gatherLimit": "Hai bisogno di uno strumento di qualità superiore.",
    "gatherLimitHand": "Hai bisogno di un attrezzo adeguato (non puoi farlo a mani nude).",
    "harvest_fail": "Non riesci a raccogliere alcunché.",
    "mobFromTree": "#1 cade improvvisamente dai rami dell'albero!",
    "noGachaCoin": "Non possiedi alcun biglietto per il distributore gacha.",
    "playedGacha": "Estrai #1 sfer#(a/e) dal distributore gacha.",
    "gachaAdd": "Registri i dati personali di #1 nella pietra del focolare.",
    "dump": "Getti #1 all'interno di #2.",
    "newDay": "Sorge una nuova alba. Un nuovo giorno ha inizio nelle terre di Ylva.",
    "reportWork": "#1 fa rapporto sui risultati del suo turno di lavoro. #2",
    "bTax": "#2 versa un'imposta di #1 oren.",
    "bDing": "#1 sviluppa e migliora l'abilità #2.",
    "bExpeditionStart": "#1 si mette in marcia per una spedizione esplorativa in #2.",
    "bExpeditionEnd": "#1 è di ritorno dalla spedizione esplorativa in #2.",
    "bNurse": "#1 rianima e presta le prime cure a #2.",
    "bRevive": "#1 fa ritorno dal regno dei morti!",
    "newKnownCraft": "Hai appreso un nuovo metodo di produzione!",
    "learnRecipeIdea": "Un lampo d'ispirazione! Ti è venuta in mente una nuova ricetta!",
    "learnRecipeSleep": "Una nuova ricetta ti si rivela nitidamente in sogno...",
    "learnRecipe": "Perfezioni la ricetta di \"#1\" (#2).",
    "learnRecipeNew": "Impari la ricetta per realizzare \"#1\"!",
    "noRecipes": "Non conosci ancora alcuna ricetta.",
    "canOnlyCarry": "#1 non entra nello zaino e può essere soltanto trasportato a mano.",
    "discoverZone": "Hai scoperto e segnato sulla mappa la posizione di #1!",
    "noBait": "Non hai esche da pesca!",
    "noAmmo": "Non hai munizioni disponibili!",
    "equipItem": "#1 equipaggia #2.",
    "equipCursed": "Un brivido sinistro e gelido gela il sangue di #1... l'oggetto è maledetto!",
    "unequipItem": "#1 ripone #2.",
    "unequipCursed": "#1 si oppone con forza sovrannaturale e rifiuta di staccarsi dal tuo corpo!",
    "unrestrained": "#1 si libera finalmente da ogni costrizione.",
    "restrained": "#1 viene brutalmente immobilizzato!",
    "errorUnemptyContainer": "Il contenitore deve essere completamente vuoto prima di compiere questa operazione.",
    "digTreasure": "La tua vanga urta qualcosa di metallico... hai dissotterrato un tesoro!",
    "digNothing": "Scavi a lungo ma non trovi nulla di interessante.",
    "digFail": "La vanga scivola senza riuscire a intaccare il terreno.",
    "mineGem": "Tra i detriti rocciosi scorgi una gemma preziosa!",
    "mineOre": "Estrai con successo del minerale grezzo.",
    "mineFail": "Il piccone rimbalza sulla parete rocciosa.",
    "chopWood": "Tagli con maestria ricavando legname di qualità.",
    "chopFail": "L'ascia fatica a intaccare la corteccia dura dell'albero.",
    "harvestCrop": "Raccogli #1 maturo dal campo.",
    "harvestSeed": "Raccogli preziosi semi da #1.",
    "eatFull": "#1 è completamente satollo e non riesce a mandare giù un altro boccone.",
    "drinkFull": "#1 non ha più sete.",
    "stomachAche": "Lo stomaco di #1 borbotta sinistramente...",
    "poisonDamage": "Il veleno nelle vene di #1 provoca #2 danni!",
    "burnDamage": "Le fiamme avvolgono #1 infliggendo #2 danni da bruciatura!",
    "coldDamage": "Il gelo pungente morde le carni di #1 infliggendo #2 danni!",
    "bleedDamage": "#1 perde copioso sangue dalla ferita aperta subendo #2 danni!",
    "acidDamage": "L'acido corrosivo consuma l'equipaggiamento di #1!",
    "etherDiseaseProgress": "La Malattia dell'Etere progredisce nelle tue membra... Senti un'inquietante trasformazione!",
    "etherDiseaseHealed": "Il Morbo dell'Etere regredisce purificando il tuo corpo.",
    "potionDrink": "#1 tracanna #2 in un sol sorso.",
    "scrollRead": "#1 recita i versi arcani scritti sulla pergamena di #2.",
    "wandZap": "#1 punta la bacchetta e ne rilascia la carica magica!",
    "chestOpen": "#1 scardina e apre il forziere.",
    "chestLocked": "Il forziere è saldamente chiuso a chiave.",
    "chestTrapped": "Attenzione! Il forziere cela un meccanismo a trappola!",
    "levelUp": "Congratulazioni! #1 sale di livello!",
    "skillLevelUp": "L'abilità #2 di #1 sale al livello #3!",
    "guildRankUp": "La tua reputazione all'interno della gilda cresce!",
    "fameUp": "La tua fama nelle terre di Ylva aumenta di #1 punti.",
    "fameDown": "La tua fama crolla di #1 punti per la vergogna."
}

def apply_game_batch():
    wb = openpyxl.load_workbook(GAME_FILE)
    ws = wb.active
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
    
    text_c = headers.get('text', 4)
    id_c = headers.get('id', 1)
    
    count = 0
    for r in range(2, ws.max_row + 1):
        id_val = str(ws.cell(r, id_c).value).strip() if ws.cell(r, id_c).value is not None else ""
        if id_val in GAME_BATCH_2:
            ws.cell(r, text_c).value = GAME_BATCH_2[id_val]
            count += 1
            
    wb.save(GAME_FILE)
    print(f"Applied {count} additional entries to Game.xlsx!")

if __name__ == "__main__":
    apply_game_batch()
