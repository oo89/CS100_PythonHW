
#1

def initialLetterCount(wordList):
    returnDic={}
    for word in wordList:
        firstLetter = word[0]
        if firstLetter in returnDic:
            returnDic[firstLetter] += 1
        else:
            returnDic[firstLetter] = 1
    return returnDic

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

#2
def initialLetters(wordList):
    returnDic = {}
    for word in wordList:
        firstLetter = word[0]
        if firstLetter in returnDic:
            if any(word in val for val in returnDic.values()): #this checks if the value for the key is already on the dic
                continue
            else:
                returnDic[firstLetter].append(word)
        else:
            returnDic[firstLetter] = [word]
    return returnDic

#on this problem, they do not specify if a lower case letter will
#be the same as a capital letter; that is why I didn't check that.



horton = ['I', 'say', 'what', 'a', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'Itest', 'Has', 'me','Me']
print(initialLetters(horton))

#3
#OJO
def shareALetter(wordList):
    returnDic = {}
    for word in wordList:
        if word in returnDic:
            continue
        else:
            listWord = []
            for letter in word:
                for word2 in wordList:
                    if letter in word2 and word2 not in listWord:
                        listWord.append(word2)
            returnDic[word] = listWord
    return returnDic
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'o','ao']
print(shareALetter(horton))





