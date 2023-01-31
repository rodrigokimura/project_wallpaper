import random
from typing import NamedTuple, Tuple


class Size(NamedTuple):
    width: int
    height: int


class Resolution(NamedTuple):
    x: int
    y: int


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def as_tuple(self):
        return (self.x, self.y)

    def distort(self, x_range: Tuple[int, int], y_range: Tuple[int, int]):
        self.x = self.x + random.randint(*x_range)
        self.y = self.y + random.randint(*y_range)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"
