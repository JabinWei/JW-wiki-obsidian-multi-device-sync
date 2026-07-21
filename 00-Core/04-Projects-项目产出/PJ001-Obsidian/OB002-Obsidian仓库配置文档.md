---
type: project
status: 已完成
tags:
  - obsidian
  - 配置文档
  - 项目产出
created: 2026-06-13
updated: 2026-06-13
---

> 本文档记录本 Obsidian 仓库的完整配置信息，包括目录结构、插件清单、主题设置、同步方案及 AI 集成等。供后续迁移、重建或多设备同步时参考。

---

## 1. 仓库概览

| 项目 | 内容 |
|------|------|
| **仓库名称** | JW-wiki-obsidian-multi-device-sync |
| **GitHub 远程** | `git@github.com:JabinWei/JW-wiki-obsidian-multi-device-sync.git` |
| **用途** | 数学笔记、代码笔记、AI 知识库管理 |
| **核心特性** | 双链笔记、本地存储、开源插件、AI 集成 |
| **操作系统** | macOS |

---

## 2. 目录结构 (IAR 知识管理框架)

```
obsidian-notes/
├── Home.md                      # 知识库首页（Excalidraw 可视化入口）
├── README.md                    # 仓库说明
│
├── 00-Core/                     # 📁 核心层 — 长期沉淀的知识
│   ├── 01-CoreKnowledge-核心知识/
│   │   ├── C001-计算机基础知识/
│   │   │   └── CB001-编程语言/
│   │   │       └── PL001-Python/       # Python 学习笔记
│   │   ├── C002-人工智能/
│   │   ├── C003-数学/
│   │   │   └── MA001-微积分/
│   │   └── C004-英语/
│   │       └── EN001-英语口语/
│   ├── 02-CardKnowledge-卡片知识/   # 原子化卡片笔记
│   ├── 03-KnowledgeMap-知识地图/    # 知识索引/MOC
│   └── 04-Projects-项目产出/
│       └── PJ001-Obsidian/           # Obsidian 项目相关文档
│
├── 10-Action/                   # 📁 行动层 — 待办事项与任务
│
├── 20-Inspiration/              # 📁 灵感层 — 收集的素材与启发
│
├── 30-Time/                     # 📁 时间层 — 计划与回顾
│   ├── 31-Vision-愿景/
│   └── 32-Weekly-周计划/
│
└── 90-Storage/                  # 📁 存储层 — 资源与模板
    ├── 91-Archive-归档/
    ├── 98-Asset-资源/
    │   ├── Excalidraw/              # Excalidraw 绘图文件
    │   ├── Mathcraft/               # Mathcraft 函数图像缓存
    │   └── MathSvg/                 # 数学 SVG 图形
    └── 99-Templates-模版/           # 各类笔记模板
```

### 编号规则

- **C** = Category（知识大类）
- **CB** = Category Branch（知识分支）
- **PL** = Programming Language（编程语言）
- **MA** = Math（数学）
- **EN** = English（英语）
- **ES** = English Speaking（英语口语）
- **PY** = Python
- **TP** = Template（模板）
- **PJ** = Project（项目）
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

---

## 10. 相关文档

- [[OB001-UPDATE LOG]] — 初始搭建日志与踩坑记录

---

> **最后更新**：2026-06-13 | **维护者**：Jobin Wei
