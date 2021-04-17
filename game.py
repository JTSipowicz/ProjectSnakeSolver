import pygame
import time

from scoreboard import Scoreboard
from colors import COLORS
from snake import Snake
from food import Food
from math_functions import compareSquares
from data_structures import Point

# Reset
# Reward
# Play() -> Direction
# Game_iteration
# is_Collision

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GAME_SPEED = 30



clock = pygame.time.Clock()
class Game:

    def __init__(self):
        pass
        
        
    def game_loop(self, scoreboard, mode):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        font = pygame.font.SysFont(None, 24)
        isGameRunning = True
        self.snake = Snake(self.surface, COLORS["snake_color"], SCREEN_WIDTH, SCREEN_HEIGHT)
        self.food = Food(self.surface, COLORS["food_color"], SCREEN_WIDTH, SCREEN_HEIGHT)

        if mode == 'Player':
            scoreboard.set_type_Player()
        else:
            scoreboard.set_type_AI()

        while isGameRunning:
            self.surface.fill(COLORS["game_color"])
            self.snake.draw_snake()
            self.food.draw()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isGameRunning = False
                
                # Control Input
                if mode == 'Player':
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
                            isGameRunning = False
                elif mode == 'AI':
                    pass
                    

            self.snake.move_snake()

            # Display Score
            score_text = font.render(str(scoreboard.get_score()), True, COLORS['text_color'])
            self.surface.blit(score_text, (300, 50))

            # Boundary Collision
            if (self.snake.get_head().x >= SCREEN_WIDTH or self.snake.get_head().x < 0 
                or self.snake.get_head().y > SCREEN_HEIGHT or self.snake.get_head().y < 0):
                if mode == 'Player':
                    #isGameRunning = False
                    self.snake.reset_snake()
                    while self.is_bad_spawn():
                        self.food.respawn()
                else:
                    pass
                scoreboard.update()
                scoreboard.save_scores()
                scoreboard.reset_score()

            # Self Collision
            if self.snake.check_self_collision():
                if mode == 'Player':
                    #isGameRunning = False
                    self.snake.reset_self.snake()
                    while self.is_bad_spawn():
                        self.food.respawn()
                else:
                    pass
                scoreboard.update()
                scoreboard.save_scores()
                scoreboard.reset_score()
            
            # food Collision
            if compareSquares(self.snake.get_head(), self.food.get_coor(), self.snake.get_length(), self.food.get_length()):
                self.snake.eat_food()
                while self.is_bad_spawn():
                    self.food.respawn()
                scoreboard.increase_score()

            pygame.display.update()    
            clock.tick(GAME_SPEED)
        
        pygame.quit()

    # Checks if food is spawing inside the self.snake body
    def is_bad_spawn(self):
        if self.snake.check_in_snake(self.food.get_coor(), self.food.get_length()):
            return True
        else:
            return False
        
