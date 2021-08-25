from algo1 import*
import random

class Environment:
    def __init__(self):

        self.sizeX = 100
        self.sizeY = 100
        self.grilla = self.crearGrilla(self.sizeX,self.sizeY)
        self.posI = self.posInicial()
        self.posF = self.posFinal(self.posI)


    def posInicial(self):
        control = True
        i = Array(2,0)
        while control == True:
            x = random.randint(0,self.sizeX-1)
            y = random.randint(0,self.sizeY-1)
            if self.grilla[x][y] != 1:
                i[0] = x
                i[1] = y
                control = False
        return i

    def posFinal(self,i):
        f = Array(2,0)
        control = True
        while control == True:
            x = random.randint(0,self.sizeX-1)
            y = random.randint(0,self.sizeY-1)
            if self.grilla[x][y] != 1 and x != i[0] and y != i[1]:
                f[0] = x
                f[1] = y
                control = False
        return f

    def accept_action(self,action,x,y):
        if action == "arriba":
            if y > 0 and self.grilla[x][y-1] != 1:
                return True
            else:
                return False
        elif action == "abajo": 
            if y < self.sizeY-1 and self.grilla[x][y+1] != 1:
                return True
            else:
                return False
        elif action == "derecha":
            if x < self.sizeX-1 and self.grilla[x+1][y] != 1:
                return True
            else:
                return False
        elif action == "izquierda":
            if x > 0 and self.grilla[x-1][y] != 1:
                return True
            else:
                return False
        else:
            return False


    def crearGrilla(self,sizeX,sizeY):

        grilla = Array(sizeX,Array(sizeY,0))
        casillas_obstaculo = int(sizeX*sizeY*0.2) #cantidad de casillas que tienen un obstaculo

        for y in range (0,sizeY):
            for x in range(0,sizeX):
                grilla[x][y] = 0

        if casillas_obstaculo != 0:
            i = 0
            control = True
            while control == True:
                x = random.randint(0,sizeX-1)
                y = random.randint(0,sizeY-1)
                if grilla[x][y] != 1:
                    grilla[x][y] = 1
                    i += 1
                if i == casillas_obstaculo:
                    control = False
        return grilla

    def imprimirGrilla(self):
        for y in range(0,self.sizeY):
            for x in range(0,self.sizeX):
                print(self.grilla[x][y], " ", end="")
            print(" ")