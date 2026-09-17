"""
Constructing a 90-Degree Square RF Pulse
==========================================
For a square RF pulse, the flip angle is:
    theta = gamma * B1 * tau_pulse

To target theta = 90° = pi/2 radians with duration tau = 2:
    B1_amplitude = (pi/2) / tau

This is the simplest possible excitation pulse — the foundation of all MRI.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
target_angle = np.pi / 2
tau = 2
B1_amplitude = target_angle / tau
B1 = np.ones_like(t) * B1_amplitude

flip_angle_rad = np.trapezoid(B1, t)
flip_angle_deg = np.degrees(flip_angle_rad)
print(f"B1 amplitude = {B1_amplitude:.4f}")
print(f"Flip angle   = {flip_angle_deg:.2f} degrees")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t, B1, color='royalblue', linewidth=2.5)
ax.fill_between(t, B1, alpha=0.2, color='royalblue')
ax.set_xlabel("Time (arb. units)", fontsize=12)
ax.set_ylabel(r"$B_1(t)$ (arb. units)", fontsize=12)
ax.set_title(f"90° Square RF Pulse — B₁ = {B1_amplitude:.3f}, θ = {flip_angle_deg:.1f}°",
             fontsize=13)
ax.set_ylim(0, 1.0)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("construct_90deg_square_pulse.png", dpi=150)
plt.show()
