from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("red")

n=int(input("Enter the number of sides :"))
colors = [
    "black",
    "white",
    "red",
    "green",
    "blue",
    "cyan",
    "yellow",
    "magenta",
    "orange",
    "purple",
    "brown",
    "gray",
    "pink",
    "turquoise",
    "gold",
    "silver",
    "navy",
    "olive",
    "maroon",
    "lime",
    "teal",
    "aqua",
    "indigo",
    "violet",
    "coral",
    "salmon",
    "tan",
    "khaki",
    "plum",
    "orchid"
]

def draw_shape (n):
    angle = 360/n
    for _ in range(n):
        tim.forward(100)
        tim.right(angle)

for i in range(3,n+3):
    tim.color(random.choice(colors))
    draw_shape(i)




my_screen = Screen()
my_screen.exitonclick()