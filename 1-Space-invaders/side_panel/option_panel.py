from customtkinter import *
APPEARANCE_MODE = "Dark"  # Modes: "System" (standard), "Dark", "Light"
COLOR_THEME = "dark-blue"  # Themes: "blue" (standard), "green", "dark-blue"


class Options:
    def __init__(self, master, game_screen, sound_ctrl):
        self.master = master
        self.game = game_screen
        self.sound_ctrl = sound_ctrl
        self.game = game_screen
        self.master = master
        frame = CTkFrame(master=self.master)
        frame.grid(row=0, column=1, )

        set_appearance_mode(APPEARANCE_MODE)
        set_default_color_theme(COLOR_THEME)

        self.life_icon = CTkLabel(frame, text=f" {self.game.lives_tracker*'❤'}", text_color="red", font=("bold", 35))
        comment_label = CTkLabel(frame, text="Try to kill all the aliens,\n"
                                             "Use Arrow Keys to move the ship,\n"
                                             "Then you win!", font=("normal", 15))
        restart_btn = CTkButton(frame, text="Restart", width=200, command=self.restart_btn_func)
        self.freeze_btn = CTkButton(frame, text="Pause", width=200, command=self.freeze_btn_func)
        self.sound_key = CTkCheckBox(frame, text="Sound", onvalue=True, offvalue=False, command=self.sound_key_func)


        # Layout
        self.life_icon.grid(row=2, column=1, padx=10, pady=50)
        restart_btn.grid(row=4, column=1, pady=20)
        self.freeze_btn.grid(row=5, column=1,)
        self.sound_key.grid(row=6, column=1, pady=20)
        comment_label.grid(row=7, column=1, pady=50)


        self.master.after(1000, self.lives_display)


    def freeze_btn_func(self):
        if self.freeze_btn.cget("text") == "Pause":
            self.game.freeze()
            self.freeze_btn.configure(text="Continue")

        elif self.freeze_btn.cget("text") == "Continue":
            self.game.game_loop()
            self.freeze_btn.configure(text="Pause")

    def restart_btn_func(self):
        self.game.restart()
        self.freeze_btn.configure(state="active")
        self.freeze_btn.configure(text="Pause")

    def lives_display(self):
        """ checks the lives 50 millisecond and updates the lives display accordingly"""
        self.life_icon.configure(text=f" {self.game.lives_tracker*'❤'}")
        if self.game.win_report:
            self.freeze_btn.configure(state="disabled")
            self.life_icon.configure(text=f"You Win!!!", font=("normal", 25))

        if self.game.lives_tracker == 0:
            self.life_icon.configure(text=f"Game Over!!!", font=("normal", 25))
            self.freeze_btn.configure(state="disabled")

        self.master.after(50, self.lives_display)

    def sound_key_func(self):
        self.sound_ctrl.sound_on = self.sound_key.get()
