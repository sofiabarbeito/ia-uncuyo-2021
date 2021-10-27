
<h3>  A. Descripción del proceso de preprocesamiento</h3>

<h5>Primero, eliminamos columnas que no aportaban información importante, como la última modificación, longitud, latitud , el área de la sección, y el nombre de la sección.
También, busqucamos la clase mayoritaria, la cual es cuando los datos tienen inclinacion peligrosa = 0, y eliminamos algunas filas hasta que llegamos a tener misma cantidad de árboles con y sin inclinación peligrosa. </h5>




<h3>  B. Resultados obtenidos sobre el conjunto de validación</h3>

<h5>Matriz de confusion</h5>

| | 0 | 1 |
| --------- | --------- | --------- |
| 0 | 2401 | 1178 |
| 1 | 925 | 1906 |

<h5> Metricas </h5>

| Accuracy| Precision | Sensitivity | Specificity |
| ------------- | ------------- | ------------- | ------------- |
| 0.8658728  | 0.9774583 | 0.8830981 | 0.130137  |

<h3>  C. Resultados obtenidos en Kaggle</h3>

<h5>AUC = 0.68083 </h5>


<h3>  D. Descripción detallada del algoritmo propuesto</h3>
<h5>Tomamos el conjunto data_set para entrenar, y , a partir de él, predecir la inclinación peligrosa de los datos del data_test. Basándonos en la parte A del trabajo práctico, eliminamos las columnas que nos parecian innecesarias (última modificación, longitud, latitud , área de la sección, nombre de la sección), dejando las realmente importantes como la sección, la especie, el diámetro del tronco y la circunferencia del tronco, ya que vimos que algunas de estas variables definian la tendencia a tener una inclinación peligrosa.  </h5>

<h5>Probamos usar variables categóricas en el diámetro del tronco, pero vimos que esto no mejoraba los resultados, asi que no lo aplicamos.  </h5>

<h5>Balanceamos la clase mayoritaria, ya que observamos que esta tenía un porcentaje demasiado alto de árboles sin inclinación peligrosa, quedando así la misma cantidad de árboles con inclinación peligrosa y no peligrosa.</h5>

<h5>Elegimos entrenar el conjunto data_set con Random Forest, ya que nos pareció bueno para generalizar, este algoritmo es una combinación de árboles predictores tal que cada árbol depende de los valores de un vector aleatorio probado independientemente y con la misma distribución para cada uno de estos. Luego, con la función predict, estimamos la inclinación peligrosa del conjunto de datos data_test.</h5>
