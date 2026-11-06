---
type: learning
status: 学习中
domain: 数学
tags:
  - 数学
  - 线性代数
  - 正交化
  - QR分解
  - 标准正交基
created: 2026-09-21
updated: 2026-09-21
---

## 🎯 学习目标

- 什么是**标准正交基**？它有什么好性质？
- 怎么把一组线性无关的向量变成一组标准正交基？Gram-Schmidt 算法步骤是什么？
- QR 分解是什么？$A = QR$，$Q$ 和 $R$ 分别是什么矩阵？
- 为什么用 QR 分解解最小二乘比直接用 $A^T A$ 更好？数值上更稳定？

---

## 📖 前置知识

- [[LA003-点积与正交性|LA003：点积与正交]]
- [[LA010-线性无关、基与维数|LA010：基和维数]]
- [[LA013-投影与投影矩阵|LA013：投影]]
- [[LA014-最小二乘|LA014：最小二乘解]]

---

## 📚 核心知识

### 标准正交基：好性质是什么

一组基 $\mathbf{q}_1, \mathbf{q}_2, \dots, \mathbf{q}_n$ 如果满足：
$$
\mathbf{q}_i^T \mathbf{q}_j = 
\begin{cases}
0 & i \neq j \\
1 & i = j
\end{cases}
$$
就说这组基是**标准正交基**。

就是说它们两两正交，每个长度都是 1。记 $Q = [\mathbf{q}_1 \ \mathbf{q}_2 \ \dots \ \mathbf{q}_n]$，那么上面的条件用矩阵写就是：
$$
Q^T Q = I
$$
太简洁了！所以 $Q^T = Q^{-1}$，$Q$ 的转置就是逆，这是标准正交矩阵最好的性质。

性质总结：
1. 标准正交矩阵 $Q$ 保持内积：$(Q\mathbf{x})^T (Q\mathbf{y}) = \mathbf{x}^T Q^T Q \mathbf{y} = \mathbf{x}^T I \mathbf{y} = \mathbf{x}^T \mathbf{y}$，内积不变，长度不变，角度不变。这就是正交变换，刚体变换，不改变几何形状。
2. 任何向量 $\mathbf{v}$ 用标准正交基表示：$\mathbf{v} = \sum_{i=1}^n c_i \mathbf{q}_i$，那么系数 $c_i = \mathbf{q}_i^T \mathbf{v}$，直接点积就得到，不用解方程组，太方便了！
3. 投影到 $C(Q)$ 的投影矩阵 $P = Q (Q^T Q)^{-1} Q^T = Q I^{-1} Q^T = Q Q^T$，简化太多了！

---

### Gram-Schmidt 正交化：从任意基到标准正交基

给一组线性无关的向量 $\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n$，我们一步步把它们变成标准正交的 $\mathbf{q}_1, \mathbf{q}_2, \dots, \mathbf{q}_n$。

思路：每一步，把新的向量减去它在之前已经正交化好的向量上的投影，剩下的部分就是和之前所有向量正交的，然后单位化。

**步骤**：

第一步：从 $\mathbf{a}_1$ 开始，先得到 $\mathbf{v}_1 = \mathbf{a}_1$，单位化：
$$
\mathbf{q}_1 = \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|} = \frac{\mathbf{a}_1}{\|\mathbf{a}_1\|}
$$

第二步：对 $\mathbf{a}_2$，减去它在 $\mathbf{q}_1$ 上的投影：
$$
\mathbf{v}_2 = \mathbf{a}_2 - (\mathbf{q}_1^T \mathbf{a}_2) \mathbf{q}_1
$$
这个 $\mathbf{v}_2$ 和 $\mathbf{q}_1$ 正交吗？验证一下：
$\mathbf{q}_1^T \mathbf{v}_2 = \mathbf{q}_1^T \mathbf{a}_2 - (\mathbf{q}_1^T \mathbf{a}_2) \mathbf{q}_1^T \mathbf{q}_1 = \mathbf{q}_1^T \mathbf{a}_2 - \mathbf{q}_1^T \mathbf{a}_2 \cdot 1 = 0$，对的，正交。然后单位化：
$$
\mathbf{q}_2 = \frac{\mathbf{v}_2}{\|\mathbf{v}_2\|}
$$

第三步：对 $\mathbf{a}_3$，减去它在 $\mathbf{q}_1$ 和 $\mathbf{q}_2$ 上的投影：
$$
\mathbf{v}_3 = \mathbf{a}_3 - (\mathbf{q}_1^T \mathbf{a}_3)\mathbf{q}_1 - (\mathbf{q}_2^T \mathbf{a}_3)\mathbf{q}_2
$$
这个 $\mathbf{v}_3$ 和 $\mathbf{q}_1, \mathbf{q}_2$ 都正交，然后单位化得到 $\mathbf{q}_3$。

一般地，第 $k$ 步：
$$
\boxed{\mathbf{v}_k = \mathbf{a}_k - \sum_{i=1}^{k-1} (\mathbf{q}_i^T \mathbf{a}_k) \mathbf{q}_i,\quad \mathbf{q}_k = \frac{\mathbf{v}_k}{\|\mathbf{v}_k\|}}
$$

一直算到最后，$\mathbf{q}_1, \dots, \mathbf{q}_n$ 就是标准正交基了。

---

### 例子：二维的 Gram-Schmidt

给 $\mathbf{a}_1 = (1, 1)$，$\mathbf{a}_2 = (1, 0)$，做正交化：

第一步：$\mathbf{v}_1 = \mathbf{a}_1 = (1, 1)$，$\|\mathbf{v}_1\| = \sqrt{1^2 + 1^2} = \sqrt{2}$，所以：
$$
\mathbf{q}_1 = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right)
$$

第二步：计算投影分量：$\mathbf{q}_1^T \mathbf{a}_2 = \frac{1}{\sqrt{2}} \cdot 1 + \frac{1}{\sqrt{2}} \cdot 0 = \frac{1}{\sqrt{2}}$，所以：
$$
\mathbf{v}_2 = (1, 0) - \frac{1}{\sqrt{2}} \cdot \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right) = (1, 0) - \left( \frac{1}{2}, \frac{1}{2} \right) = \left( \frac{1}{2}, -\frac{1}{2} \right)
$$
$\|\mathbf{v}_2\| = \sqrt{(\frac{1}{2})^2 + (-\frac{1}{2})^2} = \frac{1}{\sqrt{2}}$，单位化：
$$
\mathbf{q}_2 = \frac{\mathbf{v}_2}{1/\sqrt{2}} = \left( \frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}} \right)
$$

验证：$\mathbf{q}_1^T \mathbf{q}_2 = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} \cdot (-\frac{1}{\sqrt{2}}) = \frac{1}{2} - \frac{1}{2} = 0$，正交；长度都是 1，完美。

---

### QR 分解：$A = Q R$

Gram-Schmidt 过程其实就是把 $A$ 分解成 $Q$ 乘 $R$，其中：
- $A = [\mathbf{a}_1 \ \mathbf{a}_2 \ \dots \ \mathbf{a}_n]$，原来的矩阵；
- $Q = [\mathbf{q}_1 \ \mathbf{q}_2 \ \dots \ \mathbf{q}_n]$，标准正交列；
- $R$ 是 $n \times n$ 上三角矩阵。

为什么是上三角？我们把 Gram-Schmidt 反过来写：
$$
\begin{aligned}
\mathbf{a}_1 &= \|\mathbf{v}_1\| \mathbf{q}_1 = r_{11} \mathbf{q}_1 \\
\mathbf{a}_2 &= (\mathbf{q}_1^T \mathbf{a}_2) \mathbf{q}_1 + \|\mathbf{v}_2\| \mathbf{q}_2 = r_{12} \mathbf{q}_1 + r_{22} \mathbf{q}_2 \\
\mathbf{a}_3 &= (\mathbf{q}_1^T \mathbf{a}_3) \mathbf{q}_1 + (\mathbf{q}_2^T \mathbf{a}_3) \mathbf{q}_2 + \|\mathbf{v}_3\| \mathbf{q}_3 = r_{13} \mathbf{q}_1 + r_{23} \mathbf{q}_2 + r_{33} \mathbf{q}_3 \\
&\vdots \\
\mathbf{a}_n &= \sum_{i=1}^n r_{in} \mathbf{q}_i
\end{aligned}
$$
写成矩阵乘法就是：
$$
A = [\mathbf{a}_1 \ \dots \ \mathbf{a}_n] = [\mathbf{q}_1 \ \dots \ \mathbf{q}_n] \begin{bmatrix}
r_{11} & r_{12} & \dots & r_{1n} \\
0 & r_{22} & \dots & r_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & r_{nn}
\end{bmatrix} = Q R
$$
$R$ 对角线以下全是 0，所以是上三角矩阵！完美。

看一下我们刚才二维的例子：
$$
A = \begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix},\quad Q = \begin{bmatrix}1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & -1/\sqrt{2}\end{bmatrix}
$$
$R$ 呢？$r_{11} = \sqrt{2}$，$r_{12} = \mathbf{q}_1^T \mathbf{a}_2 = 1/\sqrt{2}$，$r_{22} = 1/\sqrt{2}$，所以：
$$
R = \begin{bmatrix}\sqrt{2} & 1/\sqrt{2} \\ 0 & 1/\sqrt{2}\end{bmatrix}
$$
验证 $Q R$：
$$
Q R = \begin{bmatrix}1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & -1/\sqrt{2}\end{bmatrix} \begin{bmatrix}\sqrt{2} & 1/\sqrt{2} \\ 0 & 1/\sqrt{2}\end{bmatrix} = \begin{bmatrix}1 & (1+1)/2 \\ 1 & (1-1)/2\end{bmatrix} = \begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix} = A
$$
完美，正好对。

---

### QR 分解解最小二乘

我们原来最小二乘解是 $\hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b}$，现在 $A = Q R$，代入：
$$
A^T A = (Q R)^T (Q R) = R^T Q^T Q R = R^T I R = R^T R
$$
$$
A^T \mathbf{b} = (Q R)^T \mathbf{b} = R^T Q^T \mathbf{b}
$$
所以正规方程变成：
$$
R^T R \hat{\mathbf{x}} = R^T Q^T \mathbf{b}
$$
如果 $A$ 列满秩，那么 $R$ 满秩可逆，所以 $R^T$ 也可逆，两边约掉 $R^T$，得到：
$$
R \hat{\mathbf{x}} = Q^T \mathbf{b}
$$
因为 $R$ 是上三角，所以直接回代就能解出 $\hat{\mathbf{x}}$，太方便了！

为什么比直接算 $A^T A$ 好？直接算 $A^T A$ 会放大数值误差，而 QR 分解数值更稳定，尤其是当 $A$ 接近列相关的时候，差异更明显。所以实际计算中，解最小二乘都用 QR 分解，不用直接算 $A^T A$。

---

## 🧪 练习 / 验证

1. 把 $\mathbf{a}_1 = (1, 1, 0), \mathbf{a}_2 = (1, 0, 1), \mathbf{a}_3 = (0, 1, 1)$ 用 Gram-Schmidt 正交化，得到标准正交基。

2. 对 $A = \begin{bmatrix}1 & 1 \\ 1 & 0 \\ 0 & 1\end{bmatrix}$，做 QR 分解，验证 $A = Q R$，$Q^T Q = I$，$R$ 上三角。

3. 用 QR 分解解最小二乘 $A\mathbf{x} = \mathbf{b}$，其中 $A = \begin{bmatrix}1 & 1 \\ 1 & 0 \\ 0 & 1\end{bmatrix}$，$\mathbf{b} = (1, 2, 3)$，得到 $\hat{\mathbf{x}}$。

4. 证明：如果 $A = Q R$ 是 QR 分解，$Q$ 是 $m \times n$ 列正交，$R$ 是 $n \times n$ 上三角，那么 $A^T A = R^T R$，所以 $\det(A^T A) = (\det R)^2 = (\prod r_{ii})^2$。

5. 为什么标准正交基的系数直接点积就能得到？证明：如果 $\mathbf{v} = \sum c_i \mathbf{q}_i$，那么 $c_i = \mathbf{q}_i^T \mathbf{v}$。

---

## 🤔 常见误区

- **误区**："Gram-Schmidt 只能对方阵做"
  **事实**：任何 $m \times n$ 矩阵，只要列线性无关（$m \ge n$），就能做 Gram-Schmidt，得到 $m \times n$ 的 $Q$ 和 $n \times n$ 的 $R$，一样分解，QR 分解对长方阵也成立。

- **误区**："QR 分解唯一"
  **事实**：如果要求 $R$ 的对角线元素都是正的，那么 QR 分解唯一；如果对角线可以有负的，就不唯一。因为你可以把某个 $\mathbf{q}_i$ 乘 $-1$，同时把 $R$ 对应行乘 $-1$，结果还是一样。

- **误区**："标准正交矩阵一定是方阵"
  **事实**：$Q$ 可以是 $m \times n$ 的长方阵，只要列标准正交，$Q^T Q = I$ 就成立；只有方阵才有 $Q Q^T = I$，长方阵 $Q Q^T$ 是投影矩阵到列空间，不是单位矩阵。

- **误区**："正交化一定要 Gram-Schmidt，别的方法不行"
  **事实**：Gram-Schmidt 是最直观的方法，实际数值计算中还有 Householder 变换等更稳定的方法，不过核心还是正交化，结果一样。

---

## 🔗 相关资源

- 上一节：[[LA014-最小二乘]]
- 下一节：[[LA016-行列式的性质与公式]]（待创建）
- MIT 18.06SC 线性代数 Lecture 13（正交基和 Gram-Schmidt）、Lecture 14（QR 分解）：https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/
- 参考教材：Gilbert Strang《Introduction to Linear Algebra》第 6 版 §4.4（Orthogonal Bases and Gram-Schmidt）
