import turtle

def Quadrat(s):
    for i in range(4):
        turtle.fd(s)
        turtle.left(90)

s=200
for i in range(20):
    s=(5/6)*s
    Quadrat(s)

    
    

