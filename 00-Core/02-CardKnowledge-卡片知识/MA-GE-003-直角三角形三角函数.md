---
type: card
status: 已完成
aliases: [三角函数, 直角三角形三角函数, 投影长度]
tags:
  - 数学
  - 几何
  - 三角函数
created: 2026-08-28
updated: 2026-08-28
---

## 💡 核心概念

在直角三角形中，**所有三角函数都定义为边长之比**，正弦、余弦、正切、余切、正割、余割都是对边、邻边、斜边的比值。余弦定义直接给出了投影长度公式，是线性代数向量投影的几何基础。

## 🔍 详细说明

### 基本定义（直角三角形，$\angle C = 90^\circ$）

![[MA-GE-003-right-triangle-trig.svg]]

设 $\angle A = \theta$，边长：
- 斜边 $AB = c$
- $\theta$ 的对边 $BC = a$
- $\theta$ 的邻边 $AC = b$

六个三角函数定义：

| 函数 | 定义（边长比） | 简化 | 值域 |
|------|----------------|------|------|
| **正弦** | $\sin\theta = \dfrac{\text{对边}}{\text{斜边}}$ | $\boxed{\sin\theta = \dfrac{a}{c}}$ | $[-1, 1]$ |
| **余弦** | $\cos\theta = \dfrac{\text{邻边}}{\text{斜边}}$ | $\boxed{\cos\theta = \dfrac{b}{c}}$ | $[-1, 1]$ |
| **正切** | $\tan\theta = \dfrac{\text{对边}}{\text{邻边}}$ | $\boxed{\tan\theta = \dfrac{a}{b}}$ | $\mathbb{R}$ (除 $\frac{\pi}{2}+k\pi$) |
| **余切** | $\cot\theta = \dfrac{\text{邻边}}{\text{对边}}$ | $\boxed{\cot\theta = \dfrac{b}{a}}$ | $\mathbb{R}$ (除 $k\pi$) |
| **正割** | $\sec\theta = \dfrac{\text{斜边}}{\text{邻边}}$ | $\boxed{\sec\theta = \dfrac{c}{b}}$ | $(-\infty, -1] \cup [1, +\infty)$ |
| **余割** | $\csc\theta = \dfrac{\text{斜边}}{\text{对边}}$ | $\boxed{\csc\theta = \dfrac{c}{a}}$ | $(-\infty, -1] \cup [1, +\infty)$ |

### 核心结论：投影长度

由余弦定义，斜边在邻边方向上的**投影长度**就是邻边长度：

$$
\boxed{b = c \cdot \cos\theta}
$$

这就是向量投影长度公式 $\text{投影长度} = \|\mathbf{v}\| \cos\theta$ 的几何来源。

### 推广到任意夹角（单位圆定义）

对于任意角度 $\theta$，放在单位圆上定义：
- 单位圆半径 $= 1$，圆心在原点
- 终边与 $x$ 轴夹角 $\theta$
- 终边与单位圆交点坐标 $(x, y)$
- 定义：$\cos\theta = x$, $\sin\theta = y$

符号规律：

| 象限 | $\cos\theta$ | $\sin\theta$ |
|--------|-------------|-------------|
| 第一象限 | $+$ | $+$ |
| 第二象限 | $-$ | $+$ |
| 第三象限 | $-$ | $-$ |
| 第四象限 | $+$ | $-$ |

### 基本恒等式

最常用的平方关系：
$$
\boxed{\sin^2\theta + \cos^2\theta = 1}
$$

倒数关系：
$$
\tan\theta = \frac{\sin\theta}{\cos\theta}, \quad \cot\theta = \frac{1}{\tan\theta}, \quad \sec\theta = \frac{1}{\cos\theta}, \quad \csc\theta = \frac{1}{\sin\theta}
$$

### 推广到向量投影

向量 $\mathbf{v}$ 在方向 $\mathbf{n}$ 上的投影长度：
$$
\text{投影长度} = \|\mathbf{v}\| \cos\theta = \frac{\mathbf{n} \cdot \mathbf{v}}{\|\mathbf{n}\|}
$$

完整推导见 [[MA-AL-001-向量投影长度]]。

## 📎 应用场景

1. 向量投影长度公式基础（线性代数）
2. 点积几何意义 $\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos\theta$
3. 余弦定理证明依赖余弦定义
4. 几何计算、物理受力分析、工程测量

## ⚡ 常见误区 / 边界

- ✔️ 这个定义只对**锐角**（直角三角形内角）直接成立，任意角度用单位圆推广
- ✔️ $\cos\theta$ 可正可负：正 = 投影同向，负 = 投影反向，零 = 正交
- ✔️ 斜三角形不用这个定义直接算边长，要用余弦定理

## 🔗 关联卡片

- [[MA-GE-001-余弦定理]]
- [[MA-GE-002-勾股定理]]
- [[MA-AL-001-向量投影长度]]
- [[LA003-点积与正交性]] — 点积几何意义

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
