"""生成余弦定理示意图（MA-GE-001-cosine-theorem.svg / .png）。

三角形 ABC，边长按「对顶点」约定：a = BC, b = CA, c = AB。
θ 画在顶点 C：向量 a（C→B）与向量 b（C→A）的夹角，第三边 c 与角相对，
满足 c² = a² + b² - 2ab cosθ。

历史修复：旧图把 θ 弧线误标在顶点 A（那是 b 与 c 的夹角），
2026-09-08 修正为画在顶点 C。
"""
import numpy as np
from matplotlib.patches import Arc
import matplotlib.pyplot as plt

A = np.array([2.0, 2.0])
B = np.array([8.0, 2.0])
C = np.array([5.0, 7.0])

fig, ax = plt.subplots(figsize=(4.63, 3.28))
ax.set_aspect("equal")
ax.axis("off")

# 三角形三边
ax.plot([A[0], B[0]], [A[1], B[1]], "k-", lw=1.5)   # 边 c = AB
ax.plot([B[0], C[0]], [B[1], C[1]], "k-", lw=1.5)   # 边 a = BC（兼向量 a）
ax.plot([C[0], A[0]], [C[1], A[1]], "k-", lw=1.5)   # 边 b = CA（兼向量 b）

# 向量箭头：从 C 出发指向 B / A，表示向量 a, b 同起点
for tip, tail in [(B, C), (A, C)]:
    ax.annotate("", xy=tip, xytext=tail,
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.5))


def angle(u, v):
    """从点 u 指向点 v 的向量与 x 轴的夹角（度，matplotlib 逆时针为正）。"""
    return np.degrees(np.arctan2(v[1] - u[1], v[0] - u[0]))


# θ 弧线：顶点 C 处、边 a 与 b 之间的夹角
th_a, th_b = sorted([angle(C, B), angle(C, A)])
r = 0.9
ax.add_patch(Arc(C, 2 * r, 2 * r, theta1=th_a, theta2=th_b, lw=1.5, edgecolor="k"))

# θ 标注：弧线外侧、沿角平分线方向
mid = np.radians((th_a + th_b) / 2)
pos = C + 1.35 * np.array([np.cos(mid), np.sin(mid)])
ax.text(pos[0], pos[1], r"$\theta$", ha="center", va="center", fontsize=14)

# 顶点标注
ax.text(A[0] - 0.35, A[1] - 0.55, r"$A$", fontsize=14)
ax.text(B[0] + 0.35, B[1] - 0.55, r"$B$", fontsize=14)
ax.text(C[0], C[1] + 0.55, r"$C$", fontsize=14)

# 边长标注（a, b 加粗表示向量）
ax.text(6.9, 4.5, r"$\mathbf{a}$", fontsize=13)    # 边 a = BC
ax.text(3.1, 4.5, r"$\mathbf{b}$", fontsize=13)    # 边 b = CA
ax.text(5.0, 1.55, r"$c$", fontsize=13)            # 边 c = AB

# 底部公式
ax.text(5.0, -0.35, r"$c^2 = a^2 + b^2 - 2ab \cos\theta$",
        ha="center", va="center", fontsize=13,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.8))

out = "/Users/weijibin/Documents/obsidian-notes/90-Storage/98-Asset-资源/MathSvg/"
fig.savefig(out + "MA-GE-001-cosine-theorem.svg", bbox_inches="tight", pad_inches=0.05)
fig.savefig(out + "MA-GE-001-cosine-theorem.png", dpi=200, bbox_inches="tight", pad_inches=0.05)
print("saved")