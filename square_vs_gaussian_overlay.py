"""
Square vs Gaussian RF Pulse — Overlay
=======================================
Side-by-side comparison of two fundamental RF pulse shapes:

Square pulse:   constant amplitude within a window, zero elsewhere
                → abrupt transitions, broader bandwidth, higher peak energy

Gaussian pulse: smooth bell-shaped envelope
                → softer transitions, narrower bandwidth, lower SAR for same flip

Both are plotted on the same axis to make the shape contrast immediately visible.
""" 
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8, 500)

square   = np.where((t >= 2) & (t <= 4), 0.8, 0.0)
A, center, sigma = 0.8, 3.0, 0.4
gaussian = A * np.exp(-(t - center)**2 / (2 * sigma**2))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t, square,   color='royalblue', lw=2.5, label='Square pulse (t=2 to 4)')
ax.plot(t, gaussian, color='darkorange', lw=2.5, label=f'Gaussian (centre={center}, σ={sigma})')
ax.set_xlabel("Time (arb. units)", fontsize=12)
ax.set_ylabel("RF Amplitude", fontsize=12)
ax.set_title("Square vs Gaussian RF Pulse — Shape Comparison", fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3); ax.set_ylim(-0.05, 1.0)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("square_vs_gaussian_overlay.png", dpi=150)
plt.show()
