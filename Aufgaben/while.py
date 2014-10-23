import turtle
import random


while True:
    Richtung=input('Richtung? N,S,O,W:')
    if Richtung=="N" or Richtung=="O" or Richtung=="S" or Richtung=="W":
        break


turtle.pu()
turtle.goto(-200,-200)
turtle.pd()
turtle.forward(400)
turtle.left(90)
turtle.forward(400) 
turtle.left(90) 
turtle.forward(400) 
turtle.left(90)
turtle.forward(400) 
turtle.left(90)


turtle.shape("turtle")

turtle.pu()
turtle.goto(0,0)
turtle.pd()

while True:
    turtle.left(90*random.randint(0,3))
    turtle.forward(50)
    if turtle.ycor()<200:
        print("Nord")
        if Richtung=="N":
            print("Richtig!")
        else:
            print("Falsch!")
        break
    if turtle.xcor()>200:
        print("Osten")
        if Richtung=="O":
            print("Richtig!")
        else:
            print("Falsch!")
        break
    if turtle.ycor()>-200:
        print("Süden")
        if Richtung=="S":
            print("Richtig!")
        else:
            print("Falsch!")
        break
    if turtle.xcor()<-200:
        print("Westen")
        if Richtung=="W":
            print("Richtig!")
        else:
            print("Falsch!")
        break
            
    #turtle.bgcolor(random.randint(0, 200)/200,random.randint(0, 200)/200,random.randint(0, 200)/200)



