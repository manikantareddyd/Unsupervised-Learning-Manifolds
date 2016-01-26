import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import numpy as np
import sys
from os import mkdir

LOL = int(sys.argv[1])
if LOL == -5000:
	i=90
	X_cor = 'Random'
	Y_cor = 'Random'
else:
	X_cor = float(sys.argv[1])
	Y_cor = float(sys.argv[2])
	NumIter = 500
	try:
		N_Neighbours = int(sys.argv[4])
	except:
		N_Neighbours = 10

np.seterr(divide='ignore', invalid='ignore')

if LOL==-5000:
	fold = 'Reduced_data/data_Rnd'
else:
	fold ='Reduced_data/data_'+str(X_cor)+'_'+str(Y_cor)+'_'+str(NumIter)+'_'+str(N_Neighbours)

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
	fold ='Plots/Plot_'+str(X_cor)+'_'+str(Y_cor)+'_'+str(NumIter)+'_'+str(N_Neighbours)

try:
	mkdir(fold)
	print "Everything STILL seems OK. Directory"
except:
	print "Everything STILL seems OK"


file  = fold +'/Plot_'


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
plt.scatter(data3['x'], data3['y'],label="XY Projection")
fig.savefig(file+'0_0_XY.png')

fig = plt.figure()
plt.scatter(data3['y'], data3['z'],label="YZ Projection")
fig.savefig(file+'0_0_YZ.png')

fig = plt.figure()
plt.scatter(data3['z'], data3['x'],label="ZX Projection")

fig.savefig(file+'0_0_ZX.png')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(data3['x'], data3['y'],data3['z'],label="3D")

fig.savefig(file+'0_0_All.png')


