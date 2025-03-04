from images import Image

def detectEdges(image,amount):
    def average(triple):
        (r,g,b) =triple
        return (r+g+b) // 3
    blackPixel =(0,0,0)
    whitePixel =(255,255,255)
    new = image.clone()

    for y in range(image.getHeight()-1):
        for x in range(image.getWidth()):
            oldP = image.getPixel(x,y)
            oldL = average(oldP)
            
            if x>0:
                leftP = image.getPixel(x - 1,y)
                leftL = average(leftP)
            else:
                leftL = oldL

            if y< image.getHeight()-1:
                downP = image.getPixel(x,y + 1)
                downL = average(downP)
            else:
                downL = oldL
                
            if abs(oldL - leftL)> amount or \
               abs(oldL - downL)> amount:
                new.setPixel(x,y,blackPixel)
            else:
                new.setPixel(x,y,whitePixel)
    return new

image2 = Image(r"C:\Users\LENOVO\OneDrive\Desktop\Python_Elective\Tutorial-Python\Image_Processing\cat.gif")
detectEdges(image2,30).draw()