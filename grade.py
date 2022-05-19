mark1=int(input("enter the mark of 1st subject "))
mark2=int(input("enter the mark of 2nd subject "))
mark3=int(input("enter the mark of 3rd subject "))
mark4=int(input("enter the mark of 4th subject "))
mark5=int(input("enter the mark of 5th subject "))
mark6=int(input("enter the mark of 6th subject "))

avgMark=(mark1+mark2+mark3+mark4+mark5+mark6)/6
totalMark=mark1+mark2+mark3+mark4+mark5+mark6
print(f"Total Mark={totalMark},\nAvg Mark={avgMark}")
if avgMark>90:
    print("Grade:A+")
elif avgMark>80:
    print("Grade:A")
elif avgMark>70:
    print("Grade:B+")
elif avgMark>60:
    print("Grade:B")
elif avgMark>50:
    print("Grade:C+")
elif avgMark>40:
    print("Grade:C")
else:
    print("Grade:fail")