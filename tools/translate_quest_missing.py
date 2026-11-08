import openpyxl

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/Quest.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    q_map = {
        ('fiama1', 'talkComplete'): 'Sì, sembra che tu ci sia riuscito. Perché non vai a sederti vicino al fuoco a berla? Oh, ed ecco una ricompensa per te.',
        ('fiama2', 'talkComplete'): 'completato',
        ('vernis_gold9', 'detail'): "La vera identità del drago annidato nelle profondità della miniera si è rivelata essere la prole del defunto Drago d'Acciaio Corgon. Torna in superficie e parla con Loytel a Vernis.",
        ('into_darkness2', 'detail'): '|Aspettiamo che Kettle faccia ritorno.',
        ('mokyu2', 'name'): 'Test',
        ('mokyu3', 'name'): 'Test',
        ('dummy', 'name'): 'Fantoccio di prova'
    }

    for r in range(2, ws.max_row+1):
        id_val = str(ws.cell(row=r, column=headers['id']).value)
        for (m_id, fld), val in q_map.items():
            if id_val == m_id and fld in headers:
                ws.cell(row=r, column=headers[fld]).value = val

    wb.save('Lang/IT/Game/Quest.xlsx')
    print('Updated Quest.xlsx')

if __name__ == '__main__':
    run()
