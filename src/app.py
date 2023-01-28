from PIL import Image, ImageDraw

from color import get_random_color, Color, get_color_matrix
from mesh import Resolution, Size, TetragonMesh


def main():
    resolution = Resolution(32, 18)
    size = Size(1920, 1080)
    mesh = TetragonMesh(size, resolution)
    colors = [
        Color(255, 0, 0),
        Color(0, 0, 255),
        Color(255, 0, 255),
        Color(0, 0, 0),
    ]
    matrix = get_color_matrix(colors, resolution)

    image = Image.new("RGB", size)
    drawing = ImageDraw.Draw(image)

    for x in range(resolution.x):
        for y in range(resolution.y):
            tetragon = mesh.get_tetragon(x, y)
            if tetragon:
                drawing.polygon(tetragon.as_primitives(), fill=matrix[x][y])

    image.save("test.png")


if __name__ == "__main__":
    main()
