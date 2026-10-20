<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Nota dan pilihan untuk kemahiran yang digunakan oleh ejen, serta Penjaga Otak.

## Struktur

```
Skills/{skill-name}/
  {skill-name}.md atau SKILL.md   apa yang kemahiran itu buat
  notes.md                        suara dan pilihan {Name} untuk kemahiran ini
  references/                     contoh dan bahan yang lebih panjang
```

## Dipasang

| Kemahiran | Folder | Apa yang ia buat |
|---|---|---|
| Penjaga Otak | `brain-keeper/` | Kemas harian dengan sendirinya, dan semakan apabila {Name} minta |
| Taklimat Pagi | `morning-brief/` | Rancangan pendek untuk hari ini, bila diminta atau setiap hari bekerja |
| Import | `import/` | Membawa masuk nota dari aplikasi lain, dengan rancangan yang {Name} luluskan dulu |
| Persediaan Mesyuarat | `meeting-prep/` | Ringkasan pendek sebelum panggilan, daripada nota dalam otak ini |
| Alat Berfikir | `thinking/` | Mencabar idea, mencari corak, mencari nota yang bercanggah |
| Aplikasi Bersambung | `connected-apps/` | Aplikasi mana yang dibaca oleh otak ini, dan peraturannya |
| No AI Slop | `no-ai-slop/` | Semakan Tulisan: menyunting tulisan supaya berbunyi seperti manusia, atau menandakan corak AI (oleh Peter Yang, Lesen MIT, tidak pernah disunting) |

## Peraturan

- Satu folder untuk setiap kemahiran, dinamakan dalam kebab-case.
- Apabila kemahiran baharu ditambah, tambah satu baris dalam jadual di atas.
- `SKILL.md` yang datang daripada orang lain tidak pernah disunting. Untuk menyesuaikan sesuatu kemahiran, tambah `notes.md` dalam foldernya.
- `brain-keeper/daily.md` dibaca oleh tugasan berjadual. Ubah hanya untuk mengubah apa yang dibuat oleh larian harian, dan pastikan ia ringkas: tiada pautan, tiada kotak nota.
