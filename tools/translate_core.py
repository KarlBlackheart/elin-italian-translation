"""
Elin Italian Translation - Core Translations Applier (Expanded)
Applica le traduzioni italiane ai file chiave con riferimento multilingue:
- General.xlsx (UI, Menu, Titoli, Configurazione, Grammatica di sistema)
- Game.xlsx (Meteo, Notifiche, Azioni primarie, Sistema)
- Element.xlsx (Attributi primari, statistiche vitali, statistiche di combattimento)
- Stat.xlsx (Stati alterati, condizioni, buff e debuff)
- Race.xlsx & Job.xlsx (Razze e Classi della creazione personaggio)
- Dialog/dialog.xlsx (Linee di dialogo base con PNG)
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LANG_IT_DIR = os.path.join(MOD_DIR, 'Lang', 'IT')

def update_excel_translations(file_path, id_col_name, trans_map):
    if not os.path.isfile(file_path):
        print(f"File non trovato: {file_path}")
        return 0

    wb = openpyxl.load_workbook(file_path)
    applied = 0

    for sname in wb.sheetnames:
        ws = wb[sname]
        headers = {}
        for c in range(1, ws.max_column + 1):
            v = ws.cell(row=1, column=c).value
            if v:
                headers[str(v).strip()] = c

        if id_col_name not in headers:
            continue

        id_c = headers[id_col_name]

        for r in range(2, ws.max_row + 1):
            rid = ws.cell(row=r, column=id_c).value
            if rid is None:
                continue
            rid_str = str(rid).strip()

            if rid_str in trans_map:
                entry = trans_map[rid_str]
                if isinstance(entry, dict):
                    for col_name, text_val in entry.items():
                        if col_name in headers:
                            ws.cell(row=r, column=headers[col_name], value=text_val)
                            applied += 1
                elif isinstance(entry, str):
                    target_col = 'text' if 'text' in headers else ('name' if 'name' in headers else None)
                    if target_col and target_col in headers:
                        ws.cell(row=r, column=headers[target_col], value=entry)
                        applied += 1

    wb.save(file_path)
    return applied

# ======================================================================
# 1. General.xlsx (UI, Menu, Grammatica di base)
# ======================================================================
general_translations = {
    # System strings
    "_'s": "#1 di #2",
    "_and": "#1 e #2",
    "_book": "#1 intitolato \"#2\"",
    "_lostproperty": "#1 smarrito",
    "_jammed": "#1 inceppato",
    "_cast_confuse": " in stato di confusione",
    "_cast_dim": " stordito",
    "_follower": "seguace di #2, #1",
    "_limitedStock": "(Scorte Limitate) #1",
    "_halfeaten": "#1 mezzo mangiato",
    "_sealed": "(Sigillato)",
    "_factionWide": "(Fazione)",
    "_shared": "#1 condiviso",
    "_evolved": "#1 Evoluto",
    "_for": "#2 per #1",
    "_bed": "#2 per #1",
    "_of": "#2 di #1",
    "_of2": "#1 #2",
    "_of3": "#2 di #1",
    "_of4": "#2 #1",
    "_parchment": "#1 con scritto \"#2\"",

    # Menu
    "admin": "Mappa Locale",
    "area": "Area",
    "charaInfo": "Dettagli",
    "factions": "Fazioni",
    "gacha": "Gacha",
    "gods": "Divinità",
    "hire": "Recluta",
    "hoard": "Tesoro",
    "m_all": "Menu Generale",
    "m_chara": "Menu Personaggio",
    "m_faction": "Menu Comunità",
    "m_system": "Menu di Sistema",
    "mode": "Modalità",
    "objInfo": "Esamina",
    "policy": "Politiche",
    "quest": "Bacheca Missioni",
    "research": "Ricerca",
    "resource": "Risorse",
    "toGlobalMap": "Mappa Globale",
    "world": "Mondo",

    # Titles / Layers
    "LayerAbility": "Abilità",
    "LayerAdmin": "Amministrazione",
    "LayerChara": "Personaggio",
    "LayerConsole": "Console",
    "LayerCredit": "Riconoscimenti",
    "LayerPixelPaint": "Editor Pixel Art",
    "LayerPickPCC": "Seleziona Parti",
    "LayerEditPCC": "Modifica Aspetto",
    "LayerFactions": "Fazioni",
    "LayerTextureViewer": "Visualizzatore Texture",
    "LayerMod": "Gestione Mod",
    "LayerHelp": "Guida",
    "LayerHire": "Candidati al Trasferimento",
    "LayerHome": "Comunità",
    "LayerInventory": "Inventario",
    "LayerTactics": "Accampamento",
    "LayerJournal": "Diario",
    "LayerPeople": "Elenco Abitanti",
    "LayerPolicy": "Modifica Politiche",
    "LayerResource": "Risorse",
    "LayerUploader": "Pubblica Mappa",
    "LayerUploaderSetting": "Opzioni di Pubblicazione",
    "LayerTech": "Albero delle Ricerche",
    "LayerWorld": "Luoghi del Mondo",

    # Mod manager
    "open_replace": "Apri",
    "delete_replace": "Elimina",
    "create_replace": "Crea Sostituzione",
    "create_replaceLocal": "Crea Sostituzione Mappa",
    "mod_order": "Ordine di Caricamento",
    "mod_restart": "*Riavvio necessario per applicare le modifiche.",
    "mod_system": "Mod Predefinite",
    "mod_publish": "Pubblica su Steam",
    "mod_created": "L'elemento è stato registrato con successo nel Workshop di Steam!",
    "mod_updated": "L'elemento è stato aggiornato con successo.",
    "mod_publish_error": "Si è verificato un errore durante l'upload.",
    "mod_info": "Mostra in Esplora File",
    "mod_activate": "Attiva",
    "mod_deactivate": "Disattiva",
    "mod_publish_warn": "Stai per pubblicare o aggiornare questo elemento su Steam Workshop.\n\n#1\n(id) #2\nAutore: #3\n\nConfermi che questo contenuto è stato creato da te?",
    "mod_export_text": "Esporta testi per la localizzazione",
    "mod_convert_local": "Converti in pacchetto locale",

    # Embark (Creazione avventura)
    "startMode": "Prologo",
    "vow_0": "Consigliato per gli avventurieri alle prime armi.\n\nSalvataggi liberi e nessuna penalità di morte per un po' di tempo.\n\nPuoi modificare queste impostazioni in qualsiasi momento.",
    "vow_1": "Consigliato per avventurieri che conoscono già il mondo di Ylva.\n\nNon è possibile salvare liberamente: il tuo destino è nelle tue mani e nella dea della fortuna.\n\nPuoi modificare queste impostazioni in qualsiasi momento.",
    "vow_-1": "Imposta liberamente ogni regola e principio.\n\nI gettoni degli obiettivi si ottengono solo mantenendo le impostazioni iniziali senza modificarle durante la partita.",

    # Categorie di costruzione e craft
    "BuildAll": "Tutto",
    "BuildDeco": "Decorazioni",
    "BuildFurniture": "Mobili",
    "BuildHobby": "Svago",
    "BuildInfra": "Infrastrutture",
    "buildNum": "Scorte",
    "BuildOther": "Altro",
    "BuildWelfare": "Benessere",
    "BuildWork": "Lavoro",
    "captionBuild": "Menu di Costruzione",
    "cat_area": "Area",
    "cat_deco": "Decorazioni",
    "cat_door": "Porte e Finestre",
    "cat_ext": "Esterni",
    "cat_facility": "Strutture",
    "cat_floor": "Pavimenti",
    "cat_food": "Cibo",
    "cat_foundation": "Fondamenta",
    "cat_furniture": "Arredamento",
    "cat_goods": "Mercanzie",
    "cat_junk": "Cianfrusaglie",
    "cat_light": "Illuminazione",
    "cat_mech": "Meccanismi",
    "cat_mount": "Cavalcature",
    "cat_obj": "Elementi Ambientali",
    "cat_other": "Altro",
}

# ======================================================================
# 2. Game.xlsx
# ======================================================================
game_translations = {
    "weather_Rain": "Comincia a piovere.",
    "weather_RainHeavy": "Piove a dirotto!",
    "weather_Storm": "Una tempesta si sta avvicinando!",
    "weather_Snow": "Inizia a nevicare.",
    "weather_SnowHeavy": "Si abbatte una bufera di neve.",
    "weather_Cloudy": "Il cielo si fa cupo.",
    "weather_Ether": "L'aria comincia a riempirsi di etere!",
    "weather_Fine": "Il cielo è sereno.",
    "welcome_intro": "Lafrontier presenta: Elin versione #1",
    "welcome": "Benvenuto, viandante! Premi '?' per aprire la guida di gioco.",
    "endDay": "Trascorre un giorno.",
    "startSiege": "L'assedio ha inizio!",
    "endSiege": "L'assedio è terminato.",
    "saved": "*Partita Salvata*",
    "tutorial_added": "Nuova voce aggiunta al Registro delle Avventure.",
    "story_added": "Un nuovo capitolo di storia è stato aggiunto.",
    "guestArrive": "#1 è arrivato in visita.",
    "stack_thing": "Unisci #1 a #2.",
    "pick_thing": "#1 raccoglie #2.",
    "pick_thing_pc": "Raccogli #2.",
    "pick_held": "#1 ripone #2 nello zaino.",
    "pick_held_pc": "Riponi #2 nel tuo zaino.",
    "backpack_full": "Non c'è più spazio nel tuo zaino!",
    "backpack_full_drop": "#1 trabocca dallo zaino e cade a terra.",
    "ding_skill": "La tua abilità in #2 è aumentata!",
    "sleep_start": "Ti addormenti profondamente...",
    "sleep_wake": "Ti svegli sentendoti riposato.",
    "hunger_starve": "Stai morendo di fame!",
    "hunger_hungry": "Il tuo stomaco brontola: hai fame.",
    "hunger_full": "Sei sazio.",
}

# ======================================================================
# 3. Element.xlsx (Attributi primari, statistiche, combattimento)
# ======================================================================
element_translations = {
    "60": {"name": "Vita", "detail": "Determina i punti ferita (HP) massimi del personaggio."},
    "61": {"name": "Mana", "detail": "Determina i punti mana (MP) massimi per lanciare incantesimi."},
    "62": {"name": "Vigore", "detail": "Determina l'energia per le azioni fisiche e la resistenza alla fatica."},
    "64": {"name": "Valore di Schivata (DV)", "detail": "Rappresenta la capacità di eludere gli attacchi nemici."},
    "65": {"name": "Valore di Protezione (PV)", "detail": "Rappresenta la riduzione percentuale e fissa dei danni fisici subiti."},
    "66": {"name": "Modificatore Mira", "detail": "Bonus alla precisione nei colpi d'attacco."},
    "67": {"name": "Modificatore Danno", "detail": "Bonus al danno inflitto negli attacchi."},
    "70": {"name": "Forza", "detail": "Misura la potenza fisica, il peso massimo trasportabile e il danno con armi pesanti."},
    "71": {"name": "Costituzione", "detail": "Rafforza la salute fisica, la resistenza ai colpi e il recupero vitale."},
    "72": {"name": "Destrezza", "detail": "Determina la precisione con le armi a distanza, il colpo critico e le abilità manuali."},
    "73": {"name": "Percezione", "detail": "Migliora l'attenzione visiva, l'individuazione di pericoli e il combattimento a distanza."},
    "74": {"name": "Apprendimento", "detail": "Aumenta la velocità di acquisizione delle competenze e l'efficacia nello studio."},
    "75": {"name": "Volontà", "detail": "Rafforza la concentrazione mentale, i punti mana e la resistenza alle illusioni."},
    "76": {"name": "Magia", "detail": "Determina il potere e l'intensità di ogni incantesimo e capacità sovrannaturale."},
    "77": {"name": "Carisma", "detail": "Influenza il fascino personale, i prezzi di vendita/acquisto e la leadership."},
    "78": {"name": "Fortuna", "detail": "Guida gli eventi fortuiti, i tiri salvezza critici e i ritrovamenti rari."},
    "79": {"name": "Velocità", "detail": "Determina la rapidità con cui il personaggio compie azioni rispetto al tempo di gioco."},
    "80": {"name": "Intelligenza", "detail": "Determina la comprensione concettuale, l'alchimia e la memoria dei tomi."},
}

# ======================================================================
# 4. Stat.xlsx (Stati alterati e condizioni)
# ======================================================================
stat_translations = {
    "55": {"name": "Provocazione", "detail": "Attira l'attenzione dei nemici proteggendo gli alleati."},
    "23": {"name": "Avvelenamento", "detail": "Il corpo è intossicato dal veleno e perde salute ad ogni azione."},
    "25": {"name": "Soffocamento", "detail": "L'aria viene a mancare: rischio di danno rapido da asfissia."},
    "26": {"name": "In Fiamme", "detail": "Le fiamme avvolgono il corpo infliggendo danni da fuoco continui."},
    "27": {"name": "Terrore", "detail": "Il terrore paralizza i sensi impedendo qualsiasi attacco offensivo."},
    "14": {"name": "Sonno", "detail": "Immerso in un sonno profondo: incapace di agire finché non viene svegliato."},
    "29": {"name": "Svenimento", "detail": "Privo di sensi e completamente indifeso."},
    "72": {"name": "Immobilizzato", "detail": "Bloccato sul posto: non puoi muoverti."},
    "2":  {"name": "Paralisi", "detail": "I muscoli non rispondono: impossibilitato a muoversi o attaccare."},
    "3":  {"name": "Cecità", "detail": "La vista è oscurata: precisione drasticamente ridotta."},
    "4":  {"name": "Confusione", "detail": "I pensieri sono annebbiati: i movimenti avvengono in direzioni casuali."},
}

# ======================================================================
# 5. Race.xlsx (Razze)
# ======================================================================
race_translations = {
    "yerles": {"name": "Yerles", "detail": "Gli Yerles sono una razza umana altamente industrializzata e pragmatica, celebre per l'ingegno bellico e l'abilità nelle armi da fuoco."},
    "eulderna": {"name": "Eulderna", "detail": "Antica stirpe legata alle energie magiche primordiali, dotata di eccezionale affinità con gli incantesimi."},
    "juere": {"name": "Juere", "detail": "Popolo agile e astuto, abituato a sopravvivere negli ambienti più ostili con furtività e riflessi fulminei."},
    "piani": {"name": "Piani", "detail": "Creature minute e graziose, dotate di un forte legame con la natura e un fascino innato."},
    "damog": {"name": "Damog", "detail": "Popolo robusto e tenace, dalle grandi doti fisiche e straordinaria resistenza alla fatica."},
    "norland": {"name": "Norland", "detail": "Abitanti delle terre del nord, fieri, resistenti al freddo estremo e abili cacciatori."},
    "elea": {"name": "Elea", "detail": "Elfi saggi custodi delle foreste e delle memorie del mondo, dotati di naturale resistenza all'Etere."},
    "snail": {"name": "Lumaca", "detail": "Una lumaca. Incredibilmente fragile, vulnerabile al sale e ridicolmente lenta. Una vera sfida per giocatori esperti!"},
    "lich": {"name": "Lich", "detail": "Essere non-morto padrone assoluto delle arti necromantiche, dotato di grande potere magico ma temuto da tutti."},
    "golem": {"name": "Golem", "detail": "Gigante di pietra e metallo, virtualmente immune al dolore e dotato di una difesa fisica impenetrabile."},
    "mutant": {"name": "Mutante", "detail": "Una creatura instabile che sviluppa nuovi arti e mutazioni anomale man mano che accresce il proprio potere."},
    "fairy": {"name": "Fata", "detail": "Minuscola creatura alata ad altissima velocità e affinità magica, incapace però di trasportare carichi pesanti."},
}

# ======================================================================
# 6. Job.xlsx (Classi)
# ======================================================================
job_translations = {
    "warrior": {"name": "Guerriero", "detail": "Maestro delle armi da mischia e dell'armatura pesante, in prima linea in ogni scontro."},
    "thief": {"name": "Ladro", "detail": "Esperto di furtività, disarmo trappole, scasso e letali attacchi a sorpresa."},
    "wizard": {"name": "Mago", "detail": "Studioso delle forze arcane, capace di devastare i nemici con potenti incantesimi."},
    "farmer": {"name": "Agricoltore", "detail": "Lavoratore instancabile legato alla terra, esperto nella coltivazione, raccolta e cucina."},
    "hunter": {"name": "Cacciatore", "detail": "Tiratore infallibile con archi e balestre, letale dalla lunga distanza e abile nella caccia."},
    "paladin": {"name": "Paladino", "detail": "Campione della giustizia protetto da armature pesanti, combina abilità belliche e preghiere sacre."},
    "warmage": {"name": "Mago Guerriero", "detail": "Guerriero versatile che fonde l'uso della spada con incantesimi offensivi a corto raggio."},
    "priest": {"name": "Sacerdote", "detail": "Devoto servitore degli dei, benedice i compagni e cura le ferite più gravi."},
    "archer": {"name": "Arciere", "detail": "Specialista del tiro con l'arco rapido e letale in ogni condizione."},
    "pianist": {"name": "Pianista", "detail": "Artista raffinato e carismatico, capace di suonare melodie sublimi e trasportare carichi pesanti."},
    "tourist": {"name": "Turista", "detail": "Un semplice viaggiatore senza abilità particolari, armato solo di macchina fotografica e tanta sfortuna!"},
    "gunner": {"name": "Pistolero", "detail": "Esperto di pistole, fucili e polvere da sparo, semina il panico a colpi di proiettili."},
    "merchant": {"name": "Mercante", "detail": "Maestro del commercio e della contrattazione, accumula ricchezze e negozia con chiunque."},
}

# ======================================================================
# 7. Dialog/dialog.xlsx
# ======================================================================
dialog_translations = {
    "food1": "Abbiamo dei piatti speciali caldi pronti per te! Con soli #1 Orens sono tutti tuoi.",
    "food2": "Ecco a te, buon appetito!",
    "healer1": "Hai ferite o soffri di qualche malanno? Per #1 Orens posso iniziare subito il trattamento.",
    "healer2": "Resta fermo un attimo. Rimetterò in sesto il tuo corpo in men che non si dica.",
    "appraise1": "Hai oggetti non identificati nello zaino? Per #1 Orens posso identificarli tutti per te.",
    "appraise2": "Perfetto, ecco qua! Ora conosci la vera natura di tutti i tuoi oggetti.",
    "guard1": "Tieni le armi nel fodero mentre ti trovi all'interno della città.",
    "guard2": "Segnala qualsiasi attività sospetta alle guardie cittadine.",
    "inn1": "Vuoi una stanza per riposare? Un buon sonno costa #1 Orens.",
    "inn2": "Sogni d'oro! Fai come se fossi a casa tua.",
}

def apply_all():
    print("Applicazione del nucleo fondamentale di traduzioni italiane...")
    
    c1 = update_excel_translations(os.path.join(LANG_IT_DIR, 'Game', 'General.xlsx'), 'id', general_translations)
    print(f"• General.xlsx: {c1} stringhe tradotte")

    c2 = update_excel_translations(os.path.join(LANG_IT_DIR, 'Game', 'Game.xlsx'), 'id', game_translations)
    print(f"• Game.xlsx: {c2} stringhe tradotte")

    c3 = update_excel_translations(os.path.join(LANG_IT_DIR, 'Game', 'Element.xlsx'), 'id', element_translations)
    print(f"• Element.xlsx: {c3} attributi/statistiche tradotti")

    c4 = update_excel_translations(os.path.join(LANG_IT_DIR, 'Game', 'Stat.xlsx'), 'id', stat_translations)
    print(f"• Stat.xlsx: {c4} condizioni/stati tradotti")

    c5 = update_excel_translations(os.path.join(LANG_IT_DIR, 'Game', 'Race.xlsx'), 'id', race_translations)
    print(f"• Race.xlsx: {c5} razze tradotte")

    c6 = update_excel_translations(os.path.join(LANG_IT_DIR, 'Game', 'Job.xlsx'), 'id', job_translations)
    print(f"• Job.xlsx: {c6} classi tradotte")

    c7 = update_excel_translations(os.path.join(LANG_IT_DIR, 'Dialog', 'dialog.xlsx'), 'id', dialog_translations)
    print(f"• dialog.xlsx: {c7} dialoghi base tradotti")

    print("Traduzioni del nucleo fondamentale applicate con successo!")

if __name__ == '__main__':
    apply_all()
