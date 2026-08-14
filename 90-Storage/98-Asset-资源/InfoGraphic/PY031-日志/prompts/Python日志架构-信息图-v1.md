Create a professional infographic following these specifications:

## Image Specifications
- **Type**: Infographic
- **Layout**: hierarchical-layers
- **Style**: chalkboard (chalk on dark board, educational whiteboard feel, hand lettering)
- **Aspect Ratio**: 16:9
- **Language**: zh

## Style Guidelines
- Background: Dark green-black chalkboard (#2F3B2F)
- Lines: Chalk white/cream strokes, slightly rough hand-drawn texture
- Accents: chalk yellow, chalk cyan, chalk pink for level labels
- Typography: Hand-lettered chalk style; code snippets in a chalk monospace feel
- Layered stack + flow, with subtle chalk dust texture

## Content

### Title
logging — 5 级日志 + 三件套

### Subtitle
级别是「门槛」（设定 INFO 会显示 INFO 及以上），logger/handler/formatter 各司其职

### 左侧：日志级别（从低到高的阶梯）
- CRITICAL（致命，程序可能崩溃）
- ERROR（错误，功能失败）
- WARNING（警告，还能跑）
- INFO（正常运行信息）
- DEBUG（调试信息）
- 标注：级别越高越关键，设定门槛后「门槛及以上」都显示

### 右侧：三件套分工（自上而下）
- logger（日志器）—— 产生日志的入口，决定「要不要记录」
- handler（处理器）—— 日志发到哪：控制台 / 文件 / 邮件
- formatter（格式化器）—— 日志长什么样：时间、级别、消息

### 连接线
- 代码 → logger →（多个）handler → 各自 formatter
- 示例：一条日志同时写控制台 + 写文件

### Bottom: Conclusion bar
「print 是临时调试，logging 是长期记录 —— 分级、落盘、可开关」
