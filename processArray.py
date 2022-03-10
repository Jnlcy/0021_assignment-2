import numpy as np
class processArray:

    def __init__(self,size):
        self.size=2
        self.setSize(size)
        self.numbers=np.random.random([self.size])*100
        self.numbers=self.numbers.round(0)
        
    def __str__(self):
        return "Array of "+str(self.size)+" numbers"+"\n"+str(self.numbers)

    def setSize(self,size):
        if(size>=2):
            self.size=size

    def hybridSort(self):
        #bubble sort part
        data = self.numbers
        for i in range(len(data)-1): # go through the list - i in [0..N-1)
            swapped = False #create a flag to show if the sorting i complete
            for j in range(len(data)-1):
                if data[j] > data[j+1]: # if wrong order
                    tmp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = tmp # swap them
                    swapped = True # and set flag to true
            if not swapped:
                print("Sorting completed")
                break#break the loop when there is no longer changes
        #looking for the smallest value
            smallest = i
            for k in range(i+1,len(data)):
                if data[k] < data[smallest]:
                    smallest = k # just record its position

            #print(data[smallest])#printing the nest smallest value

        #insert the minimum value to pslosition 0
            if smallest != i:
                tmp = data[i]
                data[i] = data[smallest] # swap it with element of position i
                data[smallest] = tmp
            print("After the ",i+1,"st iteration:")
            print(data)
            

