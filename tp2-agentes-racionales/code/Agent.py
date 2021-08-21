import random
from algo1 import *
from Environment import *

class Agent:
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
            
            #Llegamos a esquina de matriz limpiando en el camino
            while self.env.posX != 0 or self.env.posY != 0:
               # print(self.vida)
                if self.env.accept_action("arriba") == True:
                    self.up()
                    if self.perspective() == "sucio":
                        self.suck()
                if self.env.accept_action("izquierda") == True:   
                    self.left()
                    if self.perspective() == "sucio":
                        self.suck()
                if self.vida == 0:
                    break
            
            termina = False
            while self.env.posX < self.env.sizeX and self.vida > 0:
               # print(self.vida)
                if self.perspective() == "sucio":
                        self.suck()
                if self.vida == 0 or self.vida < 0:
                    break
                while self.env.accept_action("derecha") == True:
                    self.right() 
                    if self.vida == 0 or self.vida < 0:
                        termina = True
                        break
                    if self.perspective() == "sucio":
                        self.suck()
                    if self.vida == 0 or self.vida < 0:
                        termina = True
                        break

                if termina == True:
                    break
                if self.env.accept_action("abajo") == True:
                    self.down()
                if self.vida == 0 or self.vida < 0:
                        break

                if self.perspective() == "sucio":
                        self.suck()
                if self.vida == 0 or self.vida < 0:
                    break
                while self.env.accept_action("izquierda") == True:
                    self.left() 
                    if self.vida == 0 or self.vida < 0:
                        termina = True
                        break
                    if self.perspective() == "sucio":
                        self.suck()
                    if self.vida == 0 or self.vida < 0:
                        termina = True
                        break
                    
                if termina == True:
                    break
                if self.env.accept_action("abajo") == True:
                    self.down()
                if self.vida == 0 or self.vida < 0:
                        break
            
           
            
        


