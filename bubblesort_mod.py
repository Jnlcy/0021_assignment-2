
import sys



def bubbleSort(data):
    
    
        
    #bubble sort part
        for i in range(len(data)-1): # go through the list - i in [0..N-1)
            swapped = False #create a flag to show if the sorting i complete
            for j in range(len(data)-1):
                if data[j] > data[j+1]: # if wrong order
                    tmp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = tmp # swap them
                    swapped = True # and set flag to true
            if not swapped:
                break#break the loop when there is no longer changes
        #looking for the smallest value
            smallest = i
            for k in range(i+1,len(data)):
                if data[k] < data[smallest]:
                    smallest = k # just record its position

            print(data[smallest])#printing the nest smallest value

        #insert the minimum value to position 0
            if smallest != i:
                tmp = data[i]
                data[i] = data[smallest] # swap it with element of position i
                data[smallest] = tmp
            print(data)

           
        
        
       
        

def main ():
    
    data=[67,66,44,24,12]

    print("Unsorted data: ")
    print(data)
    print("\n")
    
    bubbleSort(data)
    print(data)
    

    

if __name__ == "__main__":
  main() 

