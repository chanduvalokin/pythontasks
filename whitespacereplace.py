
import re
string=input("enter a string")
if ' ' in string:
    print(re.sub(' ', '_', string))
if "_" in string:
    print(re.sub('_', ' ', string))