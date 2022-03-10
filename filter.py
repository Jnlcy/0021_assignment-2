import numpy as np
import random
import matplotlib.pyplot as plt
#creating a black square with a white diagonal
image1=np.zeros([300,300])
for i in range(0,300):
    image1[i,i]=255
plt.imsave('diag.png', image1, cmap=plt.cm.gray)
#creating a black square with a smaller square in it
image2=np.zeros([300,300])
for i in range(100,200):
    for j in range(100,200):
        image2[i,j]=255
plt.imsave('square.png', image2, cmap=plt.cm.gray)

#creating a black square with a "reverse" white diagonal
image3=np.zeros([300,300])
for i in range(0,300):
    image3[i,299-i]=255
plt.imsave('rev_diag.png', image3, cmap=plt.cm.gray)
#extracting 1/3 of each image and adding it in image 4
image4=np.zeros([300,300])
for j in range(0,100):
    image4[:,j]=image1[:,j]
for j in range(100,200):
    image4[:,j]=image2[:,j]
for j in range(200,300):
    image4[:,j]=image3[:,j]
plt.imsave('merge.png', image4, cmap=plt.cm.gray)