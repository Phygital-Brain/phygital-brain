<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Mga note at kagustuhan para sa mga skill na ginagamit ng agent, kasama ang Taga-ayos ng Utak.

## Ayos

```
Skills/{skill-name}/
  {skill-name}.md o SKILL.md    ano ang ginagawa ng skill
  notes.md                      ang boses at kagustuhan ni {Name} para sa skill na ito
  references/                   mga halimbawa at mas mahahabang materyal
```

## Naka-install

| Skill | Folder | Ano ang ginagawa |
|---|---|---|
| Taga-ayos ng Utak | `brain-keeper/` | Kusang nag-aayos araw-araw, at nagche-check-up kapag hiniling ni {Name} |
| Buod sa Umaga | `morning-brief/` | Maikling plano ng araw, kapag hiniling o tuwing araw ng trabaho |
| Import | `import/` | Nagpapasok ng mga note mula sa ibang apps, na may planong inaaprubahan muna ni {Name} |
| Paghahanda sa Meeting | `meeting-prep/` | Maikling buod bago ang isang call, mula sa mga note ng utak |
| Mga Tool sa Pag-iisip | `thinking/` | Kontrahin ang isang idea, maghanap ng pattern, maghanap ng mga note na nagkakasalungat |
| Konektadong Apps | `connected-apps/` | Kung aling apps ang binabasa ng utak, at ang mga patakaran para sa mga ito |
| No AI Slop | `no-ai-slop/` | Ang Suri sa Pagsulat: inaayos ang sulat para tunog-tao, o itinuturo ang mga pattern ng AI (gawa ni Peter Yang, MIT License, hindi kailanman ine-edit) |

## Mga patakaran

- Isang folder bawat skill, ang pangalan ay kebab-case.
- Kapag may bagong skill na idinagdag, magdagdag ng row sa table sa itaas.
- Hindi kailanman ine-edit ang `SKILL.md` na galing sa ibang tao. Para iangkop ang isang skill, magdagdag ng `notes.md` sa folder nito.
- Binabasa ng isang naka-schedule na task ang `brain-keeper/daily.md`. Baguhin lang ito para baguhin ang ginagawa ng araw-araw na takbo, at panatilihin itong simple: walang link, walang callout.
