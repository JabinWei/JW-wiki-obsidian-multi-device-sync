#!/usr/bin/env python3
"""
PY001 卡通概念图 - 漫画风格
使用渐变色彩、卡通角色、对话框、漫画面板
"""

from PIL import Image, ImageDraw, ImageFont
import math, random, os

OUTPUT_DIR = "/Users/weijibin/Documents/obsidian-notes/90-Storage/98-Asset-资源"
W, H = 1800, 1005
random.seed(42)

# ── 字体 ──
def load_font(size):
    paths = ["/System/Library/Fonts/PingFang.ttc",
             "/System/Library/Fonts/Hiragino Sans GB.ttc",
             "/Library/Fonts/Arial Unicode.ttf"]
    for p in paths:
        try: return ImageFont.truetype(p, size)
        except: pass
    return ImageFont.load_default()

FONT_BIG   = load_font(44)
FONT_H1    = load_font(30)
FONT_H2    = load_font(22)
FONT_BODY  = load_font(17)
FONT_SMALL = load_font(14)

# ── 配色方案（明亮卡通色） ──
BG_WARM   = (255, 252, 245)
C_NAVY    = (35, 45, 75)
C_RED     = (235, 75, 65)
C_ORANGE  = (250, 150, 40)
C_YELLOW  = (255, 210, 60)
C_GREEN   = (65, 185, 115)
C_BLUE    = (55, 130, 225)
C_PURPLE  = (145, 95, 220)
C_PINK    = (240, 110, 150)
C_WHITE   = (255, 255, 255)
C_DARK    = (40, 40, 55)
C_LIGHT   = (245, 245, 248)
C_GRAY    = (150, 155, 165)

def gradient_bg(draw, top_color, bottom_color):
    """垂直渐变背景"""
    for y in range(H):
        r = int(top_color[0] + (bottom_color[0]-top_color[0]) * y/H)
        g = int(top_color[1] + (bottom_color[1]-top_color[1]) * y/H)
        b = int(top_color[2] + (bottom_color[2]-top_color[2]) * y/H)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

def round_rect(draw, xy, fill, outline=None, radius=20):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline or fill, width=3)

def round_rect_gradient(draw, xy, color_top, color_bottom, radius=20):
    """带渐变的圆角矩形"""
    x1, y1, x2, y2 = xy
    # 先画底色
    draw.rounded_rectangle(xy, radius=radius, fill=color_top)
    # 叠加渐变
    for y in range(y1, y2):
        ratio = (y - y1) / (y2 - y1)
        r = int(color_top[0] + (color_bottom[0]-color_top[0]) * ratio)
        g = int(color_top[1] + (color_bottom[1]-color_top[1]) * ratio)
        b = int(color_top[2] + (color_bottom[2]-color_top[2]) * ratio)
        left = x1 + int(radius * (1 - min(1, (y-y1)/radius))) if y-y1 < radius else x1
        right = x2 - int(radius * (1 - min(1, (y-y1)/radius))) if y-y1 < radius else x2
        if y-y2 > -radius:
            left = max(left, x1)
        draw.line([(x1, y), (x2, y)], fill=(r, g, b))
    # 重新画圆角边框
    draw.rounded_rectangle(xy, radius=radius, fill=None, outline=color_bottom, width=3)

def speech_bubble(draw, x, y, w, h, color_bg, color_border, pointer_tip, pointer_dir="down"):
    """对话框气泡"""
    pad = 5
    round_rect(draw, (x, y, x+w, y+h), color_bg, color_border, radius=24)
    px, py = pointer_tip
    if pointer_dir == "down":
        pts = [(px-16, y+h-3), (px+16, y+h-3), (px, y+h+20)]
    elif pointer_dir == "up":
        pts = [(px-16, y+3), (px+16, y+3), (px, y-20)]
    draw.polygon(pts, fill=color_border)
    draw.polygon([(p[0]+(-2 if p[0]>px else 2 if p[0]<px else 0), p[1]+(-2)) for p in pts], fill=color_bg)

def text_center(draw, cx, y, text, font, color=C_DARK):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        tw = draw.textlength(line, font=font)
        draw.text((cx - tw//2, y + i*(font.size+4)), line, fill=color, font=font)

def draw_snake(draw, x, y, scale=1.0):
    """画一个可爱的卡通 Python 小蛇"""
    s = scale
    # 身体（绿色椭圆曲线）
    body_color = (75, 190, 120)
    dark_color = (40, 140, 75)
    eye_white = (255, 255, 255)
    eye_black = (30, 30, 30)
    tongue_color = C_RED

    # 身体 - 用椭圆模拟蛇的盘绕
    # 蛇身
    draw.ellipse((x-25*s, y-8*s, x+25*s, y+18*s), fill=body_color)
    draw.ellipse((x-20*s, y-14*s, x+10*s, y+10*s), fill=body_color)
    # 头部
    draw.ellipse((x+5*s, y-20*s, x+35*s, y+5*s), fill=body_color)
    # 亮色斑点
    draw.ellipse((x-10*s, y-2*s, x+2*s, y+10*s), fill=(120, 220, 155))
    draw.ellipse((x+8*s, y-12*s, x+20*s, y-3*s), fill=(120, 220, 155))
    # 眼睛
    draw.ellipse((x+18*s, y-18*s, x+26*s, y-12*s), fill=eye_white)
    draw.ellipse((x+21*s, y-17*s, x+24*s, y-14*s), fill=eye_black)
    # 微笑
    draw.arc((x+22*s, y-10*s, x+30*s, y), start=0, end=180, fill=dark_color, width=2)
    # 舌头
    draw.line([(x+32*s, y-2*s), (x+37*s, y), (x+33*s, y+3*s)], fill=tongue_color, width=2)

def panel_decor(draw, x, y, color):
    """小装饰点"""
    for dx, dy in [(0,0), (8,12), (-6,16), (14, -4)]:
        draw.ellipse((x+dx, y+dy, x+dx+4, y+dy+4), fill=color)

def big_emoji(draw, x, y, emoji, size=50):
    """画大号 emoji"""
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", size)
    except:
        font = load_font(size)
    draw.text((x, y), emoji, font=font, embedded_color=True)


def comic_header(draw, title, subtitle):
    """漫画风页眉"""
    gradient_bg(draw, C_NAVY, (55, 65, 100))
    # 装饰圆点
    for i in range(0, W, 60):
        draw.ellipse((i, 5, i+8, 13), fill=C_YELLOW)
    text_center(draw, W//2, 18, title, FONT_H1, C_WHITE)
    if subtitle:
        text_center(draw, W//2, 55, subtitle, FONT_SMALL, C_GRAY)
    # 底部波浪线
    for ix in range(0, W, 12):
        y_off = 76 + math.sin(ix/20)*4
        draw.ellipse((ix, y_off-5, ix+12, y_off+5), fill=C_YELLOW)

def comic_footer(draw, text):
    draw.rectangle([(0, H-35), (W, H)], fill=C_NAVY)
    text_center(draw, W//2, H-28, text, FONT_SMALL, C_GRAY)


# ══════════════════════════════════════════════════════
# 图1：Python 发展历史与哲学
# ══════════════════════════════════════════════════════
def img1():
    random.seed(42)
    img = Image.new("RGB", (W, H), BG_WARM)
    draw = ImageDraw.Draw(img)
    comic_header(draw, "🐍 PY001 Python 的诞生与发展", "1989年圣诞节，一个「私活」项目改变了编程世界")

    # ── 左上：起源故事（漫画面板） ──
    round_rect(draw, (30, 95, 750, 225), C_WHITE, C_BLUE, 20)
    draw.rectangle([(30, 95), (750, 125)], fill=C_BLUE)
    draw.text((150, 102), "🎄 缘起：一个圣诞节的'私活'", fill=C_WHITE, font=FONT_H2)

    # 小蛇
    draw_snake(draw, 80, 155, scale=0.9)

    multi_text = lambda x,y,lines,font,color: [draw.text((x, y+i*(font.size+8)), ln, fill=color, font=font) for i,ln in enumerate(lines)]

    multi_text(150, 140, [
        "• 1989 年圣诞节，Guido van Rossum",
        "  在阿姆斯特丹家中写了一个'私活'项目",
        "• 目标是：继承 ABC 语言的优雅，弥补其封闭的缺陷",
        "• 填补 C 语言和 Shell 脚本之间的空白",
        "• 名字来源于 Monty Python 喜剧团 🎭（不是蟒蛇！）",
    ], FONT_BODY, C_DARK)

    # ── 右上：Python 之禅 ──
    round_rect(draw, (810, 95, 1770, 225), C_WHITE, C_PURPLE, 20)
    draw.rectangle([(810, 95), (1770, 125)], fill=C_PURPLE)
    draw.text((950, 102), "🧘 Python 之禅 — 输入 import this 查看全部", fill=C_WHITE, font=FONT_H2)

    zen = [
        ("🌸", "优美胜于丑陋", "Beautiful > Ugly", C_PINK),
        ("💡", "明确胜于隐晦", "Explicit > Implicit", C_BLUE),
        ("✨", "简单胜于复杂", "Simple > Complex", C_GREEN),
        ("👀", "可读性很重要", "Readability counts", C_ORANGE),
    ]
    for i, (icon, cn, en, clr) in enumerate(zen):
        bx = 830 + i * 232
        round_rect(draw, (bx, 140, bx+215, 210), (clr[0], clr[1], clr[2], 30), clr, 14)
        big_emoji(draw, bx+75, 148, icon, 32)
        text_center(draw, bx+108, 178, cn, FONT_BODY, clr)
        text_center(draw, bx+108, 202, en, FONT_SMALL, C_GRAY)

    # ── 中：发展时间轴 ──
    round_rect(draw, (30, 340, 1770, 480), C_WHITE, C_GRAY, 20)
    draw.text((50, 350), "📅 Python 发展路线图", fill=C_DARK, font=FONT_H2)

    # 时间轴线
    ty = 410
    draw.line([(60, ty), (1740, ty)], fill=C_GRAY, width=4)
    for ix in range(60, 1750, 40):
        draw.ellipse((ix, ty-2, ix+6, ty+4), fill=C_YELLOW)

    timeline = [
        (100, "1989\n圣诞", "Guido\n启动项目", C_RED, "💻"),
        (280, "1991", "Python 0.9.0\n首次发布", C_ORANGE, "🚀"),
        (480, "1994", "1.0 版本\nlambda/map", C_YELLOW, "🔧"),
        (680, "2000", "2.0 版本\nGC+Unicode", C_GREEN, "🎉"),
        (880, "2004", "Python 之禅\nTim Peters", C_BLUE, "📜"),
        (1080,"2008", "3.0 版本\n重大升级", C_PURPLE, "⬆️"),
        (1300,"2010s", "AI/数据科学\n爆发增长", C_PINK, "📈"),
        (1500,"至今", "全球排名\nTop 1-3", C_RED, "👑"),
    ]
    for cx, label, desc, clr, emoji in timeline:
        # 节点
        draw.ellipse((cx-14, ty-14, cx+14, ty+14), fill=clr)
        draw.ellipse((cx-8, ty-8, cx+8, ty+8), fill=C_WHITE)
        # 标签
        text_center(draw, cx, ty+24, label, FONT_SMALL, clr)
        # 卡片
        bw, bh = 150, 45
        round_rect(draw, (cx-bw//2, ty+65, cx+bw//2, ty+65+bh), (clr[0],clr[1],clr[2],25), clr, 10)
        text_center(draw, cx, ty+73, emoji + " " + desc.split("\n")[0], FONT_SMALL, clr)

    # ── 名人名言 ──
    y3 = 480
    round_rect(draw, (50, 520, 1750, 600), C_NAVY, C_NAVY, 18)
    text_center(draw, W//2, 530, "💬 Guido van Rossum", FONT_H1, C_YELLOW)
    text_center(draw, W//2, 568, "「Python 是一门让程序员开心的语言」", FONT_BIG, C_WHITE)
    text_center(draw, W//2, 616, "Python = ABC 的优雅 + C 的开放性 + Monty Python 的趣味精神", FONT_BODY, C_GRAY)

    comic_footer(draw, "PY001 · 概念图 1/4 · Python 发展历史与哲学")
    img.save(f"{OUTPUT_DIR}/PY001-概念图1-发展历史与哲学.png")
    print("✅ 图1")

# ══════════════════════════════════════════════════════
# 图2：Python 代码执行过程
# ══════════════════════════════════════════════════════
def img2():
    random.seed(99)
    img = Image.new("RGB", (W, H), BG_WARM)
    draw = ImageDraw.Draw(img)
    comic_header(draw, "⚙️ PY001 Python 代码是如何执行的？", "从敲下 python my_script.py 到屏幕输出，一场精彩的魔术")

    multi_text = lambda x,y,lines,font,color: [draw.text((x, y+i*(font.size+8)), ln, fill=color, font=font) for i,ln in enumerate(lines)]

    # ── 主角：执行流水线 ──
    steps = [
        ("📄 源码\nmy_script.py", C_BLUE),
        ("🔍 词法分析\nToken 化", C_PURPLE),
        ("🌳 语法分析\n生成 AST", C_PURPLE),
        ("⚙️ 编译\n字节码 .pyc", C_GREEN),
        ("🖥️ PVM\n解释执行", C_ORANGE),
        ("💻 操作系统\n输出结果", C_RED),
    ]
    x_pos = 40
    fy = 100
    for i, (label, clr) in enumerate(steps):
        bw = 260
        round_rect(draw, (x_pos, fy, x_pos+bw, fy+90), clr, clr, 16)
        lines = label.split("\n")
        for j, ln in enumerate(lines):
            text_center(draw, x_pos+bw//2, fy+18+j*28, ln, FONT_BODY, C_WHITE)
        if i < len(steps) - 1:
            # 箭头
            ax = x_pos + bw + 5
            draw.line([(ax, fy+45), (ax+25, fy+45)], fill=C_GRAY, width=4)
            draw.polygon([(ax+30, fy+45), (ax+18, fy+38), (ax+18, fy+52)], fill=C_GRAY)
        x_pos += bw + 42

    # ── 左：编译三步骤 ──
    round_rect(draw, (30, 220, 880, 510), C_WHITE, C_BLUE, 20)
    draw.rectangle([(30, 220), (880, 256)], fill=C_BLUE)
    draw.text((220, 224), "🔬 编译阶段：了解 Python '暗中'做的事", fill=C_WHITE, font=FONT_H2)

    comp = [
        ("① 词法分析", "把源代码切成 Token： x=10 → [标识符x] [运算符=] [数字10]", "✂️"),
        ("② 语法分析", "检查语法，构建 AST 抽象语法树（代码的骨架结构）", "🌳"),
        ("③ 字节码生成", "AST 翻译成 .pyc 字节码（平台无关的中间语言）", "📦"),
    ]
    for i, (title, desc, icon) in enumerate(comp):
        sy = 268 + i*78
        round_rect(draw, (50, sy, 860, sy+65), (C_BLUE[0],C_BLUE[1],C_BLUE[2],18), C_BLUE, 12)
        draw.text((65, sy+8), f"{icon} {title}", fill=C_BLUE, font=FONT_H2)
        draw.text((65, sy+34), desc, fill=C_DARK, font=FONT_SMALL)

    # ── 右：PVM + GIL ──
    round_rect(draw, (930, 220, 1770, 510), C_WHITE, C_ORANGE, 20)
    draw.rectangle([(930, 220), (1770, 256)], fill=C_ORANGE)
    draw.text((1050, 224), "🖥️ PVM 虚拟机 + GIL 锁", fill=C_WHITE, font=FONT_H2)

    # PVM
    round_rect(draw, (950, 270, 1750, 370), (C_ORANGE[0],C_ORANGE[1],C_ORANGE[2],15), C_ORANGE, 14)
    draw_snake(draw, 990, 300, 0.8)
    multi_text(1060, 285, [
        "Python 虚拟机 (PVM) — C 语言写的基于栈的虚拟机",
        "像一个'简化版 CPU'，循环读取字节码并逐条执行",
        "LOAD_CONST 压栈 → BINARY_ADD 运算 → 结果弹栈",
    ], FONT_SMALL, C_DARK)

    # GIL
    round_rect(draw, (950, 385, 1750, 500), (C_RED[0],C_RED[1],C_RED[2],15), C_RED, 14)
    big_emoji(draw, 970, 395, "⚠️", 28)
    multi_text(1020, 395, [
        "全局解释器锁 (GIL)：同一时刻只有 1 个线程执行字节码",
        "原因：简化 CPython 内存管理（引用计数机制）",
        "后果：CPU密集任务多线程 = 无效  → 用 multiprocessing！",
    ], FONT_SMALL, C_DARK)

    # ── 底部对比 ──
    by = 756
    draw.text((40, by-30), "⚔️ Python vs Java vs C/C++ — 执行模式对比", fill=C_DARK, font=FONT_H2)
    comps = [
        ("🐍 Python", "编译→字节码 .pyc\nPVM 解释执行\n✅ 跨平台\n⚡ 速度适中", C_BLUE),
        ("☕ Java", ".java→.class 字节码\nJVM + JIT 编译\n✅ 跨平台\n⚡⚡ 速度较快", C_GREEN),
        ("⚙️ C/C++", "源码→机器码 .exe\nCPU 直接执行\n❌ 平台相关\n⚡⚡⚡ 速度最快", C_RED),
    ]
    for i, (name, desc, clr) in enumerate(comps):
        cx = 40 + i * 580
        round_rect(draw, (cx, by, cx+540, by+140), (clr[0],clr[1],clr[2],25), clr, 16)
        draw.text((cx+15, by+10), name, fill=C_WHITE, font=FONT_H2)
        multi_text(cx+15, by+42, desc.split("\n"), FONT_BODY, C_DARK)

    comic_footer(draw, "PY001 · 概念图 2/4 · Python 代码执行过程")
    img.save(f"{OUTPUT_DIR}/PY001-概念图2-代码执行过程.png")
    print("✅ 图2")

# ══════════════════════════════════════════════════════
# 图3：类型系统定位
# ══════════════════════════════════════════════════════
def img3():
    random.seed(77)
    img = Image.new("RGB", (W, H), BG_WARM)
    draw = ImageDraw.Draw(img)
    comic_header(draw, "🏷️ PY001 Python 类型系统：动态强类型", "「不需要声明类型」 ≠ 「弱类型」！一张图说清楚")

    multi_text = lambda x,y,lines,font,color: [draw.text((x, y+i*(font.size+8)), ln, fill=color, font=font) for i,ln in enumerate(lines)]

    # ── 四象限 ──
    qx, qy, qw, qh = 30, 95, 740, 700
    # 轴
    draw.line([(qx+qw//2, qy-10), (qx+qw//2, qy+qh+20)], fill=C_GRAY, width=3)
    draw.line([(qx-10, qy+qh//2), (qx+qw+20, qy+qh//2)], fill=C_GRAY, width=3)
    # 轴标签
    text_center(draw, qx+qw//2, qy-40, "强类型 ↑", FONT_H2, C_GRAY)
    text_center(draw, qx+qw//2, qy+qh+30, "弱类型 ↓", FONT_H2, C_GRAY)
    text_center(draw, qx-85, qy+qh//2-12, "← 静态", FONT_H2, C_GRAY)
    text_center(draw, qx+qw+85, qy+qh//2-12, "动态 →", FONT_H2, C_GRAY)

    quads = [
        (qx+8, qy+8, "静态强类型", "Java, C++, Rust\n编译时检查，严禁隐转", C_BLUE),
        (qx+qw//2+8, qy+8, "⭐ 动态强类型", "Python, Ruby\n无需声明，绝不偷转\n开发效率高！", C_GREEN),
        (qx+8, qy+qh//2+8, "静态弱类型", "C (void* 可强转)\n有检查但隐式转换多", C_ORANGE),
        (qx+qw//2+8, qy+qh//2+8, "动态弱类型", "JavaScript, PHP\n极其灵活，容易埋坑", C_RED),
    ]
    for qxx, qyy, label1, label2, clr in quads:
        round_rect(draw, (qxx, qyy, qxx+355, qyy+340), (clr[0],clr[1],clr[2],25), clr, 14)
        draw.text((qxx+15, qyy+10), label1, fill=clr, font=FONT_H2)
        multi_text(qxx+15, qyy+50, label2.split("\n"), FONT_SMALL, C_DARK)

    # 高亮 Python
    px, py = qx+qw//2+8, qy+8
    big_emoji(draw, px+290, py+240, "🐍", 36)
    draw_snake(draw, px+320, py+300, 0.7)

    # ── 右栏：解释 ──
    rx = 800
    round_rect(draw, (rx, 95, 1770, 700), C_WHITE, C_GRAY, 20)

    # 静态 vs 动态
    round_rect(draw, (rx+15, 108, 925, 260), (C_BLUE[0],C_BLUE[1],C_BLUE[2],15), C_BLUE, 14)
    draw.text((rx+30, 115), "📖 类型检查时机：静态 vs 动态", fill=C_BLUE, font=FONT_H2)
    draw.text((rx+30, 148), "静态：编译时检查，类型声明后不可变", fill=C_DARK, font=FONT_BODY)
    draw.text((rx+30, 175), "  Java:  int x = 10; 之后 x 只能存整数", fill=C_GRAY, font=FONT_SMALL)
    draw.text((rx+30, 208), "动态：运行时检查，变量 = 可以贴到任何对象的标签", fill=C_DARK, font=FONT_BODY)
    draw.text((rx+30, 235), "  Python:  x = 10; x = \"hello\"  完全 OK！", fill=C_GRAY, font=FONT_SMALL)

    # 强 vs 弱
    round_rect(draw, (rx+15, 285, 925, 260), (C_GREEN[0],C_GREEN[1],C_GREEN[2],15), C_GREEN, 14)

    # 强 vs 弱
    round_rect(draw, (rx+15, 378, 925, 520), (C_GREEN[0],C_GREEN[1],C_GREEN[2],15), C_GREEN, 14)
    draw.text((rx+30, 388), "📖 类型转换严格度：强 vs 弱", fill=C_GREEN, font=FONT_H2)
    draw.text((rx+30, 420), "强类型：严禁隐式转换，不同类型操作直接报错", fill=C_DARK, font=FONT_BODY)
    draw.text((rx+30, 450), "  Python:  \"5\" + 2  →  TypeError ❌", fill=C_GRAY, font=FONT_SMALL)
    draw.text((rx+30, 480), "弱类型：自动隐式类型转换（类型强制）", fill=C_DARK, font=FONT_BODY)
    draw.text((rx+30, 508), "  JavaScript:  \"5\" + 2  →  \"52\" 😱", fill=C_GRAY, font=FONT_SMALL)

    # 金句
    round_rect(draw, (rx+15, 530, 955, 620), C_NAVY, C_NAVY, 14)
    draw.text((rx+35, 542), "🎯 一句话记住", fill=C_YELLOW, font=FONT_H1)
    draw.text((rx+35, 580), "「不需要声明类型」 = 动态类型 ✓  ≠  弱类型 ✗", fill=C_WHITE, font=FONT_H2)
    draw.text((rx+35, 615), "Python = 动态 + 强 — 灵活但不放纵！", fill=C_GRAY, font=FONT_BODY)

    # ── 底部：标签 vs 盒子 ──
    by = 816
    round_rect(draw, (30, by, 880, by+100), (C_BLUE[0],C_BLUE[1],C_BLUE[2],25), C_BLUE, 14)
    draw.text((50, by+10), "🏷️ Python 标签模型", fill=C_WHITE, font=FONT_H2)
    draw.text((50, by+42), "变量 = 贴在对象上的标签，可随时贴到不同的对象上", fill=C_DARK, font=FONT_SMALL)
    draw.text((50, by+68), "x = [1,2,3]; y = x  → x 和 y 都是同一个列表的标签", fill=C_GRAY, font=FONT_SMALL)

    round_rect(draw, (920, by, 1770, by+100), (C_RED[0],C_RED[1],C_RED[2],25), C_RED, 14)
    draw.text((940, by+10), "📦 C/Java 盒子模型", fill=C_WHITE, font=FONT_H2)
    draw.text((940, by+42), "变量 = 内存中的固定盒子，存入数据必须符合盒子的大小", fill=C_DARK, font=FONT_SMALL)
    draw.text((940, by+68), "int x = 10; x = \"hello\";  → 编译错误！类型不匹配 ❌", fill=C_GRAY, font=FONT_SMALL)

    comic_footer(draw, "PY001 · 概念图 3/4 · Python 类型系统定位")
    img.save(f"{OUTPUT_DIR}/PY001-概念图3-类型系统定位.png")
    print("✅ 图3")

# ══════════════════════════════════════════════════════
# 图4：常见误区与总结
# ══════════════════════════════════════════════════════
def img4():
    random.seed(123)
    img = Image.new("RGB", (W, H), BG_WARM)
    draw = ImageDraw.Draw(img)
    comic_header(draw, "🚫 PY001 常见误区 & 核心总结", "四个最常见的新手误区，一次全部纠正！")

    multi_text = lambda x,y,lines,font,color: [draw.text((x, y+i*(font.size+8)), ln, fill=color, font=font) for i,ln in enumerate(lines)]

    # ── 四大误区 ──
    myths = [
        ("❌ 误区 1", "\"变量不需要声明类型\n所以是弱类型\"",
         "✅ 真相", "不需要声明 = 动态类型\nPython 是强类型: \"5\"+2 → Error!", C_RED, C_GREEN),
        ("❌ 误区 2", "\"Python 是纯解释型\n一行一行执行\"",
         "✅ 真相", "先编译成 .pyc 字节码\n再由 PVM 解释执行", C_RED, C_GREEN),
        ("❌ 误区 3", "\"GIL 让 Python\n完全用不了多核\"",
         "✅ 真相", "仅影响 CPU 密集多线程\nIO密集用线程，CPU用进程", C_RED, C_GREEN),
        ("❌ 误区 4", "\"Python 太慢\n不适合严肃项目\"",
         "✅ 真相", "开发效率 > 执行效率\n瓶颈用 C扩展/PyPy 解决", C_RED, C_GREEN),
    ]
    for i, (myth_label, myth_text, fact_label, fact_text, myth_c, fact_c) in enumerate(myths):
        cx = 30 + i * 440
        # 误区
        round_rect(draw, (cx, 95, cx+420, 200), (myth_c[0],myth_c[1],myth_c[2],30), myth_c, 16)
        draw_snake(draw, cx+330, 130, 0.5)
        draw.text((cx+15, 102), myth_label, fill=C_WHITE, font=FONT_H2)
        multi_text(cx+15, 140, myth_text.split("\n"), FONT_SMALL, C_DARK)

        # 向下大箭头
        ax = cx + 210
        draw.line([(ax, 208), (ax, 245)], fill=myth_c, width=5)
        draw.polygon([(ax, 255), (ax-12, 242), (ax+12, 242)], fill=myth_c)

        # 真相
        round_rect(draw, (cx, 262, cx+420, 520), (fact_c[0],fact_c[1],fact_c[2],25), fact_c, 16)
        big_emoji(draw, cx+15, 270, "✅", 28)
        draw.text((cx+55, 272), fact_label, fill=C_WHITE, font=FONT_H2)
        multi_text(cx+15, 310, fact_text.split("\n"), FONT_SMALL, C_DARK)

    # ── 核心总结 ──
    round_rect(draw, (30, 540, 1770, 730), C_NAVY, C_NAVY, 20)
    text_center(draw, W//2, 555, "🎓 PY001 核心知识点清单", FONT_H1, C_YELLOW)

    summary = [
        ("📜 历史", "Guido · 1989圣诞 · ABC · Monty Python"),
        ("🧘 哲学", "Python 之禅 · 19条格言 · import this"),
        ("⚙️ 执行", "源码→Token→AST→.pyc→PVM→OS"),
        ("🔒 GIL", "单线程执行 · CPU密集用多进程"),
        ("🏷️ 类型", "动态强类型 · 变量=标签"),
        ("🔄 对比", "vs C 机器码 · vs Java JIT"),
    ]
    for i, (icon, text) in enumerate(summary):
        col = i % 3
        row = i // 3
        sx = 55 + col * 570
        sy = 600 + row * 55
        round_rect(draw, (sx, sy, sx+540, sy+42), (255,255,255,20), C_WHITE, 10)
        draw.text((sx+12, sy+6), f"{icon}  {text}", fill=C_DARK, font=FONT_SMALL)

    comic_footer(draw, "PY001 · 概念图 4/4 · 常见误区与总结")
    img.save(f"{OUTPUT_DIR}/PY001-概念图4-常见误区与总结.png")
    print("✅ 图4")


if __name__ == "__main__":
    import sys
    if "--all" in sys.argv:
        img1(); img2(); img3(); img4()
        print(f"\n🎉 全部 4 张卡通概念图已保存到 {OUTPUT_DIR}/")
    else:
        print("🎨 生成范例...")
        img1()
        print(f"\n👉 范例: {OUTPUT_DIR}/PY001-概念图1-发展历史与哲学.png")
        print("   满意后运行: python3 gen_py001_cartoon.py --all")
