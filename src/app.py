from typing import List, Tuple

import typer
from PIL import Image, ImageDraw

from color import Color, RadialGradient
from commons import Point
from mesh import Resolution, Size, TetragonMesh


def main(
    filename: str = typer.Argument(..., help="Output filename"),
    colors: List[str] = typer.Argument(..., help="List of hex colors"),
    polygons: Tuple[int, int] = typer.Option((16, 9)),
    size: Tuple[int, int] = typer.Option((1920, 1080)),
    center: Tuple[int, int] = typer.Option((0, 0)),
    radius: int = typer.Option(2100),
):
    """
    Simple wallpaper generator.
    """
    polygons = Resolution(*polygons)
    size = Size(*size)
    mesh = TetragonMesh(size, polygons)
    gradient = RadialGradient(
        Point(*center), radius, tuple(Color.from_hex(color) for color in colors)
    )

    image = Image.new("RGB", size)
    drawing = ImageDraw.Draw(image)

    for tetragon in mesh.tetragons:
        color = gradient.get_color(tetragon.centroid())
        drawing.polygon(tetragon.as_primitives(), fill=color)

    image.save(filename)


if __name__ == "__main__":
    typer.run(main)
