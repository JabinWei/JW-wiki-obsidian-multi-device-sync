---
type: learning
status: 已完成
domain: Python
tags: [Python, 编程语言]
created: 2026-06-12
updated: 2026-06-16
---

# PY018 Python中的正则表达式

## 🎯 学习目标

- 什么是正则表达式，它在 Python 中通过哪个模块来使用？
- `re.search()`、`re.match()`、`re.findall()` 和 `re.sub()` 分别有什么作用，有什么区别？
- 元字符 `.` `*` `+` `?` `^` `$` `[]` `|` `()` 各自匹配什么？
- 如何在正则表达式中定义字符类（character class）和否定字符类？
- 捕获组（capturing groups）和非捕获组有什么不同，如何使用 `group()` 取出匹配结果？
- 贪婪匹配（greedy）与非贪婪匹配（lazy）的区别是什么，如何切换？
- 什么时候应该使用 `re.compile()` 预编译正则表达式？
- 常用的模式修饰符（flags）如 `re.IGNORECASE`、`re.DOTALL`、`re.MULTILINE` 各有什么作用？

## 📖 前置知识

[[PY019-Python中错误类型与异常处理机制|PY019-Python中错误类型与异常处理机制]]

## 📚 核心内容

正则表达式（Regular Expression，简称 regex 或 RE）是一种用来描述、匹配字符串模式的强大工具。Python 通过内置的 `re` 模块提供对正则表达式的全面支持。

---

### re 模块概览

`re` 模块是 Python 标准库的一部分，使用前需要 `import re`。它提供了两大类使用方式：

1. **模块级函数**：直接调用 `re.search()`、`re.match()` 等，适合一次性匹配。
2. **预编译对象**：通过 `re.compile()` 将模式编译为正则对象，适合多次复用同一模式，效率更高。

---

### 核心匹配函数

#### re.search(pattern, string, flags=0)

扫描整个字符串，返回**第一个**匹配的 match 对象；没有匹配则返回 `None`。

```python
import re

result = re.search(r'\d+', 'abc123def456')
print(result.group())  # 123（只返回第一个匹配）
```

#### re.match(pattern, string, flags=0)

从字符串**开头**开始匹配。如果开头不匹配，直接返回 `None`。

```python
print(re.match(r'\d+', '123abc'))   # <re.Match object> → 123
print(re.match(r'\d+', 'abc123'))   # None（开头不是数字）
```

#### re.findall(pattern, string, flags=0)

返回所有非重叠匹配的**列表**。如果模式中包含捕获组，则返回元组列表。

```python
print(re.findall(r'\d+', 'abc123def456'))  # ['123', '456']
```

#### re.finditer(pattern, string, flags=0)

返回一个迭代器，逐个产生 match 对象。适合处理大量匹配结果，节省内存。

```python
for m in re.finditer(r'\d+', 'abc123def456'):
    print(m.group(), m.span())
# 123 (3, 6)
# 456 (9, 12)
```

#### re.sub(pattern, repl, string, count=0, flags=0)

替换匹配内容。`repl` 可以是字符串或函数；`count` 控制最大替换次数（0 表示全部替换）。

```python
print(re.sub(r'\d+', 'NUM', 'a1b2c3'))      # aNUMbNUMcNUM
print(re.sub(r'\d+', 'NUM', 'a1b2c3', 2))   # aNUMbNUMc3
```

#### re.split(pattern, string, maxsplit=0, flags=0)

按模式分割字符串，返回列表。

```python
print(re.split(r'[,;]', 'a,b;c,d'))  # ['a', 'b', 'c', 'd']
```

---

### 常用元字符（Metacharacters）

| 元字符 | 含义 | 示例 |
|--------|------|------|
| `.` | 匹配任意单个字符（除换行符） | `a.c` 匹配 `abc`、`a3c` |
| `*` | 前一个字符出现 0 次或多次（贪婪） | `ab*c` 匹配 `ac`、`abbc` |
| `+` | 前一个字符出现 1 次或多次（贪婪） | `ab+c` 匹配 `abc`、`abbc`，不匹配 `ac` |
| `?` | 前一个字符出现 0 次或 1 次（贪婪） | `ab?c` 匹配 `ac`、`abc` |
| `^` | 匹配字符串开头 | `^abc` 匹配以 `abc` 开头的字符串 |
| `$` | 匹配字符串结尾 | `abc$` 匹配以 `abc` 结尾的字符串 |
| `[]` | 字符类，匹配方括号内任意字符 | `[aeiou]` 匹配任意元音字母 |
| `[^]` | 否定字符类，匹配不在方括号内的字符 | `[^0-9]` 匹配任意非数字字符 |
| `|` | 或（alternation） | `cat|dog` 匹配 `cat` 或 `dog` |
| `()` | 捕获组 | `(ab)+` 匹配 `ab`、`abab` |
| `\` | 转义字符 | `\.` 匹配字面句号 |

#### 重复限定符的扩展

| 语法 | 含义 |
|------|------|
| `{n}` | 精确匹配 n 次 |
| `{n,}` | 匹配至少 n 次 |
| `{n,m}` | 匹配 n 到 m 次 |

```python
print(re.findall(r'\d{3}', '12 345 6789'))     # ['345', '678']
print(re.findall(r'\d{2,4}', '1 23 456 7890')) # ['23', '456', '7890']
```

---

### 预定义字符类（Shorthand Character Classes）

| 简写 | 等价于 | 说明 |
|------|--------|------|
| `\d` | `[0-9]` | 数字 |
| `\D` | `[^0-9]` | 非数字 |
| `\w` | `[a-zA-Z0-9_]` | 单词字符（字母、数字、下划线） |
| `\W` | `[^a-zA-Z0-9_]` | 非单词字符 |
| `\s` | `[ \t\n\r\f\v]` | 空白字符 |
| `\S` | `[^ \t\n\r\f\v]` | 非空白字符 |
| `\b` | — | 单词边界（不消耗字符） |
| `\B` | — | 非单词边界 |

```python
print(re.findall(r'\w+', 'hello world_123!'))  # ['hello', 'world_123']
print(re.findall(r'\bcat\b', 'cat catalog cat')) # ['cat', 'cat'] — 只匹配独立单词
```

---

### 贪婪匹配 vs 非贪婪匹配

默认情况下，`*`、`+`、`?` 和 `{}` 都是**贪婪**的，即尽可能多地匹配。在它们后面加上 `?` 即可切换为**非贪婪（lazy）** 模式，尽可能少地匹配。

```python
text = '<h1>Title</h1><p>Body</p>'

# 贪婪：匹配从第一个 < 到最后一个 > 之间的所有内容
print(re.findall(r'<.*>', text))
# ['<h1>Title</h1><p>Body</p>']

# 非贪婪：逐个匹配最短的标签
print(re.findall(r'<.*?>', text))
# ['<h1>', '</h1>', '<p>', '</p>']
```

---

### 捕获组（Capturing Groups）

括号 `()` 除了用于分组和优先级控制外，还会**捕获**匹配的内容，可以通过 `group()` 方法取出。

```python
pattern = r'(\d{3})-(\d{4})-(\d{4})'
text = '电话：010-1234-5678'
m = re.search(pattern, text)
if m:
    print(m.group())    # 010-1234-5678（完整匹配）
    print(m.group(1))   # 010
    print(m.group(2))   # 1234
    print(m.group(3))   # 5678
    print(m.groups())   # ('010', '1234', '5678')
```

#### 命名捕获组

```python
pattern = r'(?P<area>\d{3})-(?P<first>\d{4})-(?P<second>\d{4})'
m = re.search(pattern, '010-1234-5678')
print(m.group('area'))     # 010
print(m.groupdict())       # {'area': '010', 'first': '1234', 'second': '5678'}
```

#### 非捕获组

在左括号后加 `?:` 表示该组仅用于分组逻辑，不捕获内容：

```python
pattern = r'(?:Mr|Ms|Mrs)\. (\w+)'
m = re.search(pattern, 'Mr. Smith')
print(m.group(1))  # Smith（只有姓名被捕获）
```

#### 反向引用

用 `\1`、`\2` 等引用前面捕获组的内容：

```python
# 查找重复单词
print(re.findall(r'\b(\w+)\s+\1\b', 'the the cat sat sat down'))
# ['the', 'sat']
```

---

### 常用模式修饰符（Flags）

修饰符可以改变正则表达式的行为。多个标志可以用 `|` 组合。

| Flag | 说明 |
|------|------|
| `re.IGNORECASE` / `re.I` | 忽略大小写 |
| `re.MULTILINE` / `re.M` | `^` 和 `$` 匹配每行的开头和结尾 |
| `re.DOTALL` / `re.S` | `.` 匹配包括换行符在内的任意字符 |
| `re.VERBOSE` / `re.X` | 允许在模式中写注释，忽略空白 |

```python
# re.IGNORECASE
print(re.findall(r'python', 'Python PYTHON python', re.I))
# ['Python', 'PYTHON', 'python']

# re.MULTILINE
text = 'first line\nsecond line'
print(re.findall(r'^\w+', text, re.M))
# ['first', 'second']

# re.DOTALL
html = '<div>\n  content\n</div>'
print(re.search(r'<div>.*</div>', html, re.S).group())
# <div>\n  content\n</div>

# re.VERBOSE — 写复杂正则时的最佳实践
pattern = re.compile(r'''
    (\d{4})    # 年
    -          # 分隔符
    (\d{2})    # 月
    -          # 分隔符
    (\d{2})    # 日
''', re.VERBOSE)
m = pattern.search('日期：2026-06-16')
print(m.groups())  # ('2026', '06', '16')
```

---

### re.compile() 预编译

当同一个正则表达式需要多次使用时，先用 `re.compile()` 编译成正则对象，可以显著提升性能并提高代码可读性。

```python
pattern = re.compile(r'\d+')
print(pattern.findall('a1b2c3'))        # ['1', '2', '3']
print(pattern.sub('X', 'a1b2c3'))       # aXbXcX
```

---

### Match 对象的常用方法

| 方法 | 返回值 | 说明 |
|------|--------|------|
| `group()` | str | 返回匹配的字符串（可指定组号） |
| `groups()` | tuple | 返回所有捕获组的元组 |
| `groupdict()` | dict | 返回命名捕获组的字典 |
| `start()` | int | 匹配的起始索引 |
| `end()` | int | 匹配的结束索引 |
| `span()` | tuple | 返回 (start, end) |

```python
m = re.search(r'(\w+)@(\w+\.\w+)', 'Email: alice@example.com')
print(m.span())    # (7, 24)
print(m.group(1))  # alice
print(m.group(2))  # example.com
```

---

### 实用常见场景与模式

**验证邮箱：**
```python
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
print(bool(re.match(email_pattern, 'user@example.com')))  # True
```

**提取 URL：**
```python
url_pattern = r'https?://[^\s]+'
text = 'Visit https://www.python.org or http://example.com'
print(re.findall(url_pattern, text))
# ['https://www.python.org', 'http://example.com']
```

**中文匹配：**
```python
print(re.findall(r'[一-鿿]+', 'Hello 世界 Python 中文'))
# ['世界', '中文']
```

**密码强度校验（至少 8 位，含大小写字母和数字）：**
```python
pwd_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
print(bool(re.match(pwd_pattern, 'Abc12345')))  # True
print(bool(re.match(pwd_pattern, 'abc12345')))  # False（缺少大写）
```

---

## 🧪 练习 / 验证

### 练习 1：提取所有数字

编写代码提取字符串中的所有数字（包括整数和小数）。

```python
import re

text = '价格：19.99元，数量：3件，折扣：0.85'
# 提示：小数点的 . 需要转义 \.
pattern = r'\d+\.?\d*'
result = re.findall(pattern, text)
print(result)
```

**预期输出：**
```
['19.99', '3', '0.85']
```

---

### 练习 2：验证手机号码

编写函数判断一个字符串是否为合法的中国大陆手机号码（1 开头，第二位 3-9，共 11 位数字）。

```python
import re

def is_valid_phone(phone):
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))

# 测试
print(is_valid_phone('13812345678'))   # 预期：True
print(is_valid_phone('12345678901'))   # 预期：False（第二位不是 3-9）
print(is_valid_phone('1381234567'))    # 预期：False（只有 10 位）
print(is_valid_phone('138123456789'))  # 预期：False（12 位）
```

**预期输出：**
```
True
False
False
False
```

---

### 练习 3：替换敏感信息

将文本中所有 18 位身份证号的第 7 到 14 位（出生日期）替换为 `********`。

```python
import re

text = '张三的身份证号是110101199001011234，李四的是320106198512153456。'

def mask_id(text):
    # 匹配 18 位身份证号，捕获前 6 位和后 4 位
    pattern = r'(\d{6})\d{8}(\d{4})'
    return re.sub(pattern, r'\1********\2', text)

print(mask_id(text))
```

**预期输出：**
```
张三的身份证号是110101********1234，李四的是320106********3456。
```

---

### 练习 4：解析日志行

从 Apache/Nginx 日志行中提取 IP 地址、时间和请求路径。

```python
import re

log = '192.168.1.100 - - [16/Jun/2026:10:30:45 +0800] "GET /api/users HTTP/1.1" 200 1234'
pattern = r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\].*?"\w+ (.*?) HTTP'

m = re.search(pattern, log)
if m:
    ip = m.group(1)
    time = m.group(2)
    path = m.group(3)
    print(f'IP: {ip}')
    print(f'Time: {time}')
    print(f'Path: {path}')
```

**预期输出：**
```
IP: 192.168.1.100
Time: 16/Jun/2026:10:30:45 +0800
Path: /api/users
```

---

### 练习 5：查找重复单词

找出文本中所有相邻出现的重复单词（不区分大小写）。

```python
import re

text = 'The the cat sat on on the mat mat.'
# 使用反向引用 \1 并用 re.IGNORECASE 忽略大小写
duplicates = re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE)
print(duplicates)
```

**预期输出：**
```
['The', 'on', 'mat']
```

---

### 练习 6：驼峰命名转下划线命名

编写函数将 `camelCase` 或 `PascalCase` 转为 `snake_case`。

```python
import re

def camel_to_snake(name):
    # 在大写字母前插入下划线，再整体转小写
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# 测试
print(camel_to_snake('camelCase'))      # 预期：camel_case
print(camel_to_snake('getHTTPResponse')) # 预期：get_http_response
print(camel_to_snake('UserID'))         # 预期：user_id
```

**预期输出：**
```
camel_case
get_http_response
user_id
```

---

### 练习 7：提取 HTML 标签之间的文本

从 HTML 片段中提取所有 `<a>` 标签的链接文本和 URL。

```python
import re

html = '<a href="https://google.com">Google</a> <a href="https://github.com">GitHub</a>'

pattern = r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>'
links = re.findall(pattern, html)

for url, text in links:
    print(f'{text} -> {url}')
```

**预期输出：**
```
Google -> https://google.com
GitHub -> https://github.com
```

---

### 练习 8：用 re.sub 的函数参数实现智能替换

将字符串中的所有数字乘以 2 后替换回去。

```python
import re

text = 'apple 3, banana 5, cherry 10'

def double(match):
    """将匹配到的数字字符串转为整数，乘以 2，再转回字符串"""
    num = int(match.group())
    return str(num * 2)

result = re.sub(r'\d+', double, text)
print(result)
```

**预期输出：**
```
apple 6, banana 10, cherry 20
```

---

## 🤔 常见误区

1. **误区：`re.match()` 会搜索整个字符串**
   **事实**：`re.match()` 仅在字符串**开头**进行匹配。要在任意位置搜索，应使用 `re.search()`。很多初学者误以为 `re.match()` 能在整个字符串中找到模式，这是错误的。

2. **误区：`.` 匹配包括换行符在内的所有字符**
   **事实**：默认情况下，`.` 不匹配换行符 `\n`。如果需要匹配所有字符（包括换行符），应使用 `re.DOTALL`（或 `re.S`）标志。

3. **误区：括号 `()` 默认只用于分组，不会影响 `findall()` 的返回结果**
   **事实**：当模式中存在捕获组时，`re.findall()` 的行为会发生改变——它只返回捕获组的内容，而不是完整的匹配。例如 `re.findall(r'(ab)+', 'abab')` 返回 `['ab']` 而非 `['abab']`。如果需要完整匹配，可使用非捕获组 `(?:...)` 或通过 `re.finditer()` 逐个获取 match 对象。

4. **误区：贪婪模式总是最好的选择**
   **事实**：在处理分隔符或标签时应优先考虑非贪婪匹配（`*?`、`+?`），否则可能会跨越多条记录过度匹配。例如在提取 HTML 标签时，`<.*>` 会吞掉整个文档，而 `<.*?>` 能正确匹配单个标签。

5. **误区：使用正则表达式解析所有结构化文本**
   **事实**：正则表达式不适合解析嵌套结构（如 HTML、JSON、XML）。对于这些格式，应使用专门的解析器（如 `html.parser`、`json`、`xml.etree.ElementTree`）。正则表达式只能处理正则语法能描述的*正则语言*，嵌套结构属于上下文无关语法。

---

## 🔗 相关资源

- 上一节：[[PY019-Python中错误类型与异常处理机制|PY019-Python中错误类型与异常处理机制]]
- 官方文档：[re — Regular expression operations](https://docs.python.org/3/library/re.html)
- 正则表达式测试工具：[regex101.com](https://regex101.com)（支持 Python 语法，可实时调试）
- 正则表达式速查表：[Regular Expressions Cheat Sheet](https://www.debuggex.com/cheatsheet/regex/python)
