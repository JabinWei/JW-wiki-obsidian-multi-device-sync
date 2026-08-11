Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: binary-comparison
- **Style**: hand-drawn-edu
- **Aspect Ratio**: 16:9
- **Language**: zh

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- If content involves sensitive or copyrighted figures, create stylistically similar alternatives
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

Side-by-side comparison of two items or concepts.

### Structure
- Vertical divider splitting image in half
- Left side: Python (CPython) — GIL 串行执行
- Right side: Java / C++ / Go / Rust — 真正并行执行
- Mirrored layout for easy comparison
- Clear visual distinction between sides with contrasting colors
- VS symbol or divider decoration in the center

### Visual Elements
- Strong vertical dividing line or gradient
- Contrasting colors per side: left side warm/caution tones, right side cool/positive tones
- Matching element positions for comparison — same data points on both sides aligned horizontally
- VS symbol at center divider

### Text Placement
- Main title centered at top: "Python 多线程 vs Java/C++ — 执行模型对比"
- Side labels (Python (CPython) / Java / C++ / Go / Rust)
- Corresponding points aligned horizontally across the divider
- Summary/结论 at bottom

## Style Guidelines

Hand-drawn educational infographic with macaron pastel color blocks on warm cream paper texture.

### Color Palette
- Background: Warm cream (#F5F0E8) with subtle paper grain texture
- Primary text: Deep charcoal (#2D2D2D) for headlines, outlines
- Macaron Blue: #A8D8EA for cool-toned information zones
- Macaron Mint: #B5E5CF for growth/positive zones (right side)
- Macaron Lavender: #D5C6E0 for abstract/concept zones
- Macaron Peach: #FFD5C2 for warm-toned zones (left side)
- Accent: Coral Red (#E8655A) for key data, warnings, emphasis
- Muted annotations: Warm gray (#6B6B6B) for secondary labels

### Visual Elements
- Macaron pastel rounded cards as distinct information zones
- Hand-drawn wavy connection lines and arrows with small text labels
- Simple stick-figure characters and cartoon icons to humanize concepts
- Doodle decorations: small stars, underlines, spirals, sparkles
- Color fills don't completely fill outlines — preserve casual hand-drawn feel
- Dashed borders for secondary or contained zones
- Small icon doodles (lock, checkmark, lightning, lightbulb, car, road) to reinforce concepts
- Bold centered quote or takeaway at the bottom
- Slight hand-drawn wobble on all lines and shapes
- Include at least one simple cartoon character or stick figure
- Generous white space between zones — each zone should breathe
- Maximum 4 macaron colors per infographic

### Avoid
- Perfect geometric shapes or straight lines
- Photorealistic elements or stock illustration style
- Pure white backgrounds
- Flat vector icons or digital-precision graphics
- Overcrowded layouts — let zones breathe
- Corporate or clinical aesthetic

---

Generate the infographic based on the content below:

## 标题
Python 多线程 vs Java/C++ — 执行模型对比

## 左侧内容：Python (CPython) — GIL 串行执行

左上方放一个 CPython 解释器图标（带锁的盒子），标"GIL 互斥锁 🔒"

三个对比维度，从左到右排列：
1. 调度模型：多线程串行执行字节码 — 线程排队轮流获取 GIL
2. CPU 利用率：单核 — 8 核 CPU 计算任务只能用 1 核
3. 形象比喻：一条车道上的多辆车 🚗🚗🚗 — 车再多同一时刻只有一辆在跑

左下结论卡片（peach 色块）：
❌ 计算密集型：多线程无加速，线程切换开销反让总耗时更长
✅ IO 密集型：IO 等待时 GIL 自动释放

## 右侧内容：Java / C++ / Go / Rust — 真正并行

右上方放操作系统线程调度器图标（多条箭头指向不同方块），标"OS 线程调度器"

三个对比维度，与左侧对齐：
1. 调度模型：多线程并行执行 — 每个线程独立跑在不同 CPU 核心上
2. CPU 利用率：多核 — 4 线程 × 4 核 = 真正同时执行
3. 形象比喻：多车道高速 🚗 | 🚗 | 🚗 — 每辆车有自己的车道

右下结论卡片（mint 色块）：
✅ 计算密集型：接近 N 倍加速
✅ IO 密集型：IO 等待时 OS 挂起线程，其他线程自然调度

## 底部共性区域（blue 色块）
💡 IO 密集型任务：两者都受益
Python：IO 等待时 GIL 释放 → 其他线程获取 GIL 继续跑
Java/C++：IO 等待时线程被 OS 挂起 → 其他线程自然调度到 CPU

## 底部核心结论（加粗居中）
核心差异不在 API，在「执行模型」— Python 多线程串行执行字节码，Java/C++/Go/Rust 多线程并行执行

## Text labels (in zh):

| Label | 用途 |
|-------|------|
| Python 多线程 vs Java/C++ | 主标题 |
| Python (CPython) | 左侧栏目标题 |
| Java / C++ / Go / Rust | 右侧栏目标题 |
| GIL 互斥锁 | 左侧核心机制标签 |
| 串行执行 | 左侧调度模型标签 |
| 真并行执行 | 右侧调度模型标签 |
| 多车道高速 | 右侧比喻标签 |
| 单车道排队 | 左侧比喻标签 |
| ❌ 计算密集型无加速 | 左侧结论 |
| ✅ 接近 N 倍加速 | 右侧结论 |
| ✅ IO 密集型都受益 | 底部结论 |
