from turtle import Turtle

PAD_MOVE = 50


class Paddle(Turtle):
    def __init__(self, width):
        super().__init__()
        self.width=width
        self.color('white')
        self.speed("fastest")
        self.shapesize(1.5, 4)
        self.pu()
        self.goto(0, -250)
        self.shape("square")



    def right(self, **kwargs):
        if self.xcor() > self.width/2-70:
            pass
        else:
            self.forward(PAD_MOVE)

    def left(self, **kwargs):
        if self.xcor() < -self.width/2+70:
            pass
        else:
            self.forward(-PAD_MOVE)