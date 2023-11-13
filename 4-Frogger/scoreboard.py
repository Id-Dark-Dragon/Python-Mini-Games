from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu(), self.hideturtle(), self.color('white'),
        self.goto(-230, 250)
        self.level = 1


    def lv_board(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f'level {self.level}', align='center', font=FONT)

    def add_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', align='center', font=FONT)