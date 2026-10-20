<!-- ADAPTING (for the agent, leave this comment out of the file):
Remove the Morning Brief row if BRIEF = off.
-->

Catatan dan preferensi untuk skill yang dipakai agen, ditambah Penjaga Otak.

## Susunan

```
Skills/{skill-name}/
  {skill-name}.md atau SKILL.md   apa yang dilakukan skill ini
  catatan.md                      gaya dan preferensi {Name} untuk skill ini
  references/                     contoh dan bahan yang lebih panjang
```

## Terpasang

| Skill | Folder | Fungsinya |
|---|---|---|
| Penjaga Otak | `brain-keeper/` | Merapikan setiap hari dengan sendirinya, dan pemeriksaan kalau {Name} minta |
| Ringkasan Pagi | `morning-brief/` | Rencana singkat untuk hari ini, kalau diminta atau setiap hari kerja |
| Impor | `import/` | Memasukkan catatan dari aplikasi lain, dengan rencana yang disetujui {Name} dulu |
| Persiapan Rapat | `meeting-prep/` | Ringkasan singkat sebelum telepon, dari catatan di otak |
| Alat Berpikir | `thinking/` | Menguji ide, menemukan pola, mencari catatan yang saling bertentangan |
| Aplikasi Terhubung | `connected-apps/` | Aplikasi yang dibaca otak, dan aturannya |
| No AI Slop | `no-ai-slop/` | Cek Tulisan: menyunting tulisan supaya terdengar manusiawi, atau menandai pola khas AI (oleh Peter Yang, Lisensi MIT, tidak pernah diedit) |

## Aturan

- Satu folder per skill, dinamai dengan huruf kecil dan tanda hubung (kebab-case).
- Kalau ada skill baru, tambahkan satu baris ke tabel di atas.
- `SKILL.md` yang berasal dari orang lain tidak pernah diedit. Untuk menyesuaikan sebuah skill, tambahkan `notes.md` di foldernya.
- `brain-keeper/daily.md` dibaca oleh tugas terjadwal. Ubah file ini hanya untuk mengubah apa yang dikerjakan rutinitas harian, dan biarkan tetap polos: tanpa tautan, tanpa callout.
