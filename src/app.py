import sys
from typing import Tuple

import typer
from PIL import Image, ImageDraw

from color import Color, LineGradient
from commons import Point
from mesh import Resolution, Size, TetragonMesh


def main(
    filename: str = typer.Argument(...),
    resolution: Tuple[int, int] = typer.Option((16, 9)),
    size: Tuple[int, int] = typer.Option((1920, 1080)),
    start: Tuple[int, int] = typer.Option((0, 0)),
    end: Tuple[int, int] = typer.Option((1920, 1080)),
    colors: Tuple[str, str] = typer.Option(("#a8df20", "#733b8c")),
):
    """
    Simple wallpaper generator.
    """
    resolution = Resolution(*resolution)
    size = Size(*size)
    mesh = TetragonMesh(size, resolution)
    gradient = LineGradient.from_points(
        Point(*start),
        Point(*end),
        (Color.from_hex(colors[0]), Color.from_hex(colors[1])),
    )

    image = Image.new("RGB", size)
    drawing = ImageDraw.Draw(image)

    for tetragon in mesh.tetragons:
        color = gradient.get_color(tetragon.centroid())
        drawing.polygon(tetragon.as_primitives(), fill=color)

    image.save(filename)


if __name__ == "__main__":
    typer.run(main)
