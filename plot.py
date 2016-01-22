import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
import os
np.seterr(divide='ignore', invalid='ignore')
data = np.genfromtxt('file.csv', delimiter=',',  names=['x', 'y', 'z'])

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(data['x'], data['y'], data['z'], label='Plot of the 3D Embedded Manifold')
ax.legend()
plt.show()