# coding: utf-8
"""
Elin Italian Localization - Drama fiama.xlsx Localizer
Translates all story dialogues of Fiama in the meadow/camp.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FIAMA_FILE = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama', 'fiama.xlsx')

FIAMA_LINES = {
    12: "Sembra che tu ti sia ripreso.",
    13: "...La tua testa sta bene?",
    16: "Grazie per avermi salvato la vita.",
    17: "Raccontami la favola della bestia mostruosa.",
    18: "Avrei qualche domanda da farti.",
    26: "Dunque hai deciso di stabilirti e vivere su queste terre. Ti auguro ogni bene per la tua nuova vita.\n\nPrima di andarmene, vorrei affidarti un piccolo compagno fedele. Cosa preferisci?",
    27: "Un cane fedele!",
    28: "Un gatto affettuoso!",
    29: "Un cucciolo d'orso!",
    30: "Una bambina smarrita!",
    43: "D'accordo. Abbine cura e trattalo con affetto.\n\nSe dovessi separarti dal tuo compagno durante i viaggi, soffia nel fischietto per richiamarlo al tuo fianco.",
    47: "Il compagno che ti avevo affidato è tornato da me zoppicando e ferito.\n\n...Ricordi cosa ti avevo raccomandato? Devi proteggerlo con più attenzione.",
    51: "Non c'è bisogno che tu mi ringrazi, ti trovavi semplicemente sulla mia strada.\n\nA dire il vero, a prima vista credevo fossi un cadavere abbandonato alle intemperie.",
    56: "C'era una volta un nobile principe che, per via di un oscuro maleficio, venne tramutato in un'orrenda e ripugnante bestia...",
    57: "Con il passare dei giorni, la fanciulla cominciò a scorgere la dolcezza nascosta sotto quell'aspetto mostruoso, finché il suo cuore non ne fu commosso...",
    58: "Una vecchia fiaba diffusa un po' ovunque.\n\nQuando ero bambina, il signor Cetrus me la raccontava spesso per farmi addormentare.",
    61: "Di cosa si tratta? Chiedi pure.",
    62: "Cos'è esattamente l'antica foresta?",
    63: "Parlami dei poteri arcani che possiedono gli Elea.",
    64: "Parlami dei 'Bambini Sognanti'.",
    65: "(Torna indietro)",
    70: "...Sul continente orientale, al di là dell'oceano che bagna Tyris, si estende una foresta primordiale sconfinata.\n\nUn intrico di alberi titanici dove la luce del sole non penetra mai, dimora ancestrale degli Elea.",
    74: "test",
    80: "Hai mai sentito parlare delle facoltà mistiche possedute dagli Elea di Vindale?\n\nSi dice che la loro comunione con la natura permetta loro di tessere la realtà come un arazzo.",
    84: "I Bambini Sognanti... poveri piccoli degli Elea a cui il destino ha negato la crescita.\n\nIl loro corpo riposa, mentre la loro coscienza vaga per sempre nel regno dei sogni.",
    85: "Non è ancora stata scoperta alcuna cura per questo misterioso morbo che chiamiamo 'il richiamo della foresta'.",
    86: "...",
    87: "...Quand'ero piccola, amavo trascorrere le giornate tra le fronde dell'antica foresta. Il signor Cetrus mi cercava disperato ogni volta.",
    91: "Vorrei tanto che tu morissi.",
    97: "Vorrei tanto che tu morissi.",
    102: "Non è che io disprezzi gli umani, ma ho sempre provato un'intesa più profonda e sincera con le bestie selvatiche.",
    103: "C'era una grotta buia vicino al luogo in cui stavamo riposando. Temo che quella creatura possa essersi smarrita laggiù...",
    109: "Ah, allora si era davvero inoltrato nella caverna! Che sollievo sapere che sta bene.\n\nTi ringrazio sentitamente per averlo riportato sano e salvo.",
    117: "A quanto pare ti stai abituando alla vita da queste parti. Prendi questo, ti tornerà utile per iniziare a coltivare la terra.",
    118: "Ash mi ha accennato di averti incaricato di esplorare la grotta.\n\n...Nymelle, un antico sepolcro dimenticato scavato nelle profondità della roccia.",
    119: "Non sappiamo quali pericoli e aberrazioni possano annidarsi nell'oscurità, perciò sii estremamente prudente.\n\nPossa la brezza guidare i tuoi passi.",
    126: "Prima che tu ti metta in cammino verso Nymelle, c'è un'abilità fondamentale che desidero insegnarti.\n\nCome scassinare una serratura usando un grimaldello.",
    132: "Non si apre, vero?\n\n...Esatto, perché ho sigillato quel forziere con una serratura di sicurezza particolarmente complessa.",
    133: "Puoi tenere sia il grimaldello sia il forziere. Quando sarai diventato un avventuriero esperto, prova a riaprirlo per scoprire cosa contiene.",
    145: "Come vola il tempo, non trovi? È già trascorsa un'intera settimana da quando ci siamo incontrati in questa radura.",
    146: "All'inizio sembravi così disorientato e insicuro, ma ora vedo la fierezza di un vero pioniere nei tuoi occhi.\n\nQuali sono i tuoi propositi per il futuro?",
    147: "Voglio esplorare i misteri e le profondità di Nefia.",
    148: "Voglio dedicarmi con tutto me stesso a sviluppare e abbellire il mio feudo.",
    149: "Voglio viaggiare e visitare ogni città e villaggio di questo mondo.",
    150: "Voglio compiere loschi incarichi proibiti di cui nessuno deve sapere nulla.",
    151: "Non voglio fare assolutamente nulla se non oziare.",
    152: "Voglio morire.",
    156: "Capisco... #last_choice...? È un proposito davvero caratteristico, calza a pennello con il tuo spirito.\n\nQualunque strada tu scelga di percorrere, ti auguro che le stelle veglino sul tuo cammino."
}

def run():
    wb = openpyxl.load_workbook(FIAMA_FILE)
    ws = wb.active
    
    # In drama files text is col 11 (text)
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
    text_c = headers.get('text', 11)
    
    count = 0
    for r, it_text in FIAMA_LINES.items():
        if r <= ws.max_row:
            ws.cell(r, text_c).value = it_text
            count += 1
            
    wb.save(FIAMA_FILE)
    print(f"fiama.xlsx completely translated: {count} lines!")

if __name__ == "__main__":
    run()
