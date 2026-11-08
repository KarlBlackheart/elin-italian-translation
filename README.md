# Mod Traduzione Italiana per Elin (Compatibile Steam Workshop)

Benvenuto nel progetto di **Traduzione Italiana di Elin**, ambientato nel ricco e profondo mondo roguelike di Ylva (creato da Noa / Lafrontier).

> ### ⚠️ Nota sulla Traduzione (Realizzata tramite IA)
> Questa localizzazione è stata creata e adattata con l'ausilio dell'**Intelligenza Artificiale (AI)**.
> Non si intende rivendicare alcun merito indebito: il progetto è nato unicamente dal desiderio di rendere *Elin* accessibile e godibile in italiano per tutti gli appassionati.
> Sebbene i testi siano stati calibrati a partire dalle fonti originali (giapponese e inglese) e testati contro le meccaniche del gioco, potrebbero esserci imprecisioni, refusi o espressioni migliorabili. Qualsiasi suggerimento, correzione o segnalazione da parte della community è caldamente incoraggiata e apprezzata!

Questo repository contiene l'intero pacchetto mod pronto all'uso, compatibile con il sistema nativo di localizzazione di Elin e conforme agli standard di **Steam Workshop**.

---

## 📁 Struttura della Mod

```
d:\Mod\Elin\
├── package.xml               # Metadati della mod per Elin e Steam Workshop
├── preview.jpg               # Grafica di anteprima 512x512 per il Workshop
├── README.md                 # Questa guida
├── link_mod.bat              # Script per collegare la mod in Elin/Package senza toccare i file originali
├── tools/                    # Strumenti di manutenzione e traduzione
│   ├── sync_update.py        # Sincronizza la mod con ogni nuova patch di Elin
│   ├── status.py             # Calcola le statistiche e l'avanzamento della traduzione
│   ├── translate_core.py     # Script per applicare traduzioni al nucleo di sistema
│   ├── translate_helper.py   # Utility per tradurre e confrontare JA/EN/IT
│   └── validate.py           # Validatore di integrità e sintassi dei file XLSX/TXT
└── Lang/
    └── IT/                   # Cartella della lingua italiana (codice 'IT')
        ├── lang.ini          # Regole di grammatica, articoli e font del motore di gioco
        ├── version.ini       # Versione sincronizzata con la build di Elin
        ├── Data/             # Dialoghi delle divinità, frasi PNG e nomi
        ├── Dialog/           # Dialoghi comuni e 36 file di trame narrative (Drama)
        ├── Game/             # 40 fogli Excel con statistiche, oggetti, razze, UI, ecc.
        ├── Text/             # Guide, libri di lore, pergamene e notizie
        └── Widget/           # Frasi e reazioni dei widget (Nenene, Nerun, Yukkuri)
```

---

## 🌐 Riferimento Multilingue (Giapponese, Inglese, Italiano)

Poiché Elin è sviluppato da un autore giapponese, molte sfumature e riferimenti sono presenti in **Giapponese (`_JP`)**.
Tutti i fogli Excel nella cartella `Lang/IT/Game/` e `Lang/IT/Dialog/` presentano le colonne affiancate:
- `colonna` (es: `name`, `text`, `detail`): Il testo in **Italiano** visibile in gioco.
- `colonna_EN`: Il testo di riferimento in **Inglese**.
- `colonna_JP`: Il testo originale in **Giapponese**.

Le voci non ancora tradotte mostrano automaticamente il testo inglese come fallback sicuro, eliminando completamente qualsiasi residuo in cinese.

---

## 🔄 Come Aggiornare la Mod ad Ogni Patch di Elin

Elin riceve aggiornamenti frequenti in Early Access. Per allineare la mod all'ultima versione del gioco senza perdere le traduzioni già fatte:

1. Assicurati che Elin sia aggiornato su Steam (`Z:\Giochi\SteamLibrary\steamapps\common\Elin`).
2. Apri un terminale nella cartella `d:\Mod\Elin` ed esegui:
   ```cmd
   python tools/sync_update.py
   ```
3. Lo script:
   - Rileverà automaticamente la nuova versione del gioco.
   - Aggiungerà le nuove voci (oggetti, quest, dialoghi) ai fogli della mod con fallback inglese.
   - Aggiornerà eventuali testi inglesi o giapponesi modificati dal dev.
   - **Preserverà al 100% tutte le traduzioni italiane già completate**.
   - Aggiornerà `version.ini`.

---

## 📊 Controllo dell'Avanzamento

Per visualizzare in qualsiasi momento quante voci sono state tradotte per ogni categoria:
```cmd
python tools/status.py
```

Per verificare che tutti i file Excel e i tag (`#1`, `{...}`) siano sani prima del test:
```cmd
python tools/validate.py
```

---

## 🎮 Come Testare la Mod nel Gioco (Senza toccare i file originali)

1. Fai doppio clic su `link_mod.bat`.
   - Verrà creato un collegamento (Junction NTFS) in `Z:\Giochi\SteamLibrary\steamapps\common\Elin\Package\Mod_Italian`.
   - I file risiedono sempre e solo in `d:\Mod\Elin`: nessuna duplicazione e nessun file originale viene toccato!
2. Avvia Elin da Steam.
3. Nel menu principale:
   - Apri **Mod** e assicurati che **Traduzione Italiana** sia attiva.
   - Apri **Opzioni** -> seleziona la lingua **Italiano**.
4. Quando vuoi scollegare la mod dal gioco, esegui:
   ```cmd
   link_mod.bat --unlink
   ```

---

## 🚀 Pubblicazione su Steam Workshop

Elin dispone di un sistema nativo integrato per pubblicare mod:

1. Collega la mod al gioco tramite `link_mod.bat`.
2. Avvia Elin con Steam aperto.
3. Vai nel menu **Mod**.
4. Seleziona la mod **Traduzione Italiana** dall'elenco locale.
5. Clicca sul pulsante **Pubblica** (o **Publish**) in basso a destra.
6. Il gioco invierà automaticamente i file, la descrizione dal `package.xml` e l'immagine `preview.jpg` a Steam Workshop!
7. Dalla pagina del Workshop su Steam potrai poi modificare la visibilità (Pubblico, Solo amici, Non in elenco) o aggiungere screenshot aggiuntivi.
