def upperLowerCount(string):
    uppercount=0
    lowercount=0
    for char in string:
        if char.isupper():
           uppercount=uppercount+1
        elif char.islower():
            lowercount=lowercount+1
    return (uppercount,lowercount)

strings=input("Enter the string ")
counts=upperLowerCount(strings)
print(f"No:of uppercase letters is {counts[0]}")
print(f"No:of lowercase letters is {counts[1]}")

        
