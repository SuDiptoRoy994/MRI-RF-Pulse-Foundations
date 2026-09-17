"""
RF Pulse Energy
================
The RF energy deposited in the sample is proportional to:
    E = integral[ B1(t)^2 dt ]

This is directly related to the Specific Absorption Rate (SAR) in MRI —
the key safety constraint on RF pulse design.

High flip angle pulses and long pulses both increase SAR.
STA reduces SAR by shortening the pulse duration.
"""
import numpy as np
import matplotlib.pyplot as plt

t  = np.linspace(0, 8, 1000)
dt = t[1] - t[0]

B1 = np.where((t >= 2) & (t <= 4), 1.6, 0.0)

flip   = np.sum(B1) * dt
energy = np.sum(B1**2) * dt

print(f"Flip-angle measure = {flip:.4f}")
print(f"RF energy measure  = {energy:.4f}  (proportional to SAR)")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t, B1, color='darkorange', linewidth=2.5)
ax.fill_between(t, B1, alpha=0.25, color='darkorange')
ax.set_xlabel("Time (arb. units)", fontsize=12)
ax.set_ylabel(r"$B_1(t)$", fontsize=12)
ax.set_title(f"Square RF Pulse — Flip = {flip:.2f} rad,  SAR ∝ Energy = {energy:.2f}",
             fontsize=12)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("calculate_rf_energy.png", dpi=150)
plt.show()
