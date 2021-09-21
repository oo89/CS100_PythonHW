
#1 a and b
def hasFinalLetter(strList, letters):
    endList = []
    for st in strList:
        for l in letters:
            if st.endswith(l):
               endList.append(st)
    return endList



strList = ["Im Oqm", "Home", "jadsaudhme"]
letters = "me"
print(hasFinalLetter(strList,letters))

strList = ['hdshweR','askjasrtR', 'sdjksder', 'ndfkjde']
letters = "eR"
print(hasFinalLetter(strList,letters))

strList = ['hdshwyu','askjasrtb', 'sdjksdl', 'ndfkjdo']
letters = "er"
print(hasFinalLetter(strList,letters))

#2
def isDivisible(maxInt, twoInts):
    returnList= []
    for i in range(0,maxInt):
        if i % twoInts[0]==0 and i % twoInts[1] == 0:
            returnList.append(i)
    return returnList

maxInt = 50
twoInts = (2, 5)
print(isDivisible(maxInt,twoInts))

maxInt = 0
twoInts = (2, 5)
print(isDivisible(maxInt,twoInts))

maxInt = 100
twoInts = (3, 7)
print(isDivisible(maxInt,twoInts))
