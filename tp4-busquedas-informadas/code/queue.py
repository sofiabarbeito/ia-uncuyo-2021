from algo1 import*
from linkedlist import*

"""
enqueue(Q,element)
Descripción: Agrega un elemento al comienzo de Q, siendo Q una estructura de tipo LinkedList.
Entrada: La cola Q (LinkedList) sobre la cual se quiere agregar el elemento y el valor del elemento (element) a agregar.
Salida: No hay salida definida.

dequeue(S)
Descripción: extrae el último elemento de la cola Q, siendo Q una estructura de tipo LinkedList.
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: la cola Q (Linkedlist) sobre el cual se quiere realizar la eliminación.
Salida : Devuelve el elemento de la cola. Devuelve None si la cola está vacía.
"""

def enqueue(Q,element):
  add(Q,element)

def dequeue(Q):
  if length(Q) >= 0 and access(Q,length(Q)-1)!= None:
    z = access(Q,length(Q)-1)
    delete(Q,z)

    return z
  else:
    return None



class PriorityNode:
  value=None
  nextNode=None
  priority=None

class PriorityQueue:
  head=None

def enqueue_priority(Q,element,prioridad):
  newNode = PriorityNode ()
  newNode.value = element
  newNode.priority = prioridad

  if Q.head == None:
	  Q.head = newNode
  else:	
    newNode.nextNode = Q.head
    Q.head = newNode
  return 0

def dequeue_priority(Q):
#recorro lista buscando mayor prioridad hasta final
  
  pri = Q.head.priority
  nodop = Q.head
  currentN = Q.head.nextNode
  while currentN != None:
    if currentN.priority > pri or currentN.priority == pri:
      pri = currentN.priority
      nodop = currentN
    currentN = currentN.nextNode
  delete(Q,nodop.value)
  return nodop.value
  



