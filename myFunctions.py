import turtle
from random import *
bob = turtle.Turtle()
bob.speed(0)
turtle.colormode(255)

#Shapes and structures

def polygon(dist,sides):
    angle=360/sides

    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)

def iso_tri(c):
    bob.color(c)
    bob.begin_fill()
    bob.forward(30)
    bob.left(100)
    bob.forward(20)
    bob.left(110)
    bob.forward(38)
    bob.end_fill()
    
def rectangle(size,c):
    bob.color(c)
    bob.begin_fill()
    bob.forward(size)
    bob.left(90)
    bob.forward(50+size)
    bob.left(90)
    bob.forward(size)
    bob.left(90)
    bob.forward(50+size)
    bob.end_fill()

def polygonFill(dist,sides,border,fill):
    angle=360/sides
    bob.pencolor(border)
    bob.fillcolor(fill)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)
    bob.end_fill()



def stair(dist,steps):
    for times in range(steps):
        bob.forward(dist)
        bob.left(90)
        bob.forward(dist)
        bob.right(90)


def comet(dist,angle,repeat):
    for times in range(repeat):
        bob.pensize(times*2)
        bob.forward(dist)
        bob.left(angle)
    




#Commands

def ghostwalk(dist):
    bob.penup()
    bob.forward(dist)
    bob.pendown()
    
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def home():
    bob.penup()
    bob.home()
    bob.pendown()



#Complex Functions

def dandelion(x,y,dist):
    jump(x,y)
    bob.setheading(0)
    rectangle(4,"green")
    bob.color(240,240,230)
    bob.setheading(0)
    jump(x+2,y+40)
    bob.begin_fill()
    for times in range(60):
        bob.forward(dist)
        bob.left(3)
        bob.forward(dist)
        bob.left(3)
        bob.forward(dist)
        bob.left(3)
        bob.forward(dist)
        bob.left(3)
        bob.forward(dist)
        bob.left(3)
        bob.forward(dist)
        bob.left(3)
        bob.stamp()
    bob.end_fill()
def petal(x,y,c):
    jump(x,y)
    bob.color(c)
    bob.begin_fill()
    comet(4,0,5)
    jump(x,y)
    bob.end_fill()
def nightshade(x,y):
    jump(x,y)
    c=(200,170,240)
    c2=(200,140,240)
    for times in range(14):
        bob.left(75)
        petal(x,y,c)
        jump(x,y)
    jump(x,y)
    bob.setheading(0)
    bob.left(3)
    for times in range(5):
        bob.left(75)
        petal(x,y,c2)
        jump(x,y)
def grass(length,c,x,y):
    bob.color(c)
    jump(x,y)
    bob.setheading(90)
    bob.begin_fill()
    bob.forward(length)
    bob.end_fill()
    jump(x-10,y)
    bob.setheading(90)
    bob.left(20)
    bob.begin_fill()
    bob.forward(length)
    bob.end_fill()
    jump(x-20,y)
    bob.setheading(90)
    bob.begin_fill()
    bob.right(10)
    bob.forward(length)
    bob.end_fill()
def grass2(length,c,x,y):
    bob.color(c)
    jump(x,y)
    bob.setheading(90)
    bob.begin_fill()
    bob.forward(length)
    bob.end_fill()
    jump(x-10,y)
    bob.setheading(90)
    bob.left(20)
    bob.begin_fill()
    bob.forward(length)
    bob.end_fill()
    


def arch(repeat,dist,sides,turn):
    for times in range(repeat):
        bob.begin_fill()
        bob.color(225-times,225-times,225-times)
        polygon(dist,sides)
        bob.left(turn)
        bob.forward(10)
        bob.end_fill()
        
def hill(size,c):
    bob.begin_fill()
    bob.color(c)
    bob.circle(size)
    bob.end_fill()

def sheep(x,y):
    bob.setheading(0)
    fill=(30,30,30)
    fill2=(50,50,50)
    # Front limb 1 
    jump(x-35,y-80)
    bob.left(30)
    polygonFill(10,3,fill,fill)
    jump(x-29,y-83)
    bob.left(2)
    polygonFill(10,3,fill,fill)
    jump(x-35,y-70)
    bob.setheading(332)
    rectangle(15,fill)
    # Front limb 2
    bob.setheading(0)
    jump(x-15,y-81)
    bob.left(30)
    polygonFill(10,3,fill2,fill2)
    jump(x-9,y-84)
    bob.left(2)
    polygonFill(10,3,fill2,fill2)
    jump(x-14,y-71)
    bob.setheading(332)
    rectangle(15,fill2)
    # Back limb 1
    jump(x+98,y-86)
    bob.left(210)
    polygonFill(10,3,fill2,fill2)
    jump(x+104,y-74)
    bob.left(120)
    polygonFill(10,3,fill2,fill2)
    jump(x+82,y-15)
    bob.setheading(200)
    rectangle(15,fill2)
    # Back limb 2
    bob.setheading(0)
    jump(x+125,y-70)
    bob.left(210)
    polygonFill(10,3,fill,fill)
    jump(x+110,y-78)
    bob.left(120)
    polygonFill(10,3,fill,fill)
    jump(x+102,y-11)
    bob.setheading(200)
    rectangle(15,fill)
    # Tail
    jump(x+115,y)
    bob.setheading(0)
    for times in range(20):
        bob.color(fill)
        bob.begin_fill()
        bob.circle(10)
        bob.left(3)
        bob.forward(1)
        bob.end_fill()
    # Body
    co=randint(200,240)
    co2=randint(200,240)
    co3=randint(200,240)
    co_all=(co,co2,co3)
    for times in range(3):
        bob.setheading(0)
        jump(x+5,y-times*10)
        for times in range(10):
            bob.color(co,co2,co3)
            bob.begin_fill()
            bob.circle(20)
            bob.end_fill()
            bob.right(2)
            ghostwalk(10)
    jump(x,y-20)
    bob.begin_fill()
    bob.circle(20)
    bob.end_fill()
    jump(x+20,y-45)
    bob.setheading(0)
    for times in range(7):
            bob.color(co,co2,co3)
            bob.begin_fill()
            bob.circle(20)
            bob.end_fill()
            bob.right(2)
            ghostwalk(10)
    jump(x+15,y-42)
    bob.setheading(0)
    for times in range(7):
            bob.color(co,co2,co3)
            bob.begin_fill()
            bob.circle(20)
            bob.end_fill()
            bob.right(2)
            ghostwalk(10)
        
    # Ear
    bob.setheading(0)
    jump(35+x,50+y)
    bob.left(210)
    iso_tri(fill2)
    bob.setheading(0)
    jump(10+x,60+y)
    bob.left(220)
    iso_tri(fill2)
    # Head
    bob.setheading(0)
    jump(x,y)
    for times in range(34):
        bob.color(fill)
        bob.begin_fill()
        bob.circle(25)
        bob.left(3)
        bob.forward(1)
        bob.end_fill()
def bird(size,c):
    bob.width(5)
    bob.color(c)
    for times in range(5):
        bob.forward(size)
        bob.left(5)
    bob.right(45)
    for times in range(5):
        bob.forward(size)
        bob.left(5)
def bird2(size,c):
    bob.width(5)
    bob.color(c)
    for times in range(5):
        bob.forward(size)
        bob.right(5)
    bob.left(45)
    for times in range(5):
        bob.forward(size)
        bob.right(5)



