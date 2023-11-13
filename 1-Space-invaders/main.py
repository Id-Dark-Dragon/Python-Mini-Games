from customtkinter import *
from game_screen.game_screen import GameScreen
from side_panel.option_panel import Options
from sound_handling.sound import Sound


class GameApp(CTk):
    def __init__(self):
        super().__init__()

        self.minsize(width=500, height=400)
        self.config(padx=10, pady=10, )
        self.title("Python Space Invaders")

        self.sound = Sound()
        self.game = GameScreen(self, self.sound)
        self.option_panel = Options(self, self.game, self.sound)
        self.mainloop()


if __name__ == "__main__":
    GameApp()








