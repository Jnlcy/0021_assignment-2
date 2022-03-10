import sys



def bubbleSort(data):
    
    
    for i in range(len(data)-1): # go through the list - i in [0..N-1)
        swapped = False
        for j in range(len(data)-1):
            if data[j] > data[j+1]: # if wrong order
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp # swap them
                swapped = True # and set flag to true
        if not swapped:
            break
        print(data)



def main ():
    data = [67, 12, 44, 24,66]
    

    print("Unsorted data")
    print(data)
    bubbleSort(data)
  

    

if __name__ == "__main__":
  main() 

