from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("snake game\\score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score {self.score} High score {self.high_score}", align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake game\\score.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!")

    def increase_score(self):
        self.score += 1

        self.update_score()
