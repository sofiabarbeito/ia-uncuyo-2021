
from algo1 import*
import math
import random

class Agent:

    def __init__(self,env):
        self.env = env
        self.h = self.funcion_objetivo(self.env.grilla)
        self.estados = 0

#--------------------------------------------------------------------
    def hillClimbing(self):
        hactual = self.h
        hmenor = hactual 
        while self.estados <= 100 and hmenor != 0:
            
            
            for i in range(0,self.env.reinas):

                estadoVecino = Array(self.env.reinas,0) #Array con mismos estados q grilla, despues vamos cambiando reinas de lugar en este
                for z in range(0,self.env.reinas):
                    estadoVecino[z] = self.env.grilla[z]

                for j in range(0,self.env.reinas):
                    estadoVecino[i] = j
                    h = self.funcion_objetivo(estadoVecino)
                    if h < hactual:
                        if h < hmenor:
                            hmenor = h
                            proximoEstado = Array(self.env.reinas,0)
                            for z in range(0,self.env.reinas):
                                proximoEstado[z] = estadoVecino[z]
            
            if hactual == hmenor:
                break
            else:
                hactual = hmenor
                self.env.grilla = proximoEstado
                self.estados += 1    
        self.h = hactual
        if self.estados < 100:
            print("Estado solución: ", self.env.grilla)
            print('h = ',self.h)  
            print("Cantidad de estados: ", self.estados)    
        else:
            print("Se alcanzó el máximo de estados")
            print("Estado solución: ", self.env.grilla)
            print('h = ',self.h)  
        '''
        if self.h == 0:
            return True
        else:
            return False
        '''
            
        
    def funcion_objetivo(self,tablero):
        h = 0
        for x in range(0,self.env.reinas):
            filax = tablero[x] #busco fila de primer reina 
            for y in range(x+1,self.env.reinas):
                filay = tablero[y]
                #la comparo con las demas columnas
                if (filax == filay): 
                    h += 1
                #la comparo con diagonales
                else:
                    diag1 = abs(filax - filay)
                    diag2 = abs(x - y)
                    if diag1 == diag2:
                        h += 1
        return h

#-------------------------------------------------------------------
    def simulatedAnnealing(self):
        #variables actual, siguiente, T, p, i

        actual = self.env.grilla
        hactual = self.h
        i = 1
        T = 100
        while T != 0 and self.estados <= 100 and hactual != 0:
            T = self.squedule(i)
            siguiente = self.sucesorAleatorio(actual)
            hsiguiente = self.funcion_objetivo(siguiente)

            if hsiguiente < hactual:
                actual = siguiente
                hactual = hsiguiente
                self.estados += 1
            else:
                E = hsiguiente - hactual 
                i+=1
                p = math.e**(-E/T)
                if p >= 0.5:
                    actual = siguiente
                    hactual = hsiguiente
                    self.estados += 1
            
        if self.estados < 100:
            print("Estado solución: ", self.env.grilla)
            print('h = ',self.h)  
            print("Cantidad de estados: ", T)     
        else:
            print("Se alcanzó el máximo de estados")
            print("Estado solución: ", self.env.grilla)
            print('h = ',self.h) 
        
        '''
        if hactual == 0:
            return True
        else:
            return False
        '''
            
    def squedule(self,t):
        return t**(-2) + 0.3
        #return -t+100

    def sucesorAleatorio(self,grilla):

        estadoVecino = Array(self.env.reinas,0) 
        for z in range(0,self.env.reinas):
            estadoVecino[z] = grilla[z]

        fila = random.randint(0,self.env.reinas-1)
        estadoVecino[fila] = random.randint(0,self.env.reinas-1)

        return estadoVecino

#--------------------------------------------------

    def genetico(self,poblacion):

        
        factual = self.fitnessPoblacion(poblacion)
        fnuevo = factual + 1

        while self.estados < 100:
            nuevaPoblacion = []
            self.estados += 1
            
            sum = 0
            for i in range(0,self.env.reinas):
                sum += i

            for x in range(0,len(poblacion)):   
                padre = self.seleccion(poblacion,sum)
                madre = self.seleccion(poblacion,sum)
                hijo = self.crucePMX(padre,madre)
                p = random.uniform(0.0, 1.0)
                if p < 0.2:
                    hijo = self.mutar(hijo)

                nuevaPoblacion.append(hijo)
                
                if len(nuevaPoblacion) == len(poblacion):
                    break

            factual = self.fitnessPoblacion(poblacion)
            fnuevo = self.fitnessPoblacion(nuevaPoblacion)

            
            #Reemplazo de poblacion
            cambiados = []
            for i in range(0,len(poblacion)):
                for j in range(0,len(nuevaPoblacion)):
                    if self.fitness(nuevaPoblacion[j]) > self.fitness(poblacion[i]) and self.buscarArray(cambiados,j) == None:
                        poblacion[i] = nuevaPoblacion[j]
                        cambiados.append(j)
                        break
           
            if factual == sum:
                break

        mayor = 0
        n = 0
        for i in range(0,len(poblacion)):
            mayornuevo = self.fitness(poblacion[i])
            if mayornuevo > mayor:
                mayor = mayornuevo
                n = i

        if self.estados < 100:
            print("Estado solución: ", poblacion[n])
            print('h = ',self.fitness(poblacion[n]))  
            print("Cantidad de estados: ", self.estados)     
        else:
            print("Se alcanzó el máximo de estados")
            print("Estado solución: ", poblacion[n])
            print('h = ',self.fitness(poblacion[n])) 

        
        if self.fitness(poblacion[n]) == sum:
            return True
        else:
            return False
        


    def fitness(self,individuo):
        sum = 0
        for i in range(0,self.env.reinas):
            sum += i
        return (sum - self.funcion_objetivo(individuo)) #numero de pares de reinas no atacadas

    def fitnessPoblacion(self,poblacion):
        mayor = 0
        sum = 0
        for i in range(0,len(poblacion)):
            sum += self.fitness(poblacion[i])
            mayornuevo = self.fitness(poblacion[i])
            if mayornuevo > mayor:
                mayor = mayornuevo
        return mayor

    def seleccionProporcional(self,poblacion,viejos):

        sumFitness = 0
        for i in range(0,len(poblacion)):
            sumFitness += self.fitness(poblacion[i])
        
        #padre
        p = self.fitness(poblacion[0])/sumFitness
        n1 = 0
        for j in range(1,len(poblacion)):
            pnuevo = self.fitness(poblacion[j])/sumFitness
            if pnuevo > p:
                cambiar = True
                for z in range(0,len(viejos)):
                    if j == viejos[z]:
                        cambiar = False
                        break
                if cambiar == True:
                    p = pnuevo
                    n1 = j

        #madre
        p = 0
        n2 = 0
        for j in range(0,len(poblacion)):
            pnuevo = self.fitness(poblacion[j])/sumFitness
            if pnuevo > p and j != n1:
                cambiar = True
                for z in range(0,len(viejos)):
                    if j == viejos[z]:
                        cambiar = False
                        break
                if cambiar == True:
                    p = pnuevo
                    n2 = j

        viejos.append(n1)
        viejos.append(n2)

        return [poblacion[n1],poblacion[n2],viejos]

    def seleccion(self,poblacion,sum):
        p = sum*0.7

        padre = random.randint(0,self.env.reinas-1)
        n = 0
        while n < self.env.reinas*2:
            n +=1 
            if self.fitness(poblacion[padre]) >= p:
                return poblacion[padre]
            else:
                padre = random.randint(0,self.env.reinas-1)
        return poblacion[padre]

        

    def seleccionTorneos(self,poblacion):
        
        num1 = random.randint(0,int(self.env.reinas-1/2))
        num2 = random.randint(num1,self.env.reinas-1)

        #padre
        n1 = 0
        p = self.fitness(poblacion[0])
        for j in range(num1,num2):
            pnuevo = self.fitness(poblacion[j])
            if pnuevo > p:
                p = pnuevo
                n1 = j
        
        #madre
        n2 = 0
        p = self.fitness(poblacion[0])
        for i in range(num1,num2):
            pnuevo = self.fitness(poblacion[i])
            if pnuevo > p and i != n1:
                p = pnuevo
                n1 = i

        return [poblacion[n1],poblacion[n2]]

    def cruzamientox2(self,padre,madre):
        n = random.randint(0,self.env.reinas-1)

        hijo1 = Array(self.env.reinas,0)
        hijo2 = Array(self.env.reinas,0)

        for i in range(0,n):
            hijo1[i] = padre[i]
            hijo2[i] = madre[i]
        
        for j in range(n,self.env.reinas):
            hijo1[j] = madre[j]
            hijo2[j] = padre[j]

        return [hijo1,hijo2]

    def cruzamiento(self,padre,madre):
        n = random.randint(0,self.env.reinas-1)

        hijo = Array(self.env.reinas,0)

        for i in range(0,n):
            hijo[i] = padre[i]
        
        for j in range(n,self.env.reinas):
            hijo[j] = madre[j]

        return hijo

    def crucePMX(self,padre,madre):
        n1 = random.randint(0,self.env.reinas-2)
        n2 = random.randint(n1,self.env.reinas-1)
        hijo = Array(self.env.reinas,0)

        for x in range(0,len(padre)):
            hijo[x] = padre[x]

        aux1 = []
        aux2 = []
        for y in range(n1,n2+1):
            aux1.append(hijo[y])
            aux2.append(madre[y])
            hijo[y] = madre[y]

        i = 0
        for z in range(0,len(hijo)):
            if z < n1 or z > n2:
                for j in range(0,len(aux2)):
                    if hijo[z] == aux2[j]:
                        hijo[z] = aux1[i]
                        i+=1
                        break
                if i >= len(aux1):
                    break

        return hijo

    def mutar(self,hijo):
        columna = random.randint(0,self.env.reinas-1)
        fila = random.randint(0,self.env.reinas-1)

        hijo[columna] = fila
        return hijo

    def buscarArray(self,vector,i):
        for x in range(0,len(vector)):
            if vector[x] == i:
                return x
        return None

