"""
Comprehensive fix for all detected localization bugs:
- Remove residual Chinese classifiers in Thing.xlsx (2,177 rows)
- Translate residual Chinese text in Chara, Block, Word, CharaText, casino_clerk, farris
- Fix placeholder mismatches in dialog.xlsx, guild_clerk, loytel, big_sister, fiama
"""
import openpyxl

# 1. Thing.xlsx: clear 'unit' where 'unit_EN' is None or empty
wb_thing = openpyxl.load_workbook('Lang/IT/Game/Thing.xlsx')
ws_thing = wb_thing['Thing']
h_thing = {ws_thing.cell(row=1, column=c).value: c for c in range(1, ws_thing.max_column + 1)}
col_u = h_thing['unit']
col_u_en = h_thing['unit_EN']

cleared_units = 0
for r in range(2, ws_thing.max_row + 1):
    u_en = ws_thing.cell(row=r, column=col_u_en).value
    if not u_en or str(u_en).strip() == '':
        if ws_thing.cell(row=r, column=col_u).value is not None:
            ws_thing.cell(row=r, column=col_u).value = None
            cleared_units += 1

wb_thing.save('Lang/IT/Game/Thing.xlsx')
print(f"Cleared {cleared_units} residual classifier units in Thing.xlsx")


# 2. Chara.xlsx: row 194 (farris)
wb_chara = openpyxl.load_workbook('Lang/IT/Game/Chara.xlsx')
ws_chara = wb_chara['Chara']
h_chara = {ws_chara.cell(row=1, column=c).value: c for c in range(1, ws_chara.max_column + 1)}
ws_chara.cell(row=194, column=h_chara['detail']).value = (
    "La maggiore delle due figlie del capovillaggio di Olvina. "
    "Pur riponendo aspettative nel Signore, non riesce in alcun modo ad accettare "
    "che egli abbia simulato la propria morte, e ritiene che il Signore dovrebbe essere morto sul serio."
)
wb_chara.save('Lang/IT/Game/Chara.xlsx')
print("Updated Chara.xlsx (farris detail)")


# 3. Block.xlsx: rows 16 & 31
wb_block = openpyxl.load_workbook('Lang/IT/Game/Block.xlsx')
ws_block = wb_block['Block']
h_block = {ws_block.cell(row=1, column=c).value: c for c in range(1, ws_block.max_column + 1)}
ws_block.cell(row=16, column=h_block['detail']).value = "Un punto d'appoggio indispensabile per qualsiasi costruzione."
ws_block.cell(row=31, column=h_block['detail']).value = "Un punto d'appoggio indispensabile per qualsiasi costruzione."
wb_block.save('Lang/IT/Game/Block.xlsx')
print("Updated Block.xlsx (detail scaffolding)")


# 4. Word.xlsx: rows 384, 401, 405, 418, 421, 422
wb_word = openpyxl.load_workbook('Lang/IT/Game/Word.xlsx')
ws_word = wb_word['Word']
h_word = {ws_word.cell(row=1, column=c).value: c for c in range(1, ws_word.max_column + 1)}
c_name = h_word['name']
ws_word.cell(row=384, column=c_name).value = "Mamma"
ws_word.cell(row=401, column=c_name).value = "Rivelatore"
ws_word.cell(row=405, column=c_name).value = "Padrone"
ws_word.cell(row=418, column=c_name).value = "Figlio del Cielo"
ws_word.cell(row=421, column=c_name).value = "Imperatore Celeste"
ws_word.cell(row=422, column=c_name).value = "Capotribù"
wb_word.save('Lang/IT/Game/Word.xlsx')
print("Updated Word.xlsx")


# 5. CharaText.xlsx: rows 10, 44, 78, 80, 81, 82, 89, 90
wb_ct = openpyxl.load_workbook('Lang/IT/Game/CharaText.xlsx')
ws_ct = wb_ct['CharaText']
h_ct = {ws_ct.cell(row=1, column=c).value: c for c in range(1, ws_ct.max_column + 1)}

# r10 Thug
ws_ct.cell(row=10, column=h_ct['aggro']).value = "「Vuoi fare a botte?」\n「Ti spoglio di tutto quello che hai!」"
ws_ct.cell(row=10, column=h_ct['dead']).value = "「Maledetto...」\n「Non finisce mica qui...」"
ws_ct.cell(row=10, column=h_ct['kill']).value = "「Dormi per sempre!」"

# r44 Brat / bully
ws_ct.cell(row=44, column=h_ct['kill']).value = "「Provaci ancora a prendermi in giro!」\n「Aahahahahahah!」\n「Va' all'inferno!」"

# r78 Chicken
ws_ct.cell(row=78, column=h_ct['calm']).value = "「Coccodè...」\n「Co-co-co...」\n「Coccodè」"
ws_ct.cell(row=78, column=h_ct['aggro']).value = "「Chicchirichì—!」"

# r80 Sheep
ws_ct.cell(row=80, column=h_ct['calm']).value = "「Bee」\n「Beeh~」\n「Beee」\n「Beee~♪」"
ws_ct.cell(row=80, column=h_ct['aggro']).value = "「Beee—!」"

# r81 Dog
ws_ct.cell(row=81, column=h_ct['calm']).value = "「Bau」\n「Bau bau!」"
ws_ct.cell(row=81, column=h_ct['aggro']).value = "「Grrr!」"
ws_ct.cell(row=81, column=h_ct['dead']).value = "「Guaio...」"

# r82 Wild dog
ws_ct.cell(row=82, column=h_ct['aggro']).value = "「Grrr bau!」"
ws_ct.cell(row=82, column=h_ct['dead']).value = "「Guaio...」"

# r89 Cow
ws_ct.cell(row=89, column=h_ct['calm']).value = "「Muu」\n「Muuu—」\n「Muuu」"

# r90 Pixie / Spirit
ws_ct.cell(row=90, column=h_ct['aggro']).value = "「Ora stai davvero esagerando!」\n「Ti meriti una bella punizione!」"
ws_ct.cell(row=90, column=h_ct['dead']).value = "「Non vale!」"

wb_ct.save('Lang/IT/Game/CharaText.xlsx')
print("Updated CharaText.xlsx")


# 6. casino_clerk.xlsx [1] r14
wb_cas = openpyxl.load_workbook('Lang/IT/Dialog/Drama/casino_clerk.xlsx')
ws_cas = wb_cas['1']
h_cas = {ws_cas.cell(row=1, column=c).value: c for c in range(1, ws_cas.max_column + 1)}
ws_cas.cell(row=14, column=h_cas['text']).value = (
    "La campana d'oro preannuncia la buona sorte... Benvenuto a bordo della 'Campana della Fortuna', "
    "l'unico dirigibile-casinò del mondo! Divertiti finché la tua borsa non sarà completamente vuota."
)
wb_cas.save('Lang/IT/Dialog/Drama/casino_clerk.xlsx')
print("Updated casino_clerk.xlsx")


# 7. farris.xlsx [farris] r116
wb_far = openpyxl.load_workbook('Lang/IT/Dialog/Drama/farris.xlsx')
ws_far = wb_far['farris']
h_far = {ws_far.cell(row=1, column=c).value: c for c in range(1, ws_far.max_column + 1)}
ws_far.cell(row=116, column=h_far['text']).value = "V-va bene..."
wb_far.save('Lang/IT/Dialog/Drama/farris.xlsx')
print("Updated farris.xlsx")


# 8. guild_clerk.xlsx [1] r15 & r29
wb_gc = openpyxl.load_workbook('Lang/IT/Dialog/Drama/guild_clerk.xlsx')
ws_gc = wb_gc['1']
h_gc = {ws_gc.cell(row=1, column=c).value: c for c in range(1, ws_gc.max_column + 1)}
ws_gc.cell(row=15, column=h_gc['text']).value = 'Bentornato alla #guild, #pc. Il tuo rango attuale è "#guild_title". In cosa posso esserti utile oggi?'
ws_gc.cell(row=29, column=h_gc['text']).value = 'Se mi parli quando il tuo contributo sarà sufficiente, potrai salire di rango nella #guild. Avanzando di rango potrai usufruire di servizi di livello superiore, perciò dai il massimo per farti valere!'
wb_gc.save('Lang/IT/Dialog/Drama/guild_clerk.xlsx')
print("Updated guild_clerk.xlsx")


# 9. loytel.xlsx [loytel] r446
wb_loy = openpyxl.load_workbook('Lang/IT/Dialog/Drama/loytel.xlsx')
ws_loy = wb_loy['loytel']
h_loy = {ws_loy.cell(row=1, column=c).value: c for c in range(1, ws_loy.max_column + 1)}
ws_loy.cell(row=446, column=h_loy['text']).value = "Ah, stai già preparando la colazione? Che ammirevole dedizione così presto la mattina, Quru... Quru.."
wb_loy.save('Lang/IT/Dialog/Drama/loytel.xlsx')
print("Updated loytel.xlsx")


# 10. big_sister.xlsx [big_sister] r14 & r26
wb_bs = openpyxl.load_workbook('Lang/IT/Dialog/Drama/big_sister.xlsx')
ws_bs = wb_bs['big_sister']
h_bs = {ws_bs.cell(row=1, column=c).value: c for c in range(1, ws_bs.max_column + 1)}
ws_bs.cell(row=14, column=h_bs['text']).value = "...Sì, è la nostra sacra missione. Proteggere le Piccole Sorelle. È il nostro... vero, #bigdaddy? Non perdoneremo mai chiunque osi far del male alle Piccole Sorelle."
ws_bs.cell(row=26, column=h_bs['text']).value = "...Eheh, una nuova Piccola Sorella è venuta da noi, #bigdaddy. Non è più smarrita. Da adesso in poi la proteggeremo a ogni costo... vero, #bigdaddy?\n\nGrazie, angelo... Ehi, #bigdaddy, credi che gli angeli esistano davvero? Se ci fossero davvero gli angeli, quanto sarebbe meraviglioso..."
wb_bs.save('Lang/IT/Dialog/Drama/big_sister.xlsx')
print("Updated big_sister.xlsx")


# 11. fiama.xlsx [fiama] r119
wb_fia = openpyxl.load_workbook('Lang/IT/Dialog/Drama/fiama.xlsx')
ws_fia = wb_fia['fiama']
h_fia = {ws_fia.cell(row=1, column=c).value: c for c in range(1, ws_fia.max_column + 1)}
ws_fia.cell(row=119, column=h_fia['text']).value = "Non sappiamo quali pericoli e aberrazioni possano annidarsi nell'oscurità, perciò sii estremamente prudente.\n\nPossa la brezza guidare sempre i tuoi passi, #pc."
wb_fia.save('Lang/IT/Dialog/Drama/fiama.xlsx')
print("Updated fiama.xlsx")


# 12. dialog.xlsx
wb_dia = openpyxl.load_workbook('Lang/IT/Dialog/dialog.xlsx')
# general r87
ws_dia_gen = wb_dia['general']
h_dia_gen = {ws_dia_gen.cell(row=1, column=c).value: c for c in range(1, ws_dia_gen.max_column + 1)}
ws_dia_gen.cell(row=87, column=h_dia_gen['text']).value = "Ne sei davvero sicuro? (Il tuo gruppo attuale verrà sciolto e ne verrà formato uno nuovo con te e #tg)."

# rumor r5
ws_dia_rumor = wb_dia['rumor']
h_dia_rumor = {ws_dia_rumor.cell(row=1, column=c).value: c for c in range(1, ws_dia_rumor.max_column + 1)}
ws_dia_rumor.cell(row=5, column=h_dia_rumor['text']).value = (
    "Non ho niente da fare.\n"
    "Eh? Che cosa vuoi?\n"
    "Sei un avventuriero, giusto? Hai qualche notizia dalle terre lontane?\n"
    "La Lega Eterna? Mai sentita nominare.\n"
    "Niente batte una buona vecchia birra crim dopo una dura giornata di lavoro.\n"
    "I gatti... perché sono così carini?\n"
    "#aka? Mai sentito parlare di te."
)

wb_dia.save('Lang/IT/Dialog/dialog.xlsx')
print("Updated dialog.xlsx")
