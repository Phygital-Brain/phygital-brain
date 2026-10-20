# 简体中文（zh-CN）术语表

## 称呼

一律用“你”，不用“您”。微信、小红书、抖音等大多数国内消费类应用都用“你”，显得亲近、不生分。

## 功能名

| English | 中文 | 说明 |
|---|---|---|
| Phygital Brain | Phygital Brain | 不翻译 |
| Brain Keeper | 大脑管家 | |
| morning brief | 晨间简报 | |
| meeting prep | 会前准备 | |
| thinking tools | 思考工具 | |
| check-up | 体检 | 常说“给我的大脑做个体检” |
| Writing Check | 写作检查 | |
| second brain | 第二大脑 | |
| your agent | 你的 AI 助手 | 不用“智能体”，普通用户更熟悉“AI 助手” |

## 顶层文件夹

| English | 中文 |
|---|---|
| About | 关于我 |
| Daily | 日记 |
| Projects | 项目 |
| Relationships | 人脉 |
| Memory | 记忆 |
| Library | 资料库 |
| Skills | 技能 |

## 子文件夹和笔记名

| English | 中文 | English | 中文 |
|---|---|---|---|
| Clients | 客户 | Collaborators | 合作者 |
| Team | 团队 | Partners | 合作伙伴 |
| decisions | 决定 | research | 调研 |
| finances | 财务 | archive | 归档 |
| applications | 申请 | competitors | 竞争对手 |
| notes | 笔记 | briefs | 需求简报 |
| drafts | 草稿 | ideas | 想法 |
| feedback | 反馈 | assets | 素材 |
| prompts | 提示词 | templates | 模板 |
| frameworks | 框架 | reports | 报告 |
| brain-keeper | 大脑管家 | morning-brief | 晨间简报 |
| meeting-prep | 会前准备 | thinking | 思考工具 |
| import | 导入 | connected-apps | 已连接的应用 |
| me | 个人档案 | goals | 目标 |
| business | 业务 | services | 服务 |
| customers | 客户画像 | pain-points | 痛点 |
| brand | 品牌 | tools | 工具 |
| cv | 简历 | biography | 个人经历 |
| tasks | 待办 | _Leads | _潜在客户 |
| daily（大脑管家的任务文件） | 每日整理 | check-up | 体检 |
| queue | 管家清单 | PAUSED | 已暂停 |

- `me` 用“个人档案”而不是“我”，因为“建好了 [[我]]”读起来别扭。
- `customers`（客户画像）和 `Clients`（客户）分开，避免同名。
- `queue` 用“管家清单”，避免和“待办”（`tasks`）混淆。
- `_Leads` 保留下划线，让它在文件夹里排在最前面。

## 固定说法

| English | 中文 |
|---|---|
| root rule 17 | 总规则第 17 条 |
| root `CLAUDE.md` | 根目录的 `CLAUDE.md` |
| info block (frontmatter) | 信息块（frontmatter） |
| compiled-truth format | “事实汇总”格式 |
| evidence | 依据 |
| wikilinks | 双链 |
| callout | 提示框 |
| routing / routing table | 归类 / 归类表 |
| Knowledge Routing | 知识归类 |
| Session Startup | 对话开始时 |
| Backups and Undo | 备份和撤销 |
| session log | 对话记录 |
| orphan note | 孤立笔记 |
| broken link | 失效链接 |
| lead | 潜在客户 |
| created on first use | 第一次用到时创建 |
| em dash | 破折号 |
| or the same in {Language} | 或者用 {Language} 说同样的意思 |

## 笔记里的标题

这些标题会写进笔记，几个文件互相引用，必须一致：

| English | 中文 |
|---|---|
| What it is | 简介 |
| Status and next step | 现状和下一步 |
| How it runs | 运行方式 |
| Where things are | 文件在哪 |
| Evidence | 依据 |
| Open / Done（待办） | 未完成 / 已完成 |
| New / Keep warm（潜在客户） | 新线索 / 保持联系 |
| Connected / None yet. | 已连接 / 暂无。 |
| Rules per project | 单个项目的规则 |
| {Name}'s Rules | {Name} 的规则 |
| Last run / Needs {Name} / To fix / Next folder | 上次运行 / 需要 {Name} 处理 / 待修复 / 下一个文件夹 |
| Open decisions / From your apps / Meetings | 待定的决定 / 来自你的应用 / 会议 |
| (from email) / (from calendar) / needs review | （来自邮件） / （来自日历） / 需要复查 |
| Summary / Files changed / Fixed / Queued / Errors | 摘要 / 改动的文件 / 已修复 / 已放进清单 / 错误 |
| Dry run | 试运行 |

## 示例里的名字

| English | 中文 |
|---|---|
| Ana Costa | 林晓 |
| Marta（编辑） | 王敏 |
| João（工作室合伙人） | 张磊 |
| Lia（经纪人） | 李娜 |
| Lisbon, Portugal | 浙江杭州 |
| Instagram / LinkedIn / TikTok 示例账号 | 小红书 / 微博 / 抖音 |
| Evernote | 印象笔记 |
| Apple Notes | 苹果备忘录 |

## 其他说明

- 触发语先写中文，再写英文原句，两种都能用。
- `{Fix mode}` 的值 `safe fixes`、`report only` 和运行提示里的 “dry run” 保留英文，因为设置技能会原样填入。
- 根目录 `CLAUDE.md` 的“语言”部分和英文原文一致：文件夹名、文件名和链接“一律和这些规则里写的完全一样”（构建时规则里的路径已经换成中文名）。
- 写作检查的清单里加了几个中文常见的 AI 味词（“赋能”、“助力”等），只是例子，规则本身没变。
- 句子式的占位符（比如 `{一句话：这个文件放了什么。}`）翻成了中文；`{Name}`、`{weekday in English}` 这类保持英文。
