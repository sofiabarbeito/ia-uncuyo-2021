import random
from algo1 import *
from Environment import *

class AgenteAleatorio:
    def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
        self.env = env
        self.posX = self.env.posX
        self.posY = self.env.posY
        self.vida = 1000

    def up(self):
        self.env.posY = self.env.posY - 1
        self.vida -= 1

    def down(self):
        self.env.posY = self.env.posY + 1
        self.vida -= 1

    def left(self):
        self.env.posX = self.env.posX - 1
        self.vida -= 1

    def right(self):
        self.env.posX = self.env.posX + 1
        self.vida -= 1

    def suck(self): # Limpia
        #print("x: ", self.env.posX)
        #print("y: ", self.env.posY)
        self.env.matriz[self.env.posX][self.env.posY] = 0
        self.env.performance += 1
        self.vida -= 1

    def idle(self): # no hace nada
        self.vida -= 1
            

    def perspective(self): #sensa el entorno
        if self.env.accept_action("limpiar") == True:
            return "sucio"
        else:
            return "limpio"

    def think(self): # implementa las acciones a seguir por el agente
        while self.vida > 0:
            n = random.randint(0,6)
            if n == 0:
                if self.perspective() == "sucio":
                    self.suck()
            elif n == 1:
                if self.env.accept_action("derecha") == True:
                    self.right()
            elif n == 2:
                if self.env.accept_action("izquierda") == True:
                    self.left()
            elif n == 3:
                if self.env.accept_action("arriba") == True:
                    self.up()
            elif n == 4:
                if self.env.accept_action("abajo") == True:
                    self.down()
            elif n == 6:
                self.idle()
