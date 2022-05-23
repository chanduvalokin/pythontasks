def descOrder(numList):
    return sorted(numList,reverse=True)

numsList=[]
numLen=int(input("Enter the no of items in list "))
print("Enter list elements")
for num in range(numLen):
    numsList.append(int(input()))

print("Number list in descending order is\n")
print(descOrder(numsList))