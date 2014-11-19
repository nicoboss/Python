#Nico Bosshard
import turtle

turtle.speed(0)
turtle.pu()
turtle.goto(0,0)
turtle.pd()
turtle.pensize(2)

for i1 in range(40):
    for i2 in range(3):
        turtle.fd(100)
        turtle.left(120)
    turtle.left(360/40)

turtle.ht()
turtle.exitonclick()
