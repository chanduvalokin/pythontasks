numItems=int(input("Enter the no of items buying: "))
if numItems < 10:
    totalCost=numItems*12
    print(f"Total cost of all items={totalCost}")
elif numItems >= 10 and numItems <= 99:
    totalCost=numItems*10
    print(f"Total cost of all items={totalCost}")
elif numItems >= 100:
    totalCost=numItems*7
    print(f"Total cost of all items={totalCost}")