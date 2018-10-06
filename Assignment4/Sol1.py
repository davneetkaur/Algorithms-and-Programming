# Pogram to draw American Flag
# Preconditon: Program is designed to handle integer/float inputs. No string inputs should be given

import turtle
import random

def getColor(color):
    if color == "white":
        return(1.000, 1.000, 1.000)
    elif color == "red":
        return(0.698, 0.132, 0.203)
    elif color == "blue":
        return(0.234, 0.233, 0.430)
    elif color == "black":
        return(0.000, 0.000, 0.000)
    elif color == "brown":
        return(0.184,0.134,0.011)
    else:
        return(random.random(),random.random(),random.random())
    
def drawShape(length, height):
    for i in range(0,2):
        turtle.fd(length)
        turtle.right(90)
        turtle.fd(height)
        turtle.right(90)

def drawRectangle(length, height, color):
    turtle.color(color)
    turtle.begin_fill()
    drawShape(length, height)
    turtle.end_fill()

def drawStar(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for lines in range (0, 5):
        turtle.fd(size)
        turtle.right(144)
    turtle.end_fill()

def drawFlag(height):
    length = float(1.9 * height)
    color = getColor("black")
    turtle.color(color)
    drawShape(length, height)

height = float(input("Enter height of the flag (between 125 and 250): "))
while (height < 125 or height > 250):
    print ("Height of the flag must be an between 125 and 250.")
    print ("Please try again.")
    height = float(input("Enter height of the flag (between 125 and 250): "))
length = float(1.9 * height)
stripLength = float(height/13)
turtle.bgcolor(getColor("anycolor"))
turtle.tracer(0,0)
turtle.penup()
turtle.setpos(-250,280)
turtle.pendown()

#to draw stripes
for i in range(0,13):
    if (i%2 ==0):
        color = getColor("red")
    else:
        color = getColor("white")
    drawRectangle(length, stripLength, color)
    turtle.right(90)
    turtle.forward(height/13)
    turtle.left(90)
    
turtle.penup()
turtle.left(90)
turtle.fd(height)
turtle.right(90)
turtle.pendown()

#to draw canton
cantonHeight = float(height * 7/13)
cantonLength = float(length * 2/5)
color = getColor("blue")
drawRectangle(cantonLength, cantonHeight, color)

#to draw outer flag
drawFlag(height)

turtle.right(90)

#to draw pole
poleLength = height * 2.2
poleHeight = poleLength/30
color = getColor("brown")
drawRectangle(poleLength, poleHeight, color)

turtle.penup()
turtle.fd(cantonHeight/11)
turtle.left(90)
turtle.fd(cantonLength/16)

#to draw stars
starDiameter = float(stripLength * 4/5)
color = getColor("white")
for i in range(0,9):
    if (i%2 == 0):
        noOfStars = 6
    else:
        noOfStars = 5
    for j in range(0,noOfStars):
        turtle.pendown()
        drawStar(starDiameter, color)
        turtle.penup()
        turtle.fd(2*starDiameter)
        turtle.pendown()
    turtle.penup()
    turtle.backward(starDiameter*11)
    turtle.right(90)
    turtle.fd(cantonHeight/10)
    turtle.left(90)

turtle.hideturtle()
turtle.update()


