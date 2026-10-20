時間とともにたまっていく知識です：決定事項、リサーチ、応募、アーカイブ。

## 振り分け

| 内容 | 置き場所 |
|---|---|
| 理由つきの決定、または外部のもの（アプリ、ウェブサイト、講座、競合）の調査 | `decisions/YYYY-MM-DD-{title}.md` |
| リサーチ（市場、トレンド、選択肢） | `research/{topic}.md` |
| 応募：求人、助成金、賞、公募（最初に必要になったときに作成） | `applications/{name}/` |
| 競合のプロフィール（最初に必要になったときに作成） | `competitors/{name}.md` |
| お金：請求書、税金、支払い。非公開 | `finances/` |
| アーカイブした決定事項 | `archive/decisions/` |
| 終わった、または古くなったリサーチ | `archive/research/` |
| 終わったプロジェクト | `archive/{name}/` |
| 打ち合わせのメモ | 何か決まったなら `decisions/`、そうでなければその日の `Daily/` の日記。打ち合わせ用のフォルダーは、メモがたくさんたまったときだけ提案します。 |

## 情報ブロック（frontmatter）

```yaml
---
type: research
date: 2026-10-13
status: active
tags: [research, pricing]
---
```

- `type`：`decision`、`research`、`application`、`competitor`。
- `date`：ノートを書いた日付。
- `status`：決定事項と応募については下を見てください。それ以外は `active` か `closed`。
- `tags`：種類、次にトピック。
- 任意：`project`、`deadline`、`description`（一文をダブルクォーテーションで囲み、最後の行に）。

## 決定事項のノート

必ず理由を書きます：誰が関わったか、何がきっかけか、何をあきらめて何を取ったか。決定そのものには `> [!important]`、わかっているリスクには `> [!warning]` を使います。

決定事項には、`date:` のすぐあとに `updated:` もつけます。`date` は作った日、`updated` は最後に見直したり変えたりした日です。

```yaml
---
type: decision
date: 2026-09-02
updated: 2026-10-13
status: open
tags: [decision, website]
---
```

- `status`：`open`（まだ検討中、または進行中）、`waiting`（ほかの人待ち）、`paused`、`closed`。
- `updated` が30日より前の決定事項は見直しが必要です。{Name}さんが「このまま続ける」「終わりにする」「アーカイブする」のどれかを選ぶまで、ブレイン整理係が知らせ続けます（どれを選んでも `updated` がその日の日付になります）。
- 決定事項を `archive/decisions/` に移すのは、{Name}さんがそう言ったときだけです。

## 応募

応募ごとにフォルダーを1つ作ります：`applications/{name}/`。中の `README.md` に、締め切り、リンク、状況、送ったものを書きます。ほかのファイル（回答、志望動機など）はその横に置きます。

- `status`：`draft`、`submitted`、`accepted`、`rejected`、`withdrawn`。
- 回答はMarkdownで残します。大きなPDFやスライドはブレインの外に置き、ノートに要約を書きます。

## ルール

- リサーチは、特に頼まれない限り中立に行います（ルートのルール23）。
- 新しいものに置き換わったリサーチは、削除せず `archive/research/` に移します。
- `finances/` は非公開で、`.claudeignore` に書かれています。{Name}さんが特定のファイルを頼んだときだけ開きます（ルートのルール8）。
