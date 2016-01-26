import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import numpy as np
import sys
from os import mkdir

data = np.genfromtxt('rec_error_'+str(int(sys.argv[1]))+'p.csv', delimiter=',',  names=['x', 'y'])


fig = plt.figure()
plt.plot(data['x'], data['y'], label='1point rec error')
fig.savefig('rec_error_'+str(int(sys.argv[1]))+'p.png')
plt.show()

