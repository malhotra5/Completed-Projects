#Reverse an array

#Method1 - 2 arrays
def reverseArrM1(arr):
    #Number of objects in array
    count = len(arr)
    finalList = []
    count = count -1
    #Taking elements from the back of arr and putting it in final list
    for x in range(len(arr)):
        finalList.append(arr[count])
        count = count - 1
    return finalList

#Method2 - 1 array
def reverseArrM2(arr):
    count = len(arr)
    count = count -1
    ##Taking elements from the back of arr and putting it in the same list
    for x in range(len(arr)):
        arr.append(arr[count-x])
    #Deleting all the orignal elements in list
    for x in range(count+1):
        del arr[0]

    return (arr)
       
ex = [2,3,4,5,6,7]

reverseArrM2(ex)
