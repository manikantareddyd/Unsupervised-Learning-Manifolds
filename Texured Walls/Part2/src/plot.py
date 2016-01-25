import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
from os import mkdir

LOL = int(sys.argv[1])
if LOL == -5000:
	i=90
	X_int = 'Random'
	Y_int = 'Random'
else:
	X_int = float(sys.argv[1])
	Y_int = float(sys.argv[2])
	NumIter = 3600
	try:
		N_Neighbours = int(sys.argv[4])
	except:
		N_Neighbours = 10

np.seterr(divide='ignore', invalid='ignore')

if LOL==-5000:
	fold = 'Reduced_data/data_Rnd'
else:
	fold ='Reduced_data/data_'+str(X_int)+'_'+str(Y_int)+'_'+'_'+str(N_Neighbours)


file3  = fold +'/Dimensions_3.csv'

data3 = np.genfromtxt(file3, delimiter=',',  names=['x', 'y', 'z'])

print "Data Loaded"



try:
	mkdir('Plots')
	print "Everything seems OK. Folder Plots Created"
except:
	print "Everything seems OK"

if LOL==-5000:
	fold = 'Plots/Plot_Rnd'
else:
	fold ='Plots/Plot_'+str(X_int)+'_'+str(Y_int)+'_'+str(NumIter)+'_'+str(N_Neighbours)

try:
	mkdir(fold)
	print "Everything STILL seems OK. Directory"
except:
	print "Everything STILL seems OK"


file  = fold +'/Plot_.png'

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
fig.savefig(file+'All.png')