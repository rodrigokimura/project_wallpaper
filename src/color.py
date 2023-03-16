import random
from abc import ABC, abstractmethod
from typing import NamedTuple, Tuple

from commons import Point


class Color(NamedTuple):
    r: int
    g: int
    b: int

    @staticmethod
    def from_hex(hex: str):
        hex = hex.lstrip("#")
        return Color(*tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4)))


def get_random_color():
    return Color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


def normalize_channel(n: int):
    if n < 0:
        return 0
    if n > 255:
        return 255
    return n


def get_color_from_relative_distance_multiple(colors: Tuple[Color, ...], d: float):
    if not colors:
        return None
    distance_between_colors = 1 / (len(colors) - 1)
    first_color_index = int(d / distance_between_colors)
    first_color = colors[first_color_index]
    second_color = colors[first_color_index + 1]
    d = (d % distance_between_colors) / distance_between_colors
    return get_color_from_relative_distance(first_color, second_color, d)


def get_color_from_relative_distance(start: Color, end: Color, d: float):
    """
    d == 0 -> closest to start
    """
    r = normalize_channel(start.r + int((end.r - start.r) * d))
    g = normalize_channel(start.g + int((end.g - start.g) * d))
    b = normalize_channel(start.b + int((end.b - start.b) * d))
    return Color(r, g, b)


def get_color_gradient(start: Color, end: Color, n: int):
    return [get_color_from_relative_distance(start, end, i / n) for i in range(n)]


def get_color_matrix(colors, resolution):
    g_first = get_color_gradient(colors[0], colors[1], resolution.x)
    g_last = get_color_gradient(colors[3], colors[2], resolution.x)
    cols = []
    for c in range(resolution.x):
        g = get_color_gradient(g_first[c], g_last[c], resolution.y)
        cols.append(g)
    return cols


class Gradient(ABC):
    @abstractmethod
    def get_color(self, point: Point):
        pass


class LineGradient(Gradient):
    start: Point
    end: Point
    colors: Tuple[Color, ...]

    @staticmethod
    def from_points(start: Point, end: Point, colors: Tuple[Color, ...]):
        gradient = LineGradient()
        gradient.start = start
        gradient.end = end
        gradient.colors = colors
        return gradient

    @staticmethod
    def from_slope(start: Point, slope: float, length: int, colors: Tuple[Color, ...]):
        import math

        slope = slope * math.pi / 180

        gradient = LineGradient()
        gradient.start = start
        gradient.end = Point(
            int(length * math.sin(slope)) + start.x,
            int(length * math.cos(slope)) + start.y,
        )
        gradient.colors = colors
        return gradient

    def get_color(self, point: Point):
        from skspatial.objects import Line
        from skspatial.objects import Point as _Point

        line = Line.from_points(
            point_a=self.start.as_tuple(), point_b=self.end.as_tuple()
        )
        projected_point = line.project_point(point.as_tuple())
        distance_from_start = projected_point.distance_point(self.start.as_tuple())
        total_distance = _Point(self.start.as_tuple()).distance_point(
            self.end.as_tuple()
        )
        return get_color_from_relative_distance_multiple(
            self.colors, float(distance_from_start / total_distance)
        )


class RadialGradient(Gradient):
    def __init__(self, center: Point, radius: int, colors: Tuple[Color, ...]) -> None:
        self.center = center
        self.radius = radius
        self.colors = colors

    def get_color(self, point: Point):
        from skspatial.objects import Point as _Point

        distance_from_center = _Point(self.center.as_tuple()).distance_point(
            point.as_tuple()
        )
        return get_color_from_relative_distance_multiple(
            self.colors, float(distance_from_center / self.radius)
        )
