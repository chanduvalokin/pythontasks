def highestAndLowestScores(scores):
    sortedScore=sorted(scores)
    return(sortedScore[0],sortedScore[len(scores)-1])

def avgScores(scores):
    sum=0
    for score in scores:
        sum=sum+score
    avgScore= sum/len(scores)
    return avgScore

def secondLargestScore(scores):
    nonDuplicateScores=list(set(scores))
    nonDuplicateScores.sort()
    return nonDuplicateScores[-2]

def warning(scores):
    for score in scores:
        if score >= 100:
            return True
    return False

def avgScoreAfterDropping(scores):
    nonDuplicateScores=list(set(scores))
    nonDuplicateScores.sort()
    nonDuplicateScores.pop(0)
    nonDuplicateScores.pop(0)
    print(f"List scores after deleting two lowest scores is {nonDuplicateScores}")
    sum=0
    for score in nonDuplicateScores:
        sum=sum+score
    avgScore=sum/len(nonDuplicateScores)
    return avgScore



testScores = []
print("Enter 10 test scores")
for  i in range(10):
    testScores.append(int(input()))

if warning(testScores):
    print("A value over hundred has been entered")

else:
    print(f"highest and lowest scores are {highestAndLowestScores(testScores)[0]} and {highestAndLowestScores(testScores)[1]}")

    print(f"\nAverage of all scores is {avgScores(testScores)}")

    print(f"\nSecond largest score is {secondLargestScore(testScores)}\n")

    print(f"\nAverage Score after dropping two lowest scores is {avgScoreAfterDropping(testScores)}")