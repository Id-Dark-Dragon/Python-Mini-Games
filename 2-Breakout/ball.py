from turtle import Turtle
from random import randint



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white'), self.pu(), self.shape("circle")
        self.goto(0, 0)
        self.speed = .08

    def move(self):
        self.fd(20)

    def vertical_collision(self):
        self.seth(180-self.heading())



    def horizontal_collision(self):
        self.seth(-self.heading())


    def start(self, x, y):
        self.goto(x, y)
        head_angel = randint(20, 160)
        self.seth(head_angel if head_angel != 90 else 30)

