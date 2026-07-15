#!/usr/bin/env python3
"""生成 PY001 Python 简介的概念图，参考 Turn-based 概念图风格"""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "/Users/weijibin/Documents/obsidian-notes/00-Core/01-CoreKnowledge-核心知识/C001-计算机基础知识/CB001-编程语言/PL001-Python"
W, H = 1800, 1005

# ── 字体 ──────────────────────────────────────────────
def load_font(size, bold=False):
    """加载中文字体"""
    paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

FONT_TITLE   = load_font(36)
FONT_H1      = load_font(28)
FONT_H2      = load_font(22)
FONT_BODY    = load_font(17)
FONT_SMALL   = load_font(14)
FONT_TINY    = load_font(12)

# ── 颜色方案 ──────────────────────────────────────────
BG       = (255, 255, 255)  # 白底
TITLE_BG = (30, 30, 45)     # 深色标题栏
ACCENT1  = (65, 105, 225)   # 皇家蓝 — 主要
ACCENT2  = (220, 80, 60)    # 红 — 强调/误区
ACCENT3  = (40, 160, 100)   # 绿 — 正确/流程
ACCENT4  = (240, 150, 30)   # 橙 — 警告/注意
ACCENT5  = (120, 80, 200)   # 紫 — 对比
GRAY1    = (245, 245, 248)  # 浅灰底
GRAY2    = (220, 220, 228)  # 边框灰
GRAY3    = (100, 100, 115)  # 文字灰
DARK     = (30, 30, 45)     # 深色文字
WHITE    = (255, 255, 255)

# ── 绘图工具函数 ──────────────────────────────────────
def new_canvas():
    return Image.new("RGB", (W, H), BG), ImageDraw.Draw(Image.new("RGB", (W, H), BG))

def draw_title_bar(draw, text, subtitle=""):
    """顶部标题栏"""
    draw.rectangle([(0, 0), (W, 80)], fill=TITLE_BG)
    draw.text((40, 18), text, fill=WHITE, font=FONT_TITLE)
    if subtitle:
        draw.text((40, 58), subtitle, fill=(180, 180, 195), font=FONT_TINY)
    # 底部装饰线
    draw.rectangle([(0, 80), (W, 85)], fill=ACCENT1)

def rounded_box(draw, xy, fill, outline=None, radius=12):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline or fill)

def arrow_right(draw, x1, y, x2, color=GRAY3, w=3):
    """右箭头"""
    draw.line([(x1, y), (x2, y)], fill=color, width=w)
    draw.polygon([(x2-8, y-6), (x2, y), (x2-8, y+6)], fill=color)

def arrow_down(draw, x, y1, y2, color=GRAY3, w=3):
    """下箭头"""
    draw.line([(x, y1), (x, y2)], fill=color, width=w)
    draw.polygon([(x-6, y2-8), (x, y2), (x+6, y2-8)], fill=color)

def text_box(draw, xy, text, font, fill=DARK, bg=None, pad=10, align="left"):
    """带背景的文字框"""
    x1, y1, x2, y2 = xy
    if bg:
        rounded_box(draw, xy, bg, radius=6)
    if align == "center":
        tw = draw.textlength(text, font=font)
        draw.text((x1 + (x2-x1-tw)/2, y1 + pad), text, fill=fill, font=font)
    else:
        draw.text((x1 + pad, y1 + pad), text, fill=fill, font=font)

def multi_text(draw, x, y, lines, font, fill=DARK, line_h=None):
    """绘制多行文本"""
    if line_h is None:
        line_h = font.size + 6
    for i, line in enumerate(lines):
        draw.text((x, y + i * line_h), str(line), fill=fill, font=font)

def h_line(draw, y, color=GRAY2, w=1):
    draw.line([(40, y), (W-40, y)], fill=color, width=w)

# ═══════════════════════════════════════════════════════
# 图1：Python 发展历史与哲学
# ═══════════════════════════════════════════════════════
def img1_history():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_title_bar(draw, "PY001 Python 发展历史与设计哲学", "Python 从哪里来，为什么这样设计？")

    # ── 时间轴 ──
    timeline_y = 115
    draw.rectangle([(40, timeline_y), (W-40, timeline_y+4)], fill=GRAY2)
    nodes = [
        (80,  "1989 圣诞", "Guido 在家\n写\"私活\"项目"),
        (340, "1991", "Python 0.9.0\n首次公开发布"),
        (600, "1994", "Python 1.0\nlambda/map/filter"),
        (860, "2000", "Python 2.0\nGC + Unicode"),
        (1120,"2008", "Python 3.0\n重大升级"),
        (1380,"2004", "Python 之禅\nTim Peters"),
    ]
    for x, label, desc in nodes:
        draw.ellipse([(x-8, timeline_y-6), (x+8, timeline_y+14)], fill=ACCENT1)
        draw.text((x - draw.textlength(label, FONT_TINY)//2, timeline_y + 18), label, fill=ACCENT1, font=FONT_TINY)
        lines = desc.split("\n")
        for i, ln in enumerate(lines):
            tw = draw.textlength(ln, FONT_SMALL)
            draw.text((x - tw//2, timeline_y + 36 + i*18), ln, fill=DARK, font=FONT_SMALL)

    # ── 左栏：灵感来源 ──
    ly = 230
    rounded_box(draw, (40, ly, 570, ly+180), GRAY1, GRAY2, 12)
    draw.text((60, ly+10), "🎬 灵感来源", fill=ACCENT1, font=FONT_H2)
    multi_text(draw, 60, ly+42, [
        "• 继承 ABC 教学语言 — 简洁、易读、易用",
        "• 弥补 ABC 缺陷 — 开放、可扩展、与 C 交互",
        "• 填补 C 和 Shell 之间的空白",
    ], FONT_BODY, line_h=28)
    multi_text(draw, 60, ly+128, [
        "🏷️ 命名来源: Monty Python 喜剧团（非蟒蛇！）",
    ], FONT_SMALL, fill=ACCENT3, line_h=22)

    # ── 右栏：Python 之禅 ──
    rounded_box(draw, (610, ly, 1760, ly+180), GRAY1, GRAY2, 12)
    draw.text((630, ly+10), "🧘 Python 之禅 (The Zen of Python)", fill=ACCENT4, font=FONT_H2)
    draw.text((630, ly+44), "输入 import this 查看全部 19 条格言", fill=GRAY3, font=FONT_SMALL)
    zen_items = [
        ("优美胜于丑陋", "Beautiful is better than ugly.", ACCENT1),
        ("明确胜于隐晦", "Explicit is better than implicit.", ACCENT3),
        ("简单胜于复杂", "Simple is better than complex.", ACCENT4),
        ("可读性很重要", "Readability counts.", ACCENT5),
    ]
    for i, (cn, en, clr) in enumerate(zen_items):
        bx = 630 + i * 280
        rounded_box(draw, (bx, ly+68, bx+260, ly+170), WHITE, clr, 8)
        draw.text((bx+12, ly+78), cn, fill=clr, font=FONT_H2)
        draw.text((bx+12, ly+118), en, fill=GRAY3, font=FONT_SMALL)

    # ── 底部：一句话总结 ──
    rounded_box(draw, (40, 430, 1760, 500), TITLE_BG, radius=12)
    draw.text((60, 446), "💡 核心认知", fill=ACCENT4, font=FONT_H2)
    multi_text(draw, 60, 478, [
        "Python = ABC 的优雅 + C 的开放 + Monty Python 的趣味精神",
        "Python 的成功秘诀：简洁哲学 × 强大社区 × AI/数据科学生态",
    ], FONT_BODY, fill=WHITE, line_h=28)

    # ── 底部卡片 ──
    cards = [
        ("👤 创造者", "Guido van Rossum\n荷兰程序员"),
        ("📅 诞生", "1989年圣诞节\n荷兰阿姆斯特丹"),
        ("🔑 关键版本", "2.0 (2000) → 3.0 (2008)\n3.0 不向后兼容"),
        ("🏆 设计目标", "易读易写\n快速开发"),
    ]
    for i, (title, desc) in enumerate(cards):
        cx = 40 + i * 440
        rounded_box(draw, (cx, 520, cx+410, 630), WHITE, GRAY2, 10)
        text_box(draw, (cx, 520, cx+410, 555), title, FONT_H2, fill=ACCENT1)
        multi_text(draw, cx+15, 565, desc.split("\n"), FONT_BODY, DARK, line_h=26)

    # 页脚
    draw.text((W//2 - 100, H-30), "PY001 Python 简介 · 概念图 1/4", fill=GRAY3, font=FONT_TINY)

    img.save(f"{OUTPUT_DIR}/PY001-概念图1-发展历史与哲学.png")
    print("✅ 图1: 发展历史与哲学")

# ═══════════════════════════════════════════════════════
# 图2：Python 代码执行过程
# ═══════════════════════════════════════════════════════
def img2_execution():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_title_bar(draw, "PY001 Python 代码执行过程", "从 .py 源码到屏幕输出，背后发生了什么？")

    # ── 执行流程（横向流水线） ──
    flow_y = 120
    steps = [
        ("📄 源代码\n.py 文件", ACCENT5, 200),
        ("🔍 词法分析\nTokenization", ACCENT1, 220),
        ("🌳 语法分析\n生成 AST", ACCENT1, 220),
        ("⚙️ 编译\n生成字节码 .pyc", ACCENT3, 240),
        ("🖥️ PVM\nPython 虚拟机", ACCENT4, 240),
        ("💻 操作系统\n最终执行", ACCENT2, 200),
    ]
    x_pos = 40
    for i, (label, color, w_box) in enumerate(steps):
        rounded_box(draw, (x_pos, flow_y, x_pos + w_box, flow_y + 90), color, radius=12)
        lines = label.split("\n")
        for j, ln in enumerate(lines):
            tw = draw.textlength(ln, FONT_BODY)
            draw.text((x_pos + (w_box - tw)//2, flow_y + 20 + j*26), ln, fill=WHITE, font=FONT_BODY)
        if i < len(steps) - 1:
            arrow_right(draw, x_pos + w_box + 4, flow_y + 45, x_pos + w_box + 26, ACCENT1, 3)
        x_pos += w_box + 30

    # ── 左栏：编译细节 ──
    ly = 240
    rounded_box(draw, (40, ly, 870, ly+350), GRAY1, GRAY2, 12)
    draw.text((60, ly+10), "🔬 编译阶段详解", fill=ACCENT1, font=FONT_H2)
    sub_items = [
        ("① 词法分析", "源代码 → Token 流", "x = 10 → 标识符x, 运算符=, 数字10"),
        ("② 语法分析", "Token → AST 抽象语法树", "检查语法，构建树状结构"),
        ("③ 字节码生成", "AST → .pyc 字节码", "平台无关的低级指令集"),
    ]
    for i, (title, flow, detail) in enumerate(sub_items):
        sy = ly + 50 + i*95
        rounded_box(draw, (60, sy, 840, sy+82), WHITE, ACCENT1 if i==0 else ACCENT3 if i==1 else ACCENT4, 8)
        draw.text((80, sy+6), title, fill=ACCENT1, font=FONT_H2)
        draw.text((80, sy+34), f"{flow}     |     {detail}", fill=DARK, font=FONT_SMALL)

    # ── 右栏：PVM + GIL ──
    rounded_box(draw, (900, ly, 1760, ly+350), GRAY1, GRAY2, 12)
    draw.text((920, ly+10), "🖥️ PVM 与 GIL", fill=ACCENT4, font=FONT_H2)

    # PVM box
    rounded_box(draw, (920, ly+50, 1740, ly+180), WHITE, ACCENT4, 8)
    draw.text((940, ly+58), "Python 虚拟机 (PVM)", fill=ACCENT4, font=FONT_H2)
    multi_text(draw, 940, ly+88, [
        "• C 语言实现的基于栈的虚拟机",
        "• 循环读取字节码指令，逐条执行",
        "• 操作数栈：LOAD_CONST 压栈 → BINARY_ADD 弹栈运算 → 压回结果",
        "• 函数调用时创建新栈帧 (Frame)，返回后销毁",
    ], FONT_SMALL, DARK, line_h=24)

    # GIL box
    rounded_box(draw, (920, ly+195, 1740, ly+338), WHITE, ACCENT2, 8)
    draw.text((940, ly+203), "⚠️ 全局解释器锁 (GIL)", fill=ACCENT2, font=FONT_H2)
    multi_text(draw, 940, ly+233, [
        "• 同一时刻只有一个线程执行 Python 字节码",
        "• 目的：简化 CPython 内存管理（引用计数）",
        "• 后果：CPU 密集型任务多线程无法利用多核",
        "• 对策：CPU密集型 → multiprocessing 多进程",
    ], FONT_SMALL, DARK, line_h=24)

    # ── 底部：语言对比 ──
    by = 615
    draw.text((40, by), "⚔️ 执行模式对比", fill=DARK, font=FONT_H1)
    draw.rectangle([(40, by+38), (1760, by+42)], fill=GRAY2)
    cols = [
        ("Python", "先编译 → 字节码(.pyc)\nPVM 逐条解释执行\n平台无关，跨平台好\n速度适中", ACCENT1),
        ("Java", ".java → .class 字节码\nJVM + JIT 即时编译\n平台无关，跨平台好\n速度较快（JIT 优化）", ACCENT3),
        ("C/C++", "源码 → 机器码(.exe)\nCPU 直接执行\n平台相关，需重编译\n速度最快", ACCENT2),
    ]
    for i, (name, desc, color) in enumerate(cols):
        cx = 40 + i * 580
        rounded_box(draw, (cx, by+52, cx+550, by+175), color, radius=12)
        draw.text((cx+15, by+58), name, fill=WHITE, font=FONT_H2)
        multi_text(draw, cx+15, by+90, desc.split("\n"), FONT_SMALL, WHITE, line_h=24)

    # 页脚
    draw.text((W//2 - 100, H-30), "PY001 Python 简介 · 概念图 2/4", fill=GRAY3, font=FONT_TINY)

    img.save(f"{OUTPUT_DIR}/PY001-概念图2-代码执行过程.png")
    print("✅ 图2: 代码执行过程")

# ═══════════════════════════════════════════════════════
# 图3：Python 类型系统定位
# ═══════════════════════════════════════════════════════
def img3_typesystem():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_title_bar(draw, "PY001 Python 类型系统定位", "Python 是动态强类型 — 一次说清「动静」与「强弱」")

    # ── 四象限核心图 ──
    qx, qy, qw, qh = 60, 110, 830, 620

    # 坐标轴
    draw.line([(qx + qw//2, qy), (qx + qw//2, qy+qh)], fill=GRAY3, width=2)  # 竖轴
    draw.line([(qx, qy + qh//2), (qx+qw, qy+qh//2)], fill=GRAY3, width=2)    # 横轴

    # 轴标签
    draw.text((qx + qw//2 - 70, qy-25), "强类型 ↑", fill=GRAY3, font=FONT_H2)
    draw.text((qx + qw//2 - 70, qy+qh+5), "弱类型 ↓", fill=GRAY3, font=FONT_H2)
    draw.text((qx-85, qy+qh//2-12), "← 静态", fill=GRAY3, font=FONT_H2)
    draw.text((qx+qw-30, qy+qh//2-12), "动态 →", fill=GRAY3, font=FONT_H2)

    # 四象限标签
    quads = [
        (qx+10, qy+10, "静态 + 强", "Java, C++, Rust", ACCENT3),
        (qx+qw//2+10, qy+10, "动态 + 强", "Python, Ruby", ACCENT1),
        (qx+10, qy+qh//2+10, "静态 + 弱", "C (void* 可强转)", ACCENT4),
        (qx+qw//2+10, qy+qh//2+10, "动态 + 弱", "JavaScript, PHP", ACCENT2),
    ]
    for qxx, qyy, label1, label2, color in quads:
        rounded_box(draw, (qxx, qyy, qxx+395, qyy+295), color, radius=12)
        draw.text((qxx+18, qyy+15), f"📌 {label1}", fill=WHITE, font=FONT_H2)
        draw.text((qxx+18, qyy+55), label2, fill=WHITE, font=FONT_SMALL)

    # Python 高亮标记
    py_x, py_y = qx+qw//2+10, qy+10
    draw.ellipse([(py_x+280, py_y+180), (py_x+360, py_y+260)], fill=WHITE)
    draw.text((py_x+292, py_y+198), "⭐\nPython", fill=ACCENT1, font=FONT_TINY)

    # ── 右栏：概念解释 ──
    rx = 920
    # 动态 vs 静态
    rounded_box(draw, (rx, 110, 1760, 580), GRAY1, GRAY2, 12)
    draw.text((rx+20, 118), "📖 两个独立维度的解释", fill=DARK, font=FONT_H1)

    concepts = [
        ("🔹 类型检查时机（横轴）", [
            "静态类型：编译时确定类型，变量声明后类型不可变",
            "  Java: int x = 10;  // x 永远是 int",
            "动态类型：运行时确定类型，变量只是「标签」可随时贴到不同对象",
            "  Python: x = 10; x = \"hello\"  # 完全合法",
        ], ACCENT1),
        ("🔸 类型转换严格度（纵轴）", [
            "强类型：严禁隐式类型转换，不同类型操作直接报错",
            "  Python: \"5\" + 2 → TypeError ❌",
            "弱类型：自动隐式类型转换（类型强制）",
            "  JavaScript: \"5\" + 2 → \"52\" ⚠️",
        ], ACCENT4),
    ]
    cy = 162
    for title, lines, color in concepts:
        draw.text((rx+20, cy), title, fill=color, font=FONT_H2)
        multi_text(draw, rx+20, cy+32, lines, FONT_SMALL, DARK, line_h=22)
        cy += 32 + len(lines)*22 + 20

    # ── 关键认知 ──
    draw.text((rx+20, 455), "🎯 关键认知", fill=ACCENT2, font=FONT_H2)
    multi_text(draw, rx+20, 485, [
        "\"不需要声明类型\" = 动态类型 ✓ ≠ 弱类型 ✗",
        "Python = 动态 + 强 — 灵活但不放纵",
    ], FONT_BODY, DARK, line_h=28)

    # ── 底部：变量模型 ──
    by2 = 745
    rounded_box(draw, (60, by2, 870, by2+120), ACCENT1, radius=12)
    draw.text((80, by2+10), "🏷️ Python 变量模型：标签 (Tag)", fill=WHITE, font=FONT_H2)
    multi_text(draw, 80, by2+42, [
        "变量 = 贴在对象上的标签，不是存储数据的盒子",
        "x = [1,2,3]; y = x  →  x 和 y 指向同一个列表对象",
    ], FONT_SMALL, WHITE, line_h=22)

    rounded_box(draw, (910, by2, 1760, by2+120), TITLE_BG, radius=12)
    draw.text((930, by2+10), "📦 C/Java 变量模型：盒子 (Box)", fill=WHITE, font=FONT_H2)
    multi_text(draw, 930, by2+42, [
        "变量 = 内存中的固定盒子，存入数据时必须符合盒子大小",
        "int x = 10; x = \"hello\"  → 编译错误 ❌",
    ], FONT_SMALL, WHITE, line_h=22)

    draw.text((W//2 - 100, H-30), "PY001 Python 简介 · 概念图 3/4", fill=GRAY3, font=FONT_TINY)
    img.save(f"{OUTPUT_DIR}/PY001-概念图3-类型系统定位.png")
    print("✅ 图3: 类型系统定位")

# ═══════════════════════════════════════════════════════
# 图4：常见误区与总结
# ═══════════════════════════════════════════════════════
def img4_misconceptions():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_title_bar(draw, "PY001 常见误区与核心总结", "避开这些坑，建立正确的 Python 认知")

    # ── 四大误区 ──
    myths = [
        ("❌ 误区 1", "\"变量不需要声明类型\n→ 所以是弱类型\"",
         "✅ 事实", "不需要声明类型 = 动态类型 ≠ 弱类型。\nPython 是强类型：\"5\" + 2 → TypeError",
         ACCENT2, ACCENT3),
        ("❌ 误区 2", "\"Python 是纯解释型\n代码一行一行执行\"",
         "✅ 事实", "Python = 编译 + 解释。源码先编译为字节码(.pyc)\n再由 PVM 逐条解释执行。",
         ACCENT2, ACCENT3),
        ("❌ 误区 3", "\"GIL 让 Python\n完全用不了多核\"",
         "✅ 事实", "GIL 只影响 CPU 密集型多线程。\nIO密集型多线程有效，CPU密集型用 multiprocessing。",
         ACCENT2, ACCENT3),
        ("❌ 误区 4", "\"Python 太慢\n不适合严肃项目\"",
         "✅ 事实", "开发效率 > 执行效率是合理的权衡。\n瓶颈可用 C 扩展/PyPy 解决；AI/数据科学生态无可替代。",
         ACCENT2, ACCENT3),
    ]
    for i, (myth_label, myth_text, fact_label, fact_text, myth_color, fact_color) in enumerate(myths):
        cx = 40 + i * 440
        # 误区卡片
        rounded_box(draw, (cx, 105, cx+410, 300), myth_color, radius=12)
        draw.text((cx+15, 115), myth_label, fill=WHITE, font=FONT_H2)
        multi_text(draw, cx+15, 155, myth_text.split("\n"), FONT_SMALL, WHITE, line_h=26)

        # 箭头
        arrow_down(draw, cx+200, 310, 340, GRAY3, 3)

        # 事实卡片
        rounded_box(draw, (cx, 350, cx+410, 540), fact_color, radius=12)
        draw.text((cx+15, 360), fact_label, fill=WHITE, font=FONT_H2)
        multi_text(draw, cx+15, 400, fact_text.split("\n"), FONT_SMALL, WHITE, line_h=26)

    # ── 核心总结 ──
    rounded_box(draw, (40, 570, 1760, 740), TITLE_BG, radius=14)
    draw.text((60, 585), "🎓 PY001 核心要点总结", fill=ACCENT4, font=FONT_H1)

    summary_items = [
        ("📜 历史", "Guido van Rossum · 1989圣诞 · 继承ABC · Monty Python命名"),
        ("🧘 哲学", "Python之禅 19条格言 · import this · 优美/明确/简单/可读"),
        ("⚙️ 执行", "源码 → Token → AST → 字节码(.pyc) → PVM解释 → OS执行"),
        ("🔒 GIL", "全局解释器锁 · 单线程执行字节码 · CPU密集型用多进程"),
        ("🏷️ 类型", "动态强类型 · 变量=标签 · 动静×强弱是独立维度"),
        ("🔄 对比", "vs C/C++: 字节码中间层 · vs Java: 相似的编译+解释路线"),
    ]
    for i, (icon, text) in enumerate(summary_items):
        col = i % 3
        row = i // 3
        sx = 60 + col * 570
        sy = 625 + row * 55
        draw.text((sx, sy), f"{icon}  {text}", fill=WHITE, font=FONT_SMALL)

    # 页脚
    draw.text((W//2 - 100, H-30), "PY001 Python 简介 · 概念图 4/4", fill=GRAY3, font=FONT_TINY)
    img.save(f"{OUTPUT_DIR}/PY001-概念图4-常见误区与总结.png")
    print("✅ 图4: 常见误区与总结")

# ═══════════════════════════════════════════════════════
if __name__ == "__main__":
    img1_history()
    img2_execution()
    img3_typesystem()
    img4_misconceptions()
    print(f"\n🎉 全部完成！4张概念图已保存到:\n   {OUTPUT_DIR}/")
