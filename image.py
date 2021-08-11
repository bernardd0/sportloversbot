from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# Retornar o endereço relativo dentro da pasta 'input'
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

def triangle(size):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    image = Image.new("RGB", (size, size), (WHITE))

    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x, y), BLACK)
    return image

def france_flag(height):
    BLUE = (0, 85, 164)
    RED = (239, 65, 53)
    WHITE = (255, 255, 255)
    width = 3*height//2

    image = Image.new("RGB", (width, height), WHITE)

    offset = width//3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2*offset, y), RED)
    return image

def japanese_flag(height):
    WHITE = (255, 255, 255)
    RED = (173, 35, 51)
    width = 3*height//2
    r = 3*height//10
    c = (width//2, height//2)

    image = Image.new("RGB", (width, height), WHITE)

    for x in range(c[0]-r, c[0]+r):
        for y in range(c[1]-r, c[1]+r):
            if (x-c[0])**2 + (y-c[1])**2 <= r**2:
                image.putpixel((x, y), RED)
    return image

if __name__ == "__main__":
    flag = japanese_flag(300)

    flag.show()