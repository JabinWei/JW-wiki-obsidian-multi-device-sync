---
type: card
status: 已完成
aliases: [下划线占位符, 占位符, underscore placeholder, _ 变量, 丢弃变量]
tags: [编程语言, Python]
created: 2026-06-22
updated: 2026-06-22
---

# Python 中 `_` 作为占位符的使用

## 💡 核心概念

在 Python 中，`_` 被广泛用作**占位符**——当一个变量名在语法上是必需的，但逻辑上你完全不关心它的值时，就用 `_` 来表示"这个值我故意忽略"。

`_` 本质上是一个**合法的普通变量名**，Python 解释器对它没有任何特殊对待（REPL 除外）。它是写给**人类读者**看的约定，不是给解释器看的指令。

> 🔑 核心原则：**当语法需要一个变量，但你不需要使用它的值时，用 `_`。**

---

## 🔍 详细说明

### 一、循环中忽略循环变量

当只需要重复执行某操作，不关心每次迭代的索引值时：

```python
# ✅ 推荐：明确表示"不用这个值"
for _ in range(5):
    print("Hello")

# 遍历时只取 value，忽略 index
for _, value in enumerate(["a", "b", "c"]):
    print(value)
```

### 二、解包（Unpacking）中丢弃不需要的值

这是 `_` 最频繁的使用场景之一：

```python
# 丢弃中间的值
name, _, age = ("Alice", "secret_code", 25)  # _ = 'secret_code'

# 用 *_ 丢弃多个值（Python 3 扩展解包）
first, *_, last = [1, 2, 3, 4, 5]
# first = 1, last = 5, _ = [2, 3, 4]（中间三个全丢弃）

x, *_, z = [10, 20, 30, 40, 50]  # x=10, z=50

# 多返回值函数中忽略部分结果
_, result = some_function()  # 只要第二个返回值
```

### 三、异常处理中忽略异常对象

```python
try:
    risky_operation()
except ValueError as _:  # 关心类型但不使用异常对象
    print("值错误，已处理")
# 等价于更常见的写法：
except ValueError:       # 连 as 都不写，更简洁
    print("值错误，已处理")
```

### 四、交互式解释器（REPL）中存储上一个结果

这是 `_` 唯一被 Python 解释器**特殊对待**的场景：

```python
>>> 1 + 2
3
>>> _
3
>>> _ * 2
6
>>> [1, 2, 3]
[1, 2, 3]
>>> _
[1, 2, 3]
```

> ⚠️ 这个特性**只在交互式解释器中有效**，脚本文件中不会自动设置 `_`。

### 五、国际化和翻译函数的别名（约定）

在 gettext 等国际化场景中，`_` 常被用作翻译函数的别名：

```python
from gettext import gettext as _
print(_("Hello World"))  # 输出对应语言的翻译
```

---

## ⚡ 关键注意事项

### `_` 被赋值后仍然可以访问

`_` **不是魔法关键字**，它就是一个叫 `_` 的普通变量。一旦被赋值，它就是那个值：

```python
name, _, age = ("Alice", "shh", 25)
print(_)  # 'shh' ← 完全可以访问

for _ in range(3):
    pass
print(_)  # 2 ← 循环结束后 _ 保留最后一次的值
```

### 多重 `_` 赋值会互相覆盖

同一作用域中后面的赋值覆盖前面的，`_` 没有例外：

```python
_, _, z = (10, 20, 30)
print(_)  # 20 —— Python 从左到右赋值，_ 先绑 10 再绑 20，最终是 20
```

### REPL 中的 `_` 容易被覆盖

```python
>>> [1, 2, 3]
[1, 2, 3]
>>> _          # _ 自动绑定到 [1, 2, 3]
[1, 2, 3]
>>> for _ in range(5):   # 循环覆盖了 REPL 的 _
...     pass
>>> _          # 4 —— 不是 [1, 2, 3] 了！
4
```

### 不要和以下概念混淆

| 符号 | 含义 | 示例 |
|------|------|------|
| `_` | 占位符，"故意忽略" | `for _ in range(5)` |
| `_name` | 单下划线前缀，表示"内部使用/受保护" | `def _helper()` |
| `__name` | 双下划线前缀，触发**名称改写**（name mangling） | `self.__secret` → `_ClassName__secret` |
| `__name__` | 双下划线前后缀，系统定义的**特殊方法/属性** | `__init__`, `__str__` |
| `*_` | 解包中的"丢弃剩余所有" | `first, *_ = [1, 2, 3]` |

---

## 📎 例子

### 例子 1：二维列表展开时忽略外层索引

```python
matrix = [[1, 2], [3, 4], [5, 6]]

# 不需要行号，只要把所有元素收集起来
flattened = []
for row in matrix:        # row 被使用了，不用 _
    for x in row:
        flattened.append(x)
print(flattened)  # [1, 2, 3, 4, 5, 6]

# 等价推导式
flattened = [x for row in matrix for x in row]
```

### 例子 2：文件读取中跳过不需要的列

```python
# CSV 场景：只要第 1 列和第 3 列
data = "Alice,25,Engineer\nBob,30,Designer\n"

for line in data.strip().split("\n"):
    name, _, job = line.split(",")
    print(f"{name} is a {job}")
# Alice is a Engineer
# Bob is a Designer
```

### 例子 3：Tkinter / GUI 绑定中忽略事件对象

```python
# 按钮回调：需要接收 event 参数但不必使用
button.bind("<Button-1>", lambda _: print("Clicked!"))

# 等价于
def on_click(event):
    print("Clicked!")   # 不读 event 的内容
button.bind("<Button-1>", on_click)
```

### 例子 4：`*_` 扩展解包实用场景

```python
# 取首尾元素
scores = [95, 88, 76, 92, 85, 78, 98]
highest, *_, lowest = sorted(scores)
print(f"最高: {highest}, 最低: {lowest}")  # 最高: 76, 最低: 98

# 切割路径：只要第一级和文件名
path = "/home/user/projects/python/main.py"
root, *_, filename = path.split("/")
print(f"root={root}, file={filename}")  # root=, file=main.py
```

---

## 🔗 关联卡片

- [[PY009-Python中的列表]] — 列表解包、`*_` 扩展解包语法
- [[PY010-Python中的元组]] — 元组解包中的 `_` 占位
- [[PY013-Python中的条件与循环]] — `for _ in range()` 循环模式
- [[PY014-Python中的函数]] — 多返回值函数中忽略部分返回值
- [[PY019-Python中错误类型与异常处理机制]] — `except Error as _` 用法
- [[PL-PY-002-format使用方法详解]] — 格式化中的 `{}` 占位符（另一类占位概念）

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
