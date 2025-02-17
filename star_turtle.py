from turtle import Turtle
t = Turtle()
num = int(input("Enter the no of stars:"))
length = int(input("Enter the length:"))
def star(t,length):
    t.down()
    t.right(75)
    t.forward(length)
    for count in range(4):
        t.down()
        t.left(144)
        t.forward(length)
        
for count in range(num):
    star(t,length)
    angle=360/num
    t.up()
    t.forward(length*2)  
    t.right(angle)


   
    
    
