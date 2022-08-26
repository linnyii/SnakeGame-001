from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # erase the effect of animation
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()  # segments will not move until forloop (all segments) is done.
    # time.sleep() -> every move will hold for 0.1
    # so we can see how segments moves
    time.sleep(0.5)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:  # you can adjust the distance by yourself.
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # if head collides with any segments in segments[]
    # trigger game_over()
    for segment in snake.segments[1:]:  # go through all items except the first one item
        if snake.head.distance(segment) < 10:
            game_is_one = False
            scoreboard.game_over()

screen.exitonclick()