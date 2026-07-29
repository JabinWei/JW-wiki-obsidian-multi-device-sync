---
type: flowchart
style: sketch-notes
aspect: 4:3
---

Illustration: Python yield generator lifecycle — ONLY about yield pause and resume. NO return comparison.

STYLE: Sketch-notes educational diagram. Warm cream paper, hand-drawn lines, soft pastels.

CONTENT: A cyclic flow showing generator lifecycle:

TOP "创建生成器": gen = count_up_to(3) → box labeled "生成器对象 (待命)", arrow down

THREE ITERATIONS in a loop:
- "next(gen) #1" → enters function → executes until `yield 1` → ⏸ PAUSED (coral marker) → caller receives 1
- "next(gen) #2" → resumes from pause → continues to `yield 2` → ⏸ PAUSED → caller receives 2  
- "next(gen) #3" → resumes → `yield 3` → ⏸ PAUSED → caller receives 3

BOTTOM "next(gen) #4": → function runs to end (no more yield) → raises StopIteration (soft red)

KEY NOTES: "暂停时保留局部变量和执行位置" | "每次 next() 从上次暂停处继续"

COLORS: Cream paper (#FAF5ED). Generator flow in pastel teal. Pause markers in coral. StopIteration in soft red. Labels in charcoal. ONLY yield mechanism — no return comparison anywhere on the image.

Watermark: "@Jabin W." bottom-right.
