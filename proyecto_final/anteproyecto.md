# ALGORITMOS DE BÚSQUEDA LOCAL: ORGANIZACIÓN DE TAREAS

### Integrantes: 

Sofia Barbeito 11640

Lucia Cairo 13030

### Descripción: 

El objetivo es averiguar qué algoritmo presenta mayores ventajas para asignar el máximo número de trabajos o tareas posible dentro de un tiempo determinado. Cada trabajo tiene su tiempo (en horas): hora de inicio propuesta y tamaño del trabajo y una tolerancia con que la hora de inicio real puede apartarse de la hora de inicio: tolerancia a desplazarse hacia la izquierda y tolerancia a desplazarse hacia la derecha, es decir cada  trabajo guarda 4 datos.

Para esto se usan los algoritmos de búsqueda local: 

Hill-Climbing, un algoritmo iterativo que comienza con una solución arbitraria a un problema y luego intenta encontrar una mejor solución variando incrementalmente un elemento de la solución 

Simulated Annealing, un algoritmo de búsqueda metaheurística cuyo objetivo general es encontrar una buena aproximación al valor óptimo de una función en un espacio de búsqueda grande aleatoria.

Algoritmos Genéticos, algoritmos que hacen evolucionar una población de individuos con acciones aleatorias semejantes a las que actúan en la evolución biológica (mutaciones y recombinaciones genéticas), así como también a una selección de acuerdo con algún criterio, en función del cual se decide cuáles son los individuos más adaptados, que sobreviven, y cuáles los menos aptos, que son descartados.

Para comparar los algoritmos vamos a realizar distintas pruebas combinando diferentes operadores, estados iniciales, funciones heurísticas y parámetros. La forma de evaluación de la eficiencia de los distintos algoritmos en este problema de optimización será a través del tiempo de ejecución, la cantidad de estados recorridos y la cantidad de trabajos asignados.

Alcance: Los algoritmos que implementaremos serán probados en conjuntos de tareas que se generarán de manera aleatoria. Luego, se desarrollará una comparación de los resultados de los tres algoritmos, determinando cuál algoritmo es el más eficiente.

Limitaciones: Los algoritmos de búsqueda local en inteligencia artificial, que son los investigados y puestos en práctica en este trabajo, presentan la desventaja de que pueden caer en un mínimo o máximo local y no salir de allí, considerando esta como la mejor solución .

### Bibliografía

Se consultó el libro AIMA 3rd Edition y AIMA 2da Edition (en español)

### Código del proyecto: 

**BL_Organizacion_Tareas** (Organización de tareas con algoritmos de Búsqueda Local)

### Justificación: 

Dado que tratamos con un problema de optimización, se pueden aplicar algoritmos/técnicas de Búsqueda local ya que estos son la base de muchos de los métodos usados en problemas de optimización. Este es un método determinístico que no necesita memoria, lo cual vemos como una ventaja muy importante. Por otro lado, el camino para llegar a la solución no nos importa, solo queremos la mejor de entre las soluciones posibles alcanzables en un tiempo razonable y esto es lo que nos ofrecen dichos algoritmos de búsqueda local en inteligencia artificial. Además, la búsqueda local es un algoritmo muy superior a la búsqueda aleatoria siendo una mejor opción para resolver el problema.   


### Listado de actividades a realizar:

*Actividad 1* Recopilación de información y/o ejemplos del problema a resolver. [2 días]

*Actividad 2* Planteo del problema inicial (crear datos de las tareas). [1 día]

*Actividad 3* Puesta a punto del código con Hill-Climbing   [4 días]

*Actividad 4* Puesta a punto del código con Simulated Annealing . [4 días]

*Actividad 5* Puesta a punto del código con Algoritmos Genéticos  [4 días]

*Actividad 6* Ejecución de los experimentos con los distintos parámetros. [2 días]

*Actividad 7* Recopilación de los resultados. [1 día]

*Actividad 8* Ordenar los resultados. [1 día]

*Actividad 9* Análisis y comparación de los resultados. [1 día]

*Actividad 10* Elaboración de conclusiones a partir de los resultados. [2 día]

*Actividad 11* Escritura de informe final. [5 días]

### Cronograma estimado de actividades:

![image](https://user-images.githubusercontent.com/88351747/139602774-d802ca6a-db8b-44f3-a792-0abc47b12ce5.png)


