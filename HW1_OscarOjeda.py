"""
Oscar Ojeda Perez
CS 100 2019F Section 105
HW 01 September 9, 2019
"""
# Exercise 5b

cars = 45
dealers = 3
workers = 25

# Exercise 5c

usedAudiA4Price = 29883.45
newAudiA4Price = 48900.99
carSellerSalaryH = 23.74

# Exercise 5d

ownerName = 'Oscar'
dealerName = 'Racso Audi'
cityDealer1 = 'Havana Cuba'

# Exercise 6

# 1.1
"""
1- If you leave out one parenthese or both in a print statement you will have an error saying the line where it is
and, also saying "SyntaxError: Missing parentheses in call to 'print'."

2- If you leave out one quotation mark while you are printing an string it will give a SyntaxError but, 
if you leave both quotation marks and the word you write is not defined before, it will give you an NameError
because you are trying to print a not defined variable

3- it will do the normal sum operation as if there were only one "+". Ex 2++2=4

4- It will give you a SyntazError, because Python 3 does not support that. 

5- if you leave a blank space between them it will give you a SyntazError but, if you put the two number 
together it will assume the number like an int. Ex: 65 

"""

# 1.2
print("1.2")
#1
seconds = (42 * 60) + 42
print("1: ", seconds,"sec")

#2
miles = 10 / 1.61
print("2: ", miles,"miles")

#3
timePerMileSec = seconds / miles
print("3: ",timePerMileSec // 60, "min" ,timePerMileSec % 60, "sec per miles" )
print("3:",1 / (timePerMileSec / 3600), "miles/h")
print('\n')

#2.1
"""
. 42 = n is no legal, it will give you an error SyntaxError. 
. x = y = 1 will be ok, both x and y will take the value of 1. 
. nothing will happens  
. SyntacError if you let that period like that. 
. it will give you a name error because xy is a string and it is trying to find some string with that name.
"""
#2.2
print("2.2")
#1
r=5
print("1: Volume:",(4/3)*(3.14 )* (r**3))
"""
to have the exact value of pi math.pi but first you have to import math

"""


#2
priceAfterDiscount = (60*24.95)/100
TotalPriceFirstCopy = priceAfterDiscount + 3
ShippingPriceOthersCopy = 0.75 * 59
TotalPriceOthersWithShipping = (priceAfterDiscount * 59) + ShippingPriceOthersCopy
totalCost = TotalPriceFirstCopy + TotalPriceOthersWithShipping
print("2: Total price:$", totalCost )

#3
leave = (6*3600) + (52*60)
firstAndThirdMileVel = 2*((8*60)+15)
secondPartV2 = 3*((7*60) + 12)
timeHomeSec = leave+firstAndThirdMileVel+secondPartV2
timeHomeH = timeHomeSec // 3600
timeHomeM = (timeHomeSec % 3600)// 60

print("3:",timeHomeH ,":", timeHomeM,"AM")






