---
type: learning
status: 已完成
domain: Python
tags:
  - Python
  - 编程语言
created: 2026-06-12
updated: 2026-06-16
---
# Python 中的关键字

## 🎯 学习目标

学完本篇后，你应该能回答以下问题：

- 什么是 Python 关键字（Keywords）？它们和普通变量名有什么区别？
- Python 3.12 共有多少个核心关键字？按功能分为哪六类？
- 逻辑与布尔类关键字（`True`、`False`、`None`、`and`、`or`、`not`、`is`、`in`）各自的作用是什么？
- 流程控制关键字（`if`、`elif`、`else`、`for`、`while`、`break`、`continue`、`pass`）分别在什么场景使用？
- 函数与类关键字（`def`、`class`、`return`、`yield`、`lambda`、`global`、`nonlocal`）的核心用法是什么？
- 异常处理关键字（`try`、`except`、`finally`、`raise`、`assert`）如何协同工作？
- 什么是"软关键字"？`match`、`case` 和 `_` 与普通关键字有何不同？

---

## 📖 前置知识

- [[PY003-Python中的内置函数]] — 了解 Python 的内置函数体系

---

## 📚 核心内容

### 关键字

在 Python 的编程世界里，我们每天都在和变量、函数、类打交道。但你是否注意过那些"不能用作变量名"的特殊单词？比如 `if`、`for`、`class`、`def`？

这些就是 **Python 关键字（Keywords）**，也被称为**保留字**。它们是 Python 语言的"基石"，拥有特殊的语法含义，是解释器理解你代码意图的关键。

---

#### 什么是关键字？

简单来说，关键字就是 Python 内部已经"预定"好的单词。你不能把它们用作变量名、函数名或类名，否则会引发 `SyntaxError`（语法错误）。

Python 是严格区分大小写的语言，所以 `True` 是关键字，但 `true` 就不是；`if` 是关键字，但 `If` 就可以作为变量名（虽然不推荐）。

你可以随时通过以下代码查看当前 Python 版本的所有关键字：

```python
import keyword

# 打印所有关键字列表
print(keyword.kwlist)

# 判断某个字符串是否是关键字
print(keyword.iskeyword("if"))  # 输出: True
```

---

#### Python关键字全景图

截至 Python 3.12，共有 **35 个**核心关键字。为了让你不再死记硬背，我将它们按功能分成了六类。

| 类别             | 关键字                                                       |
| ---------------- | ------------------------------------------------------------ |
| **逻辑与布尔**   | `True`, `False`, `None`, `and`, `or`, `not`, `is`, `in`      |
| **流程控制**     | `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `pass` |
| **函数与类**     | `def`, `class`, `return`, `yield`, `lambda`, `global`, `nonlocal` |
| **异常处理**     | `try`, `except`, `finally`, `raise`, `assert`                |
| **模块与上下文** | `import`, `from`, `as`, `with`, `del`                        |
| **异步编程**     | `async`, `await`                                             |

---

#### 核心关键字详解

**逻辑与布尔**

这些关键字用于处理真假值和逻辑关系，是所有条件判断的基础。

- **`True` / `False`**：代表真和假。注意首字母必须大写。
- **`None`**：代表"空"或"无"，类似于其他语言中的 `null`。
- **`and` / `or` / `not`**：逻辑与、或、非。例如 `if x > 0 and x < 10:`。
- **`is`**：用于判断两个变量是否指向同一个内存地址（身份比较），不同于 `==`（值比较）。详见 [[PL-PY-001-is与==的区别]]。
- **`in`**：用于判断元素是否存在于序列（如列表、字符串）中。

**流程控制**

没有这些关键字，代码只能从上到下顺序执行，它们赋予了代码"思考"和"循环"的能力。

- **`if` / `elif` / `else`**：条件判断的三剑客。Python 没有 `switch-case`（3.10 之前），全靠它们。
- **`for` / `while`**：循环结构。`for` 用于遍历序列，`while` 用于满足条件时循环。
- **`break` / `continue`**：`break` 用于彻底跳出循环，`continue` 用于跳过本次循环的剩余代码，直接进入下一次循环。
- **`pass`**：这是一个"占位符"。当你写了一个 `if` 语句或函数定义，但暂时不想写具体代码时，用 `pass` 来防止报错。

**函数与类**

这是 Python 面向对象和函数式编程的核心。

- **`def`**：定义函数的开始。
- **`class`**：定义类的开始。
- **`return`**：从函数中返回值。
- **`lambda`**：用于定义匿名函数（一行函数），常用于 `map` 或 `filter` 中。
- **`yield`**：用于生成器函数。它会让函数"暂停"并返回一个值，下次调用时从暂停处继续，极大地节省内存。
- **`global` / `nonlocal`**：用于修改变量的作用域。`global` 用于修改全局变量， `nonlocal` 用于修改嵌套函数中的外层变量。

**异常处理**

程序难免会出错，这些关键字能防止程序直接崩溃。

- **`try` / `except`**：尝试执行可能出错的代码，如果出错则捕获并处理。
- **`finally`**：无论是否出错，这段代码都会执行（常用于关闭文件、释放资源）。
- **`raise`**：主动引发一个异常。
- **`assert`**：断言。如果条件为 `False`，则程序立即报错并停止。常用于调试。

**模块与上下文：资源管理大师**

- **`import` / `from` / `as`**：用于导入模块。`as`可以给模块起别名，比如 `import numpy as np`。
- **`with`**：上下文管理器。最常用于文件操作，它能自动帮你关闭文件，无需手动`close()`。
- **`del`**：删除对象的引用，相当于告诉 Python "我不需要这个变量了"，触发垃圾回收。

**异步编程：现代高并发利器**

- **`async` / `await`**：用于编写并发代码。`async` 定义一个协程，`await` 用于等待一个异步操作完成，让程序在等待时可以去处理其他任务。

---

#### 软关键字与特殊标识符

除了上述 35 个硬性规定的关键字，Python 3.10 引入了**结构化模式匹配**，带来了几个"软关键字"：`match`、`case` 和 `_`（通配符）。

它们被称为"软"关键字，是因为它们只在特定的语法结构（`match` 语句）中才具有特殊含义，在其他地方你仍然可以将它们用作变量名（虽然极度不推荐这样做，以免混淆）。

此外，还有一些特殊的标识符命名规则，虽然不是关键字，但也需要留意：

- **`_var`**：以单下划线开头的变量，约定俗成地表示"私有"或"内部使用"。
- **`__var__`**：以双下划线开头和结尾的变量（如`__init__`），由系统定义，切勿随意命名。

---

## 🧪 练习 / 验证

### 练习 1：查看关键字列表

在 Python 交互环境中运行以下代码，你能说出当前 Python 版本共有多少个关键字吗？

```python
import keyword
print(keyword.kwlist)
print(f"共有 {len(keyword.kwlist)} 个关键字")
```

**答案（Python 3.12 环境）：**
```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
 'return', 'try', 'while', 'with', 'yield']
共有 35 个关键字
```

---

### 练习 2：大小写敏感验证

以下哪些是合法的变量名？为什么？

```python
True = 1
true = 1
If = 1
if = 1
NONE = None
```

**答案：**

| 代码 | 是否合法 | 原因 |
|---|---|---|
| `True = 1` | ❌ | `True` 是关键字 |
| `true = 1` | ✅ | `true` 不是关键字（大小写敏感） |
| `If = 1` | ✅ | `If` 不是关键字（大小写敏感），但不推荐 |
| `if = 1` | ❌ | `if` 是关键字 |
| `NONE = None` | ✅ | `NONE` 不是关键字，但不推荐（容易混淆） |

---

### 练习 3：`is` vs `==` 辨析

写出以下代码的输出结果：

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
print(a is not b)

x = None
print(x is None)
print(x == None)
```

**答案：**
```
True     # a 和 b 的值相等
False    # a 和 b 是不同的对象
True     # c 指向 a 的同一个对象
True     # a 和 b 不是同一个对象
True     # None 是单例，is 判断推荐
True     # x 的值等于 None
```

> **关键结论**：`is` 比较对象身份（内存地址），`==` 比较值。对 `None` 的判断，推荐使用 `is None`。

---

### 练习 4：`global` 与 `nonlocal` 的区别

写出以下代码的输出结果：

```python
x = "global"

def outer():
    x = "outer"

    def inner_nonlocal():
        nonlocal x
        x = "modified by nonlocal"

    def inner_new_local():
        x = "new local"  # 创建了全新的局部变量

    inner_nonlocal()
    print("after nonlocal:", x)

    inner_new_local()
    print("after new local:", x)

outer()
print("global x:", x)
```

**答案：**
```
after nonlocal: modified by nonlocal
after new local: modified by nonlocal
global x: global
```

解释：
- `nonlocal x` 修改了 `outer` 中的 `x`
- `inner_new_local` 中的 `x = "new local"` 创建了一个全新的局部变量，不影响外层的 `x`
- 全局的 `x` 始终未被修改

---

### 练习 5：`assert` 调试实战

以下 `assert` 语句哪些会触发 `AssertionError`？

```python
assert True
assert 1 + 1 == 2
assert len([1, 2, 3]) > 5, "列表长度不够"
assert 0, "零被视为 False"
```

**答案：**

第 3 行和第 4 行会触发 `AssertionError`：

```python
assert True              # ✅ 通过
assert 1 + 1 == 2        # ✅ 通过
assert len([1,2,3]) > 5  # ❌ AssertionError: 列表长度不够
assert 0                 # ❌ AssertionError: 零被视为 False  (0 是 false)
```

---

### 练习 6：`del` 关键字的作用

写出以下代码的输出结果：

```python
nums = [1, 2, 3, 4, 5]
del nums[2]
print(nums)

d = {'a': 1, 'b': 2, 'c': 3}
del d['b']
print(d)

x = 10
del x
#print(x)  # 这行如果取消注释会怎样？
```

**答案：**
```
[1, 2, 4, 5]
{'a': 1, 'c': 3}
```

`print(x)` 取消注释后会报 `NameError: name 'x' is not defined`，因为 `del x` 已经删除了变量 `x`。

---

### 练习 7：关键字综合判断

用 `keyword.iskeyword()` 判断以下哪些是关键字：

```python
import keyword

words = ['class', 'Class', 'def', 'define', 'pass', 'pass_', 'async', 'asynchronous']
for w in words:
    print(f"{w}: {keyword.iskeyword(w)}")
```

**答案：**
```
class: True
Class: False
def: True
define: False
pass: True
pass_: False
async: True
asynchronous: False
```

---

## 🤔 常见误区

- **误区 1**："`is` 和 `==` 是一样的。"
  - **事实**：`is` 比较的是对象身份（内存地址），`==` 比较的是值。例如 `a = [1,2,3]; b = [1,2,3]`，`a == b` 为 `True`，但 `a is b` 为 `False`。详见 [[PL-PY-001-is与==的区别]]。

- **误区 2**："关键字首字母小写就安全了。"
  - **事实**：`True` 是关键字，但 `true` 不是。虽然这在语法层面是安全的，但在代码中故意使用 `true = 1` 这种写法极度不推荐，会严重降低代码可读性。

- **误区 3**："`pass` 和 `continue` 是一样的。"
  - **事实**：`pass` 是空操作占位符，什么都不做；`continue` 会跳过本次循环剩余代码，直接进入下一次迭代。

- **误区 4**："`del` 删除的是对象本身。"
  - **事实**：`del` 删除的是变量名对对象的引用（减少引用计数），而不是直接销毁对象。对象只有在引用计数归零后才会被垃圾回收。

---

## 🔗 相关资源

- [[PY003-Python中的内置函数]] — 上一篇：Python 内置函数
- [[PY005-Python中的变量]] — 下一篇：变量
- [Python 官方文档 - 关键字](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#keywords)
- [Python 官方文档 - keyword 模块](https://docs.python.org/zh-cn/3/library/keyword.html)
