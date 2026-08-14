Create a professional infographic following these specifications:

## Image Specifications
- **Type**: Infographic
- **Layout**: linear-progression
- **Style**: hand-drawn-edu (macaron pastels, hand-drawn wobble lines, simple stick figures, friendly educational)
- **Aspect Ratio**: 16:9
- **Language**: zh

## Style Guidelines
- Background: Warm cream paper (#FAF5ED)
- Lines: Hand-drawn wobble strokes, soft rounded corners
- Colors: macaron pastels — soft blue, soft coral, soft green, soft amber
- Typography: Rounded friendly sans-serif; code snippets in monospace
- A simple friendly Python snake mascot guides the flow; arrows are curvy hand-drawn style

## Content

### Title
pytest fixture — yield 怎么驱动测试

### Subtitle
fixture 是一个生成器：yield 之前准备、yield 之后清理，pytest 用 next() 走走停停

### 步骤 1（准备）
- fixture 函数开始执行
- `conn = connect_database()`
- 图标：小蛇抱着一个数据库/工具盒

### 步骤 2（yield 暂停交值）
- `yield conn`
- 执行到这里「暂停」，把 conn 交给 pytest
- 图标：小蛇举着一个「暂停」牌，递出一个连接块

### 步骤 3（测试执行）
- `test_insert(db)` 里 `db` = conn
- pytest 按「参数名 = fixture 名」自动注入
- 图标：小蛇对着测试函数卡片打勾（assert 断言）

### 步骤 4（next() 恢复）
- 测试结束后，pytest 再次 `next(gen)`
- 从 yield 下一行继续执行
- 图标：小蛇按下一个「继续」按钮

### 步骤 5（清理）
- `conn.close()` 释放资源
- 即使测试失败也一定执行（pytest 用 try/finally 保证）
- 图标：小蛇把工具收进盒子

### Bottom: Conclusion bar
「yield 前 = 准备，yield 后 = 清理；测试失败也会走清理」
