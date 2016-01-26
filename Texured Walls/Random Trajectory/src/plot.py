import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import numpy as np
import sys
from os import mkdir



np.seterr(divide='ignore', invalid='ignore')

file1 = 'Reduced_data/train.csv'
file2 = 'Reduced_data/test.csv'
data1 = np.genfromtxt(file1, delimiter=',',  names=['x', 'y', 'z'])
data2 = np.genfromtxt(file2, delimiter=',',  names=['x', 'y', 'z'])
 
print "Data Loaded"



try:
	mkdir('Plots')
	print "Everything seems OK. Folder Plots Created"
except:
	print "Everything seems OK"


file  = 'Plots'


# fig = plt.figure()
# gs = gridspec.GridSpec(2, 2)
# a1=plt.scatter(data3['x'], data3['y'], label='Plot of the XY projection 3D Embedded Manifold'+' X='+str(X_cor)+' Y='+str(Y_cor))
# a1=plt.subplot(gs[0, 0])
# a2=plt.scatter(data3['y'], data3['z'], label='Plot of the YZ projection 3D Embedded Manifold'+' X='+str(X_cor)+' Y='+str(Y_cor))
# a2=plt.subplot(gs[0, 1])
# a3=plt.scatter(data3['z'], data3['x'], label='Plot of the ZX projection 3D Embedded Manifold'+' X='+str(X_cor)+' Y='+str(Y_cor))
# a3=plt.subplot(gs[1, 0])
# a4 = fig.gca(projection='3d')
# a4.scatter(data3['x'], data3['y'], data3['z'], label='Plot of the 3D Embedded Manifold'+' X='+str(X_cor)+' Y='+str(Y_cor))
# a4 = plt.subplot(gs[1, 1])
# fig.add_subplot(a1)
# fig.add_subplot(a2)
# fig.add_subplot(a3)
# fig.add_subplot(a4)ction='3d'
# fig.savefig(file+'3D.png')

fig = plt.figure()
ax = fig.add_subplot(2,2,1)
ax.scatter(data1['x'], data1['y'])
ax.set_title('XY projection')
ax = fig.add_subplot(2,2,2)
ax.scatter(data1['y'], data1['z'])
ax.set_title('YZ projection')
ax = fig.add_subplot(2,2,3)
ax.scatter(data1['z'], data1['x'])
ax.set_title('ZX projection')
ax = fig.add_subplot(2,2,4,projection='3d')
ax.scatter(data1['x'], data1['y'],data1['z'])
ax.set_title('3D Manifold')
fig.savefig(file+'/train.png')

fig1 = plt.figure()
ax = fig1.add_subplot(2,2,1)
ax.scatter(data2['x'], data2['y'])
ax.set_title('XY projection')
ax = fig1.add_subplot(2,2,2)
ax.scatter(data2['y'], data2['z'])
ax.set_title('YZ projection')
ax = fig1.add_subplot(2,2,3)
ax.scatter(data2['z'], data2['x'])
ax.set_title('ZX projection')
ax = fig1.add_subplot(2,2,4,projection='3d')
ax.scatter(data2['x'], data2['y'],data2['z'])
ax.set_title('3D Manifold')
fig1.savefig(file+'/test.png')

plt.show()