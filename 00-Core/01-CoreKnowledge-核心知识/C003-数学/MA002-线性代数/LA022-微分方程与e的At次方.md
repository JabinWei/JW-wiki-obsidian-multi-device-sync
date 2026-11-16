---
type: learning
status: 已完成
domain: 数学
tags:
  - 数学
  - 线性代数
  - 微分方程
  - 矩阵指数
  - 特征值
  - 稳态与暂态
created: 2026-10-30
updated: 2026-10-30
---

## 🎯 学习目标

- 一阶线性常微分方程组 $\mathbf{u}'=A\mathbf{u}$ 的解为什么不是 $e^{\lambda t}$ 而是 $e^{At}$？
- 怎么用特征值把耦合的微分方程组"解耦"成 $n$ 个独立的标量方程？
- 离散版 $\mathbf{u}_{k+1}=A\mathbf{u}_k$ 和连续版 $\mathbf{u}'=A\mathbf{u}$ 有什么一一对应？
- 怎么从特征值的实部直接判断解是**趋于零、趋于稳态、还是爆炸/振荡**？
- 半稳定矩阵（有零特征值）为什么会收敛到一个**稳态向量**而不是原点？

---

## 📖 前置知识

- [[LA019-行列式的应用|LA019：特征多项式 $\det(A-\lambda I)=0$]]
- [[LA020-特征值与特征向量|LA020：特征值、特征向量 $A\mathbf{x}=\lambda\mathbf{x}$]]
- [[LA021-对角化与矩阵的幂|LA021：对角化 $A=S\Lambda S^{-1}$、离散差分方程 $\mathbf{u}_{k+1}=A\mathbf{u}_k$]]

---

## 📚 核心知识

> [[LA021-对角化与矩阵的幂|上一篇]] 我们把 $\mathbf{u}_{k+1}=A\mathbf{u}_k$ 解成了 $\mathbf{u}_k=A^k\mathbf{u}_0=S\Lambda^k S^{-1}\mathbf{u}_0$。这一篇把同一套思想搬到**连续时间**：$\mathbf{u}'=A\mathbf{u}$。Strang 把这两讲紧挨着排，就是为了让你看到**离散和连续是同一个结构的两面**。

### 从标量方程到矩阵方程

#### 标量：$u'=au$ 的解是 $e^{at}$

单个一阶常微分方程：

$$\frac{du}{dt}=au,\qquad u(0)=u_0$$

我们都知道解是 $u(t)=u_0 e^{at}$。这个 $e^{at}$ 是怎么来的？把指数函数泰勒展开：

$$e^{at}=1+at+\frac{(at)^2}{2!}+\frac{(at)^3}{3!}+\dots$$

逐项求导：$\frac{d}{dt}e^{at}=a e^{at}$，正好满足方程。

#### 矩阵：$u'=Au$ 的解自然就是 $e^{At}$

把标量 $a$ 换成矩阵 $A$，定义**矩阵指数**：

$$\boxed{e^{At}=I+At+\frac{(At)^2}{2!}+\frac{(At)^3}{3!}+\dots}$$

逐项求导：$\frac{d}{dt}e^{At}=A+A^2 t+\frac{A^3 t^2}{2!}+\dots=A\,e^{At}$。所以 $\mathbf{u}(t)=e^{At}\mathbf{u}_0$ 满足 $\mathbf{u}'=A\mathbf{u}$。

> 💡 注意 $e^{At}$ 和一般矩阵乘法一样，**没有 $e^{A+B}=e^A e^B$**（除非 $AB=BA$）。所以不能随便把 $e^{At}$ 拆成 $e^{(A)t}$ 什么的——它就是一个整体。

---

### 用特征值解耦：$e^{At}=S e^{\Lambda t} S^{-1}$

[[LA021-对角化与矩阵的幂|LA021]] 里我们已经知道 $A^k=S\Lambda^k S^{-1}$。对矩阵指数同样成立——因为泰勒展开每一项都是 $A^k$：

$$e^{At}=I+At+\frac{(At)^2}{2!}+\dots=S\left(I+\Lambda t+\frac{(\Lambda t)^2}{2!}+\dots\right)S^{-1}=S\,e^{\Lambda t}\,S^{-1}$$

而 $\Lambda$ 是对角矩阵 $\operatorname{diag}(\lambda_1,\dots,\lambda_n)$，所以：

$$e^{\Lambda t}=\begin{bmatrix}e^{\lambda_1 t}&&\\&\ddots&\\&&e^{\lambda_n t}\end{bmatrix}$$

**这就是解耦**：把 $\mathbf{u}$ 按特征向量展开 $\mathbf{u}_0=c_1\mathbf{x}_1+\dots+c_n\mathbf{x}_n$，则：

$$\mathbf{u}(t)=e^{At}\mathbf{u}_0=c_1 e^{\lambda_1 t}\mathbf{x}_1+c_2 e^{\lambda_2 t}\mathbf{x}_2+\dots+c_n e^{\lambda_n t}\mathbf{x}_n$$

> 🔑 **离散和连续的一一对应**：
>
> | | 离散 $\mathbf{u}_{k+1}=A\mathbf{u}_k$ | 连续 $\mathbf{u}'=A\mathbf{u}$ |
> |---|---|---|
> | 增长因子 | $\lambda^k$ | $e^{\lambda t}$ |
> | 解耦 | $\mathbf{u}_k=\sum c_i\lambda_i^k\mathbf{x}_i$ | $\mathbf{u}(t)=\sum c_i e^{\lambda_i t}\mathbf{x}_i$ |
> | 趋于零的条件 | $\|\lambda_i\|<1$ | $\operatorname{Re}(\lambda_i)<0$ |
> | 收敛到稳态 | 有 $\|\lambda\|<1$ 的特征值 + $\lambda=1$ | 有 $\operatorname{Re}(\lambda)<0$ + $\lambda=0$ |
>
> 这张表要背下来——Strang 课上反复用。

---

### 从特征值实部直接看长期行为

解耦之后，每个模式 $e^{\lambda_i t}$ 的行为完全由 $\lambda_i$ 决定：

| $\lambda_i$ 的位置 | $e^{\lambda_i t}$ 的行为 | 例子 |
|---|---|---|
| $\operatorname{Re}(\lambda)<0$ | $t\to\infty$ 时**指数衰减到 0** | $\lambda=-2$：$e^{-2t}$ |
| $\operatorname{Re}(\lambda)=0$ | **振荡**（纯虚 $\lambda=i\omega$ 时 $e^{i\omega t}$ 是单位圆旋转） | $\lambda=i$：$e^{it}=\cos t+i\sin t$ |
| $\operatorname{Re}(\lambda)>0$ | **指数爆炸** | $\lambda=1$：$e^t$ |
| $\lambda=0$ | **常数** $e^{0}=1$（稳态方向） | 马尔可夫矩阵的平稳分布 |

**判据一句话**：
- 所有特征值实部 $<0$ ⟺ $e^{At}\to 0$（原点是吸引子）；
- 有零特征值、其余实部 $<0$ ⟺ 解趋于一个**稳态向量**（零特征值对应的特征向量方向）；
- 有正实部特征值 ⟺ 解爆炸。

---

### 例子：2×2 耦合方程的解耦

解方程组：

$$\frac{d}{dt}\begin{bmatrix}u_1\\u_2\end{bmatrix}=\begin{bmatrix}-2&1\\1&-2\end{bmatrix}\begin{bmatrix}u_1\\u_2\end{bmatrix}$$

这个矩阵 $A=\begin{bmatrix}-2&1\\1&-2\end{bmatrix}$ 是对称的，特征值好算：$\lambda_1=-1,\ \lambda_2=-3$，对应特征向量 $\mathbf{x}_1=(1,1)^T$、$\mathbf{x}_2=(1,-1)^T$。

按上面的公式：

$$\mathbf{u}(t)=c_1 e^{-t}\begin{bmatrix}1\\1\end{bmatrix}+c_2 e^{-3t}\begin{bmatrix}1\\-1\end{bmatrix}$$

初始条件 $\mathbf{u}(0)=(1,0)$ 给出 $c_1=\tfrac12,\ c_2=\tfrac12$，所以：

$$\mathbf{u}(t)=\frac12 e^{-t}\begin{bmatrix}1\\1\end{bmatrix}+\frac12 e^{-3t}\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}\frac12(e^{-t}+e^{-3t})\\\frac12(e^{-t}-e^{-3t})\end{bmatrix}$$

**两个特征值实部都是负的**，所以 $t\to\infty$ 时 $\mathbf{u}(t)\to(0,0)$——原点吸引。其中 $e^{-3t}$ 衰减得快，早期就消失；后期主导模式是 $e^{-t}(1,1)$——解沿着 $(1,1)$ 方向趋于原点。

> 💡 这个例子里矩阵 $A$ 其实就是 [[LA013-关联矩阵与图网络|图拉普拉斯]] 那种"两节点交换"的对称结构——特征值 $-1,-3$ 全负（除了全连通图总有一个零特征值），对应热传导/扩散方程的衰减。

---

### 稳态例子：$\lambda=0$ 与其余 $\operatorname{Re}<0$

如果 $A$ 有一个零特征值 $\lambda_1=0$，其余特征值实部都 $<0$，那么：

$$\mathbf{u}(t)=c_1 e^{0\cdot t}\mathbf{x}_1+\sum_{i\ge 2}c_i e^{\lambda_i t}\mathbf{x}_i=c_1\mathbf{x}_1+\text{趋于零的部分}$$

$t\to\infty$ 时解收敛到**稳态向量** $c_1\mathbf{x}_1$。这正是 [[LA021-对角化与矩阵的幂|马尔可夫链]] 的连续版本——离散时 $\lambda=1$ 给稳态，连续时 $\lambda=0$ 给稳态，对应关系见上面那张表。

> ⚠️ 注意和离散的差别：离散里"稳态因子"是 $\lambda=1$（$1^k=1$），连续里是 $\lambda=0$（$e^{0t}=1$）。不要记混。

---

### 为什么 Strang 把这讲放在对角化之后

因为这一讲**没有任何新的线性代数工具**——所有计算都是 [[LA020-特征值与特征向量|特征值]]、[[LA021-对角化与矩阵的幂|对角化]] 的直接应用。Strang 的用意是：让你看到"特征值解耦"这个思想在连续时间系统里同样成立，而且把离散/连续两张表对照着记，理解会深一层。

这也是为什么这篇笔记的前置知识全部指向 [[LA021-对角化与矩阵的幂|上一篇]]——它本质上是对角化的**第二个应用**（第一个是离散差分方程）。

---

## 🧪 练习 / 验证

1. 把标量方程 $u'=-3u$ 的解写出来，确认 $e^{-3t}\to 0$。

2. 矩阵 $A=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$（90° 旋转）的特征值是什么？$e^{At}$ 是什么？它会趋于零吗？
   （提示：$\lambda=\pm i$，纯虚数，解是周期振荡。）

3. 解方程组 $\mathbf{u}'=\begin{bmatrix}-1&0\\0&-3\end{bmatrix}\mathbf{u}$，初始条件 $\mathbf{u}(0)=(2,5)$。为什么这个方程组不需要解耦？

4. 接上题的解，$t\to\infty$ 时解沿哪个方向趋于原点？是 $(1,0)$ 还是 $(0,1)$？
   （提示：哪个衰减慢？）

5. 矩阵 $A=\begin{bmatrix}-1&1\\1&-1\end{bmatrix}$ 的特征值是什么？$e^{At}\mathbf{u}_0$ 会趋于零还是稳态向量？稳态向量朝哪个方向？
   （提示：$\lambda=0,-2$，零特征值对应的特征向量是什么？）

---

## 🤔 常见误区

- **误区**："$e^{At}$ 就是把每个元素取指数 $e^{a_{ij}t}$"
  **事实**：不是。$e^{At}$ 是用泰勒展开定义的矩阵，$(i,j)$ 位置不是 $e^{a_{ij}t}$。比如 $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$，$A^2=0$，所以 $e^{At}=I+At=\begin{bmatrix}1&t\\0&1\end{bmatrix}$——上三角的 $t$ 是泰勒展开留下的，不是元素取指数。

- **误区**："离散版和连续版的'趋于零条件'是一样的"
  **事实**：离散要 $\|\lambda\|<1$，连续要 $\operatorname{Re}(\lambda)<0$。比如 $\lambda=-0.5$：离散 $(-0.5)^k\to 0$，连续 $e^{-0.5t}\to 0$——都衰减；但 $\lambda=0.5$：离散 $0.5^k\to 0$，连续 $e^{0.5t}$ **爆炸**。差别在于离散是"乘"、连续是"积分"。

- **误区**："有零特征值的矩阵，$e^{At}$ 也会趋于零"
  **事实**：$\lambda=0$ 给出 $e^{0}=1$，是个常数项。解会趋于零特征值对应的**特征向量方向**（稳态），而不是原点。

- **误区**："$e^{A+B}=e^A e^B$"
  **事实**：只有 $AB=BA$ 时才成立。矩阵指数不像标量指数那样随便拆。

---

## 🔗 相关资源

- 上一节：[[LA021-对角化与矩阵的幂]]
- 下一节：[[LA023-对称矩阵与正定矩阵]]
- MIT 18.06 线性代数 Lecture 23（Differential Equations and $e^{At}$）：https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- 参考教材：Gilbert Strang《Introduction to Linear Algebra》第 6 版 §6.3（Differential Equations and $e^{At}$）
