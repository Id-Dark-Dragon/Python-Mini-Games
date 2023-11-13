from turtle import Turtle
from random import randint


class Food (Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle'), self.penup(), self.speed(6), self.shapesize(.5, .5)
        self.refresh()
    def refresh(self):
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.goto(randint(-270, 270), randint(-270, 270))









