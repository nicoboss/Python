import math
import random
n=1000000
Treffer=0

for i in range(n):
    if random.random() <= math.cos(random.random()*3.141592/2):
        Treffer += 1
print("Anzahl: ", n)
print("Treffer: ", Treffer)
print("Ergebniss: ", 3.141592/2*Treffer/n)
