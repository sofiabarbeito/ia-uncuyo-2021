from algo1 import*
from linkedlist import*

"""
push(S,element)
Descripción: Agrega un elemento al comienzo de S, siendo S una estructura de tipo LinkedList
Entrada: La pila S sobre la cual se quiere agregar el elemento (LinkedList) y el valor del elemento (element) a agregar.
Salida: No hay salida definida


pop(S)
Descripción: extrae el primer elemento de la pila S, siendo S una estructura de tipo LinkedList
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: la pila S (Linkedlist) sobre el cual se quiere realizar la eliminación
Salida : Devuelve el elemento eliminado. Devuelve None si la pila esta vacia.

"""



def push(S,element):
  insert(S,element,0)

def pop(S):
  if length(S) >= 0 and access(S,0)!= None:
    z = access(S,0)
    delete(S,z)
    return z
  else:
    return None
