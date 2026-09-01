---
type: card
status: 已完成
aliases: [投影长度, 向量投影]
tags:
  - 数学
  - 线性代数
  - 点积
  - 投影
created: 2026-08-28
updated: 2026-08-28
---

## 💡 核心概念

向量 $\mathbf{v}$ 在方向 $\mathbf{n}$ 上的**投影长度**，可以用点积直接计算。本质就是直角三角形三角函数的直接推论。

## 🔍 详细说明

### 公式推导

![[MA-AL-001-projection-length.svg]]

给定向量 $\mathbf{v}$ 和方向向量 $\mathbf{n}$：

1. 设夹角为 $\theta$，由**三角函数定义**：
   $$
   \text{投影长度} = \|\mathbf{v}\| \cos\theta
   $$

2. 由点积几何公式：
   $$
   \mathbf{n} \cdot \mathbf{v} = \|\mathbf{n}\| \|\mathbf{v}\| \cos\theta
   $$

3. 联立消去 $\|\mathbf{v}\| \cos\theta$，得到：
   $$
   \boxed{\text{投影长度} = \frac{\mathbf{n} \cdot \mathbf{v}}{\|\mathbf{n}\|}}
   $$

4. 如果只关心长度不关心方向（距离），加绝对值：
   $$
   \boxed{\text{投影长度（绝对值）} = \frac{|\mathbf{n} \cdot \mathbf{v}|}{\|\mathbf{n}\|}}
   $$

### 特殊情况：方向向量是单位向量

如果 $\|\mathbf{n}\| = 1$（已经单位化），公式特别简单：

$$
\text{投影长度} = \mathbf{n} \cdot \mathbf{v}
$$

这就是为什么单位向量这么常用——投影计算直接一个点积搞定。

## 📎 应用场景

1. **点到平面距离**：连接平面上一点到给定点，投影到平面法向量方向，投影长度就是距离
2. **正交分解**：把一个向量分解到多个正交方向，每个分量就是投影长度
3. **最小二乘法**：找向量在子空间上的最佳逼近，本质就是找投影

## ⚡ 常见误区 / 边界

- ✔️ 投影长度可正可负：$\mathbf{n} \cdot \mathbf{v} > 0$ 说明投影和 $\mathbf{n}$ 同向，$\mathbf{n} \cdot \mathbf{v} < 0$ 说明反向
- ✔️ 距离是长度，必须用绝对值；带符号投影保留方向信息
- ❌ 不是"向量投影"就是标量长度：向量投影本身是一个向量（沿着 $\mathbf{n}$ 方向），长度就是我们算出来的这个值

## 🔗 关联卡片

- [[MA-GE-001-余弦定理]]
- [[MA-GE-003-直角三角形三角函数]]
- [[LA003-点积与正交性]] — 点积几何意义
- 应用：**点到平面距离** → [[LA003-点积与正交性#应用2：计算点到平面的距离]]

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
