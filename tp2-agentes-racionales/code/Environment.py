import random
from algo1 import *

class Environment:
    def __init__(self,sizeX,sizeY,dirt_rate):

        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate #devuelve valor real entre 0.0 y 1.0
        self.posX = random.randint(0,sizeX-1) #creo posiciones iniciales
        self.posY = random.randint(0,sizeY-1)
        self.matriz = Array(sizeX,Array(sizeY,0))
        self.performance = 0

        #LLeno matriz de ceros
        for y in range(0,sizeY):
            for x in range (0,sizeX):
                self.matriz[x][y] = 0
        
        #Lleno de suciedad
        casillas_sucias = int(sizeX*sizeY*self.dirt_rate) #calculo cantidad de casillas sucias multiplicando a la cantidad de casillas el dirt rate

        if casillas_sucias != 0:
            i = 0
            control = True
            while control == True:
                x = random.randint(0,sizeX-1)
                y = random.randint(0,sizeY-1)
                if self.matriz[x][y] != 1:
                    self.matriz[x][y] = 1
                    i += 1
                if i == casillas_sucias:
                    control = False


    def print_environment(self):
        for y in range(0,self.sizeY):
            for x in range(0,self.sizeX):
                if self.posX == x and self.posY == y:
                    print("A  ", end="")
                else:
                    print(self.matriz[x][y], " ", end="")
            print(" ")

    def accept_action(self,action):

        if action == "arriba" and self.posY > 0:
            return True
        elif action == "abajo" and self.posY < self.sizeY-1: 
            return True
        elif action == "derecha" and self.posX < self.sizeX-1:
            return True
        elif action == "izquierda" and self.posX > 0:
            return True
        elif action == "limpiar":
            return self.is_dirty()
        elif action == "idle":
            return True
        else:
            return False

    def is_dirty(self):
        if self.matriz[self.posX][self.posY] == 1:
            return True
        else:
            return False
    
    def get_performance(self):
        return self.performance