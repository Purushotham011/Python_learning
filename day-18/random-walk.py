import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.color("red")
turtle.colormode(255)

def random_color () :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

# colors = [
#     "black",
#     "red",
#     "green",
#     "blue",
#     "cyan",
#     "yellow",
#     "magenta",
#     "orange",
#     "purple",
#     "brown",
#     "gray",
#     "pink",
#     "turquoise",
#     "gold",
#     "silver",
#     "navy",
#     "olive",
#     "maroon",
#     "lime",
#     "teal",
#     "aqua",
#     "indigo",
#     "violet",
#     "coral",
#     "salmon",
#     "tan",
#     "khaki",
#     "plum",
#     "orchid"
# ]


direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")
for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

my_screen = Screen()
my_screen.exitonclick()