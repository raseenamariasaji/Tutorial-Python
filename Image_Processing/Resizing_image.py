
from images import Image
from functools import reduce

def shrink(image,factor):
    width = image.getWidth()
    height = image.getHeight()
    new = Image(width // factor,height // factor)
    oldY = 0
    newY = 0
    while oldY < height - factor:
        oldX = 0
        newX = 0
        while oldX < width - factor:
            oldP = image.getPixel(oldX,oldY)
            new.setPixel(newX,newY,oldP)
            oldX += factor
            newX += 1
        oldY += factor
        newY += 1
    return new

image3 = Image(r"C:\Users\LENOVO\OneDrive\Desktop\Python_Elective\Tutorial-Python\Image_Processing\cat.gif")
shrink(image3,5).draw()

