---
type: learning
status: 已完成
domain: 数学
tags:
  - 数学
  - 线性代数
  - Fourier级数
  - Fourier矩阵
  - 根为单位
  - FFT
created: 2026-10-30
updated: 2026-10-30
---

## 🎯 学习目标

- Fourier 级数为什么能看成"正交函数展开"？它和最小二乘/投影有什么共同本质？
- Fourier 矩阵 $F_n$ 的元素怎么写出来？它为什么对称、为什么近乎酉？
- 根为单位 $\omega=e^{2\pi i/n}$ 在 Fourier 矩阵里起什么作用？
- FFT（快速傅里叶变换）为什么是 $F_n$ 的稀疏分解？
- 为什么说 Fourier 变换是信号处理、机器学习特征工程的基础？

---

## 📖 前置知识

- [[LA025-复矩阵与复数特征值|LA025：复数内积、$A^H$、酉矩阵]]
- [[LA016-最小二乘|LA016：正交展开与投影]] — Fourier 级数是同一套"正交基展开"
- [[LA017-Gram-Schmidt正交化与QR分解|LA017：标准正交基]]

---

## 📚 核心知识

### Fourier 级数：用正交基展开函数

任何周期函数 $f(x)$ 都能展开成复指数的线性组合：
$$
f(x) = \sum_{k=-\infty}^{\infty} c_k\, e^{ikx}
$$
这看起来和线性代数不搭边，但本质就是**正交基展开**：把 $e^{ikx}$ 看成基向量，$c_k$ 是坐标。

关键在正交性：不同频率的复指数在区间 $[0,2\pi]$ 上正交
$$
\int_0^{2\pi} e^{-ikx} e^{ilx}\,dx = \begin{cases}2\pi & k=l\\0 & k\neq l\end{cases}
$$
所以系数 $c_k$ 就是 $f$ 在基 $e^{ikx}$ 上的"投影"：
$$
c_k = \frac{1}{2\pi}\int_0^{2\pi} f(x)\, e^{-ikx}\,dx
$$

> 🔑 这和 [[LA016-最小二乘|最小二乘]] 里"向量在正交基上的坐标 = 内积除以基的长度平方"**完全是同一件事**，只是基从有限个向量换成了无限个函数。Fourier 级数 = 函数空间里的最小二乘投影。

---

### 离散化：Fourier 矩阵 $F_n$

实际计算时，我们在 $n$ 个等距点 $x_j = 2\pi j/n$（$j=0,\dots,n-1$）上采样。这时无限级数截断成有限组合，采样值 $\mathbf{f}=(f(x_0),\dots,f(x_{n-1}))^T$ 满足：

$$
\mathbf{f} = F_n\,\mathbf{c}
$$

其中 **Fourier 矩阵** $F_n$ 的元素是
$$
(F_n)_{jk} = \omega^{jk},\quad \omega = e^{2\pi i/n}
$$

$\omega$ 是**根为单位**（n-th root of unity），满足 $\omega^n=1$、且 $1,\omega,\omega^2,\dots,\omega^{n-1}$ 是所有 $n$ 次单位根。

举个 $n=4$ 的例子：$\omega=i$，
$$
F_4 = \begin{bmatrix}
1&1&1&1\\
1&i&i^2&i^3\\
1&i^2&i^4&i^6\\
1&i^3&i^6&i^9
\end{bmatrix}
= \begin{bmatrix}
1&1&1&1\\
1&i&-1&-i\\
1&-1&1&-1\\
1&-i&-1&i
\end{bmatrix}
$$
每一列都是一个频率的采样值，结构极有规律。

---

### $F_n$ 的性质：对称、近乎酉

1. **对称**：$F_n^T = F_n$（因为 $\omega^{jk}=\omega^{kj}$，对称位置元素相同）。注意是普通转置，不是共轭转置。

2. **$F_n^H F_n = nI$**：列向量在复内积下两两正交，长度平方是 $n$。
   证明：取两列 $k\neq l$，它们的内积 $\sum_{j=0}^{n-1}\overline{\omega^{jk}}\,\omega^{jl}=\sum_{j}(\omega^{l-k})^j$，这是等比级数，公比 $\omega^{l-k}\neq 1$ 且 $(\omega^{l-k})^n=1$，所以和为 0。

3. 于是 $\frac{1}{\sqrt n}F_n$ 是**酉矩阵**（标准正交基），逆就是 $\frac{1}{n}F_n^H = \frac{1}{n}\overline{F_n}$。

> 💡 计算 Fourier 系数 $\mathbf{c}=F_n^{-1}\mathbf{f}=\frac{1}{n}F_n^H\mathbf{f}$，本质就是把 $\mathbf{f}$ 投影到这 $n$ 个正交频率列上——又是投影。

---

### FFT：Fourier 矩阵的稀疏分解

直接算 $\mathbf{f}=F_n\mathbf{c}$ 需要 $n^2$ 次复数乘法（$F_n$ 是稠密的）。但 $F_n$ 结构极强：当 $n$ 是偶数时，$F_n$ 可以分解成两个稀疏的 $F_{n/2}$ 加简单的交换/缩放：
$$
F_n = \begin{bmatrix}I & D\\ I & -D\end{bmatrix}
\begin{bmatrix}F_{n/2} & 0\\ 0 & F_{n/2}\end{bmatrix} \cdot (\text{偶数行/奇数行重排})
$$
其中 $D=\text{diag}(1,\omega,\omega^2,\dots)$。

反复对半拆，复杂度从 $n^2$ 降到 $O(n\log n)$，这就是 **FFT（快速傅里叶变换）**。它不是新数学，只是发现 $F_n$ 能被递归稀疏分解——把稠密矩阵乘法拆成对数级的小运算。

> 🔑 FFT 的威力：$n=10^6$ 时，$n^2$ 是万亿次，$n\log n$ 是千万次，差上千倍。这是为什么数字信号处理（MP3、JPEG、通信）能实时跑的根本原因。

---

### 应用一瞥

- **信号处理**：把信号从时域变到频域，看清哪些频率成分强。
- **图像压缩**：JPEG 用 DCT（实数版 Fourier），扔掉高频小系数。
- **机器学习**：时序特征工程、卷积网络的频域加速、谱聚类（用图 Laplacian 的特征值，见 [[LA013-关联矩阵与图网络]]）。
- **数值线性代数**：FFT 是很多快速算法的内核。

---

## 🧪 练习 / 验证

1. 写出 $F_2$，验证它满足 $F_2^H F_2 = 2I$。

2. 验证 $F_4$ 的第 0 列和第 1 列在复内积下正交（计算 $\sum_{j=0}^3 \overline{\omega^{0}}\omega^{j}$）。

3. 为什么 Fourier 矩阵对称但不是 Hermite？（提示：对称是 $F^T=F$，Hermite 要求 $F^H=F$）

4. 用根为单位的几何意义解释：为什么 $1+\omega+\omega^2+\dots+\omega^{n-1}=0$？

5. $n=8$ 时 FFT 把乘法次数从 64 降到多少？（提示：递归对半）

---

## 🤔 常见误区

- **误区**："Fourier 级数和线性代数没关系"
  **事实**：关系大了。$e^{ikx}$ 就是一组正交基，$c_k$ 就是投影坐标，Fourier 矩阵就是这组基的坐标变换矩阵，和最小二乘、QR 是同一套理论。

- **误区**："Fourier 矩阵是酉矩阵"
  **事实**：差一点。$F_n^H F_n = nI$，不是 $I$；$\frac{1}{\sqrt n}F_n$ 才是酉矩阵。逆矩阵是 $\frac{1}{n}F_n^H$，不是 $F_n^H$。

- **误区**："FFT 是一种新的变换"
  **事实**：FFT 就是 DFT（离散 Fourier 变换），只是算法上利用 $F_n$ 的递归稀疏结构把 $n^2$ 降到 $n\log n$，数学上的矩阵还是同一个 $F_n$。

- **误区**："根为单位 $\omega$ 是随便取的"
  **事实**：$\omega=e^{2\pi i/n}$ 是 $n$ 次单位根里"旋转角最小"的那个，它的幂 $1,\omega,\dots,\omega^{n-1}$ 正好把单位圆 $n$ 等分，是 Fourier 矩阵周期性的根源。

---

## 🔗 相关资源

- 上一节：[[LA025-复矩阵与复数特征值]]
- 下一节：[[LA027-相似矩阵与Jordan形]]
- 呼应：[[LA016-最小二乘]] 的正交投影、[[LA013-关联矩阵与图网络]] 的谱聚类
- MIT 18.06SC 线性代数 Lecture 24（Markov 矩阵与 Fourier 级数）：https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/
- 参考教材：Gilbert Strang《Introduction to Linear Algebra》第 6 版 §10.3（The Fourier Matrix and Its Inverse）
