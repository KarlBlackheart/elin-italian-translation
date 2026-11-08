"""
Elin Italian Localization - Category, Area & Zone Localizer
Localizza integralmente:
- Category.xlsx (Tutte le categorie di oggetti, armi, armature, cibi, arredi e tomi)
- Area.xlsx (Tutti i tipi di stanze ed edifici della base)
- Zone.xlsx (Regioni, citta', dungeon e territori di Ylva)
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GAME_DIR = os.path.join(MOD_DIR, 'Lang', 'IT', 'Game')

CATEGORY_MAP = {
    "food": "Cibo",
    "meal": "Pasto",
    "meal_meat": "Piatto di Carne",
    "meal_fish": "Piatto di Pesce",
    "meal_vegi": "Piatto di Verdure",
    "meal_fruit": "Piatto di Frutta",
    "meal_cake": "Torta",
    "meal_bread": "Pane",
    "meal_cookie": "Biscotto",
    "meal_noodle": "Tagliolini",
    "meal_egg": "Piatto a Base di Uova",
    "meal_rice": "Piatto di Riso",
    "meal_soup": "Zuppa",
    "meal_lunch": "Pranzo al Sacco",
    "foodstuff": "Ingrediente Alimentare",
    "grain": "Cereali",
    "dough": "Impasto",
    "meat": "Carne",
    "vegi": "Verdura",
    "fruit": "Frutta",
    "mushroom": "Fungo",
    "egg": "Uovo",
    "fish": "Pesce",
    "nuts": "Frutta Secca",
    "filling": "Farcitura",
    "seasoning": "Condimento",
    "_seasoning": "Condimento",
    "herb": "Erba Medica",
    "sauce": "Salsa",
    "spice": "Spezia",
    "preserved": "Cibo a Lunga Conservazione",
    "foodstuff_raw": "Ingrediente Grezzo",
    "drink": "Bevanda",
    "_drink": "Pozione",
    "booze": "Alcolico",
    "milk": "Latticini",
    "drug": "Sostanza Farmaceutica",
    "weapon": "Arma",
    "melee": "Arma da Mischia",
    "sword": "Spada Lunga",
    "dagger": "Spada Corta",
    "blunt": "Arma Contundente",
    "staff": "Bastone da Mago",
    "axe": "Ascia",
    "polearm": "Arma ad Asta",
    "scythe": "Falce",
    "martial": "Arma da Arti Marziali",
    "ranged": "Arma a Distanza",
    "ammo": "Munizioni",
    "bow": "Arco",
    "crossbow": "Balestra",
    "gun": "Arma da Fuoco",
    "cane": "Bacchetta Magica",
    "throw": "Arma da Lancio",
    "armor": "Armatura",
    "torso": "Corazza / Busto",
    "head": "Elmo / Copricapo",
    "back": "Mantello / Schiena",
    "waist": "Cintura / Fianchi",
    "arm": "Guanti / Braccia",
    "foot": "Stivali / Calzature",
    "finger": "Anello / Dito",
    "ring": "Anello",
    "neck": "Amuleto / Collana",
    "amulet": "Amuleto",
    "shield": "Scudo",
    "toolbelt": "Cintura degli Attrezzi",
    "lightsource": "Fonte di Luce",
    "furniture": "Arredamento",
    "_furniture": "Arredo",
    "container": "Contenitore",
    "window": "Finestra",
    "light": "Illuminazione",
    "deco": "Decorazione",
    "plantpot": "Pianta in Vaso",
    "facility": "Struttura di Servizio",
    "crafter": "Banco di Lavoro",
    "processor": "Impianto di Lavorazione",
    "generator": "Generatore",
    "mount": "Supporto da Parete",
    "ext": "Elemento da Esterno",
    "mech": "Meccanismo",
    "util": "Utilità",
    "bed": "Letto",
    "chair": "Sedia",
    "table": "Tavolo",
    "door": "Porta",
    "card": "Carta Collezionabile",
    "figure": "Statuetta",
    "item": "Oggetto",
    "_item": "Oggetto",
    "rune": "Runa Magica",
    "mod": "Strumento di Modifica",
    "bait": "Esca da Pesca",
    "book": "Libro",
    "_book": "Tomo",
    "scroll": "Pergamena",
    "ancientbook": "Tomo Antico",
    "spellbook": "Grimorio di Incantesimi",
    "skillbook": "Manuale di Abilità",
    "map": "Mappa",
    "other": "Altro",
    "junk": "Rottame",
    "globe": "Mappamondo",
    "pot": "Pentola / Vaso",
    "souvenir": "Cimelio / Ricordo",
    "garbage": "Rifiuti",
    "chara": "Personaggio",
    "bill": "Fattura / Tassa",
    "valuable": "Oggetto di Valore",
    "ability": "Abilità",
    "trap": "Trappola",
    "tool": "Attrezzo",
    "_tool": "Strumento",
    "instrument": "Strumento Musicale",
    "rod": "Verga Magica",
    "catalyst": "Catalizzatore Alchemico",
    "currency": "Valuta",
}

AREA_MAP = {
    "Room": {"name": "Stanza Comune", "detail": "Spazio abitativo generale per i residenti.", "textAssign": "Trasferisci"},
    "PrivateRoom": {"name": "Stanza Privata", "detail": "Alloggio personale riservato a un residente.", "textAssign": "Assegna"},
    "Workplace": {"name": "Posto di Lavoro", "detail": "Area designata per le mansioni lavorative.", "textAssign": "Impiega"},
    "Stockpile": {"name": "Deposito Scorte", "detail": "Zona per l'accatastamento e la conservazione dei materiali.", "textAssign": ""},
    "Dump": {"name": "Discarica", "detail": "Area per lo smaltimento e l'accumulo dei rifiuti.", "textAssign": ""},
    "Farm": {"name": "Campo Agricolo", "detail": "Terreno coltivabile per la semina e il raccolto.", "textAssign": ""},
    "Ranch": {"name": "Pascolo / Allevamento", "detail": "Recinto per l'allevamento e la cura degli animali.", "textAssign": "Manda al Pascolo"},
    "Gather": {"name": "Punto di Raccolta", "detail": "Luogo adibito al recupero di risorse naturali.", "textAssign": ""},
    "Prison": {"name": "Prigione", "detail": "Cella di reclusione per prigionieri e criminali.", "textAssign": "Incarcera"},
    "Bath": {"name": "Terme / Bagno Pubblico", "detail": "Luogo rilassante dove lavarsi e recuperare le forze.", "textAssign": ""},
    "Guest": {"name": "Stanza degli Ospiti", "detail": "Alloggio accogliente dedicato ai visitatori.", "textAssign": ""},
    "Drawing": {"name": "Salotto dei Ricevimenti", "detail": "Elegante sala per incontri e trattative diplomatiche.", "textAssign": ""},
}

ZONE_MAP = {
    "world": {"name": "Ylva", "detail": "Il vasto e misterioso mondo di Ylva."},
    "ntyris": {"name": "Tyris Settentrionale", "detail": "La regione continentale del nord, ricca di città e antiche rovine."},
    "elin_valley": {"name": "Foresta di Larna", "detail": "Una fitta foresta millenaria avvolta nella nebbia."},
    "cave_elona": {"name": "Caverna sulla Collina", "detail": "Un rifugio sotterraneo scavato nelle colline, teatro di antiche leggende."},
    "kapul": {"name": "Porto Kapul", "detail": "Vivace città portuale crocevia di marinai, mercanti e contrabbandieri."},
    "beach": {"name": "Spiaggia Silenziosa", "detail": "Un litorale calmo dove le onde si infrangono sui resti del naufragio."},
    "elin_snow": {"name": "Il Grande Ghiacciaio", "detail": "Terre perennemente congelate battute da tormente implacabili."},
    "elin_plain": {"name": "Pianure di Karana", "detail": "Distese erbose ondulate che collegano le principali vie commerciali."},
    "elin_plain2": {"name": "Pleasantview", "detail": "Un colle panoramico con una splendida vista sulla vallata."},
    "elin_plain3": {"name": "Il Giardino Perduto", "detail": "Un santuario floreale nascosto tra le colline."},
    "field": {"name": "Terre Selvagge", "detail": "I territori aperti al di fuori delle mura cittadine."},
    "user": {"name": "Mappa Personalizzata", "detail": "Mappa creata dalla comunità di giocatori."},
    "hospital": {"name": "Ospedale da Campo", "detail": "Struttura medica d'emergenza per i feriti dell'Etere."},
    "somewhere": {"name": "Luogo Sconosciuto", "detail": "Una destinazione remota e inesplorata."},
    "shelter": {"name": "Rifugio Anti-Etere", "detail": "Bunker blindato per ripararsi dal letale Vento dell'Etere."},
}

def apply_categories():
    path = os.path.join(GAME_DIR, 'Category.xlsx')
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    c_count = 0
    for r in range(2, ws.max_row + 1):
        cid = ws.cell(row=r, column=1).value
        if cid and str(cid).strip() in CATEGORY_MAP:
            ws.cell(row=r, column=3, value=CATEGORY_MAP[str(cid).strip()])
            c_count += 1
    wb.save(path)
    print(f"• Category.xlsx: {c_count} categorie localizzate in italiano!")

def apply_areas():
    path = os.path.join(GAME_DIR, 'Area.xlsx')
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column + 1)}
    a_count = 0
    for r in range(2, ws.max_row + 1):
        aid = ws.cell(row=r, column=headers.get('id', 1)).value
        if aid and str(aid).strip() in AREA_MAP:
            entry = AREA_MAP[str(aid).strip()]
            if 'name' in headers: ws.cell(row=r, column=headers['name'], value=entry['name'])
            if 'detail' in headers: ws.cell(row=r, column=headers['detail'], value=entry['detail'])
            if 'textAssign' in headers and entry['textAssign']: ws.cell(row=r, column=headers['textAssign'], value=entry['textAssign'])
            a_count += 1
    wb.save(path)
    print(f"• Area.xlsx: {a_count} tipologie di stanze ed edifici localizzate!")

def apply_zones():
    path = os.path.join(GAME_DIR, 'Zone.xlsx')
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column + 1)}
    z_count = 0
    for r in range(2, ws.max_row + 1):
        zid = ws.cell(row=r, column=headers.get('id', 1)).value
        if zid and str(zid).strip() in ZONE_MAP:
            entry = ZONE_MAP[str(zid).strip()]
            if 'name' in headers: ws.cell(row=r, column=headers['name'], value=entry['name'])
            if 'detail' in headers: ws.cell(row=r, column=headers['detail'], value=entry['detail'])
            z_count += 1
    wb.save(path)
    print(f"• Zone.xlsx: {z_count} zone e regioni localizzate!")

if __name__ == '__main__':
    apply_categories()
    apply_areas()
    apply_zones()
