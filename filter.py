import numpy as np
import random
import matplotlib.pyplot as plt
#creating a black square with a white diagonal


image1=np.full([80,80],255)
plt.imsave('image1.png', image1, cmap=plt.cm.gray)
image1[:,0:16]=0
image1[:,32:48]=0
image1[:,64:80]=0
plt.imsave('lines.png', image1, cmap=plt.cm.gray)
"""
noise=0.05
for i in range (0,image1.shape[0]):
    for j in range(0,image1.shape[1]):
        if(noise > random.random()):
            image1[i,j]=255
plt.imsave('noisy_pattern.png', image1, cmap=plt.cm.gray)

def test(i,j):
    if i==0&j!=79:
        if j==0:
            testArray = np.array([[image1[i,j],image1[i+1,j]],[image1[i,j+1], image1[i+1,j+1]]])
        else:
            testArray = np.array([[image1[i,j-1],image1[i,j],image1[i,j+1]],[image1[i+1,j-1],image1[i+1,j],image1[i+1,j+1]]])
    elif j ==0&i!=79:
        testArray = np.array([[image1[i-1,j],image1[i-1,j+1]],[image1[i,j],image1[i,j+1]],[image1[i+1,j],image1[i+1,j+1]]])
    elif i==79:
        if j==79:
            testArray = np.array([[image1[i-1,j-1],image1[i,j-1]],[image1[i-1,j], image1[i,j]]])
        else:
            testArray = np.array([[image1[i-1,j-1],image1[i-1,j],image1[i-1,j+1]],[image1[i,j-1],image1[i,j],image1[i,j+1]]])
    elif j ==79:
        testArray = np.array([[image1[i-1,j-1],image1[i-1,j]],[image1[i,j-1],image1[i,j]],[image1[i+1,j-1],image1[i+1,j]]])

    else:
        testArray = np.array([[image1[i-1,j-1],image1[i-1,j],image1[i-1,j+1]],[image1[i,j-1],image1[i,j],image1[i,j+1]],[image1[i+1,j-1],image1[i+1,j],image1[i+1,j+1]]])


    return testArray

def YorN(i,j):
   


    testArray = test(i,j)
   
    k=0
    for m in range(0,testArray.shape[0]):
        for n in range(0,testArray.shape[1]):
            if testArray[m,n] == 0:
                k+=1

    if k>=4:
        return True
    else:
        return False
"""
def mean(i,j):
    sum = 0
    for m in [i-1,i,i+1]:
        for n in [j-1,j,j+1]:

            sum =sum+image1[m,n]
    return sum/8



"""
for i in range(0,image1.shape[0]):
    for j in range(0,image1.shape[1]):
        if image1[i,j]==255:
            remove=YorN(i,j)
            if remove == True:
                image1[i,j]=0
plt.imsave('filtered.png', image1, cmap=plt.cm.gray)
"""

for i in range(1,image1.shape[0]-1):
    for j in range(1,image1.shape[1]-1):
        image1[i,j]=mean(i,j)
            
plt.imsave('filter1.png', image1, cmap=plt.cm.gray)


     



 


