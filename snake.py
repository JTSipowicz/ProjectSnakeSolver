import pygame
import numpy as np
import copy
from data_structs import Direction, Point

class Snake:
    def __init__(self, surface, color, block_size, width, height):
        self.surface = surface
        self.color = color
        self.direction = Direction.RIGHT
        self.block_size = block_size
        self.head = copy.deepcopy(Point(width / 2, height / 2))
        self.segments = copy.deepcopy([self.head,
                      Point(self.head.x - self.block_size, self.head.y),
                      Point(self.head.x -(2 * self.block_size), self.head.y)])
        print(self.head)
        print(self.segments)
        
        
    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(self.surface, self.color, pygame.Rect(self.head.x, self.head.y, self.block_size, self.block_size))

    def reset(self, width, height):
        self.direction = Direction.RIGHT
        self.head = copy.deepcopy(Point(width / 2, height / 2))
        self.segments = copy.deepcopy([self.head,
                      Point(self.head.x - self.block_size, self.head.y),
                      Point(self.head.x - (2 * self.block_size), self.head.y)])

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

        x = copy.deepcopy(self.head.x)
        y = copy.deepcopy(self.head.y)
        if self.direction == Direction.RIGHT:
            x += self.block_size
        elif self.direction == Direction.LEFT:
            x -= self.block_size
        elif self.direction == Direction.DOWN:
            y += self.block_size
        elif self.direction == Direction.UP:
            y -= self.block_size


        temp_point = Point(x, y)
        self.head = copy.deepcopy(temp_point)
    
    def insert(self):
        temp_point = copy.deepcopy(self.head)
        self.segments.insert(0, temp_point)

    def get_length(self):
        return len(self.segments)

    def pop(self):
        self.segments.pop()

    def get_head(self):
        return self.head

    def set_head(self, point):
        self.head = copy.deepcopy(point)
    
    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def get_size(self):
        return self.block_size
    
    def is_in_segments(self, point):
        if point in self.segments[1:]:
            return True
