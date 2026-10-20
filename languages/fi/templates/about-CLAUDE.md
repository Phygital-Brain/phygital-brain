<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove table rows for files that weren't created.
-->

Tässä kansiossa ovat perustiedot siitä, kuka {Name} on. Nämä muistiinpanot ovat luotettava lähde kaikelle muulle työlle.

## Tiedostot

| Tiedosto | Mitä siinä on | Luokkatagi |
|---|---|---|
| `me.md` | Kuka {Name} on, miten {Name} työskentelee ja miten agentin pitää toimia | `identity` |
| `biography.md` | Elämäntarina: mistä {Name} tulee ja miten tähän on päädytty | `identity` |
| `goals.md` | Tavoitteet ja tärkeysjärjestys | `goals` |
| `business.md` | Yritys | `business` |
| `services.md` | Palvelut, tuotteet, tarjonta | `business` |
| `customers.md` | Kuka ostaa ja mistä asiakkaat tulevat | `customers` |
| `pain-points.md` | Ratkaistavat ongelmat | `customers` (tai `goals`, jos {Name} ei myy mitään) |
| `brand.md` | Ääni, sävy, sanat joita käytetään ja joita vältetään | `brand` |
| `tools.md` | Työkalut ja missä mikäkin on | `tools` |
| `cv.md` | Työhistoria, koulutus, mediassa näkyminen, palkinnot | `career` |

## Tietolohko (frontmatter)

Jokainen tiedosto täällä (paitsi tämä) alkaa näin:

```yaml
---
type: about
status: active
updated: 2026-10-13
tags: [about, identity, working-style]
description: "Kuka {Name} on ja miten agentin pitää toimia."
---
```

- `type`: aina `about`.
- `status`: `active`, tai `outdated`, kun jokin tieto on varmasti vanhentunut.
- `updated`: päivä, jolloin tiedot viimeksi muuttuivat. Sitä ei muuteta kirjoitusvirheiden tai tyylin korjauksissa.
- `tags`: ensin `about`, sitten tiedoston luokkatagi yllä olevasta taulukosta, sitten aihetagit siitä, mitä tiedostossa käsitellään (englanniksi, pienillä kirjaimilla, väliviivoilla). Päivitä aihetagit, kun osio lisätään tai poistetaan.
- `description`: yksi lause lainausmerkeissä siitä, mitä tiedostossa on. Aina viimeisenä rivinä.

## Säännöt

- Nämä tiedostot ovat luotettava lähde. Älä kopioi niiden sisältöä muualle: linkitä niihin.
- Muoto "nykytila ylhäällä, havainnot alla" (pääsääntö 17): nykyinen tilanne ylimpänä, päivätyt havainnot sen alla.
- Koko syntymäaika on vain tiedostossa `me.md`. Älä koskaan kopioi sitä tai mainitse sitä vastauksessa. Syntymävuoden saa mainita.
- Luo uusi tiedosto vain, kun uusi aihe sitä tarvitsee. Kysy ensin (pääsääntö 9).
- Kuntotarkastuksessa merkitse ne tavoitteet tiedostossa `goals.md`, joilla ei ole yhtään aktiivista projektia.
