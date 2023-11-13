from turtle import Turtle

FIRST_HEADING = 50


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white'), self.pu(), self.shape('circle')
        self.goto(0, 0)
        self.seth(FIRST_HEADING)
        self.speed = .08

    def move(self):
        self.fd(20)

    def wall_collision(self):
        self.seth(-self.heading())

    def paddle_collision(self):
        self.seth(180-self.heading())
        self.speed *= .9

    def restart(self, mark):
        self.goto(0, 0)
        self.seth(mark + FIRST_HEADING)
        self.speed = .08
