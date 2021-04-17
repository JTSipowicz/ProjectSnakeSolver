from dataclasses import dataclass

@dataclass
class Rect:
    right: int
    top: int
    left: int
    down: int 

@dataclass
class Point:
    x: int
    y: int