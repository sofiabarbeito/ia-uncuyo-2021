from linkedlist import*
from Environment import*
from Agent import*
from queue import*



#BFS
Entorno = Environment()
print("BFS")
print("posInicial: ",Entorno.posI," posFinal: ", Entorno.posF)
Entorno.imprimirGrilla()
Agente = Agent(Entorno)
print("-------")
print("Camino: ")
camino = Agente.busquedaBFS()
if camino != None:
    imprimir(camino)
else:
    print("No encontro un camino")
print("")

#DFS 
Entorno = Environment()
print("DFS")
print("posInicial: ",Entorno.posI," posFinal: ", Entorno.posF)
Entorno.imprimirGrilla()
Agente = Agent(Entorno)
print("-------")
print("Camino: ")
camino = Agente.busquedaDFS(Agente.env.sizeX*5)
if camino != None:
    imprimir(camino)
else:
    print("No encontro un camino")
print(" ")

#UNIFORME
Entorno = Environment()
print("UNIFORME")
print("posInicial: ",Entorno.posI," posFinal: ", Entorno.posF)
Entorno.imprimirGrilla()
Agente = Agent(Entorno)
print("-------")
print("Camino: ")
camino =Agente.busquedaUCS()
if camino != None:
    imprimir(camino)
else:
    print("No encontro un camino")





