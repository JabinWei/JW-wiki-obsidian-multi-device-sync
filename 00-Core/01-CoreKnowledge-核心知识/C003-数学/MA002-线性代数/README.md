# 线性代数

参考教材：Gilbert Strang《Introduction to Linear Algebra》第 6 版

## 笔记索引

| 编号 | 主题 | 状态 |
|------|------|------|
| [[LA001-线性代数的来源]] | 线性代数的起源、全局骨架 | 学习中 |
| [[LA002-向量与线性方程的几何]] | 向量基础、行图像与列图像、Ax=b | 学习中 |
| LA003-点积与正交性 | 待创建 |
| LA004-行列式 | 待创建 |
| LA005-特征值与特征向量 | 待创建 |
| LA006-正交性与投影 | 待创建 |
| LA007-奇异值分解(SVD) | 待创建 |

## 学习资源

- MIT 18.06 视频课（B站有字幕）
- 3Blue1Brown《线性代数的本质》（可视化神作）
- NumPy `np.linalg` 模块实践

2. 乘积元素的计算规则（点积定义）

  乘积 $C = AB$ 的第 $i$ 行第 $j$ 列元素 $c_{ij}$，等于：
  $$
  \boxed{c_{ij} = (\text{A的第 } i \text{ 行}) \cdot (\text{B的第 } j \text{ 列}) = \sum_{k=1}^n a_{ik} b_{kj}}
  $$

  一句话：行乘列，点积得到一个元素。

  例子：

  $$
  A = \begin{bmatrix} 1 & 2 \ 3 & 4 \end{bmatrix}{2 \times 2}, \quad B = \begin{bmatrix} 5 & 6 \ 7 & 8 \end{bmatrix}{2 \times 2}
  $$

  计算 $c_{11}$：A 的第 1 行 · B 的第 1 列 = $1 \cdot 5 + 2 \cdot 7 = 5 + 14 = 19$

  计算 $c_{12}$：A 的第 1 行 · B 的第 2 列 = $1 \cdot 6 + 2 \cdot 8 = 6 + 16 = 22$

  计算 $c_{21}$：A 的第 2 行 · B 的第 1 列 = $3 \cdot 5 + 4 \cdot 7 = 15 + 28 = 43$

  计算 $c_{22}$：A 的第 2 行 · B 的第 2 列 = $3 \cdot 6 + 4 \cdot 8 = 18 + 32 = 50$

  结果：
  $$
  AB = \begin{bmatrix} 19 & 22 \ 43 & 50 \end{bmatrix}
  $$