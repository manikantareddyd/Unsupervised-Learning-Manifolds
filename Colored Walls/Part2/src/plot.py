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

file2  = fold +'/Dimensions_2.csv'
file3  = fold +'/Dimensions_3.csv'

data2 = np.genfromtxt(file2, delimiter=',',  names=['x', 'y'])
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


file2  = fold +'/Plot_2.png'
file3  = fold +'/Plot_3.png'

plt.scatter(data3['x'], data3['y'], data3['z'], label='Plot of the 3D Embedded Manifold'+' X='+str(X_int)+' Y='+str(Y_int))
plt.savefig(file2)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(data3['x'], data3['y'], data3['z'], label='Plot of the 3D Embedded Manifold'+' X='+str(X_int)+' Y='+str(Y_int))
ax.legend()
fig.savefig(file3)
plt.show()
