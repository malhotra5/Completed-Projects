#Simulate a dice roll

import random

def roll():
    #Roll a random number
    return random.randint(1,6)

def checkernExec():
    #Ask users if they want to continue or not
    #Get response from users
    inp = input("Do you want to roll or exit")

    #Checker user response
    if (inp == "roll"):
        return None
    if (inp == "exit"):
        exit()

    #If response is not right, repeat this function   
    if (inp != "roll" or inp!= "exit"):
        print("Please enter a valid response")
        checkernExec()
    

while True:
    print(roll())
    checkernExec()
    
    
        
