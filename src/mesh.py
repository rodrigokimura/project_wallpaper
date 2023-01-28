import random
from typing import List, NamedTuple, Tuple


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

    def distort(self, x_range: Tuple[int, int], y_range: Tuple[int, int]):
        self.x = self.x + random.randint(*x_range)
        self.y = self.y + random.randint(*y_range)


class Tetragon(NamedTuple):
    a: Point
    b: Point
    c: Point
    d: Point

    def as_primitives(self):
        return [(p.x, p.y) for p in self]


class TetragonMesh:
    size: Size
    tetragons: List[List[Tetragon]]

    def __init__(self, size: Size, resolution: Resolution, distortion: float = 0.2):
        width = int(size.width / resolution.x)
        height = int(size.height / resolution.y)
        _points = [
            [Point(col * width, row * height) for col in range(resolution.x + 1)]
            for row in range(resolution.y + 1)
        ]

        distortion_range_x = (-int(width * distortion), int(width * distortion))
        distortion_range_y = (-int(height * distortion), int(height * distortion))

        self.tetragons = []
        for col in range(resolution.x):
            tetragon_row = []
            for row in range(resolution.y):
                a = _points[row][col]
                b = _points[row][col + 1]
                c = _points[row + 1][col + 1]
                d = _points[row + 1][col]
                if row != 0 and col != 0:
                    a.distort(distortion_range_x, distortion_range_y)
                if row != 0 and col != resolution.x - 1:
                    b.distort(distortion_range_x, distortion_range_y)
                if row != resolution.y - 1 and col != resolution.x - 1:
                    c.distort(distortion_range_x, distortion_range_y)
                if row != resolution.y - 1 and col != 0:
                    d.distort(distortion_range_x, distortion_range_y)
                tetragon_row.append(Tetragon(a, b, c, d))
            self.tetragons.append(tetragon_row)

    def get_tetragon(self, x: int, y: int):
        try:
            return self.tetragons[x][y]
        except IndexError:
            return None
