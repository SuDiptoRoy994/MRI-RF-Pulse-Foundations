"""
Gaussian RF Pulse — Flip Angle
================================
A Gaussian pulse has a smooth, bell-shaped envelope:
    B1(t) = A * exp( -(t - t0)^2 / (2*sigma^2) )

Compared with a square pulse of the same peak amplitude, the Gaussian:
  - deposits less RF energy (lower SAR)
  - has a narrower excitation bandwidth
  - has smoother transitions (better hardware compatibility)

The flip angle is still computed as gamma * integral[B1(t) dt].
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8, 500)
dt = t[1] - t[0]
gamma = 1.0

A, center, sigma = 0.8, 3.0, 0.4
B1 = A * np.exp(-(t - center)**2 / (2 * sigma**2))

flip = gamma * np.sum(B1) * dt
print(f"Gaussian flip angle = {flip:.4f} rad = {np.degrees(flip):.2f}°")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t, B1, color='darkorange', linewidth=2.5)
ax.fill_between(t, B1, alpha=0.25, color='orange',
                label=f'Flip angle = {np.degrees(flip):.2f}°')
ax.set_xlabel("Time (arb. units)", fontsize=12)
ax.set_ylabel(r"$B_1(t)$", fontsize=12)
ax.set_title(f"Gaussian RF Pulse — θ ≈ {np.degrees(flip):.1f}°,  σ = {sigma}", fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("gaussian_flip_angle.png", dpi=150)
plt.show()
