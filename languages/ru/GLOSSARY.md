# Glossary: Russian (ru)

## Register

- **Talking to the person** (setup messages, forms, comments in `.claudeignore`, replies the agent gives): **«вы»**, lowercase, as in most big Russian consumer apps (Яндекс, Т-Банк, Госуслуги, Ozon). Never «Вы» with a capital.
- **Rule files and skill files** (`CLAUDE.md`, the Brain Keeper and skill templates): these are the person's instructions to their agent, so they use **«ты»** imperatives («прочитай», «спроси», «не трогай»). Russians talk to AI assistants with «ты», and the trigger phrases are in «ты» too.
- **Trigger phrases** are what a person says to the agent, so they use «ты»: «проверь мой мозг», «подготовь меня к встрече с {name}». The English phrase always follows, so both work.
- `instructions_example` (text the person pastes into the agent's settings) is in the person's voice, so it uses «ты».
- "your agent" is «ваш агент» in text for the person and just «агент» in rule files.

## Grammar notes

- Russian names change with case (Анна, Анне, Анны). Templates put `{Name}` in the nominative (as the subject: «когда {Name} просит», «пусть решает {Name}») so a plain swap reads correctly. Keep it that way when editing.
- Avoid past-tense verbs and adjectives that show gender after `{Name}` or about the agent («решил», «готов»). Use the present tense or rephrase.
- Numbers with `{n}`: Russian nouns change after numbers (1 папка, 2 папки, 5 папок), so `{n}` goes in brackets or after a colon: «папки ({n})».
- No «ё»: written as «е» everywhere, as most apps do, so names, search and links never split on е/ё («отчеты», «Партнеры», «еще»).
- Quotes: «ёлочки», with „лапки“ inside them.

## Feature names

| English | Russian |
|---|---|
| Phygital Brain | Phygital Brain |
| second brain | второй мозг |
| Brain Keeper | Хранитель мозга |
| morning brief | утренняя сводка |
| meeting prep | подготовка к встрече |
| thinking tools | инструменты мышления |
| check-up | проверка |
| Writing Check | Проверка текста |
| your agent | ваш агент |

## Folder and note names

| English | Russian | Why |
|---|---|---|
| About | Профиль | One word, the usual name for "about me" in apps |
| Daily | Дневник | A daily journal |
| Projects | Проекты | |
| Relationships | Контакты | Covers people and organisations, the word apps use |
| Memory | Память | |
| Library | Библиотека | |
| Skills | Навыки | |
| Clients | Клиенты | |
| Collaborators | Соавторы | Creative partners with no money involved |
| Team | Команда | |
| Partners | Партнеры | |
| decisions | решения | |
| research | исследования | |
| finances | финансы | |
| archive | архив | |
| applications | заявки | Jobs, grants, open calls |
| competitors | конкуренты | |
| notes | заметки | |
| briefs | брифы | The word Russian creative work uses |
| drafts | черновики | |
| ideas | идеи | |
| feedback | отзывы | |
| assets | медиа | Images and media |
| prompts | промпты | |
| templates | шаблоны | |
| frameworks | методики | Plainer than «фреймворки» |
| brain-keeper | хранитель-мозга | |
| morning-brief | утренняя-сводка | |
| meeting-prep | подготовка-к-встрече | |
| thinking | мышление | |
| import | импорт | |
| connected-apps | подключенные-приложения | |
| reports | отчеты | |
| me | обо-мне | `Профиль/обо-мне.md` |
| goals | цели | |
| business | бизнес | |
| services | услуги | |
| customers | аудитория | Not «клиенты», to keep it apart from the Clients folder |
| pain-points | проблемы | «боли» is marketing slang |
| brand | бренд | |
| tools | инструменты | |
| cv | резюме | |
| biography | биография | |
| tasks | задачи | |
| _Leads | _Лиды | The usual word among freelancers and small businesses |
| daily | ежедневная-уборка | The Brain Keeper's daily task file (renamed from «ежедневно» in review: an adverb reads oddly as a file name) |
| check-up | проверка | |
| queue | очередь | |
| PAUSED | ПАУЗА | |

## Other terms

| English | Russian |
|---|---|
| info block (frontmatter) | блок информации (frontmatter) |
| daily note | заметка дня |
| Knowledge Routing / routing table | Куда что класть |
| compiled-truth format | формат «актуальная правда» |
| evidence | доказательства |
| Backups and Undo | Резервные копии и отмена |
| {Name}'s Rules | Личные правила |
| wikilinks | вики-ссылки |
| callouts | выноски |
| orphan notes | заметки-сироты |
| lead / New / Keep warm | лид / Новые / Не терять связь |
| Needs {Name} / To fix / Next folder / Last run | Нужно решение: {Name} / Исправить / Следующая папка / Последний запуск |
| dry run | пробный запуск |
| safe fixes / report only (setting values) | stay in English |
| Tax IDs | ИНН, СНИЛС |

## Example names

Ana Costa → Анна Соколова, Marta → Марина, João → Илья, Lia → Лиза, Lisbon, Portugal → Санкт-Петербург, Россия. Social links use VK and Telegram.

## Adapted, not literal

- The root `CLAUDE.md` Language section says, like the English, that folder names, file names and links stay exactly as these rules write them («в точности такими, как они написаны в этих правилах»), and info block keys and values stay in English.
- "accents" in the duplicate-name check became ё/е, short names and Latin vs Cyrillic spelling.
