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
    def _arrayDimension(self,i,j):
        image = self.image
        if i==0:
            if j==0:
                testArray = np.array([[image[i,j],image[i+1,j]],[image[i,j+1], image[i+1,j+1]]])
            else:
                testArray = np.array([[image[i,j-1],image[i,j],image[i,j+1]],[image[i+1,j-1],image[i+1,j],image[i+1,j+1]]])
        elif j ==0:
            testArray = np.array([[image[i-1,j],image[i-1,j+1]],[image[i,j],image[i,j+1]],[image[i+1,j],image[i+1,j+1]]])
        elif i==79:
            if j==79:
                testArray = np.array([[image[i-1,j-1],image[i,j-1]],[image[i-1,j], image[i,j]]])
            else:
                testArray = np.array([[image[i-1,j-1],image[i-1,j],image[i-1,j+1]],[image[i,j-1],image[i,j],image[i,j+1]]])

        elif j ==79:
            testArray = np.array([[image[i-1,j-1],image[i-1,j]],[image[i,j-1],image[i,j]],[image[i+1,j-1],image[i+1,j]]])

        else:
            testArray = np.array([[image[i-1,j-1],image[i-1,j],image[i-1,j+1]],[image[i,j-1],image[i,j],image[i,j+1]],[image[i+1,j-1],image[i+1,j],image[i+1,j+1]]])
        
        return testArray

    #a function to decide whether remove the white pixel or not
    def _removeDecision(self,i,j):
        testArray = self._arrayDimension(i,j)
   
        k=0
        for m in range(0,testArray.shape[0]):
            for n in range(0,testArray.shape[1]):
                if testArray[m,n] == 0:
                    k+=1

        if k>=4:
            return True
        else:
            return False



    def removeNoise(self):
        
        for i in range(0,self.image.shape[0]):
            for j in range(0,self.image.shape[1]):
                if self.image[i,j]==255:
                    remove=self._removeDecision(i,j)
                    if remove == True:
                        self.image[i,j]=0
        plt.imsave('filtered.png', self.image, cmap=plt.cm.gray)
        
        #if there is a white dot, replace its value by the value
        # of the majority of neighbouring pixels
        #save the resulting image in file noise_removed.png

    #def filter1(self):
        #replace the value of every pixel by the average of the values
        #of its neighbouring pixels
        #save the resulting image in file pattern_filter1.png

def main():
    pattern = noisyPattern()
    pattern.setLines()
    pattern.addNoise()
    pattern.removeNoise()


if __name__ == "__main__":
    main() 