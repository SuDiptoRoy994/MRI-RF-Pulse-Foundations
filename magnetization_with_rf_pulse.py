"""
Magnetisation During an RF Pulse
==================================
Adds a rectangular RF pulse B1(t) to the Bloch equations.
The pulse drives Mx, My, Mz away from equilibrium — this is how
MRI excites the spin system to produce a detectable signal.

After the pulse ends, the system relaxes back to equilibrium
under T1 and T2.

Bug fixed from original: the shaded axvspan now correctly marks
the actual pulse window (t = 2 to 4), matching B1(t).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

gamma = 1.0; B0 = 1.0; T1 = 4.0; T2 = 2.0; M0 = 1.0

def B1(t):
    return 0.8 if 2.0 <= t <= 4.0 else 0.0

def bloch(t, M):
    Mx, My, Mz = M
    bx = B1(t)
    return [
        gamma*B0*My - Mx/T2,
        gamma*(Mz*bx - Mx*B0) - My/T2,
       -gamma*My*bx + (M0 - Mz)/T1
    ]

t = np.linspace(0, 8, 500)
sol = solve_ivp(bloch, [0, 8], [0., 0., 1.], t_eval=t, rtol=1e-9)
pulse = [B1(ti) for ti in t]

fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

axs[0].plot(t, sol.y[0], color='#E74C3C', lw=2, label=r'$M_x$')
axs[0].plot(t, sol.y[1], color='#2980B9', lw=2, label=r'$M_y$')
axs[0].plot(t, sol.y[2], color='#27AE60', lw=2, label=r'$M_z$')
axs[0].axvspan(2, 4, color='orange', alpha=0.2, label='RF Pulse (t=2 to 4)')
axs[0].set_ylabel("Magnetisation", fontsize=12)
axs[0].set_title("Magnetisation During and After an RF Pulse", fontsize=13)
axs[0].legend(fontsize=10); axs[0].grid(True, alpha=0.3)
axs[0].spines['top'].set_visible(False); axs[0].spines['right'].set_visible(False)

axs[1].plot(t, pulse, color='darkorange', linewidth=2.5)
axs[1].fill_between(t, pulse, alpha=0.2, color='orange')
axs[1].set_xlabel("Time (arb. units)", fontsize=12)
axs[1].set_ylabel(r"$B_1(t)$", fontsize=12)
axs[1].set_title("RF Pulse Shape", fontsize=12)
axs[1].grid(True, alpha=0.3)
axs[1].spines['top'].set_visible(False); axs[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("magnetization_with_rf_pulse.png", dpi=150)
plt.show()
