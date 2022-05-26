import re

email=input("Enter your Email")

emailsplit=re.split('@',email)
print("First Part of email is ")
print(emailsplit[0])
