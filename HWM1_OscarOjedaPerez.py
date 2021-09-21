"""

Oscar Ojeda Perez
CS 100 2019F Section 105
HW M1, October 7, 2019

"""

"""
Problem 1 
Answer: e 

Problem 2 
Answer: a 

Problem 3 
Answer: a 

Problem 4 
Answer d
Correct Answer: e 
Explanation: I forgot that slicing a list would yield anther list, I thought in this case will give me the value on 
the position and the + oparation will be not posible. My learning is that not matter the slicing is only one psoition
it will return a list. 

Problem 5 
Answer: b 

Problem 6
Answer: c 
Correct Answer:b
Expl: LOL, I selected the wrong answer because I added wrong 8 + 3. I thought it was 12 therefore, it never 
will go into that elif. 

Problem 7 
Answer: d 

Problem 8 
Answer: c

Problem 9 
Answer: c

Problem 10 
Answer: e 
 
"""
#Problem 11, 12, 13
import turtle
def squareWave(t, length):
    t.forward(length)
    t.right(45)
    t.forward(length)
    t.left(45)
    t.forward(length)
    t.left(45)
    t.forward(length)
    t.right(45)
    t.forward(length)

tWave = turtle.Turtle()
squareWave(tWave,50)


def motif(t, length, num, angle ):
    for i in range(0, num):
        t.right(angle)
        squareWave(t,length)


snappy = turtle.Turtle()
motif(snappy,50,4,90)

def getDivergent(words):
    countY = 0
    countN = 0
    for eachWord in words:
        if eachWord[0] == eachWord[-1]:
            countY +=1
        else:
            countN +=1
    return (countY,countN)

advice = ['the', 'secret', 'to', 'a', 'better', 'health', 'is', 'exercise']
print(getDivergent(advice))


def printLines(line):
    numLines = int(input("Number of repetitions?"))
    for i in range(numLines):
        print(line)
    return numLines

numLinesInt = printLines('%%%%%%%%')
print(numLinesInt)


