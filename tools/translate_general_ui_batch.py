import openpyxl

gen_batch = {
    # Confirmation Dialogs
    'dialog_caption': 'Conferma',
    'dialog_quit': 'Vuoi salvare la partita ed uscire dal gioco?',
    'dialog_gotoTitle': 'Vuoi salvare la partita e tornare al menu principale?',
    'dialog_abandonQuest': 'Vuoi davvero abbandonare questa missione?',
    'dialog_rope': 'Vuoi davvero impiccarti con questa corda?',
    'dialog_claimLand': 'Vuoi davvero rivendicare questa terra come tuo dominio?',
    'dialog_relocateLand': 'Vuoi davvero trasferire la tua dimora in questo luogo?',
    'dialog_deleteMap': 'Vuoi davvero rimuovere questo luogo dalla mappa?',
    'dialog_deleteMapPiece': 'Vuoi davvero eliminare questo progetto architettonico?',
    'dialog_removeGene': 'Vuoi davvero rimuovere questo gene?',
    'dialog_restoreWarning': 'Vuoi davvero ripristinare questo salvataggio e sovrascrivere la partita corrente?',
    'dialog_switchCloud': 'Vuoi davvero modificare il formato di salvataggio?\nIl passaggio al cloud potrebbe richiedere alcuni secondi.',
    'dialog_changeDifficulty': 'Vuoi davvero infrangere il tuo vincolo #1?\n<color=red>(Questa operazione è irreversibile!)</color>',
    'dialog_needToLogOn': 'È necessario essere connessi a Steam.',
    'dialog_debugFeedback': 'Non è possibile inviare segnalazioni mentre il gioco è in modalità debug.',
    'dialog_keymap': 'Premi un tasto per assegnare l\'azione [#1].\n(Premi ESC per annullare)',

    # Keyboard / Controller Shortcuts
    'key_QuickSave': 'Salvataggio Rapido',
    'key_QuickLoad': 'Caricamento Rapido',
    'key_Console': 'Apri Console Comandi',
    'key_Chat': 'Chat',
    'key_Mute': 'Disattiva Musica',
    'key_Meditate': 'Riposa',
    'key_GetAll': 'Raccogli Tutto',
    'key_Log': 'Mostra/Nascondi Registro',
    'key_Wait': 'Attendi Turno',
    'key_Search': 'Cerca Risorse',
    'key_Fire': 'Spara / Mira',
    'key_MenuAbility': 'Abilità',
    'key_MenuChara': 'Scheda Personaggio',
    'key_MenuInventory': 'Inventario',
    'key_MenuJournal': 'Diario',
    'key_SwitchHotbar': 'Cambia Barra Rapida',
    'key_AutoCombat': 'Combattimento Automatico',
    'key_Examine': 'Esamina Oggetto',
    'key_Cancel': 'Annulla',
    'key_EmptyHand': 'Mani Nude',
    'key_Switch': 'Attendi / Esamina',
    'key_Dump': 'Scarica Registro',
    'key_MouseLeft': '(Emulazione) Clic Sinistro',
    'key_MouseMiddle': '(Emulazione) Clic Centrale',
    'key_MouseRight': '(Emulazione) Clic Destro',
    'key_AxisUp': 'Su',
    'key_AxisDown': 'Giù',
    'key_AxisLeft': 'Sinistra',
    'key_AxisRight': 'Destra',
    'key_AxisUpLeft': 'In Alto a Sinistra',
    'key_AxisUpRight': 'In Alto a Destra',
    'key_AxisDownLeft': 'In Basso a Sinistra',
    'key_AxisDownRight': 'In Basso a Destra',

    # Categories in Build & Crafting
    'cat_all': 'Tutto',
    'cat_area': 'Zona',
    'cat_spot': 'Utilità',
    'cat_storage': 'Deposito',
    'cat_terrain': 'Terreno',
    'cat_tool': 'Attrezzi',
    'cat_wall': 'Pareti',
    'cat_attack': 'Attacco',
    'cat_defense': 'Difesa',
    'cat_util': 'Utilità',
    'cat_ability': 'Abilità',

    # Policies & Difficulty (pp_...)
    'pp_template': 'Difficoltà',
    'pp_custom': 'Impostazione Personalizzata',
    'pp_permadeath': '*Morte Permanente* (Il salvataggio viene cancellato alla morte)',
    'pp_disableManualSave': 'Salvataggi e caricamenti manuali vietati',
    'pp_disableDeathPenaltyProtection': 'Nessuna protezione iniziale dalla penalità di morte',
    'pp_tax': 'Obbligo di versare le tasse',
    'pp_disableUsermapBenefit': 'Limita le azioni vantaggiose nelle mappe della community',
    'pp_Oath': 'Giuramenti (Sfide e Vincoli)',
    'pp_Workaround': 'Agevolazioni (Vantaggi Giocatore)',
    'pp_dropRate': 'Moltiplicatore Bottino Boss',
    'pp_petFeatExp': 'Moltiplicatore ESP Tratti Alleati',
    'pp_showWorkaround': 'Mostra Tutte le Leggi',
    'pp_scaleQuest': 'Scala la difficoltà dei contenuti statici con la fama',
    'pp_scaleQuest_hint': 'La difficoltà dei sotterranei di trama è normalmente fissa.\nCon questo giuramento attivo, aumenterà in proporzione alla fama dell\'avventuriero.',
    'pp_noAging': 'Eterni Tredicenni',
    'pp_noAging_hint': 'Gli abitanti generici non invecchieranno più con il trascorrere degli anni.\nTuttavia, cresceranno normalmente fino all\'età di 13 anni.',
    'pp_Flavor': 'Opzioni di Contesto',
    'pp_Legacy': 'Opzioni Legacy',
    'pp_infiniteMarketFund': 'Circolazione infinita di oren nei mercati',
    'pp_opMilk': 'Latte della dominazione',
    'pp_realAdv': 'Mondo Crudele (In arrivo)',
    'pp_realAdv_hint': '<i>Questo mondo è crudele, ma è anche straordinariamente bello.</i>\n\nIn questa modalità, la difficoltà è regolata sul bilanciamento originariamente concepito.',
    'pp_disableVoidBlessing': 'I nemici non ricevono la Benedizione dell\'Abisso',
    'pp_enableDamageReduction': 'Attenua il danno nemico nei piani più profondi',
    'pp_enableGeneDupe': 'Permette ai PNG modificati geneticamente di autoriprodursi',

    # Guild Tasks & Benefits
    'guild_fighter_task1': '・ Caccia ai mostri rari.',
    'guild_mage_task1': '・ Decifrazione di tomi antichi.',
    'guild_thief_task1': '・ Ricettazione di merci rubate.',
    'guild_merchant_task1': '・ Investimenti nei mercanti locali.',
    'guild_fighter_benefit1': '・ Sconti su vari servizi cittadini.',
    'guild_mage_benefit1': '・ Sconti sull\'acquisto di libri di incantesimi.',
    'guild_thief_benefit1': '・ Prezzo di vendita maggiorato per la refurtiva.',
    'guild_merchant_benefit1': '・ Costo d\'investimento ridotto nei negozi.',
    'guild_fighter_benefit2': '・ Taglie in denaro per la cattura di criminali ricercati.',
    'guild_mage_benefit2': '・ Servizi di riassegnazione del dominio arcano.',
    'guild_thief_benefit2': '・ Accesso esclusivo ai ricettatori del mercato nero.',
    'guild_merchant_benefit2': '・ Accesso ai commercianti di beni esotici.',
    'guild_fighter_benefit3': '・ Maggiore frequenza di apparizione dei ricercati.',
    'guild_mage_benefit3': '・ Uno slot aggiuntivo di specializzazione del dominio.',
    'guild_thief_benefit3': '・ Qualità superiore dei mobili generati naturalmente.',
    'guild_merchant_benefit3': '・ Livello bottega superiore nei negozi finanziati.',
    'guild_benefit_trainer': '・ Sconto sull\'addestramento presso l\'istruttore di gilda.',
    'guild_benefit_feat': '・ Accesso ai tratti esclusivi di classe.'
}

file_p = 'd:/Mod/Elin/Lang/IT/Game/General.xlsx'
wb = openpyxl.load_workbook(file_p)
ws = wb.active
headers = [str(c.value) for c in ws[1]]
id_col = headers.index('id') + 1
text_col = headers.index('text') + 1

count = 0
for r in range(2, ws.max_row + 1):
    rid = str(ws.cell(row=r, column=id_col).value or '').strip()
    if rid in gen_batch:
        ws.cell(row=r, column=text_col, value=gen_batch[rid])
        count += 1

wb.save(file_p)
print(f'General.xlsx translated {count} additional system, dialog, shortcut and policy strings!')
