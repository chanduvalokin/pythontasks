text=input("Enter the text")
textList=text.split()
wordCount={}
for word in textList:
    wordCount[word]=textList.count(word)

print("\nWord Count in the text")
print(wordCount)

countList=list(wordCount.values())
maxCount=max(countList)
countList.remove(maxCount)
secondMaxCount=max(countList)
countList.remove(secondMaxCount)
thirdMaxCount=max(countList)

mostCommonWords={}
for key in wordCount.keys():
    if wordCount[key]==maxCount:
        mostCommonWords[key]=maxCount
    elif wordCount[key]==secondMaxCount:
        mostCommonWords[key]=secondMaxCount
    elif wordCount[key]==thirdMaxCount:
        mostCommonWords[key]=thirdMaxCount
    

print("\n 3 Most common words are")
print(mostCommonWords)

    