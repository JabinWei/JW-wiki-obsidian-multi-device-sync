---
type: card
status: 已完成
aliases: [wraps, functools.wraps, 装饰器元数据, __name__
tags: [编程语言, Python]
created: 2026-07-20
updated: 2026-07-20
---

## 💡 核心概念

装饰器会把原函数的 `__name__`、`__doc__` 等元数据替换成 wrapper 的。`@functools.wraps(func)` 的作用是把这些元数据**拷贝回来**。基础参见 [[PY016-装饰器]]。

```python
# ❌ 不加 wraps — help() 和调试器看到的是 wrapper
def deco(func):
    def wrapper(*a, **kw):
        return func(*a, **kw)
    return wrapper

@deco
def greet(): """Say hello"""
    pass

print(greet.__name__)  # 'wrapper'  ← 名字丢了
print(greet.__doc__)   # None       ← 文档没了

# ✅ 加 wraps — 一行恢复
# @functools.wraps(func)
```

---

## 🔍 详细说明

### wraps 到底拷贝了什么？

| 属性 | 不加 wraps | 加 wraps |
|------|-----------|----------|
| `__name__` | `'wrapper'` | `'greet'` |
| `__doc__` | `None` | `'Say hello'` |
| `__module__` | `'__main__'` | 原函数所在模块 |
| `__wrapped__` | 不存在 | 指向原始函数（可绕过装饰器） |

### 谁需要 `__name__` 和 `__doc__`？

- **`help()` / `pydoc`** — 看不到原函数文档
- **Sphinx / ReadTheDocs** — 基于 docstring 生成 API 文档
- **Flask** — 路由名默认用 `func.__name__`
- **调试器 / traceback** — 栈跟踪里显示 `wrapper` 而非原函数名

### 多装饰器中放在哪？

```python
# timer 是内层装饰器，加了 wraps
# log 是外层装饰器，没写 wraps 但不受影响

@log          # 先执行 log（外层）
@timer        # 再执行 timer（内层，有 wraps）
def work(n):
    """Heavy computation."""
    return sum(range(n))

# timer 的 wraps 保护了 work 的 __name__
# log 虽然没写 wraps，但它包装的已经是 timer.wrapper
# （已被 wraps 修复过），所以 log 看到的 __name__ 仍是 'work'
```

> wraps 只需放在**最内层**（离 `def` 最近的）装饰器上。外层可以不加——它们包装的是已经保留过元数据的内层函数。

---

## 📎 例子

```python
import functools, time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - t0:.4f}s")
        return result
    return wrapper

@timer
def compute(n):
    """Compute squares up to n."""
    return [x**2 for x in range(n)]

print(compute.__name__)   # 'compute' ✅
print(compute.__doc__)    # 'Compute squares up to n.' ✅
print(compute.__wrapped__(5))  # [0, 1, 4, 9, 16] ← 绕过装饰器
```

---

## ⚡ 反例 / 边界

1. **wraps 不拷贝函数签名** — IDE 签名提示需要用 `ParamSpec`（Python 3.10+）
2. **wraps 只在定义时执行一次** — 不影响运行时性能
3. **`__wrapped__` 可绕过装饰器** — 测试或调试时有用，生产代码别依赖

---

## 🔗 关联卡片

- [[PY016-装饰器]] — 装饰器基础、三层闭包模型

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
