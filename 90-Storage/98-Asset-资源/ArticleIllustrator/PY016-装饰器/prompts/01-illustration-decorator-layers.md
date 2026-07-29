---
type: comparison
style: sketch-notes
aspect: 4:3
---

Illustration: Python decorator — two-layer vs three-layer closure model.

STYLE: Sketch-notes educational diagram. Warm cream paper, hand-drawn lines, soft pastels.

CONTENT: Two columns on cream paper:

LEFT "两层闭包 (@decorator)":
Layer 1: decorator receives func → returns wrapper
Layer 2: wrapper executes, calls original func
Example: @timer → timer(func) → wrapper
Execution: 定义时装饰（外层跑一次），调用时跑 wrapper（内层每次跑）

RIGHT "三层闭包 (@deco(args))":
Layer 1: factory receives config args → returns decorator
Layer 2: decorator receives func → returns wrapper  
Layer 3: wrapper executes, calls original func
Example: @retry(3) → retry(3)(func) → wrapper
Execution: 定义时先跑 factory 再跑 decorator（两层都跑一次），调用时跑 wrapper

BOTTOM NOTE: "两层 = 无参数装饰器 | 三层 = 带参数装饰器"

COLORS: Cream paper. Two-layer in pastel teal. Three-layer in pastel coral. Arrow flow lines in charcoal.

Watermark: "@Jabin W." bottom-right.
