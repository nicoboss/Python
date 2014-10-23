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
turtle.goto(pos[1][0],pos[1][1])
turtle.goto(pos[2][0],pos[2][1])
turtle.goto(pos[0][0],pos[0][1])

for i in range(n):
    r=random.ranint(0, 2)
    #if r==0:   
    #else if r==1:
    #else:
    
