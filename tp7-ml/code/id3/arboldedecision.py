from algo1 import*
import math
from linkedlist import*



def APRENDIZAJE_ARBOL_DECISION(ejemplos,atr,defecto):
    clas_igual = True
    for x in range(0,len(ejemplos)): #voy linea por linea, veo si clasificacion es == para todos los ej
        if x == 0:
            clasificacion = ejemplos[x][4]
        if ejemplos[x][4] != clasificacion:
            clas_igual = False
        
    
    sigo = False
    for w in range(0,len(atr)-1):
        if atr[w] != None:
            sigo = True

    if len(ejemplos) == 0: #si ejemplos esta vacio
        #print("1")
        return defecto
    elif clas_igual == True: #si clasificacion de todos los ejemplos es la misma
        #print("2")
        return clasificacion
    elif sigo == False: #si atr esta vacio
        #print("3")
        vm = valor_mayoria(ejemplos)
        return vm
    else:
        
        mejor = elegir_atributo(atr,ejemplos) #indice
        
        
        listaValores = LinkedList() #lista con valores posibles de mejor
        for i in range(0,len(ejemplos)): #voy por cada valor del atributo, hago lista con valores
            if length(listaValores) == 0: #si lista esta vacia, agrego primero valor
                add(listaValores,ejemplos[i][mejor])
            if search(listaValores,ejemplos[i][mejor]) == None: #si valor no esta en lista, lo agrego
                add(listaValores,ejemplos[i][mejor])
        print("------------------------------------")
        print("atr ",atr)
        print("mejor ", mejor, " = ",atr[mejor])
        
        
        

        #arbol = generar arbol con nodo raiz mejor
        arbol = Nodo()
        arbol.respuesta = atr[mejor]
        arbol.hijos = list()
        
        currentLV = listaValores.head
        for i in range(0,length(listaValores)):#para cada valor del atributo que elegimos 'mejor'
            ejemplosi = list() #hago lista con ejemplos que tienen el atributo mejor, para cada valor
            for q in range(0,len(ejemplos)):
                if currentLV.value == ejemplos[q][mejor]:
                    ejemplosi.append(ejemplos[q])
            print(currentLV.value)       
                        
                    
            m = valor_mayoria(ejemplosi)

            atr[mejor] = None
            
            res = APRENDIZAJE_ARBOL_DECISION(ejemplosi,atr,m) #me devuelve yes o no o arbol
            if res == 'yes' or res == 'no':
                subarbol = Nodo()
                subarbol.respuesta = res
            else:
                subarbol = res
            subarbol.value = currentLV.value
            arbol.hijos.append(subarbol)

            currentLV = currentLV.nextNode
        return arbol


def elegir_atributo(atr,ejemplos):
    #print("len atr ", len(atr))
    p = 0
    n = 0
    for i in range(0,len(ejemplos)):
        if ejemplos[i][4] == "yes":
            p += 1
        else:
            n += 1
    
    #El resto lo calculamos para cada atributo
    listaGanancia = Array(len(atr),0.0)
    for x in range(0,len(atr)-1): #voy por cada atributo
        if atr[x] != None:
            listaValores = LinkedList()
            for i in range(0,len(ejemplos)): #voy por cada valor del atributo, hago lista con valores
                if length(listaValores) == 0: #si lista esta vacia, agrego primero valor
                    add(listaValores,ejemplos[i][x])
                if search(listaValores,ejemplos[i][x]) == None: #si valor no esta en lista, lo agrego
                    add(listaValores,ejemplos[i][x])

            currentNode = listaValores.head
            pi = 0
            ni = 0
            R = 0
            while currentNode != None: #paso por cada valor, busco en ejemplos la cantidad de casos t, p y n, calculo resto R
                for i in range(0,len(ejemplos)):
                    if currentNode.value == ejemplos[i][x]:
                        if ejemplos[i][len(atr)-1] == "yes":
                            pi += 1
                        else:
                            ni += 1
                currentNode = currentNode.nextNode
                
                if ni == 0 or pi == 0:
                    ri = 0
                else:
                    ri = ((pi+ni)/(p+n))*I(pi,ni)
                R += ri

                pi = 0
                ni = 0

            G = I(p,n) - R
            listaGanancia[x] = G
        #insert(listaGanancia,G,x)
    #currentN = listaGanancia.head
    #print(length(listaGanancia))
    indice = None
    #print(listaGanancia)
    for j in range(0,len(listaGanancia)):
        if listaGanancia[j] != None:
            if indice == None:
                mayorG = listaGanancia[j]
                indice = j
            else:
                if mayorG < listaGanancia[j]:
                    mayorG = listaGanancia[j]
                    indice = j
        #currentN = currentN.nextNode
    return indice

        
#estimacion de la entropia en la informacion   
def I(p,n):
    return (-p/(p+n))*math.log((p/(p+n)),2) - (n/(p+n))*math.log((n/(p+n)),2)
        
def valor_mayoria(ejemplos):
    p = 0
    n = 0
    for i in range(0,len(ejemplos)):
        if ejemplos[i][4] == "yes":
            p += 1
        else:
            n += 1
    if p > n:
        return "yes"
    else:
        return "no"





class Nodo():
    respuesta = None #yes, no o atributo
    hijos = None #lista con nodos hijos
    value = None #valor del atributo