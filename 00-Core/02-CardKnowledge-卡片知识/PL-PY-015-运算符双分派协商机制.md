---
type: card
status: 待办
aliases: [双分派, 反射方法, __radd__, 运算符协商, operator dispatch, reflected methods]
tags: [编程语言, Python]
created: 2026-11-17
updated: 2026-11-17
---

## 💡 核心概念

==Python 二元运算符（`a + b`、`a == b` 等）执行时，先问左边 `type(a).__add__(a, b)`；左边返回 `NotImplemented` 再问右边 `type(b).__radd__(b, a)`；两边都不行才抛错==。这套"先左后右、右边反过来应答"的协议叫**双分派（dual dispatch）/ 运算符协商**，让内置类型和自定义类无需事先认识对方也能运算。

---

## 🔍 详细说明

### 一、为什么需要协商

`3 + Fraction(1, 2)` 里，`int` 是 Python 早就编译好的内置类型，它根本不知道你后面会写一个 `Fraction` 类。所以 `int.__add__` 收到右边是 Fraction 时只能返回 `NotImplemented`。Python 的解法是：

1. 先问左边："你会加这个右边的东西吗？"
2. 左边说"不会"（返回 `NotImplemented`）
3. 再问右边："那你来加左边的东西，行不？"
4. 右边用 `__radd__`（反射版本）处理

### 二、完整双分派流程（以 `a + b` 为例）

```
a + b
   │
   ▼
1. 调用 type(a).__add__(a, b)     ← 简写 a.__add__(b)
   ├── 返回真正结果 → 结束
   └── 返回 NotImplemented → 步骤 2
   ▼
2. 调用 type(b).__radd__(b, a)    ← 简写 b.__radd__(a)
   │  注意：self 仍然是 b，other 变成了 a
   ├── 返回真正结果 → 结束
   └── 返回 NotImplemented → 步骤 3
   ▼
3. TypeError: unsupported operand type(s) for +
```

> 🔑 **关键规则**：只要任一边返回**非 `NotImplemented`** 的值，协商就停止；只有两边都返回 `NotImplemented` 才报错。

### 三、反射方法表

每个二元运算符都有一个 `r` 前缀的反射版本：

| 运算符 | 左方法 | 右方法（反射） |
|--------|--------|--------------|
| `+` | `__add__` | `__radd__` |
| `-` | `__sub__` | `__rsub__` |
| `*` | `__mul__` | `__rmul__` |
| `/` | `__truediv__` | `__rtruediv__` |
| `//` | `__floordiv__` | `__rfloordiv__` |
| `%` | `__mod__` | `__rmod__` |
| `**` | `__pow__` | `__rpow__` |

### 四、反射方法到底算什么？

反射不是"重复造轮子"，而是**在操作数顺序被反转后告诉你该怎么算**。对可交换/不可交换运算，含义完全不同：

| 运算符 | `__xxx__` 算的是 | `__rxxx__` 算的是 | 顺序反转后 |
|--------|-----------------|-----------------|----------|
| `+` | `self + other` | `other + self` | 不变（可交换） |
| `*` | `self * other` | `other * self` | 不变（可交换） |
| `-` | `self - other` | `other - self` | **变了** |
| `/` | `self / other` | `other / self` | **变了** |
| `**` | `self ** other` | `other ** self` | **变了** |

减法的反射必须把顺序反过来写——见下面 Meter 例子。

### 五、`==` 的特殊之处

`==` 是最特殊的协商：

1. **兜底不同**：`+` 协商失败抛 `TypeError`，`==` 协商失败回退到 `a is b`（永远不报错，最多返回 `False`）。这就是 `A() == B()` 永远安全的原因。
2. **子类优先**：若 `b` 是 `a` 类型的子类，优先让 `b.__eq__` 先试——更具体的子类有更精确的比较逻辑。

### 六、`NotImplemented` vs `NotImplementedError`

- **`NotImplemented`**：单例值，"我不会处理这个操作数"，是协商机制的信号
- **`NotImplementedError`**：异常，"这个抽象方法还没实现"

两者完全不同，不要混淆。

---

## 📎 例子

### 用减法感受反射必须反过来写

```python
class Meter:
    def __init__(self, m):
        self.m = m
    def __repr__(self):
        return f"{self.m}米"

    # self - other
    def __sub__(self, other):
        return Meter(self.m - other.m)

    # other - self，顺序必须反过来！
    def __rsub__(self, other):
        return Meter(other.m - self.m)   # ✅ 正确

    # ❌ 错误写法：return Meter(self.m - other.m)
    #    100 - Meter(10) 会算成 10 - 100 = -90，完全反了
```

```python
a = Meter(10)
a - Meter(3)     # → __sub__：10米 - 3米 = 7米 ✓
100 - a         # → int.__sub__ 返回 NotImplemented
                # → Meter.__rsub__(a, 100)：100 - 10米 = 90米 ✓
```

### Fraction 完整例子（分步走读）

```python
from math import gcd

class Fraction:
    def __init__(self, n, d=1):
        if d == 0: raise ValueError("分母不能为0")
        g = gcd(n, d)
        self.n, self.d = n // g, d // g

    def __repr__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.n * other.d + other.n * self.d,
                            self.d * other.d)
        if isinstance(other, int):
            return Fraction(self.n + other * self.d, self.d)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return Fraction(other * self.d + self.n, self.d)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.n == other.n and self.d == other.d
        if isinstance(other, int):
            return self.d == 1 and self.n == other
        return NotImplemented

f1 = Fraction(1, 2)
```

**逐场景走读**——记住分工表：Fraction 在左走 `__add__`，Fraction 在右走 `__radd__`。

| 写法 | 调用路径 | 结果 |
|------|---------|------|
| `f1 + f1` | `Fraction.__add__(f1, f1)` → Fraction 分支 | 1/1 |
| `f1 + 1` | `Fraction.__add__(f1, 1)` → int 分支，(1+1·2)/2 | 3/2 |
| `1 + f1` | `int.__add__(1, f1)` 失败 → `Fraction.__radd__(f1, 1)` → (1·2+1)/2 | 3/2 |
| `Fraction(2,1) == 2` | `Fraction.__eq__(f, 2)` → d==1 且 n==2 | True |

> 💡 **为什么 `__add__` 和 `__radd__` 里都要写 int 分支？**
> 因为它们处理的是位置不同的 int：`f1 + 1` 的 int 在右边由 `__add__` 处理；`1 + f1` 的 int 在左边由 `__radd__` 处理。两个公式数学上是同一个东西（加法可交换），所以看着像重复。减法就不会这样——`__rsub__` 必须反过来写。

---

## ⚡ 反例 / 边界

1. **反射方法里搞反顺序**：写 `__rsub__`、`__rtruediv__`、`__rpow__` 时，最常见的错误是照抄 `__sub__` 的 `self - other` 顺序。这三种不可交换运算必须反过来 `other - self`。
2. **忘了返回 `NotImplemented`**：遇到不认识的类型要 `return NotImplemented`，**不能**抛 `TypeError` 也不能返回 `None`——返回 `None` 会让协商误以为成功了。
3. **`==` 会静默回退到身份比较**：自定义类没实现 `__eq__` 时，`a == b` 等价于 `a is b`。这不是 bug，是兜底设计。
4. **反射不是复制粘贴**：对 `+`、`*` 直接 `return self + other` 可以，但对 `-`、`/` 这么写结果会反。
5. **子类优先规则只对 `==` 生效**：算术运算符的反射不考虑子类关系，按左右顺序走。

---

## 🔗 关联卡片

- [[PL-PY-001-is与==的区别]] — `==` 与 `is` 的语义区分，本话题的起点
- [[PL-PY-016-语法糖与dunder方法名对应规则]] — 运算符对应到哪个 dunder 方法
- [[PL-PY-012-可迭代对象与迭代器协议]] — 另一种协议协商（`__iter__` / `__getitem__`）

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```

---

## 📝 待补充内容

- [ ] 富比较运算符（`<`、`>`、`<=`、`>=`）的反射协商规则——`__lt__` 没有 `__rlt__`，是怎么通过反射实现的？
- [ ] `functools.total_ordering` 装饰器如何简化比较协议
- [ ] 就地运算符（`+=`、`-=`）的协商流程：`__iadd__` 优先于 `__add__` 的细节
