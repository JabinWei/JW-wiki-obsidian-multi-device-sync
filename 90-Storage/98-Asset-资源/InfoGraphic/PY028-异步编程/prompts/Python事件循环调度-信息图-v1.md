Create a professional infographic following these specifications:

## Image Specifications
- **Type**: Infographic
- **Layout**: structural-breakdown
- **Style**: technical-schematic (Blueprint variant — white on deep blue, engineering grid, dimension lines)
- **Aspect Ratio**: 16:9
- **Language**: zh

## Style Guidelines
- Background: Deep blue (#1E3A5F) with engineering grid pattern
- Lines: White/cyan strokes with consistent weights, geometric precision
- Accents: Amber (#F59E0B) for await/suspension points, cyan for active execution
- Typography: Clean stencil/sans-serif, all-caps for key labels
- Include dimension lines, measurement annotations, and technical markers

## Content

### Title
asyncio 事件循环 — 单线程如何调度多个协程

### Subtitle
一个事件循环在多个 await 挂起点之间切换，单线程实现高并发（不是真并行）

### Center Top: 事件循环 Event Loop
- 青色边框，标注「Event Loop 单线程调度器」
- 内部：就绪任务队列（task queue），标注「就绪任务排队」

### 三个协程任务（横向排列）
- Task A：开始(绿色) → await sleep(3) 挂起(amber 沙漏) → 结束
- Task B：开始(绿色) → await sleep(1) 挂起(amber 沙漏) → 结束（早于 A）
- Task C：开始(绿色) → await 挂起(amber 沙漏) → 结束

### 关键标注
- await 挂起点用 amber 沙漏标注「挂起 / 让出控制权」
- 事件循环到各任务的切换箭头（cyan 虚线），标注「切换去跑下一个就绪任务」
- 时间轴标注：T=0 三个任务同时开始，T=1s 任务 B 结束，T=3s 任务 A/C 结束

### Bottom: Conclusion bar
「asyncio = 单线程 + 协作式调度：谁 await 谁让出，事件循环去跑下一个就绪任务」
