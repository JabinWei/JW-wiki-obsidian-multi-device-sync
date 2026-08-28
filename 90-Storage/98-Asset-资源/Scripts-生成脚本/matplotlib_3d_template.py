import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
for f in ["/System/Library/Fonts/PingFang.ttc", "/System/Library/Fonts/STHeiti Medium.ttc"]:
    try:
        font_manager.fontManager.addfont(f)
    except Exception:
        pass
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

matplotlib.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC"]
matplotlib.rcParams["axes.unicode_minus"] = False

O = np.array([0.0, 0.0, 0.0])
a1 = np.array([2, -1, 0])      # 列1
a2 = np.array([1, 2, -1])      # 列2
a3 = np.array([0, 1, 2])       # 列3
b  = np.array([1, 0, 1])       # 结果
s1 = 0.5 * a1                  # (1, -0.5, 0)
s3 = 0.5 * a3                  # (0, 0.5, 1)
path_end = s1 + s3             # (1, 0, 1) = b

lo, hi = -2.0, 3.0
fig = plt.figure(figsize=(7.2, 7.2), dpi=200)
ax = fig.add_subplot(111, projection="3d")

# --- 画一个带箭头的向量 ---
def vec_arrow(ax, start, end, color, lw=3.0, ls="-", alpha=1.0, zorder=4):
    ax.plot3D(*zip(start, end), color=color, linewidth=lw, linestyle=ls, alpha=alpha, zorder=zorder)
    d = end - start
    n = np.linalg.norm(d)
    if n < 1e-9:
        return
    # 箭头头部：在端点处画一个小三角锥（用三根短线近似）
    head_scale = 0.10
    h = head_scale
    # 构造垂直方向
    e = d / n
    ref = np.array([1,0,0]) if abs(e[0]) < 0.9 else np.array([0,1,0])
    u1 = np.cross(e, ref); u1 = u1 / np.linalg.norm(u1)
    u2 = np.cross(e, u1)
    base = end - h * e
    r = 0.09
    tips = [base + r * (u1 + u2*np.sqrt(3))/2*np.sqrt(2) for _ in range(1)]
    # 简化：箭头头用三个小线段形成锥体
    p1 = base + r * np.cos(0.0) * u1 + r * np.sin(0.0) * u2
    p2 = base + r * np.cos(2.0944) * u1 + r * np.sin(2.0944) * u2
    p3 = base + r * np.cos(4.1888) * u1 + r * np.sin(4.1888) * u2
    for p in (p1, p2, p3):
        ax.plot3D(*zip(p, end), color=color, linewidth=lw, zorder=zorder)

# --- 坐标轴（从原点出发的三条轴，末端带箭头；负半轴浅灰虚线，方便定位原点） ---
for axis, (vec, label) in enumerate([(np.array([3.2,0,0]),"X"), (np.array([0,3.2,0]),"Y"), (np.array([0,0,3.2]),"Z")]):
    ax.plot3D(*zip(O, vec), color="#444444", linewidth=1.8, zorder=2)
    # 轴末端箭头（用稍小锥体表示方向）
    d = vec
    e = d / np.linalg.norm(d)
    ref = np.array([1,0,0]) if abs(e[0]) < 0.9 else np.array([0,1,0])
    u1 = np.cross(e, ref); u1 = u1 / np.linalg.norm(u1)
    u2 = np.cross(e, u1)
    r = 0.10
    base = vec - 0.22 * e
    p1 = base + r * np.cos(0.0) * u1 + r * np.sin(0.0) * u2
    p2 = base + r * np.cos(2.0944) * u1 + r * np.sin(2.0944) * u2
    p3 = base + r * np.cos(4.1888) * u1 + r * np.sin(4.1888) * u2
    for p in (p1, p2, p3):
        ax.plot3D(*zip(p, vec), color="#444444", linewidth=1.8, zorder=2)
    ax.text(*(vec + np.array([0.15,0.1,0.05])), label, fontsize=13, fontweight="bold", color="#333333", zorder=6)
    neg = np.array([-1.4, 0, 0]) if axis == 0 else (np.array([0, -1.4, 0]) if axis == 1 else np.array([0, 0, -1.4]))
    ax.plot3D(*zip(O, neg), color="#c0c0c0", linewidth=1.2, linestyle="--", zorder=1)

# 原始列向量：灰色细虚线（从原点出发）
for v in (a1, a2, a3):
    vec_arrow(ax, O, v, "#9e9e9e", lw=1.6, ls="--", alpha=0.9, zorder=3)

# 缩放路径（首尾相接）：½a₁ 蓝、½a₃ 绿，加图例
vec_arrow(ax, O, s1, "#1f77b4", lw=3.5, zorder=5)          # ½a₁
vec_arrow(ax, s1, path_end, "#2ca02c", lw=3.5, zorder=5)   # ½a₃, 从 ½a₁ 末端出发
vec_arrow(ax, O, b, "#d62728", lw=4.0, zorder=6)           # b，红色粗线

# --- 端点：小圆点 + 坐标文字标注 ---
def mark(ax, pos, text, color="#333333", dx=0.12, dy=-0.12, dz=0.0, fs=11, bold=True):
    ax.scatter(*pos, color=color, s=30, zorder=7)
    ax.text(pos[0]+dx, pos[1]+dy, pos[2]+dz, text, fontsize=fs,
            fontweight="bold" if bold else "normal", color="#222222", zorder=7)

mark(ax, O, "O(0,0,0)", color="#333333", dx=0.1, dy=-0.1, dz=-0.15, fs=11)
mark(ax, a1, "a₁(2,-1,0)", color="#9e9e9e", dx=0.1, dy=-0.05, dz=0.05, fs=10)
mark(ax, a2, "a₂(1,2,-1)", color="#9e9e9e", dx=-0.2, dy=0.1, dz=0.0, fs=10)
mark(ax, a3, "a₃(0,1,2)", color="#9e9e9e", dx=0.1, dy=0.1, dz=0.1, fs=10)
mark(ax, s1, "½a₁", color="#1f77b4", dx=0.1, dy=-0.15, dz=0.0, fs=10)
mark(ax, path_end, "b(1,0,1)", color="#d62728", dx=-0.15, dy=0.15, dz=-0.05, fs=11)
mark(ax, b, "", color="#d62728", dx=0, dy=0, dz=0, fs=9)   # 已在上面标注

# --- 关闭 3D 刻度/网格，保持教材干净风格 ---
ax.set_xlim(lo, hi); ax.set_ylim(lo, hi); ax.set_zlim(lo, hi)
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
ax.grid(False)
ax.view_init(elev=32, azim=-42)
ax.set_proj_type("ortho")
ax.set_axis_off()

# 底部图例文字块
fig.text(0.02, 0.02,
         "虚线 = 原始列向量 a₁,a₂,a₃   蓝/绿 = ½a₁ 与 ½a₃ 首尾相接   红 = 结果 b = ½a₁ + ½a₃",
         fontsize=10, color="#444444", ha="left")

out_svg = "/Users/weijibin/Documents/obsidian-notes/90-Storage/98-Asset-资源/MathSvg/LA002-3d-column-picture.svg"
out_png = "/Users/weijibin/Documents/obsidian-notes/90-Storage/98-Asset-资源/MathSvg/LA002-3d-column-picture.png"
plt.savefig(out_svg, format="svg")
plt.savefig(out_png, format="png", dpi=200)
print("saved both (textbook style)")
