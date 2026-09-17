"""
Precession with Partial Longitudinal Magnetisation
====================================================
Same analytical precession, but Mz = 0.5 instead of 1.0.
Models a spin that has been partially tipped from equilibrium (Mz = 1)
toward the transverse plane — midway between fully relaxed and fully inverted.

This is a stepping stone toward understanding RF pulse-induced tip angles.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 400)
omega = 5

Mx = np.cos(omega * t)
My = np.sin(omega * t)
Mz = 0.5 * np.ones_like(t)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t, Mx, color='#E74C3C', lw=2, label=r'$M_x$')
ax.plot(t, My, color='#2980B9', lw=2, label=r'$M_y$')
ax.plot(t, Mz, color='#27AE60', lw=2, label=r'$M_z = 0.5$ (partial tip)')
ax.set_xlabel('Time (arb. units)', fontsize=12)
ax.set_ylabel('Magnetisation', fontsize=12)
ax.set_title(f'Precession with Partial Tip — ω = {omega} rad/s', fontsize=13)
ax.grid(True, alpha=0.3); ax.legend(fontsize=11)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("precession_partial_tip.png", dpi=150)
plt.show()
