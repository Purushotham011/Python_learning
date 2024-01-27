from turtle import Turtle

MD = 20
ST_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.s = []
        self.create_snake()
        self.h = self.s[0]

    def create_snake(self):
        for i in ST_POS:
            self.add_seg(i)

    def add_seg(self, position):
        new_s = Turtle("square")
        new_s.color("white")
        new_s.penup()
        new_s.goto(position)
        self.s.append(new_s)

    def extend(self):
        self.add_seg(self.s[-1].position())

    def move(self):
        for seg in range(len(self.s) - 1, 0, -1):
            new_x = self.s[seg - 1].xcor()
            new_y = self.s[seg - 1].ycor()
            self.s[seg].goto(new_x, new_y)
        self.h.forward(MD)

    def up(self):
        if self.h.heading() != DOWN:
            self.h.setheading(UP)

    def down(self):
        if self.h.heading() != UP:
            self.h.setheading(DOWN)

    def left(self):
        if self.h.heading() != RIGHT:
            self.h.setheading(LEFT)

    def right(self):
        if self.h.heading() != LEFT:
            self.h.setheading(RIGHT)
