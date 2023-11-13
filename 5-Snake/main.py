from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.title('snake game')
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.score_writer()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.15)
    snake.move()

    if food.distance(snake.head) < 15:
        food.refresh()
        scoreboard.score_()
        snake.tail_increase()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_is_on=False

    for seg in snake.segments:
        if snake.head.distance(seg)<10 and snake.segments[0]!=seg:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()

