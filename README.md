# 🧲 MRI RF Pulse Foundations

**A self-directed learning progression in MRI physics and RF pulse design — from spin vectors to Bloch equation simulations**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.10%2B-8CAAE6?style=flat&logo=scipy&logoColor=white)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557C?style=flat)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **This repository documents the self-directed learning journey that led to the
> [STA-Spin-Dynamics](https://github.com/SuDiptoRoy994/STA-Spin-Dynamics) project.**
> Each script builds on the previous one — from plotting a single vector to solving
> the full Bloch ODE system under an RF pulse.

---

## Overview

This collection contains 18 Python scripts organised into 5 progressive modules.
The learning arc goes:

```
Static magnetisation vector
        ↓
Analytical Larmor precession
        ↓
RF pulse design (flip angle, SAR, pulse shapes)
        ↓
Bloch ODE simulation with T1/T2 relaxation
        ↓
B1 robustness analysis → motivation for STA
```

Working through these scripts in order builds the physical intuition and
computational skills needed to understand the Shortcuts to Adiabaticity (STA)
technique demonstrated in the companion repository.

---

## Repository Structure

```
MRI-RF-Pulse-Foundations/
│
├── 01_magnetization_basics/
│   ├── magnetization_vector_3d.py          ← Single M vector in 3D
│   ├── multiple_magnetization_vectors.py   ← Multiple spin populations
│   ├── larmor_precession_analytical.py     ← Mx=cos(ωt), My=sin(ωt), Mz=const
│   └── precession_partial_tip.py           ← Partial tip: Mz = 0.5
│
├── 02_rf_pulse_fundamentals/
│   ├── construct_90deg_square_pulse.py     ← Design a 90° square pulse
│   ├── calculate_flip_angle.py             ← theta = γ ∫B1(t)dt
│   ├── calculate_rf_energy.py              ← SAR ∝ ∫B1²(t)dt
│   ├── gaussian_flip_angle.py              ← Gaussian pulse flip angle
│   └── compare_two_pulses.py               ← Same flip, different SAR
│
├── 03_bloch_ode_simulations/
│   ├── bloch_simulation_basic.py           ← First solve_ivp Bloch simulation
│   ├── bloch_t2_comparison.py              ← Two T2 values side-by-side
│   └── magnetization_with_rf_pulse.py      ← Spin response during RF pulse
│
├── 04_b1_robustness_analysis/
│   ├── b1_amplitude_vs_flip_angle.py       ← How B1 errors shift flip angle
│   ├── flip_angle_error_analysis.py        ← Absolute and % error computation
│   ├── conventional_pulse_robustness.py    ← Systematic ±20% B1 sweep
│   └── conceptual_robustness_comparison.py ← Conventional vs STA-like (conceptual)
│
├── 05_pulse_shape_comparison/
│   ├── square_vs_gaussian_overlay.py       ← Both pulses on one axis
│   └── square_vs_gaussian_subplots.py      ← Separate panels for clarity
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Module Guide

### Module 01 — Magnetization Basics

The magnetization vector **M** = (Mx, My, Mz) is the fundamental object of MRI.
These scripts build the geometric intuition before any differential equations.

| Script | What you learn |
|--------|---------------|
| `magnetization_vector_3d.py` | M lives in 3D space; Mz is along B₀ |
| `multiple_magnetization_vectors.py` | Different spin populations point in different directions |
| `larmor_precession_analytical.py` | Without relaxation, Mx and My oscillate at ω, Mz stays constant |
| `precession_partial_tip.py` | A partial tip (Mz < 1) is the starting point for understanding RF pulses |

---

### Module 02 — RF Pulse Fundamentals

An RF pulse is a time-varying magnetic field B₁(t) applied perpendicular to B₀.
The flip angle it produces is proportional to its integral:

$$\theta = \gamma \int_0^\tau B_1(t)\, dt$$

The RF energy (proportional to SAR, the tissue heating safety limit) is:

$$E \propto \int_0^\tau B_1(t)^2\, dt$$

| Script | What you learn |
|--------|---------------|
| `construct_90deg_square_pulse.py` | How to engineer B₁ and τ to hit exactly 90° |
| `calculate_flip_angle.py` | Numerical integration of pulse area → flip angle |
| `calculate_rf_energy.py` | SAR calculation — the critical safety constraint in MRI |
| `gaussian_flip_angle.py` | Gaussian pulses: same flip angle, lower peak power, less SAR |
| `compare_two_pulses.py` | Two pulses can have equal flip angles but very different SAR |

---

### Module 03 — Bloch ODE Simulations

The full Bloch equations include T₁/T₂ relaxation and require ODE integration:

$$\frac{dM_x}{dt} = \gamma B_0 M_y - \frac{M_x}{T_2}, \quad
\frac{dM_y}{dt} = -\gamma B_0 M_x - \frac{M_y}{T_2}, \quad
\frac{dM_z}{dt} = \frac{M_0 - M_z}{T_1}$$

All scripts use `scipy.integrate.solve_ivp` with the RK45 integrator.

| Script | What you learn |
|--------|---------------|
| `bloch_simulation_basic.py` | Mx, My decay with T₂; Mz recovers with T₁ — simultaneously |
| `bloch_t2_comparison.py` | Shorter T₂ → faster signal loss → less time for MRI readout |
| `magnetization_with_rf_pulse.py` | RF pulse disturbs equilibrium; spin relaxes back afterward |

---

### Module 04 — B1 Robustness Analysis

In clinical MRI, the delivered B₁ field is never perfectly uniform — it varies
with patient anatomy, field strength, and coil geometry. Any miscalibration
directly shifts the flip angle.

| Script | What you learn |
|--------|---------------|
| `b1_amplitude_vs_flip_angle.py` | Linear B₁ → flip angle dependence for conventional pulses |
| `flip_angle_error_analysis.py` | Error quantification: absolute and percentage |
| `conventional_pulse_robustness.py` | ±20% B₁ variation → proportional flip-angle error |
| `conceptual_robustness_comparison.py` | *Conceptual* illustration of what STA robustness looks like |

> **Note on the conceptual comparison:** The STA-like curve in `conceptual_robustness_comparison.py`
> uses illustrative values to show what a robust pulse *should* achieve.
> A physically rigorous STA simulation using counterdiabatic driving and
> the Bloch ODE solver is in the companion repository:
> 👉 [STA-Spin-Dynamics](https://github.com/SuDiptoRoy994/STA-Spin-Dynamics)

---

### Module 05 — Pulse Shape Comparison

Two foundational pulse shapes compared visually — the starting point for
understanding why pulse shape matters for bandwidth, SAR, and robustness.

| Script | What you learn |
|--------|---------------|
| `square_vs_gaussian_overlay.py` | Shape contrast on one axis |
| `square_vs_gaussian_subplots.py` | Separate panels for clear visual isolation |

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run any script from inside its folder
cd 01_magnetization_basics
python magnetization_vector_3d.py

# Or from the root with full path
python 03_bloch_ode_simulations/bloch_simulation_basic.py
```

Each script saves a PNG figure and prints key numerical values for self-checking.

---

## Bugs Fixed from Original Code

In the interest of transparency, four bugs in the original scripts were corrected:

| Original file | Bug | Fix applied |
|--------------|-----|-------------|
| `Bloch_Equation_Plot_1.py` | Mz legend label said `$M_y$` (duplicate); title said "omega=1" but omega=5 | Label corrected to `$M_z$`; title matches variable |
| `Bloch_equation_plot_2.py` | Same duplicate label bug | Same fix |
| `Problem_2.py` | M3 vector was labelled `M1` in the legend | Corrected to `M3` |
| `Magnetiztion_With_RF_pulses.py` | `axvspan(2, 4)` shaded the wrong region — pulse was defined over t=1 to 6 | Pulse window and shading now both use t=2 to 4 |

---

## Connection to Research

These scripts were written as self-directed preparation for graduate-level research
in MRI physics and quantum control. They establish the physical foundations —
Bloch equations, RF pulse design, and B₁ robustness — that are essential for
understanding **Shortcuts to Adiabaticity (STA)** applied to MRI.

The progression leads directly to:

🔬 **[STA-Spin-Dynamics](https://github.com/SuDiptoRoy994/STA-Spin-Dynamics)**
— Full counterdiabatic driving simulation showing 10× pulse speed-up with maintained inversion fidelity, supporting the review paper *"Can Shortcuts to Adiabaticity Overcome the Speed–Fidelity Trade-off in Neural Stimulation fMRI?"*

---

## Author

**Sudipto Roy**
MSc in Applied Physics and Electronics, Jahangirnagar University, Bangladesh
Research interests: MRI physics, RF pulse design, quantum control, medical physics
📧 diptoroy994@gmail.com | 🐙 [github.com/SuDiptoRoy994](https://github.com/SuDiptoRoy994)

---

## License

MIT — see [LICENSE](LICENSE)
