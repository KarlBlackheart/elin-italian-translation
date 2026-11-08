# coding: utf-8
"""
Elin Italian Localization - Small Drama Batch Localizer
Translates 19 drama storylines: guilds, masters, companions, NPCs.
"""

import os
import openpyxl

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DRAMA_DIR = os.path.join(MOD_DIR, 'Lang', 'IT', 'Dialog', 'Drama')

DRAMA_DATA = {
    "guild_master_fighter.xlsx": {
        10: "Solo chi è audace può conoscere il sapore della sconfitta. Solo chi conosce la sconfitta può comprendere il vero significato del coraggio."
    },
    "guild_master_mage.xlsx": {
        10: "Ah, un altro novizio entra nel nostro nido. Sarai capace di deporre uova d'oro o sei solo un altro corvo gracchiante?"
    },
    "guild_master_thief.xlsx": {
        10: "...Hai per caso desiderio di morire prima del tempo?"
    },
    "guild_master_merchant.xlsx": {
        10: "A che punto è l'incarico che ti ho affidato? Spero vivamente che tu non stia osando farmi perdere tempo prezioso.",
        15: "Bene, bene, cosa c'è? Non vedi che sono sommerso di registri contabili? Fuori il rospo, presto!",
        16: "Desidero entrare a far parte della Gilda dei Mercanti.",
        23: "Oh? Vorresti unirti alla mia illustre Gilda dei Mercanti?\n\nQualsiasi vero mercante sa bene che l'oro muove il mondo, ma la fiducia si conquista con le azioni.",
        24: "Ah, affascinante. Mi piace quello sguardo deciso e insolente. Molto bene, vediamo se vali qualcosa.",
        29: "Eccoti qui. Ho una prova per testare il tuo fiuto per gli affari.",
        30: "Ti ascolto.",
        31: "Ho cambiato idea.",
        36: "Mostrami di cosa sei capace.",
        42: "Torna quando avrai accumulato abbastanza oren per parlare da pari a pari con me."
    },
    "guild_doorman.xlsx": {
        9: "Sì, vedo che hai portato la missiva sigillata. Lascia che la esamini attentamente.",
        10: "Mmh, sembra proprio una lettera di raccomandazione autentica per l'ammissione alla gilda.",
        15: "Sembra che tu abbia cominciato ad apprendere i primi rudimenti delle arti oscure.",
        16: "Congratulazioni! Da questo momento sei formalmente ammesso nella Gilda dei Maghi. Fa' buon uso delle nostre conoscenze.",
        17: "Congratulazioni! Sei ufficialmente un membro della Gilda dei Guerrieri. Mostra il tuo valore sul campo di battaglia!",
        18: "Congratulazioni! Ora fai parte della Gilda dei Ladri. Non farti mai beccare con le mani nel sacco.",
        19: "Congratulazioni! Sei accolto tra i ranghi della Gilda dei Mercanti. Che il profitto guidi ogni tua mossa.",
        24: "Solo i membri ufficiali della gilda possono varcare questa soglia.",
        25: "Vattene, a meno che tu non abbia una lettera di raccomandazione formale.",
        26: "Non ho tempo da perdere con gli estranei.",
        27: "I non iniziati non sono i benvenuti oltre questo portone.",
        31: "Hai portato la prova della tua missione?",
        32: "Ecco qui.",
        33: "Non ancora.",
        38: "Ottimo lavoro. I tuoi meriti sono stati registrati nei nostri archivi.",
        39: "Torna quando avrai completato ciò che ti è stato ordinato.",
        44: "La gilda riconosce il tuo impegno e la tua dedizione.",
        45: "Benvenuto nel quartier generale.",
        50: "Che la fortuna assista i tuoi passi.",
        51: "Rimani fedele alle regole della gilda se ci tieni alla pelle.",
        56: "Porta sempre rispetto ai tuoi superiori.",
        57: "Hai domande sui nostri regolamenti interni?",
        58: "Come posso salire di rango?",
        59: "Niente, per ora.",
        64: "Completa le missioni bacheca e porta tributi alla gilda per accrescere la tua reputazione.",
        65: "Arrivederci."
    },
    "guild_clerk.xlsx": {
        10: "Oh, a quanto pare non sei ancora un membro ufficiale della #guild. Come sei riuscito a entrare quaggiù?",
        11: "Oh, a quanto pare non sei ancora un membro ufficiale della #guild. Come sei riuscito a entrare quaggiù?",
        12: "Oh, a quanto pare non sei ancora un membro ufficiale della #guild. Come sei riuscito a entrare quaggiù?",
        13: "Parla con Lady Marian, se hai intenzione di affiliarti alla #guild.",
        15: "Bentornato alla sede della #guild, #pc. Il tuo rango attuale è \"#guild_rank\".",
        16: "Desidero consultare i privilegi di gilda.",
        17: "Vorrei verificare i requisiti per il prossimo avanzamento.",
        18: "Arrivederci.",
        23: "Ecco a te la tabella con tutte le facilitazioni e i benefici riservati al tuo rango.",
        24: "Per salire di grado devi accumulare ulteriore contributo e dimostrare fedeltà incrollabile.",
        29: "Buona fortuna con i tuoi prossimi incarichi per conto della gilda!"
    },
    "mimu.xlsx": {
        10: ".........pi"
    },
    "raphael.xlsx": {
        8: "Ultimamente mi sono stancato dei soliti futili giochi d'amore. Ciò che bramo davvero è una passione travolgente e sconvolgente!"
    },
    "sorin.xlsx": {
        8: "Cosa c'è? Confido che sia abbastanza importante da giustificare l'interruzione delle mie meditazioni."
    },
    "vishnu.xlsx": {
        8: "...SALVE. IO SONO VISHNU. L'EQUILIBRIO PRIMORDIALE DEVE ESSERE PRESERVATO."
    },
    "poppy.xlsx": {
        10: "Bau-bau!",
        11: "Ti prendo con me, piccoletto!",
        15: "Woof!",
        22: "Bau-bau!"
    },
    "keeper_garden.xlsx": {
        8: "Cammina pure dove desideri. Ogni sentiero conduce alla medesima, immutabile visione.",
        10: "Riguardo ai gatti.",
        11: "Lo Sbocciare dei Legami.",
        26: "Perché mai i gatti sono creature così irresistibilmente adorabili, mi domando spesso?",
        31: "Il legame sincero tra compagni d'avventura è un fiore raro che sboccia solo con il tempo e la devozione.",
        36: "Fa' buon viaggio nel giardino dell'eternità."
    },
    "parttimer_jure.xlsx": {
        11: "La Chiesa della Dea Jure sta promuovendo una campagna speciale per nuove conversioni! Vorresti accostarti alla nostra fede?",
        12: "Sì, desidero convertirmi al culto di Jure.",
        13: "No, grazie.",
        21: "D'accordo, solo per essere assolutamente certi: intendi davvero convertire la tua religione al culto di Jure?",
        22: "Sì, ne sono certo.",
        23: "Ci ho ripensato.",
        28: "Che la benedizione misericordiosa di Jure vegli sempre sulla tua vita!",
        29: "Peccato! Jure piangerà per questo rifiuto... ma la porta del tempio resterà sempre aperta per te."
    },
    "ineien.xlsx": {
        11: "Benvenuto nella mia fortezza. Ho già sentito parlare delle tue imprese da Ashland. Ti stavamo aspettando.",
        12: "Avrei qualche domanda da farti.",
        14: "Arrivederci.",
        20: "In che modo posso esserti utile?",
        21: "Riguardo a questa fortezza.",
        22: "Riguardo alla situazione delle terre di Ylva.",
        27: "Questa fortezza è un baluardo strategico eretto per vigilare sulle minacce che emergono dal sottosuolo.",
        28: "Tempi oscuri incombono sul regno. Dobbiamo restare vigili e pronti a ogni evenienza."
    },
    "demitas.xlsx": {
        8: "Gli dèi e le antiche stirpi peccano di una superbia intollerabile. La loro millenaria esistenza ha ottenebrato il loro giudizio.",
        10: "Ho alcune domande da porti.",
        15: "Brami dunque attingere alla mia sterminata sapienza arcana?",
        16: "Riguardo alla prenotazione dei tomi magici.",
        17: "Riguardo alle reliquie antiche.",
        22: "Posso fare in modo che determinati tomi di incantesimi rari vengano riservati per te non appena disponibili.",
        23: "Le reliquie delle civiltà passate custodiscono un'energia immensa, ma anche terribili maledizioni per chi le maneggia senza cautela.",
        28: "Torna pure quando avrai sete di vera conoscenza."
    },
    "namamani.xlsx": {
        8: "Che posto è mai questo? Chi mi ha risvegliato?",
        10: "Riguardo agli abominii e alle creazioni artificiali.",
        24: "Porti con te uno strano e ingegnoso dispositivo. Lascia che gli dia un'occhiata da vicino.",
        25: "...Proprio come sospettavo. La circuiteria interna è approssimativa, i ritardi di segnale sono evidenti.",
        26: "Posso ricalibrarlo e ottimizzarne il rendimento, se mi procuri i componenti adatti.",
        27: "Cosa ti occorre?",
        32: "Portami frammenti di metallo conduttivo e un nucleo di cristallo intatto.",
        33: "D'accordo, mi metterò alla ricerca.",
        38: "Non metterci troppo tempo. L'efficienza è tutto in questo genere di meccanismi."
    },
    "big_sister.xlsx": {
        10: "C'è... c'è qualcuno laggiù nell'ombra?",
        11: "Guarda, #bigdaddy, un angelo... vedi?... un angelo splendente è sceso per noi!",
        12: "...Ehehe, la mia testolina fa di nuovo i capricci. Mi dispiace tanto, #bigdaddy... Ma vedi...",
        13: "Dobbiamo proteggere le Piccoline a ogni costo, vero #bigdaddy? Vero che non lasceremo che facciano loro del male?",
        14: "Sì, sorellina, ci penso io.",
        19: "Grazie, #bigdaddy... sei il mio eroe preferito di tutto il mondo!",
        20: "Stai sempre vicino a me, ti prego...",
        25: "Le Piccoline sono così dolci e fragili... non meritano di soffrire in questo posto freddo.",
        26: "Cullami ancora un po'...",
        31: "Ho sognato un prato pieno di margherite dove potevamo correre senza paura..."
    },
    "felmera.xlsx": {
        10: "L'arte, naturalmente, non è affatto un'esplosione! Essa risiede nel delicatissimo equilibrio tra grazia, armonia e composizione cromatica.",
        12: "Vorrei commissionarti un dipinto su tela.",
        13: "Desidero che tu perizi questo vecchio quadro.",
        18: "Cercati un altro pittore. Ho deciso di deporre definitivamente i pennelli... l'ispirazione mi ha abbandonato.",
        19: "Ti prego, ripensaci!",
        24: "Non insistere. Un artista senza musa è soltanto un artigiano che sporca tele bianche.",
        25: "Mostrami almeno cosa ti porta da me.",
        30: "Mmh... questo tratto di pennello... questa luce... È straordinario!",
        31: "Posso restaurarlo per te, ma richiederà tempo e pigmenti rari.",
        36: "Torna quando avrai trovato i colori adatti.",
        37: "L'arte richiede pazienza e dedizione assoluta."
    },
    "corgon.xlsx": {
        8: "(mokyu?)",
        23: "(mokyuu)",
        24: "Mokyuu!",
        25: "Mokyu.",
        30: "(mokyu... mokyu...)",
        31: "Mokyuuuu♪",
        36: "(ti osserva con occhi incuriositi e sbatte le palpebre)",
        37: "Mokyu!",
        42: "(scodinzola felice emettendo versi affettuosi)",
        43: "Mokyu~!"
    }
}

def apply_all():
    total_files = 0
    total_lines = 0
    
    for fname, lines_dict in DRAMA_DATA.items():
        fpath = os.path.join(DRAMA_DIR, fname)
        if not os.path.exists(fpath):
            continue
            
        wb = openpyxl.load_workbook(fpath)
        ws = wb.active
        headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1) if ws.cell(1, c).value}
        text_c = headers.get('text', 11)
        
        file_count = 0
        for r, text_it in lines_dict.items():
            if r <= ws.max_row:
                ws.cell(r, text_c).value = text_it
                file_count += 1
                total_lines += 1
                
        wb.save(fpath)
        total_files += 1
        print(f"File '{fname}': translated {file_count} lines.")
        
    print(f"\nCompleted! {total_files} drama files updated with {total_lines} authentic Italian lines!")

if __name__ == "__main__":
    apply_all()
