"""
Bloch Equation Simulation — Basic (scipy ODE solver)
======================================================
Solves the Bloch equations numerically using scipy.integrate.solve_ivp.
This is a significant step up from the analytical sine model: it correctly
handles T1 longitudinal recovery and T2 transverse decay simultaneously.

Bloch equations (lab frame, rotating-frame equivalent with B0 on z):
    dMx/dt =  gamma*B0*My  - Mx/T2
    dMy/dt = -gamma*B0*Mx  - My/T2
    dMz/dt =  (M0 - Mz)/T1

Start: Mx=1, My=0, Mz=0  (spin tipped into the transverse plane)
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

gamma = 1.0; B0 = 1.0; T1 = 8.0; T2 = 2.0; M0 = 1.0

def bloch(t, M):
    Mx, My, Mz = M
    return [
        gamma*B0*My - Mx/T2,
       -gamma*B0*Mx - My/T2,
        (M0 - Mz)/T1
    ]

t = np.linspace(0, 10, 500)
sol = solve_ivp(bloch, [0, 10], [1., 0., 0.], t_eval=t, rtol=1e-9)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t, sol.y[0], color='#E74C3C', lw=2, label=r'$M_x$ (T2 decay)')
ax.plot(t, sol.y[1], color='#2980B9', lw=2, label=r'$M_y$ (T2 decay)')
ax.plot(t, sol.y[2], color='#27AE60', lw=2, label=r'$M_z$ (T1 recovery)')
ax.set_xlabel("Time (arb. units)", fontsize=12)
ax.set_ylabel("Magnetisation", fontsize=12)
ax.set_title(f"Bloch Equation Simulation  (T1={T1}, T2={T2})", fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("bloch_simulation_basic.png", dpi=150)
plt.show()
print(f"Final state: Mx={sol.y[0,-1]:.3f}, My={sol.y[1,-1]:.3f}, Mz={sol.y[2,-1]:.3f}")
