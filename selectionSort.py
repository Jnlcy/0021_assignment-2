import sys



def selectionSort (data):
# go through the list - i in [0..N-1)
    for i in range (len(data)-1):
        largest= i # initialised to first index of remaining list
# loop to find smallest element in [i+1..N)
        for j in range(i+1,len(data)):
            if data[j] > data[largest]:
                largest = j # just record its position
        print(data[largest])
# after the end of the inner loop, check if there is a smaller element
# than position i in the remaining list and, if so, swap with i
        if largest != i:
            tmp = data[i]
            data[i] = data[largest] # swap it with element of position i
            data[largest] = tmp

        print(data)

def main ():
    data = [2,-3,44,9,0]
    

    print("Unsorted data")
    print(data)
    selectionSort(data)
    

    

if __name__ == "__main__":
  main() 

