#Nico
#a4
#benötigtte Module importieren
import turtle
import random

#Fenster der Grösse 800*800 vorbereiten
#Das Fenster soll mit dem Titel "Irrweg" versehen sein
turtle.setup(800,800)

#Höchstgeschwindigkeit einstellen
#Die Form und die Farbe festlegen
turtle.speed(0)
turtle.color(0,1,0)
turtle.shape('turtle')
turtle.goto(0,0)

#Vier Variablen für die Extrempositionen festlegen und auf 0 setzen
xmin=0
ymin=0
xmax=0
ymax=0

#50 Wiederholungen
#zufällige Richtung und Streckenlänge
#überprüfen, ob eine Extremkoordinate ändert
for i in range(50):
    Richtung=random.randint(0,359)
    Strecke=random.randint(20,40)
    turtle.left(Richtung)
    turtle.fd(Strecke)

    if turtle.xcor()<xmin:
        xmin=turtle.xcor()
    elif turtle.xcor()>xmax:
        xmax=turtle.xcor()

    if turtle.ycor()<ymin:
        ymin=turtle.ycor()
    elif turtle.ycor()>ymax:
        ymax=turtle.ycor()

#Farbe auf rot umstellen
turtle.color(1,0,0)

#Das minimale, umfassende Rechteck mit rot zeichnen
turtle.pu()
turtle.goto(xmin,ymin)
turtle.pd()
turtle.goto(xmin,ymin)
turtle.goto(xmax,ymin)
turtle.goto(xmax,ymax)
turtle.goto(xmin,ymax)
turtle.goto(xmin,ymin)

#Die Schildkröte verbergen und das Programm abschliessen
turtle.ht()
turtle.exitonclick()
