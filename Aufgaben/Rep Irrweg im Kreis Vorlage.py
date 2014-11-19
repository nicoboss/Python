#Irrweg auf Kreisscheibe

#turtle- und random-Modul importieren
from turtle import *
from random import *

#Kreis mit Mittelpunkt U(0/0) und Radius r=200 zeichnen
speed(0)
pu()
goto(0,-200)
pd()
circle(200)
pu()

#Turtle auf Punkt U zurücksetzen
goto(0,0)
pd()

#Initialisierung der Variablen
#in der Variablen "abstand" wird der Abstand der Turtle zum Punkt U gespeichert
abstand=0
#in der Variablen "schritte" wird die Anzahl Schritte bis die Turtle aus dem Kreis läuft gespeichert
schritte=0

#while(bedingung) ist eine Schleife die solange wiederholt wird bis "bedingung" nicht mehr zutrifft
#die Schleife soll solange wiederholt werden bis die Turtle aus dem Kreis läuft
while abstand<200:
    #befindet sich die Turtle näher als 150 Pixel bei O so wird grün gezeichnet sonst rot
    if abstand<150:
        color(0,1,0)
    else:
        color(1,0,0)

    #die Turtle dreht sich zufällig nach links oder rechts...
    #um einen zufälligen Winkel zwischen 0 und 90 Grad...
    #und legt eine zufällige Strecke zwischen 5 und 30 Pixeln in dieser Richtung zurück
    left(randrange(-90,90))
    fd(randrange(5,30))

    #die Variable "abstand" auf den aktuellsten Stand setzen
    abstand=distance(0,0)
      
    #die Variable "schritte" wird um 1 höher gesetzt
    schritte+=1


#zum Schluss werden die Anzahl gemachter Schritte ausgegeben
#print("Aus dem Kreis in ",schritte," Schritten.")
print('raus in ',schritte,' Schritten')

#... und was darf ganz am Ende eines Turtle-Programms nicht fehlen?
exitonclick()
