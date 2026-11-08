import openpyxl, json

def run():
    wb = openpyxl.load_workbook('Lang/IT/Game/Element.xlsx')
    ws = wb.active
    headers = {ws.cell(row=1, column=c).value: c for c in range(1, ws.max_column+1)}

    # altname
    alt_map = {
        '0': 'vuoto,del vuoto,etereo',
        '910': 'fuoco,rosso,ardente,di fuoco',
        '911': 'gelo,blu,freddo,di ghiaccio',
        '912': 'fulmine,giallo,elettrico,folgorante',
        '913': 'ombra,nero,tetro,oscuro',
        '914': 'mente,folle,inquietante,psichico',
        '915': 'veleno,verde,velenoso,tossico',
        '916': 'morte,infernale,degli inferi,infernale',
        '917': 'suono,acustico,vibrante,sonoro',
        '918': 'nervi,nervino,intorpidente,neurale',
        '919': 'luce,bianco,splendente,sacro',
        '920': 'caos,caotico,del caos,caotico',
        '921': 'magia,magico,intriso di magia,magico',
        '922': 'etere,eterico,dell’etere,etereo',
        '923': 'acido,corrosivo,dell’acido,acido',
        '924': 'sangue,sanguinario,emorragico,del sangue',
        '925': 'impatto,d’urto,esplosivo,esplodente',
        '926': 'vuoto,annichilente,del vuoto,annientante',
        '927': 'gatto,felino,morbidoso,dei gatti'
    }

    # levelBonus
    lb_map = {
        '123': '5,Danno fisico ridotto del 10% con scudo\n10,Colpo di Scudo (Passiva)',
        '130': '15,Effetto incantamento arma +25%\n30,Effetto incantamento arma +50%',
        '131': '25,Penalità precisione ridotta\n50,Penalità precisione ridotta',
        '132': '5,ActRush',
        '226': '1,ActRide',
        '227': '1,ActParasite',
        '281': '1,AI_Steal',
        '289': '20,Valutazione di Qualità Pregiata',
        '2003': '1,actBuildTerrain\n3,actBuildInspect\n5,actBuildCut\n7,actBuildMine\n8,actBuildCollect\n9,actBuildRecipe\n10,actBuildAnywhere'
    }

    # textInc
    inc_map = {
        '60': 'La forza vitale di #your aumenta.',
        '61': 'Il mana di #your aumenta.',
        '62': 'Il vigore di #your aumenta.',
        '70': 'I muscoli di #your si sentono più forti.',
        '71': '#1 comincia a provare piacere quando subisce colpi pesanti.',
        '72': '#1 diventa più agile e destro.',
        '73': '#1 si sente più in sintonia con il mondo.',
        '74': '#1 si sente pervaso dalla sete di conoscenza.',
        '75': 'La volontà di #your si tempra.',
        '76': 'La magia di #your migliora.',
        '77': '#1 prova piacere a mettere in mostra il proprio corpo.',
        '78': '#1 viene baciato dalla dea bendata.',
        '79': 'La velocità di #your aumenta.',
        '80': 'L’intelligenza di #your aumenta.',
        '700': 'Sembra faccia davvero bene alla pelle!',
        '756': 'Ha proprio l’odore di una sorgente termale!',
        '758': 'Come osi cibarti della carne di un dio!',
        '1205': '#1 viene ammaliato dal sapore prelibato della carne umana.',
        '1206': 'La maledizione del maniero si è abbattuta su #1.',
        '1231': '#1 riceve l’illuminazione spirituale.',
        '1270': 'Stai conducendo una vita retta e virtuosa.',
        '1271': 'Stai conducendo una vita gravata da un pesante karma.',
        '1415': 'A #1 spunta una nuova coda.',
        '1510': 'La pelle di #your diventa più dura e coriacea.',
        '1511': 'La pelle di #your diventa più dura e coriacea.',
        '1512': 'Gli occhi di #your brillano nell’oscurità.',
        '1513': 'Gli occhi di #your brillano nell’oscurità.',
        '1514': 'Le articolazioni di #your diventano incredibilmente flessibili.',
        '1515': 'Le articolazioni di #your diventano incredibilmente flessibili.',
        '1516': 'All’improvviso il sangue di #your assume riflessi verdastri!',
        '1517': 'All’improvviso il sangue di #your assume riflessi verdastri!',
        '1518': 'Le gambe di #your diventano scattanti e snelle.',
        '1519': 'Le gambe di #your diventano scattanti e snelle.',
        '1520': 'Le braccia di #your diventano incredibilmente possenti.',
        '1521': 'Le braccia di #your diventano incredibilmente possenti.',
        '1522': 'La voce di #your diventa suadente e melodiosa.',
        '1523': 'La voce di #your diventa suadente e melodiosa.',
        '1524': 'Il cervello di #your viene meccanizzato!',
        '1525': 'Il cervello di #your viene meccanizzato!',
        '1526': 'Il sangue di #your comincia a ribollire di furore.',
        '1527': 'Il sangue di #your comincia a ribollire di furore.',
        '1528': '#1 sviluppa resistenza ai fulmini.',
        '1529': '#1 sviluppa resistenza ai fulmini.',
        '1530': 'Il corpo di #your viene purificato da ogni impurità.',
        '1531': 'Il corpo di #your viene purificato da ogni impurità.',
        '1532': 'La pelle di #your formicola piacevolmente.',
        '1533': 'La pelle di #your formicola piacevolmente.',
        '1550': '#1 perde peso e si sente leggero come una piuma.',
        '1551': 'Il gonfiore sul volto di #1 comincia a svanire.',
        '1552': 'I piedi di #your tornano alla loro forma normale.',
        '1553': 'Gli occhi di #your tornano normali.',
        '1554': 'Le piume sulla schiena di #your appassiscono e cadono.',
        '1555': 'Il collo di #your torna sottile ed elastico.',
        '1556': 'Un profondo senso di pace pervade il cuore di #your.',
        '1557': 'La testa di #your torna alle sue dimensioni consuete.',
        '1558': 'Le nuvole di pioggia smettono di seguire #1.',
        '1559': '#1 non è più schiavo della dipendenza da pozioni.',
        '1560': '#1 riacquista vigore e torna in piena salute.',
        '1561': '#1 ritrova la lucidità e la fiducia in se stesso.',
        '1562': 'Il pesante carapace di #your comincia a spaccarsi e cadere.',
        '1563': 'L’aspetto esteriore di #your torna alla normalità.',
        '1564': '#1 non funge più da batteria di mana vivente.',
        '1565': 'Le mani di #your tornano pulite e libere dal veleno.'
    }

    # textDec
    dec_map = {
        '60': 'La forza vitale di #your diminuisce.',
        '61': 'Il mana di #your si indebolisce.',
        '62': 'Il vigore di #your viene meno.',
        '70': 'I muscoli di #your si intorpidiscono e perdono tono.',
        '71': '#1 perde la sopportazione al dolore.',
        '72': '#1 diventa goffo e maldestro.',
        '73': '#1 perde contatto con il mondo che lo circonda.',
        '74': '#1 perde la curiosità e la sete di sapere.',
        '75': 'La determinazione di #your vacilla.',
        '76': 'La magia di #your subisce un declino.',
        '77': '#1 comincia a evitare lo sguardo della gente.',
        '78': 'La sfortuna si abbatte su #1.',
        '79': 'La velocità di #your diminuisce.',
        '80': '#1 sente la mente annebbiarsi.',
        '701': 'Come hai potuto mangiare un gatto?!',
        '758': 'Come osi cibarti della carne di un dio!',
        '1205': '#1 si libera dall’ossessione per la carne umana.',
        '1206': 'La maledizione del maniero è stata spezzata.',
        '1231': '#1 torna allo stato normale.',
        '1270': 'Non sei più la persona virtuosa di un tempo.',
        '1271': 'Non sei più la persona malvagia di un tempo.',
        '1510': 'La pelle di #your diventa pallida e fragile.',
        '1511': 'La pelle di #your diventa pallida e fragile.',
        '1512': 'La vista di #your si indebolisce.',
        '1513': 'La vista di #your si indebolisce.',
        '1514': 'Le articolazioni di #your scricchiolano rumorosamente.',
        '1515': 'Le articolazioni di #your scricchiolano rumorosamente.',
        '1516': 'Il metabolismo di #your rallenta vistosamente.',
        '1517': 'Il metabolismo di #your rallenta vistosamente.',
        '1518': 'Le gambe di #your si storcono in modo grottesco!',
        '1519': 'Le gambe di #your si storcono in modo grottesco!',
        '1520': 'Le braccia di #your si assottigliano e perdono vigore.',
        '1521': 'Le braccia di #your si assottigliano e perdono vigore.',
        '1522': 'La voce di #your assume un timbro spaventoso e sinistro.',
        '1523': 'La voce di #your assume un timbro spaventoso e sinistro.',
        '1524': 'Il cervello di #your comincia a degenerare.',
        '1525': 'Il cervello di #your comincia a degenerare.',
        '1526': '#1 sente la testa andare a fuoco.',
        '1527': '#1 sente la testa andare a fuoco.',
        '1528': '#1 perde la resistenza ai fulmini.',
        '1529': '#1 perde la resistenza ai fulmini.',
        '1530': 'Il corpo di #your viene profanato da energie impure.',
        '1531': 'Il corpo di #your viene profanato da energie impure.',
        '1532': 'I capelli di #your cominciano a cadere a ciocche.',
        '1533': 'I capelli di #your cominciano a cadere a ciocche.',
        '1550': '#1 comincia a generare un proprio campo gravitazionale.',
        '1551': 'Il volto di #your è ricoperto da orribili piaghe.',
        '1552': 'I piedi di #your mutano in zoccoli ferini.',
        '1553': 'Gli occhi di #your cominciano a moltiplicarsi.',
        '1554': 'Delle piume bizzarre spuntano dalla schiena di #your.',
        '1555': 'Il collo di #your diventa mostruosamente tozzo e taurino.',
        '1556': 'Un odio cieco e sanguinario domina l’anima di #your.',
        '1557': 'All’improvviso la testa di #your si espande fino a dimensioni mostruose.',
        '1558': 'Nubi temporalesche iniziano a seguire #1 ovunque vada.',
        '1559': 'Pozioni! Più pozioni!! All’improvviso #1 diventa schiavo delle pozioni.',
        '1560': '#1 si sente debole, infinitamente debole.',
        '1561': '#1 cade in uno stato di demenza senile e smarrimento.',
        '1562': 'Un pesante carapace chitinoso comincia a ricoprire la pelle di #your.',
        '1563': 'Un corno blasfemo spunta sulla testa di #1.',
        '1564': '#1 si trasforma in una batteria vivente di mana.',
        '1565': 'Gocce di acido e veleno iniziano a colare dalle mani di #your.'
    }

    # textAlt
    alt_text_map = {
        '2': 'Qualità,Scadente,Qualità Comune,Discreta Qualità,Pregiata Qualità,Qualità Superiore,Qualità Regale',
        '70': 'Grasso,Asciutto,Poco Umido,Morbido,Grasso,Succoso,Esplosione di Succhi',
        '71': 'Taglia,Taglia Fata,Taglia Putit,Taglia Zucca,Taglia Mostruosa,Taglia Mammut,Taglia Titano',
        '72': 'Freschezza,Morto,Quasi In Movimento,In Movimento,Vivace,Molto Vivace,Vivo',
        '73': 'Profumo,Puzzolente,Aroma Debole,Odore Gradevole,Fragrante,Molto Fragrante,Profumo Celestiale',
        '74': 'Sapore,Insipido,Poco Gustoso,Discreto,Squisito,Delizioso,Gusto Paradisiaco',
        '75': 'Spessore,Sottile,Normale,Consistente,Corposo,Molto Spesso,Densissimo',
        '76': 'Stagionatura,Acerbo,Fresco,Maturo,Stagionato,Invecchiato,Millenario',
        '77': 'Lucentezza,Opaco,Poco Lucido,Lucido,Brillante,Splendente,Ammaliante',
        '447': 'Lucentezza,Opaco,Poco Lucido,Lucido,Brillante,Splendente,Ammaliante',
        '652': 'Ecologia,Ostile a Ylva,Delicato su Ylva',
        '700': 'Collagene,Poco Collagene,Ricco di Collagene',
        '701': ',Gatto',
        '702': ',Miscela di Veleno',
        '703': ',Miscela Afrodisiaca',
        '704': ',,Miscela di Insetti',
        '705': ',,Ingrassante',
        '706': ',,Dimagrante',
        '707': ',,A Fette',
        '708': ',Carne Umana',
        '709': ',Contaminato',
        '710': ',Pasto di Sangue,Pasto di Sangue',
        '711': ',,Catechina',
        '750': 'Conforto,Inquietante,Poco Rilassante,Rilassante,Piacevole,Molto Piacevole,Estremamente Piacevole,Paradisiaco',
        '751': 'Rarità,Comune,Poco Insolito,Insolito,Raro,Super Raro,Ultra Raro',
        '752': 'Aspetto,Orribile,Preoccupante,Accattivante,Bello,Carino,Stravagante',
        '753': 'Antidoto,Tossico,Antidoto',
        '754': 'Nervino,Allucinogeno,Calmante',
        '755': 'Emostasi,Emorragico,Emostatico',
        '756': 'Sorgente Termale,Ghiacciata,Calda',
        '757': 'Freschezza,Avanzo,Appena Preparato',
        '758': ',Carne Divina',
        '759': ',,Alta Purezza',
        '760': 'Stimolante,Sonnifero,Risvegliante',
        '761': 'Rinvigorente,Drenante,Energizzante',
        '762': 'Cottura,Bruciato,Ben Cotto',
        '763': 'Aria,Soffocante,Respirabile',
        '764': ',,Cucina Creativa',
        '765': ',,Criptico',
        '766': ',,Proibito',
        '770': 'Gittata,Ristretta,Ampliata',
        '1229': 'Adam,Adam,Adam'
    }

    count = 0
    for r in range(2, ws.max_row+1):
        eid = str(ws.cell(row=r, column=headers['id']).value)
        
        # altname
        if eid in alt_map and 'altname' in headers:
            ws.cell(row=r, column=headers['altname']).value = alt_map[eid]
            count += 1
            
        # levelBonus
        if eid in lb_map and 'levelBonus' in headers:
            ws.cell(row=r, column=headers['levelBonus']).value = lb_map[eid]
            count += 1
            
        # textInc
        if eid in inc_map and 'textInc' in headers:
            ws.cell(row=r, column=headers['textInc']).value = inc_map[eid]
            count += 1
            
        # textDec
        if eid in dec_map and 'textDec' in headers:
            ws.cell(row=r, column=headers['textDec']).value = dec_map[eid]
            count += 1
            
        # textAlt
        if eid in alt_text_map and 'textAlt' in headers:
            ws.cell(row=r, column=headers['textAlt']).value = alt_text_map[eid]
            count += 1

        # special name row
        if eid == '5037' and 'name' in headers:
            ws.cell(row=r, column=headers['name']).value = 'nessun oggetto'
            count += 1

    wb.save('Lang/IT/Game/Element.xlsx')
    print(f'Applied {count} translations to Element.xlsx (Subset A)')

if __name__ == '__main__':
    run()
