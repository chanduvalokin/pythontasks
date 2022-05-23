numList=[]
numLen=int(input("Enter the no of items in list "))
print("Enter list elements")
for num in range(numLen):
    numList.append(int(input()))

print("Nos divisible by 5 are \n")

for num in numList:
    if num%5 == 0:
        print(num)