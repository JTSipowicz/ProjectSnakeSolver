import pygame
import time

from scoreboard import Scoreboard
from colors import COLORS
from snake import Snake
from food import Food
from math_functions import compareSquares
from data_structures import Point
import numpy as np
import os 

window_x = 500
window_y = 300

os.environ['SDL_VIDEO_WINDOW_POS'] = str(window_x) + ',' + str(window_y)

class Game:

    def __init__(self, fps, scoreboard, width=640, height=480, mode='Player'):
        pygame.init()
        self.width = width
        self.height = height
        self.game_speed = fps
        self.iterations = 0
        self.scoreboard = scoreboard
        self.mode = mode
        self.isGameRunning = True
        self.font = pygame.font.SysFont(None, 24)
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.snake = Snake(self.surface, COLORS["snake_color"], self.width, self.height)
        self.food = Food(self.surface, COLORS["food_color"], self.width, self.height)
        if mode == 'Player':
            self.scoreboard.set_type_Player()
        else:
            self.scoreboard.set_type_AI()
        
    def reset(self):
        self.snake.reset()
        while self.is_bad_spawn():
            self.food.respawn()
        self.scoreboard.update()
        self.scoreboard.save_scores()
        self.scoreboard.reset_score()
        
    def player_game_loop(self):
        if self.mode == 'Player':
            while self.isGameRunning == True:
                self.game_loop()
        self.quit()

    def game_loop(self, action=None):
        self.surface.fill(COLORS["game_color"])
        self.snake.draw()
        self.food.draw()
        game_over = False
        
            
            # Control Input
        if self.mode == 'Player':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isGameRunning = False
                self.player_input(event)
        elif self.mode == 'AI':
            self.AI_input(action)
                

        self.snake.move_snake()

        # Display Score
        score_text = self.font.render(str(self.scoreboard.get_score()), True, COLORS['text_color'])
        self.surface.blit(score_text, (300, 50))

        # Collision
        if self.is_Collision(self.snake.get_head()):
            if self.mode == 'Player':
                #isGameRunning = False
                self.snake.reset()
            elif self.mode == 'AI':
                self.snake.reset()
                game_over = True
                reward = -10
                return reward, game_over, self.scoreboard.get_score()
        
        # food Collision
        if compareSquares(self.snake.get_head(), self.food.get_coor(), self.snake.get_length(), self.food.get_length()):
            self.snake.eat_food()
            while self.is_bad_spawn():
                self.food.respawn()
            scoreboard.increase_score()
            reward = 10

        pygame.display.update()    
        self.clock.tick(self.game_speed)
        if self.mode == 'AI':
            return reward, game_over, scoreboard.get_score()

    def player_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake.move_up()
            elif event.key == pygame.K_DOWN:
                self.snake.move_down()
            elif event.key == pygame.K_LEFT:
                self.snake.move_left()
            elif event.key == pygame.K_RIGHT:
                self.snake.move_right()
            if event.key == pygame.K_ESCAPE:
                self.isGameRunning = False
    
    def AI_input(self, action):
        # Move straight ahead
        if np.array_equal(action, [1, 0, 0]):
            pass
        elif np.array_equal(action, [0, 1, 0]):
            self.snake.turn_right()
        elif np.array_equal(action, [0, 0, 1]):
            self.snake.turn_left()

    def quit(self):
        pygame.quit()

    def border_collision(self, point):
        (point.x >= self.width or point.x < 0  or point.y > self.height or point.y < 0)

    def is_Collision(self, point):
        return self.snake.check_in_snake(point, self.snake.get_length()) or self.border_collision(point)

    # Checks if food is spawing inside the self.snake body
    def is_bad_spawn(self):
        if self.snake.check_in_snake(self.food.get_coor(), self.food.get_length()):
            return True
        else:
            return False

    def get_snake_head(self):
        return self.snake.get_head()

    def get__snake_length(self):
        return self.snake.get_length()
    
    def get_snake_direction(self):
        return self.snake.get_direction()

    def get_food_coor(self):
        return self.food.get_coor()
        
