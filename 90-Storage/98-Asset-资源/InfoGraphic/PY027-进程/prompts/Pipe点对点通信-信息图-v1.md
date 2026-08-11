Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: structural-breakdown
- **Style**: hand-drawn-edu
- **Aspect Ratio**: 16:9
- **Language**: zh

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- Keep information concise, highlight keywords and core concepts
- Use ample whitespace for visual clarity
- Maintain clear visual hierarchy

## Text Requirements

- All text must match the specified style treatment
- Main titles should be prominent and readable
- Key concepts should be visually emphasized
- Labels should be clear and appropriately sized
- Use the specified language for all text content

## Layout Guidelines

Internal structure visualization with cross-section of Pipe communication:
- Central subject: OS anonymous pipe in the middle (Kernel Space)
- Left side: parent_conn in main process, right side: child_conn in child process
- Exploded view showing data flow through the pipe
- Arrows showing bidirectional send/recv

## Style Guidelines

Hand-drawn educational infographic with macaron pastel color blocks on warm cream paper texture:
- Background: Warm cream (#F5F0E8) with subtle paper grain texture
- Macaron Blue: #A8D8EA for main process box
- Macaron Mint: #B5E5CF for data bytes flowing through pipe
- Macaron Lavender: #D5C6E0 for child process box
- Macaron Peach: #FFD5C2 for the OS pipe boundary
- Accent: Coral Red (#E8655A) for key callout: "无后台线程"
- Hand-drawn wavy bi-directional arrows
- Simple stick figure characters representing parent and child processes
- Doodle decorations: small stars, sparkles
- Slight hand-drawn wobble on all lines and shapes

---

Generate the infographic based on the content below:

## Topic
Pipe 管道：点对点双向通信 — Pipe Point-to-Point Duplex Communication

## Content
Pipe() 返回一对 Connection 对象（parent_conn 和 child_conn），底层是操作系统提供的匿名管道（Anonymous Pipe）。数据从一端 send() 进去，另一端 recv() 出来，先进先出（FIFO）。

关键特性：
- 双向 FIFO 字节流，无后台线程
- 点对点：只有两个端点，无法多生产者/多消费者
- pickle 序列化 + recv() 端自动反序列化
- close() 是必须的终止信号（否则另一端 recv() 永不返回）
- 速度比 Queue 快（少一层缓冲 + 无锁开销）

创建方式：
- Pipe() 默认 duplex=True（双向）
- Pipe(duplex=False) 半双工

Text labels (in zh):
- 标题：Pipe 管道：点对点双向通信
- 副标题：Pipe — Point-to-Point Duplex Communication
- 左侧：主进程 Main Process · parent_conn
- 左侧方法：.send(obj) / .recv()
- 中间：OS 匿名管道 · Anonymous Pipe · Kernel Space
- 中间数据流：data_1 (bytes) → data_2 (bytes) → ... FIFO 字节流
- 右侧：子进程 Child Process · child_conn
- 右侧方法：.send(obj) / .recv()
- 代码区：parent_conn, child_conn = Pipe()  # duplex=True 双向
- 关键特性标注：双向 FIFO · 无后台线程 · 点对点 · close() 是必须的终止信号
- 速度对比：⚡ 比 Queue 快（无缓冲层 + 无锁开销）
