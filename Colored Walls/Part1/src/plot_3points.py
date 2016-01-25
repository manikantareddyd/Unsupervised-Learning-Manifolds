import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import numpy as np
import sys
from os import mkdir



np.seterr(divide='ignore', invalid='ignore')




file3  = 'Reduced_data/data_3points/Dimensions_3-test.csv'

data3 = np.genfromtxt(file3, delimiter=',',  names=['x', 'y', 'z'])
print "Data Loaded"



fig = plt.figure()
ax = fig.add_subplot(2,2,1)
ax.scatter(data3['x'], data3['y'])
ax.set_title('XY projection')
ax = fig.add_subplot(2,2,2)
ax.scatter(data3['y'], data3['z'])
ax.set_title('YZ projection')
ax = fig.add_subplot(2,2,3)
ax.scatter(data3['z'], data3['x'])
ax.set_title('ZX projection')
ax = fig.add_subplot(2,2,4,projection='3d')
ax.scatter(data3['x'], data3['y'],data3['z'])
ax.set_title('3D Manifold')
fig.savefig('3points-test.png')
plt.show()


