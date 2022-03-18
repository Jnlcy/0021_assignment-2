from processArray import processArray


#a function to get random integer from key board
def getNumfromKeyborad():
    
    print("Please enter the number of random elements in the array")
    gotNDataCorrectly = False # a flag to loop until we get ndata correctly
    while gotNDataCorrectly == False:
        try:
            n=int(input())
            if n>0:
                gotNDataCorrectly =True
            else:
                print("Please enter positive values")
        except(NameError, SyntaxError,ValueError):
            print("Number of elements should be interger")
    return n

#main function
def main():
    n=getNumfromKeyborad()
    array = processArray(n)
    print(str(array)+"\n")
    array.hybridSort()

if __name__ == "__main__":
    main() 