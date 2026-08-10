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

Internal structure visualization with labeled parts or layers:
- Central subject: two isolated process boxes
- Parts or layers clearly shown: independent address spaces, IPC channels
- Labels with callout lines
- Exploded or cutaway view of the IPC communication channels between processes

## Style Guidelines

Hand-drawn educational infographic with macaron pastel color blocks on warm cream paper texture:
- Background: Warm cream (#F5F0E8) with subtle paper grain texture
- Macaron Blue: #A8D8EA for process boxes
- Macaron Mint: #B5E5CF for IPC channel area
- Macaron Lavender: #D5C6E0 for annotations
- Macaron Peach: #FFD5C2 for highlights
- Accent: Coral Red (#E8655A) for the "no direct access" warning
- Hand-drawn wavy connection lines and arrows with small text labels
- Simple stick-figure characters to humanize concepts
- Doodle decorations: small stars, underlines, sparkles
- Slight hand-drawn wobble on all lines and shapes
- Generous white space between zones

---

Generate the infographic based on the content below:

## Topic
进程间通信（IPC）概览 — Inter-Process Communication Overview

## Content
两个进程（进程 A 和进程 B）各自拥有独立的地址空间，不能直接互相访问内存。它们必须通过 IPC 通道（Queue、Pipe、共享内存）来通信。所有通信对象需要 pickle 序列化，传递的是副本而非引用。

- 左侧：进程 A — 独立的地址空间，data = [1]，GIL 独立，内存隔离
- 右侧：进程 B — 独立的地址空间，data = [2]，GIL 独立，内存隔离
- 中间大红色 ✕ 标记和虚线："不能直接访问"
- 下方 IPC 通信通道区域，列出三种方式：
  - Queue 队列（多生产者/多消费者）
  - Pipe 管道（点对点双工）
  - 共享内存 Value/Array（零复制）

Text labels (in zh):
- 标题：进程间通信（IPC）概览
- 副标题：Inter-Process Communication Overview
- 进程 A：独立的地址空间
- 进程 B：独立的地址空间
- 中间警告：✕ 不能直接访问
- IPC 通道标签：IPC 通信通道
- Queue 标注：Queue 队列 · 多生产者/多消费者
- Pipe 标注：Pipe 管道 · 点对点双工
- 共享内存标注：共享内存 · Value/Array (mmap)
- 底部注释：进程内存默认隔离 · pickle 序列化 · 传递副本而非引用
