# 0021_assignment-2
## Part A Hybrid Sort
Hybrid sort will mix both sorting algorithms in such a way that at the end of the first
iteration of the outer loop the smallest element will be found in the first position of the array
(due to Bubble Sort) and the largest element will be stored in the last position of the array
(due to Selection Sort). In the second iteration (of the outer loop), the second smallest
element will be stored in the second position of the array and (due to Bubble Sort) and the
second largest element will be stored in the penultimate position of the array, and so on.

To achieve the behaviour described above, Hybrid Sorts uses the code of Bubble Sort as the
main code and includes a part of Selection Sort in it as follows: whilst Bubble Sort compares
pairs of values in the array to decide whether to swap them or not (inner loop), Hybrid Sort
will use this very same loop to search for the minimum value in the array and store it in the
right position at the end of this inner iteration. Once the minimum value is found, it is
swapped with the number stored in the position where the minimum value should be stored
(that is the Selection Sort part).

The following table shows how the content of an array made of 5 elements **([67, 12, 44, 24,
66])** changes after each iteration of the outer loop (while loop) of Hybrid Sort:
• End of first iteration (while loop): **[12, 44, 24, 66,67]**
Number 67 has been bubbled up, 12 has been selected as the minimum value and
stored in first position
• End of second iteration (while loop): **[12, 24, 44, 66, 67]**
Number 66 has been bubbled up, 24 has been selected as the next minimum value and
stored in second position
• End of third iteration (while loop): **[12, 24, 44, 66, 67]**

## Part B Image Filter
Grayscale images can be stored as 2D arrays. Every element in the array is a pixel with a value
between 0 (black) and 255 (white). The Python code below uses a 2D array to create 2
images, as follows.
- Lines 1-3: Relevant modules are imported. The module matplotlib allows to read and
write image files
- Line 5: A 2D array, called image, of 300x300 elements storing the number 0 is created.
- Line 7: The 2D array image is stored as an image in the file all_black.jpg, thanks to the
method imsave available in matplotlib. The image will look like a black square of
300x300 pixels
- Lines 9-10: The number 255 is stored in the diagonal of the array. Thus, we are adding
a white diagonal line to the original image
- Line 12: The black square with the white diagonal line is stored in file line.jpg

```python
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
```
Image filters are nothing more than operations performed in the data of the array storing the
image. For example, the following code acts as a filter that mixes 3 images:

```python
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
```

Implement the methods removeNoise() and filter1() in the class noisyPattern
shown below:
```python
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
 def removeNoise(self):
 #your code here
 #if there is a white dot, replace its value by the value
 # of the majority of neighbouring pixels
 #save the resulting image in file noise_removed.png

 def filter1(self):
 #your code here
 #replace the value of every pixel by the average of the values
 #of its neighbouring pixels
 #save the resulting image in file pattern_filter1.png
 ```
