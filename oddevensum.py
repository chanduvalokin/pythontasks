def evenSum(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        if i%2==0:
            sum=sum+i
    return sum

def oddSum(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        if i%2!=0:
            sum=sum+i
    return sum

print("sum of even numbers between 15 and 35")
print(evenSum(15,35))

print("sum of odd numbers between 15 and 35")
print(oddSum(15,35))

