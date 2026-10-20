<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Note e preferenze per le skill che usa l'agente, più il Custode del Cervello.

## Struttura

```
Skill/{skill-name}/
  {skill-name}.md o SKILL.md    cosa fa la skill
  notes.md                      lo stile e le preferenze di {Name} per questa skill
  references/                   esempi e materiale più lungo
```

## Installate

| Skill | Cartella | Cosa fa |
|---|---|---|
| Custode del Cervello | `custode-del-cervello/` | Mette in ordine ogni giorno da solo, e fa un check-up quando {Name} lo chiede |
| Punto del mattino | `punto-del-mattino/` | Un breve piano della giornata, su richiesta o ogni giorno lavorativo |
| Importare | `importare/` | Porta dentro note da altre app, con un piano che {Name} approva prima |
| Preparazione alle riunioni | `preparazione-riunioni/` | Un breve riassunto prima di una chiamata, dalle note del cervello |
| Strumenti per pensare | `pensare/` | Mettere alla prova un'idea, trovare schemi ricorrenti, trovare note che non tornano |
| App collegate | `app-collegate/` | Da quali app legge il cervello, e le regole per usarle |
| No AI Slop | `no-ai-slop/` | Il Controllo di scrittura: sistema i testi perché suonino umani, o segnala gli schemi tipici dell'IA (di Peter Yang, licenza MIT, mai modificata) |

## Regole

- Una cartella per skill, con il nome in kebab-case (minuscolo con i trattini).
- Quando aggiungi una nuova skill, aggiungi una riga alla tabella qui sopra.
- Un `SKILL.md` che viene da qualcun altro non si modifica mai. Per adattare una skill, aggiungi `appunti.md` nella sua cartella.
- `custode-del-cervello/giro-quotidiano.md` viene letto da un'attività programmata. Cambialo solo per cambiare quello che fa il giro quotidiano, e tienilo semplice: niente link, niente callout.
