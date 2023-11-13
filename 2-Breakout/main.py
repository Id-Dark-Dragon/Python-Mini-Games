from turtle import Turtle, Screen
from paddle import Paddle
from brick import Brick
from margin import MarginMaker
from ball import Ball
import time
from score import Score

WIDTH = 800
HEIGHT = 600

window = Screen()
window.setup(width=WIDTH, height=HEIGHT)
window.title('Breakout')
window.bgcolor('black')
window.tracer(0)  # Set animation delay to 0

margin = MarginMaker(WIDTH, HEIGHT)

pad = Paddle(WIDTH)

window.listen()
window.onkeypress(pad.left, "Left")
window.onkeypress(pad.right, "Right")

bricks = Brick(WIDTH, HEIGHT)
bricks.bake_bricks()

ball = Ball()
ball.start(pad.xcor(), pad.ycor()+20)
heart = Score()

loop = True

while loop:
    time.sleep(ball.speed)
#     time.sleep(.3)
    ball.move()

    visible_br = []
    for br in bricks.br_list:
        # brick collision
        if br[0].isvisible():
            visible_br.append(br)
            if 10 < ball.distance(br[0]) < 35:
                bricks.brick_process(index=bricks.br_list.index(br))
                ball.horizontal_collision()
    # Win Mechanism
    if len(visible_br) == 0:
        heart.lose_win("Hooray \n You Won!")
        loop = False

    # vertical wall collision
    if ball.xcor() >= 360 or ball.xcor() <= -360:
        ball.vertical_collision()

    # ceiling collision
    if ball.ycor() >= 260:
        ball.horizontal_collision()

    # Pad collision
    if ball.distance(pad) < 50 and -250 < ball.ycor() < -230:
        ball.horizontal_collision()
    # ball miss and losing mechanism
    elif ball.ycor() < -400:
        ball.start(pad.xcor(), pad.ycor()+20)
        hearts_num = heart.miss()
        if hearts_num == 0:
            bricks.clear()
            heart.lose_win("Game Over")
            loop = False

    window.update()  # Update the screen after each frame


window.mainloop()
