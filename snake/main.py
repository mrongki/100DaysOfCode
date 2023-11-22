from border import Border
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen

import time


def stop_game():
    global is_game_over
    scoreboard.reset_score()
    is_game_over = True


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
screen.register_shape("tail", ((10, 9), (3, -10), (-3, -10), (-10, 9)))

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'd')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(stop_game, 'Escape')

border = Border()

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with wall
    x_pos = round(snake.head.xcor())
    y_pos = round(snake.head.ycor())
    if x_pos <= -280 or x_pos >= 280 or y_pos <= -280 or y_pos >= 280:
        snake.reset_snake()
        food.refresh()
        scoreboard.reset_score()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            food.refresh()
            scoreboard.reset_score()

screen.exitonclick()
