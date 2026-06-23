---
type: learning
status: 已完成
domain: Python
tags: [Python, 编程语言]
created: 2026-06-12
updated: 2026-06-16
---

# Python 中的简单数据类型

## 🎯 学习目标

1. 字符串有哪些定义方式？原生字符串（r-string）和普通字符串有什么区别？
2. Python 中常用的转义序列（`\n`、`\t`、`\\`、`\uXXXX`）各自代表什么含义？
3. 字符串常用方法（split、join、strip、replace、find、startswith 等）的参数和返回值是什么？
4. Python 的三种字符串格式化方式（%、format、f-string）各有什么特点？什么场景下该用哪种？
5. 浮点数为什么会出现 `0.1 + 0.2 != 0.3` 的精度问题？如何正确处理？
6. Python 中隐式类型转换遵循什么原则？显式类型转换（int()、float()、bool()）的核心规则是什么？
7. 字符串与字节（str 与 bytes）如何互相转换？编码和解码时需要注意什么？
8. 容器类型之间转换（list → set、dict → list）会带来哪些副作用？

## 📖 前置知识

- [[PY005-Python中的变量]]、[[PY007-Python中的运算符]] — 掌握变量定义、赋值语法和基本运算符的使用

## 📚 核心内容

在 Python 编程中，数据类型是构建一切应用的基石。很多初学者常遇到的"精度丢失"、"类型错误"等问题，往往源于对数据底层机制的不了解。
本文将深入探讨 Python 中的**字符串处理艺术**、**数值运算的真相**以及**数据类型转换的完整规则与避坑指南**。

------

### 字符串

字符串是 Python 中最灵活的数据类型。它不仅是字符的序列，更是一套强大的文本处理工具。
**核心特性**：字符串是**不可变**的。调用任何方法都不会修改原字符串，而是返回一个新的字符串。

#### 1. 定义技巧

- **单/双引号**：功能等价。建议普通情况用单引号，若字符串内含单引号（如 `It's`），则使用双引号。
- **三引号 `'''` 或 `"""`**：定义多行字符串，保留换行和缩进。
- **原生字符串 `r""` **：忽略转义字符，处理正则或路径（如 `r"C:\new"`）时必备。在文件操作中，使用原生字符串定义文件路径可以避免 `\` 被误解析为转义字符，详见 [[PY016-Python中的文件]]。

#### 2. 转义序列

在字符串中，某些字符需要使用反斜杠（`\`）进行转义处理。以下是常用的转义序列：

| 转义序列 | 说明        | 示例                                                      |
| -------- | ----------- | --------------------------------------------------------- |
| `\\`     | 反斜杠      | `print("C:\\Windows")` → `C:\Windows`                     |
| `\'`     | 单引号      | `print('It\'s a beautiful day')` → `It's a beautiful day` |
| `\"`     | 双引号      | `print("He said \"Hello\"")` → `He said "Hello"`          |
| `\n`     | 换行符      | `print("Hello\nWorld")` → `Hello` `World`                 |
| `\t`     | 制表符      | `print("Name:\tAlice")` → `Name: Alice`                   |
| `\r`     | 回车符      | `print("Hello\rWorld")` → `World`（覆盖前面内容）         |
| `\b`     | 退格符      | `print("Hello\b World")` → `Hell World`                   |
| `\f`     | 换页符      | 用于分页打印                                              |
| `\ooo`   | 八进制数    | `print("\110\145\154\154\157")` → `Hello`                 |
| `\xhh`   | 十六进制数  | `print("\x48\x65\x6c\x6c\x6f")` → `Hello`                 |
| `\uXXXX` | Unicode字符 | `print("中文")` → `中文`                          |

**注意事项**：

- 在原始字符串（`r""`）中，转义序列会被当作普通字符处理
- Windows系统路径分隔符为`\`，建议使用原始字符串或双反斜杠处理路径

#### 3. 字符串常用方法详解（参数表）

为了方便查阅，核心字符串方法整理成了以下参数表格：

**查找与判断类**
这类方法通常返回布尔值（True/False）或索引位置。

| 方法               | 语法参数                                        | 说明与示例                                                                                     |
| ---------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **startswith**   | `str.startswith(prefix[, start[, end]])`    | **检查前缀**。`prefix`为必填前缀；`start/end`为可选范围。 *示例：`"https.com".startswith("https")` -> `True`* |
| **endswith**     | `str.endswith(suffix[, start[, end]])`      | **检查后缀**。常用于判断文件类型。 *示例：`"a.jpg".endswith(".jpg")` -> `True`*                             |
| **find**         | `str.find(sub[, start[, end]])`             | **查找首次出现**。返回子字符串第一次出现的索引，如果未找到则返回 **-1**（安全）。 *示例：`'python'.find('y')` -> `1`*           |
| **rfind**        | `str.rfind(sub[, start[, end]])`            | **查找最后一次出现**。返回子字符串最后一次出现的索引，如果未找到则返回 **-1**。 *示例：`'python'.rfind('n')` -> `5`*           |
| **index**        | `str.index(sub[, start[, end]])`            | **查找最小索引**。功能同 `find`，但未找到时**抛出异常**。 *示例：`'python'.index('th')` -> `2`*                   |
| **rindex**       | `str.rindex(sub[, start[, end]])`           | **查找最大索引**。返回子字符串最后一次出现的索引，未找到则报错。 *示例：`'python'.rindex('th')` -> `2`*                    |
| **count**        | `str.count(sub[, start[, end]])`            | **统计次数**。统计子字符串出现的次数。 *示例：`"hello".count("l")` -> `2`*                                    |
| **is系列**         | `str.isdigit()` / `isalpha()` / `isspace()` | **类型判断**。`isdigit`检查是否全为数字；`isalpha`检查是否全为字母；`isspace`检查是否全为空白。                           |
| **isalnum**      | `str.isalnum()`                             | **判断是否为字母数字**。如果字符串中的所有字符都是字母数字且非空，返回 `True`。 *示例：`'Days2024'.isalnum()` -> `True`*       |
| **isdecimal**    | `str.isdecimal()`                           | **判断是否为十进制数字**。检查字符串是否只包含 0-9 的 Unicode 字符。 *示例：`'123'.isdecimal()` -> `True`*            |
| **isnumeric**    | `str.isnumeric()`                           | **判断是否为广义数字**。检查字符串是否只包含数字相关字符（包括 Unicode 分数，如 `½`）。 *示例：`'½'.isnumeric()` -> `True`*     |
| **isidentifier** | `str.isidentifier()`                        | **判断是否为有效标识符**。检查字符串是否是有效的 Python 变量名。 *示例：`'days_of_code'.isidentifier()` -> `True`*     |
| **islower**      | `str.islower()`                             | **判断是否全为小写**。如果字符串中所有字母字符都是小写，返回 `True`。 *示例：`'hello'.islower()` -> `True`*               |
| **isupper**      | `str.isupper()`                             | **判断是否全为大写**。如果字符串中所有字母字符都是大写，返回 `True`。 *示例：`'HELLO'.isupper()` -> `True`*               |

**清洗与排版类**
这类方法用于格式化输出、内容替换或清理脏数据。

| 方法             | 语法参数                                  | 说明与示例                                                                                    |
| -------------- | ------------------------------------- | ---------------------------------------------------------------------------------------- |
| **strip**      | `str.strip([chars])`                  | **移除首尾字符**。删除字符串开头和结尾的所有给定字符（默认为空白符）。 *示例：`" user ".strip()` -> `"user"`*                |
| **replace**    | `str.replace(old, new[, count])`      | **替换字符**。用给定的字符串替换子字符串。`count`指定替换次数。 *示例：`"aaabbb".replace("a", "z", 1)` -> `"zaabbb"`* |
| **大小写**        | `str.lower()` / `upper()` / `title()` | **转换大小写**。`lower`全小写；`upper`全大写；`title`每个单词首字母大写。                                        |
| **capitalize** | `str.capitalize()`                    | **首字母大写**。将字符串中的第一个字符转换为大写字母，其余转为小写。 *示例：`'thirty'.capitalize()` -> `'Thirty'`*          |
| **swapcase**   | `str.swapcase()`                      | **大小写互换**。将所有大写字符转换为小写，所有小写字符转换为大写。 *示例：`'Hi'.swapcase()` -> `'hI'`*                     |
| **center**     | `str.center(width[, fillchar])`       | **居中填充**。将字符串居中，总长`width`，两边用`fillchar`填充。 *示例：`"Hi".center(10, "-")` -> `"----Hi----"`* |
| **expandtabs** | `str.expandtabs(tabsize=8)`           | **制表符转空格**。用空格替换制表符 `\t`，默认制表符大小为 8。 *示例：`'a\tb'.expandtabs(4)` -> `'a b'`*              |
| **format**     | `str.format(*args, **kwargs)`         | **格式化字符串**。将字符串格式化为更美观的输出。 *示例：`'I am {}'.format('Alice')` -> `'I am Alice'`* 。完整用法见 [[PL-PY-002-format使用方法详解]] |

**分割与合并类**
处理结构化文本的核心工具。

| 方法           | 语法参数                            | 说明与示例                                                   |
| -------------- | ----------------------------------- | ------------------------------------------------------------ |
| **split**      | `str.split(sep=None, maxsplit=-1)`  | **分割字符串**。使用给定的字符串或空格作为分隔符来拆分字符串，`maxsplit` 参数代表最大分割成几组。 *示例：`'a,b,c'.split(',')` -> `['a', 'b', 'c']`* |
| **rsplit**     | `str.rsplit(sep=None, maxsplit=-1)` | **右分割**。从右边开始分割字符串，`maxsplit` 参数代表最大分割成几组。 |
| **splitlines** | `str.splitlines(keepends=False)`    | **按行分割**。将字符串按换行符分割成列表。                   |
| **join**       | `str.join(iterable)`                | **合并序列**。**调用者是连接符**。将列表/元组合并为字符串。 *示例：`"-".join(["a", "b"])` -> `"a-b"`* |

**其他常用方法**

| 方法            | 语法参数     | 说明与示例                                                   |
| --------------- | ------------ | ------------------------------------------------------------ |
| **len()**       | `len(str)`   | **获取长度**。返回字符串的字符数。 *示例：`len("abc")` -> `3`* |
| **in / not in** | `sub in str` | **成员检测**。判断子字符串是否存在于字符串中。 *示例：`'a' in 'abc'` -> `True`* |

#### 4. 字符串格式化

字符串格式化是将变量嵌入文本模板的过程。Python 提供了多种语法，虽然 **f-string** 是现代 Python 的首选，但理解 **% 格式化** 对于维护旧代码至关重要。

> 💡 `str.format()` 的完整用法（格式化规范语言、模板复用、动态字段名等）详见卡片 [[PL-PY-002-format使用方法详解]]。

**三种格式化方式全景对比**

| 特性         | f-string (推荐)   | str.format()              | % 格式化 (旧式)       |
| ------------ | ----------------- | ------------------------- | --------------------- |
| **语法示例** | `f"Name: {name}"` | `"Name: {}".format(name)` | `"Name: %s" % name`   |
| **性能**     | ⭐⭐⭐ (最快)        | ⭐⭐ (中等)                 | ⭐ (较慢)              |
| **可读性**   | 极佳 (代码即结果) | 良好                      | 一般 (需查表)         |
| **适用场景** | **所有新项目**    | 复杂逻辑或旧版本兼容      | 维护老代码 / 简单脚本 |

**核心格式化符号：统一速查表**

无论是 f-string 还是 % 格式化，核心都在于**控制数据的显示形态**。为了方便记忆，我将符号分为**通用布局**和**数据形态**两类。

**1. 通用布局与对齐 (适用于 f-string 和 format)**

| 符号        | 含义     | 代码示例         | 输出结果 (框内为10字符宽) |
| ----------- | -------- | ---------------- | ------------------------- |
| **`<10`**   | 左对齐   | `f"{'Hi':<10}"`  | `'Hi        '`            |
| **`>10`**   | 右对齐   | `f"{'Hi':>10}"`  | `'        Hi'`            |
| **`^10`**   | 居中对齐 | `f"{'Hi':^10}"`  | `'    Hi    '`            |
| **`:*<10`** | 指定填充 | `f"{'Hi':*<10}"` | `'Hi********'`            |
| **`+`**     | 显正负号 | `f"{5:+}"`       | `+5`                      |

**2. 数据形态与精度 (f-string vs % 符号对照)**

> **避坑提示**：`%d` 会直接**截断**浮点数而非四舍五入，而 `:.0f` 会进行四舍五入。

| 需求            | f-string / format 语法 | % 格式化语法   | 示例 (值: 3.1415)                     | 结果        |
| --------------- | ---------------------- | -------------- | ------------------------------------- | ----------- |
| **字符串通配**  | `{value}`              | `%s`           | `f"{name}"` / `"%s" % name`           | 原样输出    |
| **整数 (截断)** | `{value:d}`            | `%d`           | `f"{3.9:d}"` / `"%d" % 3.9`           | `3`         |
| **浮点数**      | `{value:.2f}`          | `%f`           | `f"{3.1415:.2f}"` / `"%.2f" % 3.1415` | `3.14`      |
| **百分比**      | `{value:.0%}`          | *(需手动计算)* | `f"{0.85:.0%}"`                       | `85%`       |
| **千位分隔**    | `{value:,}`            | *(不支持)*     | `f"{1000000:,}"`                      | `1,000,000` |
| **二进制**      | `{value:b}`            | *(不支持)*     | `f"{10:b}"`                           | `1010`      |
| **十六进制**    | `{value:x}`            | `%x`           | `f"{255:x}"` / `"%x" % 255`           | `ff`        |


#### 5. 字符串编码与解码

Python 3 中，`str` 默认存储 Unicode 字符，通过 `encode()` 转为 `bytes`（编码），通过 `decode()` 转回 `str`（解码）。

```python
text = "你好，世界！"
b = text.encode('utf-8')    # str → bytes
text = b.decode('utf-8')    # bytes → str（编解码必须一致，否则乱码）
```

> ⚠️ 读写文件时务必显式指定 `encoding='utf-8'`，Windows 系统默认编码可能是 GBK，不指定会导致乱码。

> 💡 **深入阅读**：字符编码是跨语言的通用知识。关于 Unicode 与 UTF-8/UTF-16/GBK 的关系、BOM、各语言（Python/Java/Go/JS）编码 API 以及乱码排查，详见 [[PL-002-字符编码与乱码问题]]。

------

### 数值

Python 中的数字主要分为整数（`int`）和浮点数（`float`）。

#### 1. 算术运算的细节

- **除法 `/`**：结果**总是浮点数**。例如 `4 / 2` 的结果是 `2.0`。
- **地板除 `//`**：结果向下取整（向负无穷方向）。例如 `-7 // 2` 结果是 `-4`。

#### 2. 浮点数的精度陷阱

你可能遇到过 `0.1 + 0.2 != 0.3` 的情况。这并非 Python 的 Bug，而是计算机**二进制存储机制**的通病。

- **原因**：十进制的 `0.1` 在二进制中是无限循环的，计算机只能截取有限位数。

```python
# 精度问题演示
print(0.1 + 0.2) # 输出: 0.30000000000000004

# 解决方案
from decimal import Decimal
# 1. 金融计算使用 decimal 模块 (精确十进制)
print(Decimal('0.1') + Decimal('0.2')) # 输出: 0.3

# 2. 一般比较使用范围判断
a, b = 0.1 + 0.2, 0.3
print(abs(a - b) < 1e-9) # 输出: True
```

------

### 数据类型转换

这是本文的重点部分。理解转换的**规则**（系统如何自动处理）和**避坑**（手动处理的陷阱）同样重要。

#### 核心转换规则速查表

Python 的数据类型转换分为**隐式**（自动）和**显式**（手动）。为了方便记忆，我整理了以下核心规则表：

| 转换类型          | 转换方向/函数                                 | 核心规则说明                                                                   | 典型代码示例                                             |
| ------------- | --------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------- |
| **隐式转换**(自动)  | `int` → `float` `float`→ `complex`      | **"就高不就低"原则**。 为了防止数据丢失，Python 会将低精度类型自动转换为高精度类型参与运算。                    | `result = 3 + 4.5` 结果：`7.5`(float)                 |
| **显式转换**(数值)  | `int(x)`                                | **截断原则**。 直接丢弃小数部分，**不是**四舍五入。                                           | `int(3.9)` → `3` `int(-3.9)` → `-3`                |
| **显式转换**(数值)  | `float(x)`                              | **补零原则**。 整数转浮点数自动补 `.0`。                                                | `float(5)` → `5.0`                                 |
| **显式转换**(字符串) | `int(str)` `float(str)`                 | **严格匹配原则**。 字符串必须是合法的数字格式，不能包含空格或非数字字符（除非是科学计数法）。                        | `int("123")` → `123` (✅)  `int("123.0")` → 报错 (❌)  |
| **显式转换**(布尔)  | `bool(x)`                               | **"非空即真"原则**。 只有 `0`, `None`, `""` (空串), `[]` (空列表) 等代表"空"的值才转为 `False`。 | `bool(0)` → `False` `bool("0")` → `True` (⚠️坑)     |
| **显式转换**(容器)  | `list()` / `tuple()` `set()` / `dict()` | **结构重组原则**。 `set` 会自动去重且乱序；`dict` 转列表默认只取键。                              | `set([1,2,2])` → `{1, 2}` `list({"a":1})`→ `['a']` |


## 🧪 练习 / 验证

### 练习 1：字符串方法综合运用

给定字符串 `s = " Python Programming 101 "`，写出以下操作的结果：

```python
s = "  Python Programming 101  "

# (1) 去除首尾空格
print(repr(s.strip()))
# 答案: 'Python Programming 101'

# (2) 全部转为小写
print(s.lower())
# 答案: '  python programming 101  '

# (3) 判断是否以数字结尾
print(s.strip().endswith("101"))
# 答案: True

# (4) 将 "Programming" 替换为 "Coding"
print(s.replace("Programming", "Coding"))
# 答案: '  Python Coding 101  '

# (5) 统计字母 'o' 出现的次数
print(s.count('o'))
# 答案: 2

# (6) 查找子串 "101" 第一次出现的位置
print(s.find("101"))
# 答案: 22
```

### 练习 2：split 与 join 的配合

将以下 CSV 格式字符串解析后重新组装：

```python
csv_line = "Alice,25,Engineer,Shanghai"

# (1) 按逗号分割
fields = csv_line.split(",")
print(fields)
# 答案: ['Alice', '25', 'Engineer', 'Shanghai']

# (2) 用 " | " 连接所有字段
print(" | ".join(fields))
# 答案: 'Alice | 25 | Engineer | Shanghai'

# (3) 只分割前两个逗号（maxsplit=2）
print(csv_line.split(",", 2))
# 答案: ['Alice', '25', 'Engineer,Shanghai']
```

### 练习 3：f-string 格式化实战

写出以下代码的输出结果：

```python
name = "Bob"
score = 87.6543
total = 1500000

# (1) 保留两位小数
print(f"{name} 的分数是 {score:.2f}")
# 答案: 'Bob 的分数是 87.65'

# (2) 右对齐，宽度 10，保留 1 位小数
print(f"{score:>10.1f}")
# 答案: '      87.7'

# (3) 千位分隔符 + 两位小数
print(f"总金额：¥{total:,.2f}")
# 答案: '总金额：¥1,500,000.00'

# (4) 百分比格式
print(f"完成率：{0.756:.1%}")
# 答案: '完成率：75.6%'

# (5) 居中填充，宽度 20，填充字符为 '='
print(f"{' RESULT ':=^20}")
# 答案: '====== RESULT ======'
```

### 练习 4：浮点数精度问题

判断以下代码的输出，并解释原因：

```python
# (1) 精度比较
a = 0.1 + 0.2
b = 0.3
print(a == b)
# 答案: False
# 原因: 0.1 和 0.2 在二进制中是无限循环小数，存储时被截断，
#       0.1 + 0.2 的实际值为 0.30000000000000004

# (2) 安全比较方式
print(abs(a - b) < 1e-9)
# 答案: True
# 原因: 使用容差范围判断，两者差值小于 1e-9 即视为相等

# (3) 使用 Decimal 精确计算
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))
# 答案: True
# 原因: Decimal 使用十进制存储，避免了二进制转换误差

# (4) 地板除的负值行为
print(-7 // 2)
# 答案: -4
# 原因: // 是向下取整（向负无穷方向），-3.5 向下取整为 -4

# (5) 普通除法的结果类型
print(type(4 / 2))
# 答案: <class 'float'>
# 原因: Python 中 / 除法始终返回浮点数，即使能整除
```

### 练习 5：类型转换规则判断

写出以下每行代码的结果或报错原因：

```python
# (1) 隐式转换
print(type(3 + 4.5))
# 答案: <class 'float'>
# 说明: int + float → float（就高不就低原则）

# (2) int() 截断
print(int(3.9))
print(int(-3.9))
# 答案: 3  和  -3
# 说明: int() 直接截断小数部分，不四舍五入

# (3) 字符串转 int 的严格限制
# print(int("123.0"))  # 这行会报错！
# 答案: ValueError: invalid literal for int() with base 10: '123.0'
# 正确做法: int(float("123.0")) → 123

# (4) bool() 的"非空即真"
print(bool(0))       # 答案: False
print(bool(""))      # 答案: False
print(bool("0"))     # 答案: True （非空字符串为真！）
print(bool(" "))     # 答案: True （空格也是字符！）
print(bool([]))      # 答案: False
print(bool([0]))     # 答案: True （非空列表为真！）
```

### 练习 6：字符串编码与解码

```python
# (1) 编码
text = "Hello 中文"
encoded = text.encode("utf-8")
print(type(encoded))
# 答案: <class 'bytes'>
print(encoded)
# 答案: b'Hello \xe4\xb8\xad\xe6\x96\x87'

# (2) 字节长度 vs 字符长度
print(len(text))          # 字符数
print(len(encoded))       # 字节数
# 答案: 8 和 14
# 说明: "Hello " = 6 字符 = 6 字节（ASCII），"中文" = 2 字符 = 6 字节（UTF-8 每汉字 3 字节）
#       总共 8 字符，14 字节

# (3) 解码
decoded = encoded.decode("utf-8")
print(decoded)
# 答案: 'Hello 中文'

# (4) 解码时编码不匹配会怎样？
# 如果用 GBK 解码 UTF-8 编码的中文，会出现乱码：
# wrong = encoded.decode("gbk")  # 可能乱码或报错
```

### 练习 7：容器类型转换的副作用

```python
# (1) List → Set：去重但丢失顺序
data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique = set(data)
print(type(unique))
# 答案: <class 'set'>
print(len(unique))
# 答案: 7 （去除了重复的 1 和 5）
# 注意：set 的输出顺序不保证，可能是 {1, 2, 3, 4, 5, 6, 9}

# (2) Dict → List：默认只取键
person = {"name": "Alice", "age": 30, "city": "Beijing"}
keys = list(person)
values = list(person.values())
items = list(person.items())
print(keys)
# 答案: ['name', 'age', 'city']
print(values)
# 答案: ['Alice', 30, 'Beijing']
print(items)
# 答案: [('name', 'Alice'), ('age', 30), ('city', 'Beijing')]

# (3) Set → List：恢复顺序不可靠
unique_list = list(unique)
print(type(unique_list))
# 答案: <class 'list'>
# 但顺序可能不是原始的 [3, 1, 4, 5, 9, 2, 6]
```

### 练习 8：综合实战 —— 日志解析器

编写代码解析以下日志行，提取关键信息并格式化输出：

```python
log = '[2026-06-16 14:32:05] ERROR: database connection timeout (retry 3/5) server=db-01'

# (1) 提取时间戳（方括号内的内容）
start = log.find('[') + 1
end = log.find(']')
timestamp = log[start:end]
print(timestamp)
# 答案: '2026-06-16 14:32:05'

# (2) 提取日志级别（] 之后、: 之前的部分）
level_start = log.find('] ') + 2
level_end = log.find(':')
level = log[level_start:level_end]
print(level)
# 答案: 'ERROR'

# (3) 提取服务器名（等号后面的部分）
server_start = log.find('server=') + len('server=')
server = log[server_start:]
print(server)
# 答案: 'db-01'

# (4) 格式化输出
print(f"[{timestamp}] [{level}] on {server}")
# 答案: '[2026-06-16 14:32:05] [ERROR] on db-01'

# (5) 判断是否为 ERROR 级别
is_error = log.split(']')[1].strip().startswith('ERROR')
print(is_error)
# 答案: True
```

### 练习 9：f-string 格式化实战 —— 财务对账单

**题目**：使用 f-string 的对齐、精度和千位分隔符，编写代码打印以下格式的财务对账单：

```python
items = [
  ('苹果', 5.5, 10),
  ('笔记本电脑', 9999.99, 1)
]

# 补全以下代码，使输出对齐美观
print(f"{'商品':<10} {'单价':>10} {'数量':>5} {'总价':>12}")
print("-" * 40)

for name, price, qty in items:
    total = price * qty
    # 你的代码：格式化输出每行数据
```

**答案：**

```python
items = [
  ('苹果', 5.5, 10),
  ('笔记本电脑', 9999.99, 1)
]

print(f"{'商品':<10} {'单价':>10} {'数量':>5} {'总价':>12}")
print("-" * 40)

for name, price, qty in items:
    total = price * qty
    print(f"{name:<10} {price:>10.2f} {qty:>5} {total:>12,.2f}")
```

**输出：**
```
商品            单价     数量         总价
----------------------------------------
苹果            5.50       10        55.00
笔记本电脑  9999.99        1     9,999.99
```

**说明**：`<10` 左对齐(10宽)，`>10` 右对齐(10宽)，`>12,.2f` 右对齐(12宽)+千位分隔符+2位小数。

---

### 练习 10：f-string 格式化实战 —— 进度监控

**题目**：使用 f-string 的动态宽度填充，编写一个 `print_progress(iteration, total)` 函数，实现如下进度条效果。调用 `print_progress(3, 4)` 应输出 `[===============     ] 75%`。

```python
def print_progress(iteration, total):
    percent = iteration / total
    # 你的代码：用 f-string 实现进度条

print_progress(3, 4)
```

**答案：**

```python
def print_progress(iteration, total):
    percent = iteration / total
    # 动态生成 "=" 的数量，<20 左对齐填充空格至 20 宽
    bar = f"[{'=' * int(percent * 20):<20}] {percent:.0%}"
    print(bar)

print_progress(3, 4)
# 输出: [===============     ] 75%
```

**说明**：`'=' * int(percent * 20)` 按比例生成等号，`:<20` 左对齐并用空格填满 20 字符宽度，`:.0%` 将小数格式化为百分比（如 `0.75` → `75%`）。

---

### 练习 11：数值转换中的"截断"与"四舍五入"

**题目**：写出以下代码的输出，并解释 `int()` 与 `round()` 的行为差异。

```python
# (1) int() 截断
print(int(3.9))
print(int(-3.9))

# (2) round() 四舍五入
print(round(3.9))
print(round(3.5))
```

**答案：**

```
3
-3
4
4
```

**解释**：
- `int()` 直接**截断**小数部分，不做四舍五入。`int(3.9)` → `3`，`int(-3.9)` → `-3`。
- `round()` 使用**银行家舍入法**（四舍六入五成双），`round(3.9)` → `4`，`round(3.5)` → `4`（3.5 舍入到最近的偶数 4）。

---

### 练习 12：字符串转数字的严格限制

**题目**：以下代码中 `int("123.0")` 会报错吗？如果会，写出正确的转换方式，使结果输出 `123`。

```python
data = "123.0"
# num = int(data)         # 这行会报错吗？为什么？
# 你的正确转换代码：
```

**答案：**

```python
data = "123.0"
# num = int(data)         # ❌ ValueError: invalid literal for int() with base 10: '123.0'
num = int(float(data))    # ✅ 先转 float 再转 int
print(num)                # 输出: 123
```

**解释**：`int()` 要求字符串是纯整数格式（如 `"123"`），不能包含小数点。带小数点的字符串需要先 `float()` 转为浮点数，再 `int()` 截断取整。

---

### 练习 13：布尔值的"真假"陷阱

**题目**：写出以下代码的输出，并解释为什么 `"0"` 和 `" "` 在 `if` 判断中不是 `False`。

```python
# (1) 常见误区
if "0": 
    print("A")
if " ": 
    print("B")
if "":
    print("C")

# (2) 正确做法：如果判断用户是否输入了 0
user_input = "0"
if user_input == "0":
    print("D")
```

**答案：**

```
A
B
D
```

**解释**：Python 的布尔判断遵循**「非空即真」**原则：
- `"0"` → `True`（字符串有内容，哪怕内容是字符 `0`）
- `" "` → `True`（空格也是字符，非空）
- `""` → `False`（只有空字符串才是 `False`）
- `"0" == "0"` → `True`，所以 D 也会打印

如果需要判断用户输入是否为数值 0，必须显式转换再比较：`int(user_input) == 0`。

---

### 练习 14：容器转换的副作用

**题目**：写出以下代码的输出，并说明 List→Set 和 Dict→List 转换各自丢失了什么信息。

```python
# (1) List → Set
ids = [1, 2, 3, 2, 1]
unique_ids = set(ids)
print(unique_ids)

# (2) Dict → List
user = {"name": "Alice", "age": 25}
keys = list(user)
values = list(user.values())
print(keys)
print(values)
```

**答案：**

```
{1, 2, 3}
['name', 'age']
['Alice', 25]
```

**关键副作用**：
- **List → Set**：丢失**顺序**和**重复元素**。`[1, 2, 3, 2, 1]` 变成 `{1, 2, 3}`，顺序不保证。
- **Dict → List**：`list(dict)` 默认只取**键**，值被忽略。需要值用 `.values()`，需要键值对用 `.items()`（返回 `[('name', 'Alice'), ('age', 25)]`）。

## 🤔 常见误区

### 误区 1：以为 `int()` 会四舍五入

**错误认知**：`int(3.9)` 结果是 `4`。
**事实**：`int()` 直接截断小数部分，`int(3.9)` 结果是 `3`，`int(-3.9)` 结果是 `-3`。需要四舍五入请使用 `round()`。

### 误区 2：以为字符串 `"0"` 或 `" "` 是 `False`

**错误认知**：在 `if` 判断中，`"0"` 或 `" "`（空格）会被当作 `False` 处理。
**事实**：Python 遵循"非空即真"原则。**任何非空字符串**在布尔上下文中都是 `True`，包括 `"0"`、`" "`、`"False"` 等。只有空字符串 `""` 才是 `False`。

### 误区 3：尝试直接修改字符串中的某个字符

**错误认知**：`s = "hello"; s[0] = "H"` 可以将首字符改为大写。
**事实**：Python 字符串是**不可变**的，上诉操作会抛出 `TypeError`。正确做法是创建新字符串：`s = "H" + s[1:]` 或使用 `s.capitalize()`。

### 误区 4：用 `==` 直接比较浮点数

**错误认知**：`0.1 + 0.2 == 0.3` 结果为 `True`。
**事实**：由于二进制浮点精度问题，结果为 `False`。金融计算应使用 `Decimal`，一般比较应使用容差范围 `abs(a - b) < 1e-9`。

### 误区 5：忘记显式指定文件编码导致 Windows 上乱码

**错误认知**：`open('file.txt')` 在所有系统上默认使用 UTF-8。
**事实**：Windows 系统默认编码可能是 GBK。读取 UTF-8 文件时应显式指定 `open('file.txt', encoding='utf-8')`。

## 🔗 相关资源

- **上一节**：[[PY007-Python中的运算符]]
- **下一节**：[[PY009-Python中的列表]]
- **官方文档**：[Python 字符串方法](https://docs.python.org/zh-cn/3/library/stdtypes.html#string-methods) | [Python 浮点运算](https://docs.python.org/zh-cn/3/tutorial/floatingpoint.html) | [Python 内置类型](https://docs.python.org/zh-cn/3/library/stdtypes.html)
