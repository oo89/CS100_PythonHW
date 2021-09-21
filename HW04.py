
#1
a,b,c = 3, 4, 5

if a < b:
    print("OK")
else:
    print(" NOT OK a is not less than b")

if c < b:
    print("OK")
else:
    print("NOT OK c is no less than b ")

if a + b == c:
    print("OK")
else:
    print("NO OK a + b is not = c")

#3
import turtle
color = input("Color.")
lineWidth = input("Line Width.")
lineLength = input("Line Length.")
shape = input("Shape (Line, Triangle or Square).")
intLineWidth = int(lineWidth)
intLineLength = int(lineLength)
if shape == 'Line':
    shapeL = turtle.Turtle()
    s = turtle.Screen()
    shapeL.speed(1)
    shapeL.color(color)
    shapeL.width(intLineWidth)
    shapeL.forward(intLineLength)
    shapeL.clear()
    turtle.home
    turtle.mainloop()
elif shape == 'Triangle':
    shapeT = turtle.Turtle()
    shapeT.speed(1)
    shapeT.color(color)
    shapeT.width(intLineWidth)
    shapeT.forward(intLineLength)
    shapeT.left(120)
    shapeT.forward(intLineLength)
    shapeT.left(120)
    shapeT.forward(intLineLength)
    turtle.mainloop()
elif shape == 'Square':
    shapeS = turtle.Turtle()
    shapeS.speed(1)
    shapeS.color(color)
    shapeS.width(intLineWidth)
    shapeS.forward(intLineLength)
    shapeS.left(90)
    shapeS.forward(intLineLength)
    shapeS.left(90)
    shapeS.forward(intLineLength)
    shapeS.left(90)
    shapeS.forward(intLineLength)
    turtle.mainloop()
else:
    print("Incorrect input")





