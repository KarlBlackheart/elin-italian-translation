import openpyxl, json

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/Stat.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    stat_map = {
        ('77', 'detail'): 'Condizione in cui il consumo di mana è ridotto a costo di consumare più riserve di incantesimo.',
        ('83', 'name'): 'Tecnica Iai',
        ('83', 'detail'): 'Condizione in cui la precisione e il moltiplicatore di danno aumentano fino a un certo limite in base ai turni trascorsi senza attaccare.',
        ('83', 'strPhase'): 'Tecnica Iai',
        ('84', 'detail'): 'Condizione in cui la potenza di attacco aumenta ogni volta che un attacco viene schivato.',
        ('94', 'detail'): 'Condizione che induce il sonno nelle creature vicine. Consuma mana durante il mantenimento del canto.',
        ('97', 'detail'): 'Condizione che infonde coraggio alle creature vicine. Consuma mana durante il mantenimento del canto.',
        ('106', 'detail'): 'Condizione che infligge rovina alle creature vicine. Consuma mana durante il mantenimento del canto.',
        ('110', 'detail'): 'Condizione che infonde una volontà inflessibile alle creature vicine. Consuma mana durante il mantenimento del canto.',
        ('108', 'detail'): 'Condizione in cui ti comporti da viziato con chiunque.',
        ('23', 'textPhase2'): '#1 si sente leggermente meglio.',
        ('25', 'textPhase2'): '#1 può respirare di nuovo.',
        ('32', 'detail'): 'Condizione di confusione in cui i movimenti o il lancio di incantesimi vengono ostacolati.',
        ('33', 'detail'): 'Condizione di cecità in cui non puoi vedere nulla.',
        ('35', 'detail'): 'Condizione di follia mentale.',
        ('38', 'detail'): 'Condizione di sanguinamento in cui perdi salute a ogni azione.',
        ('39', 'detail'): 'Condizione di stordimento in cui i tuoi movimenti o il lancio di incantesimi vengono ostacolati.',
        ('66', 'detail'): 'Condizione di allucinazione in cui vedi cose che non esistono.',
        ('54', 'detail'): 'Condizione di congelamento in cui la velocità di movimento è ridotta.',
        ('51', 'detail'): 'Benedizione che rigenera gradualmente i punti ferita.',
        ('64', 'detail'): 'Rigenera gradualmente i punti ferita.',
        ('86', 'detail'): 'Condizione di risveglio graduale dalla sonnolenza. Ha un impatto negativo sull’aumento di affetto.',
        ('87', 'detail'): 'Condizione di immunità alla sonnolenza e al sonno, eccetto se esausto. Impedisce il recupero del vigore tramite cibo.',
        ('56', 'detail'): "Benedizione che potenzia l'arma dell'incantatore.",
        ('60', 'detail'): 'Benedizione che permette di percepire spiriti distanti.',
        ('61', 'detail'): 'Benedizione che conferisce invisibilità.',
        ('62', 'detail'): 'Benedizione che permette di vedere oggetti e creature invisibili.',
        ('63', 'detail'): 'Benedizione che consente di camuffarsi.',
        ('28', 'detail'): 'Benedizione che conferisce visione notturna.',
        ('30', 'detail'): 'Benedizione che protegge dalle maledizioni.',
        ('59', 'detail'): 'Benedizione che conferisce resistenza ai tre elementi primari.',
        ('42', 'detail'): 'Benedizione che suscita un ardore eroico.',
        ('91', 'detail'): 'Benedizione che permette di respirare sott’acqua.',
        ('71', 'detail'): 'Benedizione che incrementa il morale.',
        ('109', 'detail'): 'Un canto che ti infonde coraggio.',
        ('111', 'detail'): 'Un canto che ti infonde una volontà inflessibile.',
        ('93', 'name'): 'Furia Berserk',
        ('93', 'detail'): 'Condizione in cui vieni consumato dall’ira e puoi compiere solo azioni offensive. Tutti i danni inflitti aumentano.',
        ('93', 'strPhase'): 'Furia Berserk',
        ('88', 'detail'): 'Benedizione che risuscita automaticamente chi la possiede alla morte.',
        ('90', 'detail'): 'Benedizione che intensifica il desiderio di autodistruzione.',
        ('76', 'detail'): 'Benedizione che potenzia gli attacchi fisici per ogni nemico abbattuto.',
        ('78', 'detail'): 'Benedizione che evoca periodicamente piogge di champagne.',
        ('79', 'detail'): 'Benedizione che protegge la mente dalla pazzia.',
        ('43', 'detail'): 'Benedizione che conferisce levitazione.',
        ('48', 'detail'): 'Benedizione che incrementa la difesa.',
        ('49', 'detail'): 'Benedizione che infonde saggezza.',
        ('52', 'detail'): 'Benedizione che conferisce invulnerabilità.',
        ('82', 'detail'): 'Condanna che provoca la morte dopo un certo periodo. Può essere spezzata abbandonando la mappa o distruggendo l’esecutore.',
        ('67', 'detail'): 'Benedizione che potenzia gli attributi.',
        ('96', 'detail'): 'Benedizione che potenzia gli attributi.',
        ('69', 'detail'): "Trasformazione in un'altra forma.",
        ('70', 'detail'): "Trasformazione in un'altra forma.",
        ('92', 'detail'): "Trasformazione in un'altra forma.",
        ('98', 'detail'): "Trasformazione in un'altra forma.",
        ('102', 'detail'): "Trasformazione in un'altra forma.",
        ('107', 'detail'): "Trasformazione in un'altra forma.",
        ('105', 'detail'): "Trasformazione in un'altra forma.",
        ('103', 'detail'): 'Condizione in cui tutti gli attacchi mettono a segno colpi critici garantiti.',
        ('104', 'detail'): 'Condizione in cui la telecinesi ha un’efficacia ridotta.',
        ('50', 'name'): 'Miasma',
        ('50', 'detail'): 'Maledizione che danneggia gradualmente il bersaglio.',
        ('50', 'strPhase'): 'Miasma',
        ('44', 'detail'): 'Maledizione che applica una gravità opprimente. Blocca il teletrasporto e gli effetti di respinta.',
        ('47', 'detail'): 'Maledizione che ostacola le incantazioni.',
        ('57', 'detail'): 'Maledizione che dimezza la difesa.',
        ('65', 'detail'): 'Maledizione che prosciuga la fortuna.',
        ('68', 'detail'): 'Maledizione che recide la fede.',
        ('58', 'detail'): 'Maledizione che indebolisce le resistenze agli elementi.',
        ('89', 'detail'): 'Maledizione che indebolisce le resistenze attraverso incubi angoscianti.',
        ('11', 'detail'): 'Condizione in cui la guarigione naturale cessa a causa di una malattia.',
        ('37', 'detail'): 'Condizione di dipendenza in cui non puoi sopravvivere senza medicinali.',
        ('41', 'detail'): 'Condizione di nausea in cui vomiti tutto ciò che ingerisci.',
        ('100', 'detail'): 'Condizione di occultamento nelle tenebre.',
        ('24', 'detail'): 'Condizione di inzuppamento d’acqua che aumenta la vulnerabilità agli attacchi elettrici.',
        ('36', 'detail'): 'Condizione di ebbrezza in cui barcolli a intervalli regolari.',
        ('40', 'detail'): 'Condizione di forte agitazione in cui non puoi muoverti per un breve istante.',
        ('85', 'detail'): 'Condizione in cui il danno inflitto è ridotto e le possibilità di usare abilità sono limitate.',
        ('46', 'detail'): 'Condizione in cui le funzioni vitali si arrestano, lasciandoti completamente immobile.',
        ('53', 'detail'): 'Condizione di ricarica in cui non puoi adoperare armi a distanza.',
        ('95', 'detail'): 'Condizione in cui il tuo spirito vacilla e l’effetto Tenacia cessa di attivarsi.',
        ('0', 'detail'): 'Livello di sazietà. Più aumenta la fame, più la velocità cala, la guarigione naturale si arresta e infine sopraggiunge la morte per inedia.',
        ('0', 'textPhase2'): "Hai lo stomaco troppo pieno per muoverti!\nTi sei saziato a dovere.\nHai ancora un languorino.\nHai ancora un languorino.\nIl tuo stomaco brontola rumorosamente!\nIl tuo stomaco brontola rumorosamente!",
        ('1', 'detail'): 'Condizione influenzata dal peso del tuo carico. Più è pesante, più lenti saranno i movimenti.',
        ('13', 'detail'): 'Livello di instabilità mentale. Se peggiora, perdi il senno e muori.',
        ('4', 'textPhase2'): 'Non hai più sonno.',
        ('7', 'detail'): 'Livello di pulizia. Influenza i guadagni di affinità e migliora strigliandosi o rilassandosi alle sorgenti termali.',
        ('8', 'name'): 'Mana',
        ('45', 'detail'): 'Punizione divina.',
        ('34', 'detail'): 'Maledizione o benedizione che altera un’abilità.',
        ('73', 'detail'): 'Benedizione che diminuisce la probabilità di imbatterti in mostri.',
        ('74', 'detail'): 'Benedizione che aumenta la probabilità di imbatterti in mostri.',
        ('75', 'detail'): 'Benedizione che aumenta la probabilità di incontrare mostri metallici.',
        ('80', 'detail'): 'Benedizione che aumenta le probabilità di assistere a eventi bizzarri.',
        ('81', 'detail'): 'Benedizione che potenzia le difese immunitarie bloccando le sostanze nocive.'
    }

    count = 0
    for r in range(2, ws.max_row+1):
        id_val = str(ws.cell(row=r, column=headers['id']).value)
        for (m_id, fld), it_txt in stat_map.items():
            if id_val == m_id and fld in headers:
                ws.cell(row=r, column=headers[fld]).value = it_txt
                count += 1

    wb.save('Lang/IT/Game/Stat.xlsx')
    print(f'Applied translations to Stat.xlsx: {count} fields updated.')

if __name__ == '__main__':
    run()
