from turtle import Turtle
from random import choice

COLOR = ["lightgreen", "turquoise", "skyblue", ]


class Brick:
    def __init__(self, width, height):
        self.turtle = None
        self.width = width
        self.height = height
        self.br_list = []


    def bake_bricks(self):
        """This make a list of bricks in this format ---> [[turtle obj., number of times it got hit], []]"""
        row = self.height / 2 - 250
        for _ in range(5):
            row += 30
            brick_x = -self.width / 2
            for _ in range(12):
                brick_x += 60
                self.turtle = Turtle()
                self.turtle.shape("square"), self.turtle.pu(), self.turtle.speed("fastest")
                self.turtle.color(choice(COLOR)), self.turtle.shapesize(.5, 2)
                self.turtle.goto(brick_x, row)

                self.br_list.append([self.turtle, 0])

    def clear(self):
        for br in self.br_list:
            br[0].hideturtle()

    def brick_process(self, index):
        if self.br_list[index][1] == 0:
            self.br_list[index][1] = 1
            self.br_list[index][0].color("pink")

        elif self.br_list[index][1] == 1:
            self.br_list[index][0].hideturtle()