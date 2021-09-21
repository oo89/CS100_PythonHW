#1
def twoWords(length, firstLetter):
    returnList = []
    while True:
        firstWord = input("Enter a " + str(length) + "-letter word plase:")
        if len(firstWord) == length:
            break
    while True:
        secondWord = input("Enter a word beginning with " + firstLetter + " please:")
        if secondWord.startswith(firstLetter.lower()):
            break
    returnList = [firstWord,secondWord]
    return returnList
print(twoWords(4,'B'))

#2
def twoWordsV2(length, firstLetter):
    returList = []
    while True:
        firstWord = input("Enter a " + str(length) + "-letter word plase:")
        if len(firstWord) == length:
            while True:
                secondWord = input("Enter a word beginning with "+ firstLetter + " please:")
                if secondWord.startswith(firstLetter.lower()):
                    returList = [firstWord, secondWord]
                    return returList
print(twoWords(4,'B'))

#2.1
def twoWordsV3(length, firstLetter):
    returList = []
    firstWord = input("Enter a " + str(length) + "-letter word plase:")
    while len(firstWord) != length:
        firstWord = input("Enter a " + str(length) + "-letter word plase:")
    secondWord = input("Enter a word beginning with " + firstLetter + " please:")
    while not secondWord.startswith(firstLetter.lower()):
        secondWord = input("Enter a word beginning with " + firstLetter + " please:")
    returList = [firstWord, secondWord]
    return returList
print(twoWordsV3(4,'B'))

#3
def checkDi(s):
    for i in range(10):
        if str(i) in s:
            return True
    return False
def enterNewPassword():
    password = input("Enter a password")
    while True:
        if len(password) >= 8 and len(password) <= 15 and checkDi(password):
            print("good password")
            break
        elif len(password) < 8 or len(password) > 15:
            password = input("Enter a password with more than 8 and less than 15 characters")
            continue
        else:
            password = input("Enter a password with at least one number")
            continue

enterNewPassword()

#4
import random
def guessNumber():
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
    number = 5 #random.randint(0, 50)
    guess = int(input("Guess 1?"))
    countGuessNumber = 2
    while True:
        if number == guess:
            print("You are right! I was thinking of "+ str(number)+"!")
            break
        elif guess > 50:
            print("Enter a number between 0-50")
            guess = int(input("Guess " + str(countGuessNumber) + "?"))
            continue
        elif number != guess and countGuessNumber <=5:
            if guess > number:
                print(str(guess)+ " is too high")
            else:
                print(str(guess)+ " is too low")
            guess = int(input("Guess "+ str(countGuessNumber)+ "?"))
            countGuessNumber +=1

            continue
        else:
            return print(number)
guessNumber()








