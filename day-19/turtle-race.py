import turtle
from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green","blue","purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtle.append(new_turtle)

if user_bet:
    race = True

while race :

    for turtle in all_turtle:

        if turtle.xcor()>230:
            race = False
            win_color = turtle.pencolor()
            if win_color== user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else :
                print(f"You've Lost! The {win_color} turtle is the winner!")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()