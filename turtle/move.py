from turtle import Turtle, Screen

tim = Turtle()
tony = Turtle()
screen = Screen()
screen.listen()



def w():
    tim.forward(10)
def s():
    tim.backward(10)
def a():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def d():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
 
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w", fun=w)
screen.onkey(key="s", fun=s)
screen.onkey(key="a", fun=a)
screen.onkey(key="d", fun=d)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
