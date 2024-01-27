from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.ls = 0
        self.rs = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.ls, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rs, align="center", font=("courier", 80, "normal"))

    def l_point(self):
        self.ls += 1
        self.update_score()

    def r_point(self):
        self.rs += 1
        self.update_score()
