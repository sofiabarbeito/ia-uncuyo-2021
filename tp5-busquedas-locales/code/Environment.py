import random
from algo1 import*

class Environment:
    def __init__(self,reinas):
        self.reinas = reinas
        self.grilla = self.crearGrilla(self.reinas)


    def crearGrilla2(self,reinas):

        grilla = Array(reinas,0)
        
        grilla[0] = 1
        grilla[1] = 1
        grilla[2] = 3
        grilla[3] = 0
            
        return grilla

    def crearGrilla(self,reinas):

        grilla = Array(reinas,0)
        
        for x in range (0,reinas):
            n = random.randint(0,reinas-1)
            grilla[x] = n #cada posicion = x es la columna, cada valor = n es la fila donde esta la reina
            
        return grilla

    def imprimirGrilla(self,grilla):
        for x in range(0,self.reinas):
            print("Columna ",x,"Fila ",grilla[x])