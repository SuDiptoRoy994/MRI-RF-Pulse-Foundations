"""
B1 Amplitude vs Flip Angle
============================
When the scanner's RF transmitter is miscalibrated, the delivered B1
field differs from the intended value. This directly changes the flip angle:

    theta = gamma * B1 * tau

This is called B1 inhomogeneity. It is unavoidable in clinical MRI,
especially at high field (3T, 7T) and in patients with implants.

This plot shows how a ±20% variation in B1 shifts the flip angle away
from the target of 90°. Robust pulse design (STA) minimises this sensitivity.
"""
import numpy as np
import matplotlib.pyplot as plt

gamma = 1.0
tau   = np.pi / 2        # pulse duration [arb.] → gives 90° at B1=1
B1_values = np.linspace(0.8, 1.2, 100)
theta_deg = np.degrees(gamma * B1_values * tau)

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
fig.suptitle(r'$B_1$ Inhomogeneity: Effect on Flip Angle', fontsize=13, fontweight='bold')

ax = axes[0]
ax.plot(B1_values, theta_deg, color='royalblue', lw=2.5)
ax.axhline(90, color='red', ls='--', lw=1.5, label='Target = 90°')
ax.set_xlabel(r'$B_1$ amplitude (normalised)', fontsize=12)
ax.set_ylabel('Flip angle (degrees)', fontsize=12)
ax.set_title(r'Flip Angle vs $B_1$ Amplitude', fontsize=12)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

ax = axes[1]
error = np.abs(theta_deg - 90)
ax.plot(B1_values, error, color='darkorange', lw=2.5)
ax.set_xlabel(r'$B_1$ amplitude (normalised)', fontsize=12)
ax.set_ylabel('Absolute flip-angle error (degrees)', fontsize=12)
ax.set_title(r'Flip-Angle Error vs $B_1$ Amplitude', fontsize=12)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("b1_amplitude_vs_flip_angle.png", dpi=150)
plt.show()
print(f"At B1=0.8: theta = {np.degrees(gamma*0.8*tau):.1f}°  error = {abs(np.degrees(gamma*0.8*tau)-90):.1f}°")
print(f"At B1=1.0: theta = {np.degrees(gamma*1.0*tau):.1f}°  error = {abs(np.degrees(gamma*1.0*tau)-90):.1f}°")
print(f"At B1=1.2: theta = {np.degrees(gamma*1.2*tau):.1f}°  error = {abs(np.degrees(gamma*1.2*tau)-90):.1f}°")
