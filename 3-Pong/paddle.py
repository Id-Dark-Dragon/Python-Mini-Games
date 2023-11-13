from turtle import Turtle


class Paddle (Turtle):
    def __init__(self, cord):
        super().__init__()
        self.color('white'), self.shapesize(5, 1), self.pu(),self.shape('square')
        self.goto(cord)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 30)
