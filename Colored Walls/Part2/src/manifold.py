from PIL import Image
import numpy as np
from sklearn import manifold
import sys
from os import mkdir

LOL = int(sys.argv[1])

if LOL == -5000:
	NumIter=5000
else:
	X_cor = float(sys.argv[1])
	Y_cor = float(sys.argv[2])
	NumIter = int(sys.argv[3])

images_Data = []
for i in range(1,NumIter):
	if LOL == -5000:
		file = 'img/POS_RND/'+str(i)+'.png'
	else:
		file = 'img/POS_'+str(X_cor)+'_'+str(Y_cor)+'/'+str(i)+'.png'
	img = Image.open(file)
	img.load()
	data = (np.array(img)).flatten()
	images_Data.append(data)

images_Data = np.array(images_Data)

try:
	N_Neighbours = int(sys.argv[4])
except:
	N_Neighbours = 10

try:
	N_Components = int(sys.argv[5])
except:
	N_Components = 3

Manifold_Transform  = manifold.Isomap(N_Neighbours, N_Components).fit_transform(images_Data)

try:
	mkdir('Reduced_data')
except:
	print "<Reduced data> already exists. Any data will be over written"

if LOL == -5000:
	file = 'Reduced_data/data_Rnd'
else:
	file  = 'Reduced_data/data_'+str(X_cor)+'_'+str(Y_cor)+'_'+str(NumIter)+'_'+str(N_Neighbours)+'_'+str(N_Components)

np.savetxt(file,Manifold_Transform,delimiter=",")