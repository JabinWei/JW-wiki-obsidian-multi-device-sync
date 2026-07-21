---
type: card
status: 已完成
aliases: [__name__, __main__, 模块入口, 双重身份]
tags: [编程语言, Python]
created: 2026-07-20
updated: 2026-07-20
---

## 💡 核心概念

每个 Python 文件都有一个内置变量 `__name__`。它让同一个 `.py` 文件拥有**双重身份**——直接运行时是程序入口，被导入时是普通模块。基础参见 [[PY019-模块]]。

| 运行方式 | `__name__` 的值 | `if` 判断 |
|----------|----------------|-----------|
| `python script.py` | `'__main__'` | ✅ 执行 |
| `import script` | `'script'`（文件名） | ❌ 跳过 |

---

## 🔍 详细说明

### 1. 解释器在幕后做了什么

```
python calc.py
    ↓
解释器读取 calc.py
    ↓
设置 __name__ = '__main__'   ← 因为是直接运行
    ↓
逐行执行，遇到 if __name__ == '__main__': → True → 执行
```

```
import calc
    ↓
解释器读取 calc.py
    ↓
设置 __name__ = 'calc'       ← 因为是导入
    ↓
逐行执行，遇到 if __name__ == '__main__': → False → 跳过
```

### 2. 标准工程化写法

```python
# calculator.py
def add(a, b):
    return a + b

def main():
    import sys
    print(add(int(sys.argv[1]), int(sys.argv[2])))

if __name__ == '__main__':
    main()
```

- `python calculator.py 3 5` → 执行 `main()`，输出 8
- `import calculator` → 只定义函数，不执行 `main()`

---

## 📎 例子

```python
# 调试代码与模块共存
def process_data(data):
    return [x * 2 for x in data]

if __name__ == '__main__':
    print(process_data([1, 2, 3]))  # 直接运行测试，导入时跳过

# 单元测试入口
if __name__ == '__main__':
    import unittest
    unittest.main()

# 性能分析入口
if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
```

---

## ⚡ 反例 / 边界

1. **不要把业务逻辑直接写进 `if` 块** — 该块应只放入口调度（`main()` 调用、参数解析），业务逻辑封装为独立函数
2. **循环导入时 `__name__` 可能不是预期值** — 模块 A 导入 B，B 又导入 A 时，未完成加载阶段变量状态不确定
3. **C / Java 没有等价物** — 那些语言用 `main()` 函数作为显式入口，Python 用 `__name__` 判断替代

---

## 🔗 关联卡片

- [[PY019-模块]] — 基础用法与 `__name__` 解释
- [[PY014-函数]] — `main()` 函数定义

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
