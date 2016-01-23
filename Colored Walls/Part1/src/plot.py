import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
import os

LOL = int(sys.argv[1])
if LOL == -5000:
	i=90
else:
	X_cor = float(sys.argv[1])
	Y_cor = float(sys.argv[2])
	NumIter = int(sys.argv[3])
	N_Neighbours = int(sys.argv[4])
	N_Components = int(sys.argv[5])


np.seterr(divide='ignore', invalid='ignore')
if LOL == -5000:
	file = 'Reduced_data/data_Rnd'
else:
	file  = 'Reduced_data/data_'+str(X_cor)+'_'+str(Y_cor)+'_'+str(NumIter)+'_'+str(N_Neighbours)+'_'+str(N_Components)

data = np.genfromtxt(file, delimiter=',',  names=['x', 'y', 'z'])
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(data['x'], data['y'], data['z'], label='Plot of the 3D Embedded Manifold')
ax.legend()
plt.show()