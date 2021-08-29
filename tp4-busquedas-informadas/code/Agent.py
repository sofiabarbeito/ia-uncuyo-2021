
from linkedlist import*


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
#--------------------------------------------------------------------

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
                return access(L,n)
            currentNode = currentNode.nextNode
            n = n + 1
        return None


    def buscoNodoMenor(self,frontera):
        h = frontera.head.value.h
        nodop = access(frontera,0)
        currentN = frontera.head.nextNode
        n = 0
        while currentN != None:
            if currentN.value.h < h :
                h = currentN.value.h
                nodop = access(frontera,n)
            n += 1
            currentN = currentN.nextNode
        delete(frontera,nodop)
        return nodop



    def Aestrella(self):
        nodo = TreeNode()
        nodo.estado = self.env.posI
        nodo.g = 0

        arbol = Tree()
        arbol.head = nodo

        nodo.h = abs(nodo.estado[0]-self.env.posF[0]) + abs(nodo.estado[1]-self.env.posF[1]) #calculo heuristica

        frontera = LinkedList()
        add(frontera,nodo)
        explorado = LinkedList()

        if nodo.estado[0] == self.env.posF[0] and nodo.estado[1] == self.env.posF[1]:
            return explorado

        while length(frontera) > 0:
                    
            nodo = self.buscoNodoMenor(frontera)
            insert(explorado,nodo,length(explorado))

            if nodo.estado[0] == self.env.posF[0] and nodo.estado[1] == self.env.posF[1]:
                return explorado
            
            self.expandirA(explorado,frontera,nodo)

        return None
        
    def expandirA(self,explorado,frontera,nodo):
        for x in range(0,4):
            n = TreeNode()
            n.padre = nodo
            n.g = nodo.g + 1
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
            if n.estado != None:
                n.h = abs(n.estado[0]-self.env.posF[0]) + abs(n.estado[1]-self.env.posF[1]) #calculo heuristica
                if self.search(explorado,n) == None:
                    add(frontera,n)
            

class Tree():
    head = None
  
class TreeNode():
    estado = None
    padre = None
    accion = None
    g = None
    h = None






    