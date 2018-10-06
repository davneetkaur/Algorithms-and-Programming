# Pogram to get user inputs and draw different shapes depending on user inputs

import turtle
import random

shapes = input("Enter number of shapes to draw (between 2 and 15): ")
while shapes.isdigit() and (int(shapes) < 2 or int(shapes) > 15):
    print ("Number of shapes must be an integer between 2 and 15.")
    print ("Please try again.")
    shapes = input("Enter number of shapes to draw (between 2 and 15): ")
    if not(shapes.isdigit()):
        break   
while not(shapes.isdigit()) or int(shapes) < 2 or int(shapes) > 15:
    print ("Number of shapes must be an integer between 2 and 15.")
    print ("Please try again.")
    shapes = raw_input("Enter number of shapes to draw (between 2 and 15): ")
    if shapes.isdigit() and int(shapes) > 2 and int(shapes) < 15:
        break
shapes = int(shapes)

sides = input("Enter number of sides in shape (between 2 and 9): ")
while sides.isdigit() and (int(sides) < 2 or int(sides) > 9):
    print ("Number of sides must be an integer between 2 and 9.")
    print ("Please try again.")
    sides = input("Enter number of sides in shape (between 2 and 9): ")
    if not(sides.isdigit()):
        break   
while not(sides.isdigit()) or int(sides) < 2 or int(sides) > 9:
    print ("Number of sides must be an integer between 2 and 9.")
    print ("Please try again.")
    sides = input("Enter number of sides in shape (between 2 and 9): ")
    if sides.isdigit() and int(sides) > 2 and int(sides) < 9:
        break
sides = int(sides)

length = input("Enter length of each side (between 30 and 100): ")
while length.isdigit() and (int(length) < 30 or int(length) > 100):
    print ("Length of a side must be an integer between 30 and 100.")
    print ("Please try again.")
    length = input("Enter length of each side (between 30 and 100): ")
    if not(length.isdigit()):
        break   
while not(length.isdigit()) or int(length) < 30 or int(length) > 100:
    print ("Length of a side must be an integer between 30 and 100.")
    print ("Please try again.")
    length = input("Enter length of each side (between 30 and 100): ")
    if length.isdigit() and int(length) > 30 and int(length) < 100:
        break
length = int(length)

turtle.tracer(0,0)
for angle in range(0, 360, 360/shapes):
    turtle.seth(angle)
    color1 = random.random()
    color2 = random.random()
    color3 = random.random()
    turtle.color(color1,color2,color3)
    turtle.begin_fill()
    turtle.fd(length)
    for lines in range (1, sides):
        turtle.left(360/sides)
        turtle.fd(length)
        lines = lines + 1
    turtle.end_fill()
turtle.hideturtle()
turtle.update()
