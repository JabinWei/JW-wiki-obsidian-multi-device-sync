---
type: learning
status: 待办
domain: Python
tags: [Python, 编程语言, 数据库]
created: 2026-08-04
updated: 2026-08-04
---

---

![[90-Storage/98-Asset-资源/CoverImage/PY025-操作MySQL/Python操作MySQL数据库-coverImage-v1.png|banner]]

## 🎯 学习目标

- 在 Python 中连接 MySQL 数据库有哪些常用库？各自有什么特点？
- 如何使用 `pymysql` 建立连接、创建游标、执行 SQL 语句？
- `cursor.fetchone()`、`fetchall()` 和 `fetchmany()` 有什么区别？
- 什么是参数化查询？它如何防止 SQL 注入？
- 事务是什么，如何在 Python 中提交和回滚事务？
- 如何使用 `with` 上下文管理器自动管理连接和游标的生命周期？
- 连接池解决了什么问题，如何使用 `DBUtils` 或 `SQLAlchemy` 管理连接池？

## 📖 前置知识

- [[PY008-简单数据类型]] — 字符串操作、格式化
- [[PY014-函数]] — 函数定义、参数传递
- [[PY023-错误类型与异常处理机制]] — try/except 异常处理

## 📚 核心内容

Python 操作 MySQL 数据库的核心流程：**建立连接 → 创建游标 → 执行 SQL → 获取结果 → 提交/回滚 → 关闭连接**。下面以最常用的 `pymysql` 为主线展开。

> `pymysql` 是纯 Python 实现的 MySQL 客户端，API 完全兼容 Python 标准库 `sqlite3` 和流行的 `psycopg2`（PostgreSQL），学一个库就等于学会了 Python 数据库操作的标准范式。

---

### 安装与连接

```bash
pip install pymysql
```

**建立连接**：

```python
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='your_password',
    database='test_db',
    charset='utf8mb4',          # 支持 emoji 和中文
    cursorclass=pymysql.cursors.DictCursor  # 返回字典而非元组
)
```

> `charset` 写 `utf8mb4` 而非 `utf8`——MySQL 的 `utf8` 是阉割版（最多 3 字节），存不了 emoji 和部分生僻字。`utf8mb4` 才是真正的 UTF-8。

**连接参数一览**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `host` | 数据库服务器地址 | `localhost` |
| `port` | 端口号 | `3306` |
| `user` | 用户名 | — |
| `password` | 密码 | — |
| `database` | 数据库名 | — |
| `charset` | 字符集 | `utf8mb4` |
| `cursorclass` | 游标类型 | `Cursor`（返回元组） |
| `autocommit` | 是否自动提交 | `False` |
| `connect_timeout` | 连接超时（秒） | `10` |

**游标类型对比**：

| cursorclass                  | `fetchone()` 返回值 | 访问方式                        |
| ---------------------------- | ---------------- | --------------------------- |
| `pymysql.cursors.Cursor`（默认） | 元组               | `row[0]`, `row[1]`          |
| `pymysql.cursors.DictCursor` | 字典               | `row['name']`, `row['age']` |
| `pymysql.cursors.SSCursor`   | 元组（服务端游标）        | 大数据量流式读取                    |

> **优先用 `DictCursor`**——代码可读性远高于元组下标访问，字段顺序调整也不影响取值逻辑。

---

### 创建游标

连接建立后，通过 `conn.cursor()` 创建游标对象。游标是 Python 与 MySQL 之间交互的媒介——**SQL 语句通过游标发送，查询结果通过游标取回**。

```python
# 使用连接时指定的 cursorclass（默认 Cursor）
cursor = conn.cursor()

# 覆盖连接级别的 cursorclass，临时指定游标类型
dict_cursor = conn.cursor(pymysql.cursors.DictCursor)
ss_cursor = conn.cursor(pymysql.cursors.SSCursor)
```

`cursor()` 方法的关键参数：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `cursor` | `cursorclass` 类型，决定 fetch 返回格式 | `conn.cursorclass`（连接时指定的值） |

> **一个连接可以创建多个游标**——每个游标独立执行各自的 SQL，互不干扰。但同一连接上同一时刻只能有一个游标在做查询，多游标并发需使用多连接或连接池。游标用完后应调用 `cursor.close()` 释放，或直接用 `with conn.cursor() as cursor:` 自动管理。

---

### 执行 SQL 的三种方式

创建游标后，有三种执行 SQL 的方法：

```python
cursor = conn.cursor()

# 方式一：execute() — 执行单条语句
cursor.execute("SELECT * FROM users WHERE age > 18")

# 方式二：executemany() — 批量执行（批量插入场景效率远高于循环 execute）
data = [('Alice', 25), ('Bob', 30), ('Cathy', 28)]
cursor.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", data)

# 方式三：execute() 执行多条语句（需在连接时加 client_flag）
# 不推荐，建议逐条执行或使用 executemany
```

---

### 获取结果

`execute()` 之后，通过游标的 fetch 方法获取数据：

| 方法 | 返回值 | 适用场景 |
|------|--------|----------|
| `fetchone()` | 单行（字典或元组），无数据返回 `None` | 按主键查询、统计行数 |
| `fetchall()` | 所有剩余行的列表 | 结果集可控的小规模查询 |
| `fetchmany(n)` | 最多 n 行 | 分批处理、分页展示 |

```python
cursor.execute("SELECT name, age FROM users ORDER BY age")

# fetchone — 取第一行
row = cursor.fetchone()
print(row)  # {'name': 'Alice', 'age': 25}

# fetchmany — 取接下来 2 行
rows = cursor.fetchmany(2)
print(rows)  # [{'name': 'Bob', 'age': 28}, {'name': 'Cathy', 'age': 30}]

# fetchall — 取全部剩余行
all_rows = cursor.fetchall()
print(all_rows)  # [{'name': 'David', 'age': 35}]
```

> 游标内部维护一个读取指针，fetch 操作是**顺次消费**的——上一步取走的行，下一步不会再返回。用 `cursor.rownumber` 可查看当前指针位置。

---

### 参数化查询与 SQL 注入防护

**这是数据库操作中最重要的一课。** 永远不要用字符串拼接构造 SQL：

```python
# ❌ 危险！SQL 注入
name = "'; DROP TABLE users; --"
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
# 拼接结果：SELECT * FROM users WHERE name = ''; DROP TABLE users; --'
# 攻击者可以执行任意 SQL
```

**正确的做法**——使用参数化查询，让驱动帮你安全地填入参数：

```python
# ✅ 参数化查询 — 占位符 + 参数元组
name = "Alice"
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
```

`%s` 只是占位符（不是 Python 的 `%` 格式化），pymysql 会将它替换为转义后的值。不同类型的参数对应同一个 `%s` 占位符：

```python
# 多个参数
cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
    ('Bob', 30, 'bob@example.com')
)

# 动态表名/列名不能参数化——需要用白名单校验
ALLOWED_COLUMNS = {'id', 'name', 'age', 'created_at'}
def safe_order_by(column):
    if column not in ALLOWED_COLUMNS:
        raise ValueError(f"Invalid column: {column}")
    cursor.execute(f"SELECT * FROM users ORDER BY {column}")  # 白名单保证安全
```

> **`%s` 是占位符，不是 `%` 格式化**——不要在 `%s` 外加引号（不要写 `'%s'`），驱动自动处理类型和转义。表名、列名、`ORDER BY`、`LIMIT` 等不能参数化，必须用白名单校验。

---

### commit、close 与事务管理

#### commit 是什么

`commit()` 的作用是**把当前事务中的所有写操作永久写入数据库**。在没有 `autocommit` 的模式下，`INSERT`/`UPDATE`/`DELETE` 执行后并不会立刻生效，而是暂存在一个"草稿区"（事务缓冲区）里，调用 `commit()` 才真正落盘。如果中途出了问题，`rollback()` 可以清空草稿区，回到修改前的状态。

```python
conn = pymysql.connect(...)         # autocommit=False（默认）

cursor.execute("INSERT INTO users VALUES (%s, %s)", ('Alice', 25))
# ↑ 此时数据还在草稿区，数据库里查不到

conn.commit()
# ↑ 草稿区的内容写入磁盘，数据才真正持久化
```

#### SELECT 需要 commit 吗？

**不需要。** `SELECT` 等查询语句只读不改，不产生草稿区的数据，`commit()` 对它没有意义。写了也不报错，但纯属多余：

```python
cursor.execute("SELECT * FROM users")   # 只读查询
conn.commit()                            # 多余，但不报错
```

只有这些操作才需要 `commit()`：

| 操作 | 需要 commit？ | 原因 |
|------|--------------|------|
| `SELECT` | ❌ 不需要 | 只读，不产生待持久化的修改 |
| `INSERT` | ✅ 需要 | 新数据在草稿区，不提交就丢了 |
| `UPDATE` | ✅ 需要 | 同上 |
| `DELETE` | ✅ 需要 | 同上 |
| `CREATE TABLE` | ✅ 需要 | DDL 语句在 pymysql 中也受事务控制 |
| `ALTER TABLE` | ✅ 需要 | 同上 |

> `autocommit=True` 模式下每条写语句自动提交，不需要手动 `commit()`。但如果 `autocommit=False`（默认），忘记 `commit()` 就直接 `close()`，这个连接上的所有写入都会丢失——草稿区随着连接关闭被 MySQL 直接丢弃。

#### close 是什么

`close()` 的作用是**断开与数据库的 TCP 连接，释放连接资源**。数据库的并发连接数是有限的，用完后不关闭会导致连接泄露——大量空闲连接占用服务端资源，新请求可能连不上数据库。

```python
conn.close()    # 断开连接，释放资源
cursor.close()  # 释放游标资源（如果连接已关则会自动释放）
```

#### commit 和 close 的执行顺序

如果连接用了 `with` 语句，pymysql 会在退出时自动处理：

```python
# with 语句下的自动行为：
with pymysql.connect(...) as conn:
    with conn.cursor() as cursor:
        cursor.execute("UPDATE users SET age = 30 WHERE name = %s", ('Alice',))
# 退出 with：无异常 → 自动 commit，然后 close
#          有异常 → 自动 rollback，然后 close
```

手动管理时必须自己处理顺序——**先 commit，后 close**：

```python
conn = pymysql.connect(...)
try:
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET age = 30 WHERE name = %s", ('Alice',))
    conn.commit()      # ✅ 先持久化
except:
    conn.rollback()    # 出错则撤销
finally:
    cursor.close()     # 再释放游标
    conn.close()       # 最后关闭连接
```

**`autocommit` 模式**：

```python
# 方式一：连接时设置（适合只读查询、交互式环境）
conn = pymysql.connect(..., autocommit=True)

# 方式二：执行后手动提交（生产环境推荐，精确控制事务边界）
conn.commit()
```

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| `autocommit=False`（默认） | 写操作需显式 `commit()` | 需要原子性的写操作 |
| `autocommit=True` | 每条写语句自动提交 | 只读查询、临时数据分析 |

> `autocommit=True` 时 `rollback()` 无效——已自动提交的语句无法回滚。

---

### 上下文管理器

pymysql 的连接和游标都支持 `with` 语句，自动处理关闭和提交/回滚：

```python
# 连接级别 — 退出时自动 commit 或 rollback
with pymysql.connect(host='localhost', user='root', password='pw', database='test') as conn:
    with conn.cursor() as cursor:   # 退出 with 块自动关闭游标
        cursor.execute("INSERT INTO logs (msg) VALUES (%s)", ('hello',))
    # 游标已自动关闭
# 连接退出 with 时自动 commit（无异常）或 rollback（有异常），然后关闭连接
```

**与手动管理的对比**：

```python
# ❌ 需要手动处理 — open 和 close 距离远，容易遗漏
conn = pymysql.connect(...)
cursor = conn.cursor()
cursor.execute(...)
conn.commit()
cursor.close()    # ← 容易忘记
conn.close()      # ← 容易忘记

# ✅ with 语句 — 生命周期与缩进绑定，不会遗漏
with pymysql.connect(...) as conn:
    with conn.cursor() as cursor:
        cursor.execute(...)
    # 无需手动 commit/close — 自动处理
```

---

### 连接池

每次请求都新建连接 → 执行 → 关闭，开销巨大（TCP 三次握手 + MySQL 认证）。**连接池**维护一组已建立的长连接，随取随用，用完归还：

```bash
pip install dbutils
```

```python
from dbutils.pooled_db import PooledDB
import pymysql

# 创建连接池（全局单例）
pool = PooledDB(
    creator=pymysql,       # 使用的数据库模块
    maxconnections=10,     # 最大连接数
    mincached=2,           # 初始化时创建的闲置连接数
    maxcached=5,           # 池中最多闲置连接数
    blocking=True,         # 连接池满时是否等待
    host='localhost', user='root', password='pw', database='test',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

# 从池中获取连接（和普通连接用法完全一样）
def query_users():
    conn = pool.connection()      # 从池中借一个连接
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
    finally:
        conn.close()              # 归还连接到池（而非真正断开）
```

> **务必调用 `conn.close()`**——连接池模式下它不是真正关闭连接，而是将连接**归还到池中**供下次复用。忘记关闭会导致连接泄露，池中连接耗尽后所有请求阻塞。

**`maxconnections`、`maxcached`、`mincached`、`blocking`**：

四个参数共同定义了连接池的行为：

| 参数 | 含义 | 示例 |
|------|------|------|
| `maxconnections` | **硬上限**——池中最多同时存在的流动连接总数（借出的 + 闲置的） | `20` |
| `maxcached` | 闲置连接**上限**——池中最多闲置几个（归还时超出就关） | `10` |
| `mincached` | 闲置连接**下限**——池中最少保持几个热连接（低于就自动补） | `2` |
| `blocking` | 池满后怎么办——`True` 排队等，`False` 直接报错 | `True` |

`mincached` 和 `maxcached` 定义的是**同一个闲置池**的下限和上限，不是两个独立的池子：

```
maxcached=10 ── 闲置上限（归还时超过就砍）
      ↑
  闲置池中      ← 实际数在 2~10 之间随流量波动
      ↓
mincached=2  ── 闲置下限（被取走就自动补）
      0
```

三参各管一摊，不会互相叠加。一个完整波动周期：

```
低谷：借出=0，闲置=2（mincached 兜底）
突发：
  借走 2 → 闲置 0，触发 mincached → 自动补 2，闲置回到 2
  又来 10 个请求 → 补到闲置 2 + 借出 12，流动总数 14（< maxconnections=20 ✅）
归还：
  逐步归还 → 闲置 2 → 5 → 10
  又还一个 → 闲置 11 > maxcached → 关掉 1 个，闲置回到 10
```

> - `mincached` 解决**突发流量**——池底始终有热连接备着，来了就取
> - `maxcached` 解决**低谷浪费**——闲时不囤积过多连接占用 MySQL 资源
> - `maxconnections` 解决**并发上限**——用户能同时借出多少连接
> - 多数场景只设其中一两个就够了，三个全设用于精细调优

**连接池的回收机制**：

`PooledDB` 没有后台线程或定时器来自动回收连接，它靠两个被动机制清理：

1. **主动归还**——借出的连接不会自动回池，必须调用 `conn.close()` 触发归还。这是最主要的方式。
2. **池满淘汰**——当归还导致闲置数超过 `maxcached`，多余的连接被真正关闭，不会留在池里。没有 `maxcached` 的话池子只扩张不收敛，峰值过后闲置数会长期卡在高位。

> 闲置连接本身不会拖慢性能——每个闲置连接仅占 MySQL 几百 KB 内存，不消耗 CPU、不产生 I/O。每次新建连接（TCP 三次握手 + MySQL 认证，约 10-50ms）的开销远大于留几条闲置连接。连接池用微小的内存代价换取了每笔请求省下建连延迟，这正是它存在的意义。

**连接池本身需要关闭吗？**

| 场景 | 做法 | 原因 |
|------|------|------|
| Web 应用 / 长期服务 | 不关，模块级单例随进程消亡 | 和应用同生命周期，关掉反而影响后续请求 |
| 一次性脚本 | `pool.close()` | 释放干净，确保进程正常退出 |
| 单元测试 tearDown | `pool.close()` | 隔离用例，避免连接残留 |

`pool.close()` vs `conn.close()`——对象不同：

```python
conn.close()   # 归还连接（不是真正断开），生产代码里高频调用
pool.close()   # 销毁整个池，关闭所有连接。通常不需要手动调用
```

---

### 各库对比

| 库 | 特点 | 适用场景 |
|----|------|----------|
| `pymysql` | 纯 Python，轻量，API 标准 | 大多数项目首选 |
| `mysql-connector-python` | Oracle 官方，纯 Python 和 C 扩展两种模式 | 需要官方支持的场景 |
| `mysqlclient` | C 扩展，速度快，Django 默认 | 高性能、Django 项目 |
| `SQLAlchemy` | ORM，支持多数据库，迁移工具 | 复杂业务模型、多数据库 |

> 只用 MySQL → `pymysql`；需要 ORM/多数据库 → `SQLAlchemy`；Django 项目 → `mysqlclient` 是自动安装的默认驱动。

---

## 🧪 练习 / 验证

> 💡 暂时没装 MySQL？可以用 Python 自带的 `sqlite3` 替代练习——只需把 `%s` 统一替换为 `?`，`pymysql.connect(...)` 替换为 `sqlite3.connect(':memory:')`，其余 API（cursor/execute/fetchall/commit/with）完全一致。

---

### 练习 1：建表与插入数据

编写代码连接 MySQL，创建 `students` 表并插入三条记录。

```python
import pymysql

with pymysql.connect(
    host='localhost', user='root', password='pw', database='test',
    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
) as conn:
    with conn.cursor() as cursor:
        # 建表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                age INT NOT NULL,
                score DECIMAL(4,1) DEFAULT 0.0
            )
        ''')

    # 批量插入
    data = [('张三', 20, 88.5), ('李四', 22, 92.0), ('王五', 21, 76.5)]
    with conn.cursor() as cursor:
        cursor.executemany(
            "INSERT INTO students (name, age, score) VALUES (%s, %s, %s)",
            data
        )
# conn 退出 with 自动提交

# 验证
with pymysql.connect(
    host='localhost', user='root', password='pw', database='test',
    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)
```

> [!info]- 预期输出
> ```
> {'id': 1, 'name': '张三', 'age': 20, 'score': 88.5}
> {'id': 2, 'name': '李四', 'age': 22, 'score': 92.0}
> {'id': 3, 'name': '王五', 'age': 21, 'score': 76.5}
> ```

---

### 练习 2：参数化查询实现登录校验

编写函数 `check_login(username, password)`，使用参数化查询防止 SQL 注入。

```python
import pymysql

def check_login(username, password):
    with pymysql.connect(
        host='localhost', user='root', password='pw', database='test',
        charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id FROM users WHERE username = %s AND password = %s",
                (username, password)
            )
            return cursor.fetchone() is not None

# 正确调用
print(check_login('alice', 'secret123'))

# 攻击尝试 — 参数化查询下攻击字符串被当作普通值处理，不会改变 SQL 语义
print(check_login("' OR 1=1 --", ''))  # → False（安全）
```

> [!info]- 预期输出
> ```
> True
> False
> ```

---

### 练习 3：事务——转账操作

编写 `transfer(from_id, to_id, amount)` 函数实现转账，要求使用事务保证原子性。

```python
import pymysql

def transfer(from_id, to_id, amount):
    conn = pymysql.connect(
        host='localhost', user='root', password='pw', database='bank',
        charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with conn.cursor() as cursor:
            # 检查余额
            cursor.execute("SELECT balance FROM accounts WHERE id = %s", (from_id,))
            row = cursor.fetchone()
            if row is None:
                raise Exception(f"账户 {from_id} 不存在")
            if row['balance'] < amount:
                raise Exception(f"账户 {from_id} 余额不足")

            # 扣款
            cursor.execute(
                "UPDATE accounts SET balance = balance - %s WHERE id = %s",
                (amount, from_id)
            )
            # 入账
            cursor.execute(
                "UPDATE accounts SET balance = balance + %s WHERE id = %s",
                (amount, to_id)
            )
        conn.commit()
        print(f"转账成功：{from_id} → {to_id}，金额 {amount}")
    except Exception as e:
        conn.rollback()
        print(f"转账失败，已回滚：{e}")
    finally:
        conn.close()

# 正常转账
transfer(1, 2, 200)

# 余额不足
transfer(1, 2, 2000)
```

> [!info]- 预期输出
> ```
> 转账成功：1 → 2，金额 200
> 转账失败，已回滚：账户 1 余额不足
> ```

---

### 练习 4：连接池查询

使用 `DBUtils` 创建连接池，通过连接池执行分页查询。

```python
from dbutils.pooled_db import PooledDB
import pymysql

pool = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=1,
    maxcached=3,
    blocking=True,
    host='localhost', user='root', password='pw', database='test',
    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor,
)

def get_page(page=1, page_size=10):
    """分页查询 students 表"""
    offset = (page - 1) * page_size
    conn = pool.connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM students ORDER BY id LIMIT %s OFFSET %s",
                (page_size, offset)
            )
            return cursor.fetchall()
    finally:
        conn.close()  # 归还到池

# 查询第 1 页
print(get_page(1, 2))
```

> [!info]- 预期输出
> ```
> [{'id': 1, 'name': '张三', 'age': 20, 'score': 88.5},
>  {'id': 2, 'name': '李四', 'age': 22, 'score': 92.0}]
> ```

---

## 🤔 常见误区

1. **误区：用字符串拼接构建 SQL**
   **事实**：这是引发 SQL 注入的根本原因。始终使用参数化查询（`%s` 占位符 + 参数元组），让驱动完成转义和类型转换。即便是内部脚本也不应拼接——习惯决定安全底线。

2. **误区：`fetchall()` 适用于任何场景**
   **事实**：当查询结果很大（百万行级别）时，`fetchall()` 会将全部数据加载到内存，可能导致 OOM。大数据量场景应使用 `SSCursor`（服务端游标）配合 `fetchmany()` 逐批读取，或直接在 SQL 中 `LIMIT` 分页。

3. **误区：忘记关闭连接/游标**
   **事实**：数据库的连接数是有限的，不关闭连接会造成连接泄露，最终耗尽连接池导致服务不可用。用 `with` 语句自动管理生命周期是更好的选择。

4. **误区：连接池模式下 `conn.close()` 会断开连接**
   **事实**：连接池模式下 `close()` 只是归还连接到池，并不会真正断开。但如果忘记调用 `close()`，连接不会被归还，等同于泄露。

5. **误区：`autocommit=True` 下可以回滚**
   **事实**：`autocommit=True` 让每条语句立即提交，`rollback()` 无法撤销已提交的内容。需要原子性的写操作必须设 `autocommit=False` 并显式调用 `commit()`/`rollback()`。

---

## 🔗 相关资源

- 上一节：[[PY024-正则表达式]]
- **卡片知识**：[[PL-005-正则表达式基础]]
- 官方文档：[PyMySQL Documentation](https://pymysql.readthedocs.io/)
- [DBUtils 文档](https://dbutils.readthedocs.io/)
- [SQLAlchemy 官方文档](https://docs.sqlalchemy.org/)

## 📝 待补充内容

- [ ] ORM 框架 SQLAlchemy 的深度介绍 — 模型定义、关联查询、Session 管理
- [ ] 异步 MySQL 操作 — aiomysql 的使用
- [ ] MySQL 慢查询日志分析与 Python 集成
- [ ] 数据库迁移工具 Alembic 的使用
- [ ] 连接池参数调优 — maxconnections、maxcached 的最佳实践
