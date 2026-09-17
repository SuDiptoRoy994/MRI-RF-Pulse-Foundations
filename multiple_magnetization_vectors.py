"""
Multiple Magnetization Vectors
================================
Three magnetization vectors plotted simultaneously.
Illustrates how different spin populations can point in different directions,
the starting point for understanding spin ensembles in MRI.

Bug fixed: original code labelled M3 as M1 in the legend.
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

vectors = {
    r'$M_1$ = (1, 0, 5)': ([1, 0, 5], 'red'),
    r'$M_2$ = (3, 4, 2)': ([3, 4, 2], 'royalblue'),
    r'$M_3$ = (0, 0, 6)': ([0, 0, 6], 'green'),
}

for label, (v, color) in vectors.items():
    ax.quiver(0, 0, 0, v[0], v[1], v[2],
              color=color, linewidth=3, label=label, arrow_length_ratio=0.12)

ax.set_xlabel(r'$M_x$', fontsize=12); ax.set_ylabel(r'$M_y$', fontsize=12)
ax.set_zlabel(r'$M_z$', fontsize=12)
ax.set_xlim(0, 6); ax.set_ylim(0, 6); ax.set_zlim(0, 6)
ax.set_title('Multiple Magnetization Vectors', fontsize=14)
ax.legend(fontsize=11); ax.grid(True)
plt.tight_layout()
plt.savefig("multiple_magnetization_vectors.png", dpi=150)
plt.show()
