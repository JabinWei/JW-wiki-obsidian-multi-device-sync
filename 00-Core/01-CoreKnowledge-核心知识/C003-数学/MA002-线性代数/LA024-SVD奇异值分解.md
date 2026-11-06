---
type: learning
status: 学习中
domain: 数学
tags:
  - 数学
  - 线性代数
  - 奇异值分解
  - SVD
  - 低秩近似
created: 2026-09-21
updated: 2026-09-21
---

## 🎯 学习目标

- 什么是奇异值分解（SVD）？任何矩阵都能做 SVD 吗？
- 奇异值是什么？奇异向量是什么？它们和特征值特征向量是什么关系？
- SVD 怎么写成四个子空间的形式？四个基本子空间怎么安排到 $U$ 和 $V$ 里？
- SVD 怎么用来做低秩近似？为什么 Eckart-Young-Mirsky 定理说截断 SVD 是最好的近似？
- SVD 在数据科学里有什么用？比如主成分分析（PCA）。

---

## 📖 前置知识

- [[LA011-四个基本子空间与秩定理|LA011：四个基本子空间]]
- [[LA019-对角化与矩阵的幂#对称矩阵一定正交对角化|LA019：对称矩阵正交对角化]]
- [[LA020-对称矩阵与正定矩阵#正定矩阵|LA020：正定矩阵性质]]

---

## 📚 核心知识

### 奇异值分解：基本形式

对任意 $m \times n$ 矩阵 $A$，秩为 $r$，都可以分解成：
$$
\boxed{A = U \Sigma V^T}
$$
其中：
- $U$ 是 $m \times m$ 正交矩阵，列是左奇异向量；
- $V$ 是 $n \times n$ 正交矩阵，列是右奇异向量；
- $\Sigma$ 是 $m \times n$ 对角矩阵，对角线是奇异值 $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$，其他位置都是零。

这就是**奇异值分解**（Singular Value Decomposition，SVD），任何矩阵不管是不是方阵，不管秩多少，都能做奇异值分解。太神奇了，这是线性代数里非常漂亮的结论。

---

### 奇异值和奇异向量怎么来的

我们看 $A^T A$，它是 $n \times n$ 对称半正定矩阵，所以可以正交对角化：
$$
A^T A = V \Lambda V^T
$$
特征值都是非负的，记 $\lambda_i = \sigma_i^2$，所以 $\sigma_i = \sqrt{\lambda_i} > 0$ 对 $i=1,\dots,r$，这些 $\sigma_i$ 就是**奇异值**，$V$ 的列就是**右奇异向量** $\mathbf{v}_i$。

然后左奇异向量定义：
$$
\mathbf{u}_i = \frac{1}{\sigma_i} A \mathbf{v}_i,\quad i=1,\dots,r
$$
这些 $\mathbf{u}_i$ 是标准正交的，我们可以把它们扩充成整个 $\mathbb{R}^m$ 的一组标准正交基，得到 $U = [\mathbf{u}_1 \dots \mathbf{u}_m]$，正交矩阵。

所以我们看：
$$
A V = U \Sigma
$$
两边右乘 $V^T$：$A V V^T = U \Sigma V^T$ ⇒ $A = U \Sigma V^T$，完美，推导出来了。

同理，$A A^T = U \Sigma \Sigma^T U^T$，所以 $A A^T$ 的特征值就是 $\sigma_i^2$，左奇异向量就是它的特征向量，两边一致。

---

### SVD 和四个基本子空间

因为我们把奇异值按从大到小排：$\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$，所以 $V$ 可以分成两部分：前 $r$ 列对应行空间，后 $n-r$ 列对应零空间；$U$ 前 $r$ 列对应列空间，后 $m-r$ 列对应左零空间：
$$
V = [V_r \quad V_{n-r}],\quad U = [U_r \quad U_{m-r}]
$$
所以：
$$
A = U_r \Sigma_r V_r^T
$$
这个就是**紧 SVD**，$U_r$ 是 $m \times r$，$\Sigma_r$ 是 $r \times r$ 对角，$V_r^T$ 是 $r \times n$，比 full SVD 更紧凑，秩 $r$ 所以不用多余的零。

完美对应四个基本子空间：
1. $V$ 的前 $r$ 列：行空间 $C(A^T)$ 的一组标准正交基；
2. $V$ 的后 $n-r$ 列：零空间 $N(A)$ 的一组标准正交基；
3. $U$ 的前 $r$ 列：列空间 $C(A)$ 的一组标准正交基；
4. $U$ 的后 $m-r$ 列：左零空间 $N(A^T)$ 的一组标准正交基。

所以 SVD 一次性给了四个子空间的标准正交基，太方便了！

---

### 低秩近似：截断 SVD 是最好的近似

奇异值递减排列：$\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$，我们取前 $k$ 个奇异值，近似 $A$：
$$
A_k = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^T + \dots + \sigma_k \mathbf{u}_k \mathbf{v}_k^T
$$
$A_k$ 秩是 $k$，Eckart-Young-Mirsky 定理说：**在所有秩 $k$ 的矩阵中，$A_k$ 到 $A$ 的 Frobenius 距离最小**，也就是：
$$
\| A - A_k \|_F^2 = \sum_{i=k+1}^r \sigma_i^2
$$
所以这个近似是最好的低秩近似。

这个结论太重要了，数据压缩、降维都靠它。比如一张图片，秩很高，我们取前几十个奇异值，就能近似得很好，压缩比很高，质量损失很小。

---

### 主成分分析（PCA）

给定一组数据，中心化后记为矩阵 $X$，每行一个样本，每列一个特征，我们对 $X^T X$ 做 SVD，最大的几个奇异值对应的右奇异向量就是主方向，投影到这些方向上，保留最多方差，所以降维了，这就是主成分分析（PCA），本质就是 SVD。

所以机器学习里降维、数据压缩都常用 SVD，非常有用。

---

## 🧪 练习 / 验证

1. 求 $A = \begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix}$ 的奇异值分解，计算 $A^T A$，求特征值特征向量，得到奇异值和 $V$，然后算 $U$，验证 $A = U \Sigma V^T$。

2. 证明：$\det(A^T A) = (\sigma_1 \sigma_2 \dots \sigma_n)^2$，对 $n \times n$ 方阵 $A$。

3. 证明：$\|A\|_F^2 = \sigma_1^2 + \dots + \sigma_r^2$，Frobenius 范数平方等于奇异值平方和。

4. 对 $A = \begin{bmatrix}1 & 2 & 3 \\ 4 & 5 & 6\end{bmatrix}$，写出紧 SVD 的形状，$U_r$ 多少行多少列，$\Sigma_r$ 多少，$V_r^T$ 多少。

5. 为什么说 PCA 本质就是 SVD？解释一下。

---

## 🤔 常见误区

- **误区**："只有方阵才能做 SVD"
  **事实**：不对，任何 $m \times n$ 矩阵都能做 SVD，不管 $m$ 和 $n$ 是否相等，这是 SVD 的一大优点。

- **误区**："奇异值就是特征值"
  **事实**：奇异值是 $A^T A$ 特征值的平方根，不是 $A$ 的特征值，只有对称半正定矩阵奇异值才等于特征值。一般矩阵奇异值都是正的，特征值可以负可以复。

- **误区**："SVD 只能用来降维，别的没用"
  **事实**：SVD 用处太多了，求伪逆、解最小二乘、机器学习、图像处理、推荐系统、自然语言处理（LSA）都用，现在大语言模型里也有用。

- **误区**："截断 SVD 近似误差很大"
  **事实**：不对，前几个大奇异值已经包含了大部分信息，后面小奇异值一般是噪声，扔掉反而降噪，效果更好。

---

## 🔗 相关资源

- 上一节：[[LA020-对称矩阵与正定矩阵]]
- MIT 18.06SC 线性代数 Lecture 29（奇异值分解）：https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/
- 参考教材：Gilbert Strang《Introduction to Linear Algebra》第 6 版 §7.1（Singular Values and Singular Vectors）
