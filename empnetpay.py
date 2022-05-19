empid=input("enter employee id: ")
name=input("Enter the name of employee: ")
basicpay=int(input("Enter the basic pay: "))

if basicpay>=10000:
    hra=basicpay*.15
    da=basicpay*.08
    netpay=basicpay+hra+da
    print(f"HRA of employee {name} is {hra}")
    print(f"DA of employee {name} is {da}")
    print(f"Netpay of employee {name} is Rs {netpay}")

elif basicpay>=5000 and basicpay<10000:
    hra=basicpay*.1
    da=basicpay*.05
    netpay=basicpay+hra+da
    print(f"HRA of employee {name} is {hra}")
    print(f"DA of employee {name} is {da}")
    print(f"Netpay of employee {name} is Rs {netpay}")

elif basicpay<5000:
    hra=basicpay*.05
    da=basicpay*.03
    netpay=basicpay+hra+da
    print(f"HRA of employee {name}is {hra}")
    print(f"DA of employee {name} is {da}")
    print(f"Netpay of employee {name} is Rs {netpay}")