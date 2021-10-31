from algo1 import*
from linkedlist import*
from arboldedecision import*
import csv


tennis = open("C:/Users/sofia/OneDrive/Documentos/FACULTAD/Licenciatura/3/2/Inteligencia Artificial I/TPs/tp7/parte c/tennis.csv")
ejemplos = csv.reader(tennis)
listaEjemplos = list(ejemplos)

atr = listaEjemplos[0] 

atri = Array(len(atr),"")
for i in range(0,len(atr)):
    atri[i] = atr[i]

listaEjemplos.remove(atr)
#print(len(atri))
arbol = APRENDIZAJE_ARBOL_DECISION(listaEjemplos,atri,"no")


print("Raiz: ")
print("atributo ",arbol.respuesta)


print("--------------------------------")
for i in range(0,3):
    print(i)
    print("atributo ", arbol.hijos[i].respuesta)
    print("valor ",arbol.hijos[i].value)


print("--------------------------------")
print("windy")
current = arbol.hijos[0].hijos #lista de hijos de temp
for i in range(0,len(current)):
    print(i)
    print("atributo ", current[i].respuesta)
    print("valor ",current[i].value)

print("--------------------------------")
print("humidity")
current = arbol.hijos[2].hijos #lista de hijos de temp
for i in range(0,len(current)):
    print(i)
    print("atributo ", current[i].respuesta)
    print("valor ",current[i].value)
