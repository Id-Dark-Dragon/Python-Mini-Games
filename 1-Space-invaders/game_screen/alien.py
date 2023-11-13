from cnfigs import *
from turtle import RawTurtle


class Alien:
    def __init__(self, screen):
        self.aliens_lst = []
        self.turtle = None
        self.screen = screen
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.left_to_right = True
        self.create()
        
    def create(self):
        """This make a list of bricks in this format ---> [{turtle obj., number of times it got hit}]"""

        row = self.height / 2 - 200
        for _ in range(ALIENS_ROWS):
            row += 50
            brick_x = -self.width / 2
            for _ in range(ALIENS_IN_A_ROW):
                brick_x += 60
                self.turtle = RawTurtle(self.screen)
                self.turtle.shape(image_alien)
                self.turtle.pu()
                self.turtle.speed("fastest")
                self.turtle.goto(brick_x, row)
                self.turtle.hit_times = 0

                self.aliens_lst.append(self.turtle)

    def collective_move(self):
        # Alien stop at side walls
        if self.aliens_lst[ALIENS_IN_A_ROW - 1].pos()[0] > SCREEN_WIDTH / 2 - 20:
            self.left_to_right = False

        elif self.aliens_lst[0].pos()[0] < -(SCREEN_WIDTH / 2 - 20):
            self.left_to_right = True

        if self.left_to_right is True:
            for alien in self.aliens_lst:
                alien.fd(ALIENS_SPEED)
        elif self.left_to_right is False:
            for alien in self.aliens_lst:
                alien.fd(-ALIENS_SPEED)







