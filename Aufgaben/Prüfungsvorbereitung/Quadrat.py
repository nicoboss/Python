#Nico Bosshard
import turtle

turtle.pu()
turtle.goto(-100,-100)
turtle.pd()

turtle.pensize(4)

turtle.color(1,0,0)
turtle.goto(100, -100)
turtle.color(0,0,1)
turtle.goto(100, 100)
turtle.color(0,1,0)
turtle.goto(-100, 100)
turtle.color(0,0,0)
turtle.goto(-100, -100)

turtle.hideturtle()
turtle.exitonclick()
