import math
import turtle
import random

turtle.speed(0)
turtle.setup(800,800)
#turtle.bgcolor(random.randint(0, 200)/200,random.randint(0, 200)/200,random.randint(0, 200)/200)
turtle.pu()
#turtle.setpos(-300,100)
turtle.goto(0,-300)
turtle.pd()

turtle.circle(300)

n=10000
na=1
ne=2
alpha=2+math.pi/n


for i in range(n):
    #turtle.bgcolor(random.randint(0, 200)/200,random.randint(0, 200)/200,random.randint(0, 200)/200)
    turtle.pd()
    turtle.goto(300*math.cos(i*na*alpha),300*math.sin(i*na*alpha))
    turtle.pu()
    turtle.goto(300*math.cos(i*ne*alpha),300*math.sin(i*ne*alpha))
    
    
