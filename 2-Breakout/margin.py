from turtle import Turtle
from random import choice


class MarginMaker(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.color("white")
        self.shapesize(1, 1)
        self.hideturtle()
        self.pu()
        self.goto((-width/2)+20, (-height/2)+20)
        self.pd()
        self.speed("fastest")
        self.goto((-width/2)+20, (height/2)-20)
        self.goto((+width / 2) - 20, (height / 2) - 20)
        self.goto((+width / 2) - 20, (-height / 2) + 20)