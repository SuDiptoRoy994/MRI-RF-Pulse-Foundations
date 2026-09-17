"""
Comparing Two RF Pulses — Flip Angle and SAR
=============================================
Two rectangular pulses with different amplitude and duration:
  Pulse A: shorter and taller
  Pulse B: longer and shorter

Key insight: pulses can have the same flip angle but very different
RF energy (SAR). Pulse A has higher peak power but lower total energy.
"""
import numpy as np
import matplotlib.pyplot as plt

t  = np.linspace(0, 8, 1000)
dt = t[1] - t[0]

B1_A = np.where((t >= 2) & (t <= 4), 0.8, 0.0)   # shorter, taller
B1_B = np.where((t >= 1) & (t <= 5), 0.4, 0.0)   # longer, shorter

flip_A = np.sum(B1_A) * dt;  energy_A = np.sum(B1_A**2) * dt
flip_B = np.sum(B1_B) * dt;  energy_B = np.sum(B1_B**2) * dt

print(f"Pulse A — Flip: {flip_A:.3f} rad,  Energy: {energy_A:.3f}")
print(f"Pulse B — Flip: {flip_B:.3f} rad,  Energy: {energy_B:.3f}")

fig, axs = plt.subplots(2, 1, figsize=(10, 7))

axs[0].plot(t, B1_A, color='royalblue', lw=2, label=f'Pulse A  (flip={flip_A:.2f} rad, SAR∝{energy_A:.2f})')
axs[0].plot(t, B1_B, color='darkorange', lw=2, label=f'Pulse B  (flip={flip_B:.2f} rad, SAR∝{energy_B:.2f})')
axs[0].set_ylabel(r'$B_1(t)$', fontsize=12)
axs[0].set_title('Two RF Pulses — Same Flip Angle, Different SAR', fontsize=13)
axs[0].legend(fontsize=10); axs[0].grid(True, alpha=0.3)
axs[0].spines['top'].set_visible(False); axs[0].spines['right'].set_visible(False)

labels = ['Flip A', 'Flip B', 'Energy A', 'Energy B']
values = [flip_A, flip_B, energy_A, energy_B]
colors = ['royalblue', 'darkorange', 'royalblue', 'darkorange']
bars = axs[1].bar(labels, values, color=colors, alpha=0.75)
axs[1].set_ylabel('Value (arb. units)', fontsize=12)
axs[1].set_title('Flip Angle vs RF Energy Comparison', fontsize=13)
axs[1].grid(axis='y', alpha=0.3)
axs[1].spines['top'].set_visible(False); axs[1].spines['right'].set_visible(False)
for bar, val in zip(bars, values):
    axs[1].text(bar.get_x() + bar.get_width()/2, val + 0.02, f'{val:.2f}',
                ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("compare_two_pulses.png", dpi=150)
plt.show()
