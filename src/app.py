import sys

from PIL import Image, ImageDraw

from color import Color, LineGradient
from commons import Point
from mesh import Resolution, Size, TetragonMesh


def main():
    resolution = Resolution(16, 9)
    size = Size(1920, 1080)
    mesh = TetragonMesh(size, resolution)
    gradient = LineGradient.from_slope(
        Point(0, 0), 30, 2000, (Color(168, 233, 32), Color(107, 35, 156))
    )

    image = Image.new("RGB", size)
    drawing = ImageDraw.Draw(image)

    for x in range(resolution.x):
        for y in range(resolution.y):
            tetragon = mesh.get_tetragon(x, y)
            color = gradient.get_color(tetragon.centroid())
            drawing.polygon(tetragon.as_primitives(), fill=color)

    if len(sys.argv) > 1:
        image.save(sys.argv[1])
    else:
        image.show()


if __name__ == "__main__":
    main()
