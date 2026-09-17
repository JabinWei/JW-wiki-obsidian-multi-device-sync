---
type: card
status: 已完成
aliases: [余弦定理, 余弦公式]
tags:
  - 数学
  - 几何
  - 三角形
created: 2026-08-28
updated: 2026-09-09
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

> 📐 $\theta$ 标注在顶点 $C$ 处，即边 $a$（向量 $\overrightarrow{CB}$）与边 $b$（向量 $\overrightarrow{CA}$）的夹角；第三边 $c$ 与 $\theta$ **相对**，所以 $c^2 = a^2 + b^2 - 2ab \cos\theta$。把边 $a, b$ 看成从 $C$ 出发的两个向量，第三边就是 $\mathbf{a} - \mathbf{b}$。

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

## 📐 证明

> 💡 余弦定理有多种证法。**证法一、证法二只用勾股定理，完全不碰点积**——它们说明余弦定理是**独立成立**的几何事实，没有循环论证。证法三用点积，适合学过点积之后作为"另一种验证"，不用作主要证明。

### 证法一：坐标法（只用勾股定理）

把 $C$ 放在原点，让边 $b$（$CA$）沿 $x$ 轴：

$$
C = (0, 0), \quad A = (b, 0), \quad B = (a\cos\theta,\ a\sin\theta)
$$

$B$ 的坐标由三角函数在直角三角形中的定义给出（$CB = a$，与 $x$ 轴夹角为 $\theta$）。于是第三边 $c = |AB|$：

$$
\begin{aligned}
c^2 &= (a\cos\theta - b)^2 + (a\sin\theta)^2 \\
&= a^2\cos^2\theta - 2ab\cos\theta + b^2 + a^2\sin^2\theta \\
&= a^2(\underbrace{\cos^2\theta + \sin^2\theta}_{=1}) + b^2 - 2ab\cos\theta \\
&= a^2 + b^2 - 2ab\cos\theta
\end{aligned}
$$

只用了勾股定理（两点距离公式）和 $\sin^2\theta + \cos^2\theta = 1$，**没有用到点积**。

### 证法二：作高线（经典几何证法）

以角 $A$ 为例（边 $b, c$ 夹着角 $A$，$a$ 是它的对边），过 $C$ 向 $AB$ 作垂线，垂足为 $D$，三角形被分成两个直角三角形：

![[MA-GE-001-altitude-proof.svg]]

- 直角三角形 $ACD$：$AD = b\cos A$，$CD = b\sin A$
- 于是 $BD = c - AD = c - b\cos A$
- 直角三角形 $BCD$ + 勾股定理：

$$
\begin{aligned}
a^2 &= CD^2 + BD^2 \\
&= (b\sin A)^2 + (c - b\cos A)^2 \\
&= b^2\sin^2 A + c^2 - 2bc\cos A + b^2\cos^2 A \\
&= b^2 + c^2 - 2bc\cos A
\end{aligned}
$$

> 🔑 把「角 $A$」换成任一角、字母轮换，就是同一个模板：**任一边的平方 = 另外两边的平方和 − 2×两边×两边夹角的余弦**。换成角 $C$ 就是开头的 $c^2 = a^2 + b^2 - 2ab\cos\theta$。
>
> ⚠️ 上面默认 $\angle A$ 是锐角（垂足落在线段 $AB$ 上）；钝角时**图形会变、公式不变**，具体推理见下一小节。

### 证法二（续）：钝角三角形的情况

上面的图形里 $\angle A$ 是锐角，垂足 $D$ 在线段 $AB$ 上，$AD = b\cos A > 0$。当 $\angle A$ 是**钝角**（$90^\circ < A < 180^\circ$）时 $\cos A < 0$，垂足 $D$ 不再落在线段 $AB$ 上，而是落在 **$AB$ 的延长线**上、在 $A$ 的另一侧：

![[MA-GE-001-altitude-proof-obtuse.svg]]

- 直角三角形 $ACD$ 中，$AD$ 这一段与 $B$ 方向相反，用**有向长度**仍是 $AD = b\cos A$（此时为负值）；高度则恒为 $CD = b\sin A > 0$（钝角处 $\sin A > 0$ 不变）
- $B$ 与 $D$ 分居 $A$ 两侧，故 $BD = c - AD = c - b\cos A$，与锐角时写成**同一个式子**
- 若 $\angle A = 90^\circ$ 则 $AD = 0$、$D$ 就是 $A$，公式退化为勾股定理 $a^2 = b^2 + c^2$

于是勾股定理的推理链与锐角时逐字相同：

$$
\begin{aligned}
a^2 &= CD^2 + BD^2 \\
&= (b\sin A)^2 + (c - b\cos A)^2 \\
&= b^2\sin^2 A + c^2 - 2bc\cos A + b^2\cos^2 A \\
&= b^2 + c^2 - 2bc\cos A
\end{aligned}
$$

> 💡 为什么 $\cos A < 0$ 不破坏推导？因为展开后的 $b^2 + c^2 - 2bc\cos A$ 是**对任意 $\cos A$ 都成立的恒等式**。$\cos A$ 为负只意味着有向长度 $AD = b\cos A$ 是负的（垂足退到延长线上），「$BD = c - AD$ + 勾股定理」这条推理链一字未改。所以钝角三角形的公式与锐角完全相同，**变了的只是中间图形的形状**。

### 证法三：向量法（选读，需先会点积）

把两边看成从同一点出发的向量 $\mathbf{a}, \mathbf{b}$，第三边就是 $\mathbf{a} - \mathbf{b}$：

$$
\begin{aligned}
\|\mathbf{a} - \mathbf{b}\|^2 &= (\mathbf{a} - \mathbf{b}) \cdot (\mathbf{a} - \mathbf{b}) \\
&= \mathbf{a} \cdot \mathbf{a} + \mathbf{b} \cdot \mathbf{b} - 2\mathbf{a} \cdot \mathbf{b} \\
&= \|\mathbf{a}\|^2 + \|\mathbf{b}\|^2 - 2\|\mathbf{a}\| \|\mathbf{b}\| \cos\theta
\end{aligned}
$$

左边就是 $c^2$，所以 $c^2 = a^2 + b^2 - 2ab \cos\theta$，证毕。

> 💡 注意方向：最后一步**用了**点积公式 $\mathbf{a}\cdot\mathbf{b} = \|\mathbf{a}\|\|\mathbf{b}\|\cos\theta$，所以这其实是 **「点积公式 ⟹ 余弦定理」**，不能拿它给没学过点积的人"证明"余弦定理。
>
> 反方向那条路在 [[LA003-点积与正交性]] 里：用（纯几何独立成立的）余弦定理去**证明**点积公式。两条路方向相反，各是各的主线，**别拼成一条循环链**。余弦定理不欠点积任何东西——证法一、证法二已经独立证明了它。

## 📎 应用场景

1. **已知两边一夹角，求第三边**
2. **已知三边，求任意角的余弦/角度**
3. **线性代数**：证明点积的几何意义 $\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \|\mathbf{w}\| \cos\theta$
4. **解析几何**：计算两点距离、向量夹角

## ⚡ 常见误区 / 边界

- ❌ 误区："余弦定理只适用于锐角三角形" → 事实：对锐角/直角/钝角三角形都成立，钝角的余弦为负，公式依然正确
- ❌ 误区："余弦定理只能解三角形" → 事实：它是连接边长和夹角的桥梁，在向量、解析几何、积分都有用

## 🔗 关联卡片

- [[MA-GE-002-勾股定理]]（特例）
- [[MA-GE-003-直角三角形三角函数]]
- [[LA003-点积与正交性]]（用余弦定理证明点积夹角公式）
- 📝 变更日志：[[CHGLOG-MA-GE-001-余弦定理]]

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
