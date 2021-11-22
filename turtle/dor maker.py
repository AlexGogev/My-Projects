#dot painting

from turtle import Turtle
import random
import turtle
turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
rgb_colors = [(27, 159, 27), (101, 99, 101), (118, 162, 118), (182, 164, 182), (4, 48, 4), (140, 170, 140), (5, 2, 5), (185, 
145, 185), (229, 94, 229), (84, 61, 84), (0, 126, 0), (11, 218, 11), (27, 20, 27), (1, 1, 1), (132, 144, 132), (228, 106, 228), (25, 114, 25), (238, 173, 238), (243, 172, 243), (247, 148, 247), (182, 40, 182), (232, 222, 232), (239, 57, 239), (98, 95, 98), (128, 96, 128), (104, 110, 104), (216, 216, 216), (205, 217, 205), (182, 178, 182), (193, 211, 193)]


tim.setheading(225)
tim.forward(250)
tim.setheading(0)

num_of_dots = 100

for i in range(1, num_of_dots+1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle.Screen()
screen.exitonclick()
