import numpy as np
import random
import matplotlib.pyplot as plt

class noisyPattern:
    def __init__(self):
        self.image=np.full([80,80],255)
        self.setLines()
    def setLines(self):
        self.image[:,0:16]=0
        self.image[:,32:48]=0
        self.image[:,64:80]=0
        plt.imsave('lines.png', self.image, cmap=plt.cm.gray)
    def addNoise(self):
        noise=0.05
        for i in range (0,self.image.shape[0]):
            for j in range(0,self.image.shape[1]):
                if(noise > random.random()):
                    self.image[i,j]=255
        plt.imsave('noisy_pattern.png', self.image, cmap=plt.cm.gray)

# The function to consider boundary conditions
    def _extendPixel(self):
        image_new = np.full([82,82],50)
        for i in range(1,81):
            for j in range(1,81):
                image_new[i,j]=self.image[i-1,j-1]
        return image_new
        

    def _removeBoundary(self,image_new):
        image_old = np.full([80,80],255)
        for i in range(0,80):
            for j in range(0,80):
                image_old[i,j]=image_new[i+1,j+1]

        return image_old

    #a function to decide whether remove the white pixel or not
    def _removeDecision(self,i,j,image):
       
        k=0
        for m in [i-1,i,i+1]:
            for n in [j-1,j,j+1]:
                #count when the pixel is black
                if image[m,n] == 0:
                    k+=1
        #if the majority is black return true,turn the white pixel into black
        if k>=4:
            return True
        else:
            return False


    #removes most noise at edges and all noise in the middle
    def removeNoise(self):
        
        image=self._extendPixel()
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                if image[i,j]==255:
                    remove=self._removeDecision(i,j,image)
                    if remove == True:
                        image[i,j]=0
        self.image = self._removeBoundary(image)
        plt.imsave('noise_removed.png', self.image, cmap=plt.cm.gray)
        
        #if there is a white dot, replace its value by the value
        # of the majority of neighbouring pixels
        #save the resulting image in file noise_removed.png

    def _mean(self,i,j,image_new):
       
        sum = 0
        for m in [i-1,i,i+1]:
            for n in [j-1,j,j+1]:

                sum =sum+image_new[m,n]
        return sum/8

    def filter1(self):
        #replace the value of every pixel by the average of the values
        #of its neighbouring pixels
        #save the resulting image in file pattern_filter1.png
        image_new=self._extendPixel()
        for i in range(1,image_new.shape[0]-1):
            for j in range(1,image_new.shape[1]-1):
                image_new[i,j]=self._mean(i,j,image_new)
        image_new = self._removeBoundary(image_new)
        plt.imsave('pattern_filter1.png',image_new, cmap=plt.cm.gray)


