"""
Update remaining phrases in Element.xlsx and General.xlsx.
"""
import openpyxl

# 1. Element.xlsx
wb = openpyxl.load_workbook('Lang/IT/Game/Element.xlsx')
ws = wb['Element']
h = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column + 1)}
c_extra = h['textExtra']

ws.cell(row=418, column=c_extra).value = '+#1 Dominio Specializzato'
ws.cell(row=516, column=c_extra).value = '+#1 Proiettile Magico'
ws.cell(row=520, column=c_extra).value = '+#1 Proiettile da Tiro,Ricarica più Rapida'
ws.cell(row=525, column=c_extra).value = 'Apprende la postura "Maconomia"\nMaconomia Migliorata'
ws.cell(row=831, column=c_extra).value = "@ConBerserk,Aumenta i danni del bersaglio"
ws.cell(row=839, column=c_extra).value = '@ConIncognito,Attiva l\'effetto di campo "In Allerta"'

wb.save('Lang/IT/Game/Element.xlsx')
print('Updated Element.xlsx')

# 2. General.xlsx
wb_g = openpyxl.load_workbook('Lang/IT/Game/General.xlsx')
ws_g = wb_g['General']
hg = {ws_g.cell(row=1, column=c).value: c for c in range(1, ws_g.max_column + 1)}
c_t = hg['text']

ws_g.cell(row=85, column=c_t).value = 'Sig. Adams'
ws_g.cell(row=1603, column=c_t).value = '#1 ecopunti'

wb_g.save('Lang/IT/Game/General.xlsx')
print('Updated General.xlsx')
