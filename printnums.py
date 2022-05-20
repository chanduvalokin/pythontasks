def multiplesOfNumber(num1,num2,num):
    sum=0
    for n in range(num1,num2+1):
        if n%num==0:
            print(n)
            sum=sum+n
    print(f"Sum of multiples of {num} b/w 1-20 is {sum}\n")

print("Multiples of 2 b/w 1-20 are ")
multiplesOfNumber(1,20,2)

print("Multiples of 3 b/w 1-20 are ")
multiplesOfNumber(1,20,3)