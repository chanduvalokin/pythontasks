orglist=[]
orglen=int(input("Enter no of elements in list "))
for index in range(orglen):
    orglist.append(input())

oddlenlist=[]
for oddindex in range(1,orglen,2):
    oddlenlist.append(orglist[oddindex])

print("\nList of odd index elements are\n")
print(oddlenlist)
