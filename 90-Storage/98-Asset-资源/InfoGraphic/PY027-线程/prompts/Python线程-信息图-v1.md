---
layout: structural-breakdown
style: hand-drawn-edu
aspect: 16:9
language: zh
---

# Infographic: Python 多线程编程 (threading)

## Global Style
Warm cream paper (#F5F0E8) background with subtle grain. All lines have slight hand-drawn wobble — no perfect geometry. Macaron pastel rounded cards as information zones. Simple stick-figure Python snake character with multiple arms. Doodle decorations throughout.

## Title (Top, bold hand-lettered)
🐍 Python 的千手观音 — 多线程编程
Subtitle: 共享内存、GIL 限制、IO 并发利器

## Top Left — GIL 机制 (Macaron Lavender #D5C6E0 card)
**GIL（全局解释器锁）**：同一时刻只有一个线程执行 Python 字节码。
- 计算密集型：多线程无效（甚至更慢）
- IO 密集型：IO 等待时释放 GIL → 多线程有效 ✅
- Stick figure snake with multiple arms, only ONE arm holds a glowing golden pen (GIL)

## Main Section — Structural Breakdown: 三大核心机制

**Section 1 (Macaron Blue #A8D8EA): 线程创建与生命周期**
- Thread(target=func, args=(...)) → start() → join()
- daemon=True：主线程退出时自动被杀（后台心跳、日志刷新）
- 子类化 Thread：重写 run() 方法
- Stick figure launching multiple mini-snakes

**Section 2 (Macaron Mint #B5E5CF): 竞态条件与 Lock**
- counter += 1 不是原子操作 → 多线程同时读写 = 结果不可预测
- Lock：同一时刻只有一个线程进入临界区
- RLock：可重入锁，同一线程可多次 acquire
- ⚠️ Lock 不释放 = 死锁
- Lock icon with shield, stick figures queuing

**Section 3 (Macaron Peach #FFD5C2): Queue 线程安全队列**
- queue.Queue()：内置线程安全，生产者-消费者模式的黄金标准
- put() 放入 / get() 取出（空则阻塞） / task_done() 标记完成
- ✅ 优先用 Queue，不要手动 Lock + list
- Conveyor belt doodle: Producer → Queue → Consumer

## Bottom Section — ThreadPoolExecutor (Macaron Lavender card)
- with ThreadPoolExecutor(max_workers=3) as executor:
- executor.submit() + as_completed()：先完成先处理
- executor.map()：保持顺序
- 与 ProcessPoolExecutor API 完全统一

## Bottom Takeaway (bold, centered, Coral Red)
"IO 密集用多线程，计算密集用多进程。共享数据加 Lock，线程通信用 Queue。"
