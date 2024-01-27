from turtle import Turtle, Screen
sam = Turtle()
print(sam)
sam.shape("turtle")
sam.forward(100)
sam.color("red")
sam.left(90)
sam.left(90)
sam.forward(100)

sam.begin_fill()
while True:
    sam.forward(200)
    sam.left(170)
    if abs(sam.pos()) < 1:
        break
sam.end_fill()

my_screen = Sc-reen()
print(my_screen.canvheight)
my_screen.exitonclick()
