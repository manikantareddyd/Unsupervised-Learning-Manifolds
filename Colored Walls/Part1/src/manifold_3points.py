from PIL import Image
import numpy as np
from sklearn import manifold
import sys
from os import mkdir

images_Data = []
for i in range(0,500):
	file = 'img/POS_100.0_100.0/'+str(i)+'.png'
	img = Image.open(file)
	data = (np.array(img)).flatten()
	images_Data.append(data)
	img.close()
	file = 'img/POS_0.0_0.0/'+str(i)+'.png'
	img = Image.open(file)
	data = (np.array(img)).flatten()
	images_Data.append(data)
	img.close()
	file = 'img/POS_-100.0_0.0/'+str(i)+'.png'
	img = Image.open(file)
	data = (np.array(img)).flatten()
	images_Data.append(data)
	img.close()
	del data

images_Data = np.array(images_Data)

print "Trying to fit a 3d manifold"
Manifold_3			= 	manifold.Isomap(10, 3)
Data_Transform_3	=   Manifold_3.fit_transform(images_Data)

print "Manifolds now Created. Writing to files"

fold = 'Reduced_data/data_3points'

file3  = fold +'/Dimensions_3-test2.csv'

np.savetxt(file3,Data_Transform_3,delimiter=",")

print "Files have been created"
