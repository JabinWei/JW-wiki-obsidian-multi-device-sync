---
type: card
status: 已完成
aliases: [enumerate, 带索引遍历, 计数遍历]
tags: [编程语言, Python]
created: 2026-09-17
updated: 2026-09-17
---

## 💡 核心概念

`enumerate()` 是 Python 的内置函数，把「可迭代对象」包装成一个「(索引, 值) 元组」的迭代器，让你在 `for` 循环里**边遍历边拿到编号**，一举替代 `range(len())` 和手动计数器。

```python
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    print(i, color)

# 0 red
# 1 green
# 2 blue
```

---

## 🔍 详细说明

### 1. 语法与 start 参数

`enumerate(iterable, start=0)`：`start` 控制**编号从几开始**，默认 0；遍历出的元素值不受影响。

```python
# 从 1 开始编号（打印菜单、给棋盘标注行号常用）
for i, color in enumerate(colors, start=1):
    print(f'{i}. {color}')

# 1. red
# 2. green
# 3. blue
```

> 打印带行号的棋盘时，用 `enumerate(board, start=1)` 让行号从 1 起跳，直接对应用户输入的坐标——不必自己再 `i + 1`。

### 2. 底层原理：它到底返回了什么

`enumerate()` 返回的是一个 **enumerate 对象**（迭代器），每次 `next()` 吐出一个 `(index, value)` 元组；`for` 循环再把这个元组**解包**成两个变量。

```python
e = enumerate(['a', 'b', 'c'])
print(e)             # <enumerate object at 0x...>
print(next(e))       # (0, 'a')
print(next(e))       # (1, 'b')
print(next(e))       # (2, 'c')
```

所以 `for i, v in enumerate(x)` 里的 `i, v`，本质是元组解包（解包概念见 [[PL-PY-005-元组不可变性的真正边界]]）。

### 3. 为什么不用 range(len())

手动拿索引是「反 Python」的老写法，`enumerate` 更简洁也更不易错：

```python
# ❌ 老派写法：手动计数，啰嗦且易错
for i in range(len(colors)):
    print(i, colors[i])

# ✅ enumerate：一步到位
for i, color in enumerate(colors):
    print(i, color)
```

### 4. 常用场景

| 场景 | 写法 |
|------|------|
| 边遍历边拿索引 | `for i, v in enumerate(seq)` |
| 从 1 开始编号 | `enumerate(seq, start=1)` |
| 只要值、忽略索引 | `for _, v in enumerate(seq)` |
| 逐字符带位置 | `for i, ch in enumerate('abc')` |

### 5. enumerate 与 zip 的分工

- `enumerate`：**一个序列** + 它的位置编号。
- `zip`：**多个序列**按位置配对（见 [[PY003-内置函数]]）。

---

## ⚡ 反例 / 边界

### 边界 1：enumerate 对象是「一次性」迭代器

```python
e = enumerate(['a', 'b'])
list(e)          # [(0, 'a'), (1, 'b')]
list(e)          # []  ← 已经耗尽，不能再用了
```

> 想复用就重新调 `enumerate()`，或者先 `list(enumerate(...))` 转成列表存起来。

### 边界 2：start 只改编号，不改遍历顺序

```python
for i, v in enumerate(['a', 'b'], start=10):
    print(i, v)
# 10 a
# 11 b
# ← start 只是让编号从 10 起跳，元素本身还是按原顺序遍历
```

### 边界 3：编号是「计数器」，不是真实索引

`enumerate` 本质上就是个计数器，它**不会回头核验**序列有没有真正的可寻址下标。遍历字典时，编号对应「第几个键」，而不是字典下标（字典本就没有下标）：

```python
for i, k in enumerate({'a': 1, 'b': 2}):
    print(i, k)   # 0 a  1 b  ← 编号是遍历顺序，不是"索引"
```

---

## 🔗 关联卡片

- [[PY013-条件与循环]] — `for` 循环与解包遍历的完整语法
- [[PL-PY-012-可迭代对象与迭代器协议]] — `enumerate` 返回的正是迭代器
- [[PL-PY-005-元组不可变性的真正边界]] — `for i, v in ...` 背后的元组解包
- [[PY003-内置函数]] — `zip()`、`range()` 等兄弟函数
- [[PY022-枚举]] — 别搞混：`enum.Enum` 是「定义常量集合」，`enumerate()` 是「遍历时计数」

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```