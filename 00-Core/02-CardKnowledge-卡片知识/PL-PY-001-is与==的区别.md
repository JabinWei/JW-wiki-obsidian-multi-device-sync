---
type: card
status: 已完成
aliases: [is vs ==, 身份运算符, identity operator]
tags: [编程语言, Python]
created: 2026-06-18
updated: 2026-06-18
---

## 💡 核心概念

- **`==`** 比较的是**值是否相等**（value equality）
- **`is`** 比较的是**对象身份是否相同**（identity equality），即两个变量是否指向内存中的**同一个对象**

---

## 🔍 详细说明

Python 中每个对象在内存中都有一个唯一的身份标识（可通过 `id()` 查看）。`is` 运算符本质上就是在比较两个对象的 `id()` 是否相等。

| 比较维度 | `==` | `is` |
|---------|------|------|
| 比较内容 | 值（内容） | 对象身份（内存地址） |
| 底层实现 | 调用 `__eq__()` 方法 | 比较 `id(a) == id(b)` |
| 使用场景 | 日常值比较 | `None` 判断、单例对象 |
| 可变性 | 可被自定义类重载 | 不可重载 |

### 使用建议

- **绝大多数场景使用 `==`**：比较数值、字符串、列表内容等
- **与 `None` 比较用 `is`**：`x is None`（PEP 8 推荐，更快且不会被重载的 `__eq__` 干扰）
- **判断单例对象用 `is`**：如 `True`、`False`、`None`

### 小整数驻留（Integer Interning）陷阱

CPython 会缓存 -5 到 256 的小整数，因此对这个范围内的整数，`is` 可能意外返回 `True`：

```python
a = 256
b = 256
print(a is b)  # True（CPython 缓存了小整数）

a = 257
b = 257
print(a is b)  # False（超出缓存范围，是两个不同对象）
```

> **结论**：永远不要用 `is` 来比较数值，依赖 CPython 的实现细节会导致难以发现的 bug。

---

## 📎 例子

```python
a = [1, 2, 3]
b = [1, 2, 3]   # 新建一个内容相同的列表
c = a            # c 是 a 的引用（别名）

# == 比较值
print(a == b)    # True — 两个列表内容相同
print(a == c)    # True — 内容当然相同

# is 比较对象身份
print(a is b)    # False — 两个独立创建的列表，内存地址不同
print(a is c)    # True — c 就是 a，指向同一个对象

# 验证内存地址
print(id(a))     # 例如 4332156480
print(id(b))     # 例如 4332156544（不同于 a）
print(id(c))     # 例如 4332156480（与 a 相同）
```

**修改一个变量会影响另一个吗？**

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

c.append(4)
print(a)  # [1, 2, 3, 4] — a 也被修改了！因为 c 和 a 是同一个对象
print(b)  # [1, 2, 3] — b 不受影响，因为它是独立的对象
```

**`is None` 是最佳实践：**

```python
x = None

# ✅ 推荐（PEP 8）
if x is None:
    print("x 是 None")

# ❌ 可行但不推荐（__eq__ 可能被重载，有隐患）
if x == None:
    print("x 是 None")
```

---

## ⚡ 反例 / 边界

**不要用 `is` 比较数值：**

```python
# ❌ 错误示范
a = 1000
b = 500 + 500
print(a is b)  # 结果不确定，依赖 Python 实现
```

**`is` 不可被重载**：自定义类无法修改 `is` 的行为，它始终比较内存地址。这与 `==` 不同——`==` 可以通过定义 `__eq__()` 方法来自定义比较逻辑。

**简短字符串的驻留陷阱**：与整数类似，CPython 会驻留（intern）某些短字符串，导致 `is` 的结果不可预测：

```python
a = "hello"
b = "hel" + "lo"
print(a is b)  # 在 CPython 中可能为 True（字符串驻留），但不应依赖此行为
```

---

## 🔗 关联卡片

- [[PY004-关键字]] — `is` 关键字定义
- [[PY007-运算符]] — 成员与身份运算符
- [[PY009-列表]] — 列表比较中的 `is` vs `==`
- [[PY005-变量]] — 变量是对象标签，理解对象身份的基础

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
