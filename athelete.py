
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
    print("List of option:",option)
    new_df =df
    
    try:
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

    if len(new_df) == 0:
        return len(new_df),df
    else:
        return len(new_df), new_df
    

def plotting(n,df):
    if 0< n <100:
    
        plt.scatter(df['Weight'],df['ID'],)
        plt.savefig("scatter.png")
        print("File scatter.png saved")
    elif n>= 100:
        plt.hist(df['Weight'],12)
        plt.savefig(" hist.png")
        print("File hist.png saved")





#read csv file and store it as dataframe
df = pd.read_csv("athlete_events.csv")
records, new_df =filtering(df)

print("=======================================")

print(records ,"records")
plotting(records,new_df)

print("=======================================")

   










   


