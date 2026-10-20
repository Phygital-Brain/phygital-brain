<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Note și preferințe pentru abilitățile pe care le folosește agentul, plus Îngrijitorul creierului.

## Structură

```
Skills/{skill-name}/
  {skill-name}.md sau SKILL.md   ce face abilitatea
  notes.md                       stilul și preferințele pe care le are {Name} pentru abilitatea asta
  references/                    exemple și materiale mai lungi
```

## Instalate

| Abilitate | Folder | Ce face |
|---|---|---|
| Îngrijitorul creierului | `brain-keeper/` | Face ordine singur în fiecare zi și un check-up când îl cere {Name} |
| Rezumatul de dimineață | `morning-brief/` | Un plan scurt al zilei, la cerere sau în fiecare zi lucrătoare |
| Import | `import/` | Aduce note din alte aplicații, cu un plan pe care {Name} îl aprobă mai întâi |
| Pregătirea pentru întâlniri | `meeting-prep/` | Un rezumat scurt înainte de un apel, din notele creierului |
| Instrumente de gândire | `thinking/` | Pune o idee la încercare, găsește tipare, găsește note care se contrazic |
| Aplicații conectate | `connected-apps/` | Din ce aplicații citește creierul și regulile pentru ele |
| No AI Slop | `no-ai-slop/` | Verificarea textelor: corectează textele ca să sune omenește sau semnalează tiparele de inteligență artificială (de Peter Yang, licență MIT, nemodificată niciodată) |

## Reguli

- Un folder pentru fiecare abilitate, cu numele în kebab-case (litere mici, cu cratime).
- Când se adaugă o abilitate nouă, adaugă un rând în tabelul de mai sus.
- Un `SKILL.md` venit de la altcineva nu se modifică niciodată. Ca să adaptezi o abilitate, adaugă `notes.md` în folderul ei.
- `brain-keeper/daily.md` e citit de o activitate programată. Schimbă-l doar ca să schimbi ce face runda zilnică, și ține-l simplu: fără linkuri, fără casete.
