---
type: learning
status: 已完成
domain: Python
tags: [Python, 编程语言]
created: 2026-06-29
updated: 2026-06-29
---
# PY017-回调函数、柯里化与 partial

## 🎯 学习目标

1. 回调函数是什么？同步回调和异步回调有何区别？
2. 柯里化如何实现参数复用和延迟执行？
3. `functools.partial` 的底层原理是什么？与 `lambda` 有何区别？
4. 回调、柯里化、partial 三者分别解决什么问题？在什么场景下选择哪个？

## 📖 前置知识

- [[PY015-高阶函数]] — 需理解函数作为参数传递（高阶函数基础部分）

## 📚 核心内容

### 回调函数

#### 1. 为什么叫"回调函数"？

很多初学者觉得"回调"这个名字难以理解——它本质上不就是把一段代码打包，传给另一个函数去执行吗？为什么叫"回调"？

**名字的来源："回调" = "回过头来调用"**

关键在于**控制权的反转**：

- **普通函数调用**：你主动调用函数 → 你掌控时机 → 你主动拿结果
- **回调函数**：你把函数交给别人 → 别人在某个时机 → **回过头来调用你的函数**

打个比方，你打电话给客服：

- **普通调用**：你打过去，对方立刻接，你问什么对方答什么
- **回调（callback）**：你打过去，对方说"现在忙，你留个号码，我**回头打给你**"——你留的那个号码，就是回调函数。你不是当场得到结果，而是把"联系方式"（函数）给了对方，对方在合适的时机**回**过来**调**用你。

这就是"回调"二字的由来——不是你调它，是它**回过头来调你**给的那个函数。

#### 2. 什么是回调函数？

简单来说，回调函数就是一个被作为参数传递给另一个函数的函数，并且这个函数会在某个特定的时刻被"回调"（即执行）。

想象一下你去餐厅吃饭。你点完菜后（发起请求），不需要站在厨房门口等着（阻塞），而是回到座位玩手机。当菜做好了（任务完成），服务员会叫你的号或者把菜端上来（回调）。在这里，"把菜端上来"这个动作，就是回调。

用伪代码来呈现这个场景：

```python
import time

def 点菜(菜品, 上菜时的动作):      # 上菜时的动作 = 回调函数
    print(f"收到订单：{菜品}")
    print("厨房开始做菜...")
    time.sleep(2)                  # 模拟做菜耗时
    做好的菜 = f"一盘{菜品}"
    上菜时的动作(做好的菜)          # ← 菜做好了，回过头来调用你给的回调

def 端上来(菜):
    print(f"服务员把{菜}端到桌上，请慢用！")

def 叫号取餐(菜):
    print(f"叮咚——{菜}好了，请到取餐台自取！")

# 你点菜时，把"完成后做什么"作为回调塞给餐厅
点菜("红烧肉", 端上来)     # 服务员端上来（回调=端上来）
点菜("麻辣烫", 叫号取餐)   # 通知你去取（回调=叫号取餐）

print("你回到座位玩手机...")  # 主线程不阻塞，继续干自己的事
```

对照餐厅比喻，代码中的每一行对应什么角色：

| 代码 | 餐厅场景中的含义 |
|------|-----------------|
| `点菜()` | 你向餐厅发起请求 |
| `"红烧肉"` | 你要点的菜（业务数据） |
| `端上来` / `叫号取餐` | **回调函数**——你留给餐厅的"联系方式"，告诉你菜好了之后**做什么** |
| `上菜时的动作(做好的菜)` | 厨房**回过头来调用**你给的回调（控制权反转） |
| `print("你回到座位玩手机...")` | 主线程不等结果，继续执行其他任务 |

**同一个 `点菜()` 函数，传入不同的回调（`端上来` vs `叫号取餐`），就表现出完全不同的行为——这就是回调的核心价值。**

#### 3. 核心特点

- **控制权反转**：不是你掌控调用时机，而是你把函数交出去，由对方决定何时调用。
- **延迟执行**：回调函数通常不会立即执行，而是等待特定条件满足（如任务完成、事件触发）。
- **解耦**：主函数不需要知道回调函数的具体实现细节，只需要知道何时调用它。这大大降低了代码的耦合度。
- **灵活性**：通过传递不同的回调函数，我们可以让同一个主函数表现出完全不同的行为。

#### 4. 实战场景

**4.1 同步回调**：最常见的如数据处理。

```python
def calculate(a, b, callback):
    # 主逻辑：计算
    result = callback(a, b)
    print(f"最终结果: {result}")

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# 传递加法逻辑
calculate(10, 20, add)      # 输出: 最终结果: 30
# 传递乘法逻辑
calculate(10, 20, multiply) # 输出: 最终结果: 200
```

**4.2 异步回调**：在处理耗时任务（如网络请求、文件读写）时，为了不阻塞主线程，我们通常使用回调。

```python
import time
import threading

def download_file(url, callback):
    def task():
        print(f"正在下载 {url}...")
        time.sleep(2) # 模拟耗时
        callback("下载成功！")
    # 开启新线程模拟异步
    threading.Thread(target=task).start()

def on_complete(msg):
    print(f"收到通知: {msg}")

download_file("http://example.com", on_complete)
print("主线程继续执行其他任务...")
```

---

### 柯里化：化繁为简的魔法

#### 1. 什么是柯里化？

柯里化（Currying）这个名字来源于数学家 Haskell Curry。它的核心思想非常优雅：**将一个接受多个参数的函数，转换成一系列只接受一个参数的函数。**

用数学公式表达就是：
`f(x, y, z)` 变为 `f(x)(y)(z)`

#### 2. 为什么要用柯里化？

柯里化不仅仅是为了炫技，它解决了实际开发中的两个痛点：**参数复用**和**延迟执行**。

**手动实现柯里化**

让我们看一个最基础的加法函数是如何被柯里化的：

```python
# 普通函数
def add(x, y, z):
    return x + y + z

# 柯里化版本
def curried_add(x):
    def inner_y(y):
        def inner_z(z):
            return x + y + z
        return inner_z
    return inner_y

# 调用方式
result = curried_add(1)(2)(3) 
print(result) # 输出: 6
```

#### 3. 柯里化参数复用

假设我们有一个计算商品总价的函数，税率是固定的，但价格和数量是变化的。

```python
def calculate_price(tax_rate, price, quantity):
    return (price * quantity) * (1 + tax_rate)

# 使用柯里化
def curried_price(tax_rate):
    def with_price(price):
        def with_quantity(quantity):
            return (price * quantity) * (1 + tax_rate)
        return with_quantity
    return with_price

# 场景：我们要处理很多美国订单（税率0.08）
us_order = curried_price(0.08)

# 现在我们得到了一个专门处理美国订单的函数，不需要再传税率了
order_1 = us_order(100) # 价格100
total = order_1(2)      # 数量2
print(total) # 输出: 216.0
```

通过柯里化，我们"冻结"了税率参数，生成了一个更专用的函数，代码复用性大大增强。

---

### Python 中的 `partial`

#### 1. 核心定义与底层原理

`partial` 来自 Python 的标准库 `functools`。它的核心作用是 **"参数预填充"**，即把一个函数的部分参数（位置参数或关键字参数）提前"冻结"住，返回一个新的、参数更少的可调用对象。

**底层原理：**
当你调用 `partial` 时，它返回的是一个 `partial` 类的实例对象。这个对象内部保存了三个只读属性：

- `func`：保存原始的函数对象。
- `args`：保存你提前绑定的位置参数。
- `keywords`：保存你提前绑定的关键字参数。

当你调用这个新对象时，它会把新传入的参数与内部保存的 `args` 和 `keywords` 合并，然后一起传给原始的 `func` 去执行。

#### 2. 基础语法与参数绑定规则

基本语法结构为：`new_func = partial(原函数, *固定位置参数, **固定关键字参数)`。

在绑定参数时，有几个非常关键的规则需要注意：

1. **位置参数按顺序冻结**：传入的位置参数会从原函数的第一个参数开始依次绑定。
2. **调用时的参数合并**：调用新函数时传入的参数，会拼接在已冻结的位置参数后面。
3. **关键字参数的覆盖机制**：在创建 `partial` 时绑定的关键字参数，可以在后续调用新函数时**被重新指定（覆盖）**；但已绑定的位置参数不能被覆盖。

**代码演示参数规则：**

```python
from functools import partial

def info(name, age, city="北京"):
    print(f"姓名: {name}, 年龄: {age}, 城市: {city}")

# 1. 冻结位置参数 name="张三"
user_info = partial(info, "张三")
user_info(25)  # 输出: 姓名: 张三, 年龄: 25, 城市: 北京

# 2. 冻结关键字参数，且后续调用可以覆盖
beijing_user = partial(info, city="上海")
beijing_user("李四", 30)          # 输出: 姓名: 李四, 年龄: 30, 城市: 上海
beijing_user("王五", 28, city="广州") # 城市被成功覆盖为广州！
```

#### 3. 四大核心实战场景

**3.1 同一个函数被反复调用，大部分参数都一样**

这是 `partial` 最日常的用法。你有一个函数，每次调用它时某几个参数总是一样的——每次手写既繁琐又容易出错。用 `partial` 把不变的参数"冻住"，生成一个更简短的新函数。

```python
from functools import partial

# 场景：你的应用里到处需要把十六进制字符串转成整数
# 每次都要写 base=16，又长又容易忘
print(int('1A', base=16))   # 26
print(int('FF', base=16))   # 255
print(int('A3', base=16))   # 163

# 用 partial 把 base=16 冻住，新函数只需要传一个参数
hex_to_int = partial(int, base=16)

print(hex_to_int('1A'))     # 26  —— 一眼就知道这是在"十六进制转整数"
print(hex_to_int('FF'))     # 255
print(hex_to_int('A3'))     # 163
```

再比如日志输出，每次都要写同样的 `level`：

```python
import logging

# 项目中到处是 logging.log(level, msg)，level 写错一次就分类错误
logging.log(logging.WARNING, "磁盘空间不足")
logging.log(logging.WARNING, "连接超时")

# 冻住 level，变成一个"专门打 warning 日志"的函数
warn = partial(logging.log, logging.WARNING)
warn("磁盘空间不足")   # 简洁，且绝对不会写错级别
warn("连接超时")
```

> **一句话**：一个参数你发现自己写了三遍以上，就可以考虑用 `partial` 把它冻住。

---

**3.2 框架要求"无参函数"，但你的逻辑需要知道"是谁触发的"**

很多框架（GUI、Web、异步任务）的回调接口规定死了函数签名——比如按钮的 `command` 必须是 `f()`，不能是 `f(btn_id)`。但你的业务代码需要区分"是哪个按钮被点了"。

`partial` 可以提前把额外信息"塞进"参数里，返回一个表面上是无参、实际上参数已经藏在里面的函数。

```python
from functools import partial

# 你的业务函数：需要知道是哪个按钮
def on_click(button_name):
    print(f"用户点击了 [{button_name}]")

# 框架要求 command 是无参函数，partial 帮你把参数"提前塞进去"
btn_save = partial(on_click, "保存按钮")
btn_delete = partial(on_click, "删除按钮")
btn_logout = partial(on_click, "退出登录按钮")

# 这些 btn_* 表面上是无参可调用对象，框架可以直接用
btn_save()     # 输出: 用户点击了 [保存按钮]
btn_delete()   # 输出: 用户点击了 [删除按钮]
btn_logout()   # 输出: 用户点击了 [退出登录按钮]
```

同样的模式适用于 Tkinter、PyQt、asyncio 回调等任何"框架规定死回调签名"的场景。

> **一句话**：当你需要把"多参函数"塞进"只接受无参回调"的接口里时，用 `partial` 把参数提前填好。

---

**3.3 配合 map/filter/sorted 等高阶函数**

`map(fn, data)` 要求 `fn` 只能接收一个参数。如果你的业务函数需要多个参数，直接传给 `map` 会报错——这时用 `partial` 把多余的参数冻住。

```python
from functools import partial

# 你的业务函数：需要两个参数（基数 + 数字）
def scale(num, factor):
    return num * factor

nums = [1, 2, 3, 4, 5]

# ❌ 直接传 scale 给 map 不行——map 只会给一个参数，factor 没传，报错
# list(map(scale, nums))  # TypeError

# ✅ 用 partial 把 factor 冻住，scale 就变成了"只收一个参数"的函数
double = partial(scale, factor=2)
triple = partial(scale, factor=3)

print(list(map(double, nums)))  # [2, 4, 6, 8, 10]
print(list(map(triple, nums)))  # [3, 6, 9, 12, 15]
```

`filter` 和 `sorted` 同理。再看一个结合 `sorted` 的例子：

```python
# sorted 的 key 参数要求 f(item) → 排序依据值
# 但你的比较逻辑需要外部配置（比如用户偏好）

def by_field(item, field):
    return item.get(field, 0)

records = [{"name": "张三", "score": 88}, {"name": "李四", "score": 95}]

# 冻住 field="score"，变成 sorted 可以直接用的 key 函数
sort_by_score = partial(by_field, field="score")
print(sorted(records, key=sort_by_score, reverse=True))
# [{'name': '李四', 'score': 95}, {'name': '张三', 'score': 88}]
```

> **一句话**：高阶函数限制了你传的函数长什么样，`partial` 帮你把"不合规"的函数改造成"合规"的。

---

**3.4 把"环境依赖"提前注入，让业务函数更纯净**

在真实项目中，很多函数依赖外部资源运行——数据库连接、日志对象、API 密钥、配置文件。每次调用都传这些"环境参数"会让业务逻辑淹没在样板代码里。

`partial` 可以把这些依赖提前"注入"，让最终的调用代码只关心业务本身。

```python
from functools import partial

# 模拟：一个需要数据库连接才能运行的查询函数
def query(db_connection, sql):
    print(f"在 [{db_connection}] 上执行: {sql}")
    return f"结果_of_{sql}"

# 你的数据库连接（项目启动时就确定的）
main_db = "主数据库-192.168.1.100"
backup_db = "备份数据库-192.168.1.101"

# 把连接"注入"进去，生成两个纯净的查询工具
query_main = partial(query, main_db)
query_backup = partial(query, backup_db)

# 业务代码里只用关心 SQL 本身，不用每次传数据库连接
query_main("SELECT * FROM users")
query_backup("SELECT * FROM users")
# 输出:
# 在 [主数据库-192.168.1.100] 上执行: SELECT * FROM users
# 在 [备份数据库-192.168.1.101] 上执行: SELECT * FROM users
```

这就是"依赖注入"的朴素版本——不需要框架，不需要装饰器，`partial` 就能做到。

> **一句话**：把"环境相关、万年不变"的参数提前用 `partial` 冻住，让你的业务调用代码只关心业务本身。

#### 4. 偏函数 (partial) vs Lambda 表达式

虽然很多时候 `partial` 能做的事，`lambda` 也能做，但在工程实践中更推荐使用 `partial`，对比如下：

| 维度           | functools.partial                    | lambda 表达式                        |
| -------------- | ------------------------------------ | ------------------------------------ |
| **语义清晰度** | 极高，明确表达"预设参数"的意图       | 较低，意图模糊，需要阅读具体代码     |
| **可读性**     | 结构清晰，尤其在参数较多时           | 参数多了容易变成又长又乱的"面条代码" |
| **调试体验**   | 友好，对象会保留原函数信息           | 较差，报错时通常只显示 `<lambda>`    |
| **序列化**     | 支持 `pickle` 序列化（可用于多进程） | **不支持**序列化                     |

#### 5. 最佳实践与避坑指南

+ **注意性能边界**：`partial` 在调用时会有微小的额外开销（因为它需要合并参数）。在极度追求性能的纳秒级核心计算循环中，直接调用原函数可能会稍快一些。

+ **合理命名**：使用 `partial` 后，一定要给生成的新函数起一个有意义的名字（如 `bin2int` 而不是简单的 `p_func`），否则会降低代码的可读性。

+ **小心位置参数的顺序**：`partial` 固定位置参数时是严格按照从左到右的顺序。如果你想跳着固定后面的位置参数，必须使用关键字参数的形式来绑定。

## 🧪 练习 / 验证

### 练习 1：partial 应用

使用 `functools.partial` 将内置的 `sorted` 函数创建一个按字符串长度排序的新函数 `sort_by_length`，然后对列表 `["apple", "kiwi", "banana", "pear"]` 排序。

**答案：**

```python
from functools import partial

sort_by_length = partial(sorted, key=len)
words = ["apple", "kiwi", "banana", "pear"]
print(sort_by_length(words))
# 输出: ['kiwi', 'pear', 'apple', 'banana']
```

## 🔗 相关资源

- [[PY015-高阶函数]] — 前置知识：高阶函数与闭包
- [[PY016-装饰器]] — 并列笔记：基于闭包的函数增强技术
- 官方文档：[functools — Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html)