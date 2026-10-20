<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Noti na mapendeleo ya ujuzi (skills) anaotumia wakala, pamoja na Mtunzaji wa Ubongo.

## Muundo

```
Skills/{skill-name}/
  {skill-name}.md au SKILL.md   ujuzi huu unafanya nini
  noti.md                       sauti na mapendeleo ya {Name} kwa ujuzi huu
  references/                   mifano na maelezo marefu zaidi
```

## Vilivyowekwa

| Ujuzi | Folda | Unafanya nini |
|---|---|---|
| Mtunzaji wa Ubongo | `brain-keeper/` | Hupanga kila siku peke yake, na hufanya ukaguzi {Name} anapoomba |
| Muhtasari wa Asubuhi | `morning-brief/` | Mpango mfupi wa siku, ukiombwa au kila siku ya kazi |
| Kuingiza | `import/` | Huleta noti kutoka programu nyingine, kwa mpango ambao {Name} anaukubali kwanza |
| Maandalizi ya Mkutano | `meeting-prep/` | Maelezo mafupi kabla ya simu, kutoka kwenye noti za ubongo |
| Zana za Kufikiri | `thinking/` | Kupinga wazo, kutafuta mwenendo, kutafuta noti zisizokubaliana |
| Programu Zilizounganishwa | `connected-apps/` | Ubongo unasoma programu zipi, na kanuni zake |
| No AI Slop | `no-ai-slop/` | Ukaguzi wa Maandishi: hurekebisha maandishi yasikike kama ya binadamu, au huonyesha mitindo ya AI (na Peter Yang, leseni ya MIT, haibadilishwi kamwe) |

## Kanuni

- Folda moja kwa kila ujuzi, yenye jina kwa mtindo wa kebab-case.
- Ujuzi mpya ukiongezwa, ongeza mstari kwenye jedwali hapo juu.
- `SKILL.md` iliyotoka kwa mtu mwingine haibadilishwi kamwe. Ili kubadilisha ujuzi upendavyo, ongeza `notes.md` ndani ya folda yake.
- `brain-keeper/daily.md` inasomwa na kazi iliyopangwa kwa ratiba. Ibadilishe tu kama unataka kubadilisha kile kinachofanyika kila siku, na iwe rahisi: bila viungo, bila callouts.
