---
layout: linear-progression
style: technical-schematic
aspect: 16:9
language: zh
---

# Infographic: Python pymysql 操作 MySQL 全流程

## Title
Python 操作 MySQL 数据库全流程（pymysql）

## Main Flow — 6-Step Linear Progression (horizontal, left to right)

**Step 1: 建立连接 connect()**
- pymysql.connect(host, port, user, password, database, charset='utf8mb4')
- 连接参数：host, port=3306, user, password, database, charset, cursorclass, autocommit
- Icon: plug/socket connection icon

**Step 2: 创建游标 cursor()**
- conn.cursor() — SQL 通过游标发送，结果通过游标取回
- 游标类型：Cursor(元组), DictCursor(字典), SSCursor(服务端游标)
- Icon: pointer/cursor icon

**Step 3: 执行 SQL execute()**
- execute(sql, params) — 单条执行
- executemany(sql, params_list) — 批量执行
- ⚠️ 用 %s 占位符，禁止字符串拼接（SQL 注入风险）
- Icon: gear/execute icon

**Step 4: 获取结果 fetch**
- fetchone() → 单行, fetchall() → 全部, fetchmany(n) → N行
- 游标指针顺次消费，取过的行不再返回
- Icon: download/receive icon

**Step 5: 提交/回滚 commit/rollback**
- SELECT 不需要 commit，INSERT/UPDATE/DELETE 需要
- autocommit=False → 手动 commit；autocommit=True → 自动提交
- 异常时 rollback() 撤销草稿区数据
- Icon: checkmark/shield icon

**Step 6: 关闭连接 close()**
- cursor.close() → conn.close()
- 或用 with 语句自动管理生命周期
- 连接池模式下 close() = 归还，不是断开
- Icon: power/close icon

## Bottom Section — Key Comparisons (2 panels side by side)

**Panel A: SQL 注入对比**
- ❌ f"SELECT * FROM users WHERE name = '{name}'" — 危险!
- ✅ "SELECT * FROM users WHERE name = %s", (name,) — 安全

**Panel B: 游标类型对比**
- Cursor → row[0] 元组下标
- DictCursor → row['name'] 字典键名
- SSCursor → 大数据流式读取

## Top-Right Corner: 连接池架构
PooledDB(maxconnections=20, mincached=2, maxcached=10)
→ pool.connection() 借 → conn.close() 还

## Visual Design
- Blueprint style: white lines on deep blue (#1E3A5F) background
- Grid pattern background with subtle engineering grid
- 6 steps connected by arrows with step numbers in circles
- Clean sans-serif Chinese font, technical stencil feel
- Amber (#F59E0B) highlights for warnings and key points
- Cyan callouts for tips and notes
- Each step has a distinct icon and 2-3 bullet points
