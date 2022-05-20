vowels=['a','e','i','o','u','A','E','I','O','U']
string=input("Enter the string ")
count=0
for char in string:
    if char in vowels:
        count=count+1
print(f"No of vowels in the string is {count}")