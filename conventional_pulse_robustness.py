"""
Conventional Square Pulse — B1 Robustness Test
================================================
Systematically tests how a conventional square pulse responds to
B1 field variations of ±20%.

Result: flip angle scales linearly with B1, so any miscalibration
directly translates to a proportional flip-angle error.
This is the core weakness of conventional pulses that motivates
adiabatic and STA approaches.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
target_angle  = np.pi / 2
B1_amplitude  = target_angle / 2.0
B1_nominal    = np.ones_like(t) * B1_amplitude
B1_scales     = np.array([0.8, 0.9, 1.0, 1.1, 1.2])

actual_angles = [np.degrees(np.trapezoid(s * B1_nominal, t)) for s in B1_scales]
actual_angles = np.array(actual_angles)
errors        = np.abs(actual_angles - 90)

print(f"B1 scale:           {B1_scales}")
print(f"Actual angles (°):  {np.round(actual_angles, 2)}")
print(f"Flip-angle errors:  {np.round(errors, 2)}")

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(B1_scales, actual_angles, 'o-', color='#D7191C', lw=2.5,
        markersize=9, label='Conventional square pulse')
ax.axhline(90, color='gray', ls='--', lw=1.5, label='Target = 90°')
ax.set_xlabel(r'$B_1$ scale factor', fontsize=12)
ax.set_ylabel('Actual Flip Angle (degrees)', fontsize=12)
ax.set_title(r'Conventional Pulse: Flip Angle vs $B_1$ Miscalibration', fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("conventional_pulse_robustness.png", dpi=150)
plt.show()
