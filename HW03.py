
#1
import turtle
s = turtle.Screen()
t_size = 100 
shapeT = turtle.Turtle()
shapeT.color('Red')
shapeT.width(10)
shapeT.speed()
shapeT.forward(t_size)
shapeT.left(120)
shapeT.forward(t_size)
shapeT.left(120)
shapeT.forward(t_size)
shapeT.left(120)
shapeT.up()
shapeT.goto(200,0)
shapeT.down()
shapeT.forward(t_size)
shapeT.left(90)
shapeT.forward(t_size)
shapeT.left(90)
shapeT.forward(t_size)
shapeT.left(90)
shapeT.forward(t_size)
shapeT.up()
shapeT.goto(400,0)
shapeT.down()
shapeT.right(270)
shapeT.forward(t_size)
shapeT.left(72)
shapeT.forward(t_size)
shapeT.left(72)
shapeT.forward(t_size)
shapeT.left(72)
shapeT.forward(t_size)
shapeT.left(72)
shapeT.forward(t_size)
shapeT.up()

shapeT.goto(0,0)
shapeT.clear()

#2
"""
circulos concentricos 
"""
shapeT.up()
shapeT.right(90)

shapeT.forward(50)

shapeT.right(270)
shapeT.down()
shapeT.circle(50)
shapeT.up()
turtle.home
shapeT.right(90)
shapeT.forward(50)
shapeT.right(270)
shapeT.down()
shapeT.circle(100)
shapeT.up()
turtle.home
shapeT.right(90)
shapeT.forward(50)
shapeT.right(270)
shapeT.down()
shapeT.circle(150)
shapeT.up()
turtle.home
shapeT.right(90)
shapeT.forward(50)
shapeT.down()
shapeT.right(270)
shapeT.down()
shapeT.circle(200)
shapeT.up()
turtle.home

shapeT.clear()
#turtle.mainloop()

# 3
import math

print("The factorial of 100 is : ", math.factorial(100))
print("The log of 1,000,000 with base 2: ",math.log(1000000,2))
print(math.gcd(63,49))







