import turtle
import random
import math

from turtle import * 
left(180)
for i in range(200):
    if i<50:
        forward(2)
    elif i<100:
        left(3.6)
        forward(2)
    elif i<150:
        right(3.6)
        forward(2)
    else:
        forward(2)
                

#AAA=input('Eingabe: ')
#print('Aussgabe: ', AAA)

turtle.shape('turtle')

for i in range(20):
    turtle.pencolor(1-i/20,i/20,i/20)
    radius=1.35**i
    turtle.pensize(i/2)
    turtle.circle(radius,180)
