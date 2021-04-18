import pygame
from math_functions import compareSquares
from data_structures import Point

LENGTH = 10
STEP_DISTANCE = 10

class Snake:
    def __init__(self, surface, color, width, height):
        self.surface = surface
        self.color = color
        self.head = Point(width / 2, height / 2)
        self.hasEaten = False
        self.direction = 'RIGHT'
        self.segments = [Point(width, height), 
                        Point(width - LENGTH, height), 
                        Point(width - (LENGTH * 2), height), 
                        Point(width - (LENGTH * 3), height)]

    def draw(self):
        for seg in self.segments:
            pygame.draw.rect(self.surface, self.color,[seg.x, seg.y, LENGTH, LENGTH])
            
    
    def move_snake(self):
        if self.direction == 'UP':
            self.head.y -= STEP_DISTANCE
        if self.direction == 'DOWN':
            self.head.y += STEP_DISTANCE
        if self.direction == 'LEFT':
            self.head.x -= STEP_DISTANCE
        if self.direction == 'RIGHT':
            self.head.x += STEP_DISTANCE

        # Required syntax to avoid shallow copy
        new_point = Point(self.head.x, self.head.y)
        self.segments.insert(0, new_point)
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
    
    def turn_right(self):
        if self.direction != 'RIGHT':
            self.direction = 'DOWN'
        if self.direction != 'UP':
            self.direction = 'RIGHT'
        if self.direction != 'LEFT':
            self.direction = 'UP'
        if self.direction != 'DOWN':
            self.direction = 'LEFT'
    
    def turn_left(self):
        if self.direction != 'RIGHT':
            self.direction = 'UP'
        if self.direction != 'UP':
            self.direction = 'LEFT'
        if self.direction != 'DOWN':
            self.direction = 'UP'
        if self.direction != 'DOWN':
            self.direction = 'RIGHT'
        
    def eat_food(self):
        self.hasEaten = True
    
    def check_self_collision(self):
        for segment in self.segments[1:]:
            if self.head.x == segment.x and self.head.y == segment.y:
                return True
        return False

    def check_in_snake(self, point, point_length):
        for segment in self.segments:
            if compareSquares(segment, point, LENGTH, point_length):
                return True
        return False

    def reset(self):
        self.head = Point(300, 200)
        self.segments = [Point(300, 200), Point(300 - LENGTH, 200), Point(300 - (LENGTH * 2), 200), Point(300 - (LENGTH * 3), 200)]
        self.direction = 'RIGHT'

    def get_length(self):
        return LENGTH
    def get_direction(self):
        return self.direction
    def get_head(self):
        return self.head