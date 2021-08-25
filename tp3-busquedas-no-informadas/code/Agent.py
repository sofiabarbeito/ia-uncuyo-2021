
from linkedlist import*
import queue
import stack


class Agent:

    def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
        self.env = env
        self.posX = self.env.posI[0]
        self.posY = self.env.posI[1]

    def up(self,nodo):
        if self.env.accept_action("arriba",nodo.estado[0],nodo.estado[1]):
            self.posY = self.posY - 1
            return [nodo.estado[0],nodo.estado[1]-1]
        else:
            return None

    def down(self,nodo):
        if self.env.accept_action("abajo",nodo.estado[0],nodo.estado[1]):
            self.posY = self.posY + 1
            return [nodo.estado[0],nodo.estado[1]+1]
        else:
            return None
        
    def right(self,nodo):
        if self.env.accept_action("derecha",nodo.estado[0],nodo.estado[1]):
            self.posX = self.posX + 1
            return [nodo.estado[0]+1,nodo.estado[1]]
        else:
            return None

    def left(self,nodo):
        if self.env.accept_action("izquierda",nodo.estado[0],nodo.estado[1]):
            self.posX = self.posX - 1
            return [nodo.estado[0]-1,nodo.estado[1]]
        else:
            return None

#-------------BFS-------------------------------------------------------------------
    def busquedaBFS(self):
        nodo = BFSNode()
        nodo.estado = self.env.posI
        nodo.profundidad = 0
        arbol = BFS()
        arbol.head = nodo

        frontera = LinkedList()
        add(frontera,nodo)
        explorado = LinkedList()
        
        while length(explorado)-1 < self.env.sizeX*self.env.sizeY:
            if length(frontera) <= 0:
                break

            nodo = queue.dequeue(frontera)
            add(explorado,nodo)
            #self.imprimir(frontera)
            #print("-----------------")
            if nodo.estado[0] == self.env.posF[0] and nodo.estado[1] == self.env.posF[1]:
                #recorro desde nodo hasta arriba con padre y formo camino
                camino = LinkedList()
                currentNode = nodo
                while currentNode != None:
                    add(camino,currentNode.estado)
                    currentNode = currentNode.padre
                return camino
            #Ahora insertamos en frontera los nodos sucesores de nodo
            self.expandirBFS(explorado,frontera,nodo)
        return None

    def expandirBFS(self,explorado,frontera,nodo):
        for x in range(0,4):
            n = BFSNode()
            n.padre = nodo
            n.profundidad = nodo.profundidad + 1
            if x == 0:
                n.estado = self.up(nodo)
                n.accion = "arriba"
            elif x == 1:
                n.estado = self.down(nodo)
                n.accion = "abajo"
            elif x == 2:
                n.estado = self.right(nodo)
                n.accion = "derecha"
            elif x == 3:
                n.estado = self.left(nodo)
                n.accion = "izquierda"
            if n.estado != None and self.search(frontera,n) == None and self.search(explorado,n) == None:
                add(frontera,n)

#----------------DFS------------------------------------------------------

    def busquedaDFS(self,limite):
        nodo = DFSNode()
        nodo.estado = self.env.posI
        nodo.profundidad = 0
        arbol = DFS()
        arbol.head = nodo

        frontera = LinkedList()
        add(frontera,nodo)
        explorado = LinkedList()
        
        while length(explorado)-1 < self.env.sizeX*self.env.sizeY:
            if length(frontera) <= 0:
                break
            if nodo.profundidad >= (limite):
                break
            nodo = stack.pop(frontera)
            add(explorado,nodo)
            #self.imprimir(frontera)
            #print("-----------------")
            if nodo.estado[0] == self.env.posF[0] and nodo.estado[1] == self.env.posF[1]:
                #recorro desde nodo hasta arriba con padre y formo camino
                camino = LinkedList()
                currentNode = nodo
                while currentNode != None:
                    add(camino,currentNode.estado)
                    currentNode = currentNode.padre
                return camino
            #Ahora insertamos en frontera los nodos sucesores de nodo
            self.expandirDFS(explorado,frontera,nodo)
        return None

    def expandirDFS(self,explorado,frontera,nodo):
        for x in range(0,4):
            n = DFSNode()
            n.padre = nodo
            n.profundidad = nodo.profundidad + 1
            if x == 0:
                n.estado = self.up(nodo)
                n.accion = "arriba"
            elif x == 1:
                n.estado = self.down(nodo)
                n.accion = "abajo"
            elif x == 2:
                n.estado = self.right(nodo)
                n.accion = "derecha"
            elif x == 3:
                n.estado = self.left(nodo)
                n.accion = "izquierda"
            if n.estado != None and self.search(frontera,n) == None and self.search(explorado,n) == None:
                add(frontera,n)

#--------UNIFORME--------------------------------------------------------
    def busquedaUCS(self):
        nodo = UCSNode()
        nodo.estado = self.env.posI
        nodo.profundidad = 0
        nodo.costo = 1
        arbol = UCS()
        arbol.head = nodo

        frontera = queue.PriorityQueue()
        queue.enqueue_priority(frontera,nodo,nodo.costo)
        explorado = LinkedList()
        
        while length(explorado)-1 < self.env.sizeX*self.env.sizeY:
            if length(frontera) <= 0:
                break

            nodo = queue.dequeue_priority(frontera)
            add(explorado,nodo)
            #self.imprimir(frontera)
            #print("-----------------")
            if nodo.estado[0] == self.env.posF[0] and nodo.estado[1] == self.env.posF[1]:
                #recorro desde nodo hasta arriba con padre y formo camino
                camino = LinkedList()
                currentNode = nodo
                while currentNode != None:
                    add(camino,currentNode.estado)
                    currentNode = currentNode.padre
                return camino
            #Ahora insertamos en frontera los nodos sucesores de nodo
            self.expandirUCS(explorado,frontera,nodo)
        return None

    def expandirUCS(self,explorado,frontera,nodo):
        for x in range(0,4):
            n = UCSNode()
            n.costo = 1
            n.padre = nodo
            n.profundidad = nodo.profundidad + 1
            if x == 0:
                n.estado = self.up(nodo)
                n.accion = "arriba"
            elif x == 1:
                n.estado = self.down(nodo)
                n.accion = "abajo"
            elif x == 2:
                n.estado = self.right(nodo)
                n.accion = "derecha"
            elif x == 3:
                n.estado = self.left(nodo)
                n.accion = "izquierda"
            if n.estado != None and self.search(frontera,n) == None and self.search(explorado,n) == None:
                queue.enqueue_priority(frontera,n,n.costo)



#-------------------------------------------------------------------------

    def imprimir(self,L):
        currentnode=L.head
        while currentnode != None:
            print(currentnode.value.estado)
            currentnode=currentnode.nextNode

    
    def search(self,L,element):
        currentNode = L.head
        n = 0
        while currentNode != None:
            if element.estado[0] == currentNode.value.estado[0] and element.estado[1] == currentNode.value.estado[1]:
                return n
            currentNode = currentNode.nextNode
            n = n + 1
        return None



class BFS():
    head = None
  
class BFSNode():
    estado = None
    padre = None
    accion = None
    profundidad = None

class DFS():
    head = None
  
class DFSNode():
    estado = None
    padre = None
    accion = None
    profundidad = None

class UCS():
    head = None
  
class UCSNode():
    estado = None
    costo = None
    padre = None
    accion = None
    profundidad = None









    