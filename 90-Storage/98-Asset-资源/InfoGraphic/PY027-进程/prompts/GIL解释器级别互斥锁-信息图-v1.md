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
- Accents: Amber (#F59E0B) for GIL locks and key callouts, cyan for process labels
- Typography: Clean stencil/sans-serif, all-caps for key labels
- Include dimension lines, measurement annotations, and technical markers

## Content

### Title
GIL 是解释器级别的互斥锁 — 多进程如何绕过 GIL

### Subtitle
每个 CPython 解释器实例拥有独立的 GIL，进程 A 和进程 B 各管各的锁，互不干扰

### Left Side: 进程 A
- OS 进程（独立内存空间）
- 内部：CPython 解释器实例 A
- GIL_A 互斥锁（amber 高亮标注"🔒 GIL_A"）
- 线程 1 持有 GIL 执行中（cyan 标注）
- 线程 2 等待 GIL（灰色/暗淡）
- 标注：占用 CPU 核心 0

### Right Side: 进程 B
- OS 进程（独立内存空间）
- 内部：CPython 解释器实例 B
- GIL_B 互斥锁（amber 高亮标注"🔒 GIL_B"）
- 线程 1 持有 GIL 执行中（cyan 标注）
- 线程 2 等待 GIL（灰色/暗淡）
- 标注：占用 CPU 核心 1

### Center: 关键标注
两个 GIL 完全隔离 — 不共享、不影响、各锁各的

### Top: 入口
multiprocessing.Process(target=fn) → fork() / spawn() → 创建两个独立进程

### Bottom: 结论
GIL 不是系统全局锁，每个进程 = 独立的 CPython 解释器 = 独立的 GIL → 多进程实现真正并行

## Text Labels (zh)
- 主标题：GIL 是解释器级别的互斥锁
- 进程 A / 进程 B
- CPython 解释器（独立实例）
- GIL_A / GIL_B
- 线程 1 执行中 / 线程 2 等待
- CPU 核心 0 / CPU 核心 1
- fork() / spawn()
- 结论：多进程 = 多解释器 = 多 GIL → 真正并行
