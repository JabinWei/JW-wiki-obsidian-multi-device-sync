---
type: card
status: 已完成
aliases: [推导式, comprehension, 列表推导式, 字典推导式, 集合推导式, 生成器表达式]
tags: [编程语言, Python]
created: 2026-07-20
updated: 2026-07-20
---

## 💡 核心概念

Python 四种推导式语法几乎一致，区别仅在外层括号。本文聚焦**四者横向对比**和**常见混淆点**，基础用法参见对应核心笔记。

| 类型 | 语法 | 结果 | 基础参见 |
|------|------|------|----------|
| 列表 | `[expr for x in iterable]` | `list` | [[PY009-列表#列表解析]] |
| 字典 | `{k: v for k, v in iterable}` | `dict` | [[PY011-字典]] |
| 集合 | `{expr for x in iterable}` | `set` | [[PY012-集合]] |
| 生成器 | `(expr for x in iterable)` | `generator` | [[PY015-高阶函数]] |

---

## 🔍 详细说明

### 1. 同一逻辑，四种写法

```python
# 把 0-9 中的偶数平方，结果去重
numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9]

# 列表推导式 — 保留所有结果
[x**2 for x in numbers if x % 2 == 0]
# [4, 4, 16, 36, 36, 64]

# 集合推导式 — 自动去重
{x**2 for x in numbers if x % 2 == 0}
# {64, 4, 36, 16}

# 字典推导式 — 键值映射
{x: x**2 for x in range(1, 5)}
# {1: 1, 2: 4, 3: 9, 4: 16}

# 生成器表达式 — 惰性求值，按需产出
gen = (x**2 for x in numbers if x % 2 == 0)
next(gen)  # 4
next(gen)  # 4
```

### 2. map/filter vs 推导式

```python
numbers = [1, 2, 3, 4, 5]

# map + lambda — 需要理解两个概念
list(map(lambda x: x**2, numbers))    # [1, 4, 9, 16, 25]

# 推导式 — 直觉化，无需 lambda
[x**2 for x in numbers]               # [1, 4, 9, 16, 25]

# filter + lambda — 嵌套心智负担
list(filter(lambda x: x % 2 == 0, numbers))

# 推导式 — 条件直接写在句末
[x for x in numbers if x % 2 == 0]    # [2, 4]
```

> **结论**：单一映射/过滤用推导式更 Pythonic。已封装好的具名函数可继续用 `map()`。

### 3. 高频混淆：`if-else` 位置决定行为

```python
grades = [85, 60, 92, 45, 78]

# if-else 在表达式位置 → 映射（不变元素数量）
["通过" if g >= 60 else "挂科" for g in grades]
# ['通过', '通过', '通过', '挂科', '通过']   ← 5 入 5 出

# if 在末尾 → 过滤（可能减少元素）
[g for g in grades if g >= 60]
# [85, 60, 92, 78]                          ← 5 入 4 出
```

---

## 📎 例子

```python
# 字典推导式 — fromkeys 陷阱的正确替代
keys = ['a', 'b', 'c']
# ❌ dict.fromkeys(keys, []) — 所有键共享同一个 []
# ✅ 字典推导式 — 每个键独立创建
d = {k: [] for k in keys}
d['a'].append(1)
print(d)  # {'a': [1], 'b': [], 'c': []}  ← 互不影响

# 嵌套循环 vs 推导式 — 可读性对比
pairs = []
for x in [1, 2, 3]:
    for y in ['a', 'b']:
        if x != 2:
            pairs.append((x, y))

# 推导式 — 同样逻辑，一行表达
[(x, y) for x in [1, 2, 3] for y in ['a', 'b'] if x != 2]
```

---

## ⚡ 反例 / 边界

1. **嵌套超过两层** → 回归传统 for 循环，可读性 > 炫技
2. **大数据量** → 用生成器 `()` 代替列表 `[]`，避免一次性占满内存
3. **需多次访问结果** → 用列表，生成器只能消费一次
4. **推导式用于副作用（如 `print`）** → 反模式，用 for 循环

---

## 🔗 关联卡片

- [[PY009-列表#列表解析]] — 列表推导式基础语法与执行步骤
- [[PY011-字典]] / [[PY012-集合]] / [[PY015-高阶函数]]
- [[PL-007-Timsort混合排序算法]]

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
