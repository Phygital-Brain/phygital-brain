<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Muistiinpanot ja mieltymykset taidoille, joita agentti käyttää, sekä siivousapuri.

## Rakenne

```
Skills/{skill-name}/
  {skill-name}.md tai SKILL.md   mitä taito tekee
  notes.md                       {Name}: oma tyyli ja mieltymykset tälle taidolle
  references/                    esimerkit ja pidempi aineisto
```

## Asennetut

| Taito | Kansio | Mitä se tekee |
|---|---|---|
| Siivousapuri | `brain-keeper/` | Siistii joka päivä itsestään ja tekee kuntotarkastuksen, kun {Name} pyytää |
| Aamukatsaus | `morning-brief/` | Lyhyt suunnitelma päivälle, pyydettäessä tai joka työpäivä |
| Tuonti | `import/` | Tuo muistiinpanot muista sovelluksista suunnitelmalla, jonka {Name} hyväksyy ensin |
| Tapaamisen valmistelu | `meeting-prep/` | Lyhyt katsaus ennen puhelua aivojen muistiinpanojen pohjalta |
| Ajattelutyökalut | `thinking/` | Haasta idea, löydä toistuvia kuvioita, löydä muistiinpanot, jotka ovat ristiriidassa |
| Yhdistetyt sovellukset | `connected-apps/` | Mistä sovelluksista aivot lukevat ja mitkä säännöt niitä koskevat |
| No AI Slop | `no-ai-slop/` | Tekstitarkistus: muokkaa tekstin ihmisen kuuloiseksi tai merkitsee tekoälyn kaavat (tekijä Peter Yang, MIT-lisenssi, ei koskaan muokata) |

## Säännöt

- Yksi kansio jokaiselle taidolle, nimettynä kebab-case-muodossa (pienet kirjaimet ja väliviivat).
- Kun uusi taito lisätään, lisää rivi yllä olevaan taulukkoon.
- `SKILL.md`-tiedostoa, joka on tullut joltain muulta, ei koskaan muokata. Taidon voi sovittaa omaan käyttöön lisäämällä sen kansioon `notes.md`.
- Ajastettu tehtävä lukee tiedostoa `brain-keeper/daily.md`. Muuta sitä vain, kun halutaan muuttaa päivittäisen ajon toimintaa, ja pidä se pelkistettynä: ei linkkejä, ei huomiolaatikoita.
