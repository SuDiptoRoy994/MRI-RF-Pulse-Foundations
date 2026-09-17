"""
Magnetization Vector in 3D Space
==================================
A single magnetization vector M = (2, 3, 5) plotted on 3D axes.
This visualises the fundamental object in MRI physics: the net nuclear
magnetisation vector of a proton spin ensemble.

Physical meaning of components:
  Mx, My — transverse plane (detected as the NMR/MRI signal)
  Mz     — longitudinal (along the static B0 field)
"""
import numpy as np
import matplotlib.pyplot as plt

M = np.array([2, 3, 5])

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, M[0], M[1], M[2], color='royalblue', linewidth=2.5,
          arrow_length_ratio=0.15)
ax.set_xlim(0, 6); ax.set_ylim(0, 6); ax.set_zlim(0, 6)
ax.set_xlabel(r'$M_x$', fontsize=12)
ax.set_ylabel(r'$M_y$', fontsize=12)
ax.set_zlabel(r'$M_z$', fontsize=12)
ax.set_title("Magnetization Vector M = (2, 3, 5)", fontsize=13)
plt.tight_layout()
plt.savefig("magnetization_vector_3d.png", dpi=150)
plt.show()
print(f"Vector magnitude |M| = {np.linalg.norm(M):.3f}")
