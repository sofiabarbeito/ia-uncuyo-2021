from Environment import*
from algo1 import*
from Agent import*
from AgenteAleatorio import*
'''
#Punto B

Entorno = Environment(32,32,0.4)

Entorno.print_environment()

print("-------------------------")
#Punto C

Agente = Agent(Entorno)
Agente.think()


Entorno.print_environment()

print()
'''
#Punto E

Entorno1 = Environment(16,16,0.4)
Entorno1.print_environment()
Agente1 = AgenteAleatorio(Entorno1)
Agente1.think()
print("-------------------------")

Entorno1.print_environment()

