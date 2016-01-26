from PIL import Image
import numpy as np
from sklearn import manifold
import sys
from os import mkdir

images_Data = []
for i in range(0,500):
	file = 'img/POS_100.0_150.0/'+str(i)+'.png'
	img = Image.open(file)
	data = (np.array(img)).flatten()
	images_Data.append(data)
	img.close()
	file = 'img/POS_-160.0_150.0/'+str(i)+'.png'
	img = Image.open(file)
	data = (np.array(img)).flatten()
	images_Data.append(data)
	img.close()
	file = 'img/POS_140.0_-150.0/'+str(i)+'.png'
	img = Image.open(file)
	data = (np.array(img)).flatten()
	images_Data.append(data)
	img.close()
	file = 'img/POS_-140.0_-150.0/'+str(i)+'.png'
	img = Image.open(file)
	data = (np.array(img)).flatten()
	images_Data.append(data)
	img.close()
	del data

images_Data = np.array(images_Data)
Manifold_3			= 	manifold.Isomap(n_neighbors=10, n_components=int(sys.argv[1]))
Manifold_3.fit(images_Data)
rec_error=Manifold_3.reconstruction_error()

print str(sys.argv[1]),',',str(rec_error)