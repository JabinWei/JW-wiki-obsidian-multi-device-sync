---
layout: comparison-matrix
style: hand-drawn-edu
aspect: 16:9
language: zh
---

# Infographic: Python 多进程编程 (multiprocessing)

## Global Style
Warm cream paper (#F5F0E8) background with subtle grain. All lines have slight hand-drawn wobble — no perfect geometry. Macaron pastel rounded cards as information zones. Simple stick-figure Python snake characters. Doodle decorations throughout.

## Title (Top, bold hand-lettered)
🐍 Python 的分身术 — 多进程编程
Subtitle: 绕过 GIL，真正并行

## Top Section — Core Concept (Macaron Lavender card)
**为什么需要多进程？** GIL 让多线程计算任务串行化。每个进程有独立的 Python 解释器和 GIL → 真正多核并行。
Stick figure snake splitting into four identical snakes, each working in its own room.

## Main Section — 3-Column Comparison Matrix

**Column 1 (Macaron Blue #A8D8EA): 多进程 vs 多线程**
- 🟢 多进程：独立内存，IPC 通信，CPU 密集型 ✅
- 🟡 多线程：共享内存，GIL 限制，IO 密集型 ✅
- 创建开销：进程大 / 线程小

**Column 2 (Macaron Mint #B5E5CF): Pool vs ProcessPoolExecutor**
- Pool：map/apply_async/imap，回调方便
- ProcessPoolExecutor：submit/as_completed，异常处理更好
- 新项目优先 ProcessPoolExecutor

**Column 3 (Macaron Peach #FFD5C2): Queue vs Pipe vs 共享内存**
- Queue：多生产者/多消费者，任务分发首选
- Pipe：点对点双工，两进程直连
- Value/Array：共享内存，配合 Lock 使用

## Bottom Section — Key Methods Cheatsheet (Macaron Lavender)
| start() → 启动 | join() → 等待 | terminate() → 强制终止 | is_alive() → 检查存活 |
Pool: map() / apply_async() / close() / join()

## Right Side — IPC Flow Diagram (wavy arrows)
Producer → Queue.put() → Queue → Queue.get() → Consumer
Dad pipe → conn.send() → Pipe → conn.recv() → Child pipe

## Bottom Takeaway (bold, centered, Coral Red)
"CPU 密集用多进程，IO 密集用多线程。if __name__ == '__main__' 千万别忘！"
