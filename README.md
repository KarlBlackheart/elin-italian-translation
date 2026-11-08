# 🇮🇹 Mod Traduzione Italiana per Elin (Early Access)

[![Compatibilità](https://img.shields.io/badge/Elin-EA%200.23.338%2B-blue.svg)](https://store.steampowered.com/app/2135890/Elin/)
[![Lingua](https://img.shields.io/badge/Lingua-Italiano-green.svg)](#)
[![Stato Traduzione](https://img.shields.io/badge/Testo%20Umano-100%25%20Tradotto-brightgreen.svg)](#)
[![Licenza](https://img.shields.io/badge/Licenza-Community%20Open%20Source-orange.svg)](#)

Benvenuto nel progetto di **Traduzione Italiana di Elin**, l'acclamato RPG roguelike sandbox creato da **Noa / Lafrontier** (autore del celebre *Elona*).

Questo repository contiene la localizzazione completa in lingua italiana, conforme alle specifiche ufficiali del motore di gioco e pronta sia per l'installazione manuale che per la pubblicazione su **Steam Workshop**.

---

> [!IMPORTANT]
> ### ⚠️ Nota di Trasparenza sull'Uso dell'Intelligenza Artificiale (AI)
> Questa localizzazione è stata realizzata e calibrata con l'ausilio di **Intelligenza Artificiale (AI)**.
> **Non si intende rivendicare alcun merito indebito:** il progetto nasce unicamente dalla passione per *Elin* e dal desiderio di renderlo accessibile e godibile in italiano per tutta la community dei videogiocatori.
> 
> Benché tutti i testi siano stati adattati attingendo direttamente alle fonti originali (giapponese e inglese), contestualizzati rispetto alle meccaniche di gioco e convalidati a livello di codice motore, trattandosi di un lavoro generato con il supporto dell'IA **possono essere presenti imprecisioni, refusi, calchi o sfumature da affinare**.
> 
> **Il contributo e il feedback di tutti sono fondamentali:** qualsiasi segnalazione, correzione o suggerimento è sempre il benvenuto!

---

## 📖 Contenuti della Traduzione

La mod traduce il **100% dei testi leggibili dall'essere umano**, preservando con assoluta precisione ogni variabile e tag tecnico di sistema (`#1`, `#2`, `<color=...>`, `{topic,...}`, ecc.):

* 📜 **Libri di Folclore, Guide e Pergamene (94 file)**:
  - Tutti i 25 numeri del *Settimanale dell'Avventuriero*.
  - Tutte le leggende e i miti religiosi (Yufu, Horome, Opatos, Ehekatl, Kumiromi, Mani, Lulwy, Jure, ecc.).
  - Tutte le guide pratiche di gioco (cucina, pesca, agricoltura, magia, fedi, gestione della casa).
  - Tutte le pergamene personali (la saga di lettere di Lutz, lettere d'amore, lettere trial, ecc.).
  - Tutte le gazzette periodiche del mondo di gioco.
* 🎭 **Dialoghi di Trama e Filmati (Drama - 36 file)**:
  - Tutti gli eventi di trama narrativi (Fiama, Loytel, Kettle, Demitas, Ashland, Nerun, ecc.).
  - Interazioni con le divinità presso gli altari, mercanti, gilde e compagni.
* ⚔️ **Equipaggiamento, Oggetti e Costruzione (oltre 4.000 voci)**:
  - Tutte le armi, armature, materiali, cibi, collezionabili, arredi, semi, ricette e blocchi.
* 🧙 **Statistiche, Talenti e Magia (oltre 3.200 voci)**:
  - Tutti i talenti, incantesimi, abilità, posture, resistenze elementali, alterazioni di stato e mutazioni.
* 🖥️ **Interfaccia Grafica e Sistema (UI & Engine)**:
  - Tutti i menu, notifiche di combattimento, bacheche delle missioni, inventario, impostazioni e gestione del salvataggio/Steam Cloud.
  - **Correzioni di sintassi del motore C#**:
    - Risolto l'ordine procedurale nome/materiale (`#2 di #1`, es. *Spada di argento*, *Scudo di vetro* anziché all'inglese *argento Spada*).
    - Risolto il formato di professioni e ruoli PNG nei log e bacheche (`#2 (#1)`, es. *Tomyzof (barista)*).
    - Risolta la concordanza al risveglio e nei messaggi di stato (`#1 ti/si svegli./sveglia.` -> *Tu ti svegli*).
    - Configurate le varianti contestuali per il giocatore (`parasite_pc` per le missioni di scorta).

---

## 🎮 Come Installare la Mod

### Metodo 1: Collegamento Rapido (Consigliato per Windows)
Se hai scaricato o clonato questa cartella sul tuo PC:
1. Chiudi *Elin* se è aperto.
2. Fai doppio clic sul file **[`link_mod.bat`](link_mod.bat)** presente nella cartella della mod.
   - Lo script troverà automaticamente la tua installazione di Steam e collegherà la cartella in `Elin/Package/Mod_Italian` tramite una *Junction NTFS* trasparente (senza duplicare spazio su disco).
   - Se hai installato Elin in un percorso personalizzato, lo script ti chiederà semplicemente di indicarlo.
3. Avvia **Elin** da Steam.
4. Nel menu iniziale:
   - Clicca su **Mod** e verifica che **Traduzione Italiana** sia spuntata/attiva.
   - Clicca su **Impostazioni** (o *Config*) -> seleziona la lingua **Italiano**.
5. Quando desideri rimuovere il collegamento, basta eseguire:
   ```cmd
   link_mod.bat --unlink
   ```

### Metodo 2: Installazione Manuale
1. Copia l'intera cartella di questo progetto (o rinominala in `Mod_Italian`).
2. Incollala all'interno della cartella dei pacchetti di Elin:
   ```
   <Percorso-Libreria-Steam>\steamapps\common\Elin\Package\Mod_Italian
   ```
3. Avvia il gioco e seleziona **Italiano** nelle Impostazioni.

### Metodo 3: Steam Workshop (Quando Disponibile)
1. Iscriviti alla mod dalla pagina ufficiale di Steam Workshop.
2. Avvia il gioco e seleziona la lingua **Italiano** dal menu delle impostazioni.

---

## 🚀 Come Pubblicare la Mod su Steam Workshop

Se sei l'autore o un maintainer del pacchetto e desideri aggiornare o pubblicare la mod sul Workshop:
1. Collega la mod alla cartella di gioco con `link_mod.bat`.
2. Avvia *Elin* con Steam regolarmente aperto.
3. Nel menu iniziale, entra in **Mod**.
4. Clicca su **Traduzione Italiana** nell'elenco locale.
5. Clicca sul pulsante **Pubblica** (o **Publish**) in basso a destra.
6. Il gioco invierà automaticamente i file, la descrizione definita in `package.xml` e la grafica `preview.jpg` a Steam Workshop.

---

## 🛠️ Manutenzione e Aggiornamenti alle Nuove Patch

*Elin* riceve costanti aggiornamenti in Early Access. La cartella `tools/` contiene suite di script Python per mantenere la mod sincronizzata:

* **Convalida dell'integrità e dei tag di gioco**:
  ```cmd
  python tools/validate.py
  ```
  Analizza tutti gli 82 fogli Excel per garantire che non vi siano tag corrotti, errori XML o segnaposto mancanti.
* **Sincronizzazione con nuove patch di Elin**:
  ```cmd
  python tools/sync_update.py
  ```
  Rileva le nuove stringhe introdotte dagli sviluppatori, le integra con fallback sicuro e **preserva integralmente ogni riga italiana già tradotta**.
* **Verifica dell'avanzamento**:
  ```cmd
  python tools/status.py
  ```

---

## 🤝 Come Contribuire e Segnalare Errori

Hai notato una frase poco chiara, un refuso o una battuta che suona strana in gioco? **Il tuo aiuto è preziosissimo!**

1. **Apri una Segnalazione (Issue)**:
   - Vai nella scheda [Issues](../../issues) di questo repository su GitHub.
   - Clicca su **New Issue** e descrivi l'errore (allega uno screenshot se possibile, oppure indica dove hai letto la frase).
2. **Invia una Modifica (Pull Request)**:
   - Fai un *Fork* del repository.
   - I file di testo e dialogo si trovano nei comodi fogli Excel in `Lang/IT/Game/` e `Lang/IT/Dialog/`.
   - Modifica la colonna italiana mantenendo i tag di riferimento (`#1`, `#2`, ecc.).
   - Esegui `python tools/validate.py` per accertarti che il file sia valido.
   - Invia la tua *Pull Request*!

---

## ⚖️ Note Legali e Riconoscimenti

* **Elin** è un videogioco sviluppato e detenuto da **Noa / Lafrontier**. Tutti i diritti sui contenuti originali del gioco, sui testi e sugli asset appartengono ai rispettivi proprietari.
* Questa mod di localizzazione è un progetto gratuito, indipendente e non ufficiale realizzato per scopi amatoriali e di accessibilità dalla community italiana.
