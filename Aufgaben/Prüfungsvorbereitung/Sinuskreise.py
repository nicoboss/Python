import turtle
import math

turtle.setup(800,800)
turtle.speed(0)
turtle.pu()
turtle.goto(0,-200)

x=[]
y=[]

for i in range(360):
    turtle.circle(200,1)
    x.append(turtle.xcor())
    y.append(turtle.ycor())

turtle.pd()
turtle.ht()

for a in range(40):
    for i in range(180):
        print(i)
        #print(x[i])
        #print(y[i])
        turtle.goto(x[i*2]+math.sin(i*2)*(20+(a*10)),y[i*2]+math.cos(i*2)*(20+(a*10)))

