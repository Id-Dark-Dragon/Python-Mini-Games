from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.start()


    def move(self):
        self.fd(MOVE_DISTANCE)

    def start(self):
        self.pu(), self.seth(90), self.shape('turtle'), self.color('green')
        self.goto(STARTING_POSITION)

    def move_down(self):
        self.backward(MOVE_DISTANCE)