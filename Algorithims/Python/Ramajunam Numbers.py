#Finding ramanujam numbers using numbers from range from 1 to N. Example ramajunam in range from 1 to 10 is 
import math

def giveMe(n):

        AllNums = []
        dic = {}
        count = 0

        #Finding all possible cubes added and appending in list as-  list = [cubes added, number1ThatMakes_CubesAdded, number2ThatMakes_cubesAdded, ......]
        for i in range (1,n+1):
                #Range is i to n+1 to avoid half the values created. Example - 1**3 + 2**3 will give same value as 2**3 + 1**3 So the second value is ignored.
                for x in range (i,n+1):
                        num = i**3 + x**3
                        #Appendin num and the numbers that make up num
                        AllNums.append(num)
                        AllNums.append(i)
                        AllNums.append(x)
        
        #Creating dictionary as dict = {key_Is_The_RamajunamNo. : [no.of_Times_Key_Appeared, number1ThatMakes_CubesAdded, number2ThatMakes_cubesAdded,.......]}
        for i in AllNums:
                #All ramajunam numbers are 3rd intervals in AllNums
                #Checking if its the 3rd interval in AllNums
                if (count%3 == 0):
                        try:
                                #Updating the count of element in when key re-appears
                                dic[i][0] += 1
                                #Appending the values that make up the repeated ramajunam number from AllNums list
                                dic[i].append(AllNums[count+1])
                                dic[i].append(AllNums[count+2])
                        except KeyError:
                                #Making a list in the dictionary with i as key- list = [no.of_Times_Key_Appeared, number1ThatMakes_CubesAdded, number2ThatMakes_cubesAdded,.......]
                                dic[i] = [1, AllNums[count+1], AllNums[count+2]]
                #Incrementing the value of count to avoid if command above
                count = count + 1
        count = 0

        #Going through all the keys in the dictionary
        for i in dic.keys():
            #If the No.of_Times_the_key_appeared is more than 2
            if(dic[i][0] >= 2):
                #Print the ramajunam number(the key is dictionary)
                print(i)
                #Print all the number in the list that make up the ramjunam number
                for x in range(1,len(dic[i])):
                    #Print the numbers
                    print(dic[i][x])
                        
                        
#Get input from the user
UpperRange = int(input("Enter the upperRange:"))
#Print numbers that make ramajunam number and the ramajunam number
giveMe(UpperRange)
