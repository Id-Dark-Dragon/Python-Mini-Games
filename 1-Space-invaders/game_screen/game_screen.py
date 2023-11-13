import random
from customtkinter import *
from tkinter import Canvas
from turtle import TurtleScreen
from .ship import Ship
from .alien import Alien
from .bullet import Bullet
from .bricks import Brick
from cnfigs import *


class GameScreen:
    def __init__(self, master, sound_ctrl):
        self.master = master
        self.sound_ctrl = sound_ctrl
        game_frame = CTkFrame(master=self.master)
        game_frame.grid(row=0, column=0, rowspan=10)

        canvas = Canvas(master=game_frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        canvas.grid(row=0, column=0)

        self.game_loop_after_func = None
        self.lives_tracker = LIVES
        self.win_report = False

        self.screen = TurtleScreen(canvas, )
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.register_shape(image_ship)
        self.screen.register_shape(image_alien)
        self.screen.register_shape(image_alien_angry)

        # ___________Game element initializing____________________
        self.ship_blt = Bullet(self.screen, "green", "up")

        # Ship Creation and bindings
        self.ship = Ship(self.screen)
        self.master.bind("<Right>", self.ship.right)
        self.master.bind("<Left>", self.ship.left)

        self.bricks = Brick(self.screen)

        self.aliens = Alien(self.screen)

        self.alien_blt = Bullet(self.screen, "red", "down")
        self.alien_blt.shoot(random.choice(self.aliens.aliens_lst).pos())

        self.ship_blt.shoot(self.ship.pos())

        self.game_loop()

    def game_loop(self):
        self.ship_blt_ctrl()
        self.alien_blt_ctrl()

        # Win mechanism, enables when there is no alien no shoot
        if self.alien_blt_ctrl() is False:
            self.win()
            return

        for alien in self.aliens.aliens_lst:
            # Bullet crash with alien
            if alien.distance(self.ship_blt) < 20 and self.ship_blt.isvisible() and alien.isvisible():
                alien.hit_times += 1
                self.sound_ctrl.play("alien_smash")
                if alien.hit_times < 2:
                    alien.shape(image_alien_angry)

                # if bullet has crashed more than once with the alien
                else:
                    alien.hideturtle()
                self.ship_blt.hideturtle()

        # Bullet crash with brick
        for brick in self.bricks.br_list:
            if brick.distance(self.ship_blt) < 30 and self.ship_blt.isvisible() and brick.isvisible():
                brick.hideturtle()
                self.ship_blt.hideturtle()

            elif brick.distance(self.alien_blt) < 30 and self.alien_blt.isvisible() and brick.isvisible():
                brick.hideturtle()
                self.alien_blt.hideturtle()

        # Bullet crash with ship
        if self.alien_blt.distance(self.ship) < 30 and self.alien_blt.isvisible():
            self.sound_ctrl.play("ship_smash")
            self.lives_tracker -= 1
            # Ship blinking
            self.ship.blink()
            self.alien_blt.hideturtle()
            # Losing mechanism
            if self.lives_tracker == 0:
                self.lose()
                return

        self.aliens.collective_move()

        self.screen.update()
        self.game_loop_after_func = self.master.after(50, self.game_loop)

    def freeze(self):
        self.master.after_cancel(self.game_loop_after_func)
        return

    def restart(self):
        self.freeze()
        self.__init__(self.master, self.sound_ctrl)
        return

    def win(self):
        CTkLabel(master=self.master, text="You Win!", font=("bold", 35)).grid(row=0, column=0)
        self.win_report = True
        self.sound_ctrl.play("win")

    def lose(self):
        CTkLabel(master=self.master, text="You Lose! \n Select 'Restart'", font=("bold", 35)).grid(row=0, column=0)
        self.sound_ctrl.play("lose")


    def ship_blt_ctrl(self):
        # Shoot new ship bullet after bullet went out of screen.
        if not -SCREEN_HEIGHT / 2 + 10 < self.ship_blt.pos()[1] < SCREEN_HEIGHT / 2 - 10:
            self.ship_blt.shoot(self.ship.pos())
        self.ship_blt.fd(SHIP_BULLET_SPEED)

    def alien_blt_ctrl(self):
        # Choose random alien to Shoot if bullet went out of screen
        if not -SCREEN_HEIGHT / 2 + 10 < self.alien_blt.pos()[1] < SCREEN_HEIGHT / 2 - 10:
            # select between visible aliens
            vis_list = [a for a in self.aliens.aliens_lst if a.isvisible() is True]
            if len(vis_list) == 0:
                return False
            else:
                self.alien_blt.shoot(random.choice(vis_list).pos())
        self.alien_blt.fd(ALIEN_BULLET_SPEED)


















