#Nico
import random

while(1):
    Input=input('Gebe bitte eine Zahl von 2 bis 12 ein und drücke Enter: ')
    a=random.randint(1, 1)
    b=random.randint(1, 1)
    s=a+b

    if s==Input:
        print('Gut geraten!')
    else:
        print('Falsch geraten. Richtig wäre ', s)

    if not input('Nochmahls raten? Drücke j und Enter um das Spiel zu wiederholen: ')=="j":
        break
    print('')
    

