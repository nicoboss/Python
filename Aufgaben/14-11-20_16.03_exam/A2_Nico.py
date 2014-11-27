#Nico
import turtle

turtle.setup(800,800)
turtle.pensize(3)
turtle.speed(0)
turtle.pu()
turtle.goto(-250,0)
turtle.pd()

for i2 in range(10):
    for i2 in range(3):
        turtle.fd(40)
        turtle.left(120)
    turtle.pu()
    turtle.fd(50)
    turtle.pd()

turtle.ht()
turtle.exitonclick()
