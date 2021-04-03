import pygame
import time

from scoreboard import Scoreboard
from colors import COLORS
from snake import Snake
from food import Food
from math_functions import compareSquares

def game_loop(scoreboard, mode):
    pygame.init()
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400

    GAME_SPEED = 10
    isGameRunning = True

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    font = pygame.font.SysFont(None, 24)

    clock = pygame.time.Clock()

    snake = Snake(surface, COLORS["snake_color"], SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    food = Food(surface, COLORS["food_color"], SCREEN_WIDTH, SCREEN_HEIGHT)
    if mode == 'Player':
        scoreboard.set_type_Player()

    while isGameRunning:
        surface.fill(COLORS["game_color"])
        snake.draw_snake()
        food.draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False
            
            # Control Input
            if mode == 'Player':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.move_up()
                    elif event.key == pygame.K_DOWN:
                        snake.move_down()
                    elif event.key == pygame.K_LEFT:
                        snake.move_left()
                    elif event.key == pygame.K_RIGHT:
                        snake.move_right()
                    if event.key == pygame.K_ESCAPE:
                        isGameRunning = False
                    if event.key == pygame.K_SPACE:
                        pygame.time.wait(30000)
            elif mode == 'AI':
                pass

        snake.move_snake()

        # Display Score
        score_text = font.render(str(scoreboard.get_score()), True, COLORS['text_color'])
        surface.blit(score_text, (300, 50))

        # Boundary Collision
        if snake.get_X() >= SCREEN_WIDTH or snake.get_X() < 0 or snake.get_Y() > SCREEN_HEIGHT or snake.get_Y() < 0:
            isGameRunning = False
            scoreboard.update()
            scoreboard.save_scores()
            scoreboard.reset_score()

        # Self Collision
        if snake.check_self_collision():
            isGameRunning = False
            scoreboard.update()
            scoreboard.save_scores()
            scoreboard.reset_score()
        
        # Food Collision
        if compareSquares(snake.get_X(), food.get_X(), snake.get_Y(), food.get_Y(), snake.get_length(), food.get_length()):
            snake.eat_food()
            food.respawn()
            scoreboard.increase_score()

        pygame.display.update()    
        clock.tick(GAME_SPEED)


    pygame.quit()
