## Custode del Cervello

Il Custode del Cervello si prende cura di questo cervello in due modi. I suoi file sono in `Skills/brain-keeper/`.

- **Ogni giorno, da solo:** un giro programmato di `Skills/brain-keeper/daily.md`. Piccole correzioni sicure, un resoconto e un elenco delle cose che solo {Name} può decidere, in `Skills/brain-keeper/queue.md`.
- **Check-up, quando {Name} lo chiede:** "fai un check-up al mio cervello", "check up my brain", "metti in ordine il mio cervello", "tidy my brain", o la stessa cosa in {Language}: leggi `Skills/brain-keeper/check-up.md` e seguilo.
- "avvia il custode del cervello", "run the brain keeper", o la stessa cosa in {Language}: leggi `Skills/brain-keeper/daily.md` e fai un giro adesso.
- "avvia il custode del cervello nel cloud", "run the brain keeper in the cloud", o la stessa cosa in {Language}: segui il Passo 3, "In the cloud", della skill `brain-keeper` di Phygital Brain.
- "metti in pausa il custode del cervello", "pause the brain keeper", o la stessa cosa in {Language}: crea `Skills/brain-keeper/PAUSED.md` con una riga: la data di oggi e "Pausa chiesta da {Name}". Confermalo in una riga.
- "riattiva il custode del cervello", "resume the brain keeper", o la stessa cosa in {Language}: elimina `Skills/brain-keeper/PAUSED.md` (per questo file non serve controllare i link). Confermalo in una riga.
- "cosa ha fatto il custode del cervello", "what did the brain keeper do", o la stessa cosa in {Language}: leggi gli ultimi resoconti in `Skills/brain-keeper/reports/` e spiegali con parole semplici. Segnala qualsiasi cosa inattesa.
- Per cambiare quello che fa il giro quotidiano, {Name} lo chiede in chat. Solo allora si modifica `daily.md`.
- Il check-up non considera `Skills/brain-keeper/reports/` e `queue.md` quando cerca le note orfane.
