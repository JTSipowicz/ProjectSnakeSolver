from tkinter import *

from scoreboard import Scoreboard
from data_structs import COLORS
from game import SnakeGame
from agent import Agent, train

scoreboard = Scoreboard()
scoreboard.load_scores()
game = SnakeGame(scoreboard)
agent = Agent()

class Menu(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Snake Solver")
        self["bg"] = COLORS["background"]
        self.config(padx=30, pady=60)

        # Main Menu 
        self.menu_frame = Frame(self)
        self.menu_frame['bg'] = COLORS["background"]

        # Scoreboard Menu 
        self.scoreboard_frame = Frame(self)
        self.scoreboard_frame['bg'] = COLORS["background"]

        # AI Menu 
        self.ai_frame = Frame(self)
        self.ai_frame['bg'] = COLORS["background"]

        # Main Menu Widgets 
        title_label = Label(self.menu_frame, text="Snake Solver", font=("Noto Sans", 32, "bold"), bg=COLORS['background'], fg=COLORS["text_color"])
        title_label.grid(column=0, row=0, pady=30)

        play_button = Button(self.menu_frame, text="Play Snake", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], command=self.player_game)
        play_button.grid(column=0, row=1, pady=30)

        AI_button = Button(self.menu_frame, text="Manage AI", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], command=self.show_ai_menu)
        AI_button.grid(column=0, row=2, pady=30)

        score_button = Button(self.menu_frame, text="Scoreboard", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], command=self.show_scoreboard)
        score_button.grid(column=0, row=3, pady=30)

        # Scoreboard Widgets 
        score_title_label = Label(self.scoreboard_frame, text="Scoreboard", font=("Noto Sans", 32, "bold"), bg=COLORS['background'], fg=COLORS["text_color"])
        score_title_label.grid(column=0, row=0, pady=30, sticky="W")

        score_go_back_button = Button(self.scoreboard_frame, text="Back", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], command=self.show_main_menu)
        score_go_back_button.grid(column=2, row=0, pady=30, sticky="E")

        scoreboard_text = Text(self.scoreboard_frame, font=("Noto Sans", 32, "bold"), bg=COLORS['background'], fg=COLORS["text_color"], width=20, height=11)
        for i in range(10):
            score = scoreboard.get_high_scores(i)
            text = str(score["Place"]) + '\t' + score["Type"] + '\t' + str(score["Score"]) + '\n'
            scoreboard_text.insert(END, text)
        scoreboard_text.grid(column=0, columnspan=3, row=2)

        # AI Widgets
        ai_title_label = Label(self.ai_frame, text="AI Functions", font=("Noto Sans", 32, "bold"), bg=COLORS['background'], fg=COLORS["text_color"])
        ai_title_label.grid(column=0, row=0, pady=30)

        ai_go_back_button = Button(self.ai_frame, text="Back", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], command=self.show_main_menu)
        ai_go_back_button.grid(column=1, row=0, pady=30, sticky="E")

        fit_button = Button(self.ai_frame, text="Fit Model", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], width=14, command=self.AI_game)
        fit_button.grid(column=0, row=1, pady=30, columnspan=2)

        test_button = Button(self.ai_frame, text="Test Model", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], width=14, command=self.test_model)
        test_button.grid(column=0, row=2, pady=30, columnspan=2)

        statistics_button = Button(self.ai_frame, text="Statistic", font=("Noto Sans", 24, "bold"), bg=COLORS["box_color"], fg=COLORS["light_text"], width=14, command=self.show_statistics)
        statistics_button.grid(column=0, row=3, pady=30, columnspan=2)
        
        # Menu Initialization at construction
        self.show_main_menu()
        

    def show_main_menu(self):
        self.scoreboard_frame.grid_forget()
        self.ai_frame.grid_forget()
        self.menu_frame.grid(column=0, row=0)

    def show_scoreboard(self):
        self.menu_frame.grid_forget()
        self.scoreboard_frame.grid(column=0, row=0)

    def show_ai_menu(self):
        self.menu_frame.grid_forget()
        self.ai_frame.grid(column=0, row=0)

    def fit_model(self):
        pass

    def test_model(self):
        pass

    def show_statistics(self):
        pass

    def player_game(self):
        game.game_loop()
    
    def AI_game(self):
        train(scoreboard)
    
app = Menu()
app.mainloop()