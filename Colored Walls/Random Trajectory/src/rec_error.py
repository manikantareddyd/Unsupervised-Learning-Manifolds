from PIL import Image
import numpy as np
from sklearn import manifold
import sys
from os import mkdir,remove

train_coords = np.genfromtxt('train_Coords.csv', delimiter=',')
train_Data = []

for i in train_coords:
	for j in range(0,100,3):
		file = 'img/train/'+str(int(i[0]))+'_'+str(int(i[1]))+'_'+str(j)+'.png'
		img = Image.open(file)
		data = (np.array(img)).flatten()
		train_Data.append(data)
		del data
		img.close()

train_Data = np.array(train_Data)

Manifold_3			= 	manifold.Isomap(n_neighbors=10, n_components=int(sys.argv[1]))
Manifold_3.fit(train_Data)

rec_error=Manifold_3.reconstruction_error()
print str(sys.argv[1])+","+str(rec_error)
