def findMultSum(rang):
    nums = []
    for i in range(rang):
        if(i%3 == 0 or i%5 == 0):
            if i in nums:
                pass
            else:
                nums.append(i)
    sumed = 0
    for i in nums:
        sumed = sumed + i
    return sumed


print(findMultSum(1000))
    
