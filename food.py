import pygame
import random
from data_structures import Point

FOOD_LENGTH = 20
BORDER = 40

class Food:
    def __init__(self, surface, color, screen_width, screen_height):
        self.surface = surface
        self.color = color
        self.width_bound = screen_width
        self.height_bound = screen_height
        self.position = Point(random.randrange(BORDER, (self.width_bound - BORDER)), random.randrange(BORDER, (self.height_bound - BORDER)))


    def respawn(self):
        self.position = Point(random.randrange(BORDER, (self.width_bound - BORDER)), random.randrange(BORDER, (self.height_bound - BORDER)))

    def draw(self):
        pygame.draw.rect(self.surface, self.color, [self.position.x, self.position.y, FOOD_LENGTH, FOOD_LENGTH])

    def get_coor(self):
        return self.position
    
    def get_length(self):
        return FOOD_LENGTH