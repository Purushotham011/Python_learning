from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.h.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.incscore()

    # Detect collision with wall
    if snake.h.xcor() > 280 or snake.h.xcor() < -280 or snake.h.ycor() > 280 or snake.h.ycor() < -280 :
        score.game_over()
        game = False

    # Detect collision with tail

    for segment in snake.s[1:]:
        if snake.h.distance(segment) < 10 :
            game = False
            score.game_over()


screen.exitonclick()
