import turtle

x = 0
y = 0
z = 10
a = 3
r = 120
turtle.shape('turtle')

for i in range(10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for j in range(a):
        turtle.forward(z)
        turtle.left(r)
    a += 1
    x -= 10
    y -= 10
    z += 20
