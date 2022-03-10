import numpy as np
import random
import matplotlib.pyplot as plt
#creating a black square of 300x300 pixels
image=np.zeros([300,300])
#saving black square to png file
plt.imsave('all_black.jpg', image, cmap=plt.cm.gray)
#drawing a white diagonal
for i in range(0,300):
 image[i,i]=255

#saving png file
plt.imsave('line.jpg', image, cmap=plt.cm.gray)