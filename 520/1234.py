import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = y = z =[]
csv = np.genfromtxt('horizons_results_ssbWRTsuncenter.csv', delimiter=",")
X = csv[:,2]
Y = csv[:,3]
Z = csv[:,4]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X, Y, Z, label='Horizon_results')
ax.legend()
plt.show()
