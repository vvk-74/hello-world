import turtle
import math

z = 20
a = 3
g = 120

turtle.shape('turtle')
# r = a / (2 * math.sin((2* math.pi)/(2 * n)))

def radius(a, n):
    r = a / (2 * math.sin((2* math.pi)/(2 * n)))
    return r


for i in range(10):
    R = radius(z, a)
    x = R * math.cos(g)
    y = R * math.sin(g)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for j in range(a):
        turtle.forward(z)
        turtle.left(g)
    a += 1
    z += 10
    g = 360 / a


