from turtle import Turtle, Screen, back
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height=600)
screen.title("Pong!")
screen.tracer(0)

r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() 
    ball.move()
    
    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor()  > -340:
        ball.bounce_x()

    #detect r miss
    if ball.xcor() > 380:
        ball.reset_possition()
        score.l_point()

    #detect l mill
    if ball.xcor() < -380:
        ball.reset_possition()
        score.r_point()

screen.exitonclick()