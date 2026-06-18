---
type: learning
status: 已完成
domain: Python
tags: [Python, 编程语言]
created: 2026-06-12
updated: 2026-06-16
---

# PY012-Python中的集合

## 🎯 学习目标

1. 什么是 Python 中的集合？它有哪些核心特性（无序性、唯一性、可变性）？
2. 如何正确创建集合？为什么不能用 `{}` 创建空集合？
3. 集合的增删查操作有哪些方法？`remove()` 和 `discard()` 有什么区别？
4. 集合支持哪些数学运算（并集、交集、差集、对称差集）？对应的运算符和方法是什么？
5. 集合如何与其他数据结构（列表、元组、字典）互相转换？如何保持顺序去重？
6. 什么是集合推导式（Set Comprehension）？如何使用它快速生成集合？
7. `frozenset` 是什么？它和普通的 `set` 有什么区别？适用于哪些场景？
8. 为什么集合的元素查找速度极快（O(1)）？其底层数据结构是什么？

## 📖 前置知识

在学习集合之前，请确保已掌握：[[PY011-Python中的字典]]

## 📚 核心内容

在 Python 的数据结构世界里，如果说列表（List）是全能战士，字典（Dict）是键值对大师，那么集合（Set）就是那个追求"唯一"与"极速"的效率专家。它源于数学中的集合论，以其独特的**无序性**和**元素唯一性**，在数据去重、成员资格检查以及集合运算等场景中展现出无与伦比的优势。

------

### 集合是什么？核心特性一览

Python 中的集合（Set）是一个**无序的、可变的、元素唯一**的容器。

- **无序性  (Unordered) :** 集合中的元素没有固定的顺序，这意味着你不能通过索引（如  `my_set[0]`）来访问元素。每次打印集合，元素的显示顺序都可能不同。
- **元素唯一性  (Unique Elements) :** 集合中不允许存在重复的元素。当你尝试添加一个已存在的元素时，集合不会发生任何变化。这个特性使其成为数据去重的绝佳工具。
- **可变性  (Mutable) :** 集合本身是可变的，你可以随时添加或删除元素。但请注意，集合中的**元素本身必须是不可变类型**（即可哈希的），例如数字、字符串、元组。列表或字典这类可变对象不能作为集合的元素。

### 集合与其他数据结构对比

为了更清晰地理解集合的定位，我们将其与列表、元组和字典进行对比。

| 特性           | 列表 (List)  | 元组 (Tuple) | 字典 (Dict)      | 集合 (Set)                   |
| -------------- | ------------ | ------------ | ---------------- | ---------------------------- |
| **有序性**     | 有序         | 有序         | 3.7+ 插入有序    | **无序**                     |
| **可变性**     | 可变         | 不可变       | 可变             | **可变**                     |
| **元素唯一性** | 允许重复     | 允许重复     | 键唯一，值可重复 | **元素唯一**                 |
| **索引访问**   | 支持         | 支持         | 通过键访问       | **不支持**                   |
| **核心用途**   | 存储有序序列 | 存储常量序列 | 存储键值对映射   | **去重、快速查找、集合运算** |

### ️集合的创建与初始化

创建集合主要有两种方式，但有一个新手极易踩的"坑"。

1. **使用花括号 `{}`** 这是最直观的方式，但**不能用于创建空集合**。

   ```python
   # 创建包含元素的集合
   fruits = {'apple', 'banana', 'orange'}
   print(fruits)  # 输出: {'banana', 'apple', 'orange'} (顺序可能不同)
   
   # 创建时自动去重
   numbers = {1, 2, 3, 2, 1}
   print(numbers)  # 输出: {1, 2, 3}
   ```

2. **使用 `set()` 构造函数** 这是**创建空集合的唯一正确方式**，也可以从其他可迭代对象（如列表、元组）创建集合。

   ```python
   # 创建空集合
   empty_set = set()
   print(type(empty_set))  # 输出: <class 'set'>
   
   # 从列表创建集合并去重
   my_list = [1, 2, 3, 2, 1]
   my_set = set(my_list)
   print(my_set)  # 输出: {1, 2, 3}
   ```

> **常见错误 `{}` 创建空集合**
>
> 千万不要这样做！`{}` 创建的是一个**空字典 (dictionary)**，而不是空集合。
> ```python
> not_a_set = {}
> print(type(not_a_set))  # 输出: <class 'dict'>
> ```

### 集合的增删改查操作

集合的操作非常直观，但删除操作中有个细节需要注意。

| 操作类型 | 方法/运算符        | 描述                                                   | 代码示例                |
| -------- | ------------------ | ------------------------------------------------------ | ----------------------- |
| **增加** | `add(element)`     | 添加单个元素                                           | `my_set.add(4)`         |
|          | `update(iterable)` | 添加多个元素（来自列表、元组等）                       | `my_set.update([5, 6])` |
| **删除** | `remove(element)`  | 删除指定元素，若元素不存在则**抛出 `KeyError`**        | `my_set.remove(3)`      |
|          | `discard(element)` | 删除指定元素，若元素不存在**则什么也不做**（推荐使用） | `my_set.discard(3)`     |
|          | `pop()`            | **随机**删除并返回一个元素（因为集合无序）             | `item = my_set.pop()`   |
|          | `clear()`          | 清空集合中的所有元素                                   | `my_set.clear()`        |
| **查询** | `in` / `not in`    | 检查元素是否存在，**速度极快 (O(1))**                  | `if 3 in my_set:`       |
|          | `len(set)`         | 获取集合中元素的数量                                   | `len(my_set)`           |

> **常见错误 `remove()` 和 `discard()`**
>
> 当你不确定一个元素是否存在于集合中时，使用 `remove()` 可能会导致程序因 `KeyError` 而崩溃。在这种情况下，使用 `discard()` 是更安全的选择。
>
> ```python
> my_set = {1, 2, 3}
> my_set.remove(4)    #  报错: KeyError: 4
> my_set.discard(4)   #  不会报错，安全执行
> ```

集合没有直接的"修改"操作。如果你想"修改"一个元素，实际上是先删除旧元素，再添加新元素。

### 集合的数学运算

集合最强大的功能之一就是支持数学中的集合运算，这让处理两组数据之间的关系变得异常简单。

假设有两个集合：

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
```

| 运算名称     | 运算符  | 方法                        | 描述                                 | 结果示例                   |
| ------------ | ------- | --------------------------- | ------------------------------------ | -------------------------- |
| **并集**     | `A | B` | `A.union(B)`                | 包含两个集合中所有不重复的元素       | `{1, 2, 3, 4, 5, 6, 7, 8}` |
| **交集**     | `A & B` | `A.intersection(B)`         | 包含两个集合共有的元素               | `{4, 5}`                   |
| **差集**     | `A - B` | `A.difference(B)`           | 包含在A中但不在B中的元素             | `{1, 2, 3}`                |
| **对称差集** | `A ^ B` | `A.symmetric_difference(B)` | 包含在A或B中，但不同时在两者中的元素 | `{1, 2, 3, 6, 7, 8}`       |

此外，还有一些用于判断集合关系的方法：

- `A.issubset(B)`: 判断A是否为B的子集。
- `A.issuperset(B)`: 判断A是否为B的超集。
- `A.isdisjoint(B)`: 判断A和B是否没有交集（即交集为空）。

### 与其他数据结构的转换

集合与其他数据结构的转换非常频繁，尤其是在去重场景下。

```python
# 1. 列表/元组 转 集合 (主要用途：去重)
my_list = [1, 2, 2, 3, 4, 4]
unique_set = set(my_list)
print(unique_set)  # 输出: {1, 2, 3, 4}

# 2. 集合 转 列表/元组
# 注意：转换后的顺序是不确定的！
my_set = {3, 1, 4, 1, 5}
list_from_set = list(my_set)
print(list_from_set)  # 输出可能是 [1, 3, 4, 5]，也可能是其他顺序

# 如果需要排序，可以结合 sorted() 函数
sorted_list = sorted(my_set)
print(sorted_list)  # 输出: [1, 3, 4, 5]

# 3. 保持顺序的去重技巧
# 如果想对列表去重并保持原有顺序，可以使用 dict.fromkeys()
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique_ordered_list = list(dict.fromkeys(original_list))
print(unique_ordered_list)  # 输出: [3, 1, 4, 5, 9, 2, 6]
```

> **常见错误**
>
> 由于集合是无序的，当你把它转换成列表时，元素的顺序是无法保证的。如果你需要一个有序且无重复的列表，记得在转换后使用 `sorted()` 函数。

### 补充知识

1. **集合推导式 (Set Comprehension)** 和列表推导式类似，集合推导式提供了一种简洁的方式来创建集合。

   ```python
   # 创建一个包含0-9平方的集合
   squares = {x**2 for x in range(10)}
   print(squares)  # 输出: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
   
   # 带条件的集合推导式
   even_squares = {x**2 for x in range(10) if x % 2 == 0}
   print(even_squares)  # 输出: {0, 4, 16, 36, 64}
   ```

2. **不可变集合 (frozenset)** 标准的 `set` 是可变的，因此它本身是不可哈希的，不能作为另一个集合的元素或字典的键。`frozenset` 就是为了解决这个问题而生的。它一旦创建，内容就无法更改。

   ```python
   # 创建 frozenset
   fs = frozenset([1, 2, 3])
   # fs.add(4)  #  报错: AttributeError，不可变
   
   # 作为另一个集合的元素
   set_of_sets = {fs, frozenset([4, 5, 6])}
   print(set_of_sets)
   
   # 作为字典的键
   my_dict = {fs: "这是一个不可变集合"}
   print(my_dict[fs])  # 输出: 这是一个不可变集合
   ```

3. **性能优势：为什么集合查找这么快？** 集合的底层是基于**哈希表 (Hash Table)** 实现的。这意味着检查一个元素是否在集合中（`x in my_set`）的时间复杂度接近 O(1)，无论集合有多大，查找速度都几乎不变。相比之下，在列表中查找元素的时间复杂度是 O(n)，需要逐个遍历，数据量大时速度会慢得多。

   ```python
   # 性能对比示例
   import time
   
   large_list = list(range(1000000))
   large_set = set(large_list)
   
   # 列表查找 (慢)
   start = time.time()
   999999 in large_list
   print(f"列表查找耗时: {time.time() - start:.5f}秒")  # 耗时较长
   
   # 集合查找 (快)
   start = time.time()
   999999 in large_set
   print(f"集合查找耗时: {time.time() - start:.5f}秒")  # 几乎是瞬间完成
   ```

## 🧪 练习 / 验证

### 练习 1：创建集合并去重

将以下列表转换为集合，观察重复元素是否被自动去除。

```python
my_list = [1, 2, 3, 2, 4, 5, 3, 1, 6, 5]
unique_set = set(my_list)
print(unique_set)
```

**答案：**
```
{1, 2, 3, 4, 5, 6}
```
（元素顺序可能与上述不同，因为集合是无序的）

---

### 练习 2：集合的增删操作

写出以下代码的输出，并解释 `remove()` 和 `discard()` 的区别。

```python
fruits = {'apple', 'banana', 'orange'}

fruits.add('grape')
print(f'A: {fruits}')

fruits.discard('mango')
print(f'B: {fruits}')

fruits.remove('mango')   # 这行会发生什么？
```

**答案：**
```
A: {'apple', 'banana', 'orange', 'grape'}
B: {'apple', 'banana', 'orange', 'grape'}
第三行: KeyError: 'mango'
```
**解释：** `discard()` 删除不存在的元素时静默无操作；`remove()` 在元素不存在时抛出 `KeyError`，程序会崩溃。

---

### 练习 3：集合数学运算

使用 Python 计算以下两组数据的并集、交集、差集和对称差集。

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f'并集 (A|B):    {A | B}')
print(f'交集 (A&B):    {A & B}')
print(f'差集 (A-B):    {A - B}')
print(f'差集 (B-A):    {B - A}')
print(f'对称差 (A^B):  {A ^ B}')
```

**答案：**
```
并集 (A|B):    {1, 2, 3, 4, 5, 6, 7, 8}
交集 (A&B):    {4, 5}
差集 (A-B):    {1, 2, 3}
差集 (B-A):    {6, 7, 8}
对称差 (A^B):  {1, 2, 3, 6, 7, 8}
```

---

### 练习 4：列表去重并保持原有顺序

给定一个包含重复元素的列表，请去除重复元素的同时**保持原始顺序**。

```python
original = [4, 2, 5, 2, 7, 4, 8, 5, 1, 7]
unique_ordered = list(dict.fromkeys(original))
print(unique_ordered)
```

**答案：**
```
[4, 2, 5, 7, 8, 1]
```

---

### 练习 5：集合推导式

使用集合推导式创建以下集合：
1. 0 到 9 之间所有偶数的平方集合
2. 0 到 20 之间所有能被 3 整除的数的集合

```python
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f'偶数平方: {even_squares}')

multiples_of_3 = {x for x in range(21) if x % 3 == 0}
print(f'3的倍数: {multiples_of_3}')
```

**答案：**
```
偶数平方: {0, 4, 16, 36, 64}
3的倍数: {0, 3, 6, 9, 12, 15, 18}
```

---

### 练习 6：frozenset 的使用

完成以下代码，理解 frozenset 的用途。

```python
# 创建两个 frozenset
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# frozenset 支持集合运算吗？试试看
print(f'交集: {fs1 & fs2}')
print(f'并集: {fs1 | fs2}')

# 能否将 frozenset 放入普通 set？
nested = {fs1, fs2}
print(f'嵌套集合: {nested}')

# 能否将普通 set 放入普通 set？
try:
    { {1, 2}, {3, 4} }
except TypeError as e:
    print(f'错误: {e}')
```

**答案：**
```
交集: frozenset({3})
并集: frozenset({1, 2, 3, 4, 5})
嵌套集合: {frozenset({1, 2, 3}), frozenset({3, 4, 5})}
错误: unhashable type: 'set'
```
**解释：** frozenset 支持所有集合运算，且因为不可变（可哈希），可以作为另一个集合的元素。普通 set 不可哈希，无法嵌套。

---

### 练习 7：成员检查性能对比

运行以下代码，观察列表与集合在成员检查上的性能差异。

```python
import time

data = list(range(1000000))
list_container = data
set_container = set(data)

# 列表查找
start = time.time()
result_list = 999999 in list_container
list_time = time.time() - start

# 集合查找
start = time.time()
result_set = 999999 in set_container
set_time = time.time() - start

print(f'列表查找 999999: {result_list}, 耗时 {list_time:.6f} 秒')
print(f'集合查找 999999: {result_set}, 耗时 {set_time:.6f} 秒')
print(f'集合比列表快约 {list_time / set_time:.0f} 倍')
```

**答案（示例输出）：**
```
列表查找 999999: True, 耗时 0.025034 秒
集合查找 999999: True, 耗时 0.000035 秒
集合比列表快约 715 倍
```
实际倍数取决于硬件，但集合查找始终比列表查找快数个数量级（O(1) vs O(n)）。

---

### 练习 8：子集、超集与不相交判断

写出以下代码的输出。

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}

print(f'A 是 B 的子集: {A.issubset(B)}')
print(f'B 是 A 的超集: {B.issuperset(A)}')
print(f'A 与 C 无交集: {A.isdisjoint(C)}')
print(f'B 与 C 无交集: {B.isdisjoint(C)}')
```

**答案：**
```
A 是 B 的子集: True
B 是 A 的超集: True
A 与 C 无交集: True
B 与 C 无交集: True
```

---

## 🤔 常见误区

1. **用 `{}` 创建空集合**
   - **错误做法：** `empty = {}`
   - **事实：** `{}` 创建的是空字典（`<class 'dict'>`），而不是空集合。创建空集合必须使用 `set()`。
   - **正确做法：** `empty = set()`

2. **混淆 `remove()` 与 `discard()` 的行为**
   - **错误认知：** 两者行为完全一样，只是名字不同。
   - **事实：** `remove(element)` 在元素不存在时抛出 `KeyError` 异常；`discard(element)` 在元素不存在时静默无操作。当不确定元素是否存在时，应使用 `discard()`。

3. **试图将可变对象放入集合**
   - **错误做法：** `my_set = {[1, 2], [3, 4]}`
   - **事实：** 集合中的元素必须是不可变（可哈希）类型。列表、字典、普通集合本身都不能作为集合的元素。如需嵌套集合，使用 `frozenset`。
   - **正确做法：** `my_set = {frozenset([1, 2]), frozenset([3, 4])}`

4. **假设集合是有序的或可以通过索引访问**
   - **错误认知：** 集合像列表一样有顺序，可以通过 `my_set[0]` 访问。
   - **事实：** 集合是无序的，不支持索引访问（`TypeError: 'set' object is not subscriptable`）。将集合转换为列表后的顺序也不确定，如需有序去重，使用 `dict.fromkeys()` 技巧。

5. **低估集合查找的性能优势**
   - **错误认知：** 小数据量用列表 `in` 就够了，集合和列表差不多。
   - **事实：** 集合基于哈希表实现，成员检查时间复杂度为 O(1)；列表需要逐个遍历 O(n)。在大量成员检查的场景下（如循环中反复判断），使用集合可获得数十到数千倍的性能提升。

## 🔗 相关资源

- 上一节：[[PY011-Python中的字典]]
- 下一节：[[PY013-Python中的条件与循环]]
- Python 官方文档（集合）：https://docs.python.org/zh-cn/3/tutorial/datastructures.html#sets
- Python 官方文档（frozenset）：https://docs.python.org/zh-cn/3/library/stdtypes.html#frozenset
