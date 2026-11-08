"""
Add the remaining 59 details to Thing.xlsx.
"""
import openpyxl

THING_FILE = 'Lang/IT/Game/Thing.xlsx'

ADDITIONAL_DETAILS = {
    'ticket_fortune': 'Un vecchio tagliando di carta consumato. Vi si legge: "Campagna di supporto per nuovi avventurieri! Carovana di Nino – La tua guida nel viaggio senza mappe!"',
    'fortune_ball': 'Una sfera di metallo usata nelle estrazioni della lotteria. Non è accessibile al pubblico, ma a volte viene portata fuori.',
    'map_treasure': 'Un antico brandello di pergamena contrassegnato da una "X" rossa. La mappa è consunta e sbiadita in più punti.',
    'map': 'Una pergamena topografica con segnate le posizioni di rovine ancestrali, cripte e caverne.',
    'book_plan': 'Un denso trattato accademico di amministrazione e governo. Leggerlo permette di acquisire un\'abilità di insediamento o una politica territoriale.',
    'book_skill': 'Un manuale pratico che consente di apprendere una specifica abilità dopo un\'attenta lettura.',
    'ticket_melilith': 'Un biglietto fatto a mano. La grafia è infantile, ma tracciata con incredibile cura e dedizione.',
    'book_story_home': 'Un diario colmo dei ricordi di Farris, vergato con mano magistrale. Tra le pagine sono disseminati piccoli ritratti e scarabocchi affettuosi.',
    'book_tutorial': 'Un vecchio volume logoro contenente guide e consigli per viandanti. Consente di rivedere i tutorial già consultati.',
    'backpack_holding': 'Una bisaccia incantata che alleggerisce misticamente il peso di tutto ciò che viene riposto al suo interno.',
    'quiver': 'Una faretra da spalla per frecce e dardi. Le munizioni qui custodite vengono ricaricate in via prioritaria.',
    'purse': 'Un borsellino di cuoio morbido per custodire monete e piccoli preziosi.',
    'grimoire': 'Un tomo arcano che ti permette di assimilare tutti i libri di incantesimi e i testi antichi riposti al suo interno mentre dormi. Va maneggiato con cautela. Non è possibile usare più grimori contemporaneamente.',
    'container_magic': 'Un forziere extradimensionale in grado di stipare una quantità strabiliante di oggetti.',
    'statue_weird': 'Una statuetta di legno intagliata grande quanto un palmo. Raffigura un neonato avvolto in teli sporchi e logori.',
    'plat': 'Una rara moneta di platino dal valore inestimabile, ambita dai maestri d\'armi e gilde.',
    'money3': 'Una radice di mandragora essiccata... o no?',
    'money2': 'Una barra di oro metallico purificato di elevata caratura.',
    'money': 'La valuta corrente ufficiale delle terre di North Tyris.',
    'medal': 'Una medaglia antica e lucente. Si mormora che collezionisti bizzarri farebbero follie per averla.',
    'pillow_itzpalt': 'Un cuscino da abbraccio con le sacre fattezze del dio degli elementi Itzpalt.',
    'sky_incinerator': 'Una fornace navale che produce i biglietti da navigatore dei cieli.',
    'sky_helm': 'Il timone di plancia che stabilisce la prossima rotta della nave volante.',
    'teleporter_gate': 'Un portale magico per ridiscendere in superficie.',
    'teleporter': 'Un cancello di curvatura che teletrasporta casualmente nei mondi condivisi da altri avventurieri.',
    'teleporter2': 'Un portale di selezione che consente di visitare una mappa già esplorata tra quelle create da altri avventurieri.',
    'recharger': 'Un dispositivo che permette il teletrasporto specificando la destinazione, purché collegata alla rete di insediamenti.',
    'machine_gene2': 'Un sofisticato macchinario scientifico per la manipolazione genetica.',
    'hitchingpost': 'Una colonna da ormeggio per legare la propria cavalcatura. Mentre è legata, è possibile cambiarne l\'aspetto di sella.',
    'scarecrow': 'Uno spaventapasseri che delimita il campo in cui i contadini svolgeranno i lavori agricoli.',
    'book_resident': 'Un registro tascabile che mostra l\'elenco dettagliato dei residenti.',
    'hammer': 'Un martello da lavoro per smontare e riciclare oggetti.',
    'hammer_strip': 'Uno strumento speciale per rimuovere i marchi di qualità dai mobili.',
    'brush_strip': 'Un solvente a pennello per sverniciare e rimuovere tinture applicate.',
    'butcherknife': 'Una mannaia da macellaio per macellare bestiame e ricavarne carni fresche.',
    'shears': 'Cesoie affilate per tosare la lana del bestiame.',
    'hoe': 'Una zappa agricola per dissodare e arare le zolle di terra.',
    'fishingRod': 'Una canna da pesca da lanciare nelle acque ricche di pesci.',
    'brush': 'Una spazzola morbida per strigliare e toelettare i propri compagni animali.',
    'dye': 'Una fiala di tintura liquida colorata per tingere abiti e manufatti.',
    'rune': 'Una pietra runica incisa con glifi arcani, utilizzata per infondere incantamenti negli equipaggiamenti.',
    'rune_free': 'Una pietra runica speciale che consente di applicare un incantamento senza consumare slot di incisione.',
    'gene': 'Un frammento di DNA che racchiude i tratti ereditari e fisici di un organismo.',
    'gene_brain': 'Un frammento genomico che conserva gli schemi di comportamento e pensiero dell\'organismo.',
    'ingot': 'Un lingotto di metallo raffinato e colato, pronto per la forgiatura.',
    'rope': 'Una corda solida, spessa e resistente. Abbastanza robusta da potervisi impiccare.',
    'wall': 'Una parete solida. Posizionabile su pavimenti o piattaforme rialzate.',
    'ramp': 'Una rampa inclinata. Posizionabile su pavimenti o piattaforme rialzate.',
    'pillar': 'Una colonna architettonica. Ruotandola è possibile regolarne l\'altezza.',
    'fence': 'Una staccionata o recinzione. Posizionabile su pavimenti o piattaforme rialzate.',
    'block': 'Un blocco strutturale solido per erigere muri e costruzioni.',
    'floor': 'Una mattonella o sezione di pavimento da posare a terra.',
    'deco': 'Un rivestimento decorativo per pavimenti. Non si consuma con l\'uso; utilizzandolo nuovamente nello stesso punto si rimuove la decorazione.',
    'platform': 'Una piattaforma sopraelevata installabile a mezz\'aria.',
    'obj': 'Un elemento d\'arredo scenico. Posizionabile su pavimenti o piattaforme.',
    '1276': 'Una pergamena sacra che fa compiere il grande viaggio a una moltitudine di Piccole Sorelle. Metà delle Piccole Sorelle nel Piccolo Giardino ascenderà, accrescendo la tua influenza.',
}

def run():
    wb = openpyxl.load_workbook(THING_FILE)
    ws = wb['Thing']
    headers = {ws.cell(1, c).value: c for c in range(1, ws.max_column+1)}

    det_c = headers['detail']
    id_c = headers['id']
    count = 0
    for r in range(2, ws.max_row+1):
        cid = str(ws.cell(r, id_c).value)
        if cid in ADDITIONAL_DETAILS:
            ws.cell(r, det_c, ADDITIONAL_DETAILS[cid])
            count += 1

    wb.save(THING_FILE)
    print(f"Applied {count} additional detail translations to Thing.xlsx")

if __name__ == '__main__':
    run()
