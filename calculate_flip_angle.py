"""
Flip Angle from a Square RF Pulse
===================================
The flip angle theta is proportional to the integral of B1(t):
    theta = gamma * integral[ B1(t) dt ]

Here gamma = 1 (normalised units). We integrate numerically.

Physical insight: a longer pulse or stronger B1 produces a larger tip angle.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8, 500)
dt = t[1] - t[0]
gamma = 1.0

# Square pulse active from t=2 to t=4
B1 = np.where((t >= 2) & (t <= 4), 0.8, 0.0)
flip = gamma * np.sum(B1) * dt

print(f"Flip angle = {flip:.4f} rad = {np.degrees(flip):.2f}°")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t, B1, color='royalblue', linewidth=2.5)
ax.fill_between(t, B1, alpha=0.25, color='royalblue',
                label=f'Pulse area → θ = {np.degrees(flip):.1f}°')
ax.set_xlabel("Time (arb. units)", fontsize=12)
ax.set_ylabel(r"$B_1(t)$", fontsize=12)
ax.set_title(f"Square RF Pulse — Numerical Flip Angle = {np.degrees(flip):.2f}°", fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("calculate_flip_angle.png", dpi=150)
plt.show()
