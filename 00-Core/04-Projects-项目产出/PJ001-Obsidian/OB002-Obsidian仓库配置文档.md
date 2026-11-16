---
type: project
status: 已完成
tags:
  - obsidian
  - 配置文档
  - 项目产出
created: 2026-06-13
updated: 2026-11-16
---

> 本文档记录本 Obsidian 仓库的完整配置信息，包括目录结构、插件清单、主题设置、同步方案及 AI 集成等。供后续迁移、重建或多设备同步时参考。

---

## 1. 仓库概览

| 项目 | 内容 |
|------|------|
| **仓库名称** | JW-wiki-obsidian-multi-device-sync |
| **GitHub 远程** | `git@github.com:JabinWei/JW-wiki-obsidian-multi-device-sync.git` |
| **用途** | 数学笔记、代码笔记、AI 知识库管理、音乐收藏 |
| **核心特性** | 双链笔记、本地存储、开源插件、AI 集成 |
| **操作系统** | macOS |

---

## 2. 目录结构 (IAR 知识管理框架)

```
obsidian-notes/
├── Home.md                      # 知识库首页（Excalidraw 可视化入口）
├── README.md                    # 仓库说明
├── .gitignore                   # 忽略 macOS/Obsidian 瞬态文件
│
├── 00-Core/                     # 📁 核心层 — 长期沉淀的知识
│   ├── 01-CoreKnowledge-核心知识/
│   │   ├── C001-计算机基础知识/
│   │   │   ├── CB001-编程语言/
│   │   │   │   └── PL001-Python/          # Python 学习笔记
│   │   │   ├── CB002-数据结构与算法/
│   │   │   │   ├── DSAL001-概念/          # 语言无关概念（笔记用 DS/AL 前缀）
│   │   │   │   ├── DSAL002-Python/        # 各语言实现
│   │   │   │   ├── DSAL003-C/
│   │   │   │   ├── DSAL004-C++/
│   │   │   │   ├── DSAL005-Java/
│   │   │   │   └── DSAL006-JavaScript/
│   │   │   ├── CB003-计算机知识导论/        # 计算机知识导论（底层原理，参考《大话计算机》）
│   │   │   └── CB004-操作系统/
│   │   │       ├── OS001-原理/            # 操作系统通用原理（笔记用 OSB 前缀）
│   │   │       └── OS002-Linux/           # Linux 使用实操（笔记用 LX 前缀）
│   │   ├── C002-人工智能/
│   │   │   └── AI001-数据分析/             # Numpy + Pandas
│   │   ├── C003-数学/
│   │   │   ├── MA001-微积分/
│   │   │   ├── MA002-线性代数/
│   │   │   └── MA999-数学学习路线.md      # 辅助文件从 999 往下排
│   │   ├── C004-英语/
│   │   │   ├── EN001-英语口语/
│   │   │   └── EN002-Podcast/
│   │   ├── C005-全栈开发/
│   │   ├── C006-网络安全/
│   │   ├── C007-音乐/
│   │   │   └── MU001-钢琴/            # 按所学主题建子目录（声乐/吉他/琴谱收藏…）
│   │   └── C008-工具/
│   │       └── TL001-ClaudeCode/      # Claude Code 使用笔记（TL = Tool 工具类前缀）
│   ├── 02-CardKnowledge-卡片知识/   # 原子化卡片笔记
│   ├── 03-KnowledgeMap-知识地图/    # 知识索引/MOC
│   ├── 04-Projects-项目产出/
│   │   ├── PJ001-Obsidian/           # Obsidian 项目相关文档
│   │   ├── PJ002-知识卡片提取计划.md  # 核心知识→卡片知识提取
│   │   ├── PJ003-仓库健康报告/       # 定期仓库健康检查
│   │   └── PJ004-Python项目练习/     # Python 项目实战
│   └── 05-IPManagement-IP形象管理/   # 个人IP形象「小蓝」设定与插图范式
│
├── 10-Action/                   # 📁 行动层 — 待办事项与任务
│
├── 20-Inspiration/              # 📁 灵感层 — 收集的素材与启发
│
├── 30-Time/                     # 📁 时间层 — 计划与回顾
│   ├── 31-Vision-愿景/
│   └── 32-Weekly-周计划/
│
├── 40-Library/                  # 📁 书架层 — 已读书籍卡片
│
├── generated-images/            # 📁 AI 生成图片（私密，已 gitignore，仅本地）
│   └── prompts/                  #   每个图片的 Prompt 文件（只保留最终版）
│
└── 90-Storage/                  # 📁 存储层 — 资源与模板
    ├── 91-Archive-归档/
    ├── 97-Changelog-更新日志/       # 笔记变更日志
    ├── 98-Asset-资源/
    │   ├── ArticleIllustrator/      # 文章插图
    │   ├── Circuit/                 # 电路图
    │   ├── CoverImage/              # 封面图
    │   ├── Diagram/                 # 技术图表（SVG）
    │   ├── Excalidraw/              # Excalidraw 绘图文件
    │   ├── ImageFootage/            # 图片素材
    │   ├── InfoGraphic/             # 信息图
    │   ├── Mathcraft/               # Mathcraft 函数图像缓存
    │   ├── MathSvg/                 # 数学 SVG 图形
    │   ├── PdfFootage/              # PDF 素材
    │   └── VideoFootage/            # 视频素材
    └── 99-Templates-模版/           # 各类笔记模板
```

### 编号规则

**主内容编号**：从 `001` 往上递增（如 `MA001`、`MA002`、`MA003`...）

**辅助文件编号**：从 `999` 往下递减（如 `MA999`、`MA998`、`MA997`...）
> 辅助文件包括：学习路线、索引、元信息、工具脚本等非核心学习内容

**前缀清单**：

- **C** = Category（知识大类）
- **CB** = Category Branch（知识分支）
- **AI** = Artificial Intelligence（人工智能分支）
- **PL** = Programming Language（编程语言）
- **MA** = Math（数学）
- **MU** = Music（音乐）
- **CA** = Calculus（微积分）
- **LA** = Linear Algebra（线性代数）
- **EN** = English（英语）
- **ES** = English Speaking（英语口语）
- **EP** = English Podcast（英语播客）
- **PY** = Python
- **DS** = Data Structure（数据结构）
- **AL** = Algorithm（算法）
- **NP** = NumPy（数据分析）
- **PD** = Pandas（数据分析）
- **CL** = C Language（C 语言）
- **TP** = Template（模板）
- **PJ** = Project（项目）
- **PYPJ** = Python Project（Python 项目练习）
- **CC** = Claude Code（Claude Code 工具）
- **CI** = Computer Introduction（计算机知识导论）
- **OB** = Obsidian

---

## 3. 多端同步方案

使用 **GitHub** 进行多设备同步：

```bash
# 远程仓库
git@github.com:JabinWei/JW-wiki-obsidian-multi-device-sync.git

# 同步流程
git add .
git commit -m "update"
git push origin master
```

> **注意**：`.obsidian/` 配置目录已纳入版本控制，克隆后可保留一致的插件和主题配置。

> **`.gitignore` 规则**：已排除 macOS 系统垃圾（`.DS_Store` 等）、Obsidian 界面瞬态状态（`workspace.json`、`cache/`、`.trash/`）、插件运行时上下文（`termy/agent-context/`）、`node_modules/`，以及 `generated-images/`（AI 生成私密图片，仅本地保存），避免多设备同步时产生冲突。

---

## 4. Obsidian 全局设置

### 4.1 外观 (`appearance.json`)

| 设置项 | 值 |
|--------|-----|
| 基础主题 | **Minimal** |
| 主题模式 | 跟随系统 (`system`) |
| 基础字号调节 | 启用 |
| 显示功能区 | 启用 |
| 原生菜单 | 禁用 |

### 4.2 编辑器与文件 (`app.json`)

| 设置项 | 值 |
|--------|-----|
| 始终更新链接 | ✅ 启用 |
| PDF 导出 - 包含文件名 | ✅ 启用 |
| PDF 页面尺寸 | Letter |
| PDF 缩放 | 100% |

### 4.3 核心插件状态 (`core-plugins.json`)

**已启用：**

| 核心插件 | 状态 |
|----------|------|
| 文件列表 | ✅ |
| 全局搜索 | ✅ |
| 快速切换 | ✅ |
| 关系图谱 | ✅ |
| 反向链接 | ✅ |
| 白板 (Canvas) | ✅ |
| 出链 | ✅ |
| 标签面板 | ✅ |
| 属性 (Properties) | ✅ |
| 页面预览 | ✅ |
| 日记 | ✅ |
| 模板 | ✅ |
| 笔记重组 | ✅ |
| 命令面板 | ✅ |
| 编辑器状态 | ✅ |
| 书签 | ✅ |
| 大纲 | ✅ |
| 字数统计 | ✅ |
| 文件恢复 | ✅ |
| Sync (同步) | ✅ |
| Bases (数据库) | ✅ |

**已禁用：** 脚注、斜杠命令、Markdown 导入器、ZK 前缀器、随机笔记、幻灯片、录音机、工作区、发布、Web 查看器

---

## 5. 社区插件清单

### 5.1 核心功能增强

| 插件 | 版本 | 用途 | 来源 |
|------|------|------|------|
| **Dataview** | 0.5.68 | 通过查询语法对笔记进行高级数据检索和展示 | 官方市场 |
| **Templater** | 2.20.5 | 高级模板引擎，支持类 Handlebars 语法 | 官方市场 |
| **Note Refactor** | 1.8.2 | 提取笔记内容为新笔记，拆分笔记 | 官方市场 |
| **Easy Typing** | 6.0.8 | 编辑体验优化，自动格式化 | 官方市场 |
| **Notebook Navigator** | 3.1.2 | 双栏文件浏览器，替代默认文件列表 | 官方市场 |

### 5.2 数学与绘图

| 插件 | 版本 | 用途 | 来源 |
|------|------|------|------|
| **Mathcraft (Albus)** | 2.3.2 | 定理编号、公式编号、TikZ 渲染、GeoGebra 集成、函数绘图 | BRAT（`AlbusGuo/obsidian-mathcraft`）|
| **LaTeX Suite** | 1.11.5 | 快速 LaTeX 数学排版，代码片段与快捷键 | 官方市场 |
| **Excalidraw** | 2.23.12 | 手绘风格流程图、示意图、可视化绘图 | 官方市场 |

### 5.3 图片与图床

| 插件 | 版本 | 用途 | 来源 |
|------|------|------|------|
| **Image Auto Upload** | 4.1.0 | 粘贴图片自动通过 PicGo 上传到 OSS 图床 | 官方市场 |

> **图床配置**：使用 PicGo + 阿里云 OSS（上海地域）
> - 存储桶地址：`picgo-storage-typora.oss-cn-shanghai.aliyuncs.com`

### 5.4 AI 集成

| 插件 | 版本 | 用途 | 来源 |
|------|------|------|------|
| **Claudian** | 2.0.24 | 在 Obsidian 中内嵌 Claude Code 编程助手 | BRAT（`YishenTu/claudian`）|
| **Termy** | 1.4.1 | 内置终端模拟器，支持 Claude Code CLI | 官方市场 |

> **AI 链路架构**：
> ```
> Obsidian → Termy/Claudian 插件 → Claude Code CLI
>                                    ↓
>                            CC Switch（代理）
>                                    ↓
>                       DeepSeek API (deepseek-chat)
>                       API 地址: https://api.deepseek.com
> ```

### 5.5 主题与样式

| 插件 | 版本 | 用途 | 来源 |
|------|------|------|------|
| **Minimal Theme Settings** | 8.2.3 | Minimal 主题的细分配置（颜色/字体/特性） | 官方市场 |
| **Style Settings** | 1.0.9 | 全局 CSS 变量调整控件 | 官方市场 |
| **Callout Manager** | 1.1.1 | 快速创建和自定义 Callout 块 | 官方市场 |

### 5.6 插件管理

| 插件 | 版本 | 用途 | 来源 |
|------|------|------|------|
| **BRAT** | 2.0.8 | 安装和测试插件 Beta 版本 | 官方市场 |

---

## 6. 关系图谱配置

```json
{
  "collapse-filter": true,
  "showOrphans": true,
  "centerStrength": 0.5187,
  "repelStrength": 10,
  "linkStrength": 1,
  "linkDistance": 250,
  "scale": 1
}
```

---

## 7. 工作区布局

当前工作区采用三分栏布局：

| 区域 | 内容 |
|------|------|
| **左侧边栏** (466.5px) | 文件列表 → 搜索 → 书签 → 笔记本导航器 |
| **主编辑区** | Markdown 编辑器 + Excalidraw 绘图 + Claudian AI 面板 |
| **右侧边栏** (300px, 折叠) | 反向链接 → 出链 → 标签 → 属性 → 大纲 → Claudian 视图 |
| **底部终端** | Termy 终端（Claude Code） |

---

## 8. 模板清单

存储于 `90-Storage/99-Templates-模版/`：

| 模板文件 | 用途 |
|----------|------|
| TP001-通用笔记模版 | 通用临时笔记 |
| TP002-卡片笔记模版 | 原子化知识卡片 |
| TP003-索引笔记模版 | MOC（内容地图）索引 |
| TP004-项目笔记模版 | 项目产出文档 |
| TP005-读书笔记模版 | 阅读笔记记录 |
| TP006-闪念笔记模版 | 快速捕捉灵感 |
| TP007-任务行动模版 | 行动/待办事项 |
| TP008-灵感创意模版 | 创意记录与孵化 |
| TP009-愿景规划模版 | 长期愿景与目标 |
| TP010-周计划模版 | 每周计划安排 |
| TP011-系统学习模版 | 系统化学习笔记 |

---

## 9. AI 环境配置要点

### CC Switch 配置
- API 地址：`https://api.deepseek.com`
- 模型名称：`deepseek-chat`
- API Key：DeepSeek 平台申请的 `sk-xxx`

### Claude Code 安装
```bash
npm install -g @anthropic-ai/claude-code
```

### Termy 终端路径问题
若 Termy 无法识别 `claude` 命令，在 `~/.zshrc` 中添加：
```bash
export PATH="$HOME/.npm-global/bin:/opt/homebrew/bin:$PATH"
source ~/.zshrc
```

### Claude Code 二进制修复
若报错 `native binary not installed`：
```bash
npm cache clean --force
npm uninstall -g @anthropic-ai/claude-code
npm install -g --include=optional @anthropic-ai/claude-code
```

### image-gen Skill（AI 生图）

用于生成阿砚 IP 封面、概念插图、封面图。基于 `gpt-image-2` 模型，走 apimart.ai 异步接口。

**目录结构**：
```
~/.claude/skills/image-gen/
├── SKILL.md                # skill 说明（Claude Code 自动加载）
├── .env                    # API 配置（不入库，本地私有）
└── scripts/
    └── generate_image.py  # 统一生图脚本
```

**`.env` 字段**（API key 不写进仓库，从 apimart.ai 控制台申请后本地填写）：
| 字段 | 含义 | 示例值 |
|------|------|--------|
| `IMG_BASE_URL` | API 端点 | `https://api.apimart.ai/v1` |
| `IMG_MODEL` | 模型名 | `gpt-image-2` |
| `IMG_API_KEY` | 密钥 | （从 apimart.ai 控制台获取，**不要提交到 git**） |

**脚本完整参数**：
| 参数 | 说明 | 默认 |
|------|------|------|
| `--prompt` / `--prompt-file` | Prompt 文本或从文件读取（二选一） | 必填 |
| `--output-dir` | 输出目录 | `generated-images` |
| `--env-file` | .env 路径 | 自动向上查找 |
| `--mode` | `sync` / `async` | 按 base URL 自动检测（含 apimart → async） |
| `--size` | 比例：`1:1` / `2:3` / `3:2` / `16:9` / `9:16` 等 | `1:1` |
| `--resolution` | `1k` / `2k` / `4k` | `2k` |
| `--image` | 参考图路径（可多次传，用于角色一致性锁脸） | 无 |
| `--poll-interval` | 异步轮询间隔秒数 | `5` |
| `--timeout` | 异步轮询超时秒数 | `180` |
| `--format` | `png` / `jpeg` / `webp` | `png` |

**常用调用**：
```bash
# 横版 banner（封面图，16:9）
cd ~/.claude/skills/image-gen && python3 scripts/generate_image.py \
  --env-file .env \
  --prompt-file <repo>/generated-images/prompts/prompt-xxx-v1.md \
  --output-dir <repo>/generated-images \
  --size 16:9 --resolution 2k

# 竖版人物全身（2:3）
python3 scripts/generate_image.py --env-file .env \
  --prompt "..." --output-dir generated-images --size 2:3 --resolution 2k
```

**行为约定**：
- 异步模式自动轮询（约 40s/张），单张费用约 $0.015
- 生成文件落 `<output-dir>/image-{时间戳}.png`，**生成后必须按仓库规则重命名并搬运**——见 OB003 §5.2「阿砚 IP 封面生成 SOP」
- prompt 草稿先写在仓库 `generated-images/prompts/prompt-{slug}-v{N}.md`（gitignore 临时区），定稿后 prompt 也要搬进 `CoverImage/{笔记名}/prompts/` 入库
- **配套 Skill**：`stem-illustration`（科研示意图生图，同一套 API 配置）

**迁移到新电脑时**：
1. 从 apimart.ai 控制台申请新 API key
2. 在 `~/.claude/skills/image-gen/` 下放 `SKILL.md` + `scripts/generate_image.py`（从旧机拷贝或重新安装 skill）
3. 本地创建 `.env`，填入 `IMG_BASE_URL=https://api.apimart.ai/v1`、`IMG_MODEL=gpt-image-2`、`IMG_API_KEY=<新 key>`
4. 仓库内的 `generated-images/prompts/` 和 `90-Storage/98-Asset-资源/CoverImage/` 随 git 同步，不需要额外配置

---

## 10. 相关文档

- [[OB001-UPDATE LOG]] — 初始搭建日志与踩坑记录
- [[OB003-仓库笔记管理默认规则]] — 笔记编写与管理规范
- [[OB004-AI协作记忆]] — AI 跨会话持久记忆（学习策略、用户偏好、项目状态）
- [[PJ002-知识卡片提取计划]] — 卡片知识提取跟踪
- [[PJ003-仓库健康报告/2026-07-20-仓库健康报告]] — 仓库健康检查

---

> **最后更新**：2026-11-16 | **维护者**：Jabin W.
