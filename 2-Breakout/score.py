from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hearts_num = 3
        self.color('red'), self.pu(), self.hideturtle()
        self.goto(-250, 230)
        self.score = 0

        self.writer()

    def writer(self):
        self.clear()
        self.write(self.hearts_num * "❤", align="center", font=('TkDefaultFont', 35, 'normal'))

    def miss(self):
        self.hearts_num -= 1
        self.writer()
        return self.hearts_num

    def lose_win(self, text):
        self.goto(0, 0)
        self.clear()
        self.write(text, align="center", font=("font_path", 35, 'normal'))

