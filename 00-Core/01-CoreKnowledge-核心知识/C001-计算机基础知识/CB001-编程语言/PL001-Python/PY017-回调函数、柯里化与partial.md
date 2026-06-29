---
type: learning
status: 已完成
domain: Python
tags: [Python, 编程语言]
created: 2026-06-29
updated: 2026-06-29
---

# PY017-回调函数、柯里化与partial

## 🎯 学习目标

1. 回调函数是什么？同步回调和异步回调有何区别？
2. 柯里化如何实现参数复用和延迟执行？
3. `functools.partial` 的底层原理是什么？与 `lambda` 有何区别？
4. 回调、柯里化、partial 三者分别解决什么问题？在什么场景下选择哪个？

## 📖 前置知识

- [[PY015-高阶函数]] — 需理解函数作为参数传递（高阶函数基础部分）

## 📚 核心内容

### 回调函数

#### 1. 什么是回调函数？

简单来说，回调函数就是一个被作为参数传递给另一个函数的函数，并且这个函数会在某个特定的时刻被"回调"（即执行）。

想象一下你去餐厅吃饭。你点完菜后（发起请求），不需要站在厨房门口等着（阻塞），而是回到座位玩手机。当菜做好了（任务完成），服务员会叫你的号或者把菜端上来（回调）。在这里，"把菜端上来"这个动作，就是回调。

#### 2. 核心特点

- **延迟执行**：回调函数通常不会立即执行，而是等待特定条件满足（如任务完成、事件触发）。
- **解耦**：主函数不需要知道回调函数的具体实现细节，只需要知道何时调用它。这大大降低了代码的耦合度。
- **灵活性**：通过传递不同的回调函数，我们可以让同一个主函数表现出完全不同的行为。

#### 3. 实战场景

**3.1 同步回调**：最常见的如数据处理。

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

**3.2 异步回调**：在处理耗时任务（如网络请求、文件读写）时，为了不阻塞主线程，我们通常使用回调。

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

当你调用这个新对象时，它会把新传入的参数与内部保存的 `args` 和 `keywords` 合并，然后一起传给原始的 `func`去执行。

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

#### 3.  四大核心实战场景

**3.1 简化高频重复调用（代码更语义化）**
当某个函数需要反复调用且大部分参数相同时，用 `partial` 可以生成语义更明确的专用工具函数。

```python
from functools import partial
# 比如将任意进制字符串转为十进制，经常需要固定 base 参数
int_from_hex = partial(int, base=16)
print(int_from_hex('1A'))  # 输出 26，比 int('1A', base=16) 更直观
```

**3.2 完美适配回调与事件处理（携带上下文）**
在 GUI 编程（如 Tkinter, PyQt）或异步回调中，框架往往只允许传递固定签名的函数。`partial` 可以在不改变函数签名的情况下，把额外的上下文数据（如用户ID、配置信息）"夹带"进去。

```python
import tkinter as tk
from functools import partial

def on_click(btn_id):
    print(f"按钮 {btn_id} 被点击了")

root = tk.Tk()
# 这里的 command 期望一个无参函数，partial 完美适配
btn1 = tk.Button(root, text="按钮1", command=partial(on_click, 1))
btn2 = tk.Button(root, text="按钮2", command=partial(on_click, 2))
```

**3.3 配合高阶函数（map, sorted, reduce 等）**
当高阶函数要求传入的函数只能接收一个参数，而你的业务逻辑函数需要多个参数时，`partial` 是最佳解决方案。

```python
from functools import partial
data = [1, 2, 3, 4]
# map 要求传入的函数只能接收一个参数
double = partial(map, lambda x: x * 2)
print(list(double(data)))  # 输出 [2, 4, 6, 8]
```

**3.4 作为装饰器工厂或依赖注入**
在构建复杂系统时，可以用 `partial` 提前把数据库连接、日志对象、环境配置等"依赖"注入到业务函数中，生成纯净的业务回调函数。

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
