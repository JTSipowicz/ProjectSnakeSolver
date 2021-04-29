import pygame
import random
from data_structs import *
from scoreboard import Scoreboard
from food import Food
import numpy as np

pygame.init()
font = pygame.font.SysFont('arial', 25)

SPEED = 40
HUMAN_SPEED = 20
BLOCK_SIZE = 20

class SnakeGame:
    def __init__(self, scoreboard, w=400, h=400):
        self.w = w
        self.h = h
        self.scoreboard = scoreboard
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        self.food = Food(self.display, COLORS["food_color"], 20, self.w, self.h)
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        # init game state
        self.direction = Direction.RIGHT
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2 * BLOCK_SIZE), self.head.y)]
        #self.snake.reset(self.w, self.h)
        self.scoreboard.update()
        self.scoreboard.save_scores()
        self.scoreboard.reset()
        self.food.spawn()
        self.frame_iteration = 0

    def play_step(self, action):
        self.frame_iteration += 1
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # 2. move
        self.move(action) # update the head
        self.snake.insert(0, self.head)     # temp change
        
        # 3. check if game over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.scoreboard.get_score()

        # 4. place new food or just move
        if self.head == self.food.get_coor():
            self.scoreboard.increase()
            reward = 10
            self.food.spawn()
        else:
            self.snake.pop()
        
        # 5. update ui and clock
        self.update()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return reward, game_over, self.scoreboard.get_score()

    def game_loop(self):
        isGameRunning = True
        self.reset()
        while isGameRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.move_down()
                    elif event.key == pygame.K_LEFT:
                        self.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.move_right()
                    if event.key == pygame.K_ESCAPE:
                        isGameRunning = False

            self.player_move()
            self.snake.insert(0, self.head)
            
            if self.is_collision():
                self.reset()

            if self.head == self.food.get_coor():
                self.scoreboard.increase()
                self.food.spawn()
            else:
                self.snake.pop()
            
            self.update()
            self.clock.tick(HUMAN_SPEED)

        pygame.quit()

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # hits boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # hits itself
        if pt in self.snake[1:]:
            return True

        return False

    def update(self):
        self.display.fill(COLORS["background"])
        for pt in self.snake:
            pygame.draw.rect(self.display, COLORS["snake_color"], pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
        self.food.draw()
        text = font.render(str(self.scoreboard.get_score()), True, COLORS["text_color"])
        self.display.blit(text, [self.w / 2, 30])
        pygame.display.flip()

    def  player_move(self):
        x = self.head.x
        y = self.head.y
        if self.direction == Direction.UP:
            y -= BLOCK_SIZE
        if self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        if self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        
        self.head = Point(x, y)

    def move(self, action):
        # [straight, right, left]

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)
    
    def move_up(self):
        if self.direction != Direction.DOWN:
            self.direction = Direction.UP
    def move_down(self):
        if self.direction != Direction.UP:
            self.direction = Direction.DOWN
    def move_left(self):
        if self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
    def move_right(self):
        if self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def get_food_cor(self):
        return self.food.get_coor()