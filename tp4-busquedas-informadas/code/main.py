from linkedlist import*
from Environment import*
from Agent import*



Entorno = Environment()
print("posInicial: ",Entorno.posI," posFinal: ", Entorno.posF)

Agente = Agent(Entorno)

camino = Agente.Aestrella()
if camino != None:
    current = camino.head
    while current != None:
        print(current.value.estado)
        current = current.nextNode
else:
    print("No encontro un camino")





