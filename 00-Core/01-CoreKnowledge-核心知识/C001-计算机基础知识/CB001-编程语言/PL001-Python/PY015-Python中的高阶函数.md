---
type: learning
status: 已完成
domain: Python
tags: [Python, 编程语言]
created: 2026-06-12
updated: 2026-06-16
---

# Python 中的高阶函数

## 🎯 学习目标

1. 什么是高阶函数？Python 中函数为什么被称为第一类公民？
2. 如何将函数作为参数传递给另一个函数？有哪几种传递参数的方式？
3. 什么是闭包？闭包形成的三个硬性条件是什么？
4. 装饰器的本质是什么？多个装饰器的叠加执行顺序是怎样的？
5. 带参数的装饰器是如何通过三层闭包实现的？
6. 什么是柯里化？`functools.partial` 与 `lambda` 有何区别？
7. `map`、`filter`、`reduce` 三个内置高阶函数各自的作用是什么？
8. `yield` 关键字如何工作？它与 `return` 的本质区别是什么？

## 📖 前置知识

- [[PY014-Python中的函数]] — 掌握 Python 函数定义、参数传递、作用域等基础知识

## 📚 核心内容

### 高阶函数

在 Python 中，函数被视为**第一类公民（First-class Object）**。这意味着函数可以像整数、字符串或列表一样，被赋值给变量、作为参数传递，或者作为返回值。

**场景一：接收函数作为参数（将逻辑抽象化）**
你可以将一个函数传递给另一个函数，让接收方决定如何处理这个函数。这常用于将"做什么"和"怎么做"分离。

```python
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    # 接收函数 f 作为参数，体现了高阶用法
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result) # 15
```

**场景二：将函数作为返回值（动态生成逻辑）**
一个函数可以根据传入的参数，动态返回不同的函数。

```python
def square(x): return x ** 2
def cube(x): return x ** 3

def get_operation(type):
    if type == 'square':
        return square  # 返回函数对象
    elif type == 'cube':
        return cube

operation = get_operation('square')
print(operation(3)) # 输出 9
```

#### 函数带参传递与不带参传递

当你把函数作为参数传递时，你传递的确实是**函数对象本身**（通常通过函数名），但这并不意味着你不能传递"参数"。

实际上，我们有三种主要的方法，既能把"函数"传进去，又能把"参数"带进去。

**1. 基础理解：为什么只传函数名？**

首先，我们要区分**"函数本身"**和**"函数的执行结果"**。

- `my_func`（不带括号）：代表**函数这个对象**（就像一把枪）。
- `my_func()`（带括号）：代表**执行函数**并拿到结果（就像开枪后的子弹）。

当你把函数作为参数传给另一个函数（比如装饰器或回调）时，你的目的是让接收方**在合适的时机去调用这把"枪"**。如果你传的是 `my_func()`，那就等于你在传递之前就先把枪开了，接收方拿到的只是子弹（返回值），而不是枪。

所以，**传递函数名是为了保留"执行权"**。

**2. 如果想传参数怎么办？**

虽然在形式参数表里写的是"函数名"，但在实际调用时，完全可以把参数一起"打包"带进去。

**方法一：接收方负责传参（最常用）**

这是最标准的做法。你把函数传进去，同时把参数也传进去，由接收方（高阶函数）来负责组装。

```python
def my_add(x, y):
    return x + y

# 接收方定义了 func, a, b 三个参数
def calculator(func, a, b):
    # 接收方在这里把参数传给函数
    return func(a, b) 

# 调用时：把函数名、参数1、参数2 分开传
result = calculator(my_add, 10, 20) 
print(result) # 输出 30
```

**方法二：使用 Lambda 表达式（打包传递）**

如果你不想修改接收方函数的定义（比如接收方只能接收一个参数），你可以用 `lambda` 把"函数+参数"打包成一个**新的匿名函数**。

```python
def my_add(x, y):
    return x + y

# 假设这个函数只能接收一个参数（函数）
def run_task(task_func):
    print("开始执行任务...")
    result = task_func() # 接收方不需要知道参数，只管运行
    print(f"结果是: {result}")

# 重点看这里：
# 我们传的不是 my_add，而是一个"包裹"
# 这个包裹里包含了 my_add 和参数 10, 20
run_task(lambda: my_add(10, 20)) 
```

**原理**：`lambda: my_add(10, 20)` 创建了一个没有参数的小函数，当你调用它时，它内部会去调用 `my_add(10, 20)`。

**方法三：使用 `functools.partial`（偏函数）**

这是 Python 提供的专门工具，用来"冻结"函数的某些参数。

```python
from functools import partial

def my_add(x, y):
    return x + y

# 创建一个新函数，把 x 固定为 100
add_100 = partial(my_add, 100)

def run_task(task_func):
    # 只需要传 y 的值
    print(task_func(5)) 

run_task(add_100) # 相当于执行 my_add(100, 5)
```

---

### Python 闭包

#### 1. 什么是闭包

通常函数执行完后，内部的局部变量就会被销毁。但闭包打破了这个规则。如果一个内部函数引用了外部函数的变量，并且这个内部函数被返回到了外部，那么这个内部函数就会"死死抓住"那些变量，不让它们被销毁。

闭包是指嵌套函数中，**内部函数引用了外部函数的变量**，即使外部函数已经执行完毕，这些变量依然被保留在内存中。

#### 2. 闭包形成的三个硬性条件：

1. **嵌套函数**：必须在一个函数内部定义另一个函数。
2. **引用外部变量**：内部函数必须引用外部函数的局部变量（这个变量被称为**自由变量**）。
3. **返回内部函数**：外部函数必须返回这个内部函数。

**代码示例：**

示例一：

```python
def add_ten():
    ten = 10
    def add(num):
        return num + ten # 内部函数使用了外部函数的变量 ten
    return add

closure_result = add_ten()
print(closure_result(5)) # 15
```

示例二：

```python
def outer_func(name):
    # name 是外部函数的局部变量
    def inner_func():
        # 内部函数引用了外部的 name
        print(f"Hello, {name}!")
    # 返回内部函数
    return inner_func

# 创建闭包
greeter = outer_func("Alice")
# 此时 outer_func 已经执行结束了，但 "Alice" 依然被 greeter 记在心里
greeter()  # 输出: Hello, Alice!
```

#### 3. 闭包的作用

闭包打破了作用域的限制，使得变量可以被"私有化"保存。它是实现装饰器、回调函数以及函数式编程中柯里化的基础。

其实"装饰器为什么能记住函数"、"回调怎么携带上下文"，本质上都是闭包在起作用。

我们可以把闭包理解为：**一个"有记忆"的函数，它不仅携带代码，还携带了它被创造时的环境。**

#### 4. 闭包核心原理：`__closure__` 与 `nonlocal`

**4.1 它是如何"记忆"的？（`__closure__`）**

Python 使用一种叫 **Cell（单元格）** 的对象来保存这些变量。你可以通过 `__closure__` 属性来查看闭包到底记住了什么。

```python
def make_adder(x):
    def adder(y):
        return x + y
    return adder

fn = make_adder(10)
print(fn.__closure__) 
# 输出类似: (<cell at 0x...: int object at 0x...>,)
# 这说明 fn 确实持有一个指向 x=10 的引用
```

**4.2 如何修改记忆？（`nonlocal`）**

默认情况下，闭包只能**读取**外部变量。如果你想**修改**它（比如做一个计数器），必须使用 `nonlocal` 关键字声明。

```python
def counter():
    count = 0
    def increment():
        nonlocal count  # 声明：我要修改外层的 count，而不是创建新的局部变量
        count += 1
        return count
    return increment

c = counter()
print(c()) # 1
print(c()) # 2 (记忆被修改了)
```

#### 5. 闭包的三大实战场景

**5.1 数据封装（模拟私有变量）**

在 Python 没有严格的私有属性（像 Java 的 `private`）之前，闭包是实现数据隐藏的最佳方式。

```python
def create_wallet(initial_balance):
    balance = initial_balance # 这是一个"私有"变量，外部无法直接访问
    
    def get_balance():
        return balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
        
    return get_balance, deposit

get_bal, dep = create_wallet(100)
# 外部无法直接修改 balance，只能通过 dep 函数修改
dep(50) 
print(get_bal()) # 150
```

**5.2 函数工厂（定制化函数）**

根据传入参数的不同，批量生成不同功能的函数。

```python
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2) # 生成一个专门乘2的函数
triple = make_multiplier(3) # 生成一个专门乘3的函数

print(double(5)) # 10
print(triple(5)) # 15
```

**5.3 装饰器的基石**

装饰器本质上就是一个接收函数作为参数，并返回一个闭包的高阶函数。下面会详细讲述装饰器的相关内容。

#### 6. 经典的"晚绑定"陷阱

**问题代码**：

```python
def create_multipliers():
    return [lambda x: x * i for i in range(5)]

# 预期：0, 4, 8, 12, 16
# 实际：[16, 16, 16, 16, 16] (假设 x=4)
for multiplier in create_multipliers():
    print(multiplier(4))
```

**原因**：
Python 的闭包是**"晚绑定"**的。也就是说，`lambda` 里的 `i` 并不是在循环时确定的，而是在**函数被调用时**去查找 `i` 的值，因为函数定义的时候 `i` 就已经完成了循环，已经变成了 4。当循环结束，`i` 变成了 4，所以所有的 `lambda` 都去乘 4。

**解决方案**：
利用**默认参数**在函数定义时求值的特性，把 `i` 的值"冻结"住。

```python
def create_multipliers_fixed():
    return [lambda x, i=i: x * i for i in range(5)]

# 现在输出正常了：0, 4, 8, 12, 16
```

### Python 装饰器

装饰器是一种设计模式，允许用户**在不修改原函数代码结构的情况下**，为其添加新功能。它本质上是一个接收函数作为参数并返回函数的高阶函数。

- **语法糖**：使用 `@decorator_name` 放在函数定义上方。

```python
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting()) # 输出: WELCOME TO PYTHON
```

#### 1. 多个装饰器的叠加

在实际开发中，我们经常需要给一个函数同时添加多个功能（例如：既需要记录日志，又需要验证权限）。这时可以使用**多个装饰器**。

**执行顺序规则：**
Python 解析装饰器时，遵循 **"由内向外"**（从下往上）的原则。

1. 离函数定义最近的装饰器（最下面的 `@`）最先执行。
2. 它的返回值会被传递给上一层装饰器。

```python
def decorator_a(func):
    print("装饰器 A 正在定义...")
    def wrapper(*args, **kwargs):
        print("执行装饰器 A 的逻辑")
        return func(*args, **kwargs)
    return wrapper

def decorator_b(func):
    print("装饰器 B 正在定义...")
    def wrapper(*args, **kwargs):
        print("执行装饰器 B 的逻辑")
        return func(*args, **kwargs)
    return wrapper

# 应用两个装饰器
@decorator_a
@decorator_b
def say_hello():
    print("Hello!")

# 输出顺序分析：
# 1. 定义阶段（代码加载时）：先打印 "装饰器 B..."，再打印 "装饰器 A..."
# 2. 调用阶段（say_hello() 执行时）：
say_hello()
```

**调用时的输出结果：**

```text
装饰器 B 正在定义...
装饰器 A 正在定义...
执行装饰器 A 的逻辑
执行装饰器 B 的逻辑
Hello!
```

**深度解析：代码执行流程**

我们可以把这段代码的执行分为两个阶段：

**阶段一：定义与装饰（代码加载时）**

这时候函数还没运行，Python 正在"装修"你的代码。

1. **定义 `decorator_b`**：打印 "装饰器 B 正在定义..."。
2. **定义 `decorator_a`**：打印 "装饰器 A 正在定义..."。
3. **遇到 `@decorator_a` 和 `@decorator_b`**：
   - 先执行 `@decorator_b`：把原始的 `say_hello` 传给 `decorator_b`，得到一个新的 `wrapper_b`。
   - 再执行 `@decorator_a`：把 `wrapper_b` 当作参数传给 `decorator_a`（此时 `func` = `wrapper_b`），得到最终的 `wrapper_a`。
   - **关键点**：此时 `decorator_a` 里的 `func` 实际上指向的是 `decorator_b` 包装后的函数。

**阶段二：调用执行（运行 `say_hello()` 时）**

这时候你调用了最终的 `wrapper_a`。

1. **进入 `wrapper_a`**：
   - 打印 "执行装饰器 A 的逻辑"。
   - 执行 `func(*args, **kwargs)`。注意，这里的 `func` 是通过闭包找到的，它指向 `wrapper_b`。
2. **进入 `wrapper_b`**（即上面的 `func`）：
   - 打印 "执行装饰器 B 的逻辑"。
   - 执行 `func(*args, **kwargs)`。这里的 `func` 指向最原始的 `say_hello`。
3. **进入原始 `say_hello`**：
   - 打印 "Hello!"。

**在学习过程中关于上述示例代码执行步骤提出了如下几个问题：**

**问题一：** 代码中 `func` 是作为参数传入，`func` 参数是怎么传递进装饰函数的？`say_hello` 函数并没有定义形参，但是在装饰器中的 `func` 函数是有 `*args` 、`**kwargs` 两个参数，为什么还能正常执行？

**1. `func` 参数去哪了？（闭包的力量）**

在 Python 中，**内部函数可以访问外部函数的变量**，即使外部函数已经执行完毕。这就是**闭包**。

+ **传递过程**：当你写 `@decorator_a` 时，Python 实际上执行了 `decorator_a(say_hello)`。

- **接收过程**：`decorator_a` 的定义是 `def decorator_a(func):`，所以 `say_hello` 这个函数对象就被赋值给了变量 `func`。

- **捕获过程**：在 `decorator_a` 内部定义的 `wrapper` 函数，直接使用了 `func`。Python 解释器非常聪明，它发现 `wrapper` 用到了外层作用域的 `func` 变量，于是把它"打包"进了 `wrapper` 的记忆里（即闭包）。

所以，`wrapper` 不需要在括号里声明 `func`，因为它已经通过"血缘关系"（作用域）拿到了 `func` 的引用。

**2. `*args` 和 `**kwargs` 的作用（万能接收器）**

你可能会问："那 `say_hello()` 调用时没有参数，为什么 `wrapper` 还要写 `*args, **kwargs`？"

这是为了**通用性**。

+ **接收调用参数**：当你调用 `say_hello()` 时，实际上是调用了 `wrapper()`。如果 `say_hello` 将来改了，变成了 `say_hello(name)`，`wrapper` 必须有能力接收这个 `name`。
+ **透传机制**：`wrapper` 使用 `*args` 和 `**kwargs` 来接收所有可能传进来的参数，然后原封不动地通过 `func(*args, **kwargs)` 传给原本的函数。

虽然在这个例子中 `say_hello` 没有参数，但加上 `*args, **kwargs` 是编写装饰器的**标准最佳实践**，这样无论被装饰的函数有什么参数，装饰器都能正常工作。

**问题二：** 装饰器和手动链式调用方式上有什么区别？是如何实现的？

**1. 装饰器语法 vs. 手动链式调用**

首先，我要告诉你一个 Python 的秘密：**装饰器语法本质上就是链式调用的语法糖**。

当你写下面的代码时：

```python
@decorator_a
@decorator_b
def say_hello():
    print("Hello!")
```

Python 解释器在后台**自动**帮你执行了下面的链式代码：

```python
def say_hello():
    print("Hello!")

# 第一步：先用 decorator_b 包装
temp_func = decorator_b(say_hello) 

# 第二步：再用 decorator_a 包装第一步的结果
say_hello = decorator_a(temp_func)
```

或者写得更紧凑一点（从下往上）：

```python
say_hello = decorator_a(decorator_b(say_hello))
```

**结论**：如果你手动写出 `say_hello = decorator_a(decorator_b(say_hello))`，它**绝对不会报错**，运行结果和用 `@`符号是一模一样的。

**2. 为什么你会觉得"会报错"？（常见误区）**

如果你尝试手动调用却报错了，通常是因为犯了以下两个错误之一：

**误区一：忘记把结果赋值回去**

装饰器的作用是**返回一个新的函数**。如果你只是调用装饰器，但不接收它的返回值，原来的函数就不会变。

- **错误写法**：

  ```python
  def say_hello(): print("Hello")
  
  decorator_b(say_hello) # 只是运行了装饰器，但没接收返回值！
  decorator_a(say_hello) # 还是在装饰原始函数
  
  say_hello() # 这里调用的还是那个没被装饰的原始函数
  ```

  *虽然这不会直接报错（TypeError），但你会发现装饰器里的打印语句根本没执行，或者逻辑没生效。*

- **正确写法**：

  ```python
  say_hello = decorator_b(say_hello) # 必须接住返回的那个 wrapper
  say_hello = decorator_a(say_hello)
  ```

**误区二：混淆了"装饰阶段"和"调用阶段"**

这可能是你觉得"报错"的真正原因。

请看这段代码：

```python
# 假设这是装饰器定义
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("执行逻辑")
        return func(*args, **kwargs)
    return wrapper
  
# 这里省略了 some_func 函数的定义

# 错误的手动调用尝试
result = my_decorator(some_func)(100) 
```

如果你这样写，Python 会先执行 `my_decorator(some_func)`，它返回 `wrapper` 函数。然后 Python 会立即尝试执行 `wrapper(100)`。

- 如果 `some_func` 本身不接受参数，而 `wrapper` 接收了 `100` 并试图传给 `some_func`，这时候就会报 `TypeError`。
- **装饰器语法**的好处在于，它把"包装"这个动作隔离开了。`@my_decorator` 只是把函数包装好放在那里，直到你显式调用 `say_hello()` 时才会触发参数传递的检查。

**3. 手动链式调用的正确姿势（实战演示）**

为了证明手动链式调用是完全可行的，我们来手动模拟一下之前的例子。

```python
def decorator_a(func):
    print("装饰器 A 正在定义...")
    def wrapper(*args, **kwargs):
        print("执行装饰器 A 的逻辑")
        return func(*args, **kwargs)
    return wrapper

def decorator_b(func):
    print("装饰器 B 正在定义...")
    def wrapper(*args, **kwargs):
        print("执行装饰器 B 的逻辑")
        return func(*args, **kwargs)
    return wrapper

# 1. 定义原始函数
def say_hello():
    print("Hello!")

# 2. 手动链式调用 (模拟 @ 语法)
# 注意顺序：从下往上，先 B 后 A
print("--- 开始手动装饰 ---")
step_1 = decorator_b(say_hello)      # 此时打印 "装饰器 B..."，step_1 是 wrapper_b
final_func = decorator_a(step_1)     # 此时打印 "装饰器 A..."，final_func 是 wrapper_a

print("--- 开始调用 ---")
final_func() 
# 输出顺序：
# --- 开始手动装饰 ---
# 装饰器 B 正在定义...
# 装饰器 A 正在定义...
# --- 开始调用 ---
# 执行装饰器 A 的逻辑
# 执行装饰器 B 的逻辑
# Hello!
```

**4. 什么时候必须用链式调用？**

虽然 `@` 语法很优雅，但在某些高级场景下，我们必须使用手动链式调用（或者叫组合装饰器）。

比如，我想写一个"超级装饰器"，它可以根据配置动态决定是否开启某些装饰器：

```python
def apply_logging(func, use_logging=True):
    if use_logging:
        # 这里就不能用 @ 语法了，必须手动链式调用
        func = decorator_a(func) 
    return func

# 动态应用装饰器
my_func = apply_logging(some_raw_function, use_logging=False)
```

**问题三：** 在定义装饰器函数 `decorate_a` 以及 `decorate_b` 的时候并不会执行外部函数的 `print` 函数，但是当定义通过装饰器修饰的 `say_hello` 函数的时候，发现会输出 `装饰器 B 正在定义...`，`装饰器 A 正在定义...`，为什么还没有调用 `say_hello` 函数，就已经执行了装饰器的定义？

这正是 Python 装饰器最核心、也是最容易让人困惑的机制。

当你在定义一个被装饰的函数时，**装饰器本身（外层函数）会立即执行**。接下来需要把装饰器的执行过程拆分为 **"装修阶段"**（定义时）和 **"居住阶段"**（调用时）。

**核心结论：**

当你写下 `@my_decorator` 并定义函数时：

1. **装饰器的外层逻辑（外层函数体）**：**立即执行**。
2. **装饰器的内层逻辑（wrapper 函数体）**：**暂不执行**（等到你调用被装饰函数时才执行）。

**代码实证：看输出顺序**

请看下面这段代码，注意 `print` 语句的位置和输出顺序：

```python
def my_decorator(func):
    # 【位置 A】这是装饰器的外层逻辑
    print(">>> 1. 装饰器正在构建（定义时立即执行）")
    
    def wrapper():
        # 【位置 B】这是装饰器的内层逻辑
        print("      2. 包装逻辑（调用时才执行）")
        func()
        
    return wrapper

print("--- 开始定义被装饰函数 ---")

@my_decorator
def say_hello():
    print("      3. 原函数逻辑")

print("--- 定义结束，准备调用 ---")

say_hello()
```

**实际输出结果：**

```text
--- 开始定义被装饰函数 ---
>>> 1. 装饰器正在构建（定义时立即执行）
--- 定义结束，准备调用 ---
      2. 包装逻辑（调用时才执行）
      3. 原函数逻辑
```

**为什么会这样？（底层原理）**

Python 解释器在处理 `@my_decorator` 语法糖时，实际上是在执行赋值操作。

当你写：

```python
@my_decorator
def say_hello():
    ...
```

Python 实际上执行了：

```python
def say_hello():
    ...

# 关键就在这里！
# 这行代码在定义阶段立即运行了 my_decorator 函数
say_hello = my_decorator(say_hello) 
```

因为 `my_decorator(say_hello)` 是一个**函数调用**，所以 `my_decorator` 函数体内部的代码（即【位置 A】）必须运行，才能返回结果。

**两个阶段的详细对比**

为了帮你理清思路，我们可以把装饰器看作一个**工厂**：

| 阶段                      | 动作         | 发生了什么？                                                 | 对应代码位置                       |
| ------------------------- | ------------ | ------------------------------------------------------------ | ---------------------------------- |
| **阶段一：装修** (定义时) | **工厂开工** | 装饰器函数被调用。它接收原函数，做一些**初始化设置**（比如注册插件、读取配置），然后打包返回一个 `wrapper`。 | **外层函数体** (立即执行)          |
| **阶段二：居住** (调用时) | **使用产品** | 你调用 `say_hello()`，实际是在调用工厂生产出来的 `wrapper`。这时才会执行**具体的业务增强逻辑**（比如计时、鉴权）。 | **内层 wrapper 函数体** (延迟执行) |

**避坑指南**

理解了这个机制，你在写装饰器时要注意：

1. **不要在装饰器外层写耗时操作**：
   如果你在【位置 A】（外层函数体）写了数据库连接或复杂的计算，那么**只要程序一启动（导入模块），这些代码就会运行**，哪怕你还没调用函数。这会导致程序启动变慢。
2. **利用这个特性做"一次性"工作**：
   如果你有些逻辑只需要运行一次（比如"向全局注册表注册这个函数"），那么把它放在装饰器的**外层函数体**（【位置 A】）是完美的，因为它只在定义时运行一次。

#### 2. 装饰器多层闭包处理流程

在 Python 中，当装饰器需要接收参数（例如 `@my_decorator(arg)`）或者需要保留被装饰函数的元数据并支持复杂逻辑时，通常会使用多层闭包。

 **2.1 核心概念**

当装饰器带有参数时，单层的 `decorator(func)` 无法直接接收额外参数，因此需要增加一层外层函数来捕获这些参数，形成 `wrapper_outer(arg) -> decorator(func) -> wrapper_inner(*args, **kwargs)` 的三层结构。

**2.2 三层闭包的职责划分**

| 层级      | 函数名(约定俗成)                     | 触发时机                     | 核心职责                              |
| :------ | :---------------------------- | :----------------------- | :-------------------------------- |
| **第一层** | `decorator_factory` / `outer` | **模块加载/解释器遇到 `@` 时立即执行** | 接收装饰器的配置参数，返回真正的装饰器函数。            |
| **第二层** | `decorator` / `middle`        | **紧跟第一层执行**              | 接收被装饰的目标函数 (`func`)，定义并返回实际的包装函数。 |
| **第三层** | `wrapper` / `inner`           | **每次调用被装饰函数时执行**         | 实际执行业务逻辑（如前置检查、后置处理），并调用原始目标函数。   |

**2.3 关键注意点**

- **执行顺序**：第一层和第二层在程序启动（或类定义）时就已执行完毕；只有第三层是在业务运行时才执行的。
- **元数据丢失问题**：多层嵌套后，原函数的 `__name__`、`__doc__` 会被最内层的 `wrapper` 覆盖。**必须**在最内层装饰器上使用 `@functools.wraps(func)`。
- **状态保持**：外层闭包捕获的参数在整个应用生命周期内保持不变，常被用来做配置开关、缓存字典等。

**2.4 代码示例：带参数的计时与重试装饰器**

这个例子展示了如何利用三层闭包实现一个可配置的"失败重试+耗时统计"装饰器。

```python
import time
import functools

# ================= 第一层闭包：接收装饰器自身的参数 =================
def retry_and_log(max_retries=3, log_prefix="[LOG]"):
    """
    装饰器工厂：负责捕获 max_retries 和 log_prefix
    触发时机：解释器解析到 @retry_and_log(...) 时立即执行
    """
    print(f"🔧 [第一层] 正在初始化装饰器配置: retries={max_retries}, prefix='{log_prefix}'")
    
    # ============= 第二层闭包：接收被装饰的目标函数 =============
    def decorator(func):
        """
        真正的装饰器：负责捕获 func，并返回包装后的函数
        触发时机：紧随第一层之后立即执行
        """
        print(f"🎯 [第二层] 正在装饰函数: {func.__name__}")
        
        # ========== 第三层闭包：实际执行时的包装逻辑 ==========
        @functools.wraps(func)  # 【关键】保留原函数的元数据
        def wrapper(*args, **kwargs):
            """
            包装函数：处理具体业务逻辑
            触发时机：每次手动或被其他代码调用 target_func() 时执行
            """
            attempt = 0
            start_time = time.time()
            
            while attempt < max_retries:
                try:
                    print(f"{log_prefix} 正在执行 {func.__name__} (第 {attempt + 1} 次尝试)")
                    result = func(*args, **kwargs)  # 调用原始函数
                    
                    elapsed = time.time() - start_time
                    print(f"{log_prefix} ✅ {func.__name__} 成功! 耗时: {elapsed:.4f}s")
                    return result
                    
                except Exception as e:
                    attempt += 1
                    print(f"{log_prefix} ❌ {func.__name__} 失败: {e}")
                    if attempt >= max_retries:
                        print(f"{log_prefix} ⛔ 达到最大重试次数 ({max_retries})，放弃执行。")
                        raise
                    time.sleep(0.5)  # 简单退避
                    
        return wrapper  # 第二层返回第三层
    return decorator  # 第一层返回第二层


# ================= 测试运行 =================
print("="*50)
print(">>> 阶段1: 模块加载，定义函数并应用装饰器")
print("="*50)

@retry_and_log(max_retries=2, log_prefix="[API]")
def fetch_data(url):
    """从指定URL获取数据"""
    print(f"   -> 模拟请求: {url}")
    if "fail" in url:
        raise ConnectionError("网络超时")
    return {"status": 200, "data": "Hello World"}

print(f"\n当前函数名: {fetch_data.__name__}")
print(f"当前函数文档: {fetch_data.__doc__}\n")

print("="*50)
print(">>> 阶段2: 实际业务调用")
print("="*50)

# 正常调用
fetch_data("https://api.example.com/data")

print("-"*50)

# 异常调用（触发重试机制）
try:
    fetch_data("https://api.fail.com/data")
except ConnectionError:
    print("[MAIN] 主线程捕获到最终抛出的异常\n")
```

**2.5 控制台输出结果分析**

运行上述代码，你可以清晰地看到三层闭包的执行时序：

```text
==================================================
>>> 阶段1: 模块加载，定义函数并应用装饰器
==================================================
🔧 [第一层] 正在初始化装饰器配置: retries=2, prefix='[API]'
🎯 [第二层] 正在装饰函数: fetch_data

当前函数名: fetch_data          <-- 证明 @wraps 生效，没有被变成 wrapper
当前函数文档: 从指定URL获取数据

==================================================
>>> 阶段2: 实际业务调用
==================================================
[API] 正在执行 fetch_data (第 1 次尝试)
   -> 模拟请求: https://api.example.com/data
[API] ✅ fetch_data 成功! 耗时: 0.0000s
--------------------------------------------------
[API] 正在执行 fetch_data (第 1 次尝试)
   -> 模拟请求: https://api.fail.com/data
[API] ❌ fetch_data 失败: 网络超时
[API] 正在执行 fetch_data (第 2 次尝试)
   -> 模拟请求: https://api.fail.com/data
[API] ❌ fetch_data 失败: 网络超时
[API] ⛔ 达到最大重试次数 (2)，放弃执行。
[MAIN] 主线程捕获到最终抛出的异常
```

**2.6 进阶提示**

如果你的多层闭包还需要修改**可变状态**（例如记录函数被调用的总次数），可以在第二层闭包中声明一个非局部变量：

```python
def decorator(func):
    call_count = 0  # 绑定在当前闭包的局部作用域
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count  # 【关键】声明修改外层闭包变量
        call_count += 1
        print(f"该函数已被调用 {call_count} 次")
        return func(*args, **kwargs)
    return wrapper
```

这种设计模式在编写 ORM 路由注册、权限校验中间件、以及 AOP（面向切面编程）时非常常见。
#### 3. 带参数的装饰器：

如果被装饰的函数需要参数，包装器也需要接收这些参数。

```python
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("装饰器：我住在 {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("我是 {} {}. 我喜欢教学.".format(first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh", "Finland")
```

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

1. **配合高阶函数（map, sorted, reduce 等）**
   当高阶函数要求传入的函数只能接收一个参数，而你的业务逻辑函数需要多个参数时，`partial` 是最佳解决方案。

```python
from functools import partial
data = [1, 2, 3, 4]
# map 要求传入的函数只能接收一个参数
double = partial(map, lambda x: x * 2)
print(list(double(data)))  # 输出 [2, 4, 6, 8]
```

1. **作为装饰器工厂或依赖注入**
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

---

### 内置高阶函数：Map, Filter, Reduce

Python 内置了三个非常强大的高阶函数，常配合 Lambda 表达式使用，用于处理列表等可迭代对象。

#### 1. Map 函数：映射

`map()` 接收一个函数和一个可迭代对象，将函数作用于可迭代对象的**每一个元素**，并返回处理后的结果。

```python
numbers = [1, 2, 3, 4, 5]
# 将每个数字平方
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25]
```

`map(function, m, n)` 函数还可以对多个可迭代对象进行处理，会依次迭代处理 `map(function, m1, n1)`， `map(function, m2, n2)`…… 处理结果长度取决于多个迭代对象中最短的一个个数。

`map` 函数只有获取结果集中的元素的时候才会发生函数处理。

#### 2. Filter 函数：过滤

`filter()` 接收一个返回布尔值的函数和一个可迭代对象，**筛选**出使函数返回 `True` 的元素。

```python
numbers = [1, 2, 3, 4, 5]
# 筛选出偶数
even_numbers = filter(lambda x : x % 2 == 0, numbers)
print(list(even_numbers)) # [2, 4]
```

#### 3. Reduce 函数：归约

`reduce()` 定义在 `functools` 模块中。它接收一个函数和一个可迭代对象，将函数累积地作用于元素，最终**返回一个单一的值**。

我们假设有一个数字列表 `[1, 2, 3, 4]`，我们的规则（也就是你传入的函数）是**"把它们加起来"**。

| 轮次  | 手里的累积值 (Accumulator) | 列表里的当前值 (Current) | 运算后的新累积值 |
| ----- | -------------------------- | ------------------------ | ---------------- |
| 初始  | 1 (列表第1个元素)          | 2 (列表第2个元素)        | 3 (1+2)          |
| 第1轮 | 3 (上一轮的结果)           | 3 (列表第3个元素)        | 6 (3+3)          |
| 第2轮 | 6 (上一轮的结果)           | 4 (列表第4个元素)        | 10 (6+4)         |

```python
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']
# 将所有字符串数字相加
total = reduce(lambda x, y: int(x) + int(y), numbers_str)
print(total) # 15
```

**注意：** `reduce` 函数中的自定义函数只能有两个参数。

#### 4. 深度解析：Map vs 列表推导式

虽然 `map` 很强大，但在 Python 中，**列表推导式**通常被认为更具 Python 风格且可读性更好。
例如：`[x**2 for x in numbers]` 通常比 `list(map(lambda x: x**2, numbers))` 更受欢迎。

### yield 关键字

在 Python 中，`yield` 是一个极其强大且优雅的关键字。它的核心作用是**将普通函数转变为生成器（Generator）**，从而实现"惰性求值"（Lazy Evaluation）和状态保持。

#### 1. 核心概念与工作原理

- **生成器函数**：只要函数体内包含 `yield` 关键字，它就不再是普通函数，而是一个生成器对象。调用该函数时，**不会立即执行函数体**，而是返回一个生成器迭代器。
- **暂停与恢复**：当执行到 `yield` 语句时，函数会**暂停执行**，并将 `yield` 后面的值返回给调用者。此时函数的所有局部变量、指令指针等状态都会被冻结并保存在内存中。下次通过 `next()` 或 `for` 循环触发时，函数会从上次暂停的地方**继续往下执行**。
- **返回值差异**：普通函数使用 `return` 结束并返回单一结果；而生成器可以多次 `yield`，产出一系列值的序列。

#### 2. yield vs return 的本质区别

| 特性       | `return`         | `yield`          |
| :------- | :--------------- | :--------------- |
| **函数类型** | 普通函数             | 生成器函数            |
| **执行行为** | 遇到即终止，销毁局部作用域    | 遇到即暂停，保留局部作用域    |
| **产出次数** | 只能返回一次           | 可产出多次（流式输出）      |
| **内存占用** | 一次性生成所有数据存入列表/元组 | 每次只生成一个元素，极度节省内存 |

#### 3. 三大核心应用场景

#### 场景一：处理海量数据（惰性计算）

当你需要处理几百万行日志或数据库记录时，使用 `yield` 可以避免 OOM（内存溢出）。

```python
def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()  # 每次只在内存中保留一行

# 内存占用极低，无论文件多大
for line in read_large_file("huge_log.txt"):
    if "ERROR" in line:
        print(line)
```

#### 场景二：无限序列生成器

因为状态被保存，生成器可以按需生成无限长的序列，而不会撑爆内存。

```python
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

counter = infinite_counter()
print(next(counter))  # 0
print(next(counter))  # 1
```

#### 场景三：双向通信 (`send()` 方法)

这是 `yield` 最容易被忽略的高级用法。**`yield` 不仅能把值传出去，还能接收外部传入的值。**

```python
def accumulator():
    total = 0
    while True:
        # 1. 把当前的 total 返回给外部
        # 2. 暂停等待外部 send() 传入新值
        # 3. 外部 send 的值会被赋值给 increment
        increment = yield total  
        if increment is None: break
        total += increment

acc = accumulator()
next(acc)                # 【必须】先启动生成器，推进到第一个 yield 处
print(acc.send(10))      # 输出: 10 (0 + 10)
print(acc.send(20))      # 输出: 30 (10 + 20)
```

#### 4. 进阶语法补充

- **`yield from` (Python 3.3+)**：用于委托生成器。它可以自动迭代另一个可迭代对象，并将产生的值直接透传给外层调用者，常用于树的遍历或异步编程中的协程嵌套。
    
    ```python
    def chain(*iterables):
        for it in iterables:
            yield from it  # 等价于 for item in it: yield item
    ```
    
- **异常处理**：可以使用 `generator.throw(Exception)` 从外部向生成器内部抛出异常，或者在生成器内部用 `try...except` 捕获由 `send()` 触发的异常。

#### 5. ⚠️ 常见避坑指南

1. **首次启动陷阱**：如果使用了 `send(value)`，必须先调用一次 `next(gen)` 或 `send(None)` 来激活生成器，否则直接 `send(非None值)` 会报 `TypeError`。
2. **不可重复消费**：生成器是一次性的迭代器。一旦遍历到底（抛出 `StopIteration`），就无法重置。如果需要再次使用，必须重新调用生成器函数创建新实例。
3. **不要缓存生成器**：如果你把生成器转成了 `list(gen)`，它就失去了省内存的意义，退化成了一次性加载的普通列表。

## 🧪 练习 / 验证

### 练习 1：高阶函数基础

编写一个高阶函数 `apply_twice(func, value)`，将函数 `func` 对 `value` 连续应用两次，并返回结果。

**答案：**

```python
def apply_twice(func, value):
    return func(func(value))

# 测试
def add_three(x):
    return x + 3

print(apply_twice(add_three, 10))  # 输出: 16  (10+3=13, 13+3=16)
```

---

### 练习 2：闭包与计数器

使用闭包实现一个 `create_counter(start)` 函数，每次调用返回递增 1 的值，起始值为 `start`。

**答案：**

```python
def create_counter(start):
    count = start
    def increment():
        nonlocal count
        current = count
        count += 1
        return current
    return increment

counter = create_counter(10)
print(counter())  # 输出: 10
print(counter())  # 输出: 11
print(counter())  # 输出: 12
```

---

### 练习 3：修复晚绑定陷阱

以下代码的输出是什么？请指出问题并修复，使每次调用 `funcs[0]()` 到 `funcs[4]()` 分别输出 `1, 4, 9, 16, 25`（即输出当前索引的平方）。

```python
funcs = [lambda: x**2 for x in range(1, 6)]
for f in funcs:
    print(f())
```

**答案：**

原代码由于晚绑定，`x` 在循环结束时为 5，所以所有 lambda 都输出 `25`。修复方案：

```python
funcs = [lambda x=x: x**2 for x in range(1, 6)]
for f in funcs:
    print(f())
# 输出:
# 1
# 4
# 9
# 16
# 25
```

---

### 练习 4：编写一个日志装饰器

编写一个 `@log_call` 装饰器，在每次调用被装饰函数时打印函数名和传入的参数，以及返回值。

**答案：**

```python
import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}, 参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 返回: {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(3, 7))
# 输出:
# 调用 add, 参数: (3, 7), {}
# add 返回: 10
# 10
```

---

### 练习 5：map + filter + reduce 综合

给定列表 `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`，使用 `map`、`filter`、`reduce` 计算所有偶数的平方和。

**答案：**

```python
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 方法一：组合使用
evens = filter(lambda x: x % 2 == 0, nums)
squares = map(lambda x: x ** 2, evens)
result = reduce(lambda x, y: x + y, squares)
print(result)  # 输出: 220

# 方法二：列表推导式（更 Pythonic）
result2 = sum(x**2 for x in nums if x % 2 == 0)
print(result2)  # 输出: 220
```

---

### 练习 6：partial 应用

使用 `functools.partial` 将内置的 `sorted` 函数创建一个按字符串长度排序的新函数 `sort_by_length`，然后对列表 `["apple", "kiwi", "banana", "pear"]` 排序。

**答案：**

```python
from functools import partial

sort_by_length = partial(sorted, key=len)
words = ["apple", "kiwi", "banana", "pear"]
print(sort_by_length(words))
# 输出: ['kiwi', 'pear', 'apple', 'banana']
```

---

### 练习 7：yield 生成器

编写一个生成器函数 `fibonacci(n)`，它生成前 `n` 个斐波那契数。

**答案：**

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))
# 输出: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### 练习 8：带参数的三层闭包装饰器

编写一个 `@repeat(n)` 装饰器，使被装饰函数重复执行 `n` 次，并返回最后一次执行的结果。

**答案：**

```python
import functools

def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
                print(f"第 {i+1} 次执行完成")
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return f"你好, {name}!"

print(greet("World"))
# 输出:
# Hello, World!
# 第 1 次执行完成
# Hello, World!
# 第 2 次执行完成
# Hello, World!
# 第 3 次执行完成
# 你好, World!
```

## 🤔 常见误区

### 误区 1：把函数调用结果当作函数对象传递

**错误认知**：高阶函数接收参数时，直接写 `my_func()` 就能把函数传进去。

**事实**：`my_func` 是函数对象本身，`my_func()` 是函数的**执行结果**。如果把 `my_func()` 传给高阶函数，接收方拿到的不是函数本身，而是函数的返回值，无法在合适的时机"回调"。

```python
# ❌ 错误：传递的是 my_add 的调用结果（TypeError: 'int' object is not callable）
def run_task(task_func):
    result = task_func()

# run_task(my_add(10, 20))  # 相当于 run_task(30)，而 30 不能被调用

# ✅ 正确：传递函数对象，用 lambda 包裹参数
run_task(lambda: my_add(10, 20))
```

---

### 误区 2：认为闭包会复制外部变量的值

**错误认知**：闭包创建时会把外部变量的值"快照"保存下来。

**事实**：闭包保存的是对外部变量的**引用**（晚绑定），只有在函数被调用时才去查找变量的值。这导致了经典的循环中 `lambda` 的"晚绑定"问题。

```python
funcs = [lambda: i for i in range(3)]
# 全部输出 2，因为调用时 i 已经是 2
print([f() for f in funcs])  # [2, 2, 2]

# ✅ 修复：用默认参数在定义时求值
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]
```

---

### 误区 3：忘记录接装饰器的返回值

**错误认知**：执行 `decorator_b(say_hello)` 就能装饰 `say_hello`。

**事实**：装饰器**返回一个新的函数**，必须把返回值重新赋值给原变量名，否则原来的函数不会有任何改变。

```python
# ❌ 错误：没有接返回值
decorator_b(say_hello)   # 返回的 wrapper 被丢弃
say_hello()              # 调用的还是原始函数

# ✅ 正确
say_hello = decorator_b(say_hello)  # 用 @decorator_b 语法糖自动做这一步
say_hello()                          # 现在调用的是包装后的函数
```

---

### 误区 4：认为生成器可以重复消费

**错误认知**：`next(gen)` 遍历到头后，可以再次从头开始遍历。

**事实**：生成器是**一次性迭代器**。一旦抛出 `StopIteration`，就无法重置。需要重新调用生成器函数创建新的生成器实例。

```python
gen = (x for x in range(3))
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] — 生成器已耗尽，不会重新产出

# ✅ 正确：重新创建
gen = (x for x in range(3))
print(list(gen))  # [0, 1, 2]
```

---

### 误区 5：`map`/`filter` 返回的是列表

**错误认知**：`map(func, iterable)` 和 `filter(func, iterable)` 直接返回列表。

**事实**：在 Python 3 中，`map()` 和 `filter()` 返回的是**迭代器对象**，只有在迭代时才会真正执行计算（惰性求值）。需要显式调用 `list()` 才能转为列表。

```python
result = map(lambda x: x*2, [1, 2, 3])
print(result)        # <map object at 0x...> — 不是列表！
print(list(result))  # [2, 4, 6]
```

## 🔗 相关资源

- 前置笔记：[[PY014-Python中的函数]]
- 后续笔记：[[PY016-Python中的文件]]
- 官方文档：[functools — Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html)
- 官方文档：[Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- 官方文档：[PEP 318 — Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
