<h2> PUNTO 1 </h2>
<h4> 
Grilla de 9x9, con 81 casillas en total, consideramos que tiene 81 variables.
</h4>
<h4> 
Las casillas vacías tienen el dominio D = {1,2,3,4,5,6,7,8,9}, y las que ya estaban llenas, tienen un solo valor.
</h4>
<h4> 
Hay 27 restricciones, para cada fila, columna y caja de 9 casillas, en donde los valores no se pueden repetir. Lo podemos plantear así, en donde las columnas son del 1 al 9, y las filas de la A al I:
</h4>
<h4> 
TodosDiferentes (A1,A2,A3,A4,A5,A6, A7, A8, A9)
  </h4>
<h4> 
TodosDiferentes (B1,B2,B3,B4,B5,B6,B7,B8,B9)
</h4>
<h4> 
· · ·
  </h4>
<h4> 
TodosDiferentes (A1,B1,C1,D1,E1, F1,G1,H1, I1)
  </h4>
<h4> 
TodosDiferentes (A2,B2,C2,D2,E2, F2,G2,H2, I2)
  </h4>
<h4> 
· · ·
  </h4>
<h4> 
TodosDiferentes (A1,A2,A3,B1,B2,B3,C1,C2,C3)
  </h4>
<h4> 
TodosDiferentes (A4,A5,A6,B4,B5,B6,C4,C5,C6)
  </h4>
<h2> PUNTO 2 </h2>

  ![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp6-csp/imagenes/PUNTO2A.PNG?raw=true)
  
  ![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp6-csp/imagenes/PUNTO2B.PNG?raw=true)
  
  ![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp6-csp/imagenes/PUNTO2C.PNG?raw=true)
  
<h2> PUNTO 3 </h2>
<h4> 
Tenemos n variables, con dominios de tamaño d como mucho y una cantidad c de restricciones. La verificación de la arco-consistencia de una variable se puede realizar en tiempo O(d^2), luego debemos verificar cada restricción para cada variable, entonces lo multiplicamos por la cantidad de restricciones, y por los valores del dominio de cada variable, dando como resultado en el peor caso: O(c . d^3).
</h4>

<h2> PUNTO 4 </h2>
<h4>
Podriamos preprocesar las restricciones para que para cada valor de Xi, llevamos un seguimiento de esas variables Xk por las cuales un arco desde Xk a Xi se satisface para ese valor particular de Xi. Esta estructura de datos se puede computar en un tiempo proporcional al tamaño de la representacion del problema. Después, cuando un valor de Xi es eliminado, reducimos por 1 la cuenta de valores posibles para cada arco (Xk,Xi) guardado con ese valor, no deberiamos insertar cada arco (Xk, Xi), por lo que la complejidad en el peor caso que antes era O(n^2xd^3), ahora es O(n^2xd^2).
</h4>

<h2> PUNTO 5 </h2>
<h3>Punto a </h3>
<h4>
Cualquier CSP estructurado por árbol puede resolverse en tiempo lineal en el número de variables. El algoritmo tiene los siguientes pasos:
</h4>
<h4> 
Elija cualquier variable como la raíz del árbol, y ordene las variables desde la raíz a las hojas de tal modo que el padre de cada nodo en el árbol lo precede en el ordenamiento. Etiquetar las variables X1…, Xn en orden. Ahora, cada variable excepto la raíz tiene exactamente una variable\padre.
</h4>
<h4> 

Para j desde n hasta 2, aplicar la consistencia de arco al arco (Xi, Xj), donde Xi es el padre de Xj, quitando los valores del dominio que sea necesario.
</h4>
<h4> 

Para j desde 1 a n, asigne cualquier valor para Xj consistente con el valor asignado para Xi, donde Xi es el padre de Xj.
</h4>
<h4> 
En el paso 1, en el que convertimos el grafo de restricciones en un árbol, solo nos quedan arcos que conectan a los hijos con sus padres, es decir, hay solo una restricción binaria, por lo que no deberemos resolver una consistencia mayor a 2-consistencia o arco consistencia.
</h4>
<h3>Punto b </h3>
<h4> 
Lo argumentado en el ejercicio anterior es suficiente porque ya no hace falta verificar, por ejemplo, que no se cumplan las restricciones de 3-consistencia o camino consistencia, ya que como solo hay restricciones binarias, una vez resueltas, llegamos a la solución. 
</h4>
 
<h2> PUNTO 6 </h2>
<h3>
Forward Checking
</h3>
<h4>
4
  </h4>
<h4>
Tiempo de ejecucion: [0.0]
  </h4>
<h4>
Estados: [26]
</h4>
<h4>
8
  </h4>
<h4>
Tiempo de ejecucion: [0.00894308090209961]
  </h4>
<h4>
Estados: [876]
</h4>
<h4>
10
  </h4>
<h4>
Tiempo de ejecucion: [0.01300191879272461]
  </h4>
<h4>
Estados: [975]
</h4>
<h4>
12
  </h4>
<h4>
Tiempo de ejecucion: [0.04969286918640137]
  </h4>
<h4>
Estados: [3066]
</h4>
<h4>
15
  </h4>
<h4>
Tiempo de ejecucion: [0.6376485824584961]
  </h4>
<h4>
Estados: [20280]
</h4>
<h3> Tiempo de ejecucion</h3>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp6-csp/imagenes/forwardcheckingtiempo.PNG?raw=true)

<h3> Estados</h3>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp6-csp/imagenes/forwardcheckingestados.PNG?raw=true)

<h3>
Backtracking
</h3>
<h4>
4
  </h4>
<h4>
Tiempo de ejecucion: [0.0]
  </h4>
<h4>
Estados: [274]
</h4>
<h4>
8
  </h4>
<h4>
Tiempo de ejecucion: 0.124683746338298
  </h4>
  <h4>
Estados: 233189
</h4>
<h4>
10
  </h4>
<h4>
Tiempo de ejecucion: [4.050742864608765]
  </h4>
<h4>
Estados: [1660100]
</h4>
<h4>
12
  </h4>
<h4>
Tiempo de ejecucion: [33.45374655723572]
  </h4>
<h4>
Estados: [12506605]
</h4>
<h4>
15
  </h4>
<h4>
Tiempo de ejecucion: [873.6974053382874]
  </h4>
<h4>
Estados: [291364134]
</h4>

<h3> Tiempo de ejecucion</h3>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp6-csp/imagenes/backtrackingtiempo.PNG?raw=true)

<h3> Estados</h3>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp6-csp/imagenes/backtrackingestados.PNG?raw=true)
