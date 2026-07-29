---
type: comparison
style: sketch-notes
aspect: 3:2
---

Illustration: Python parameter passing — immutable vs mutable objects.

STYLE: Sketch-notes educational diagram. Warm cream paper, hand-drawn lines, soft pastels. Clean, focused, one concept.

CONTENT: Two side-by-side examples on cream paper:

LEFT "不可变对象 (int/str/tuple)":
- Box labeled "a=10" → function modify(x) → x=11 inside function → a still 10 outside
- Arrow shows: function gets a COPY, original untouched
- Label: "像值传递"

RIGHT "可变对象 (list/dict)":
- Box labeled "b=[1,2,3]" → function modify(lst) → lst.append(4) → b becomes [1,2,3,4]
- Arrow shows: function gets the REFERENCE, modifies the SAME object
- Label: "像引用传递"

BOTTOM WARNING: "可变默认参数陷阱" with code: ❌ def f(lst=[]) → ✅ def f(lst=None)

COLORS: Cream paper. Immutable side in pastel blue. Mutable side in pastel coral. Warning in soft yellow.

Watermark: "@Jabin W." bottom-right.
