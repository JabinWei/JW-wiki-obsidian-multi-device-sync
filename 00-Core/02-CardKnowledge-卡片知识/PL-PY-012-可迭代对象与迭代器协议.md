---
type: card
status: 已完成
aliases: [迭代器, Iterator, Iterable, 可迭代对象, 迭代器协议, __iter__, __next__]
tags: [编程语言, Python]
created: 2026-08-13
updated: 2026-08-13
---

## 💡 核心概念

Python 用「迭代器协议」统一了「遍历」这件事：
一个对象只要实现了 `__iter__`（返回迭代器）和 `__next__`（返回下一个值，耗尽抛 `StopIteration`），
就能被 `for` 循环遍历。`for` 不关心你是列表、文件还是生成器。

---

## 🔍 详细说明

### 1. 三个概念的关系：谁包含谁

```
可迭代对象 (Iterable)   ← 实现 __iter__，能被 iter() 取出迭代器
   └── 迭代器 (Iterator)  ← 实现 __next__，每次吐一个值，吐完抛 StopIteration
         └── 生成器 (Generator) ← 迭代器的一种，yield 函数 / 生成器表达式自动实现协议
```

用代码验证「谁是什么」：

```python
x = [1, 2, 3]

# 判断是否可迭代：有 __iter__ 就行
print('__iter__' in dir(x))    # True  ← 列表是可迭代对象
# 判断是否是迭代器：要有 __next__
print('__next__' in dir(x))    # False ← 列表不是迭代器，只是可迭代

it = iter(x)                   # 从可迭代对象「取出」迭代器
print('__next__' in dir(it))   # True  ← 这才是迭代器
```

### 2. for 循环背后的真相（解开黑盒）

`for item in x` 其实是一段固定的展开，Python 在背后替你跑：

```python
# for item in x:
#     print(item)
# 完全等价于 ↓

it = iter(x)               # ① 调 __iter__，拿到迭代器
while True:
    try:
        item = next(it)    # ② 调 __next__，拿下一个值
        print(item)
    except StopIteration:  # ③ 没值了，正常退出（不是报错）
        break
```

> 这就是为什么任何实现协议的对象都能被 `for` 遍历——`for` 只认 `iter()` 和 `next()` 这两个接口，不看对象内部长什么样。

### 3. 手动驱动 next()：直接看协议

```python
it = iter([1, 2, 3])
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
print(next(it))   # StopIteration  ← 耗尽后抛这个异常，for 靠它知道「结束了」
```

### 4. 可迭代对象 vs 迭代器：差别到底在哪

**一句话本质**：

- **可迭代对象 = 数据本身**（一本「书」），它不记录你读到哪了
- **迭代器 = 正在读的「书签」**，它记录当前读到哪一页，只能往后翻

> 书永远在那里，读多少遍都还在；书签读完一次就夹在最后一页了，想再读得换个新书签。

**一刀切判据：`iter(x) is x`**

```python
lst = [1, 2, 3]
it = iter(lst)

print(iter(lst) is lst)   # False  ← 列表：iter() 返回的是「新东西」，不是列表自己
print(iter(it) is it)     # True   ← 迭代器：iter() 返回的就是它自己
```

> 这是 Python 官方最干净的判据：
> `iter(x) is x` 为 **False** → 可迭代对象（每次给你一个新书签）
> `iter(x) is x` 为 **True**  → 迭代器（它就是那个书签本身）

**关键：位置存在「迭代器」里，不在「可迭代对象」里**

```python
lst = [1, 2, 3]

it1 = iter(lst)   # 从列表取出书签 1
it2 = iter(lst)   # 再取书签 2

print(next(it1))  # 1
print(next(it2))  # 1  ← it1 已经读了一个，但 it2 不受影响，各自从 1 开始

print(next(it1))  # 2  ← 只有 it1 自己往前走，列表 lst 从头到尾没变过
```

> 看最后一行就懂了：**列表 `lst` 全程没有「位置」这回事**，它只是每次吐出一个「从 0 开始」的新书签；而 `it1` 这个书签自己记着「我读到第 2 个了」。

**对比总表**

| 维度 | 可迭代对象 (Iterable) | 迭代器 (Iterator) |
|------|----------------------|-------------------|
| 本质 | 数据容器（书） | 遍历游标（书签） |
| 记不记「读到哪」 | 不记 | 记 |
| `iter(x) is x` | `False` | `True` |
| 能不能反复遍历 | 能（每次取新书签） | 不能（书签走到头就没了） |
| 直接 `next(x)` | ❌ 报 TypeError | ✅ 可以 |
| 例子 | 列表、元组、字典、字符串、文件 | `iter(列表)`、生成器 |

### 5. 自定义迭代器（协议落地）

自己写一个能被 `for` 遍历的对象，只需要实现两个方法：

```python
class CountUp:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):      # for 先调这个，拿迭代器
        return self          # 迭代器返回自己

    def __next__(self):      # for 每次调这个，拿下一个值
        self.i += 1
        if self.i > self.n:
            raise StopIteration   # 吐完了，通知 for 停下
        return self.i

for x in CountUp(3):
    print(x)   # 1
               # 2
               # 3
```

### 6. 常见的可迭代对象全家福

```python
for x in [1, 2, 3]: ...            # 列表
for k in {'a': 1, 'b': 2}: ...     # 字典（默认遍历键）
for line in open('data.txt'): ...  # 文件（逐行，天生是迭代器）
for i in range(5): ...             # range
for x in (x*2 for x in [1,2,3]): ...  # 生成器表达式
```

---

## ⚡ 反例 / 边界

```python
next([1, 2, 3])
# TypeError: 'list' object is not an iterator
# ← 列表只可迭代，不能直接 next，要先 iter()
```

1. **迭代器是一次性的**：耗尽后不能回退，想再来只能重新 `iter()` 或重新建生成器（同 [[PY015-高阶函数]] 生成器误区）
2. **别把「可迭代」当「迭代器」**：直接 `next(列表)` 会报错，先 `iter()`
3. **一眼判断**：`iter(x) is x` 为 `False` 是可迭代对象，为 `True` 是迭代器

---

## 🔗 关联卡片

- [[PY015-高阶函数]] — `yield` 生成器、`map`/`filter` 返回迭代器
- [[PL-PY-006-Python推导式全家桶]] — 生成器表达式 `(x for x in ...)`
- [[PY013-条件与循环]] — `for` 循环的底层机制
- [[PY003-内置函数]] — `iter()`/`next()`/`zip()`/`enumerate()`

## 📥 被哪些笔记引用

```dataview
LIST
FROM [[]]
SORT file.name ASC
```
