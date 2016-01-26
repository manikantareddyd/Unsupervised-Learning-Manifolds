import numpy as np
from sklearn.neighbors import NearestNeighbors as NN
train = np.genfromtxt('Reduced_data/train.csv',delimiter=',')
test  = np.genfromtxt('Reduced_data/test.csv',delimiter=',')

neigh = NN(n_neighbors=15,n_jobs=3)
neigh.fit(train)

Indices=neigh.kneighbors(test,n_neighbors=15,return_distance=False)


del test
del train

train_coords = np.genfromtxt('train_Coords.csv',delimiter=',')
test_coords  = np.genfromtxt('test_Coords.csv',delimiter=',')

error_dist=[]
error_theta=[]
error_all = []
for i in range(0,len(test_coords)):
	Actual_neigh=[]
	np.array(Actual_neigh)
	for j in Indices[i]:
		t=j
		tmp=train_coords[t/100]
		Actual_neigh.append([tmp[0],tmp[1],3.6*t%100])
	mean_all		= np.divide(np.sum(Actual_neigh,0),10)
	Actual_all   	= test_coords[i]
	mean_theta		= mean_all[2:]
	Actual_theta	= Actual_all[2:]
	mean_xy			= mean_all[:2]
	Actual_xy		= Actual_all[:2]
	error_all.append(np.linalg.norm(Actual_all-mean_all))
	error_theta.append(np.linalg.norm(Actual_theta-mean_theta))
	error_dist.append(np.linalg.norm(Actual_xy-mean_xy))

print sum(error_all)/1000,sum(error_dist)/1000,sum(error_theta)/1000
