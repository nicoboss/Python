#a3 Name
#benötigtte Module importieren
import turtle
import random

#Der Spieler kann schätzen
#Die Schätzung wird unter guess abgespeichert
gues=input('Schätze die Anzahl der benötigten Markierungen: ')

#Höchstgeschwindigkeit einstellen
#Die Form als 'turtle' festlegen
turtle.speed(0)
turtle.shape('turtle')

#Gehege und Zielkreis zeichnen
#Gehege: Quadrat mit einer Ecke in (0/0) und Seitenlänge 300
for i in range(4):
    turtle.forward(300)
    turtle.left(90)

#Zielkreis: Zufälliger Mittelpunkt M mit 30<x,y<270 und Radius=30
#Verwende für M die Variablen xm und ym
turtle.pu()
xm=random.randrange(30, 270)
ym=random.randrange(0, 270)
turtle.goto(xm, ym)
turtle.pd()
turtle.circle(30, 360)

#Mit der Variablen anzahl zählen wir die benötigten Markierungen
#Lege ihren Startwert fest
anzahl=1

#Die Turtle wird in den Ursprung gesetzt
turtle.pu()
turtle.goto(0, 0)
turtle.pd()

#Unter abstand speicherst du den Abstand zwischen M und der Turtle
abstand=turtle.distance(xm, ym)

#Es wird entschieden, ob die Turtle im Zielkreis ist
#Die Turtle wird zufällig im Gehege platziert
#Der neue Abstand zum Kreismittelpunkt wird ermittelt
#Sie verrichtet ihr Geschäft der Grösse 10
#Die Zufallspositionen werden gezählt
while(abstand>30):
    turtle.pu()
    turtle.goto(random.randrange(0, 300), random.randrange(0, 300))
    turtle.pd()
    abstand=turtle.distance(xm, ym)
    print(abstand)
    turtle.color(0.7,0.4,0.1)
    turtle.circle(10, 360)
    turtle.color(0,0,0)
    anzahl+=1

#Die benötigte Anzahl der Markierungen wird ausgegeben
print('Anzahl der benötigte Markierungen: ', anzahl)

#Es wird ausgegeben ob gut oder schlecht geschätzt wurde
if gues==anzahl:
    print('Gut geschätzt!')
else:
    print('Schlecht geschätzt!')

#das darf nicht fehlen am Schluss
turtle.exitonclick()


