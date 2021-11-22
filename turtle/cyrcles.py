from turtle import Turtle, Screen, colormode, pendown

import random

tim = Turtle()
tim.pensize(5)
colormode(255)
def rand_collor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r,b,g)
    return colors
tim.speed("fastest")

for i in range(360):
    tim.color(rand_collor())
    tim.circle(150)
    tim.right(1.5)
    
    

screen = Screen()
screen.exitonclick()

