from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,score_pos):
        super().__init__()
        self.color('white'), self.pu(), self.hideturtle(),self.goto(score_pos)
        self.score = 0
        self.writer()

    def writer(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=('Arial', 20, 'normal'))


    def add_score(self):
        self.score+=1
        self.writer()



