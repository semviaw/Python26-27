from myFunctions import *
#   Bird          ________________________________
bc=(200,200,200)
bc1=(210,210,210)
bc2=(220,220,220)
bc3=(230,230,230)
jump(200,200)
bird(7,bc1)
jump(165,180)
bob.setheading(0)
bird(4,bc)


jump(650,250)
bob.setheading(0)
bird2(10,bc2)
turtle.tracer(0)
jump(-650,100)
bob.setheading(0)
bird2(10,bc)
turtle.tracer(0)

jump(-500,200)
bob.setheading(0)
bird2(5,bc)
turtle.tracer(0)
bob.width(1)
jump(-600,320)
bob.setheading(0)
bird2(4,bc)
turtle.tracer(0)
bob.width(1)

jump(450,400)
bob.setheading(0)
bird2(10,bc)
turtle.tracer(0)
bob.width(1)

# Arches    ________________________________________
home()
bob.setheading(0)
bob.left(90)
arch(225,100,4,1)
jump(200,0)
bob.setheading(90)
arch(85,75,4,2)
bob.setheading(90)



# Hills    _________________________________________

c=(220,245,220)
c1=(215,242,215)
c2=(210,240,210)
c3=(205,238,205)
jump(-230,9)
bob.setheading(180)
hill(500,c)
jump(0,70)
bob.setheading(180)
hill(500,c)
jump(-600,-200)
hill(500,c2)

# Front Arches     _________________________________

bob.setheading(135)
jump(500,-300)
arch(225,100,4,1)


# Front Hills    _________________________________________

bob.setheading(135)
jump(1000,-200)
hill(500,c3)


# Sun       ____________________________________________

jump(900,550)
for times in range(34):
    fill=(250,250,180)
    bob.begin_fill()
    bob.color(fill)
    bob.circle(150)
    bob.left(3)
    bob.forward(1)
    bob.end_fill()


# Animals      ____________________________________________

sheep(275,-50)
sheep(400,-150)


# Grass and flowers     ____________________________________________

grass(5,"green",-100,-100)
grass(10,"green",-200,-50)
grass2(10,"green",-300,-200)
grass2(10,"green",300,-278)
grass(10,"green",-500,-176)
grass(5,"green",46,20)
grass(10,"green",20,-300)
grass(5,"green",-78,-380)
grass(12,"green",-630,-240)
grass(7,"green",-560,-343)
grass(10,"green",670,-400)
grass(15,"green",720,-295)
grass(7,"green",450,-400)

dandelion(-120,45,1)
dandelion(-170,15,1)
dandelion(170,28,1)
dandelion(570,-75,1)

nightshade(23,-100)
bob.setheading(0)
nightshade(-260,-180)
bob.setheading(0)
nightshade(-660,-240)
bob.setheading(0)
nightshade(-610,-275)

bob.setheading(0)
nightshade(610,-375)
bob.setheading(0)
nightshade(670,-400)
bob.setheading(0)
nightshade(570,-425)
