---
type: card
status: 已完成
aliases: [__new__, __init__, 构造函数, 单例模式, 不可变类型继承]
tags: [编程语言, Python]
created: 2026-07-20
updated: 2026-07-20
---

## 💡 核心概念

`__new__` 负责**创建**对象（分配内存，返回空实例），`__init__` 负责**初始化**对象（给实例挂载属性）。执行顺序：先 `__new__`，再 `__init__`。基础参见 [[PY020-类]]。

```
__new__  → 分配内存，创建空实例（毛坯房）
__init__ → 给实例挂载属性（装修入住）
```

| | `__new__` | `__init__` |
|---|-----------|------------|
| 做什么 | 创建空实例 | 挂载属性 |
| 第一个参数 | `cls` — 类对象本身 | `self` — 已创建的空实例 |
| 返回值 | **必须返回**实例 | 只能返回 `None` |
| 时机 | 先执行 | 后执行 |
| 日常代码 | 极少重写 | 天天写 |

---

## 🔍 详细说明

### 1. 执行顺序

```python
obj = MyClass('Alice')

# Python 内部等价于：
# Step 1: MyClass.__new__(MyClass, 'Alice') → 分配内存，创建空实例
# Step 2: 如果 __new__ 返回了 MyClass 的实例
# Step 3: 自动调用 instance.__init__('Alice')
```

### 2. 什么时候需要重写 `__new__`

```python
# 场景1：单例模式
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a, b = Singleton(), Singleton()
print(a is b)  # True — 始终返回同一个实例

# 场景2：继承不可变类型（str/tuple/int）
class UpperStr(str):
    def __new__(cls, value):
        value = value.upper()       # 必须在创建之前修改
        return super().__new__(cls, value)

print(UpperStr('hello'))  # HELLO
# __init__ 对不可变类型无效 — str 创建后就无法被修改了
```

> `cls` 是类对象本身（类似 `self` 是实例对象），由 Python 解释器自动传入。取名 `cls` 只是惯例。

---

## ⚡ 反例 / 边界

1. **99% 的场景不需要重写 `__new__`** — 初始化属性用 `__init__` 足够
2. **`__new__` 返回非本类实例会跳过 `__init__`** — 这是设计，不是 bug
3. **`__init__` 不能返回除 `None` 外的值** — 否则 `TypeError`
4. **继承 str/tuple/int 必须在 `__new__` 里修改值** — 它们创建后就不可变了

---

## 🔗 关联卡片

- [[PY020-类]] — `__init__` 基础用法
- [[PL-PY-005-元组不可变性的真正边界]] — 不可变对象的特性

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
