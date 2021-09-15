from Agent import*
from Environment import*
import math

print("Hill CLimbing")
E = Environment(4)
A = Agent(E)
A.hillClimbing()

print(" ")
print("Simulated Anneling")
E = Environment(4)
A = Agent(E)
A.simulatedAnnealing()

print(" ")
print("Genetico")
reinas = 4
tamanopoblacion = 200
E = Environment(reinas)
A = Agent(E)
poblacion = Array(tamanopoblacion,Array(reinas,0))
for i in range(0,tamanopoblacion):
    grilla = Array(E.reinas,0)
    for x in range (0,E.reinas):
        n = random.randint(0,E.reinas-1)
        grilla[x] = n
    poblacion[i] = grilla

A.genetico(poblacion)

