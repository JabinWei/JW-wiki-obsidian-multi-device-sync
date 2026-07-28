---
layout: binary-comparison
style: storybook-watercolor
aspect: 16:9
language: zh
---

Create an educational infographic comparing Python tuples vs lists in Chinese.

STYLE: storybook-watercolor — Soft watercolor painted feel, whimsical brush strokes, gentle color bleeds, storybook illustration aesthetic. Warm, dreamy, artistic. Like a beautifully illustrated children's encyclopedia page, but sophisticated. No harsh borders.

CONTENT — Two-column comparison:

LEFT "列表 List": Mutable | 可增删改 | 内存大 | 不能做字典键 | 方法多 (append/pop/sort)

RIGHT "元组 Tuple": Immutable | 只读 | 内存小速度快 | **可做字典键** | 方法少 (count/index)

CENTER: 
- 单元素陷阱: (42) ≠ (42,) — 逗号是关键
- 解包: a,b = (1,2) | a,*b = (1,2,3) 
- namedtuple: t.name 替代 t[0]

BOTTOM: "不可变的是引用，不是对象 — PL-PY-005"

COLORS: Soft watercolor — indigo #5B7A9E, dusty rose #C4887C, sage green #8FA88F, warm cream #F5F0E8. Organic brush edges, no hard lines. Title in soft hand-lettered font.
