#1
def file_copy(in_file, out_file):
    inFile = open(in_file,'r')
    outFile = open(out_file,'w')
    for line in inFile:
        outFile.write(line)
    outFile.close()
    inFile.close()

file_copy('first.txt','copy')
copy_f = open('copy')
print(copy_f.read())

#2
def file_stats(in_file):
    inFile = open(in_file,'r')
    counterLines = 0
    counterWords = 0
    counterChars = 0
    for line in inFile:
        counterLines += 1
        wordsList = line.split()
        counterWords += len(wordsList)
        for current_word in wordsList:
            counterChars+= len(current_word)
    print("Number of lines: " + str(counterLines))
    print("Number of Words: " + str(counterWords))
    print("Number of Chars: " + str(counterChars))
file_stats('second.txt')

#3
def repeat_words(in_file, out_file):
    inFile = open(in_file, 'r')
    outFile = open(out_file, 'w')
    for line in inFile:
        wordDict=[]
        duplicates =[]
        wordsD = line.split()
        for word in wordsD:
            wordClean = word.strip(' .!?,').lower()
            if wordClean in wordDict :
                if wordClean not in duplicates:
                    duplicates.append(wordClean)
                else:
                    continue
            else:
                wordDict.append(wordClean)
        if duplicates == []:
            continue
        else:
            outFile.write(" ".join(duplicates))
            outFile.write('\n')
    inFile.close()
    outFile.close()

inF = 'thirdin.txt'
outF = 'thirdout.txt'
repeat_words(inF,outF)





            



