"""
Translate final remaining strings in Element.xlsx, _adv.xlsx, _main.xlsx, and _tutorial.xlsx.
"""
import openpyxl

# 1. Element.xlsx
wb_elem = openpyxl.load_workbook('Lang/IT/Game/Element.xlsx')
ws_elem = wb_elem['Element']
headers_elem = {ws_elem.cell(row=1, column=c).value: c for c in range(1, ws_elem.max_column + 1)}
col_extra = headers_elem['textExtra']

# Row 519: Magic Manners
ws_elem.cell(row=519, column=col_extra).value = "Previene i danni agli oggetti\nPreviene i danni agli oggetti (Intero gruppo)"

# Row 528: Looter
ws_elem.cell(row=528, column=col_extra).value = "Probabilità del #1% che l'equipaggiamento raro rilasciato dai nemici sia di qualità superiore"

# Row 830: Bane
ws_elem.cell(row=830, column=col_extra).value = "@ConBane,Riduce la precisione del bersaglio"

wb_elem.save('Lang/IT/Game/Element.xlsx')
print("Updated Element.xlsx")


# 2. _adv.xlsx [god]
wb_adv = openpyxl.load_workbook('Lang/IT/Dialog/Drama/_adv.xlsx')
ws_god = wb_adv['god']
headers_adv = {ws_god.cell(row=1, column=c).value: c for c in range(1, ws_god.max_column + 1)}
col_text_adv = headers_adv['text']

ws_god.cell(row=30, column=col_text_adv).value = "- Ti avvicini all'altare, rievocando in silenzio le antiche leggende degli dèi.\n\n <color=olive>《#god_name》</color>\n\n#god_desc\n\n#god_benefit"
ws_god.cell(row=31, column=col_text_adv).value = "Venera #god_name."
ws_god.cell(row=32, column=col_text_adv).value = "(Allontanati)"
ws_god.cell(row=37, column=col_text_adv).value = "Una voce divina risuona nella tua mente.\n\n\"#godtalk_worship\""

wb_adv.save('Lang/IT/Dialog/Drama/_adv.xlsx')
print("Updated _adv.xlsx")


# 3. _main.xlsx [index] & [fiama]
wb_main = openpyxl.load_workbook('Lang/IT/Dialog/Drama/_main.xlsx')

# [index]
ws_main_idx = wb_main['index']
headers_main_idx = {ws_main_idx.cell(row=1, column=c).value: c for c in range(1, ws_main_idx.max_column + 1)}
col_text_main_idx = headers_main_idx['text']

main_index_map = {
    5: "Riunione a Corte",
    6: "Una Fanciulla Misteriosa",
    7: "L'Arte della Lira",
    8: "Il Sogno di Rem-Ido",
    9: "Il Signore di Willow",
    10: "(test) Il Signore di Willow 2",
    11: "(test) La Partenza",
    12: "(test) Il Tradimento",
    13: "(test) Collina di Nymelle",
    14: "Epilogo",
    15: "Titoli di Coda"
}
for r, t in main_index_map.items():
    ws_main_idx.cell(row=r, column=col_text_main_idx).value = t

# [fiama]
ws_fiama = wb_main['fiama']
headers_fiama = {ws_fiama.cell(row=1, column=c).value: c for c in range(1, ws_fiama.max_column + 1)}
col_text_fiama = headers_fiama['text']

fiama_map = {
    39: "(Dopo la partenza con Ash e Fiama, prossimamente)",
    54: "Lascia che ti parli un po' di me.",
    56: "Nacqui in un piccolo villaggio di Mysilia.\n\nMia madre morì prima che potessi rammentarla,\ne mio padre, un ubriacone violento, mi picchiava ogni giorno.\n\nI bambini del villaggio mi trattavano come una reietta,\ne i miei fratellastri mi consideravano un'estranea.",
    57: "Ho mai sorriso, anche una sola volta, in quel villaggio?\n\nPersino crescendo, quando imparai a difendermi da sola,\nil muro che avevo eretto tra me e il mondo non è mai crollato.",
    59: "Poco dopo la fine della Guerra dei Dieci Anni,\nil villaggio fu falciato dal morbo.\n\nAll'epoca avevo appena otto anni.\n\nDopo che mio padre morì di una fine miserabile e dolorosa,\ni miei fratelli lasciarono la casa per fuggire verso la capitale di Mysilia.",
    60: "Rimasi sola, affamata e abbandonata a me stessa,\ne rimasi a guardare con sollievo il cadavere deforme di mio padre decomporsi.",
    61: "...Fu in una notte d'inverno come quella\nche incontrai Ser Cetrus.",
    63: "Lord Cetrus, il Signore Elea,\nil Duca di Willow sulla collina,\nrideva spesso e suonava con gioia la sua lira di corno d'antilope\nogni volta che si faceva vedere nelle taverne malfamate del villaggio.\n\nE ogni volta che c'erano bambini attorno,\nintonava antiche saghe e leggende degli Elea.",
    64: "Tutti gli abitanti di Willow lo amavano profondamente.\n\nCosì, quando seppe di me e venne a cercarmi,\nnon provai alcuna paura.",
    65: "Prese la mia mano ruvida e graffiata\ne mi condusse nel calore della cucina della fortezza di Willow.",
    66: "Camminammo in silenzio lungo l'interminabile sentiero notturno verso il forte.\n\nE per tutto il tempo, non lasciò mai andare la mia mano che stringeva dolcemente.",
    82: "(Alla fortezza di Willow. Prossimamente)",
    84: "(Alla fortezza di Willow. Prossimamente)"
}
for r, t in fiama_map.items():
    ws_fiama.cell(row=r, column=col_text_fiama).value = t

wb_main.save('Lang/IT/Dialog/Drama/_main.xlsx')
print("Updated _main.xlsx")


# 4. _tutorial.xlsx [index]
wb_tut = openpyxl.load_workbook('Lang/IT/Dialog/Drama/_tutorial.xlsx')
ws_tut_idx = wb_tut['index']
headers_tut_idx = {ws_tut_idx.cell(row=1, column=c).value: c for c in range(1, ws_tut_idx.max_column + 1)}
col_text_tut_idx = headers_tut_idx['text']

tut_index_map = {
    5: "L'Inizio dell'Avventura",
    6: "Uso degli Attrezzi",
    7: "Cose Molto Importanti",
    8: "L'Equipaggiamento",
    9: "Il Cibo",
    10: "Risorse Lavorate",
    11: "Durezza dei Materiali",
    12: "Sonno e Riposo",
    13: "Proprietà degli Oggetti",
    14: "Mappa del Mondo",
    15: "Crescita e Talenti",
    16: "Fama",
    17: "Karma",
    18: "Condizione di Criminale",
    19: "Debolezza e Rigenerazione",
    20: "Danni da Acido all'Equipaggiamento",
    21: "Fede e Preghiera",
    22: "Morte e Penalità",
    23: "Rianimare Compagni e Abitanti",
    24: "La Fine dell'Infanzia",
    25: "Acque Pericolose",
    26: "Effetti di Campo",
    27: "Morbo dell'Etere",
    28: "Accampamento dei Viandanti",
    29: "Le Città",
    30: "Influenza",
    31: "Cassa delle Consegne",
    32: "Pietra del Focolare",
    33: "Lavoro e Passatempi",
    34: "Pascolo e Bestiame",
    35: "Il Problema dei Rifiuti",
    36: "Le Stagioni",
    37: "Dimostrazione di Nerun",
    38: "Allerta Invernale",
    39: "L'Ora del Ragnarok"
}

for r, t in tut_index_map.items():
    ws_tut_idx.cell(row=r, column=col_text_tut_idx).value = t

wb_tut.save('Lang/IT/Dialog/Drama/_tutorial.xlsx')
print("Updated _tutorial.xlsx")
