"""生成余弦定理「作高线」证法的钝角情形示意图（MA-GE-001-altitude-proof-obtuse.svg / .png）。

当角 A 为钝角（90° < A < 180°）时 cos A < 0，垂足 D 落在 AB 的延长线上（A 的另一侧）。
用有向长度：AD = b·cos A < 0，BD = c − b·cos A，代入勾股定理的代数与锐角情形逐字相同。
"""
import numpy as np
from matplotlib.patches import Arc
import matplotlib.pyplot as plt

A_DEG = 120.0
b = 4.5                 # 边 AC
c = 7.0                 # 边 AB
A = np.array([0.0, 0.0])
B = np.array([c, 0.0])
C = np.array([b * np.cos(np.radians(A_DEG)), b * np.sin(np.radians(A_DEG))])  # cosA<0 → C 在 A 左侧
D = np.array([C[0], 0.0])   # 垂足：AB 延长线上、A 的另一侧

fig, ax = plt.subplots(figsize=(7.6, 4.4))
ax.set_aspect("equal")
ax.axis("off")

# 底边：A-B 实线，A-D 延长线部分用点线
ax.plot([A[0], B[0]], [0, 0], "k-", lw=1.6)
ax.plot([D[0], A[0]], [0, 0], "k:", lw=1.0)

# 三角形两条斜边
for P, Q in [(B, C), (C, A)]:
    ax.plot([P[0], Q[0]], [P[1], Q[1]], "k-", lw=1.6)

# 高线 CD（虚线）与直角标记
ax.plot([C[0], D[0]], [C[1], D[1]], "k--", lw=1.2)
s = 0.28
ax.plot([D[0], D[0] + s], [D[1], D[1] + s], "k-", lw=1.1)
ax.plot([D[0], D[0] + s], [D[1] + s, D[1] + s], "k-", lw=1.1)

# 钝角 A 的弧线（0° → 120°）
ax.add_patch(Arc(A, 1.8, 1.8, theta1=0, theta2=A_DEG, lw=1.4, edgecolor="k", zorder=3))

# 顶点标注
ax.text(A[0] - 0.30, A[1] - 0.60, r"$A$", fontsize=15)
ax.text(B[0] + 0.28, B[1] - 0.60, r"$B$", fontsize=15)
ax.text(C[0] + 0.10, C[1] + 0.55, r"$C$", fontsize=15)
ax.text(D[0] - 0.55, D[1] - 0.58, r"$D$", fontsize=13)

# 线段标注（有向长度：AD = b cos A < 0）
ax.text(D[0] - 0.55, 2.0, r"$b\sin A$", fontsize=12.5, ha="right")  # 高线 CD，仍 > 0（放高线左侧空处）
ax.text(-1.15, -1.15, r"$-b\cos A$", fontsize=12.5)                    # |AD| = -b cos A（下沉避免碰顶点标签）
ax.text(2.40, 0.45, r"$c-b\cos A$", fontsize=12.5)         # BD
ax.text(2.50, -0.85, r"$c$", fontsize=13)                  # 底边 AB
ax.text(-2.40, 3.15, r"$b$", fontsize=13)                  # 边 AC
ax.text(3.35, 2.55, r"$a$", fontsize=13)                   # 边 BC

out = "/Users/weijibin/Documents/obsidian-notes/90-Storage/98-Asset-资源/MathSvg/"
fig.savefig(out + "MA-GE-001-altitude-proof-obtuse.svg", bbox_inches="tight", pad_inches=0.05)
fig.savefig(out + "MA-GE-001-altitude-proof-obtuse.png", dpi=200, bbox_inches="tight", pad_inches=0.05)
print("saved")