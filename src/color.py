import random

from typing import NamedTuple


class Color(NamedTuple):
    r: int
    g: int
    b: int


get_random_color = lambda: Color(
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
)

def get_color_gradient(start: Color, end: Color, n: int):
    r = int((end.r - start.r) / n)
    g = int((end.g - start.g) / n)
    b = int((end.b - start.b) / n)

    return [
        Color(
            start.r + r * i,
            start.g + g * i,
            start.b + b * i,
        )
        for i in range(n)
    ]


def get_color_matrix(colors, resolution):
    g_first = get_color_gradient(colors[0], colors[1], resolution.x)
    g_last = get_color_gradient(colors[3], colors[2], resolution.x)
    cols = []
    for c in range(resolution.x):
        g = get_color_gradient(g_first[c], g_last[c], resolution.y)
        cols.append(g)
    return cols
