import openpyxl

game_msg_it = {
    'fish_miss': 'Non hai pescato nulla...\nIl pesce scappa.\nI pesci ti ignorano.\nSembra che non vogliano abboccare.',
    'fish_ehe': 'O almeno così sembrava... Il pesce svanisce misteriosamente nel nulla.',
    'fish_ehe2': 'Miao...',
    'fish_ehe3': 'Avverti un vago segno di buona sorte.',
    'fish_get': '#1 cattura #2!',
    'fish_start': '#1 comincia a pescare con #2.',
    'fish_start2': '#1 comincia a pescare.',
    'mine_start': '#1 inizia a scavare la parete rocciosa con #2.',
    'dig_start': '#1 comincia a scavare il terreno con #2.',
    'seeZone': 'Vedi #1.',
    'seeZoneDanger': 'Vedi #1 (Livello di Rischio: #2).',
    'debuff_resist': '#1 resiste all\'effetto.',
    'summon_ally': '#1 chiama un alleato in proprio soccorso.',
    'summon_ally_fail': 'Ma non accorre alcun aiuto...',
    'zapRod': '#1 sprigiona il potere di #2.',
    'nothingHappens': 'Non sembra accadere nulla...',
    'grow_hair': 'Incredibile, a #1 ricrescono i capelli!',
    'grow_hair_fail': 'Incredibile, a #1 ricrescono i capelli! ...Ma era solo un\'illusione.',
    'teleported': '#1 svanisce improvvisamente.',
    'antiTeleport': 'L\'aria attorno a #1 vibra freneticamente.',
    'exileClosed': 'Una misteriosa barriera ti impedisce l\'accesso.',
    'voidClosed': 'È richiesta una licenza speciale per esplorare questa zona.',
    'zoneClosed': 'Un potere arcano tiene questo luogo sotto sigillo.',
    'zoneBlocked': 'Il passaggio è ostruito.',
    'cantEditPlaylist': 'Non è possibile modificare la musica in questa zona.',
    'music_start': '#1 comincia a suonare #2.',
    'music_reward': 'Il pubblico entusiasta dona a #1 un totale di #2 oren.',
    'frown': '#2 lancia un\'occhiataccia a #1.',
    'setHome': 'Questa terra è ora il tuo dominio ufficiale.',
    'setSpawn': '#1 memorizza la tua presenza.',
    'unsetSpawn': '#1 perde la memoria del luogo.',
    'invalidAction': 'Non puoi compiere quest\'azione qui.\nImpossibile!',
    'cancel_act_pc': 'La tua azione è stata interrotta.',
    'cancel_act': '#1 fulmina #2 con lo sguardo.',
    'cancel_act2': '#1 viene interrott#o.',
    'calledGuard': '#1 invoca le guardie a gran voce!',
    'spotHidden': '#1 individua #2.',
    'spotMedal': 'Hai trovato una Piccola Medaglia!',
    'spotMedalStep': '*tintinnio luminoso*',
    'spotMedalNear': 'Percepisci la presenza di qualcosa di prezioso nelle vicinanze.',
    'toggle_fire': '#1 accende #2.',
    'toggle_ele': '#1 attiva #2.',
    'trap_disarm': '#1 disarma la trappola con successo.',
    'trap_disarm_fail': '#1 tenta di disarmare la trappola, ma fallisce!',
    'trap_set': '#1 piazza una trappola sul terreno.',
    'bounty': 'La Gilda dei Guerrieri ti ricompensa con #2 oren per la taglia completata!',
    'pray_god': '#1 rivolge una fervida preghiera a #2.',
    'pray_curse': 'L\'ira divina si abbatte su #1!',
    'pray_bless': '#2 concede la sua benedizione a #1.',
    'altar_convert': 'L\'altare viene convertito alla fede di #1!',
    'altar_burn': 'L\'altare viene avvolto da fiamme purificatrici.',
    'god_gift': '#1 riceve un dono sacro da #2!',
    'eat_rotten': 'Questo cibo è completamente andato a male!',
    'eat_poison': 'Questo cibo era avvelenato!',
    'eat_delicious': 'Che delizia assoluta! Un pasto memorabile.',
    'drink_potion': '#1 beve #2.',
    'read_scroll': '#1 recita le parole scritte su #2.',
    'read_book': '#1 comincia a leggere #2.',
    'open_chest': '#1 scassina e apre #2.',
    'chest_locked': '#1 è saldamente chiuso a chiave.',
    'door_locked': 'La porta è sbarrata da una solida serratura.',
    'door_unlocked': '#1 scatta e si sblocca.',
    'door_broken': '#1 si sfonda con un forte schianto!',
    'rest_start': '#1 si sdraia per riposare.',
    'rest_end': '#1 si sveglia rinfrancat#o dal sonno.',
    'sleep_deep': '#1 sprofonda in un sonno ristoratore.',
    'sleep_nightmare': '#1 si sveglia di soprassalto in preda agli incubi!'
}

file_p = 'd:/Mod/Elin/Lang/IT/Game/Game.xlsx'
wb = openpyxl.load_workbook(file_p)
ws = wb.active
headers = [str(c.value) for c in ws[1]]
id_col = headers.index('id') + 1
text_col = headers.index('text') + 1

count = 0
for r in range(2, ws.max_row + 1):
    rid = str(ws.cell(row=r, column=id_col).value or '').strip()
    if rid in game_msg_it:
        ws.cell(row=r, column=text_col, value=game_msg_it[rid])
        count += 1

wb.save(file_p)
print(f'Game.xlsx translated/updated {count} gameplay messages!')
