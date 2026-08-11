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

Internal structure visualization with exploded/layered view of shared memory:
- Top layer: Physical Memory with Value('i', 0) cell
- Middle: mmap mapping arrows pointing down to both processes
- Bottom layer: Process A (left) and Process B (right) virtual address spaces
- Both processes connect via mmap to the same physical memory
- Warning box at bottom showing race condition scenario

## Style Guidelines

Hand-drawn educational infographic with macaron pastel color blocks on warm cream paper texture:
- Background: Warm cream (#F5F0E8) with subtle paper grain texture
- Macaron Blue: #A8D8EA for Process A box
- Macaron Mint: #B5E5CF for the shared physical memory with "零复制" emphasis
- Macaron Lavender: #D5C6E0 for Process B box
- Macaron Peach: #FFD5C2 for mmap mapping arrows
- Accent: Coral Red (#E8655A) for Lock warning and race condition
- Hand-drawn wavy mmap connection lines
- Simple stick figures representing the two processes reading/writing to the same memory
- Cartoon lock icon emphasizing "需要Lock保护"
- Doodle decorations: small stars, sparkles
- Slight hand-drawn wobble on all lines and shapes

---

Generate the infographic based on the content below:

## Topic
共享内存：mmap 零复制原理 — Shared Memory Zero-Copy via mmap

## Content
Value 和 Array 通过 mmap（内存映射）实现：操作系统将同一块物理内存分别映射到进程 A 和进程 B 的虚拟地址空间中。

关键特性：
- 零复制：进程 A 写一个值，进程 B 立刻能看到——没有序列化，没有复制
- 直接读写：v.value = 42 或 x = v.value，无需 pickle
- ctypes 类型：'i'=int(4B), 'd'=double(8B), 'f'=float(4B)
- 必须用 Lock 保护复合操作

竞态条件：v.value += 1 看起来是一步，实际是 LOAD → ADD → STORE 三步。如果两个进程同时执行，可能出现两次+1只增加一次的结果。必须用 with val.get_lock() 保护。

Text labels (in zh):
- 标题：共享内存：mmap 零复制原理
- 副标题：Shared Memory — Zero-Copy via mmap
- 物理内存标签：物理内存 Physical Memory · Value('i', 0) · ctypes 类型
- mmap 映射线标注：mmap 映射 · 共享同一物理页
- 进程 A：进程 A 虚拟地址空间 · v.value = 42 · 直接读写无需 pickle
- 进程 B：进程 B 虚拟地址空间 · v.value += 1 · 直接读写无需 pickle
- 绿色标注：✅ 零复制 · 无需 pickle · 直接读写
- 警告框：⚠️ 竞态条件：LOAD→ADD→STORE 非原子操作 · 必须用 Lock 保护！
- 竞态示例：A读v(0)→B读v(0)→A写v(1)→B写v(1) 结果=1（期望=2）
