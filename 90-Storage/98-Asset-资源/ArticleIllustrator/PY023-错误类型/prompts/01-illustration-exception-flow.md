---
type: flowchart
style: sketch-notes
aspect: 4:3
---

Illustration: Python try/except/else/finally execution flow.

STYLE: Sketch-notes educational flowchart. Warm cream paper, hand-drawn lines, soft pastels.

CONTENT: A decision-tree flowchart showing exception handling paths:

START (pastel green): "进入 try 块"
↓
DECISION DIAMOND: "有异常？"
↓ NO → RIGHT PATH: "执行 else 块" (pastel teal) → "执行 finally" (pastel gray) → END
↓ YES → 
DECISION: "被 except 捕获？"
↓ YES → "执行匹配的 except" (pastel coral) → "执行 finally" (pastel gray) → END
↓ NO → "执行 finally" (pastel gray) → "异常向上传播" (pastel red, dashed arrow)

Also show a small secondary box: "finally 中的 return/break/continue vs try 中的" with notes.

BOTTOM SUMMARY: 4 scenarios in pastel blocks:
1. 正常: try → else → finally
2. 捕获: try → except → finally  
3. 未捕获: try → finally → 传播
4. return: finally → return

COLORS: Cream paper. Try=green, except=coral, else=teal, finally=gray, error=red. Hand-drawn.

Watermark: "@Jabin W." bottom-right.
