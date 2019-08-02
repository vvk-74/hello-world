import turtle
import math

z = 10
a = 3
g = 120

turtle.shape('turtle')
# r = a / (2 * math.sin((2* math.pi)/(2 * n)))

def radius(a, n):
    r = a / (2 * math.sin((2* math.pi)/(2 * n)))
    return r


for i in range(10):
    R = radius(z, a)
    print(R)
    x = R
    y = 0
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(g/2)
    for j in range(a):
        g = (180 * (a-2))/a
        turtle.left(g)
        turtle.forward(z)

    a += 1
    z += 10



