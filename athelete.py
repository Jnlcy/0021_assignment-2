
import pandas as pd
import matplotlib.pyplot as plt


def userOption():
    #create a flag to loop until correct input is given
    correctInput = False
    while correctInput == False:   
        try:
            print("Please enter the numbers of the filter you would like to use (e.g. 234 if you want to filter by age,team and year)")
            print("1.Sex\n2.Age\n3.Team\n4.Year\n5.Sport")
            #take input from user
            number = input()
            #store each digit in a list
            option = [int(x) for x in str(number)]
            #check if all inputs are valid
            
            #check if the user enters
            if len(option)>5:
                print("Too many options.")
                raise ValueError
            elif len(option) != len(set(option)):
                print("Please do not enter repeated options.")
                raise ValueError        
            else:
                for y in option:
                    if 1<= y <=5:
                        pass
                    else:
                        print(y,"is a non valid number")
                        raise ValueError
                correctInput = True
                          
        except(ValueError):
            print("Try again")
        
    return option

def filtering(df):
    option = userOption()
    new_df =df
    
    try:
        #ask for further information for the filter
        for x in option:
            if x == 1:
                sex = input("Enter F for Female, M for Male: ")
                temp =new_df[(new_df['Sex']==sex)]

            elif x == 2:
                age = input("Enter age in years: ")
                temp =new_df[(new_df['Age']==int(age))]
                    

            elif x == 3:               
                team = input("Enter the name of team: ")
                temp =new_df[(new_df['Team']==team)]
                    

            elif x == 4:                
                year =input("Enter the year: ")
                temp =new_df[(new_df['Year']==int(year))]
                    

            elif x == 5:
                sport = input("Enter the name of the sport: ")
                temp =new_df[(new_df['Sport']==sport)]

            new_df = temp
           
            
    except(ValueError,TypeError):
        new_df =[]
    #return 0 when error occur
    if len(new_df) == 0:
        return len(new_df),df
    #otherwise return length of the new data frame and the length of the data frame
    else:
        return len(new_df), new_df
    

def plotting(n,df):

    if 0< n <100:#if records found fewer thatn 100, plot scatter graph
        plt.scatter(df['ID'],df['Weight'])
        plt.xlabel('ID of Atheletes') 
        plt.ylabel('Weight (kg)') 
        plt.title(label='Scatter Plot of the Weight of Selected Atheletes',fontsize='16')
        plt.savefig("scatter.png")
        print("File scatter.png saved")

    elif n>= 100:#if records found equal to or more than 100, plot histogram

        plt.hist(df['Weight'],12)
        plt.xlabel('Weight of the Atheletes (kg)') 
        plt.ylabel('Number of records') 
        plt.title(label = "Histogram of the weight of selected Atheletes", fontsize ='16')
        plt.savefig(" hist.png")
        print("File hist.png saved")

    #If the number of rows is equal to 0, no plot is generated


#The program body

df = pd.read_csv("athlete_events.csv")#read csv file and store it as dataframe
records, new_df =filtering(df)

print("\n=======================================")

print(records ,"records")
plotting(records,new_df)

print("=======================================")