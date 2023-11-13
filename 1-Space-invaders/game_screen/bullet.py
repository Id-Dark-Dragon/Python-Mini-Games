from turtle import RawTurtle


class Bullet(RawTurtle):
    def __init__(self, screen, color, orientation: str):
        super().__init__(screen)
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.shapesize(.1, 2)
        self.color(color)
        if orientation == "up":
            self.seth(90)
        elif orientation == "down":
            self.seth(270)
        else:
            raise ValueError

    def shoot(self, start_pos):
        self.speed(0)

        self.setpos(start_pos[0], start_pos[1])
        self.speed(2)
        self.showturtle()



