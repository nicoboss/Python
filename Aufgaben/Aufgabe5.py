import math
import turtle
import random
turtle.speed(0)
turtle.setup(800,800)
turtle.pu()


n=1000
pos = [-200,-200],[200,-200],[0,200]
turtle.goto(pos[0][0],pos[0][1])
turtle.pd()

for i in range(2):
    turtle.fd(400)
    turtle.left(120)
    pos[i][0]=turtle.xcor()
    pos[i][1]=turtle.ycor()

turtle.fd(400)
turtle.left(120)


for i in range(n):
    r=random.randint(0, 2)
    if r==0:
        turtle.goto((pos[0][0]+pos[1][0])/2, (pos[0][1]+pos[1][1])/2)
    elif r==1:
        turtle.goto((pos[1][0]+pos[2][0])/2, (pos[1][1]+pos[2][1])/2)
    else:
        turtle.goto((pos[2][0]+pos[0][0])/2, (pos[2][1]+pos[0][1])/2)
    
