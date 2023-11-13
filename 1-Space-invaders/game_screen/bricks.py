from cnfigs import *
from turtle import RawTurtle
from random import choice

COLOR = ["lightgreen", "turquoise", "skyblue", ]


class Brick:
    def __init__(self, screen):
        self.turtle = None
        self.screen = screen
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.br_list = []

        self.bake_bricks()

    def bake_bricks(self):
        row = self.height / 2 - 400
        for _ in range(5):
            row += 20
            brick_x = -self.width / 2 + 20
            for _ in range(10):
                brick_x += 50
                self.turtle = RawTurtle(self.screen)
                self.turtle.shape("square"), self.turtle.pu(), self.turtle.speed("fastest")
                self.turtle.color(choice(COLOR)), self.turtle.shapesize(.2, 2)
                self.turtle.goto(brick_x, row)

                self.br_list.append(self.turtle)

    def clear(self):
        for br in self.br_list:
            br[0].hideturtle()
