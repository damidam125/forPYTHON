import turtle
import random

def meaninglessGraph(tur, cord, colour) :
    tur.penup()
    tur.home()
    tur.pendown()
    tur.pencolor(colour)
    tur.speed('fastest')
    for a in list(range(1,cord-50,2)) :
        tur.goto(a, random.randrange(1,50)+a)


tur = turtle.Turtle()
w = 150
screen=tur.getscreen().setworldcoordinates(0,0,w,w)
tur.pensize(3)
meaninglessGraph(tur, w, "red")
meaninglessGraph(tur, w, "blue")
turtle.done()