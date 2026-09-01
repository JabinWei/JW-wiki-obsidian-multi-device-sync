---
type: card
status: 已完成
aliases: [余弦定理, 余弦公式]
tags:
  - 数学
  - 几何
  - 三角形
created: 2026-08-28
updated: 2026-08-28
---

## 💡 核心概念

**余弦定理**是任意三角形中**边长与夹角**关系的基本定理，是勾股定理对任意三角形的推广，也是证明点积夹角公式的基础。

## 🔍 详细说明

### 公式

设三角形三边长为 $a, b, c$，$a$ 和 $b$ 的夹角为 $\theta$，则第三边 $c$ 满足：

$$
\boxed{c^2 = a^2 + b^2 - 2ab \cos\theta}
$$

![[MA-GE-001-cosine-theorem.svg]]

### 变形形式

知道三边求夹角，可以改写为：

$$
\cos\theta = \frac{a^2 + b^2 - c^2}{2ab}
$$

### 特殊情况：直角三角形

当 $\theta = 90^\circ$，$\cos\theta = 0$，余弦定理退化为**勾股定理**：

$$
c^2 = a^2 + b^2
$$

所以**勾股定理是余弦定理的特例**，余弦定理是勾股定理的推广。

## 📎 应用场景

1. **已知两边一夹角，求第三边**
2. **已知三边，求任意角的余弦/角度**
3. **线性代数**：证明点积的几何意义 $\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos\theta$
4. **解析几何**：计算两点距离、向量夹角

### 证明（向量法）

把两边看成从同一点出发的向量 $\mathbf{a}, \mathbf{b}$，第三边就是 $\mathbf{a} - \mathbf{b}$：

$$
\begin{aligned}
\|\mathbf{a} - \mathbf{b}\|^2 &= (\mathbf{a} - \mathbf{b}) \cdot (\mathbf{a} - \mathbf{b}) \\
&= \mathbf{a} \cdot \mathbf{a} + \mathbf{b} \cdot \mathbf{b} - 2\mathbf{a} \cdot \mathbf{b} \\
&= \|\mathbf{a}\|^2 + \|\mathbf{b}\|^2 - 2\|\mathbf{a}\| \|\mathbf{b}\| \cos\theta
\end{aligned}
$$

左边就是 $c^2$，所以 $c^2 = a^2 + b^2 - 2ab \cos\theta$，证毕。

## ⚡ 常见误区 / 边界

- ❌ 误区："余弦定理只适用于锐角三角形" → 事实：对锐角/直角/钝角三角形都成立，钝角的余弦为负，公式依然正确
- ❌ 误区："余弦定理只能解三角形" → 事实：它是连接边长和夹角的桥梁，在向量、解析几何、积分都有用

## 🔗 关联卡片

- [[MA-GE-002-勾股定理]]（特例）
- [[MA-GE-003-直角三角形三角函数]]
- [[LA003-点积与正交性]]（用余弦定理证明点积夹角公式）

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
