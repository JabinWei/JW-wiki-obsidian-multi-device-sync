#!/usr/bin/env python3
"""Generate Excalidraw four-quadrant diagram for Python type system"""
import json, gzip, base64, sys

elements = []
next_id = 0
def uid():
    global next_id
    next_id += 1
    return f"elem{next_id:04d}"

# Colors
RED_BG = "#fff0f0"
RED_STROKE = "#e03131"
ORANGE_BG = "#fff9db"
ORANGE_STROKE = "#f08c00"
BLUE_BG = "#e7f5ff"
BLUE_STROKE = "#1971c2"
GREEN_BG = "#d3f9d8"
GREEN_STROKE = "#2f9e44"
DARK = "#1e1e1e"
GRAY = "#868e96"
WHITE = "#ffffff"

def rect(x, y, w, h, bg, stroke, roundness=None):
    el = {"type":"rectangle","id":uid(),"x":x,"y":y,"width":w,"height":h,
          "strokeColor":stroke,"backgroundColor":bg,"fillStyle":"solid",
          "strokeWidth":2,"roughness":0,"opacity":100,"groupIds":[],
          "strokeSharpness":"sharp","seed":1234,"version":1,"isDeleted":False,
          "boundElements":[],"updated":1718123456789,"link":"","locked":False}
    if roundness:
        el["roundness"] = {"type": 3}
    else:
        el["roundness"] = {"type": 1}
    return el

def arrow(x, y, points, stroke=DARK, sw=2):
    return {"type":"arrow","id":uid(),"x":x,"y":y,
            "points":points,"strokeColor":stroke,"strokeWidth":sw,
            "roughness":0,"opacity":100,"groupIds":[],
            "strokeSharpness":"round","seed":1234,"version":1,"isDeleted":False,
            "boundElements":[],"updated":1718123456789,"link":"",
            "locked":False,"startBinding":None,"endBinding":None,
            "startArrowhead":None,"endArrowhead":"arrow","roundness":{"type":2}}

def text(x, y, w, h, txt, fs=20, ff=1, ta="center", va="middle", color=DARK):
    return {"type":"text","id":uid(),"x":x,"y":y,"width":w,"height":h,
            "text":txt,"fontSize":fs,"fontFamily":ff,"textAlign":ta,
            "verticalAlign":va,"containerId":None,"originalText":txt,
            "autoResize":True,"lineHeight":1.25,"strokeColor":color,
            "backgroundColor":"transparent","fillStyle":"solid",
            "strokeWidth":1,"roughness":0,"opacity":100,"groupIds":[],
            "strokeSharpness":"sharp","seed":1234,"version":1,"isDeleted":False,
            "boundElements":[],"updated":1718123456789,"link":"","locked":False}

# ===================== BUILD DIAGRAM =====================

# Title
elements.append(text(350, 15, 500, 45, "编程语言类型系统 · 四大象限", fs=28, ff=1))

# Quadrant backgrounds
elements.append(rect(95, 75, 480, 295, RED_BG, RED_STROKE))
elements.append(rect(625, 75, 480, 295, ORANGE_BG, ORANGE_STROKE))
elements.append(rect(95, 435, 480, 320, BLUE_BG, BLUE_STROKE))
elements.append(rect(625, 435, 480, 320, GREEN_BG, GREEN_STROKE))

# Axes
elements.append(arrow(80, 400, [[0,0], [1050,0]]))
elements.append(arrow(600, 50, [[0,0], [0,720]]))

# Axis labels
elements.append(text(40, 405, 120, 30, "静  态", fs=22, ff=1, ta="left"))
elements.append(text(50, 432, 140, 24, "（编译时检查）", fs=14, ff=1, ta="left", color=GRAY))
elements.append(text(1060, 405, 120, 30, "动  态", fs=22, ff=1, ta="right"))
elements.append(text(1050, 432, 140, 24, "（运行时检查）", fs=14, ff=1, ta="right", color=GRAY))

elements.append(text(625, 53, 150, 30, "弱类型", fs=22, ff=1, ta="center"))
elements.append(text(625, 80, 180, 24, "（允许隐式转换）", fs=14, ff=1, ta="center", color=GRAY))
elements.append(text(625, 753, 150, 30, "强类型", fs=22, ff=1, ta="center"))
elements.append(text(625, 780, 180, 24, "（严禁隐式转换）", fs=14, ff=1, ta="center", color=GRAY))

# Quadrant 1: Static + Weak (TL)
elements.append(text(335, 120, 200, 35, "静态弱类型", fs=22, ff=1, color=RED_STROKE))
elements.append(text(335, 170, 300, 40, "C  /  C++", fs=26, ff=1))
elements.append(text(335, 230, 400, 80, "系统编程的基石\n赋予程序员极大的权限直接操作内存\n自然隐式转换多，「能力越大，责任越大」", fs=14, ff=1, color=GRAY))

# Quadrant 2: Dynamic + Weak (TR)
elements.append(text(865, 120, 200, 35, "动态弱类型", fs=22, ff=1, color=ORANGE_STROKE))
elements.append(text(865, 170, 400, 40, "JavaScript / PHP / Perl", fs=26, ff=1))
elements.append(text(865, 230, 400, 80, "Web 开发的早期功臣\n代码极其灵活，上手极快\n隐式类型转换容易埋坑，催生了 TypeScript", fs=14, ff=1, color=GRAY))

# Quadrant 3: Static + Strong (BL)
elements.append(text(335, 480, 200, 35, "静态强类型", fs=22, ff=1, color=BLUE_STROKE))
elements.append(text(335, 530, 400, 40, "Java / C# / Go / Rust", fs=26, ff=1))
elements.append(text(335, 590, 400, 80, "企业级开发的最爱\n必须先声明类型，编译时就能拦住绝大部分错误\n代码运行效率高，维护省心", fs=14, ff=1, color=GRAY))

# Quadrant 4: Dynamic + Strong (BR) - Python highlighted!
elements.append(text(865, 480, 200, 35, "动态强类型 ⭐", fs=22, ff=1, color=GREEN_STROKE))
elements.append(text(865, 530, 400, 40, "Python  /  Ruby", fs=26, ff=1))
elements.append(text(865, 590, 400, 80, "灵活的「实干派」—— Python 在此！\n无需声明类型，写代码飞快\n运算时极讲原则，严禁偷偷转换类型", fs=14, ff=1, color=GRAY))

# Arrow labels on axes
elements.append(text(350, 390, 30, 20, "←", fs=20, ff=1, color=GRAY))
elements.append(text(850, 390, 30, 20, "→", fs=20, ff=1, color=GRAY))
elements.append(text(590, 230, 30, 20, "↑", fs=20, ff=1, color=GRAY))
elements.append(text(590, 550, 30, 20, "↓", fs=20, ff=1, color=GRAY))

# Corner note
elements.append(text(600, 40, 200, 20, "类型检查时机 →", fs=14, ff=1, color=GRAY))
elements.append(text(568, 400, 30, 200, "类\n型\n转\n换\n严\n格\n度", fs=14, ff=1, ta="center", color=GRAY))

# Python confidence marker in quadrant 4
elements.append(text(865, 660, 400, 55, "✅ 开发效率高  ✅ 逻辑 Bug 少\n❌ 不偷偷做类型转换", fs=15, ff=1, color="#2f9e44"))

# Build final JSON
drawing = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "gridSize": None,
        "viewBackgroundColor": "#ffffff"
    },
    "files": {}
}

json_str = json.dumps(drawing, ensure_ascii=False, separators=(',', ':'))

# Gzip compress then base64 encode
compressed = base64.b64encode(gzip.compress(json_str.encode('utf-8'))).decode('ascii')

# Fold to 80-char lines
lines = [compressed[i:i+80] for i in range(0, len(compressed), 80)]
print('\n'.join(lines))
