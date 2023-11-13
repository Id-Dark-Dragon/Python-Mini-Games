from playsound import playsound
from cnfigs import *


class Sound:
    def __init__(self):
        self.sound_on = None

    def play(self, sound_name):
        if self.sound_on:
            if sound_name == "win":
                playsound(win_efc, block=False)
            if sound_name == "lose":
                playsound(lose_efc, block=False)
            if sound_name == "ship_smash":
                playsound(ship_efc, block=False)
            if sound_name == "alien_smash":
                playsound(alien_efc, block=False)

