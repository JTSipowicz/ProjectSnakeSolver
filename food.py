import pygame
import random

FOOD_LENGTH = 20
BORDER = 40

class Food:
    def __init__(self, surface, color, screen_width, screen_height):
        self.surface = surface
        self.color = color
        self.width_bound = screen_width
        self.height_bound = screen_height
        self.position = [random.randrange(BORDER, (self.width_bound - BORDER)), random.randrange(BORDER, (self.height_bound - BORDER))]


    def respawn(self):
        self.position = [random.randrange(BORDER, (self.width_bound - BORDER)), random.randrange(BORDER, (self.height_bound - BORDER))]

    def draw(self):
        pygame.draw.rect(self.surface, self.color, [self.position[0], self.position[1], FOOD_LENGTH, FOOD_LENGTH])

    def get_X(self):
        return self.position[0]
    
    def get_Y(self):
        return self.position[1]
    
    def get_length(self):
        return FOOD_LENGTH