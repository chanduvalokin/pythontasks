text = input('Enter a string: ')
wordlist= text.split()

word = input('Enter a word to delete: ')

if word not in wordlist:
    print(f"Word {word} is not present in string")
    print()

else:
    for element in wordlist:
        if element== word:

            wordlist.remove(word)

text = ' '.join(wordlist)
print('String after deletion:',text)
