import turtle
import random

t = turtle.Turtle("turtle")

def moveKame(x, y):
    t.goto(x, y)
    tSize = random.randrange(2, 10)
    t.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    t.color((r, g, b))
    tAngle = random.randrange(0, 360)

    # turtle.penup()
    t.goto(x, y)
    t.left(tAngle)
    t.stamp()


tSize, tAngle = 0, 0
r, g, b = 0.0, 0.0, 0.0

t.screen.onclick(moveKame)

turtle.done()
