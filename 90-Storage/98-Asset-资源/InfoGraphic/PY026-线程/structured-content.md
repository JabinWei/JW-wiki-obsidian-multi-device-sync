# Structured Content: Python vs Java/C++ 多线程执行模型对比

## 标题
Python 多线程 vs Java/C++ — 执行模型对比

## 学习目标
理解 Python (CPython) GIL 串行执行 vs Java/C++/Go/Rust 真正并行执行的本质差异

## 左侧：Python (CPython) — GIL 串行执行

- **核心概念**：CPython 解释器中有一个全局互斥锁 GIL，同一时刻只有一个线程执行 Python 字节码
- **调度模型**：多线程串行执行字节码，线程排队轮流获取 GIL
- **CPU 利用率**：单核（GIL 限制），8 核 CPU 计算任务只能用 1 核
- **比喻**：一条车道上的多辆车，车再多同一时刻只有一辆在跑
- **计算密集型**：❌ 多线程无加速，线程切换开销反让总耗时更长
- **IO 密集型**：✅ IO 等待时 GIL 自动释放，其他线程获取 GIL 继续跑

## 右侧：Java / C++ / Go / Rust — 真正并行

- **核心概念**：操作系统线程调度器将线程分配到不同 CPU 核心，真正同时执行
- **调度模型**：多线程并行执行，每个线程独立跑在不同核心上
- **CPU 利用率**：多核，4 线程 × 4 核 = 真正同时执行
- **比喻**：多车道高速，每辆车有自己的车道，真正同时行驶
- **计算密集型**：✅ 接近 N 倍加速
- **IO 密集型**：✅ IO 等待时操作系统挂起线程，其他线程自然调度到 CPU

## 底部共性
IO 密集型任务两者都受益 — Python IO 等待时释放 GIL，Java/C++ IO 等待时 OS 挂起线程

## 核心结论
核心差异不在 API，在「执行模型」— Python 多线程串行执行字节码，Java/C++ 多线程并行执行

## Text Labels (zh)

| Label | Position |
|-------|----------|
| Python 多线程 vs Java/C++ | 顶部标题 |
| Python (CPython) | 左侧标题 |
| Java / C++ / Go / Rust | 右侧标题 |
| GIL 互斥锁 / 串行执行 | 左侧标签 |
| 真并行 / 多核同时执行 | 右侧标签 |
| 单车道 / 多辆车排队 | 左侧比喻 |
| 多车道高速 / 并行行驶 | 右侧比喻 |
| ❌ 计算密集型无加速 | 左侧结论 |
| ✅ 接近 N 倍加速 | 右侧结论 |
| IO 密集型两者都受益 | 底部共性 |

## Design Instructions
- Layout: binary-comparison (A vs B)
- Style: hand-drawn-edu (macaron pastels, hand-drawn wobble, stick figures)
- 左右对比 Python 的 GIL 瓶颈 vs Java 的真正并行
- 用 stick figure 或简单卡通角色增加亲和力
- 用括号引号突出核心结论
