---
layout: bento-grid
style: technical-schematic
aspect: 16:9
language: zh
---

Create an educational infographic about Python list operations in Chinese.

STYLE: technical-schematic — Blueprint engineering grid background, clean technical lines, but with hand-drawn annotation accents for warmth. Think architectural blueprint with sketch notes in the margins. Not cold or corporate — an engineer's notebook.

CONTENT (4 cards on blueprint grid):

CARD 1 (top-left): "CRUD 操作速查" —
A compact reference table showing list methods with time complexity:
append O(1) | insert O(n) | extend O(k)
pop O(1) | remove O(n) | del / clear
lst[i]=x | lst[1:4]=[a,b] | sort O(n log n)
in O(n) | index O(n) | count O(n)
Tiny annotation: "✅ O(1) 操作优先使用"

CARD 2 (top-right): "sort vs sorted" —
Side-by-side comparison with blueprint divider line:
list.sort(): 原地修改 | O(1)内存 | 返回None | 🔗底层Timsort
sorted(): 新建列表 | O(n)内存 | 返回新列表 | 原数据不变
Small note: "Python 使用 Timsort — 详见PL-007卡片"

CARD 3 (bottom-left): "列表比较四法" —
Four methods in a clean row:
1. `==` 严格比较(顺序+内容)
2. `Counter()` 忽略顺序
3. `set()` 忽略顺序+去重
4. 集合运算 `- &` 找差异/交集
Each with tiny code snippet example

CARD 4 (bottom-right): "翻转与反转" —
Side-by-side:
reverse(): 原地 | O(n/2) | 无返回值
[::-1]: 新建 | O(n) | 返回新列表
Small note: "大列表用 reverse() 省内存"

TITLE: "Python 列表全场景操作" in clean technical font, confident.

COLORS: Blueprint blue (#1E3A5F) grid on off-white (#F5F7FA) paper. Hand-drawn annotations in warm amber (#C8883C). Method names in deep charcoal. Complexity labels in muted coral (#D4786B). Clean, technical, approachable.

Keep text minimal. Blueprint precision + hand-drawn warmth.
