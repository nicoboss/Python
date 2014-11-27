#Nico
import random

while(1):
    Input=input('Gebe bitte eine Zahl von 2 bis 12 ein und drücke Enter: ')
    a=random.randint(1, 6)
    b=random.randint(1, 6)
    s=a+b

    if str(s)==Input:
        print('Gut geraten!')
    else:
        print('Falsch geraten. Richtig wäre ', s)

    if not input('Nochmahls raten? Drücke j und Enter um das Spiel zu wiederholen: ')=="j":
        break
    print('')
    

