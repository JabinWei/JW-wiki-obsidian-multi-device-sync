---
type: draft
status: 草稿
tags: [编程语言, Python, 数据模型]
created: 2026-11-17
---

# Python 运算符协商机制（双分派）

> 草稿来源：PL-PY-001（is 与 == 的区别）延伸讨论，由 `x == None` 为什么可行展开。

## 核心问题

`a + b`、`a == b` 这种二元运算符，到底是谁的方法？为什么两个完全陌生的类型（比如内置 `int` 和自己写的 `Fraction`）之间也能做运算？

## 为什么需要"协商"

最朴素的想法是：`a + b` 就调用 `type(a).__add__(a, b)`（简写 `a.__add__(b)`）。但问题来了——如果 `a` 是内置类型（比如 `int`），`b` 是自己写的类：

```python
3 + Fraction(1, 2)
```

`int` 是 Python 早就编译好的内置类型，**根本不知道**你后面会写一个 `Fraction` 类。所以 `int.__add__` 收到右边是你的 Fraction 时，没法处理，只能返回 `NotImplemented`。

Python 的解法：
1. 先问左边："你会加这个右边的东西吗？"
2. 左边说"不会"（返回 `NotImplemented`）
3. 再问右边："那你来加左边的东西，行不？"
4. 右边（你的 Fraction）说"行"，用 `__radd__` 处理

这样两个完全陌生的类型之间也能运算，不需要任何一方预先知道对方。

## 完整的双分派流程

> 说明：下面的流程图用 `a.__add__(b)` 这种简写来表示实例方法调用。严格来说，运算符调用的是 `type(a).__add__(a, b)`——从类上找方法，`a` 作为 `self` 传入。这里用简写只是为了流程图简洁。

以 `a + b` 为例：

```
a + b
   │
   ▼
1. 调用 type(a).__add__(a, b)
   │  （简写：a.__add__(b)）
   │
   ├── 返回了真正的结果 → 结束
   └── 返回 NotImplemented → 进入步骤 2
   │
   ▼
2. 调用 type(b).__radd__(b, a)（反射加法）
   │  （简写：b.__radd__(a)）
   │
   ├── 返回了真正的结果 → 结束
   └── 返回 NotImplemented → 进入步骤 3
   │
   ▼
3. 两边都搞不定 → 抛 TypeError: unsupported operand type(s) for +
```

**关键规则**：只要有任何一边返回了**非 `NotImplemented`** 的值，协商就停止。只有当两边**都返回 `NotImplemented`** 时，才报错。

## 反射方法（Reflected Methods）

每个运算符都有一个对应的"反射版本"，名字就是在原名前加 `r`：

| 运算符 | 左操作数方法 | 右操作数方法（反射） |
|--------|------------|-------------------|
| `+` | `__add__` | `__radd__` |
| `-` | `__sub__` | `__rsub__` |
| `*` | `__mul__` | `__rmul__` |
| `/` | `__truediv__` | `__rtruediv__` |
| `//` | `__floordiv__` | `__rfloordiv__` |
| `%` | `__mod__` | `__rmod__` |
| `**` | `__pow__` | `__rpow__` |
| `<<` | `__lshift__` | `__rlshift__` |
| `&` | `__and__` | `__rand__` |
| `^` | `__xor__` | `__rxor__` |
| `\|` | `__or__` | `__ror__` |

**反射的语义**：`type(b).__radd__(b, a)`（简写 `b.__radd__(a)`）等价于"反过来算"——本来是 `a + b`，现在让 `b` 站在左边的位置加 `a`。注意反射方法的参数顺序：self 还是 `b`，other 变成了 `a`。

### 为什么 `__radd__` 和 `__add__` 看起来在做一样的事？

很多人会困惑：加法和乘法的反射版本，逻辑好像和原版一样？这不是巧合，而是因为**加法和乘法是可交换运算**。

数学上：
- **加法可交换**：`a + b = b + a`
- **乘法可交换**：`a × b = b × a`
- **减法不可交换**：`a - b ≠ b - a`
- **除法不可交换**：`a ÷ b ≠ b ÷ a`

反射方法存在的意义，就是当**操作数顺序被反转**时，告诉你该怎么算。对于可交换运算，顺序反转无所谓；对于不可交换运算，顺序反转结果就完全变了。

| 运算符 | `__xxx__` 计算的是 | `__rxxx__` 计算的是 | 顺序反转后结果变不变 |
|--------|-------------------|-------------------|-------------------|
| `+` | `self + other` | `other + self` | **不变**（可交换）→ 感觉一样 |
| `*` | `self * other` | `other * self` | **不变**（可交换）→ 感觉一样 |
| `-` | `self - other` | `other - self` | **变了**（不可交换）→ 完全不同 |
| `/` | `self / other` | `other / self` | **变了**（不可交换）→ 完全不同 |
| `//` | `self // other` | `other // self` | **变了**（不可交换）→ 完全不同 |
| `%` | `self % other` | `other % self` | **变了**（不可交换）→ 完全不同 |
| `**` | `self ** other` | `other ** self` | **变了**（不可交换）→ 完全不同 |

#### 用减法直观感受：反射版本必须反过来写

假设你写一个 `Meter`（长度）类：

```python
class Meter:
    def __init__(self, m):
        self.m = m
    def __repr__(self):
        return f"{self.m}米"

    # self - other
    def __sub__(self, other):
        print(f"  __sub__: {self} - {other}")
        return Meter(self.m - other.m)

    # 注意！这时候是 other - self，不是 self - other！
    def __rsub__(self, other):
        print(f"  __rsub__: {other} - {self}")
        return Meter(other.m - self.m)   # ← 顺序反了！
```

**情况 1：正常减法（左边是 Meter）**

```python
a = Meter(10)
b = Meter(3)

a - b
# → Meter.__sub__(a, b)
# __sub__: 10米 - 3米
# 结果：7米 ✓
```

**情况 2：左边是 int，右边是 Meter（触发反射）**

```python
# 100 - a，意思是"从 100 米里减去 a 的 10 米"
# 数学上应该是 100 - 10 = 90 米

100 - a
# → int.__sub__(100, a) 返回 NotImplemented（int 不认识 Meter）
# → 触发 Meter.__rsub__(a, 100)
# __rsub__: 100 - 10米
# 结果：90米 ✓
```

**关键来了**：如果 `__rsub__` 像 `__sub__` 那样写 `self.m - other.m`，会变成什么？

```python
def __rsub__(self, other):
    return Meter(self.m - other.m)   # ❌ 错误写法
```

那 `100 - a` 就会变成 `a.m - 100 = 10 - 100 = -90米`，完全反了！

**所以 `__rsub__` 必须反过来写 `other.m - self.m`**——这就是它和 `__sub__` 做的事情不一样的地方。

#### 回到加法：为什么看起来一样？

因为加法可交换，`other + self` 和 `self + other` 数学上结果一样：

```python
class Meter:
    def __add__(self, other):
        return Meter(self.m + other.m)

    def __radd__(self, other):
        # 加法可交换，other + self == self + other
        # 所以这里写什么顺序都无所谓
        return Meter(other.m + self.m)
```

很多标准库的类（比如 `Fraction`、`Decimal`）的 `__radd__` 甚至直接就是 `return self + other`，因为加法可交换，没必要重写。

#### 一句话总结

反射方法不是"重复造轮子"，而是**在操作数顺序反转后告诉你该怎么算**：
- 对 `+`、`*` 这种可交换运算，顺序反转不影响结果，所以 `__radd__` 和 `__add__` 看起来在做一样的事
- 对 `-`、`/`、`**` 这种不可交换运算，顺序反转结果完全不同，`__rsub__` 和 `__sub__` 做的事情**正好相反**

## `==` 与其他运算符的差异

`==` 是最特殊的：

### 1. 兜底行为不同

- `+` 协商失败 → **抛 TypeError**
- `==` 协商失败 → **返回 `a is b` 的结果**（兜底身份比较）

这就是为什么你永远不会看到 `A() == B()` 报错——最多返回 `False`。

### 2. 子类优先规则

```python
class Animal:
    def __eq__(self, other):
        return NotImplemented

class Dog(Animal):
    def __eq__(self, other):
        return True

a = Animal()
d = Dog()
a == d   # 谁先？
```

如果右边的对象是左边对象类型的子类，**优先让右边的 `__eq__` 先试**。这样 `a == d` 会先调用 `d.__eq__(a)`，因为 `Dog` 是更具体的子类，可能有更精确的比较逻辑。

## 完整例子：Fraction 类

```python
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("分母不能为 0")
        g = gcd(numerator, denominator)
        self.n = numerator // g
        self.d = denominator // g

    def __repr__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        print(f"  [调试] Fraction.__add__({other!r})")
        if isinstance(other, Fraction):
            return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)
        if isinstance(other, int):
            return Fraction(self.n + other * self.d, self.d)
        return NotImplemented

    def __radd__(self, other):
        print(f"  [调试] Fraction.__radd__({other!r})")
        if isinstance(other, int):
            return Fraction(other * self.d + self.n, self.d)
        return NotImplemented

    def __eq__(self, other):
        print(f"  [调试] Fraction.__eq__({other!r})")
        if isinstance(other, Fraction):
            return self.n == other.n and self.d == other.d
        if isinstance(other, int):
            return self.d == 1 and self.n == other
        return NotImplemented

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
```

### 分步走读：为什么 `__add__` 和 `__radd__` 里都有 int 分支？

初学最容易绕的就是这里。先记住一个分工表：

| 写法 | self 是谁 | 谁来响应 |
|------|-----------|----------|
| `f1 + 1` | f1（Fraction 在左） | `f1.__add__(1)` |
| `1 + f1` | f1（Fraction 在右） | 先试 `1.__add__(f1)`，失败后 `f1.__radd__(1)` |

**Fraction 必须同时写 `__add__` 和 `__radd__`**，因为它既可能站左边也可能站右边。

#### 场景 ① `f1 + f2`

```
→ Fraction.__add__(f1, f2)
→ other 是 Fraction 分支
→ (1*3 + 1*2)/(2*3) = 5/6
```

#### 场景 ② `f1 + 1`（Fraction 在左）

```
→ Fraction.__add__(f1, 1)
→ other 是 int 分支：(self.n + other*self.d)/self.d = (1 + 1*2)/2 = 3/2
→ Fraction 站左边，自己能处理右边的 int，不触发反射
```

#### 场景 ③ `1 + f1`（int 在左，Fraction 在右）—— 关键

```
→ int.__add__(1, f1) 返回 NotImplemented（内置 int 不认识 Fraction）
→ 触发反射：Fraction.__radd__(f1, 1)
           ↑ 注意：self 仍然是右边的 f1，other 变成了左边的 1
→ other 是 int 分支：(other*self.d + self.n)/self.d = (1*2 + 1)/2 = 3/2
```

#### 为什么两个方法里都要写 int 分支？

因为它们处理的是**位置不同**的 int：

```python
# f1 + 1：int 在右边，由 __add__ 处理
def __add__(self, other):
    if isinstance(other, int):
        return Fraction(self.n + other * self.d, self.d)
        # 数学含义：self + other = n/d + 1 = (n + 1*d)/d

# 1 + f1：int 在左边，由 __radd__ 处理
def __radd__(self, other):
    if isinstance(other, int):
        return Fraction(other * self.d + self.n, self.d)
        # 数学含义：other + self = 1 + n/d = (1*d + n)/d
```

两个公式数学上是同一个东西（加法可交换），所以看着像重复。如果是减法，`__rsub__` 必须把顺序反过来写（见前面 Meter 例子）。

#### 场景 ④ `f == 2`（Fraction 等于 int）

```python
f = Fraction(2, 1)   # 也就是 2/1
f == 2
# → Fraction.__eq__(f, 2)
# → other 是 int 分支：self.d == 1 and self.n == other
# → d=1 且 n=2 == 2 → True
# 含义：这个分数是不是整数，值等不等于那个 int
```

## 关键概念：`NotImplemented` vs `NotImplementedError`

- **`NotImplemented`**：一个单例值，表示"我不会处理这个操作数"，是协商机制的信号
- **`NotImplementedError`**：一个异常，表示"这个抽象方法还没实现"

两者完全不同，不要混淆。

## 设计哲学

1. **开闭原则**：内置类型不需要为你的类预留接口，你的类也不需要为别人预留。
2. **对称扩展**：`__radd__` 让"右边是自定义类型、左边是内置类型"这种常见场景也能工作。
3. **兜底安全**：`==` 协商失败时回退到身份比较，不会让程序崩溃；算术运算失败时直接报错。
4. **子类优先**：`==` 的协商顺序考虑了继承关系，让更具体的类型有优先话语权。

## 关联卡片

- [[PL-PY-001-is与==的区别]] — 本话题的起点
- 待补充：PY 运算符相关卡片
