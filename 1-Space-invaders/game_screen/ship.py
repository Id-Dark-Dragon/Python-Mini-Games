from cnfigs import *
from turtle import RawTurtle

from time import sleep



class Ship(RawTurtle):
    def __init__(self, screen):
        super().__init__(screen)
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.create()

    def create(self):
        self.shape(image_ship)
        self.goto(0, -(self.height/2)+100)

    def right(self, *args):
        if self.xcor() > self.width / 2 - 70:
            pass
        else:
            self.forward(PAD_MOVE)

    def left(self, *args):
        if self.xcor() < -self.width / 2 + 70:
            pass
        else:
            self.forward(-PAD_MOVE)

    def blink(self):
        for _ in range(5):
            self.hideturtle()
            self.screen.update()
            sleep(0.2)
            self.showturtle()
            self.screen.update()
            sleep(0.2)
