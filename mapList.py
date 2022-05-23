numList=range(1,10)
squareNumList=[]
for num in numList:
    squareNumList.append(num**2)

mapDict=dict()
for index in range (len(numList)):
    mapDict[numList[index]]=squareNumList[index]

print("\nmapped dictionary of numlist and numsquarelist is")
print(mapDict)
