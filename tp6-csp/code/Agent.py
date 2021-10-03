from algo1 import*
import math
import random

class Agent:

    def __init__(self,env):
        self.env = env
        self.estados = 0

   
    def atacado(self,i, j):
        #columnas
        for k in range(0,self.env.reinas):
            if self.env.grilla[i][k] == 1 or self.env.grilla[k][j] == 1:
                return True
        #diagonales
        for k in range(0,self.env.reinas):
            for l in range(0,self.env.reinas):
                if (k+l == i+j) or (k-l == i-j):
                    if self.env.grilla[k][l] == 1:
                        return True
        return False

    def backtracking(self):
        for x in range(0,self.env.reinas):
            for y in range(0,self.env.reinas):
                self.env.grilla[x][y] = 0
        return self.backtrack(self.env.reinas)

        
    def backtrack(self,n):
        if n == 0:
            return True
        for i in range(0,self.env.reinas):
            for j in range(0,self.env.reinas):
                self.estados += 1
                if (not(self.atacado(i,j))) and (self.env.grilla[i][j]!=1):
                    self.env.grilla[i][j] = 1
                    if self.backtrack(n-1) == True:
                        return True
                    self.env.grilla[i][j] = 0

        return False

#--------------------------------------------------------------------------------

    def forwardChecking(self):
        fw = Array(self.env.reinas,Array(self.env.reinas))
        for x in range(0,self.env.reinas):
            for y in range(0,self.env.reinas):
                #si fw[x][y] == 1, no se permite, == 0 se permite
                fw[x][y] = 0

        return self.fwRecursivo(fw,0)

    def fwRecursivo(self,fw,n):
        
        if n == 0:
            for x in range(0,self.env.reinas): #Elijo una columna de la grilla (n), y pruebo todas las filas (x)
                self.estados += 1
                for y in range(0,self.env.reinas):
                    if y != x: #la unica posicion permitida es x, pone como unica posibilidad fw[n][x] = 0
                        fw[n][y] = 1 
                    else:
                        fw[n][y] = 0


                result = self.fwRecursivo(fw,n+1)
                if result == True:
                    self.grilla = fw
                    return True
        else:
            control = True
            for y in range(0,self.env.reinas): #tengo que verificar q no se interponga con reinas anteriores
                self.estados += 1
                columna = n 
                fila = y
                
                
                
                for z in range(n-1,-1,-1):
                    continuar = False
                    #la comparo con columnas anteriores
                    if (fila == self.searchPermitido(fw,z)): 
                     #   print("1")
                        control = False
                        continuar = True
                        break
                    #la comparo con diagonal arriba
                    elif self.searchPermitido(fw,z) == fila-(n-z):
                      #  print("2")
                        control = False
                        continuar = True
                        break
                    #la comparo con diagonal abajo 
                    elif self.searchPermitido(fw,z) == fila+(n-z):
                       # print("3")
                        control = False
                        continuar = True
                        break
                    else:
                        control = True
                        #print("4")
                
                if continuar == True:
                    continue
                #si pasa esta parte, lo elije para probar


                for z in range(0,self.env.reinas):
                    if z != fila: #la unica posicion permitida es x, pone como unica posibilidad fw[n][y] = 0
                        fw[n][z] = 1 
                    else:
                        fw[n][z] = 0
                if n+1 == self.env.reinas:
                    self.grilla = fw
                    return True
                result = self.fwRecursivo(fw,n+1)
                if result == True:
                    self.grilla = fw
                    return True
                else:
                    for z in range(0,self.env.reinas):
                        fw[n][z] = 1 
            
            if control == False:
                return False



    def searchPermitido(self,fw,z):
        for x in range(0,self.env.reinas):
            if fw[z][x] == 0:
                return x

    def imprimirFW(self,fw):
        for x in range(0,self.env.reinas):
            print(fw[x])