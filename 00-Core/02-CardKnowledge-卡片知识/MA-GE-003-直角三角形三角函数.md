---
type: card
status: 已完成
aliases: [三角函数, 直角三角形三角函数, 投影长度]
tags:
  - 数学
  - 几何
  - 三角函数
created: 2026-08-28
updated: 2026-09-07
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

### 特殊角速查表

两条基本直角三角形的三边比（可由勾股定理验证）：

| 类型 | 角度 | 三边比（短边 : 中边 : 斜边） |
|------|------|------------------------------|
| 等腰直角 | $45^\circ$-$45^\circ$-$90^\circ$ | $1 : 1 : \sqrt{2}$ |
| 半等边 | $30^\circ$-$60^\circ$-$90^\circ$ | $1 : \sqrt{3} : 2$ |

由三边比即得常用角度的三角函数值：

| $\theta$ | 弧度 | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|----------|------|--------------|--------------|--------------|
| $0^\circ$ | $0$ | $0$ | $1$ | $0$ |
| $30^\circ$ | $\dfrac{\pi}{6}$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{3}}{3}$ |
| $45^\circ$ | $\dfrac{\pi}{4}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $1$ |
| $60^\circ$ | $\dfrac{\pi}{3}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}$ | $\sqrt{3}$ |
| $90^\circ$ | $\dfrac{\pi}{2}$ | $1$ | $0$ | 不存在 |

**记忆法**：$\sin$ 值按 $0^\circ \to 90^\circ$ 依次为 $\dfrac{\sqrt{0}}{2}, \dfrac{\sqrt{1}}{2}, \dfrac{\sqrt{2}}{2}, \dfrac{\sqrt{3}}{2}, \dfrac{\sqrt{4}}{2}$；$\cos$ 是同一序列**倒着读**；$\tan\theta = \dfrac{\sin\theta}{\cos\theta}$。

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

**平方关系**：
$$
\boxed{\sin^2\theta + \cos^2\theta = 1}, \qquad
1 + \tan^2\theta = \sec^2\theta, \qquad
1 + \cot^2\theta = \csc^2\theta
$$

**倒数关系**：
$$
\cot\theta = \frac{1}{\tan\theta}, \quad
\sec\theta = \frac{1}{\cos\theta}, \quad
\csc\theta = \frac{1}{\sin\theta}
$$

**商数关系**（六个函数间的核心桥梁）：
$$
\tan\theta = \frac{\sin\theta}{\cos\theta}, \quad
\cot\theta = \frac{\cos\theta}{\sin\theta}
$$

### 诱导公式（任意角 → 锐角）

先用周期化小、再用奇偶性处理负角：
$$
\sin(\theta + 2k\pi) = \sin\theta, \quad
\cos(\theta + 2k\pi) = \cos\theta, \quad
\tan(\theta + k\pi) = \tan\theta
$$
$$
\sin(-\theta) = -\sin\theta, \quad
\cos(-\theta) = \cos\theta, \quad
\tan(-\theta) = -\tan\theta
$$

**参考角法**（求任意角函数值三步）：
1. 用周期把 $\theta$ 化到 $[0,\, 2\pi)$；
2. 求参考角 $\theta'$：终边与 $x$ 轴所夹的锐角（$0 \le \theta' \le \frac{\pi}{2}$）；
3. 函数值的大小取 $\theta'$ 的函数值，**正负号由原角所在象限**决定（见上文符号表）。

常用诱导公式（口诀：**奇变偶不变，符号看象限**，设 $\alpha$ 为锐角）：

| 角度 | $\sin$ | $\cos$ | $\tan$ |
|------|--------|--------|--------|
| $-\alpha$ | $-\sin\alpha$ | $\cos\alpha$ | $-\tan\alpha$ |
| $\pi - \alpha$ | $\sin\alpha$ | $-\cos\alpha$ | $-\tan\alpha$ |
| $\pi + \alpha$ | $-\sin\alpha$ | $-\cos\alpha$ | $\tan\alpha$ |
| $2\pi - \alpha$ | $-\sin\alpha$ | $\cos\alpha$ | $-\tan\alpha$ |
| $\dfrac{\pi}{2} - \alpha$ | $\cos\alpha$ | $\sin\alpha$ | $\cot\alpha$ |
| $\dfrac{\pi}{2} + \alpha$ | $\cos\alpha$ | $-\sin\alpha$ | $-\cot\alpha$ |

### 和角与差角公式

$$
\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta
$$
$$
\boxed{\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta}
$$
$$
\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}
$$

### 二倍角公式

$$
\sin 2\theta = 2\sin\theta\cos\theta
$$
$$
\boxed{\cos 2\theta = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta}
$$
$$
\tan 2\theta = \frac{2\tan\theta}{1 - \tan^2\theta}
$$

**降幂公式**（二倍角的逆用）：
$$
\cos^2\theta = \frac{1 + \cos 2\theta}{2}, \qquad
\sin^2\theta = \frac{1 - \cos 2\theta}{2}
$$

### 半角公式

$$
\sin\frac{\theta}{2} = \pm\sqrt{\frac{1 - \cos\theta}{2}}, \qquad
\cos\frac{\theta}{2} = \pm\sqrt{\frac{1 + \cos\theta}{2}}
$$
$$
\tan\frac{\theta}{2} = \frac{1 - \cos\theta}{\sin\theta} = \frac{\sin\theta}{1 + \cos\theta}
$$

（「$\pm$」由 $\frac{\theta}{2}$ 所在象限决定）

### 积化和差与和差化积

**积化和差**（积 ⇄ 和差，常用于积分计算）：
$$
\sin\alpha\cos\beta = \frac{\sin(\alpha + \beta) + \sin(\alpha - \beta)}{2}, \quad
\cos\alpha\cos\beta = \frac{\cos(\alpha + \beta) + \cos(\alpha - \beta)}{2}
$$
$$
\sin\alpha\sin\beta = \frac{\cos(\alpha - \beta) - \cos(\alpha + \beta)}{2}, \quad
\cos\alpha\sin\beta = \frac{\sin(\alpha + \beta) - \sin(\alpha - \beta)}{2}
$$

**和差化积**：
$$
\sin\alpha \pm \sin\beta = 2\sin\frac{\alpha \pm \beta}{2}\cos\frac{\alpha \mp \beta}{2}
$$
$$
\cos\alpha + \cos\beta = 2\cos\frac{\alpha + \beta}{2}\cos\frac{\alpha - \beta}{2}, \qquad
\cos\alpha - \cos\beta = -2\sin\frac{\alpha + \beta}{2}\sin\frac{\alpha - \beta}{2}
$$

> 🔑 记法：以上公式中**只需牢固记忆和角公式**，二倍角、降幂、半角、和差化积均可由它（配合 $\sin^2 + \cos^2 = 1$）现场推出。

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
5. 任意角求值、三角恒等变换与公式化简（诱导、和差角、倍角）

## ⚡ 常见误区 / 边界

- ✔️ 这个定义只对**锐角**（直角三角形内角）直接成立，任意角度用单位圆推广
- ✔️ $\cos\theta$ 可正可负：正 = 投影同向，负 = 投影反向，零 = 正交
- ✔️ 斜三角形不用这个定义直接算边长，要用余弦定理
- ✔️ 表中 $90^\circ$ 的 $\tan$ 不存在：$\tan\theta = \sin\theta/\cos\theta$，此处分母为零
- ✔️ 诱导公式求值结果的正、负取决于原角所在象限，先定大小再定符号

## 🔗 关联卡片

- [[MA-GE-001-余弦定理]]
- [[MA-GE-002-勾股定理]]
- [[MA-AL-001-向量投影长度]]
- [[MA-AL-002-向量夹角]] — 由点积几何定义反解 $\theta$
- [[LA003-点积与正交性]] — 点积几何意义

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
