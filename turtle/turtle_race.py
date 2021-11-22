from turtle import Turtle, Screen, color
import turtle
import random

import os
#reset = os.startfile("C:/Users/Alex/Desktop/Portfolio Python/turtle/turtle_race.py")
is_race_on = False
screen = Screen()

screen.setup(width= 500,height=400)

colors = ["blue","red","pink","green","yellow","orange"]
names = ["Alex","Mama","Alison","Mimi"]
all_turtles = []

def setup():
    disposition = -40
    for i in range(0,6):
        Tim = Turtle(shape="turtle")
        Tim.color(colors[i])
        Tim.penup()
        Tim.goto(x=-230, y=disposition)
        disposition += 30
        all_turtles.append(Tim)

def start():
    setup()
    user_bet = screen.textinput("make bet", "Guess who will win?")

    if user_bet:
        is_race_on = True

    while is_race_on:  
        for i in all_turtles:
            if i.xcor() > 230:
                winner = i.pencolor()
                is_race_on = False
                print(f'{i.pencolor()} wins!"')
                if winner == user_bet:
                    print("weldone")
                else:
                    print("try again")
                    
                    
                    
                    
                    
                    
            distance = random.randint(0,10)
            i.forward(distance)

start()
screen.exitonclick()