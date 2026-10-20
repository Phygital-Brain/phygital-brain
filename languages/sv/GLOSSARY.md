# Ordlista svenska (sv)

## Tilltal

Informellt "du", som i nästan alla svenska konsumentappar. Samma i hela setet: i formulären, i meddelandena och i regelfilerna (även instruktionerna till agenten skrivs med "du"). {Name} får inget pronomen: där engelskan säger "they" står {Name} igen, eller så är meningen omskriven, så att ingen får fel kön. Vi använder inte "hen" heller, eftersom namnet läser lättare. Roller som "Owner" är skrivna så att inget kön behövs (i teamtabellen "Ansvarig", i texten "Fråga {Name} först").

## Namn på funktioner

| Engelska | Svenska | Varför |
|---|---|---|
| Phygital Brain | Phygital Brain | Stannar på engelska |
| Brain Keeper | Städhjälpen | Säger direkt vad den gör. "Brain Keeper" vore bara ett främmande ord för vanliga människor |
| morning brief | morgonöversikt | "Översikt" är vanligt i svenska appar, "brief" är det inte |
| meeting prep | mötesförberedelse | |
| thinking tools | tankeverktyg | |
| check-up | hälsokoll | Låter som en koll hos läkaren, alla förstår det |
| Writing Check | Textkoll | |
| second brain | andra hjärna | |
| your agent | din agent | |

## Mappar (översta nivån)

| Engelska | Svenska |
|---|---|
| About | Profil |
| Daily | Dagbok |
| Projects | Projekt |
| Relationships | Kontakter |
| Memory | Minne |
| Library | Bibliotek |
| Skills | Skills |

- **Profil** i stället för "Om mig": ett ord, och mappen innehåller mer än bara personen (mål, företag, varumärke).
- **Dagbok**: en anteckning per dag, precis som en dagbok.
- **Kontakter** i stället för "Relationer": "relationer" låter som kärleksliv.
- **Skills** stannar, eftersom agentappar använder ordet så även på svenska. "Färdigheter" låter fel här.

## Undermappar och anteckningar

| Engelska | Svenska | Engelska | Svenska |
|---|---|---|---|
| Clients | Kunder | me | jag |
| Collaborators | Samarbeten | goals | mål |
| Team | Team | business | företag |
| Partners | Partner | services | erbjudande |
| decisions | beslut | customers | målgrupp |
| research | research | pain-points | problem |
| finances | ekonomi | brand | varumärke |
| archive | arkiv | tools | verktyg |
| applications | ansökningar | cv | cv |
| competitors | konkurrenter | biography | biografi |
| notes | anteckningar | tasks | uppgifter |
| briefs | underlag | _Leads | _Förfrågningar |
| drafts | utkast | daily | daglig |
| ideas | idéer | check-up | hälsokoll |
| feedback | feedback | queue | öppna-punkter |
| assets | media | PAUSED | PAUSAD |
| prompts | prompter | brain-keeper | städhjälpen |
| templates | mallar | morning-brief | morgonöversikt |
| frameworks | metoder | meeting-prep | mötesförberedelse |
| import | import | thinking | tankeverktyg |
| connected-apps | anslutna-appar | reports | rapporter |

- **customers = målgrupp**, inte "kunder": annars skulle det finnas `kunder.md` i Profil och mappen `Kunder` i Kontakter, och de är lätta att blanda ihop.
- **queue = öppna-punkter**: "kö" låter tekniskt. I texterna heter filen "listan över öppna punkter".
- **_Leads = _Förfrågningar**: "leads" är det inte alla som känner till.
- **research** stannar: ordet används så i svenskt arbetsliv.

## Fasta ord

| Engelska | Svenska |
|---|---|
| note | anteckning |
| daily note | dagsanteckning |
| info block (frontmatter) | infoblock (frontmatter) |
| root `CLAUDE.md` | huvud-`CLAUDE.md` |
| root rule 9 | huvudregel 9 |
| folder root | huvudmappen |
| Knowledge Routing | Var allt hamnar |
| routing table | tabellen "Var allt hamnar" |
| Backups and Undo | Säkerhetskopior och ångra |
| backup | säkerhetskopia |
| compiled-truth format | formatet "läget överst, belägg under" |
| Evidence (rubrik) | Belägg |
| What it is / Status and next step | Vad det är / Läge och nästa steg |
| {Name}'s Rules | Regler för {Name} |
| Session Startup | När en session börjar |
| session log | sessionslogg |
| trigger | utlösare |
| run (Brain Keeper) | körning |
| dry run | testkörning (den engelska utlösaren "dry run" fungerar också) |
| safe fixes / report only | stannar på engelska (värden som installationen fyller i) |
| Needs {Name} / To fix / Next folder / Last run | Behöver {Name} / Att rätta / Nästa mapp / Senaste körning |
| orphan note | föräldralös anteckning |
| broken link | trasig länk |
| lead | förfrågan |
| contact person | kontaktperson |
| em dash | tankstreck |
| Queued (rubrik i rapporten) | Lagt på listan |
| Drifting goals (hälsokoll) | Mål utan projekt |
| (from email) / (from calendar) | (från mejl) / (från kalendern) |
| connector | connector |
| cloud drive | molnlagring |

## Exempel

Namnen (Ana, Marta, João, Lia) är desamma som på engelska. Orten i formuläret är "Stockholm, Sverige" i stället för "Lisbon, Portugal", och exempelsajten är "https://dinsida.se".

## Platshållare inom klammerparentes

Riktiga platshållare (`{Name}`, `{Language}`, `{person or company}`, `{weekday in English}` och så vidare) stannar exakt som de är. Klamrar som innehåller en instruktion eller en exempeltext som agenten skriver in i anteckningen (till exempel `{En mening: vad den här filen innehåller.}`) är översatta, så att texten i anteckningen blir svensk.
