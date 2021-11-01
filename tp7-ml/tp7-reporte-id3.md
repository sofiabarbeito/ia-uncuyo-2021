<h2> Árbol de Decisión sobre dataset tennis.csv: </h2>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/arbol.png?raw=true)



<h2> Estrategias de los árboles de decisión para datos de tipo real: </h2>
<h4>
Si intentamos predecir un valor numérico real, como el precio de una obra de arte, necesitamos un árbol de regresión. 
</h4>
<h4>
Un árbol de regresión es contruido a través de un proceso conocido como Binary Recursive Partitioning, el cual es un proceso iterativo que separa la información en particiones o ramas, y después continúa separando cada partición en grupos mas pequeños, mientras el algorimto se mueve a cada rama.
</h4>
<h4>
Inicialmente, todos los datos del training set son agrupados en una misma partición. El algoritmo entonces empieza dividiendo los datos en una de las dos primeras particiones o ramas, usando cualquier división binaria posible en cada campo. El algoritmo selecciona la división que minimiza la suma de las desviaciones de la media en las dos particiones. Esta regla de división luego es aplicada en cada una de las nuevas ramas. Este proceso continua hasta que cada nodo llega a la cantidad de nodos mínimos especificado por el usuario, y se convierte en un nodo terminal.  
</h4>

<h4>
Los tres métodos que más se usan con árboles de regresión son:  Bagging (bootstrap aggregating), Boosting, y Random Forest.
</h4>
<h4>
  Bagging fue unos de los primeros algoritmos de ensamble que se escribieron. Es un algoritmo simple, pero muy efectivo. Bagging genera muchos conjuntos de entrenemaiento usando muestreo aleatorio con reemplazo (bootstrap sampling), aplica el algoritmo de árboles de regresión para cada set, después toma el promedio de los modelos para calcular las predicciones de los datos nuevos. 
</h4>
<h4>
  La idea detrás del boosting es ajustar, de forma secuencial, múltiples weak learners (modelos sencillos que predicen solo ligeramente mejor que lo esperado por azar). Cada nuevo modelo emplea información del modelo anterior para aprender de sus errores, mejorando iteración a iteración. Tres de los algoritmos de boosting más empleados son AdaBoost, Gradient Boosting y Stochastic Gradient Boosting.
  </h4>
<h4>
  El método Random Trees es una variación de Bagging. Este método funciona entrenando muchos árboles de regresión débiles usando un número de características selecionadas aleatoriamente. Después, toma el valor promedio de los aprendices débiles, y asigna ese valor para el predictor fuerte. Típicamente, el nímero de árboles débiles generados podrian tener un tamaño grande dependiendo del tamaño y la dificultad del conjunto de entrenamiento. Random Trees son paralelizables, por ser una variante de Bagging. Sin embargo, como selecionan una cantidad limitada de características en cada iteración, el funcionamiento es mas rápido que el de bagging. 
    </h4>
  
  
  
 
  
  
