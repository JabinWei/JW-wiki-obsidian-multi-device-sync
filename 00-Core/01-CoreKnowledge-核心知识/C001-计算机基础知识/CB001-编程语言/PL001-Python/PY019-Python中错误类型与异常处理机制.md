---
type: learning
status: 已完成
domain: Python
tags: [Python, 编程语言]
created: 2026-06-12
updated: 2026-06-16
---

# Python 中错误类型与异常处理机制

## 🎯 学习目标

- Python 中的「语法错误」和「异常」有什么区别？
- 常见的 Python 内置异常类型有哪些？各自在什么场景下触发？
- `try...except...else...finally` 四个子句的执行顺序是什么？
- 如何用 `raise` 手动抛出异常？什么情况下需要使用它？
- 如何自定义异常类？它和内置异常相比有什么优势？
- `except Exception` 和裸 `except:` 有什么区别？为什么应该避免后者？
- 如何在 `except` 块中获取原始异常对象并使用它的属性？
- `finally` 子句在什么情况下不会执行？它和 `else` 子句的使用场景有何不同？

## 📖 前置知识

在学习本内容之前，需要掌握：
- [[PY018-Python中的类]] — 理解类的继承（自定义异常需要继承 `Exception` 类）

## 📚 核心内容

在 Python 编程中，程序运行时难免会遇到各种错误。Python 将这些错误分为两类：**语法错误 (Syntax Errors)** 和 **异常 (Exceptions)**。语法错误通常导致程序无法启动，而异常则是在程序运行过程中发生的。

---

### Python 常见错误类型 (Built-in Exceptions)

Python 提供了丰富的内置异常类型，用于标识不同的错误场景。了解这些常见错误有助于快速定位和解决问题。

**常见异常类型速查表：**

| 异常类型              | 触发场景                               | 代码示例                            |
| --------------------- | -------------------------------------- | ----------------------------------- |
| **SyntaxError**       | 语法错误，代码不符合 Python 语法规则   | `if True print("Hello")` (缺少冒号) |
| **NameError**         | 名称错误，尝试使用未定义的变量或函数   | `print(x)` (x 未声明)               |
| **TypeError**         | 类型错误，对不支持的数据类型执行了操作 | `"Hello" + 5` (字符串与整数拼接)    |
| **ValueError**        | 值错误，函数接收到正确类型但不合适的值 | `int("abc")` (无法转换的字符串)     |
| **IndexError**        | 索引错误，访问序列中不存在的索引       | `lst = [1]; print(lst[5])`          |
| **KeyError**          | 键错误，访问字典中不存在的键           | `d = {}; d['key']`                  |
| **ZeroDivisionError** | 除零错误，除数为 0                     | `10 / 0`                            |
| **FileNotFoundError** | 文件未找到，尝试打开不存在的文件       | `open("missing.txt")`               |

---

### 异常处理机制 (Try-Except)

当程序出现异常时，如果不进行处理，程序会立即终止并打印错误信息。为了防止这种情况，Python 提供了 `try...except...else...finally` 语句块来捕获和处理异常。

**核心语法结构：**

```python
try:
    # 尝试执行的代码块
    risky_code()
except SpecificError as e:
    # 如果发生 SpecificError 类型的异常，执行此处代码
    print(f"发生了错误: {e}")
except AnotherError:
    # 可以有多个 except 块来处理不同类型的错误
    pass
else:
    # 可选。如果没有发生任何异常，执行此处代码
    print("一切正常！")
finally:
    # 可选。无论是否发生异常，都会执行此处代码（常用于资源清理）
    print("这是无论如何都会执行的清理代码")
```

**代码示例：除法运算的安全处理**

```python
def safe_divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("错误：除数不能为零！")
        return None
    except TypeError:
        print("错误：请输入数字进行运算！")
        return None
    else:
        print(f"计算结果是: {result}")
        return result
    finally:
        print("本次除法运算尝试结束。")

# 测试
safe_divide(10, 2)  # 正常情况
safe_divide(10, 0)  # 除零异常
safe_divide(10, 'a') # 类型异常
```

---

### 抛出异常 (Raise)

除了 Python 自动触发异常，我们也可以使用 `raise` 语句手动触发异常。这在验证函数参数或强制程序逻辑时非常有用。

**代码示例：年龄验证**

```python
def set_age(age):
    if age < 0:
        # 手动抛出 ValueError 异常
        raise ValueError("年龄不能为负数！")
    print(f"年龄设置为: {age}")

try:
    set_age(-5)
except ValueError as e:
    print(f"捕获到异常: {e}")
```

---

### 自定义异常

虽然 Python 提供了很多内置异常，但在开发大型项目或特定库时，你可能需要定义自己的异常类型。这可以通过创建继承自 `Exception` 类（或其子类）的新类来实现。

**代码示例：定义银行余额不足异常**

```python
class InsufficientFundsError(Exception):
    """自定义异常：余额不足"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        # 调用父类构造函数
        super().__init__(f"余额不足。当前余额: {balance}, 尝试支出: {amount}")

def withdraw(balance, amount):
    if amount > balance:
        # 抛出自定义异常
        raise InsufficientFundsError(balance, amount)
    balance -= amount
    print(f"取款成功。剩余余额: {balance}")
    return balance

# 使用自定义异常
try:
    current_balance = 100
    withdraw(current_balance, 150)
except InsufficientFundsError as e:
    print(e) # 输出: 余额不足。当前余额: 100, 尝试支出: 150
```

## 🧪 练习 / 验证

**练习 1：判断异常类型**

阅读以下代码片段，写出每段代码会抛出什么异常类型。

```python
# (a)
x = [1, 2, 3]
print(x[3])

# (b)
d = {"name": "Alice"}
print(d["age"])

# (c)
num = int("12.5")

# (d)
result = "abc" + 123
```

<details>
<summary>答案</summary>

```
(a) IndexError — 列表索引 3 超出范围（列表只有 3 个元素，索引为 0,1,2）
(b) KeyError — 字典中没有键 "age"
(c) ValueError — "12.5" 是浮点数字符串，不能直接转为 int（可用 float() 先转换）
(d) TypeError — 不能将字符串与整数直接拼接
```

</details>

---

**练习 2：追踪 try-except-else-finally 执行流**

阅读以下代码，写出完整的输出顺序。

```python
def demo():
    try:
        print("A")
        x = 10 / 0
        print("B")
    except ZeroDivisionError:
        print("C")
    except Exception:
        print("D")
    else:
        print("E")
    finally:
        print("F")
    print("G")

demo()
```

<details>
<summary>答案</summary>

```
A
C
F
G
```

解释：
1. `print("A")` 执行，输出 A
2. `10 / 0` 触发 `ZeroDivisionError`，跳转到相应的 except 块
3. `print("B")` 被跳过（异常发生后 try 块剩余代码不再执行）
4. 匹配到 `except ZeroDivisionError`，输出 C
5. `else` 块被跳过（因为发生了异常）
6. `finally` 块始终执行，输出 F
7. 异常被捕获后程序继续，执行 `print("G")`，输出 G

</details>

---

**练习 3：捕获多个异常**

补全以下函数，使其能安全地将用户输入的字符串转为整数并计算倒数。需要处理三种错误：输入不是数字、输入是 0、其他未知错误。每种错误打印不同的提示信息。

```python
def reciprocal():
    user_input = input("请输入一个数字: ")
    try:
        num = int(user_input)
        result = 1 / num
    except ValueError:
        print("错误：输入的不是有效的整数！")
    except ZeroDivisionError:
        print("错误：0 没有倒数！")
    else:
        print(f"{num} 的倒数是 {result}")
    finally:
        print("计算结束。")

# 测试场景（模拟输入）：
# 输入 "10"  → 预期输出：10 的倒数是 0.1 \n 计算结束。
# 输入 "abc" → 预期输出：错误：输入的不是有效的整数！ \n 计算结束。
# 输入 "0"   → 预期输出：错误：0 没有倒数！ \n 计算结束。
```

<details>
<summary>答案</summary>

上面的代码已经补全。关键点：
- `except ValueError` 捕获 `int()` 转换失败
- `except ZeroDivisionError` 捕获除零操作
- `else` 只在没有异常时执行（打印结果）
- `finally` 无论是否异常都执行清理/收尾

三个测试场景的输出：
```
# 输入 "10"
10 的倒数是 0.1
计算结束。

# 输入 "abc"
错误：输入的不是有效的整数！
计算结束。

# 输入 "0"
错误：0 没有倒数！
计算结束。
```

</details>

---

**练习 4：使用 raise 验证函数参数**

编写函数 `calculate_grade(score)`，要求：
- 如果 `score` 不是整数或浮点数，抛出 `TypeError`
- 如果 `score < 0` 或 `score > 100`，抛出 `ValueError`
- 如果输入合法，按以下规则返回等级：
  - 90-100: "A"
  - 80-89: "B"
  - 70-79: "C"
  - 60-69: "D"
  - 0-59: "F"

```python
def calculate_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError(f"分数必须是数字，收到了 {type(score).__name__}")
    if score < 0 or score > 100:
        raise ValueError(f"分数必须在 0-100 之间，收到了 {score}")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 验证
print(calculate_grade(95))   # 输出: A
print(calculate_grade(73))   # 输出: C
print(calculate_grade(45))   # 输出: F

# 以下调用会抛出异常：
# calculate_grade("优秀")     # TypeError: 分数必须是数字，收到了 str
# calculate_grade(120)        # ValueError: 分数必须在 0-100 之间，收到了 120
# calculate_grade(-10)        # ValueError: 分数必须在 0-100 之间，收到了 -10
```

<details>
<summary>答案</summary>

完整代码如上。关键要点：
- 使用 `isinstance(score, (int, float))` 检查类型
- `raise TypeError(...)` 和 `raise ValueError(...)` 提供清晰的错误信息
- 将 `raise` 放在函数开头，作为「前置条件守卫」，阻止非法输入进入后续逻辑

</details>

---

**练习 5：自定义异常**

定义一个 `InvalidEmailError` 自定义异常，并在函数 `validate_email(email)` 中使用。验证规则：
- `@` 必须存在且只能出现一次
- 用户名部分（`@` 左侧）和域名部分（`@` 右侧）都不能为空
- 域名必须包含至少一个 `.`

```python
class InvalidEmailError(Exception):
    """自定义异常：邮箱格式无效"""
    def __init__(self, email, reason):
        self.email = email
        self.reason = reason
        super().__init__(f"邮箱 '{email}' 无效: {reason}")

def validate_email(email):
    if not isinstance(email, str):
        raise TypeError("邮箱必须是字符串")
    
    # 检查 @ 的数量
    at_count = email.count("@")
    if at_count == 0:
        raise InvalidEmailError(email, "缺少 @ 符号")
    if at_count > 1:
        raise InvalidEmailError(email, "存在多个 @ 符号")
    
    # 分割用户名和域名
    username, domain = email.split("@")
    
    if not username:
        raise InvalidEmailError(email, "@ 之前不能为空")
    if not domain:
        raise InvalidEmailError(email, "@ 之后不能为空")
    if "." not in domain:
        raise InvalidEmailError(email, "域名中缺少 .")
    
    return True

# 测试
test_cases = [
    "user@example.com",    # 有效
    "userexample.com",     # 缺少 @
    "user@@example.com",   # 多个 @
    "@example.com",        # 用户名为空
    "user@",               # 域名为空
    "user@domain",         # 域名无点号
]

for email in test_cases:
    try:
        validate_email(email)
        print(f"✅ {email} 有效")
    except InvalidEmailError as e:
        print(f"❌ {e}")

# 预期输出：
# ✅ user@example.com 有效
# ❌ 邮箱 'userexample.com' 无效: 缺少 @ 符号
# ❌ 邮箱 'user@@example.com' 无效: 存在多个 @ 符号
# ❌ 邮箱 '@example.com' 无效: @ 之前不能为空
# ❌ 邮箱 'user@' 无效: @ 之后不能为空
# ❌ 邮箱 'user@domain' 无效: 域名中缺少 .
```

<details>
<summary>答案</summary>

完整代码如上。关键设计要点：
- `InvalidEmailError` 继承 `Exception`，携带 `email` 和 `reason` 属性
- `super().__init__(...)` 确保异常对象可以正确转换为字符串
- `validate_email()` 对每种违规情况分别抛出带有描述性错误信息的异常
- 调用方可以用 `except InvalidEmailError as e` 捕获，并通过 `e.email` / `e.reason` 获取详细信息

</details>

---

**练习 6：为什么不要用裸 except:**

以下两个版本的函数看起来都能处理错误，但其中一个有严重隐患。找出隐患并说明原因。

```python
# 版本 A
def process_data_a(data):
    try:
        result = 100 / len(data)
        return result
    except:
        print("出错了！")
        return None

# 版本 B
def process_data_b(data):
    try:
        result = 100 / len(data)
        return result
    except ZeroDivisionError:
        print("数据列表为空！")
        return None
    except TypeError:
        print("传入的不是列表！")
        return None
```

<details>
<summary>答案</summary>

**版本 A 的问题（裸 `except:` 的三大隐患）：**

1. **会捕获不应该捕获的异常**：比如用户按下 `Ctrl+C` 触发的 `KeyboardInterrupt` 或系统退出信号 `SystemExit`，这些通常不应该被应用程序吞掉，而应该让程序正常终止。

2. **隐藏了未预见的错误**：如果 `process_data_a` 内部有 bug（比如拼写错误、逻辑错误），裸 `except:` 也会捕获并静默处理，导致你永远不知道代码有问题，难以调试。

3. **错误信息丢失**：打印的统一 "出错了！" 没有区分错误类型，无法帮助调用方或开发者定位问题。

**版本 B 更好**，因为它：
- 只捕获了预期的 `ZeroDivisionError` 和 `TypeError`
- 每种错误有对应的提示信息
- 未预见的异常不会被吞掉，会正常向上传播（方便调试）

**最佳实践**：永远不要使用 `except:` 或 `except Exception` 而不加限制，应明确指定要捕获的异常类型。

</details>

---

**练习 7：文件操作的异常处理**

编写函数 `read_config(filename)`，安全地读取配置文件并返回内容字符串。要求：
- 如果文件不存在，打印提示并返回 `None`
- 如果文件编码错误导致 `UnicodeDecodeError`，尝试用 `latin-1` 编码重新读取
- 如果权限不足（`PermissionError`），打印提示并返回 `None`
- 使用 `finally` 确保无论如何都打印 "读取操作已结束"

```python
def read_config(filename):
    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        return content
    except FileNotFoundError:
        print(f"配置文件 '{filename}' 不存在")
        return None
    except PermissionError:
        print(f"没有权限读取 '{filename}'")
        return None
    except UnicodeDecodeError:
        print("UTF-8 解码失败，尝试使用 latin-1 编码...")
        try:
            if f:
                f.close()
            f = open(filename, "r", encoding="latin-1")
            content = f.read()
            return content
        except Exception as e:
            print(f"备选编码也失败: {e}")
            return None
    finally:
        if f:
            f.close()
        print("读取操作已结束")

# 测试场景：
# read_config("exists.txt")       → 返回文件内容 + "读取操作已结束"
# read_config("not_found.txt")    → "配置文件 'not_found.txt' 不存在" + "读取操作已结束"
# read_config("/etc/shadow")      → "没有权限读取 '/etc/shadow'" + "读取操作已结束"
```

<details>
<summary>答案</summary>

完整代码如上。关键设计要点：
- `f = None` 初始化变量，防止 `NameError`
- 按具体性从高到低排列 `except` 块（`FileNotFoundError` → `PermissionError` → `UnicodeDecodeError`）
- `UnicodeDecodeError` 处理中先关闭原有文件句柄再重新打开
- `finally` 中检查 `if f:` 再关闭，避免对 `None` 调用 `.close()`
- 内层的 `except Exception as e` 用于捕获备选编码尝试中的未预期错误，同时不吞掉所有系统级异常

</details>

---

**练习 8：异常链与 raise from**

阅读以下代码，写出输出结果并解释 `raise ... from ...` 的作用。

```python
class DataError(Exception):
    pass

def load_data():
    try:
        raw = int("abc")
    except ValueError as e:
        raise DataError("数据加载失败") from e

try:
    load_data()
except DataError as err:
    print(f"捕获: {err}")
    print(f"原因: {err.__cause__}")
```

<details>
<summary>答案</summary>

**输出：**
```
捕获: 数据加载失败
原因: invalid literal for int() with base 10: 'abc'
```

**`raise ... from ...` 的作用**：
- 将原始异常 `ValueError` 设置为新异常 `DataError` 的 `__cause__` 属性
- 这样在异常回溯中会显示两个异常，明确展示因果关系：
  ```
  DataError: 数据加载失败
  The above exception was the direct cause of the following exception:
  ValueError: invalid literal for int() with base 10: 'abc'
  ```
- 比直接 `raise DataError("数据加载失败")` 保留了更多调试信息
- 如果想隐藏原始异常链，可以用 `raise DataError("数据加载失败") from None`（此时 `__cause__` 为 `None`，但 `__suppress_context__` 为 `True`）

</details>

## 🤔 常见误区

**误区 1：「`except Exception` 和 `except:` 是一样的」**

**事实**：不一样。`except:` 会捕获所有异常，包括 `SystemExit`、`KeyboardInterrupt`、`GeneratorExit` 等系统级异常，这些异常继承自 `BaseException` 而非 `Exception`。裸 `except:` 可能导致程序无法通过 `Ctrl+C` 正常终止。建议始终指定明确的异常类型。

---

**误区 2：「`finally` 块中的代码永远都会执行」**

**事实**：在绝大多数情况下是的，但以下情形 `finally` 不会执行：
- Python 解释器在被操作系统强制杀死时（`kill -9` / `SIGKILL`）
- 代码在 `finally` 之前发生了死循环且无法跳出
- 程序内部调用了 `os._exit()` 直接终止进程（绕过清理流程）

`finally` 设计用于清理资源（关闭文件、释放锁等），但不应该依赖它来处理关键业务逻辑。

---

**误区 3：「在 `except` 块中捕获异常后程序会自动继续执行 try 块的剩余代码」**

**事实**：一旦异常被捕获，try 块中异常发生点之后的代码不会恢复执行。如果想重试，需要将整个 try 块放入循环中。例如：

```python
# 错误的期望：希望捕获异常后继续执行 print("继续")
try:
    result = 10 / 0
    print("继续")  # 这行永远不会执行
except ZeroDivisionError:
    print("除数不能为零")
```

---

**误区 4：「异常处理越多越好，一个函数中应该尽可能多地用 try-except」**

**事实**：过度使用异常处理会使代码难以阅读和调试。原则是：
- 只在确实能处理异常的地方捕获（知道如何处理错误）
- 预期内的条件用 `if` 判断（如检查键是否存在），而不是依赖 `try-except`
- 让无法处理的异常向上层传播，在最外层统一捕获和记录

---

**误区 5：「自定义异常只是换个名字，没实际用处」**

**事实**：自定义异常在大型项目中至关重要：
- 允许调用方按业务逻辑分类处理（如 `except PaymentError`）
- 可以携带额外的上下文信息（如 `balance` 和 `amount`）
- 提升了代码的可读性和可维护性
- 有助于构建清晰的异常层级结构（如 `PaymentError` → `InsufficientFundsError`, `PaymentTimeoutError`）

## 🔗 相关资源

- 上一节：[[PY018-Python中的类]]
- 下一节：[[PY020-Python中的正则表达式]]
- Python 官方文档：[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- Python 官方文档：[Errors and Exceptions Tutorial](https://docs.python.org/3/tutorial/errors.html)
- 异常层级结构参考：[Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
