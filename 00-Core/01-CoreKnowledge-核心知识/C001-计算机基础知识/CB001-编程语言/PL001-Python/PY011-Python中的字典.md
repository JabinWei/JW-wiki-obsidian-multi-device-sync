---
type: learning
status: 已完成
domain: Python
tags: [Python, 编程语言]
created: 2026-06-12
updated: 2026-06-16
---

# Python 中的字典

## 🎯 学习目标

1. 字典是什么？它与列表、元组等序列类型的本质区别是什么？
2. 如何安全地访问字典中的值，避免 `KeyError` 崩溃？
3. `update()` 方法的原理是什么？它能否链式调用？
4. 浅拷贝与深拷贝的区别是什么？什么场景下必须使用深拷贝？
5. `fromkeys()` 和 `setdefault()` 分别适用于什么场景？
6. 如何在字典与 JSON 字符串之间安全转换？
7. 字典推导式能做哪些批量操作？

## 📖 前置知识

在学习本文之前，请确保已掌握：[[PY010-Python中的元组]]

## 📚 核心内容

字典（Dictionary）是 Python 中唯一的一种**映射型**数据结构。它由一系列**键值对（Key-Value Pair）**组成，每个键（Key）都与一个值（Value）关联。

想象一下你手中的字典：通过“单词”（键）快速找到“解释”（值）。在编程中，这种结构处理结构化数据时效率极高。

------

### 基础定义与创建

字典中的键必须是**不可变类型**（如字符串、数字、元组），且在字典中只能出现一次（唯一性）。值可以是任意数据类型。

#### 常见的创建方式

最常用的是使用花括号 `{}`，但 `dict()` 构造函数其实非常强大，支持多种参数形式。

| 方式           | 说明                                 | 示例代码                                 |
| -------------- | ------------------------------------ | ---------------------------------------- |
| **花括号**     | 最直观，直接定义                     | `{'name': 'Jason', 'age': 25}`           |
| **二维列表**   | 列表套列表，每对必须是2个元素        | `dict([['name', 'sun'], ['score', 90]])` |
| **元组列表**   | 列表套元组，常用于数据库查询结果转换 | `dict()`                                 |
| **字符串列表** | 字符串长度必须为2（键, 值）          | `dict(['12', '34'])`                     |

```python
#  技巧：使用 zip 函数合并两个列表创建字典
keys = ['name', 'age', 'city']
values = ['Jason', 25, 'Beijing']
person = dict(zip(keys, values))
# 输出: {'name': 'Jason', 'age': 25, 'city': 'Beijing'}
```

------

### 核心操作：访问、增、删、改

#### 1. 字典的访问方式

在开发中，访问不存在的键是导致程序崩溃（`KeyError`）的常见原因。我们需要掌握**安全访问**的技巧。

| 方式         | 语法                     | 特点                             | 推荐指数           |
| ------------ | ------------------------ | -------------------------------- | ------------------ |
| **直接访问** | `dict[key]`              | 键不存在直接报错                 | (仅限确定键存在时) |
| **安全访问** | `dict.get(key, default)` | **键不存在返回默认值，程序不崩** | (强烈推荐)         |

```python
person = {'name': 'Jason', 'age': 25}

#  危险操作：如果'id'不存在，程序会抛出 KeyError
# print(person['id']) 

#  推荐操作：安全获取，如果没有则返回 "未知"
user_id = person.get('id', "未知")
print(user_id) # 输出: 未知
```

**批量访问（遍历）**

当你需要处理字典中的所有数据时，Python 提供了三个核心方法：`.items()`、`.keys()` 和 `.values()`。它们返回的是**视图对象**，动态且节省内存。

- **`.items()`**：同时获取键和值（最常用）。
- **`.keys()`**：仅获取键。
- **`.values()`**：仅获取值。

```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust'}

# 1. 遍历键值对 (推荐写法)
for name, language in favorite_languages.items():
    print(f"{name.title()}: {language.title()}")

# 2. 遍历键
for name in favorite_languages.keys():
    print(name)

# 3. 遍历值 (结合 set 去重)
print("Languages mentioned:")
for language in set(favorite_languages.values()):
    print(language)
```

#### 2. 添加与修改

你可以直接通过赋值来修改，也可以使用 `update()` 进行批量操作。

**`update()` 方法的原理与用法**

`update()` 是字典的“批量更新神器”，它的核心原理是**就地修改（In-place Modification）**。

- **原理机制**：
  1. **覆盖与添加**：它会遍历传入的字典或键值对。如果键已存在，则**覆盖**旧值；如果键不存在，则**添加**新键值对。
  2. **无返回值**：它直接修改原字典对象，返回值为 `None`。这意味着你不能链式调用（如 `d.update(...).update(...)` 会报错）。
  3. **浅更新**：如果值是可变对象（如嵌套字典），它只会替换引用，而不会递归合并内部数据。

```python
person = {'name': 'Jason', 'age': 25}

# 1. 直接赋值（单点修改）
person['job'] = 'Engineer'  # 添加
person['age'] = 26          # 修改

# 2. 使用 update() 批量更新（推荐）
# 场景A：传入另一个字典
person.update({'city': 'Beijing', 'gender': 'male'})

# 场景B：传入关键字参数
person.update(age=27)

# 注意：print(person.update(...)) 会输出 None
```

#### 3. 删除

Python 提供了多种删除方式，根据场景选择最合适的一种。

| 方法            | 语法                     | 说明                                               |
| --------------- | ------------------------ | -------------------------------------------------- |
| **`del`**       | `del dict[key]`          | 简单直接，键不存在会报错。                         |
| **`pop()`**     | `dict.pop(key, default)` | **最安全**。删除并返回被删除的值，支持默认值防错。 |
| **`popitem()`** | `dict.popitem()`         | 删除**最后一个**插入的键值对（类似栈）。           |
| **`clear()`**   | `dict.clear()`           | 清空整个字典。                                     |

**使用字典推导式进行批量/条件删除**

```python
data = {'a': 1, 'b': 2, 'c': None, 'd': 4}

# 场景：删除所有值为 None 的项
clean_data = {k: v for k, v in data.items() if v is not None}
# 输出: {'a': 1, 'b': 2, 'd': 4}
```

------

### 字典的复制：浅拷贝与深拷贝

这是一个经典的面试题，也是实际开发中的“坑”。直接赋值 `new_dict = old_dict` 只是复制了引用（别名），修改新字典会影响原字典。

#### 1. 浅拷贝

创建了新字典，但内部的可变元素（如列表）仍然指向同一内存地址。

- **方法**：`dict.copy()` 或 `dict(old_dict)`
- **后果**：修改新字典里的**列表**，原字典也会变。

#### 2. 深拷贝

完全克隆，包括嵌套的列表和字典。

- **方法**：`import copy; copy.deepcopy(old_dict)`
- **后果**：新旧字典完全独立，互不干扰。

#### 3. 代码示例对比

```python
import copy

# 原始字典，包含一个嵌套列表
original = {'name': 'Jason', 'skills': ['Python', 'Java']}

# --- 浅拷贝演示 ---
shallow_copy = original.copy()
shallow_copy['name'] = 'Mike'          # 修改不可变值
shallow_copy['skills'].append('C++')   # 修改可变列表

print(f"原始字典 (浅拷贝后): {original}")
# 输出: {'name': 'Jason', 'skills': ['Python', 'Java', 'C++']}
# 注意：skills 列表被修改了！

# --- 深拷贝演示 ---
deep_copy = copy.deepcopy(original)
deep_copy['skills'].append('Go')       # 修改列表

print(f"原始字典 (深拷贝后): {original}")
# 输出: {'name': 'Jason', 'skills': ['Python', 'Java', 'C++']}
# 注意：skills 列表未受影响，Go 没有加进来
```

------

### 多结构嵌套

字典的灵活性在于它可以无限嵌套，非常适合表示 JSON 格式的数据。

#### 1. 字典列表

用于管理多个同类型的对象（如用户列表、商品列表）。

```python
aliens = []
for i in range(3):
    aliens.append({'color': 'green', 'points': 5})
```

#### 2. 字典中的字典

用于表示复杂的层级关系（如用户信息）。

```python
users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein'},
    'mcurie': {'first': 'marie', 'last': 'curie'}
}
```

------

### ️ 补充两个常用的方法

除了基础操作，这两个方法能让你的代码更 Pythonic。

#### 1. `fromkeys()`：快速初始化

当你需要创建一个包含多个键，且初始值都一样的字典时（比如初始化计数器）。

```python
# 初始化商品库存，默认都为 0
products = ['apple', 'banana', 'orange']
stock = dict.fromkeys(products, 0)
# 输出: {'apple': 0, 'banana': 0, 'orange': 0}
```

#### 2. `setdefault()`：智能设置默认值

“如果有就返回，没有就创建”。这在处理日志或统计时非常有用。

```python
user_info = {'name': 'Jason'}

# 键不存在：自动添加 'city': 'Beijing' 并返回 'Beijing'
city = user_info.setdefault('city', 'Beijing')

# 键已存在：不做任何修改，直接返回原值 'Jason'
name = user_info.setdefault('name', 'Mike') 
```

------

### 字典与其他数据结构的转换

#### 字典与列表的转换

这是最常见的转换场景，通常涉及提取键、值或键值对。

**1. 字典 → 列表**
当你直接使用 `list()` 转换字典时，默认提取的是**所有的键**。如果需要提取值或键值对，需要配合字典的方法使用。

| 转换目标       | 方法                  | 代码示例                          | 结果         |
| -------------- | --------------------- | --------------------------------- | ------------ |
| **提取键**     | `list(dict)`          | `list({'a': 1, 'b': 2})`          | `['a', 'b']` |
| **提取值**     | `list(dict.values())` | `list({'a': 1, 'b': 2}.values())` | `[1, 2]`     |
| **提取键值对** | `list(dict.items())`  | `list({'a': 1, 'b': 2}.items())`  | ``           |

**2. 列表 → 字典**
列表转字典稍微复杂一点，列表的结构必须能被解析为“键-值”关系。

- **场景 A：嵌套列表/元组（最常用）**
  列表中的每个元素也是一个包含两个元素的容器（如 `[键, 值]` 或 `('键', '值')`）。

  ```python
  data = [['name', 'Jason'], ['age', 25]]
  print(dict(data))
  # 输出: {'name': 'Jason', 'age': 25}
  ```

- **场景 B：两个列表合并**
  如果你有两个列表，一个存键，一个存值，可以使用 `zip()` 函数将它们打包后再转换。

  ```python
  keys = ['name', 'age']
  values = ['Jason', 25]
  print(dict(zip(keys, values)))
  # 输出: {'name': 'Jason', 'age': 25}
  ```

#### 字典与字符串的转换

这种转换通常用于数据的持久化存储（如写入文件）或网络传输（如 API 接口）。

**1. 字典 → 字符串**
虽然可以直接用 `str()` 强转，但在实际开发中，我们更推荐使用 JSON 格式。

- **方法 A：`json.dumps()`（推荐）**
  生成标准的 JSON 格式字符串，键名强制为双引号，兼容性最好。

  ```python
  import json
  d = {'name': 'Jason', 'age': 25}
  s = json.dumps(d)
  print(s) # 输出: {"name": "Jason", "age": 25}
  ```

- **方法 B：`str()`**
  直接转换为 Python 对象的字符串表示，键名通常是单引号。仅适用于简单的调试打印。

  ```python
  d = {'name': 'Jason'}
  print(str(d)) # 输出: {'name': 'Jason'}
  ```

**2. 字符串 → 字典**
将字符串还原为字典，通常是因为接收到了 JSON 数据。

- **方法 A：`json.loads()`（推荐）**
  安全、标准地将 JSON 字符串解析为字典。

  ```python
  import json
  s = '{"name": "Jason", "age": 25}'
  d = json.loads(s)
  print(d['name']) # 输出: Jason
  ```

- **方法 B：`eval()`（慎用！）**
  虽然 `eval()` 可以将字符串当作 Python 代码执行从而转换字典，但它存在巨大的**安全漏洞**（如果字符串来源不可信，可能导致代码注入）。除非你完全信任数据源，否则**不要使用**。

#### 字典与元组、集合的转换

**1. 字典 元组**

- **字典 → 元组**：规则与转列表类似，`tuple(dict)` 默认提取键。

  ```python
  d = {'a': 1, 'b': 2}
  print(tuple(d)) # 输出: ('a', 'b')
  ```

- **元组 → 字典**：元组内必须包含成对的键值数据。

  ```python
  t = (('a', 1), ('b', 2))
  print(dict(t)) # 输出: {'a': 1, 'b': 2}
  ```

**2. 字典 集合**

- **字典 → 集合**：`set(dict)` 默认提取键，且集合具有**去重**和**无序**的特性。

  ```python
  d = {'a': 1, 'b': 2}
  print(set(d)) # 输出: {'a', 'b'} (顺序可能不同)
  ```

- **集合 → 字典**：**不能直接转换**。因为字典需要键值对，而集合只有单个元素。通常需要先通过逻辑处理将集合转换为列表或元组（成对形式），再转为字典。

## 🧪 练习 / 验证

### 练习 1：安全访问与默认值

**题目**：给定字典 `config = {'host': 'localhost', 'port': 8080}`，分别使用 `get()` 方法安全获取键 `'host'`、`'debug'`（不存在，返回 `False`）、`'timeout'`（不存在，返回 `30`）。

**答案**：

```python
config = {'host': 'localhost', 'port': 8080}

print(config.get('host'))         # 'localhost'
print(config.get('debug', False)) # False
print(config.get('timeout', 30))  # 30

# 字典本身不会因此增加新的键
print(config)
# 输出: {'host': 'localhost', 'port': 8080}
```

---

### 练习 2：使用 update() 批量更新

**题目**：字典 `user = {'name': 'Alice', 'age': 25}`。执行以下操作后，字典的内容是什么？`update()` 调用本身的返回值是什么？

```python
result = user.update({'age': 26, 'city': 'Shanghai'})
```

**答案**：

```python
user = {'name': 'Alice', 'age': 25}

result = user.update({'age': 26, 'city': 'Shanghai'})

print(user)   # {'name': 'Alice', 'age': 26, 'city': 'Shanghai'}
print(result) # None

# 解释：update() 就地修改原字典，无返回值。'age' 被覆盖，'city' 被新增。
```

---

### 练习 3：浅拷贝 vs 深拷贝

**题目**：运行以下代码，写出每一行 `print` 的输出结果。

```python
import copy

data = {'nums': [1, 2, 3], 'name': 'test'}

shallow = data.copy()
shallow['nums'].append(4)
shallow['name'] = 'changed'

deep = copy.deepcopy(data)
deep['nums'].append(5)

print(data['nums'])
print(data['name'])
print(deep['nums'])
```

**答案**：

```python
print(data['nums'])  # [1, 2, 3, 4]
print(data['name'])  # 'test'
print(deep['nums'])  # [1, 2, 3, 4, 5]

# 解释：
# - shallow['nums'].append(4) 修改了共享的列表，因此 data['nums'] 也变了。
# - shallow['name'] = 'changed' 修改的是不可变字符串，会创建新对象，data['name'] 不受影响。
# - deep['nums'].append(5) 修改的是完全独立的副本，不影响 data。
```

---

### 练习 4：字典推导式过滤与转换

**题目**：给定 `scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}`，使用字典推导式创建一个新字典，仅包含分数 >= 90 的学生，且将分数转换为等级（>= 90 → 'A'）。

**答案**：

```python
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}

grades = {name: 'A' for name, score in scores.items() if score >= 90}
print(grades)
# 输出: {'Bob': 'A', 'David': 'A'}
```

---

### 练习 5：setdefault() 统计词频

**题目**：使用 `setdefault()` 统计字符串 `"apple banana apple orange banana apple"` 中每个单词的出现次数，结果应为一个字典。

**答案**：

```python
text = "apple banana apple orange banana apple"
words = text.split()

word_count = {}
for word in words:
    word_count.setdefault(word, 0)
    word_count[word] += 1

# 更简洁的写法（setdefault 返回当前值）：
word_count = {}
for word in words:
    count = word_count.setdefault(word, 0)
    word_count[word] = count + 1

print(word_count)
# 输出: {'apple': 3, 'banana': 2, 'orange': 1}
```

---

### 练习 6：安全删除键

**题目**：给定 `inventory = {'sword': 1, 'shield': 2, 'potion': 5}`，使用 `pop()` 安全删除键 `'shield'`（打印被删除的值），并尝试删除不存在的键 `'helmet'`，设置默认返回值为 `'not found'`。

**答案**：

```python
inventory = {'sword': 1, 'shield': 2, 'potion': 5}

removed = inventory.pop('shield')
print(removed)   # 2（被删除的值）

not_found = inventory.pop('helmet', 'not found')
print(not_found) # 'not found'

print(inventory)
# 输出: {'sword': 1, 'potion': 5}
```

---

### 练习 7：字典与 JSON 互转

**题目**：将字典 `data = {'user': 'Jason', 'active': True, 'score': None, 'items': [1, 2, 3]}` 转换为 JSON 字符串，然后再从 JSON 字符串还原为字典，并验证还原后的字典与原字典是否相等。

**答案**：

```python
import json

data = {'user': 'Jason', 'active': True, 'score': None, 'items': [1, 2, 3]}

# 字典 → JSON 字符串
json_str = json.dumps(data)
print(json_str)
# 输出: {"user": "Jason", "active": true, "score": null, "items": [1, 2, 3]}
# 注意：True → true, None → null（JSON 标准）

# JSON 字符串 → 字典
restored = json.loads(json_str)
print(restored)
# 输出: {'user': 'Jason', 'active': True, 'score': None, 'items': [1, 2, 3]}

print(restored == data)  # True
```

---

### 练习 8：fromkeys() 的陷阱

**题目**：以下代码有什么问题？如何修正？

```python
matrix = dict.fromkeys(['row1', 'row2', 'row3'], [])
matrix['row1'].append(1)
print(matrix)
```

**答案**：

```python
# 问题代码的输出：
# {'row1': [1], 'row2': [1], 'row3': [1]}
# 所有键共享同一个列表对象！因为 fromkeys() 只为第二个参数创建一次对象。

# 修正方法：使用字典推导式，为每个键创建独立的空列表
matrix = {k: [] for k in ['row1', 'row2', 'row3']}
matrix['row1'].append(1)
print(matrix)
# 输出: {'row1': [1], 'row2': [], 'row3': []}
```

## 🤔 常见误区

1. **误区：`get()` 找不到键时会自动将键写入字典。**
   - **事实**：`get()` 是纯读取操作，不会修改字典。它只是在找不到键时**返回**默认值，键不会被添加到字典中。如需“没有则创建”，请使用 `setdefault()`。

2. **误区：`update()` 可以用 `.` 链式调用。**
   - **事实**：`update()` 的返回值是 `None`，链式调用（如 `d.update(a).update(b)`）会在第二步抛出 `AttributeError`。需要多次更新时，分多行调用或在一次 `update()` 中传入全部数据。

3. **误区：字典的 `copy()` 方法能完全复制嵌套字典。**
   - **事实**：`copy()` 是浅拷贝，嵌套的可变对象（如字典内的列表、字典）仍然共享引用。修改嵌套对象会影响原字典。需要完全独立的副本时请使用 `copy.deepcopy()`。

4. **误区：`fromkeys()` 为每个键创建独立的值对象。**
   - **事实**：`dict.fromkeys(keys, [])` 中，`[]` 只被创建一次，所有键都指向同一个列表对象。对任一键的值做原地修改会影响所有键。可变默认值请用字典推导式代替。

5. **误区：字典的键可以直接使用列表。**
   - **事实**：字典的键必须是**可哈希（hashable）**的不可变类型。列表是可变类型，不可哈希，不能作为字典的键。可以作为键的类型包括：字符串、数字、元组（元组内的元素也必须全是不可变类型）、`frozenset` 等。

## 🔗 相关资源

- 上一节：[[PY010-Python中的元组]]
- 下一节：[[PY012-Python中的集合]]
- 官方文档：[Python 字典类型 — docs.python.org](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- 拓展阅读：[Python 官方教程 — 字典](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
