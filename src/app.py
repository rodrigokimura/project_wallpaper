from PIL import Image, ImageDraw

from color import get_random_color
from mesh import Resolution, Size, TetragonMesh


def main():
    resolution = Resolution(32, 18)
    size = Size(1920, 1080)
    mesh = TetragonMesh(size, resolution)

    image = Image.new("RGB", size)
    drawing = ImageDraw.Draw(image)

    for x in range(resolution.x):
        for y in range(resolution.y):
            tetragon = mesh.get_tetragon(x, y)
            if tetragon:
                drawing.polygon(tetragon.as_primitives(), fill=get_random_color())

    image.show()


if __name__ == "__main__":
    main()
