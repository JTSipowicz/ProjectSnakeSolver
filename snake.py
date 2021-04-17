import pygame
from math_functions import compareSquares

LENGTH = 10
STEP_DISTANCE = 10

class Snake:
    def __init__(self, surface, color, width, height):
        self.surface = surface
        self.color = color
        self.head = [width, height]
        self.hasEaten = False
        self.direction = 'RIGHT'
        self.segments = [[width, height], 
                        [width - LENGTH, height], 
                        [width - (LENGTH * 2), height], [width - (LENGTH * 3), height]]
        self.draw_snake()

    def draw_snake(self):
        for seg in self.segments:
            pygame.draw.rect(self.surface, self.color,[seg[0], seg[1], LENGTH, LENGTH])
            
    
    def move_snake(self):
        if self.direction == 'UP':
            self.head[1] -= STEP_DISTANCE
        if self.direction == 'DOWN':
            self.head[1] += STEP_DISTANCE
        if self.direction == 'LEFT':
            self.head[0] -= STEP_DISTANCE
        if self.direction == 'RIGHT':
            self.head[0] += STEP_DISTANCE

        # Updating Segments, [:] required to avoid shallow copy bug
        self.segments.insert(0, self.head[:])
        if self.hasEaten:
            self.hasEaten = False
        else:
            self.segments.pop()
            
    
    def move_up(self):
        if self.direction != 'DOWN':
            self.direction = 'UP'
    def move_down(self):
        if self.direction != 'UP':
            self.direction = 'DOWN'
    def move_left(self):
        if self.direction != 'RIGHT':
            self.direction = 'LEFT'
    def move_right(self):
        if self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def eat_food(self):
        self.hasEaten = True
    
    def check_self_collision(self):
        for segment in self.segments[1:]:
            if self.head[0] == segment[0] and self.head[1] == segment[1]:
                return True
        return False

    def reset_snake(self):
        self.head = [300, 200]
        self.segments = [[300, 200], [300 - LENGTH, 200], [300 - (LENGTH * 2), 200], [300 - (LENGTH * 3), 200]]
        self.direction = 'RIGHT'

    def get_length(self):
        return LENGTH
    def get_direction(self):
        return self.direction
    def get_X(self):
        return self.head[0]
    def get_Y(self):
        return self.head[1]