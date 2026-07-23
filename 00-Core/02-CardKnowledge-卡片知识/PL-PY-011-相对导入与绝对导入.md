---
type: card
status: 已完成
aliases: [import, 绝对导入, 相对导入, -m, __package__, 导入报错]
tags: [编程语言, Python]
created: 2026-07-20
updated: 2026-07-20
---

## 💡 核心概念

**绝对导入**：从 `sys.path` 中的某个目录出发，写出完整路径。**相对导入**：从当前模块的 `__package__` 位置出发，用 `.` 和 `..` 描述相对路径。基础参见 [[PY019-模块]]。

```python
# 绝对导入 — 走 sys.path 从头找
from my_project.utils import helper

# 相对导入 — 走 __package__ 当锚点
from . import helper         # 同级
from ..utils import helper   # 上级
```

---

## 🔍 详细说明

### 1. 绝对导入 — 从根出发

```python
# 写完整路径，Python 从 sys.path 里面依次搜索
import my_project.utils.helper
from my_project.core.engine import start
```

### 2. 相对导入 — 从锚点出发

```python
# 文件位置：my_project/core/engine.py
# 运行方式：python -m my_project.core.engine
# Python 自动设置：__package__ = 'my_project.core'

from . import config        # → my_project.core.config
from ..utils import helper  # → my_project.utils.helper
from ... import base        # → my_project.base
```

`__package__` 就是锚点，`.` 和 `..` 基于它做路径运算。

### 3. 什么时候用哪种

| 场景 | 推荐 | 原因 |
|------|:--:|------|
| 跨大层级调用 | 绝对导入 | 路径清晰，重构友好 |
| 包内部组织 | 相对导入 | 包名变了不会断，移动整个包也不怕 |
| 第三方库引用 | 绝对导入 | 无歧义 |

---

## 📎 例子

```python
# 项目结构
my_project/
├── __init__.py
├── utils/
│   └── helper.py
└── core/
    └── engine.py

# core/engine.py — 两种写法都合法
from my_project.utils import helper   # 绝对
from ..utils import helper            # 相对

# 运行：python -m my_project.core.engine
```

---

## ⚡ 反例 / 边界

1. **不能用相对导入跳到包外面** — `..` 最多退到顶级包，再退报错
2. **相对导入只适用于包内** — `python -m` 的入口文件不能用相对导入（它是 `__main__`，不属于任何包）

---

## ❓ 常见疑问

**Q: 为什么 `python my_project/core/engine.py` 报相对导入错误？**
A: 直接 `python xxx.py` 运行时 `__package__ = None`，`.` 没有锚点。必须用 `python -m my_project.core.engine`。

**Q: `cd` 到模块目录下再 `python engine.py` 也不行？**
A: 不行。`cd` 只改变终端目录，Python 照样当孤立脚本跑，`__package__` 还是 `None`。

**Q: `-m` 后面用 `.` 和 `/` 有区别吗？**
A: 有。`.` 是包路径（`my_project.core.engine`），`/` 是文件路径。`-m` 只认 `.`。

| 运行方式 | `__package__` | 相对导入 |
|----------|:--:|:--:|
| `python -m my_project.core.engine` | `'my_project.core'` | ✅ |
| `python my_project/core/engine.py` | `None` | ❌ |

---

## 🔗 关联卡片

- [[PY019-模块]] — import 基础语法与模块组织

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
