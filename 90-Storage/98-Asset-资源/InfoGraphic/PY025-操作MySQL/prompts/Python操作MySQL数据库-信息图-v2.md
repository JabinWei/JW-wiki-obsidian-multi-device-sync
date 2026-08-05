---
layout: linear-progression
style: hand-drawn-edu
aspect: 16:9
language: zh
---

# Infographic: Python pymysql 操作 MySQL 全流程

## Global Style
Warm cream paper (#F5F0E8) background with subtle grain. All lines have slight hand-drawn wobble — no perfect geometry. Macaron pastel rounded cards as information zones. Simple stick-figure Python snake character appears at key steps. Doodle decorations: small stars, sparkles, wavy underlines throughout.

## Title (Top, bold hand-lettered)
🐍 Python 操作 MySQL 全流程
Subtitle: pymysql 六步走，从连接到关闭

## Main Flow — 6 Steps as pastel cards, connected by wavy hand-drawn arrows (horizontal)

**Card 1 (Macaron Blue #A8D8EA): ① 连接 connect()**
- pymysql.connect(host, port, user, password, database)
- 默认端口 3306，charset='utf8mb4'
- Stick figure holding a plug, connecting to a database icon

**Card 2 (Macaron Mint #B5E5CF): ② 创建游标 cursor()**
- conn.cursor() — SQL 和结果的中转站
- DictCursor 让结果像字典一样访问
- Stick figure with a pointer/arrow cursor icon

**Card 3 (Macaron Lavender #D5C6E0): ③ 执行 SQL execute()**
- execute(sql, %s 占位符)
- ⚠️ 禁止字符串拼接！（Coral Red emphasis）
- executemany() 批量插入更快
- Lock icon with checkmark

**Card 4 (Macaron Peach #FFD5C2): ④ 获取结果 fetch**
- fetchone() / fetchall() / fetchmany(n)
- 游标指针顺次消费
- Stick figure catching floating data blocks

**Card 5 (Macaron Blue): ⑤ 提交/回滚 commit/rollback**
- SELECT 不需要 commit
- INSERT/UPDATE/DELETE 必须 commit
- 出错 rollback() 撤销草稿
- Shield icon with checkmark and X

**Card 6 (Macaron Mint): ⑥ 关闭 close()**
- cursor.close() → conn.close()
- 连接池：close() = 归还，不是断开
- Power button icon

## Bottom Section — Two comparison panels in doodle boxes

**Left panel (dashed border): SQL 注入对比**
- ❌ f"SELECT ... WHERE name = '{name}'" → 危险！
- ✅ "SELECT ... WHERE name = %s", (name,) → 安全
- Coral Red (#E8655A) warning doodle

**Right panel (dashed border): 连接池小贴士**
- PooledDB 参数：maxconnections(上限) / mincached(下限) / maxcached(闲置上限)
- 借：pool.connection() → 还：conn.close()
- Lightbulb doodle icon

## Bottom Takeaway (bold, centered)
"用 %s 占位符，别拼字符串。commit 写操作，close 还连接。"
