"""
Larmor Precession — Analytical Model
======================================
Nuclear spins in a static B0 field precess at the Larmor frequency omega.
Without relaxation, this produces sinusoidal oscillations in Mx and My
while Mz stays constant (no energy exchange with the lattice).

    Mx(t) = cos(omega * t)
    My(t) = sin(omega * t)
    Mz(t) = 1   [constant — no T1 or T2 relaxation modelled here]

For a full model including T1/T2 relaxation and ODE integration,
see 03_bloch_ode_simulations/.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 400)
omega = 2   # Larmor frequency [rad/s]

Mx = np.cos(omega * t)
My = np.sin(omega * t)
Mz = np.ones_like(t)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t, Mx, color='#E74C3C', lw=2, label=r'$M_x = \cos(\omega t)$')
ax.plot(t, My, color='#2980B9', lw=2, label=r'$M_y = \sin(\omega t)$')
ax.plot(t, Mz, color='#27AE60', lw=2, label=r'$M_z = 1$ (constant)')
ax.set_xlabel('Time (arb. units)', fontsize=12)
ax.set_ylabel('Magnetisation', fontsize=12)
ax.set_title(f'Larmor Precession (analytical) — ω = {omega} rad/s', fontsize=13)
ax.grid(True, alpha=0.3); ax.legend(fontsize=11)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("larmor_precession_analytical.png", dpi=150)
plt.show()
