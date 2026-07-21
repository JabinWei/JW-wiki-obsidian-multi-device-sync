---
type: card
status: 已完成
aliases: [for else, while else, nobreak, 循环else]
tags: [编程语言, Python]
created: 2026-07-20
updated: 2026-07-20
---

## 💡 核心概念

Python 的 `else` 可以绑定到 `for`/`while` 循环。**`else` 块仅在循环正常结束（未遇到 `break`）时执行。** 基础用法参见 [[PY013-条件与循环#for...else 结构]]。

记忆规则：**No break → else 执行。**

---

## 🔍 详细说明

### 1. 两种写法对比

```python
# 方法 A：标志变量（传统风格）
found = False
for item in items:
    if match(item):
        found = True
        break
if not found:
    handle_not_found()

# 方法 B：for...else（Python 风格）
for item in items:
    if match(item):
        break
else:
    handle_not_found()
```

### 2. while...else 同理

```python
# 正常退出循环 → else 执行
count = 3
while count > 0:
    count -= 1
else:
    print("倒计时结束")

# 有 break → else 跳过
while True:
    if done():
        break
else:
    print("永远不会执行")
```

### 3. 为什么叫 else？

Guido van Rossum 解释：这里的 `else` 语义更接近「then」（循环完成之后），而不是「otherwise」。理解为 `nobreak` 最准确。

---

## 📎 例子

```python
# 搜索匹配
for user in users:
    if user['name'] == target:
        return user
else:
    raise ValueError(f"用户 {target} 不存在")

# 素数判断
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

# 重试机制
for attempt in range(3):
    if api_call():
        break
else:
    raise TimeoutError("重试 3 次均失败")
```

---

## ⚡ 反例 / 边界

1. **空循环也会触发 else**：`for x in []: pass` → `else` 执行
2. **`continue` 不影响**：只是跳过当次迭代，else 仍然执行
3. **`return`/`raise` 同样跳过 else**：任何跳出循环的方式都算「非正常结束」
4. **Python 独有语法**：Java/JavaScript/C 无此结构

---

## 🔗 关联卡片

- [[PY013-条件与循环#for...else 结构]] — 基础用法与示例
- [[PY023-错误类型与异常处理机制]] — try...else 类似逻辑

---

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
