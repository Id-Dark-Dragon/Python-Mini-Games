from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

window = Screen()
window.setup(width=800, height=600), window.title('Ping Pong'), window.bgcolor('black')
window.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
l_player = ScoreBoard((-70, 250))
r_player = ScoreBoard((70, 250))

window.listen()
window.onkeypress(l_paddle.up, 'Up'), window.onkeypress(l_paddle.down, 'Down')
window.onkeypress(r_paddle.up, 'w'), window.onkeypress(r_paddle.down, 's')


loop_on = True

while loop_on:
    time.sleep(ball.speed)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_collision()

    if ball.xcor() > 380:
        ball.restart(+90)
        l_player.add_score()
    elif ball.xcor() < -380:
        ball.restart(0)
        r_player.add_score()

    if (ball.xcor() > 335 or ball.xcor() < -335) and (ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50):
        ball.paddle_collision()

    ball.move()
    window.update()
window.exitonclick()
