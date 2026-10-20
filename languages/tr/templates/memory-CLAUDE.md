Zamanla biriken bilgi: kararlar, araştırmalar, başvurular ve arşiv.

## Ne nereye gider

| İçerik | Gideceği yer |
|---|---|
| Gerekçesiyle bir karar ya da dışarıdaki bir şeyle ilgili inceleme (uygulama, web sitesi, kurs, rakip) | `decisions/YYYY-MM-DD-{title}.md` |
| Araştırma (pazar, trendler, seçenekler) | `research/{topic}.md` |
| Başvurular: iş, hibe, ödül, açık çağrılar (ilk kullanımda oluşturulur) | `applications/{name}/` |
| Rakip profilleri (ilk kullanımda oluşturulur) | `competitors/{name}.md` |
| Para: faturalar, vergiler, ödemeler. Özel | `finances/` |
| Arşivlenmiş kararlar | `archive/decisions/` |
| Bitmiş ya da eskimiş araştırmalar | `archive/research/` |
| Bitmiş projeler | `archive/{name}/` |
| Toplantı notları | Bir karar çıktıysa `decisions/`, yoksa o günün `Daily/` notu. Toplantı için ayrı bir klasörü sadece çok sayıda toplantı notu olduğunda öner. |

## Bilgi bloğu (frontmatter)

```yaml
---
type: research
date: 2026-10-13
status: active
tags: [research, pricing]
---
```

- `type`: `decision`, `research`, `application`, `competitor`.
- `date`: notun yazıldığı tarih.
- `status`: kararlar ve başvurular için aşağıya bak. Diğer her şey: `active` ya da `closed`.
- `tags`: önce tür, sonra konu.
- İsteğe bağlı: `project`, `deadline`, `description` (çift tırnak içinde tek cümle, son satır).

## Karar notları

Her zaman nedenini yaz: kimler vardı, karara ne yol açtı, neyden vazgeçilip ne seçildi. Kararın kendisi için `> [!important]`, bilinen riskler için `> [!warning]` kullan.

Kararlarda `date:` satırının hemen arkasından `updated:` de gelir. `date` oluşturulduğu gün, `updated` en son gözden geçirildiği ya da değiştiği gündür.

```yaml
---
type: decision
date: 2026-09-02
updated: 2026-10-13
status: open
tags: [decision, website]
---
```

- `status`: `open` (hâlâ karar veriliyor ya da üzerinde çalışılıyor), `waiting` (başka birini bekliyor), `paused`, `closed`.
- `updated` tarihi 30 günden eski olan bir kararın gözden geçirilmesi gerekir. Düzen Bekçisi, {Name} kararı koruyana, kapatana ya da arşivleyene kadar onu işaretler (her biri `updated` alanını o güne çeker).
- Bir karar `archive/decisions/` içine ancak {Name} söylerse taşınır.

## Başvurular

Her başvuru için bir klasör: `applications/{name}/`. İçinde son tarihi, bağlantıyı, durumu ve neyin gönderildiğini tutan bir `README.md` olur. Diğer dosyalar (cevaplar, niyet mektubu) onun yanında durur.

- `status`: `draft`, `submitted`, `accepted`, `rejected` ya da `withdrawn`.
- Cevapları markdown olarak tut. Büyük PDF'ler ve sunumlar bu klasörün dışında kalır: bir notta özetle.

## Kurallar

- Araştırma varsayılan olarak tarafsızdır (ana kural 23).
- Yerini yenisine bırakan araştırmayı silmek yerine `archive/research/` içine taşı.
- `finances/` özeldir ve `.claudeignore` içinde listelenir. Sadece {Name} belirli bir dosyayı isterse aç (ana kural 8).
