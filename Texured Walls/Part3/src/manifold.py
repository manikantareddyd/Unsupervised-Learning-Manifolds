from PIL import Image
import numpy as np
from sklearn import manifold
import sys
from os import mkdir,remove

print "Reading Images of Training Set"
train_coords = np.genfromtxt('train_Coords.csv', delimiter=',')
train_Data = []

for i in train_coords:
	for j in range(0,100):
		file = 'img/train/'+str(int(i[0]))+'_'+str(int(i[1]))+'_'+str(j)+'.png'
		img = Image.open(file)
		data = (np.array(img)).flatten()
		train_Data.append(data)
		del data
		img.close()

train_Data = np.array(train_Data)

print "Traning Images read"

try:
	N_Neighbours = int(sys.argv[1])
except:
	print "Number of Neighbours not specified. Assuming 5"
	N_Neighbours = 5


print "Trying to fit a 3d manifold"
Manifold_3			= 	manifold.Isomap(N_Neighbours, 3)
Data_Transform_3	=   Manifold_3.fit_transform(train_Data)
print "Manifolds now Created. Writing to files"

try:
	mkdir('Reduced_data')
	print "Everything seems OK"
except:
	print "Everything seems OK"

file3  = 'Reduced_data/train.csv'

np.savetxt(file3,Data_Transform_3,delimiter=",")

print "Files have been created\n"

print "Reading test Images"

test_coords = np.genfromtxt('test_Coords.csv', delimiter=',')
test_data = []
for i in test_coords:
		file = 'img/test/'+str(int(i[0]))+'_'+str(int(i[1]))+'_'+str(int(i[2]))+'.png'
		img = Image.open(file)
		data = (np.array(img)).flatten()
		test_data.append(data)
		del data
		img.close()

test_data = np.array(test_data)


print "Now estimating reduced coordinates of random data"

Rand_Data_Transform = Manifold_3.transform(test_data)

print "Printing Estimated reduced coordinates to file"
np.savetxt('Reduced_data/test.csv',Rand_Data_Transform,delimiter=",")