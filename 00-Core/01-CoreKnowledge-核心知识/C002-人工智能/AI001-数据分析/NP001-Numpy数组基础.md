---
type: learning
status: 已完成
domain: NumPy
tags: [Python, 数据分析]
created: 2026-08-17
updated: 2026-08-17
---

## 🎯 学习目标

- 为什么数据分析离不开 NumPy？它解决了 Python `list` 的什么问题？
- `ndarray` 是什么？它和 `list` 的本质区别在哪？
- 怎么创建数组：`np.array` / `np.zeros` / `np.ones` / `np.arange` / `np.linspace`
- 看懂数组的关键属性：`shape` / `ndim` / `size` / `dtype`
- `dtype` 是什么，怎么用 `astype` 转换类型

## 📖 前置知识

- [[PY009-列表]] — list 的基本操作与特性
- [[PY019-模块]] — 如何 `import` 第三方库

## 📚 核心内容

NumPy（Numerical Python）是 Python 做数值计算、数据分析、机器学习的**地基**。你以后会碰到的 Pandas、scikit-learn、PyTorch，几乎都在它的数组之上构建。所以这一步值得走稳。

### 为什么 Python 的 list 不够用

list 很灵活——可以塞任意类型、随意增删。但正是这种「灵活」让它做数值计算时**慢**：

```python
# 给 100 万个数字每个加 1
lst = list(range(1_000_000))
result = [x + 1 for x in lst]      # Python 层逐个循环，慢
```

慢的根因有三层：

1. **存的是指针**：list 里每个元素都是指向独立 Python 对象的指针，内存不连续，CPU 缓存利用差；
2. **运行时类型检查**：每次运算都要先问「这个元素是什么类型」，开销大；
3. **Python 层循环**：`for` 循环本身在解释器里跑，效率低。

NumPy 的 **ndarray**（N 维数组）就是冲着这三个问题来的。

### ndarray：一块连续、同质的数组

`ndarray` 的三大特性，正好对应 list 的三个痛点：

| 特性 | 含义 | 解决的痛点 |
|------|------|-----------|
| **同质（homogeneous）** | 所有元素同一个 `dtype` | 不用运行时类型检查 |
| **连续内存** | 一块连续的内存块 | CPU 缓存友好 |
| **向量化** | 运算在底层 C 实现，一次算整块 | 不用 Python 循环 |

> 🔑 一句话记住区别：**list 是「一箱装杂物的抽屉」，ndarray 是「一块连续排好的数字矩阵」。** 前者灵活，后者快。

```python
import numpy as np     # 约定俗成的别名 np

arr = np.array([1, 2, 3, 4, 5])
print(arr)             # [1 2 3 4 5]  （注意：没有逗号）
print(type(arr))       # <class 'numpy.ndarray'>
```

### 创建数组的几种方式

```python
import numpy as np

# ① 从 list / tuple 创建
np.array([1, 2, 3])
np.array([[1, 2, 3], [4, 5, 6]])   # 二维：2 行 3 列

# ② 全 0 / 全 1（传 shape 元组）
np.zeros((2, 3))                   # 2 行 3 列全 0
np.ones((2, 3))                    # 全 1

# ③ 等差数列
np.arange(0, 10, 2)                # [0 2 4 6 8]，类似 range，左闭右开
np.linspace(0, 1, 5)               # [0.  0.25 0.5  0.75 1. ]，0~1 等分 5 个点

# ④ 全空数组（值未初始化，是内存垃圾，一般不直接用）
np.empty((2, 2))
```

> 💡 `np.arange` 和内置 `range` 用法几乎一样，但返回的是 ndarray 而不是 range 对象。`np.linspace` 则是「闭区间、按点数等分」，适合取一段连续区间。

### 看懂数组的四个关键属性

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr.shape    # (2, 3)  形状：2 行 3 列
arr.ndim     # 2       维度数（几维）
arr.size     # 6       元素总数
arr.dtype    # dtype('int64')  元素的数据类型
```

| 属性 | 含义 | 示例值 |
|------|------|--------|
| `shape` | 每个维度的大小（元组） | `(2, 3)` |
| `ndim` | 维度数 | `2` |
| `size` | 元素总数 | `6` |
| `dtype` | 元素的数据类型 | `int64` |

> 🔑 维度可以这么理解：**一维 = 向量，二维 = 矩阵，三维及以上 = 张量**（机器学习里天天见）。`ndim` 是「有几维」，`shape` 是「每一维各有多大」。

### dtype：同质带来的「约束」

ndarray 要求所有元素同一类型，创建时**自动推断** dtype：

```python
np.array([1, 2, 3]).dtype        # dtype('int64')
np.array([1.0, 2.0]).dtype       # dtype('float64')
np.array([1, 2.5]).dtype         # dtype('float64')  ← int 被提升成 float
np.array(["a", "bc"]).dtype      # dtype('<U2')      ← 字符串，取最长那个的长度
```

**混合类型会向上提升**：`int → float → str`。所以 `np.array([1, "a"])` 里的 1 也会变成字符串 `"1"`。

用 `astype` 显式转换类型：

```python
arr = np.array([1, 2, 3])        # int64
arr.astype(float)                # 转成 float64
arr.astype(np.float64)           # 等价写法
```

> ⚠️ 常见类型有 `int8/int16/int32/int64`（整数，数字越大越占内存但能存更大的数）、`float32/float64`（浮点）、`bool`、`<Ux`（字符串）。做机器学习时 `float32/float64` 用得最多。

### 感受一次向量化的速度

先不深入原理（[[NP003-数组运算与广播]] 会展开），这里先直观感受一下 ndarray 为什么值得用：

```python
import numpy as np

arr = np.arange(1_000_000)
arr + 1          # 瞬间完成——底层 C 循环，没有 Python for
```

同样给 100 万个数加 1，list 要跑一段 Python 循环，ndarray 一行搞定、且快一个数量级以上。这就是「向量化」的威力，也是整个 NumPy 系列要反复用的核心思想。

---

## 🧪 练习 / 验证

### 练习 1：创建并检查数组

创建 `[[1,2,3],[4,5,6]]` 的 ndarray，打印它的 `shape`、`ndim`、`size`、`dtype`。

> [!info]- 答案
> ```python
> import numpy as np
> arr = np.array([[1, 2, 3], [4, 5, 6]])
> print(arr.shape)   # (2, 3)
> print(arr.ndim)    # 2
> print(arr.size)    # 6
> print(arr.dtype)   # int64
> ```

### 练习 2：用多种方式创建

分别用 `np.zeros`、`np.ones`、`np.arange`、`np.linspace` 创建以下数组：

- 3 行 2 列全 0
- 3 行 2 列全 1
- `[0, 3, 6, 9]`
- `[0, 0.5, 1]`（0 到 1 等分 3 个点）

> [!info]- 答案
> ```python
> np.zeros((3, 2))
> np.ones((3, 2))
> np.arange(0, 12, 3)     # [0 3 6 9]
> np.linspace(0, 1, 3)    # [0.  0.5 1. ]
> ```

### 练习 3：判断 dtype 与转换

写出 `np.array([1, 2.0])` 和 `np.array([1, "a"])` 的 dtype，然后把 `[1.7, 2.9]` 转成整数，观察结果。

> [!info]- 答案
> ```python
> np.array([1, 2.0]).dtype   # float64（int 提升为 float）
> np.array([1, "a"]).dtype   # <U1（都变成字符串）
>
> np.array([1.7, 2.9]).astype(int)   # [1 2]  ← 直接截断，不四舍五入！
> ```

---

## 🤔 常见误区

1. **「ndarray 就是带了很多方法的 list」**
   **事实**：本质不同。list 存的是指向 Python 对象的指针，ndarray 是连续内存 + 统一 dtype。这决定了性能差一个数量级，不是「方法多一点」的差别。

2. **「用 Python 循环遍历 ndarray 做计算」**
   **事实**：能用，但慢，等于把 NumPy 的优势全扔了。正确姿势是向量化（一次对整块运算），这也是 [[NP003-数组运算与广播]] 的主角。

3. **「dtype 无所谓，反正都是数字」**
   **事实**：dtype 决定内存占用和精度——`int8` 最大只能存 127，`float32` 精度不如 `float64`。而且混合类型会静默提升，`np.array([1, 2.5])` 里的 1 悄悄变成 float。

4. **「ndarray 能像 list 一样混合存任意类型」**
   **事实**：不能。一旦创建 dtype 就固定，塞不同类型会被强制提升成统一类型（int 甚至可能变成字符串）。

5. **「shape 和 ndim 是同一个东西」**
   **事实**：`ndim` 是「有几维」（一个数字），`shape` 是「每一维各有多大」（一个元组）。`np.zeros((2,3))` 的 ndim 是 2，shape 是 `(2, 3)`。

---

## 🔗 相关资源

- 下一节：[[NP002-索引与切片]]
- 上一级索引：[[数据分析-MOC]]
- Python 前置：[[PY009-列表]]
- NumPy 官方文档：[NumPy Documentation](https://numpy.org/doc/)
- 官方快速入门：[NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
