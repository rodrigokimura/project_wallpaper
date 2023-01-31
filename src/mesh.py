from typing import List, NamedTuple

from commons import Point, Resolution, Size


class Tetragon(NamedTuple):
    a: Point
    b: Point
    c: Point
    d: Point

    def as_primitives(self):
        return [(p.x, p.y) for p in self]

    def centroid(self):
        x = int(sum(p.x for p in self) / 4)
        y = int(sum(p.y for p in self) / 4)
        return Point(x, y)


class TetragonMesh:
    size: Size
    _tetragons: List[List[Tetragon]]

    def __init__(self, size: Size, resolution: Resolution, distortion: float = 0.2):
        self.resolution = resolution
        width = int(size.width / resolution.x)
        height = int(size.height / resolution.y)
        _points = [
            [Point(col * width, row * height) for col in range(resolution.x + 1)]
            for row in range(resolution.y + 1)
        ]

        distortion_range_x = (-int(width * distortion), int(width * distortion))
        distortion_range_y = (-int(height * distortion), int(height * distortion))

        self._tetragons = []
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
            self._tetragons.append(tetragon_row)

    @property
    def tetragons(self):
        for x in range(self.resolution.x):
            for y in range(self.resolution.y):
                yield self._tetragons[x][y]
