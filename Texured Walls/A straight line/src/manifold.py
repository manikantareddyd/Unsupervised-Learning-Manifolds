from PIL import Image
import numpy as np
from sklearn import manifold
import sys
from os import mkdir


LOL = int(sys.argv[1])


if LOL == -5000:
	NumIter=500
else:
	X_int = float(sys.argv[1])
	Y_int = float(sys.argv[2])


images_Data = []
for i in range(0,3600):
	if LOL == -5000:
		file = 'img/POS_Rnd/'+str(i)+'.png'
	else:
		file ='img/('+str(X_int)+')+('+str(Y_int)+')=1'+'/'+str(i)+'.png'
	img = Image.open(file)
	img.load()
	data = (np.array(img)).flatten()
	images_Data.append(data)

images_Data = np.array(images_Data)



try:
	N_Neighbours = int(sys.argv[4])
except:
	print "Number of Neighbours not specified. Assuming 10"
	N_Neighbours = 10

print "Trying to fit a 3d manifold"
Manifold_3			= 	manifold.Isomap(N_Neighbours, 3)
Data_Transform_3	=   Manifold_3.fit_transform(images_Data)

print "Manifolds now Created. Writing to files"


try:
	mkdir('Reduced_data')
	print "Everything seems OK"
except:
	print "Everything seems OK"


if LOL==-5000:
	fold = 'Reduced_data/data_Rnd'
else:
	fold ='Reduced_data/data_'+str(X_int)+'_'+str(Y_int)+'_'+'_'+str(N_Neighbours)


try:
	mkdir(fold)
	print "Everything STILL seems OK"
except:
	print "Everything STILL seems OK"


file3  = fold +'/Dimensions_3.csv'

np.savetxt(file3,Data_Transform_3,delimiter=",")

print "Files have been created"
