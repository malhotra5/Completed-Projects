inFile = open("shuffle.in", "r")
allLines = []
totalVal = []
changeOrder = []
nums = []
count = 0
number = 0
rand = []
q = 0
#Getting values from file
for val in inFile.read().splitlines():
    allLines.append(val)

changeOrder.append(allLines[1])
nums.append(allLines[2])
inFile.close()

changeOrder[0] = changeOrder[0].split()
nums[0] = nums[0].split()

#Taking all values and putting it into a different list
for i in changeOrder[0]:
    for x in i:
            changeOrder.append(x)

for i in nums[0]:
    nums.append(i)
del nums[0]
del changeOrder[0]

end1 = [0,0,0,0,0]
end2 = [0,0,0,0,0]
end3 = [0,0,0,0,0]
#Swapping the order
def swapOrder(nums, end):
    for i in changeOrder:
        q = changeOrder.index(i)
        end[q] = nums[int(i)-1]

swapOrder(nums, end1)
swapOrder(end1, end2)
swapOrder(end2, end3)
#Writing output into file
file = open("shuffle.out", "w")
file.write(str(end3))
file.close()
