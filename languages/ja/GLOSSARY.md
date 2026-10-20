# 日本語（ja）用語集

The words chosen for the Japanese set, and why.

## Register

- Everything a person reads: polite です・ます, like Japanese consumer apps (LINE, Notion, Apple). Never 敬語 beyond that (no ございます, いたします).
- Rule files (`CLAUDE.md`) use です・ます in sentences, and short noun endings (体言止め) in tables and short bullets, as Japanese help pages do. Instructions to the agent use 〜します / 〜してください.
- Buttons and options are short plain phrases (「今すぐ接続する」「あとで」「次へ」), as Japanese apps write them.
- Trigger phrases (what a person says to the agent) are casual 〜して (「ブレインを総点検して」), which is how people really talk to an assistant. The English phrase follows each one.
- The person is called {Name}さん in the rule files. Example people get さん too (森さん).
- Japanese punctuation: 。、「」（）and full-width ：. No em dash, no ―.

## Feature names

| English | Japanese | Why |
|---|---|---|
| Phygital Brain | Phygital Brain | stays English |
| second brain | セカンドブレイン | the term Japanese readers know from the book and blogs |
| brain (the person's brain) | ブレイン | short, matches セカンドブレイン; 脳 sounds medical |
| Brain Keeper | ブレイン整理係 | 係 = the one in charge of a job; says what it does (tidies) |
| morning brief | 朝のまとめ | plain; ブリーフィング is office jargon |
| meeting prep | 打ち合わせ準備 | 打ち合わせ is the everyday word for a work meeting |
| thinking tools | 思考ツール | common, short |
| check-up | 総点検 | a full look at everything; 点検 alone sounds small |
| Writing Check | 文章チェック | everyday |
| your agent | あなたのエージェント (often just エージェント) | Japanese usually drops あなたの |
| dry run | テスト実行 | |

## Top folders

| English | Japanese |
|---|---|
| About | プロフィール |
| Daily | 日記 |
| Projects | プロジェクト |
| Relationships | 人脈 |
| Memory | 記録 |
| Library | ライブラリ |
| Skills | スキル |

- 日記 over デイリー: everyday word, and the folder is a day-by-day journal.
- 人脈 over 人間関係: 人間関係 sounds like personal or family life; 人脈 is the people you work with.
- 記録 over メモリー: decisions, research, money and the archive are records.

## Subfolders and notes

| English | Japanese | | English | Japanese |
|---|---|---|---|---|
| Clients | クライアント | | me | 自分 |
| Collaborators | 協力者 | | goals | 目標 |
| Team | チーム | | business | ビジネス |
| Partners | パートナー | | services | サービス |
| decisions | 決定事項 | | customers | 顧客 |
| research | リサーチ | | pain-points | 悩み |
| finances | お金 | | brand | ブランド |
| archive | アーカイブ | | tools | ツール |
| applications | 応募 | | cv | 経歴 |
| competitors | 競合 | | biography | 生い立ち |
| notes | メモ | | tasks | タスク |
| briefs | 依頼内容 | | _Leads | _見込み客 |
| drafts | 下書き | | brain-keeper | ブレイン整理係 |
| ideas | アイデア | | daily (keeper task) | 毎日の整理 |
| feedback | フィードバック | | check-up | 総点検 |
| assets | 素材 | | queue | 確認リスト |
| prompts | プロンプト | | PAUSED | 一時停止中 |
| templates | テンプレート | | morning-brief | 朝のまとめ |
| frameworks | フレームワーク | | meeting-prep | 打ち合わせ準備 |
| reports | レポート | | thinking | 思考ツール |
| import | 取り込み | | connected-apps | 連携アプリ |

- Clients (クライアント) and customers (顧客) stay different words: one is a folder of people, the other the note about who buys.
- Japanese has no case and no spaces, so names have no hyphens.

## Fixed terms

| English | Japanese |
|---|---|
| note | ノート (a person's notes from other apps: メモ) |
| daily note | 日記 |
| info block (frontmatter) | 情報ブロック（frontmatter） |
| compiled-truth format | まとめ形式 |
| current truth / evidence | 今の情報 / 根拠 |
| Knowledge Routing | 情報の振り分け |
| Session Startup | チャットの始め方 |
| Backups and Undo | バックアップと元に戻す |
| {Name}'s Rules | {Name}さんのルール |
| What it is / Status and next step | 概要 / 状況と次の一歩 |
| How it runs / Where things are | 自動で動いているもの / ファイルの場所 |
| lead / New / Keep warm | 見込み客 / 新規 / つながりを保つ |
| Needs {Name} / To fix / Next folder / Last run | {Name}さんの確認待ち / 修正待ち / 次のフォルダー / 前回の実行 |
| Open decisions / From your apps / Meetings | 未完了の決定事項 / アプリから / 打ち合わせ |
| needs review | 見直しが必要 |
| (from email) / (from calendar) | （メールより） / （カレンダーより） |
| broken link / orphan note | リンク切れ / 孤立したノート |
| work day | 仕事の日 |
| scheduled task | 予定タスク |
| em dash | 長いダッシュ（em dash） |
| connector | コネクター |

## Placeholders

Placeholders the check script knows (`{Name}`, `{Language}`, `{weekday in English}`, `{person or company}`, `{Project-Name}` and the like) are copied exactly. Longer braces that describe what to write (`{一文で：…}`) are translated, since the agent fills them in Japanese.

## Example names

| English | Japanese |
|---|---|
| Ana Costa (illustrator) | 佐藤花 |
| Marta (editor) | 森さん |
| João (studio partner) | 健太 |
| Lia (agent) | 中村さん (マネージャー) |
| Lisbon, Portugal | 東京都 |

LINE was added next to WhatsApp in rule 31, since it is the chat app most people in Japan use.
