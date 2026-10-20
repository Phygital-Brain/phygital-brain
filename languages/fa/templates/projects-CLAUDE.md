هر پروژه یک پوشه است که با رسیدن اطلاعات بزرگ‌تر می‌شود. `README.md` تنها نقطه شروع است.

## هر چیز کجا می‌رود

| محتوا | کجا |
|---|---|
| خلاصه، وضعیت، مهلت، قدم‌های بعدی | `Projects/{name}/README.md` |
| یادداشت‌های کاری {Name} | `Projects/{name}/notes/{topic}.md` |
| تحقیق | `Projects/{name}/research/{topic}.md` |
| بریف، مشخصات، نیازها | `Projects/{name}/briefs/{name}.md` |
| پیش‌نویس، فیلم‌نامه، محتوای نوشتاری | `Projects/{name}/drafts/{name}.md` |
| ایده‌ها | `Projects/{name}/ideas/{name}.md` |
| بازخورد | `Projects/{name}/feedback/{name}.md` |
| عکس و رسانه | `Projects/{name}/assets/` |
| مطالب قدیمی همین پروژه | `Projects/{name}/archive/` |

اسم پوشه‌ها با خط فاصله بین کلمه‌ها است، بدون شماره در اولشان (`research/`، نه `01-Research/`). اگر هیچ‌کدام از این‌ها جور نبود، پروژه می‌تواند پوشه خودش را اضافه کند.

## ساختار README

1. بلوک اطلاعات (پایین‌تر)، با یک `description`.
2. `## چیست`: یک یا دو خط، با لینک به [[goals]].
3. `## وضعیت و قدم بعدی`: کجای کار است، قدم بعدی.
4. `## چطور اجرا می‌شود`: فقط اگر چیزی خودکار اینجا می‌نویسد (یک کار زمان‌بندی‌شده، یک اسکریپت).
5. `## چه چیزی کجاست`: فقط وقتی زیرپوشه‌ها ساخته شدند. یک جدول کوچک با لینک به هر کدام.

## بلوک اطلاعات (frontmatter)

```yaml
---
type: notes
date: 2026-10-13
status: active
project: Website-Redesign
tags: [website-redesign, notes]
---
```

- `type`: `project` (همان README، که `created`، `updated` و `description` هم دارد)، `notes`، `research`، `brief`، `draft`، `idea`، `feedback`، `plan`.
- `status`: `active`، `paused` یا `done`. وضعیت README همان وضعیت پروژه است.
- `project`: اسم پوشه پروژه.
- `tags`: اول پروژه، بعد نوع.

## قوانین

- پروژه تازه فقط یک `README.md` است. زیرپوشه فقط وقتی بسازید که محتوایی برسد که لازمش دارد، و از README به آن لینک بدهید.
- README فهرست است. محتوای زیرپوشه‌ها را در آن تکرار نکنید.
- داخل پروژه `CLAUDE.md` نگذارید. قوانین یک پروژه در بخش «قوانین هر پروژه» پایین می‌آیند.
- در بلوک اطلاعات هر یادداشت مربوط، `project:` را بگذارید.
- پروژه تمام‌شده فقط وقتی {Name} بگوید به `Memory/archive/{name}/` می‌رود.
- هر پروژه باید به هدفی در [[goals]] کمک کند. در چکاپ، هدف‌های بی‌پروژه و پروژه‌های بی‌هدف را علامت بزنید.

## قوانین هر پروژه

<!-- Rules for one project only. Add a line when a project needs its own rule: "**Project-Name:** the rule." -->
