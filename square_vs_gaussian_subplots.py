"""
Square vs Gaussian RF Pulse — Subplots
========================================
The same two pulse shapes shown in separate panels for clear visual isolation.
Useful for comparing shape characteristics independently before overlaying.

Subplot layout:
  Top:    Square pulse — abrupt onset, constant amplitude, abrupt end
  Bottom: Gaussian pulse — smooth symmetric bell curve
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8, 500)

square   = np.where((t >= 2) & (t <= 4), 0.8, 0.0)
A, center, sigma = 0.8, 3.0, 0.4
gaussian = A * np.exp(-(t - center)**2 / (2 * sigma**2))

fig, axs = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
fig.suptitle("RF Pulse Shapes: Square vs Gaussian", fontsize=13, fontweight='bold')

axs[0].plot(t, square, color='royalblue', lw=2.5)
axs[0].fill_between(t, square, alpha=0.2, color='royalblue')
axs[0].set_ylabel("RF Amplitude", fontsize=12)
axs[0].set_title("Square Pulse", fontsize=12, fontweight='bold')
axs[0].set_ylim(-0.05, 1.0); axs[0].grid(True, alpha=0.3)
axs[0].spines['top'].set_visible(False); axs[0].spines['right'].set_visible(False)

axs[1].plot(t, gaussian, color='darkorange', lw=2.5)
axs[1].fill_between(t, gaussian, alpha=0.2, color='orange')
axs[1].set_xlabel("Time (arb. units)", fontsize=12)
axs[1].set_ylabel("RF Amplitude", fontsize=12)
axs[1].set_title("Gaussian Pulse", fontsize=12, fontweight='bold')
axs[1].set_ylim(-0.05, 1.0); axs[1].grid(True, alpha=0.3)
axs[1].spines['top'].set_visible(False); axs[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("square_vs_gaussian_subplots.png", dpi=150)
plt.show()
