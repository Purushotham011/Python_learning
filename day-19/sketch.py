from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()


def f():
    tim.forward(10)
def b():
    tim.backward(10)
def l():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
def r():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)
def clear():
    tim.reset()

scr.listen()
scr.onkey(f,"w")
scr.onkey(l,"a")
scr.onkey(b,"s")
scr.onkey(r,"d")
scr.onkey(clear,"c")
scr.exitonclick()