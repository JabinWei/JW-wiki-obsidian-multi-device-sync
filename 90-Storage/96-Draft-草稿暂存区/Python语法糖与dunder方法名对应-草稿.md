---
type: draft
status: 草稿
tags: [编程语言, Python, 数据模型]
created: 2026-11-17
---

# Python 语法糖与 dunder 方法名的对应规则

> 草稿来源：由"`a + b` 为什么会自动调用 `__add__`"展开，理清 Python 语法到特殊方法的硬绑定。

## 核心问题

看到 `a + b`，怎么知道它会调用 `__add__`？这个对应关系是约定、是巧合、还是语言规范？

**答案：是语言规范，硬绑定。** 不是记忆题，是规则。

## 最核心的规则：语法到方法名的固定映射

Python 设计了一张**写死的对照表**。你看到的每个运算符/语法，都对应一个固定名字的双下划线方法（叫"dunder method"，双下划线 = double underscore → dunder）。

### 先搞清楚：完整调用形式到底传几个参数？

这是最容易被简写误导的地方。以 `a + b` 为例，**完整的、严格等价的调用形式是**：

```python
type(a).__add__(a, b)
#  ↑      ↑    ↑    ↑
#  类    方法  self  other
#             =a   =b
```

注意 `__add__` 是实例方法，它有两个参数：
- **第一个参数 `self`**：就是左边的对象 `a` 本身（Python 自动传进去）
- **第二个参数 `other`**：就是右边的对象 `b`

代入具体类型就很直观了：

```python
3 + 5
# 等价于：
int.__add__(3, 5)     # self=3, other=5 → 返回 8

"abc" + "def"
# 等价于：
str.__add__("abc", "def")   # self="abc", other="def" → 返回 "abcdef"
```

> ⚠️ **重要说明**：为了表格简洁，下面的对照表用的是简写 `type(a).__add__(b)`。这是**省略了 self 的记号**，不代表只传一个参数。实际调用时 `a` 一定会作为第一个参数（self）传进去。完整形式永远是 `type(a).__add__(a, b)`。

### 算术运算符

| 你写的语法 | Python 实际调用（简写） | 完整形式 | 含义 |
|-----------|----------------------|---------|------|
| `a + b` | `type(a).__add__(b)` | `type(a).__add__(a, b)` | 加法 |
| `a - b` | `type(a).__sub__(b)` | `type(a).__sub__(a, b)` | 减法（subtraction） |
| `a * b` | `type(a).__mul__(b)` | `type(a).__mul__(a, b)` | 乘法（multiplication） |
| `a / b` | `type(a).__truediv__(b)` | `type(a).__truediv__(a, b)` | 真除法 |
| `a // b` | `type(a).__floordiv__(b)` | `type(a).__floordiv__(a, b)` | 地板除 |
| `a % b` | `type(a).__mod__(b)` | `type(a).__mod__(a, b)` | 取模（modulo） |
| `a ** b` | `type(a).__pow__(b)` | `type(a).__pow__(a, b)` | 幂运算（power） |
| `a @ b` | `type(a).__matmul__(b)` | `type(a).__matmul__(a, b)` | 矩阵乘法（Python 3.5+） |

### 位运算符

| 语法 | 方法 |
|------|------|
| `a << b` | `__lshift__` |
| `a >> b` | `__rshift__` |
| `a & b` | `__and__` |
| `a \| b` | `__or__` |
| `a ^ b` | `__xor__` |
| `~a` | `__invert__` |

### 比较运算符

| 语法 | 方法 | 含义 |
|------|------|------|
| `a == b` | `__eq__` | equal |
| `a != b` | `__ne__` | not equal |
| `a < b` | `__lt__` | less than |
| `a <= b` | `__le__` | less or equal |
| `a > b` | `__gt__` | greater than |
| `a >= b` | `__ge__` | greater or equal |

### 其他常见语法

| 语法/内置函数 | 方法 |
|--------------|------|
| `len(a)` | `__len__` |
| `str(a)` | `__str__` |
| `repr(a)` | `__repr__` |
| `a[i]` | `__getitem__(i)` |
| `a[i] = v` | `__setitem__(i, v)` |
| `del a[i]` | `__delitem__(i)` |
| `a(...)` | `__call__(...)` |
| `with a:` | `__enter__` / `__exit__` |
| `iter(a)` | `__iter__` |
| `next(a)` | `__next__` |
| `abs(a)` | `__abs__` |
| `int(a)` | `__int__` |
| `float(a)` | `__float__` |
| `bool(a)` | `__bool__` |
| `hash(a)` | `__hash__` |
| `del a` | `__del__`（析构函数） |

## 关键细节：是从类上找方法，不是从实例上找

上面已经说了完整形式是 `type(a).__add__(a, b)`。这里要再强调一个初学者最容易踩的坑：你可能以为 `a + b` 等价于直接在实例上调用：

```python
a.__add__(b)   # ❌ 这是实例方法的简写，和运算符行为不完全等价
```

**不对**。Python 在执行 `a + b` 时，是这样做的：

```python
type(a).__add__(a, b)   # ✅ 正确理解
#  ↑ 从 type(a)（类）上找 __add__，不是从 a（实例）上找
```

两者看起来差不多，但有一个关键区别——**Python 从 `type(a)`（对象的类）上找 `__add__` 方法，而不是从对象实例本身找**。

### 为什么要这样设计？防止被实例属性欺骗

```python
class Foo:
    def __add__(self, other):
        return "我是类上的 __add__"

a = Foo()
a.__add__ = lambda other: "我是实例上伪装的 __add__"

print(a + 1)          # 我是类上的 __add__（运算符走类方法）
print(a.__add__(1))   # 我是实例上伪装的 __add__（普通属性查找，先找实例）
```

**为什么 `a + 1` 不被欺骗？** 因为 Python 的运算符重载规则明确规定：运算符的 dunder 方法**必须从类型（类）上查找**，忽略实例字典里的同名属性。这是为了保证运算符行为的稳定性——你不能通过给某个实例挂个属性就改变 `+` 的行为。

但如果你手写 `a.__add__(1)`，那就没有这个保护，Python 会按普通属性查找顺序（先实例、后类）找到那个伪装的 lambda。

> 这也解释了为什么 `a + b` 和 `a.__add__(b)` 在大多数时候等价，但在某些边缘情况下会不同——运算符走的是**类型字典优先**，普通方法调用走的是**实例字典优先**。

## 反射方法：r 前缀

每个二元运算符都有一个反射版本，名字就是在原方法名前加 `r`：

- `__add__` → `__radd__`
- `__sub__` → `__rsub__`
- `__mul__` → `__rmul__`
- `__eq__` → （没有反射，因为等式是对称的）

反射方法在什么情况下被调用？详见 [[Python运算符协商机制-草稿]]。

## 怎么"知道"这个映射？三种可靠方法

### 方法 1：查文档（最权威）

Python 官方文档有一张专门的表叫 **"Special method names"**（特殊方法名），在语言参考的 Data Model 章节：

```
https://docs.python.org/3/reference/datamodel.html#special-method-names
```

这张表把所有 dunder 方法、对应的语法触发条件、参数、返回值要求都写得清清楚楚。这是"标准答案"。

### 方法 2：实验验证（最直接）

写一个 tracing 类，把所有 dunder 方法都打上日志：

```python
class Tracing:
    def __add__(self, other):
        print(f"__add__ 被调用，other={other}")
        return "加法结果"
    def __eq__(self, other):
        print(f"__eq__ 被调用，other={other}")
        return True
    def __lt__(self, other):
        print(f"__lt__ 被调用，other={other}")
        return False

t = Tracing()

t + 10    # 打印 __add__ 被调用
t == 10   # 打印 __eq__ 被调用
t < 10    # 打印 __lt__ 被调用
```

这是最诚实的方法——你不需要背，写个类跑一下就知道。

### 方法 3：用 `dir()` 反向查表

```python
print(dir(5))
# 输出：['__abs__', '__add__', '__and__', '__bool__', ...]
```

拿到一个对象，看它有哪些 dunder，就知道它支持哪些语法。看到 `__add__` 就知道它支持 `+`，看到 `__lt__` 就知道它支持 `<`。

## 记忆规律（不需要死记硬背）

1. **算术运算符**：方法名就是运算符的英文全称/缩写
   - `+` → `add`（加法）
   - `-` → `sub`（subtraction）
   - `*` → `mul`（multiplication）
   - `/` → `truediv`（真除法，区别于 Python 2 的 `/`）
   - `//` → `floordiv`（地板除）
   - `%` → `mod`（modulo）
   - `**` → `pow`（power）

2. **比较运算符**：英文缩写
   - `==` → `eq`（equal）
   - `!=` → `ne`（not equal）
   - `<` → `lt`（less than）
   - `<=` → `le`（less or equal）
   - `>` → `gt`（greater than）
   - `>=` → `ge`（greater or equal）

3. **反射版本**：原方法名前加 `r`

4. **内置函数**：通常就是函数名本身
   - `len()` → `__len__`
   - `str()` → `__str__`
   - `int()` → `__int__`
   - `bool()` → `__bool__`
   - `iter()` → `__iter__`

## 用 `operator` 模块验证

标准库 `operator` 模块提供了所有运算符的函数形式：

```python
import operator

print(operator.add(3, 5))     # 8，等价于 3 + 5
print(operator.eq(3, 5))      # False，等价于 3 == 5
print(operator.lt(3, 5))       # True，等价于 3 < 5
```

`operator.add` 内部做的事就是 `type(a).__add__(a, b)`。

## 总结

1. **语法到方法名是语言硬绑定的**：看到 `a + b`，就知道 Python 在调用 `type(a).__add__(a, b)`。
2. **方法名有规律**：运算符英文 + dunder 包裹，反射加 `r` 前缀，比较用英文缩写。
3. **三种验证方法**：查官方文档、写 tracing 类、`dir(obj)` 反向查表。
4. **关键细节**：运算符是从**类**上找 dunder，不是从实例上找。这就是为什么实例上的同名属性不会改变运算符行为。

一句话：**`+` 不是"恰好调用了 `__add__`"，而是 Python 语法层面规定了 `+` 这个符号在执行时必须去查 `__add__`。** 这是语言设计，不是巧合。

## 关联卡片

- [[PL-PY-001-is与==的区别]] — 本话题的起点
- [[Python运算符协商机制-草稿]] — 配合阅读，理解协商如何使用这些方法
- 待补充：PY 运算符相关卡片
