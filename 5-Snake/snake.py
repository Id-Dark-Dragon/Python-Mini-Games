from turtle import Turtle,Screen

DISTANCE_FD = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]


    def creat_snake(self):
        x_cord = 0.0
        for nums in range(3):
            self.add_segments()
            self.square.goto(x=x_cord, y=0)
            x_cord -= 20
            self.segments.append(self.square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.head.fd(DISTANCE_FD)

    def add_segments(self):
        self.square = Turtle(shape='square')
        self.square.color('red')
        self.square.pu()

    def tail_increase(self):
        self.add_segments()
        self.segments.append(self.square)
        self.square.goto(self.segments[-1].pos())


        self.move()


    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)

    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)
        elif self.head.heading() == 270:
            self.head.left(90)

    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)
