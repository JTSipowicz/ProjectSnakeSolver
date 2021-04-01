import pygame
import time
import random
from snake import Snake
from food import Food
from math_functions import compareSquares

pygame.init()

GREEN = (0, 255, 0)
BLUE = (50, 150, 210)
WHITE = (0, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

GAME_SPEED = 10

surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snek Game")

clock = pygame.time.Clock()

def game_loop():
    isAppRunning = True
    isGameRunning = True

    snake = Snake(surface, GREEN, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    food = Food(surface, BLUE, SCREEN_WIDTH, SCREEN_HEIGHT)

    while isGameRunning:
        surface.fill(WHITE)
        snake.draw_snake()
        food.draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False
            
            # Control Input
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
                    # For debugging purposes
                    coordinates = [(snake.get_X(), snake.get_Y()), (food.get_X(), food.get_Y())]
                    print(coordinates)

        snake.move_snake()

        # Boundary Collision
        if snake.get_X() >= SCREEN_WIDTH or snake.get_X() < 0 or snake.get_Y() > SCREEN_HEIGHT or snake.get_Y() < 0:
            isGameRunning = False

        # Self Collision
        if snake.check_self_collision():
            isGameRunning = False
        
        # Food Collision
        if compareSquares(snake.get_X(), food.get_X(), snake.get_Y(), food.get_Y(), snake.get_length(), food.get_length()):
            snake.eat_food()
            food.respawn()

        pygame.display.update()    
        clock.tick(GAME_SPEED)


    pygame.quit()
    quit()

game_loop()