from turtle import Turtle

def star(t,length):
    t.down()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(75)
    t.forward(length)
    for count in range(4):
        t.left(144)
        t.forward(length)
    t.end_fill()

def pattern(t,length,star,num):  
    angle=360/num
    for count in range(num):
        t.up()
        cur_angle = count * angle
        t.right(cur_angle)
        t.forward(length*2)  
        t.left(cur_angle)
        star(t,length)
        t.up()
        t.home()


num = int(input("Enter the no of stars:"))
length = int(input("Enter the length:"))
t = Turtle()
pattern(t,length,star,num)
