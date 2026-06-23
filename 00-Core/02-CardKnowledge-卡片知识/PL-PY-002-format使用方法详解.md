---
type: card
status: 已完成
aliases: [str.format, 字符串格式化, format method]
tags: [编程语言, Python]
created: 2026-06-22
updated: 2026-06-22
---

# Python `str.format()` 使用方法详解

## 💡 核心概念

`str.format()` 是 Python 内置的字符串格式化方法，通过在字符串中使用 `{}` 占位符，将变量按指定格式嵌入文本。它是连接旧式 `%` 格式化与现代 f-string 之间的桥梁，在 **复用模板** 和 **动态构建格式串** 场景中仍有不可替代的价值。

---

## 🔍 详细说明

### 一、基本占位符

| 用法          | 示例                                             | 输出            |
| ----------- | ---------------------------------------------- | ------------- |
| **位置参数**    | `'{0} {1}'.format('hello', 'world')`           | `hello world` |
| **省略索引**    | `'{} {}'.format('hello', 'world')`             | `hello world` |
| **关键字参数**   | `'{name} is {age}'.format(name='Bob', age=25)` | `Bob is 25`   |
| **混合使用**    | `'{0} is {age}'.format('Bob', age=25)`         | `Bob is 25`   |
| **字典解包**    | `'{name} {age}'.format(**person)`              | 按字典键展开        |
| **列表/元组索引** | `'{0[0]} {0[1]}'.format(['a', 'b'])`           | `a b`         |
| **对象属性访问**  | `'{0.name}'.format(obj)`                       | 调用 `obj.name` |

> **注意**：混合使用时，位置参数必须在关键字参数之前，且占位符不能为空 `{}`。

---

### 二、格式化规范（Format Specification Mini-Language）

完整语法：`{ [字段名] [ !转换 ] [ :格式规范 ] }`

#### 1. 对齐与填充 `[fill]align][width]`

| 符号   | 含义          | 示例 `format(3.14, …)`    | 输出（宽度 8）   |
| ---- | ----------- | ----------------------- | ---------- |
| `<`  | 左对齐         | `'{:<8}'.format(3.14)`  | `3.14    ` |
| `>`  | 右对齐（数字默认）   | `'{:>8}'.format(3.14)`  | `    3.14` |
| `^`  | 居中          | `'{:^8}'.format(3.14)`  | `  3.14  ` |
| `=`  | 符号左对齐，数字右对齐 | `'{:=8}'.format(-3.14)` | `-   3.14` |
| 填充字符 | 放在对齐符前      | `'{:*>8}'.format(3.14)` | `****3.14` |

#### 2. 数字精度与类型

| 格式 | 说明 | 示例 | 输出 |
|------|------|------|------|
| `:.2f` | 定点数，保留 2 位小数 | `'{:.2f}'.format(3.14159)` | `3.14` |
| `:.0f` | 四舍五入到整数 | `'{:.0f}'.format(3.5)` | `4` |
| `:.2%` | 百分比，保留 2 位 | `'{:.2%}'.format(0.756)` | `75.60%` |
| `:,` | 千位分隔符 | `'{:,}'.format(1000000)` | `1,000,000` |
| `:e` | 科学计数法 | `'{:e}'.format(3141.59)` | `3.141590e+03` |
| `:b` / `:o` / `:x` | 二进制/八进制/十六进制 | `'{:b}'.format(10)` | `1010` |
| `:d` | 十进制整数（截断） | `'{:d}'.format(3.9)` | `3` |

#### 3. 字符串截断

| 示例                                 | 输出           | 说明               |
| ---------------------------------- | ------------ | ---------------- |
| `'{:.5}'.format('Hello World')`    | `Hello`      | 截取前 5 个字符        |
| `'{:>10.5}'.format('Hello World')` | `     Hello` | 右对齐 10 宽，截取 5 字符 |

#### 4. 符号控制

| 格式  | 说明        | 示例                  | 输出    |
| --- | --------- | ------------------- | ----- |
| `+` | 正数也显示符号   | `'{:+}'.format(42)` | `+42` |
| `-` | 只显示负号（默认） | `'{:-}'.format(42)` | `42`  |
| 空格  | 正数前留空格    | `'{: }'.format(42)` | ` 42` |

---

### 三、`!` 转换标志

在格式规范之前，可以用 `!` 对值进行预处理：

| 标志   | 等价操作      | 示例                    | 输出     |
| ---- | --------- | --------------------- | ------ |
| `!s` | `str()`   | `'{!s}'.format(42)`   | `42`   |
| `!r` | `repr()`  | `'{!r}'.format('hi')` | `'hi'` |
| `!a` | `ascii()` | `'{!a}'.format('中文')` | `'中文'` |

---

### 四、format() 与 f-string、% 格式化对比

| 维度            | `str.format()`         | **f-string**（推荐） | `%` 格式化（旧式）        |
| ------------- | ---------------------- | ---------------- | ------------------ |
| **语法**        | `'{} {}'.format(a, b)` | `f'{a} {b}'`     | `'%s %s' % (a, b)` |
| **性能**        | 中等                     | **最快**（编译时优化）    | 较慢                 |
| **复用模板**      | ⭐⭐⭐ **最适合**            | ❌ 字符串定义时变量必须存在   | ⭐⭐ 可复用             |
| **动态字段名**     | ⭐⭐⭐ 天然支持               | ⭐⭐ 需嵌套 `{}`      | ❌ 繁琐               |
| **可读性（简单场景）** | 一般                     | ⭐⭐⭐ 最佳           | 较差                 |
| **向后兼容**      | Python 2.6+            | Python 3.6+      | Python 全版本         |

> **核心结论**：日常编码优先使用 f-string；当格式模板需要**多次复用**或**动态构建**时，使用 `str.format()`。

---

## 📎 例子

### 例子 1：位置与关键字混用

```python
# 基本位置
print('{0} + {1} = {2}'.format(1, 2, 3))    # 1 + 2 = 3

# 关键字
print('{name} scores {score:.1f}'.format(
    name='Alice', score=87.654
))  # Alice scores 87.7

# 字典解包
person = {'name': 'Bob', 'age': 30}
print('Name: {name}, Age: {age}'.format(**person))
```

### 例子 2：格式化规格嵌套

```python
# 宽度可以来自另一个变量
for i, fruit in enumerate(['apple', 'banana', 'cherry'], 1):
    print('{0}. {1:.<20}'.format(i, fruit))

# 输出：
# 1. apple...............
# 2. banana..............
# 3. cherry..............
```

### 例子 3：模板复用（format 独有的优势场景）

```python
# 定义一次模板，多次使用
template = '[{level:>8}] {timestamp} - {message}'

print(template.format(level='INFO', timestamp='10:30:01', message='Server started'))
print(template.format(level='ERROR', timestamp='10:30:05', message='Connection refused'))
# [    INFO] 10:30:01 - Server started
# [   ERROR] 10:30:05 - Connection refused
```

### 例子 4：动态列宽表格

```python
data = [('Apple', 5.5, 10), ('Watermelon', 3.0, 20)]
col_widths = [15, 8, 8]

for name, price, qty in data:
    print('{0:<{w1}} {1:>{w2}.2f} {2:>{w3}}'.format(
        name, price, qty, w1=col_widths[0], w2=col_widths[1], w3=col_widths[2]
    ))
# Apple           5.50       10
# Watermelon      3.00       20
```

### 例子 5：访问列表元素与对象属性

```python
# 列表索引
data = ['Alice', 25, 'Engineer']
print('{0[0]} is a {0[2]}, age {0[1]}'.format(data))
# Alice is a Engineer, age 25

# 对象属性
from collections import namedtuple
Person = namedtuple('Person', 'name age')
p = Person('Bob', 30)
print('{0.name} is {0.age} years old'.format(p))
# Bob is 30 years old
```

---

## ⚡ 反例 / 边界

### 边界 1：位置参数与关键字参数混用时的顺序限制

```python
# ✅ 正确：位置参数在前
'{0} {name}'.format('Hello', name='World')

# ❌ 错误：关键字在前
'{name} {0}'.format(name='World', 'Hello')
# SyntaxError: positional argument follows keyword argument
```

### 边界 2：`{}` 与索引占位符不能混用

```python
# ❌ 错误
'{0} {}'.format(1, 2)  # ValueError: cannot switch from manual to automatic field numbering

# ✅ 要么全用索引，要么全用自动
'{0} {1}'.format(1, 2)  # OK
'{} {}'.format(1, 2)    # OK
```

### 边界 3：大括号转义

```python
# 输出真正的大括号，使用双大括号
print('The set is {{{0}, {1}}}'.format(1, 2))  # The set is {1, 2}
```

### 边界 4：`:.0f` 四舍五入 vs `:d` 截断

```python
print('{:d}'.format(3.9))   # 3（和 int() 一样，直接截断）
print('{:.0f}'.format(3.9)) # 4（四舍五入）
print('{:.0f}'.format(3.5)) # 4（银行家舍入：偶数偏好）
```

### 边界 5：可变参数作为字段引用

```python
# 占位符中使用 *args 间接引用
args = ['Alice', 'Bob']
# ❌ 不能直接 '{0[0]}'.format(*args) — *args 不是列表
# ✅ 应该用
print('{0} and {1}'.format(*args))  # Alice and Bob
```

---

## 🔗 关联卡片

- [[PY008-Python中的简单数据类型]] — 字符串格式化全景对比（f-string / format / %）
- [[PL-PY-001-is与==的区别]] — 对象比较运算符

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
