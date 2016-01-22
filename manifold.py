from PIL import Image
import numpy as np
from sklearn import manifold
import sys
import os

X_cor = float(sys.argv[1])
Y_cor = float(sys.argv[2])
NumIter = int(sys.argv[3])

images_Data = []
for i in range(1,NumIter):
	file = 'img/POS_'+str(X_cor)+'_'+str(Y_cor)+'/'+str(i)+'.png'
	img = Image.open(file)
	img.load()
	data = (np.array(img)).flatten()
	images_Data.append(data)

images_Data = np.array(images_Data)

N_Neighbours = int(sys.argv[4])
N_Components = int(sys.argv[5])

Manifold_Transform  = manifold.Isomap(N_Neighbours, N_Components).fit_transform(images_Data)

np.savetxt("file.csv",Manifold_Transform,delimiter=",")