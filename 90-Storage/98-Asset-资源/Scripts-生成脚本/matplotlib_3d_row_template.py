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

# ============ 三维方程组（行图像）：三个平面相交于一点 ============
#  平面1: 2x + y = 1      （竖直平面，与 z 无关）
#  平面2: -x + 2y + z = 0 （一般平面）
#  平面3: -y + 2z = 1     （竖直平面，与 x 无关）
#  解: (x, y, z) = (0.5, 0, 0.5)

P = np.array([0.5, 0.0, 0.5])   # 交点/解

lo, hi = -1.5, 2.5
fig = plt.figure(figsize=(7.2, 7.2), dpi=200)
ax = fig.add_subplot(111, projection="3d")

# ---------- 坐标轴（教材风格：正半轴实线 + 箭头，负半轴浅灰虚线） ----------
for axis, (vec, label) in enumerate([(np.array([2.8,0,0]),"X"), (np.array([0,2.8,0]),"Y"), (np.array([0,0,2.8]),"Z")]):
    ax.plot3D(*zip(np.zeros(3), vec), color="#444444", linewidth=1.8, zorder=2)
    d = vec; e = d / np.linalg.norm(d)
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
    neg = np.array([-1.2, 0, 0]) if axis == 0 else (np.array([0, -1.2, 0]) if axis == 1 else np.array([0, 0, -1.2]))
    ax.plot3D(*zip(np.zeros(3), neg), color="#c0c0c0", linewidth=1.2, linestyle="--", zorder=1)

# ---------- 三个平面（半透明网格） ----------
x = np.linspace(lo, hi, 25)
y = np.linspace(lo, hi, 25)
Xg, Yg = np.meshgrid(x, y)

# 平面1: y = 1 - 2x（用 x,z 参数化，y 由 x 决定）
X1, Z1 = np.meshgrid(x, np.linspace(lo, hi, 25))
Y1 = 1 - 2 * X1
ax.plot_surface(X1, Y1, Z1, alpha=0.28, color="#d62728", edgecolor="none", zorder=1)
# 直接在平面上标注
ax.text(-0.6, 2.2, -0.4, "平面1: 2x+y=1", fontsize=11, fontweight="bold", color="#d62728", zorder=7)

# 平面2: z = x - 2y
Z2 = Xg - 2 * Yg
ax.plot_surface(Xg, Yg, Z2, alpha=0.28, color="#1f77b4", edgecolor="none", zorder=1)
ax.text(2.2, -1.0, 3.8, "平面2: -x+2y+z=0", fontsize=11, fontweight="bold", color="#1f77b4", zorder=7)

# 平面3: z = (1 + y) / 2
Z3 = (1 + Yg) / 2
ax.plot_surface(Xg, Yg, Z3, alpha=0.28, color="#2ca02c", edgecolor="none", zorder=1)
ax.text(-1.3, 2.2, 1.7, "平面3: -y+2z=1", fontsize=11, fontweight="bold", color="#2ca02c", zorder=7)

# ---------- 三条交线（两两平面相交） ----------
t = np.linspace(lo, hi, 60)
# L12: 平面1∩平面2 => y = 1-2x, z = 5x-2
ax.plot3D(t, 1 - 2*t, 5*t - 2, color="#8b2252", linewidth=3.0, zorder=5)
ax.text(-0.05, 1.1, -2.25, "L₁₂: 平面1∩平面2", fontsize=10, fontweight="bold", color="#8b2252", zorder=7, rotation=0)
# L13: 平面1∩平面3 => y = 1-2x, z = 1-x
ax.plot3D(t, 1 - 2*t, 1 - t, color="#a67c00", linewidth=3.0, zorder=5)
ax.text(-1.4, 2.0, 2.4, "L₁₃: 平面1∩平面3", fontsize=10, fontweight="bold", color="#a67c00", zorder=7)
# L23: 平面2∩平面3 => y = 2z-1, x = 5z-2（用 z 参数化）
ax.plot3D(5*t - 2, 2*t - 1, t, color="#00695c", linewidth=3.0, zorder=5)
ax.text(0.6, -0.95, -0.5, "L₂₃: 平面2∩平面3", fontsize=10, fontweight="bold", color="#00695c", zorder=7)

# ---------- 交点标注（教材风格：小圆点 + 文字） ----------
ax.scatter(*P, color="#111111", s=60, zorder=8)
ax.text(P[0]+0.12, P[1]-0.1, P[2]+0.15, "解 P(0.5, 0, 0.5)\n三线共点",
        fontsize=11, fontweight="bold", color="#111111", zorder=8,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.85, edgecolor="#333333", linewidth=1))

# ---------- 关闭刻度/网格，教材干净风格 ----------
ax.set_xlim(lo, hi); ax.set_ylim(lo, hi); ax.set_zlim(lo, hi)
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
ax.grid(False)
ax.view_init(elev=32, azim=-42)
ax.set_proj_type("ortho")
ax.set_axis_off()

# 底部图例文字块
fig.text(0.02, 0.02,
         "三个平面两两相交产生三条直线 L₁₂, L₁₃, L₂₃；三条交线交于一点 = 方程组的解 P(0.5,0,0.5)",
         fontsize=10, color="#444444", ha="left")

out_svg = "/Users/weijibin/Documents/obsidian-notes/90-Storage/98-Asset-资源/MathSvg/LA002-3d-row-picture.svg"
out_png = "/Users/weijibin/Documents/obsidian-notes/90-Storage/98-Asset-资源/MathSvg/LA002-3d-row-picture.png"
plt.savefig(out_svg, format="svg")
plt.savefig(out_png, format="png", dpi=200)
print("saved both (row picture, textbook style)")