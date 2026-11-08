"""
Elin Italian Localization - _tutorial.xlsx (Drama Tutorial & Fairy Nerun)
Localizza i dialoghi della fatina Nerun e le spiegazioni narrative del prologo/tutorial.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TUTORIAL_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama', '_tutorial.xlsx')

TUTORIAL_LINES = {
    13: "...",
    14: "Lo senti anche tu?\nQuest'aria insolita... c'è una speciale 'Legge del Mondo' che governa questo posto.",
    15: "Esatto: qualcosa come un 'Effetto Ambientale' sta pulsando attraverso la terra.",
    16: "Un Effetto Ambientale è una regola speciale che si applica unicamente alla mappa in cui ti trovi.",
    17: "C'è una forza primordiale qui, abbastanza potente da piegare le leggi stesse della natura.",
    18: "...Fai molta attenzione mentre avanzi.",

    23: "Dlin-dlin!\nRiesci a crederci?\nSono già passati duemila giorni da quando hai iniziato la tua avventura!",
    24: "...",
    25: "Caspita, sei davvero longevo, non è vero?",
    26: "Io?\n...Che insolente! Sono pur sempre una giovane e radiosa fanciulla fatata, che credevi?!",
    27: "Ma ahimè!\nQuesto mondo non durerà in eterno.\nLa fine si avvicina inesorabile...",
    28: "L'Ora del Ragnarok...\nPersino io non so con esattezza cosa accadrà quando i fili del destino si spezzeranno.",
    29: "Purtroppo, non è ancora stato trovato alcun modo per scongiurare questo tragico epilogo...",
    30: "...",
    31: "Vorrei continuare ad andare all'avventura insieme a te per sempre...",
    32: "Quindi...\nChe ne dici se d'ora in avanti facciamo scorrere il tempo un po' più lentamente?",

    35: "Guarda un po', un'erba medicinale!",
    36: "A volte tra i prati selvatici crescono piante dai colori sgargianti:\nsono erbe officinali, o talvolta erbe aromatiche.",
    37: "Naturalmente possono essere usate anche come condimento in cucina!\nSe le macini in un mortaio di pietra, puoi ricavarne polveri curative!",
    38: "Perché non apri il tuo zaino e dai un'occhiata all'erba che hai appena raccolto?",
    39: "Vedrai le sue proprietà magiche indicate tra parentesi quadre, come 【Emostatico】!",
    40: "Per esempio, se crei una benda usando un'erba con proprietà emostatiche, guarirai le ferite da sanguinamento molto più in fretta!",
    41: "Ogni colore di erba possiede effetti terapeutici diversi,\nquindi è sempre saggio farne una bella scorta di ogni tonalità!",
    42: "Capito il trucco? 'Color-ite' le tue tasche!",
    43: "...",

    47: "Dlin-dlin!\nL'inverno... l'inverno sta arrivando!",
    48: "Assicurati di completare la raccolta di tutti i raccolti nei campi.",
    49: "In inverno la terra gela e le piante non crescono affatto!\nFaresti meglio a terminare il raccolto prima che la prima neve imbianchi il suolo.",
}

def apply():
    print(f"Caricamento di {TUTORIAL_FILE}...")
    wb = openpyxl.load_workbook(TUTORIAL_FILE)
    ws = wb.active

    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column + 1)}
    text_c = headers.get('text', 11)

    translated = 0
    for r, it_text in TUTORIAL_LINES.items():
        if r <= ws.max_row:
            ws.cell(row=r, column=text_c, value=it_text)
            translated += 1

    wb.save(TUTORIAL_FILE)
    print(f"[OK] Applicate {translated} battute narrative a _tutorial.xlsx!")

if __name__ == '__main__':
    apply()
