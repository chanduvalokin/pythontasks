string=input("Enter a String")
from itertools import permutations
anagrams=permutations(string)
for i in list(anagrams):
    print(''.join(list(i)))