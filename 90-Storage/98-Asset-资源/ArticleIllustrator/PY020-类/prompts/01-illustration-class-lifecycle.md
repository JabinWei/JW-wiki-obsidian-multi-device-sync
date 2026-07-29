---
type: flowchart
style: sketch-notes
aspect: 4:3
---

Illustration: Python class lifecycle from creation to destruction.

STYLE: Sketch-notes educational flowchart. Warm cream paper, hand-drawn lines, soft pastels.

CONTENT: A left-to-right timeline/flow with 4 stages, connected by hand-drawn arrows:

STAGE 1 "__new__(cls)": 
- Box label: "创建空实例"
- Sub-text: "分配内存, 返回裸对象"
- Pastel blue block

STAGE 2 "__init__(self)": 
- Box label: "初始化属性"
- Sub-text: "self.name = name"
- Pastel coral block  
- Arrow from Stage 1 reads: "如果 __new__ 返回本类实例"

STAGE 3 "使用阶段":
- Box label: "对象存活期"
- Sub-text: "调用方法, 访问属性"
- Pastel green block

STAGE 4 "__del__": 
- Box label: "销毁"
- Sub-text: "引用计数归零时自动调用"
- Pastel gray block, dashed border

BOTTOM NOTE: "99% 只需 __init__ | 重写 __new__ 用于单例/不可变类型继承"

COLORS: Cream paper. Stage 1 in pastel blue. Stage 2 in coral. Stage 3 in green. Stage 4 in gray.

Watermark: "@Jabin W." bottom-right.
