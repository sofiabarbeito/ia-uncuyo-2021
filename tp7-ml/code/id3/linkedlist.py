from algo1 import *
from math import*

class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None

def add(L,element):
  newNode = Node ()
  newNode.value = element

  if L.head == None:
	  L.head = newNode
  else:	
    newNode.nextNode = L.head
    L.head = newNode
  return L

def search(L,element):
  currentNode = L.head
  n = 0
  while currentNode != None:
    if element == currentNode.value :
      return n
    currentNode = currentNode.nextNode
    n = n + 1
  return None

def insert(L,element,position):
  newNode = Node()
  newNode.value=element
  if position <= length(L):
    if position == 0 :
      add(L,element)
    else:	
      previousNode = L.head
      nextnode = previousNode.nextNode
      i = 1
      while i < (position) :
        nextnode = nextnode.nextNode
        previousNode = previousNode.nextNode
        i=i+1
      
      newNode.nextNode = nextnode 
      previousNode.nextNode = newNode
    return position
  else:
    return None

def delete(L,element):
  posicion = search(L,element)
  if posicion == None:
    return None
  else:
    if posicion == 0:
      L.head = L.head.nextNode
    else:
      currentNode = L.head
      nextN = currentNode.nextNode
      i = 1
      while i < posicion:
        currentNode = currentNode.nextNode
        nextN = nextN.nextNode
        i = i + 1

      currentNode.nextNode = nextN.nextNode

def length(L):
  currentNode = L.head
  n = 0
  if currentNode == None:
    return 0
  while currentNode != None:
    currentNode = currentNode.nextNode
    n = n + 1
  return n

def access(L,position): 
  currentNode = L.head
  n = 0
  if position <= length(L):
    while currentNode != None:
      if n == position:
        return currentNode.value
      currentNode = currentNode.nextNode
      n = n + 1
  else:
    return None

def update(L,element,position):
  currentNode = L.head
  n = 0
  if position <= length(L):
    while currentNode != None: 
      if n == position:
        if currentNode.value != None:
          currentNode.value = element
          return position
        else:
          return None
      currentNode = currentNode.nextNode
      n = n + 1
  else:
    return None

def imprimir(L):
	currentnode=L.head
	while currentnode != None:
		print(currentnode.value)
		currentnode=currentnode.nextNode

def inverse(L):
  if L.head != None:
    Q = LinkedList()
    current = L.head

    for i in range(0,length(L)-1):  #menos 1 asi va desde 0 a n
      current = current.nextNode
    Q.head = current
    longitud = length(L) - 2  #menos 2 pq va desde 0 a n-1
    Qcurrent = Q.head
    while longitud >= 0:
      current = L.head
      for i in range (0,longitud):
        current = current.nextNode
      longitud = longitud - 1
      Qcurrent.nextNode = current 
      Qcurrent = Qcurrent.nextNode
      if i == 0:
        Qcurrent.nextNode = None
    L.head = Q.head
  else:
    return None

def move(L,position_orig,position_dest):
  currentNode = L.head
  n = 0
  while currentNode != None:
    if n == position_orig:
      vo = access(L,position_orig)
    if n == position_dest:
      vd = access(L,position_dest)
    n = n + 1
    currentNode = currentNode.nextNode

  currentNode = L.head
  n = 0
  while currentNode != None:
    if n == position_orig:
      currentNode.value = vd
    if n == position_dest:
      currentNode.value = vo
    n = n + 1
    currentNode = currentNode.nextNode

def transformador(lista,vector):
  if lista != 0:
    current = lista.head
    vector = Array(length(lista),0)
    for x in range(0,length(lista)):
      vector[x] = current.value
      current = current.nextNode
    return vector
  else: 
    L = LinkedList()
    current = L.head
    for x in range(0,len(vector)):
      insert(L,vector[x],length(L))
    return L

