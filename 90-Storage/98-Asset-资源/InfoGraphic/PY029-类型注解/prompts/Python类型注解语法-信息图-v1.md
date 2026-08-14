Create a professional infographic following these specifications:

## Image Specifications
- **Type**: Infographic
- **Layout**: bento-grid
- **Style**: corporate-memphis (flat vector, vibrant, geometric Memphis shapes, clean modern)
- **Aspect Ratio**: 16:9
- **Language**: zh

## Style Guidelines
- Background: Warm off-white (#FAF5ED) with subtle flat geometric accents
- Cards: Rounded rectangles with flat fills, distinct accent colors per card
- Colors: deep navy (#1E3A5F), coral (#F27A5E), teal (#2A9D8F), amber (#F4A261), muted gold
- Typography: Clean sans-serif, key code snippets in monospace
- Flat vector illustration style, generous spacing, no photographic textures

## Content

### Title
Python 类型注解 — 给代码写说明书

### Subtitle
注解是给人/IDE 看的「类型说明书」，运行时不强制检查，配合 mypy 做静态检查

### 卡片 1：变量注解
- 语法：`变量名: 类型 = 值`
- 示例：`name: str = "Alice"` / `age: int = 30` / `scores: list[int] = [90, 85]`

### 卡片 2：函数注解
- 语法：`def 函数名(参数: 类型) -> 返回类型:`
- 示例：`def add(a: int, b: int) -> int:`
- 标注 `-> None` 表示不返回有用值

### 卡片 3：常用类型
- 基础：`int` / `str` / `float` / `bool`
- `Optional[T]` = T 或 None（Python 3.10+ 写作 `T | None`）
- `Union[X, Y]` = X 或 Y（写作 `X | Y`）
- `Any` = 任意类型（逃逸口，慎用）

### 卡片 4：泛型
- `list[int]`、`dict[str, int]`、`tuple[int, str]`
- 容器 + 元素类型，比裸 `list` 更精确
- Python 3.9+ 直接用内建小写版本

### 卡片 5：mypy 静态检查
- 不运行代码，扫描源码推演类型
- 抓出 `add(1, "2")` 这种运行前就能发现的类型错误
- 报错是「提示」，不影响程序运行

### Bottom: Conclusion bar
「类型注解 = 描述性说明，不改运行行为；真正的检查交给 mypy / IDE」
