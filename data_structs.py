from enum import Enum
from collections import namedtuple

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

COLORS = {
    "background": '#C8C2AA',
    "text_color": '#4D493E',
    "light_text": '#f8f4e1',
    "food_color": '#3A6351',
    "snake_color": '#393232',
    "game_color" : '#F2EDD7',
    "box_color": '#897853'
}