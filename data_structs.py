from enum import Enum
from collections import namedtuple

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

COLORS = {
    "background": '#000000',
    "text_color": '#FFD700',
    "light_text": '#FFC0CB',
    "food_color": '#FFFFFF',
    "snake_color": '#50C878',
    "game_color" : '#0000FF',
    "box_color": '#800080'
}