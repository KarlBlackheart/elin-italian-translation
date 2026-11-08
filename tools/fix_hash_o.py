"""
Fix all literal '#o' occurrences across the localization:
- Correct item names in Thing.xlsx
- Correct combat/status notifications in Stat.xlsx and Game.xlsx
- Correct quest descriptions in Quest.xlsx
- Correct dialog and god_talk lines
"""
import openpyxl

# 1. Thing.xlsx
wb_t = openpyxl.load_workbook('Lang/IT/Game/Thing.xlsx')
ws_t = wb_t['Thing']
h_t = {ws_t.cell(row=1, column=c).value: c for c in range(1, ws_t.max_column + 1)}
c_name = h_t['name']

thing_fixes = {
    250: 'antico libro rilegato',
    1811: 'piccola finestra di vetro',
    1812: 'piccola finestra di vetro',
    1814: 'piccola finestra di vetro',
    1884: 'piccolo peluche morbido',
    2356: 'pesce antico'
}
for r, val in thing_fixes.items():
    ws_t.cell(row=r, column=c_name).value = val

wb_t.save('Lang/IT/Game/Thing.xlsx')
print("Fixed Thing.xlsx item names")


# 2. Stat.xlsx
wb_s = openpyxl.load_workbook('Lang/IT/Game/Stat.xlsx')
ws_s = wb_s['Stat']

stat_fixes = [
    (12, 12, '#1 è avvelenato.\n#1 soffre per via di un potente veleno.'),
    (18, 12, '#1 è intrappolato nelle spire.'),
    (19, 12, '#1 è paralizzato.'),
    (24, 12, '#1 è stordito.'),
    (39, 12, '#1 si sente pervaso da eroismo.'),
    (41, 12, "#1 viene pervaso dall'euforia."),
    (44, 12, '#1 viene consumato da una furia cieca!'),
    (54, 12, '#1 riceve una condanna a morte.'),
    (57, 12, '#1 è stato trasmutato.'),
    (58, 12, '#1 è stato trasmutato.'),
    (59, 12, '#1 è stato trasmutato.'),
    (60, 12, '#1 è stato trasmutato.'),
    (68, 12, '#1 è avvolto dal miasma di #2.'),
    (69, 12, "#1 viene schiacciato da un'intensa gravità."),
    (70, 12, '#1 è avvolto da una fitta nebbia silente.'),
    (71, 12, '#1 si sente debole e spossato.'),
    (73, 12, '#1 subisce la scomunica.'),
    (73, 18, '#1 viene perdonato.'),
    (75, 12, '#1 è tormentato da un incubo tremendo.'),
    (76, 12, '#1 si sente malato.'),
    (81, 12, "#1 è fradicio d'acqua."),
    (99, 18, '#1 viene perdonato.')
]
for r, c, val in stat_fixes:
    ws_s.cell(row=r, column=c).value = val

wb_s.save('Lang/IT/Game/Stat.xlsx')
print("Fixed Stat.xlsx status messages")


# 3. Game.xlsx
wb_g = openpyxl.load_workbook('Lang/IT/Game/Game.xlsx')
ws_g = wb_g['Game']
ws_g.cell(row=191, column=4).value = '#1 viene interrotto.'
wb_g.save('Lang/IT/Game/Game.xlsx')
print("Fixed Game.xlsx r191")


# 4. Quest.xlsx
wb_q = openpyxl.load_workbook('Lang/IT/Game/Quest.xlsx')
ws_q = wb_q['Quest']
ws_q.cell(row=12, column=6).value = "Hai ricevuto un invito da Melilith, un'enigmatica nobildonna che abita in una villa isolata."
ws_q.cell(row=79, column=6).value = "Hai promesso di aiutare Loytel a saldare il suo debito colossale di 20 milioni di oren!"
ws_q.cell(row=95, column=6).value = "Hai raggiunto il Villaggio degli Esuli. Parla con gli anziani della comunità."
wb_q.save('Lang/IT/Game/Quest.xlsx')
print("Fixed Quest.xlsx quest descriptions")


# 5. dialog.xlsx
wb_d = openpyxl.load_workbook('Lang/IT/Dialog/dialog.xlsx')
ws_d = wb_d['rumor']
ws_d.cell(row=20, column=2).value = (
    "Se veneri Kumiromi, potresti trovare semi preziosi all'interno dei frutti.\n"
    "Se possiedi un'elevata resistenza all'illusione, sarai protetto dagli attacchi di follia.\n"
    "Benedire i bastoni magici è un'ottima idea: le cariche aumenteranno e il potere sarà più stabile.\n"
    "Mentre sei bagnato, subisci pochissimi danni da fuoco, ma i colpi di fulmine ti faranno molto più male!\n"
    "Vomitare troppo frequentemente porta rapidamente all'anoressia. In caso di malattia, idratati con bevande nutrienti.\n"
    "Le pozioni benedette di ripristino attributi potenziano temporaneamente il corpo e la mente oltre i loro limiti normali.\n"
    "Contro i nemici più temibili, prova a lanciare addosso a loro pozioni maledette per indebolirli drasticamente!"
)
wb_d.save('Lang/IT/Dialog/dialog.xlsx')
print("Fixed dialog.xlsx rumor r20")


# 6. god_talk.xlsx
wb_gt = openpyxl.load_workbook('Lang/IT/Data/god_talk.xlsx')
ws_gt = wb_gt['1']
ws_gt.cell(row=11, column=5).value = 'Ueee♪ Sei tornato? Sei tornato!'
wb_gt.save('Lang/IT/Data/god_talk.xlsx')
print("Fixed god_talk.xlsx r11")
