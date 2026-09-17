"""生成余弦定理「作高线」证法示意图（MA-GE-001-altitude-proof.svg / .png）。

证法二：过顶点 C 向 AB 作垂线，垂足 D，把三角形分成两个直角三角形，
对 CD、BD 用勾股定理展开即得余弦定理。本图展示该构造与关键线段关系：
AD = b cos A，CD = b sin A，BD = c - b cos A。
"""
import numpy as np
from matplotlib.patches import Arc
import matplotlib.pyplot as plt

A_DEG = 60.0
b = 5.0                 # 边 AC
c = 7.0                 # 边 AB
A = np.array([0.0, 0.0])
B = np.array([c, 0.0])
C = np.array([b * np.cos(np.radians(A_DEG)), b * np.sin(np.radians(A_DEG))])
D = np.array([C[0], 0.0])

fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.set_aspect("equal")
ax.axis("off")

# 三角形三条边
for P, Q in [(A, B), (B, C), (C, A)]:
    ax.plot([P[0], Q[0]], [P[1], Q[1]], "k-", lw=1.6)

# 高线 CD（虚线）与直角标记
ax.plot([C[0], D[0]], [C[1], D[1]], "k--", lw=1.2)
s = 0.28
ax.plot([D[0], D[0] + s], [D[1], D[1] + s], "k-", lw=1.1)
ax.plot([D[0], D[0] + s], [D[1] + s, D[1] + s], "k-", lw=1.1)

# 角 A 的弧线
ax.add_patch(Arc(A, 1.0, 1.0, theta1=0, theta2=A_DEG, lw=1.4, edgecolor="k"))

# 顶点标注
ax.text(A[0] - 0.30, A[1] - 0.60, r"$A$", fontsize=15)
ax.text(B[0] + 0.28, B[1] - 0.60, r"$B$", fontsize=15)
ax.text(C[0], C[1] + 0.55, r"$C$", fontsize=15)
ax.text(D[0] + 0.18, D[1] - 0.58, r"$D$", fontsize=13)

# 线段标注
ax.text(C[0] + 0.28, 2.15, r"$b\sin A$", fontsize=12.5)   # CD
ax.text(1.22, 0.45, r"$b\cos A$", fontsize=12.5)          # AD
ax.text(4.80, 0.45, r"$c-b\cos A$", fontsize=12.5)        # BD
ax.text(3.5, -0.82, r"$c$", fontsize=13)                  # 底边 AB
ax.text(0.62, 2.62, r"$b$", fontsize=13)                  # 边 AC
ax.text(5.15, 2.42, r"$a$", fontsize=13)                  # 边 BC

out = "/Users/weijibin/Documents/obsidian-notes/90-Storage/98-Asset-资源/MathSvg/"
fig.savefig(out + "MA-GE-001-altitude-proof.svg", bbox_inches="tight", pad_inches=0.05)
fig.savefig(out + "MA-GE-001-altitude-proof.png", dpi=200, bbox_inches="tight", pad_inches=0.05)
print("saved")