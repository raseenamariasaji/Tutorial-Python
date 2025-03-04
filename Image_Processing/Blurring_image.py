from images import Image
from functools import reduce

image=Image(r"C:\Users\LENOVO\OneDrive\Desktop\Python_Elective\Tutorial-Python\Image_Processing\cat.gif")

def blur(image):
    def Sum(tri0, tri1):
        (r0, g0, b0) = tri0
        (r1, g1, b1) = tri1
        return (r0 + r1, g0 + g1, b0 + b1)

    new = image.clone()  # Make sure clone() works; otherwise, use copy()
    
    for y in range(1, image.getHeight() - 1):
        for x in range(1, image.getWidth() - 1):
            oldP = image.getPixel(x, y)
            left = image.getPixel(x - 1, y)
            right = image.getPixel(x + 1, y)
            top = image.getPixel(x, y - 1)
            bottom = image.getPixel(x, y + 1)
            sums = reduce(Sum, [oldP, left, right, top, bottom])
            avg = tuple(map(lambda x: x // 5, sums))
            new.setPixel(x, y, avg)

    new.draw()

blur(image)
