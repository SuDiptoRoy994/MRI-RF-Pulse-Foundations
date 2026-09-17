"""
Bloch Simulation — Effect of T2 on Transverse Decay
======================================================
Compares two T2 values to show how different tissues or field conditions
lead to faster or slower signal decay.

Longer T2 → signal persists longer → more time for MRI readout.
Shorter T2 → signal dies quickly → less time for readout.

This is why T2 is a key tissue contrast parameter in MRI.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

gamma = 1.0; B0 = 1.0; T1 = 4.0; M0 = 1.0

def bloch(t, M, T2):
    Mx, My, Mz = M
    return [
        gamma*B0*My - Mx/T2,
       -gamma*B0*Mx - My/T2,
        (M0 - Mz)/T1
    ]

t = np.linspace(0, 10, 500)
sol1 = solve_ivp(bloch, [0,10], [1.,0.,0.], args=(2.0,), t_eval=t, rtol=1e-9)
sol2 = solve_ivp(bloch, [0,10], [1.,0.,0.], args=(0.5,), t_eval=t, rtol=1e-9)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t, sol1.y[0], 'r-',  lw=2, label=r'$M_x$ (T2 = 2.0)')
ax.plot(t, sol1.y[1], 'b-',  lw=2, label=r'$M_y$ (T2 = 2.0)')
ax.plot(t, sol2.y[0], 'r--', lw=2, label=r'$M_x$ (T2 = 0.5)')
ax.plot(t, sol2.y[1], 'b--', lw=2, label=r'$M_y$ (T2 = 0.5)')
ax.set_xlabel("Time (arb. units)", fontsize=12)
ax.set_ylabel("Transverse Magnetisation", fontsize=12)
ax.set_title("Effect of T2 on Transverse Magnetisation Decay", fontsize=13)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("bloch_t2_comparison.png", dpi=150)
plt.show()
