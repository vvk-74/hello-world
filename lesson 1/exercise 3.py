import turtle

x = 0
y = 0
z = 10
turtle.shape('turtle')

for i in range(10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for j in range(4):
        turtle.forward(z)
        turtle.left(90)
    x -= 10
    y -= 10
    z += 20





