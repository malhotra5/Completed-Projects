#Make users guess random computer generated numbers
import random
#Generate random number
num = random.randint(0,100)
print('Guess your number:')

while True:
    #Get value from user
    __value__ = int(input('Enter your value'))

    #Check if value is less than computer generated number
    if __value__ < num:
         print("It's a bigger number")

    #Check if value is greater than computer generated number
    elif __value__ > num:
        print("It's a smaller number")

    #Check if value is computer generated number
    elif __value__ == num:
        print("YOU GOT IT RIGHT!")
        break
