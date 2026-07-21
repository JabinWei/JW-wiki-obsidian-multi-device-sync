---
type: card
status: 已完成
aliases: [Timsort, 混合排序, 归并排序, 插入排序, run, 稳定排序, Python sort]
tags: [编程语言, 算法]
created: 2026-07-15
updated: 2026-07-20
---

## 💡 核心概念

Timsort 是 Python 内置排序方法（`list.sort()` 和 `sorted()`）的底层实现，由 Tim Peters 于 2002 年设计。它是一种**混合稳定排序算法**，将归并排序（Merge Sort）和插入排序（Insertion Sort）的优点结合，专门针对现实世界中"部分有序"的数据进行了极致优化。

---

## 🔍 详细说明

### 为什么是"混合"算法？

| 算法 | 擅长场景 | 在 Timsort 中的角色 |
|------|----------|---------------------|
| **插入排序** | 小规模数据（n < 32~64） | 对每个 run 内部排序或扩充 |
| **归并排序** | 大规模数据 | 将所有 run 两两归并 |

插入排序在小数组中常数因子极低，比归并排序更快；归并排序在大数组中保证 O(n log n) 的上界。Timsort 在两种策略间自适应切换。

### 核心机制：Run（自然有序子序列）

Timsort 不是把数组直接对半切，而是先扫描数据，识别出**自然有序的子序列**——即 run：

- 从左到右扫描，遇到一个连续递增（或严格递减）的子序列，记为一个 run。
- 如果递减，则将其原地翻转为递增（保证稳定性）。
- 如果 run 太短（小于 `minrun`，通常 32~64），则用**插入排序**将其扩充到 minrun 长度。

**minrun 的选择**：Python 中 `minrun` 取 32，计算公式为 `minrun = n >> (位长 / 2)`，使 run 数量刚好是 2 的幂或略少，有利于归并的平衡性。

### 归并策略

收集到的 run 放入一个栈中，归并时遵循两个不等式约束，确保栈中 run 的长度保持平衡：

- A > B + C（栈顶第三个 run 的长度大于前两个之和）
- B > C（栈顶第二个 run 的长度大于栈顶 run）

不满足时触发归并，始终合并相邻的较小 run，保持合并树的平衡。

### 优化技巧：Galloping 模式

当两个 run 归并时，如果一个 run 的元素连续多次都来自同一侧，Timsort 会进入 **galloping（飞奔）模式**：不再逐个比较，而是用指数搜索一次性跳过一大段，大幅减少比较次数。这让 Timsort 在数据分布极度不均时依然高效。

### 时间复杂度

| 情况 | 复杂度 | 说明 |
|------|--------|------|
| 最优（已排好序） | **O(n)** | 一次扫描确认有序，不触发归并 |
| 平均 | **O(n log n)** | 与归并排序一致 |
| 最差 | **O(n log n)** | 有上界保证，不会退化到 O(n²) |
| 空间 | **O(n)** | 需要临时数组存放归并结果 |

### 稳定性

Timsort 是**稳定排序**：如果两个元素的值相等（`a == b`），排序前 a 在 b 前面，排序后 a 依然在 b 前面。这在多级排序中至关重要——例如先按姓名排序再按年龄排序，同年龄者的姓名顺序不会被打乱。

---

## 📎 例子

```python
# 基本使用 —— 底层就是 Timsort
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  # [1, 2, 5, 5, 6, 9]

# 验证稳定性：按第二个元素排序，等值时保持原顺序
pairs = [('a', 3), ('b', 1), ('c', 3), ('d', 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)
# [('b', 1), ('d', 2), ('a', 3), ('c', 3)]
# ('a', 3) 和 ('c', 3) 的第二个元素相等，
# 'a' 在原序列中先于 'c'，排序后依然先于 'c'

# 部分有序数据的优势 —— Timsort 接近 O(n)
mostly_sorted = [1, 2, 3, 4, 100, 5, 6, 7, 8, 9]
mostly_sorted.sort()  # 极快：扫描到两个极长的自然 run，仅需一次归并
```

---

## ⚡ 反例 / 边界

1. **完全逆序的最差场景**：当数组完全逆序时，每个元素都是独立的单元素 run，归并次数最多，时间复杂度趋近 O(n log n) 的标准归并排序，无法享受自适应优化的红利。

2. **非稳定排序的对比**：快速排序（Quicksort）平均也是 O(n log n)，但它**不稳定**，且最差情况（选到极值 pivot）退化到 O(n²)。Timsort 通过精确的 run 划分和归并约束避免了这些问题。

3. **空间代价**：Timsort 需要 O(n) 的额外空间用于归并，远高于快速排序的 O(log n) 栈空间。在极端受限的嵌入式环境中这是需要权衡的因素。

---

## 🔗 关联卡片

- 核心笔记：[[PY009-列表]]
- 官方源码：[CPython listobject.c — Timsort 实现](https://github.com/python/cpython/blob/main/Objects/listobject.c)
- 参考：[Timsort 算法详解 (Wikipedia)](https://en.wikipedia.org/wiki/Timsort)
- **跨语言影响力**：
  - **Java**：`Arrays.sort(Object[])` 对对象数组使用 Timsort（Java 7+）
  - **Swift**：标准库 `sort()` 使用 Timsort
  - **Rust**：`slice::sort()` 使用 Timsort 变体
  - **Android**：Dalvik/ART 运行时采用 Timsort
  - **V8（Chrome/Node.js）**：`Array.prototype.sort` 使用 Timsort

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
