# Pogram to draw shapes

import turtle
import random
for angle in range(0, 360, 15):
    turtle.seth(angle)
    color1 = random.random()
    color2 = random.random()
    color3 = random.random()
    turtle.color(color1,color2,color3)
    turtle.begin_fill()
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
    turtle.end_fill()
turtle.hideturtle()
turtle.update()

