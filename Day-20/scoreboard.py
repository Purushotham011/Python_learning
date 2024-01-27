from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.upscore()
        self.incscore()

    def upscore(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal "))

    def incscore(self):
        self.score += 1
        self.clear()
        self.upscore()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=("Arial", 24, "normal "))