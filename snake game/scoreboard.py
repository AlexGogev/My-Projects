from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0 
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score {self.score}", align='center' )
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over!")
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()