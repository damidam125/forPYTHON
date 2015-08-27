import turtle

t1 = turtle.Turtle()
screen=t1.getscreen()

w=150

screen.setworldcoordinates(-w,-w,w,w)

for a in list(range(0,100,20)):
    t1.circle(25+a, 180)

turtle.done()