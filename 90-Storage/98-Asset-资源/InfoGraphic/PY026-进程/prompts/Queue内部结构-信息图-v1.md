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

Internal structure visualization with exploded view of Queue's internal components:
- Central subject: multiprocessing.Queue box with cutaway view
- Parts separated outward showing three internal components
- Labels with callout lines connecting each part
- Data flow arrows showing put() → buffer → get() path

## Style Guidelines

Hand-drawn educational infographic with macaron pastel color blocks on warm cream paper texture:
- Background: Warm cream (#F5F0E8) with subtle paper grain texture
- Macaron Blue: #A8D8EA for the Queue outer boundary
- Macaron Mint: #B5E5CF for the internal buffer
- Macaron Lavender: #D5C6E0 for Feeder Thread
- Macaron Peach: #FFD5C2 for Pipe and Lock components
- Accent: Coral Red (#E8655A) for Lock emphasis
- Hand-drawn wavy connection lines and arrows
- Simple cartoon icons: clipboard for buffer, lock icon, pipe/tube icon
- Doodle decorations: small stars, sparkles
- Slight hand-drawn wobble on all lines and shapes
- Generous white space between zones

---

Generate the infographic based on the content below:

## Topic
multiprocessing.Queue 内部结构 — Queue Internal Architecture

## Content
Queue 的底层不是一个简单的列表——它由三部分组成：内部缓冲区（deque）、Pipe（管道）、Lock（互斥锁）和一个 Feeder Thread（后台线程）。

数据流：q.put(item) → pickle 序列化 → 内部缓冲区 → Feeder Thread 从缓冲区取数据 → 写入 Pipe → 另一端 q.get() 读取 → pickle 反序列化

三个子组件：
- Pipe 管道：负责二进制数据传输
- Lock 互斥锁：保证 put/get 的线程安全
- Feeder Thread：后台线程，从缓冲区取数据 → pickle 序列化 → 写入 Pipe

底部提示 sentinel 终止模式：生产者发送 None → 消费者收到后 break

Text labels (in zh):
- 标题：multiprocessing.Queue 内部结构
- 副标题：Queue Internal Architecture
- 外部接口左：q.put(item) · 放入数据 · pickle 序列化
- 外部接口右：q.get() · 取出数据 · pickle 反序列化
- Queue 边界标签：multiprocessing.Queue
- 缓冲区：内部缓冲区（deque）· thread-safe 双端队列
- Pipe：Pipe 管道 · 二进制数据传输
- Lock：Lock 互斥锁 · 保证线程安全
- Feeder Thread：Feeder Thread 后台线程 · 取数据→序列化→写管道
- 底部提示：💡 终止模式：生产者 → q.put(None) → 消费者收到 None → break
