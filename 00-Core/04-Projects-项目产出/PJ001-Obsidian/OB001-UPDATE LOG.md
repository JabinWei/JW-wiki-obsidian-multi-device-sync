---
type: project
status: 已完成
tags: [obsidian, 项目产出]
created: 2026-06-13
updated: 2026-06-13
---

### 多端同步（这里使用 github）

1. 在 github 上面新建一个用于存放 obsidian 笔记的仓库。
2. 直接可以使用 git 命令行来初始化本地文件夹仓库。

### 在 obsidian 上建立图床

1. 首先从 github 上面搜索 Picgo 软件进行下载。
2. 在 obsidian 的插件市场中找到 image auto upload 插件，安装并启用。
3. 然后在 picgo 按照如下配置已经申请的 oss 存储桶资源。
![image.png](https://picgo-storage-typora.oss-cn-shanghai.aliyuncs.com/picgo-settings.png)

### 在 obsidian 上面可以自行绘制流程图

1. 在插件仓库中找到 Excalidraw 插件，安装并启用

### 在 obsidian 上支持绘制数学函数图像

1. 找到 `https://github.com/AlbusGuo/obsidian-mathcraft` 地址。
2. 搜索 BRAT 插件安装启用。
3. 打开 BRAT 插件设置面板，找到 `Add Plugins` 按钮。
![image.png](https://picgo-storage-typora.oss-cn-shanghai.aliyuncs.com/BART-settings.png)
4. 按照界面填写对应的项目地址。
![image.png|661](https://picgo-storage-typora.oss-cn-shanghai.aliyuncs.com/mathcraft-plugin-settings.png)
5. 再点击 `Add plugin` 即可成功添加 mathcraft 插件。

### 如何在 Obsidian 中接入 CC（Claude Code）

1. 在终端使用命令 `npm install -g @anthropic-ai/claude-code`，前提是已经完成 `node` 以及 `git` 的安装，mac 用户可以选择使用 homebrew 安装 `node` 以及 `git`。
2. 安装完成可以在终端尝试执行 `claude --version`，看一下是否安装成功。
3. 安装 `CC Switch` 软件（推荐），当然也可以直接在终端当中直接执行 `claude` 命令启动 `claude`。`CC Switch` 地址 `https://github.com/farion1231/cc-switch`。（因为 Claude Code 暂时国内不支持使用，故通过 `CC Switch` 软件代理连接）
4. 在 CC Switch 软件里面配置 
	+ API地址：`https://api.deepseek.com`
	- API Key：你刚才复制的那个 `sk-xxx`
	- 模型名称：`deepseek-chat`
![image.png](https://picgo-storage-typora.oss-cn-shanghai.aliyuncs.com/obsidian-project-update.png)
5. 然后通过 BRAT 插件安装 Claudian 插件（地址：`https://github.com/YishenTu/claudian`）连接本地 Claude Code 模型。
6. 还可以安装 Termy 插件 `https://github.com/ZyphrZero/Termy` 在终端执行 claude。
注意：
+ 如果在使用 Termy 插件时报错无法识别到 claude 命令。
	+ 我用的方法是现在电脑终端使用 `which claude` 找到对应的路径。然后找到 `~/.zshrc` 文件，在里面添加 `export PATH="$HOME/.npm-global/bin:/opt/homebrew/bin:$PATH"`。
	+ 然后重启 `source ~/.zshrc` 使配置生效。
+ 如果报错 `Error: claude native binary not installed.` 处理方式：
```
npm cache clean --force 
npm uninstall -g @anthropic-ai/claude-code 
npm install -g --include=optional @anthropic-ai/claude-code
```