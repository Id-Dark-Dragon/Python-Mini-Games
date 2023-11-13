from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        hs = open('data.txt', mode='r')
        self.high_score = int(hs.read())
        hs.close()
        self.color('white'), self.pu(), self.speed(10), self.goto(x=0, y=270), self.hideturtle()
        self.score_writer()

    def score_(self):

        self.score += 1
        self.high_score_()
        self.score_writer()

    def score_writer(self):

        self.clear()
        self.write(f'you\'r score: {self.score}   High score: {self.high_score}', align='center', font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write('Game Over', align='center', font=('Arial', 15, 'normal'))

    def high_score_(self):
        if self.score > self.high_score:
            self.high_score += 1
            with open('data.txt', mode='w') as hs:
                hs.write(f'{self.high_score}')