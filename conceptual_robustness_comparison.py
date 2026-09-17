"""
Conceptual B1 Robustness Comparison
=====================================
Compares a conventional square pulse against a conceptual STA-like robust pulse.

IMPORTANT NOTE: The robust/STA-like curve is illustrative only — the values
(89.2, 89.6, 90.0, 90.4, 90.8 degrees) are chosen to demonstrate near-flat
B1 tolerance qualitatively. A true STA design requires full Bloch equation
simulation with counterdiabatic driving (see the STA-Spin-Dynamics repository).

Physical motivation: STA-designed pulses have intrinsic robustness to B1
variation because fidelity is enforced by the geometry of the Hamiltonian
eigenstate trajectory, not by precise amplitude calibration.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
B1_amplitude  = (np.pi / 2) / 2.0
B1_scales     = np.array([0.8, 0.9, 1.0, 1.1, 1.2])

actual_angles = [np.degrees(np.trapezoid(s * np.ones_like(t) * B1_amplitude, t))
                 for s in B1_scales]
actual_angles = np.array(actual_angles)

# Conceptual STA-like angles (illustrative — not computed from STA equations)
robust_angles = np.array([89.2, 89.6, 90.0, 90.4, 90.8])

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(B1_scales, actual_angles, 'o-', color='#D7191C', lw=2.5, markersize=9,
        label='Conventional square pulse')
ax.plot(B1_scales, robust_angles, 's--', color='#1A9641', lw=2.5, markersize=9,
        label='Robust / STA-like (conceptual)')
ax.axhline(90, color='gray', ls=':', lw=1.5, label='Target = 90°')
ax.set_xlabel(r'$B_1$ scale factor ($k$)', fontsize=12)
ax.set_ylabel('Flip Angle (degrees)', fontsize=12)
ax.set_title(r'$B_1$ Robustness: Conventional vs STA-like Pulse (Conceptual)', fontsize=12)
ax.legend(fontsize=11); ax.set_ylim(60, 120); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("conceptual_robustness_comparison.png", dpi=150)
plt.show()
