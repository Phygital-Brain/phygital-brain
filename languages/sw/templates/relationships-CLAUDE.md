<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the "Where a new lead goes" section if there's no `Clients/` folder. Remove subfolder rows that weren't created.
Each subfolder gets its own `CLAUDE.md` from `relationships-subfolder-CLAUDE.md`.
-->

Kila mtu ambaye {Name} anafanya naye kazi: noti moja kwa kila mtu au shirika.

## Folda ndogo

| Folda | Nani anakaa humo |
|---|---|
| `Clients/` | Watu na kampuni ambao {Name} anawafanyia kazi |
| `Collaborators/` | Washirika wa ubunifu, mnasaidiana, hakuna pesa inayohusika |
| `Team/` | Watu wanaofanya kazi pamoja na {Name} au kwa ajili ya {Name} (wafanyakazi huru, wasaidizi) |
| `Partners/` | Mashirika ambayo {Name} anajenga jina pamoja nayo (vyombo vya habari, kumbi, majukwaa) |

## Mteja mtarajiwa mpya anakwenda wapi

- Mawasiliano ya kwanza bila maelekezo halisi bado: mstari chini ya `## Wapya` ndani ya `Clients/_Leads.md` (inatengenezwa mara ya kwanza inapohitajika).
- Jibu linalosema "labda baadaye": mstari chini ya `## Endelea kuwasiliana` ndani ya `Clients/_Leads.md`.
- Maelekezo halisi, simu au makadirio ya bei yanayoendelea: noti ya mteja `Clients/{client-name}.md` yenye `status: prospect`.

Mteja mtarajiwa akipanda hatua moja, mhamishie mahali panapofuata na umwondoe pale alipokuwa.

## Sehemu ya taarifa (frontmatter)

Kila noti hapa (isipokuwa faili za `CLAUDE.md` na `_Leads.md`) inaanza hivi:

```yaml
---
type: client
status: active
last-contact: 2026-10
tags: [relationship, client, fashion, brazil]
description: "Sentensi moja rahisi kuhusu wao ni akina nani na uhusiano wao na {Name}."
---
```

- `type`: `client`, `collaborator`, `team` au `partner`.
- `status`: `active` (kazi au mawasiliano ndani ya miezi 12 iliyopita), `prospect` (mnaongea, hamjawahi kufanya kazi pamoja), `dormant` (hakuna mawasiliano kwa miezi 12 au zaidi), `closed` (imeisha kabisa).
- `last-contact`: mwezi wa karibuni zaidi wenye mawasiliano au kazi halisi, `YYYY-MM`. Iache tupu kama haijulikani.
- `tags`: `relationship`, kisha aina, kisha lebo 2 hadi 5 za mada (sekta, nchi, aina ya kazi), kwa Kiingereza, herufi ndogo, vistari.
- `description`: sentensi moja, ndani ya alama za nukuu mbili. Kila mara mstari wa mwisho.
- Si lazima: `aliases` (majina mengine wanayoitwa), `project` (mradi wa sasa).

## Kanuni

- **Hakuna nakala mbili.** Kabla ya kutengeneza noti, tafuta jina na namna zake nyingine za kuandikwa (herufi zenye alama, majina mafupi, jina la chapa dhidi ya jina la kampuni). Noti ikiwepo, itumie na uongeze tahajia mpya kwenye `aliases`. Usitengeneze kamwe noti ya pili kwa mtu au kampuni ileile.
- **Muundo wa "ukweli wa sasa juu, ushahidi chini"** (kanuni kuu ya 17): wao ni akina nani na hali ya sasa juu, historia yenye tarehe chini.
- **Isasishe kila mara.** {Name} anapowasiliana kweli na mtu (barua pepe, simu, kazi iliyokabidhiwa), sasisha `last-contact` kuwa mwezi huu, na `status` kama imebadilika.
- **Watu wa mawasiliano** ndani ya kampuni (wakala, meneja, mhariri) ni maandishi ya kawaida ndani ya noti ya kampuni, kamwe si `[[viungo]]`, na hawapati noti yao wenyewe. Ukitaka kuwataja mahali pengine, weka kiungo kwa kampuni: `[[Jina la Kampuni|Jina la Mtu]]`.
- **Taarifa binafsi** (namba za simu, barua pepe, anwani za nyumbani) zinakaa ndani ya noti ya mtu huyo au ya kampuni hiyo tu. Usizinakili kamwe kwenye noti za siku au noti nyingine.
- Unganisha watu kutoka kwenye miradi na noti za siku kwa `[[wikilinks]]`.
- Tengeneza folda ndogo mpya pale tu aina mpya ya uhusiano inapojitokeza. Uliza kwanza.
