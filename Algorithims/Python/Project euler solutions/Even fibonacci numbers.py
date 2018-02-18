##Problem number 2

#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Solution - 4613732

def findEvenFiboSum():
    #Original starting numbers
    nums = [1,2]
    sumed = 2
    #Assuming that at least 1000 numbers reach values of 4 million
    for i in range(1,1000):
        #Checking if the new fibonacci number exceeds 4 million by adding previous 2 numbers in the list
        if (nums[i-1] + nums[i] > 4000000):
            break
        else:
            #Checking if the new fibonacci number is even 
            if ((nums[i - 1] + nums[i])%2 == 0):
                #If condition is true, add the fibonacci number to the final sum
                sumed = sumed + nums[i -1] + nums[i]
            #Append new fibonacci number in the list
            nums.append(nums[i - 1] + nums[i])
    #Return sum of even fibonacci numbers
    return sumed

#Printing solution
print(findEvenFiboSum())
