from tkinter import *

from scoreboard import Scoreboard
from colors import COLORS
from game import game_loop

scoreboard = Scoreboard()
scoreboard.load_scores()

def main_loop():
    window = Tk()
    
    window.title("Snake Solver")
    window["bg"] = COLORS["background"]
    window.config(padx=30, pady=60)

    title_label = Label(text="Snake Solver", font=("Noto Sans", 32, "bold"), bg=COLORS['background'], fg=COLORS["text_color"])
    title_label.grid(column=0, row=0, pady=30)

    play_button = Button(text="Play Snake", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], command=lambda: game_loop(scoreboard, 'Player'))
    play_button.grid(column=0, row=1, pady=30)

    AI_button = Button(text="Manage AI", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], command=game_loop)
    AI_button.grid(column=0, row=2, pady=30)

    score_button = Button(text="Scoreboard", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], command=game_loop)
    score_button.grid(column=0, row=3, pady=30)

    window.mainloop()

main_loop()