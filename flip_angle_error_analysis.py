"""
Flip-Angle Error Analysis — Computational Experiment
======================================================
Given a set of actual flip angles (e.g., measured from scanner calibration),
compute absolute and percentage errors relative to the target (90°).

This is a prototype of the error analysis one would run when evaluating
a new pulse design or calibrating a scanner.
"""
import numpy as np
import matplotlib.pyplot as plt

target  = 90.0
actual  = np.array([80, 85, 88, 89, 90, 91, 92, 95, 100])
error   = np.abs(actual - target)
pct_err = (error / target) * 100

print(f"Target angle: {target}°")
print(f"Actual angles:      {actual}")
print(f"Absolute errors (°): {error}")
print(f"Percentage errors:   {np.round(pct_err, 2)}")

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
fig.suptitle('Flip-Angle Error Analysis', fontsize=13, fontweight='bold')

ax = axes[0]
ax.plot(actual, error, 'o-', color='royalblue', lw=2, markersize=8)
ax.axvline(target, color='red', ls='--', lw=1.5, label='Target = 90°')
ax.set_xlabel('Actual Flip Angle (degrees)', fontsize=12)
ax.set_ylabel('Absolute Error (degrees)', fontsize=12)
ax.set_title('Absolute Error', fontsize=12)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

ax = axes[1]
ax.plot(actual, pct_err, 's-', color='darkorange', lw=2, markersize=8)
ax.axvline(target, color='red', ls='--', lw=1.5, label='Target = 90°')
ax.set_xlabel('Actual Flip Angle (degrees)', fontsize=12)
ax.set_ylabel('Percentage Error (%)', fontsize=12)
ax.set_title('Percentage Error', fontsize=12)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("flip_angle_error_analysis.png", dpi=150)
plt.show()
