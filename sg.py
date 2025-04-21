#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 14:21:33 2025

@author: miguelaresta
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

np.random.seed(0)
x = np.linspace(0, 2 * np.pi, 100)
y = (np.sin(x)*np.exp(x) )+ 140*np.random.normal(0, 0.1, x.size)


window_size = 40

poly_order = 3
y_smooth = savgol_filter(y, window_size, poly_order, deriv = 0)

plt.scatter(x, y, label='Noisy Signal',alpha = 0.6)
plt.plot(x, y_smooth, label='Smoothed Signal', color='red')
plt.grid(lw=2,ls=':')
plt.xlabel('Time Step')
plt.ylabel("Value")
plt.legend()
plt.show()