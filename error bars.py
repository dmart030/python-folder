# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:59:48 2016

@author: D
"""

import numpy as np
import matplotlib.pyplot as plt

# example data
x = (1,10,1000,10000)
y = (0,1.92*100000000000000000000000,1.47/100000000000000000000,1.465/10000000000000000000)

# example variable error bar values
yerr = (0, 0.78/100000000000000000000000, 0.85/1000000000000000000000,0.91/100000000000000000000)

# First illustrate basic pyplot interface, using defaults where possible.
plt.figure()
plt.errorbar(x, y, yerr=0.4)
plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")
'''
# Now switch to a more OO interface to exercise more features.
fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
ax = axs[0,0]
ax.errorbar(x, y, yerr=yerr, fmt='o')
ax.set_title('Vert. symmetric')

# With 4 subplots, reduce the number of axis ticks to avoid crowding.
ax.locator_params(nbins=17)

ax = axs[0,1]
ax.errorbar(x, y, xerr=xerr, fmt='o')
ax.set_title('Hor. symmetric')

ax = axs[1,0]
ax.errorbar(x, y, yerr=[yerr, 2*yerr], xerr=[xerr, 2*xerr], fmt='--o')
ax.set_title('H, V asymmetric')

ax = axs[1,1]
ax.set_yscale('log')
# Here we have to be careful to keep all y values positive:
ylower = np.maximum(1e-2, y - yerr)
yerr_lower = y - ylower

ax.errorbar(x, y, yerr=[yerr_lower, 2*yerr], xerr=xerr,
            fmt='o', ecolor='g', capthick=2)
ax.set_title('Mixed sym., log y')

fig.suptitle('Variable errorbars')

plt.show()
'''
