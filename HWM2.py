
"""
Problem 1 
Answer: b 

Problem 2 
Answer: b 

Problem 3 
Answer: c

Problem 4 
Answer a

Problem 5 
Answer: e 
Error out of range 

Problem 6
Answer: d

Problem 7 
Answer: a

Problem 8 
Answer: d

Problem 9 
Answer: b

Problem 10 
Answer: c
"""
# Problem 11, 12, 13

import turtle
def drawSquare(t, length):
    t.pendown()
    for i in range(4):
        t.forward(length)
        t.right(90)


t = turtle.Turtle()
drawSquare(t, 100)

def offsetSquares(t, length, num, x0offset, y0offset ):
    for i in range(num):
        drawSquare(t,length)
        t.penup()
        t.forward(x0offset)
        t.right(90)
        t.forward(y0offset)
        t.left(90)


offsetSquares(t, 100, 4, 20, 10)


def indexByLength(s):
    d = {}
    for word in s.split():
        listToAppend = []
        for word2 in s.split():
            if len(word) == len(word2) and word2 not in listToAppend:
                listToAppend.append(word2)
                d[len(word)] = listToAppend #remember that i can do d[].append(word) porque ya sabe que es una lista
            else:
                continue
    return d
#ojo list(set(worda)) set convierte una lista en un set que solo tiene items no
# repetidos y despues se convierte de nuevo en una lista
#words is a list

text = 'I was indecisive but now I am not too sure'
print(indexByLength(text))

def cloneLines(inFile,outfile):
    inF = open(inFile,'r')
    outF = open(outfile,'w')
    for line in inF:
        words = line.split()
        #you can use here set  (si creas una lista con uniques words using set entonces
        # despues puedes check si unique es menor que el otro entonces si es menor
        # entonces es que le quitaste algo y la usas )
        for word in words:
            if words.count(word) > 1:
                outF.write(line)
                break
    inF.close()
    outF.close()
cloneLines('william.txt', 'clones.txt')


