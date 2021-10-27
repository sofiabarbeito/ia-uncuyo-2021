
<h3>  A. Descripción del proceso de preprocesamiento (si es que lo hubiera)</h3>

<h5>Eliminé columnas que no aportaban información importante, como la última modificación, longitud, latitud , el área de la sección, y el nombre de la sección.
También busqué la clase mayoritaria, la cual es cuando los datos tienen inclinacion peligrosa = 0, y eliminé algunas filas. </h5>




<h3>  B. Resultados obtenidos sobre el conjunto de validación</h3>

<h5>Matriz de confusion</h5>

| | 0 | 1 |
| --------- | --------- | --------- |
| 0 | 2401 | 1178 |
| 1 | 925 | 1906 |

<h5> Metricas </h5>

| Accuracy| Precision | Sensitivity | Specificity |
| ------------- | ------------- | ------------- | ------------- |
| 0.8658728  | 0.8830981 | 0.9774583 | 0.02540107  |

<h3>  C. Resultados obtenidos en Kaggle</h3>

<h5>AUC = 0.68083 </h5>


<h3>  D. Descripción detallada del algoritmo propuesto</h3>
<h5>Tomamos el conjunto data_set para entrenar, y , a partir de el, predecir la inclinaicon peligrosa de los datos del data_test. Basandonos en la parte A del trabajo practico, eliminamos las columnas que nos parecian innecesarias (última modificación, longitud, latitud , área de la sección, nombre de la sección), dejando las realmente impotantes como la seccion, la especie, el diametro del tronoco y la circunferencia del tronco, ya que vimos que algunas de estas variables definian la tendencia a tener una inclinacion peligrosa.  </h5>

<h5>Probamos usar variables categoricas en el diametro del tronco, pero vimos que esto no mejoraba, los resultados, asi que no lo aplicamos.  </h5>

<h5>Balanceamos la clase mayoritaria, ya que observamos que esta tenia un porcentaje demasiado alto de arboles sin inclinacion peligrosa, quedando asi la misma cantidad de arboles con inclinacion peligrosa y no peligrosa.</h5>

<h5>Entrenamos el conjunto data_set con Random Forest, el cual ... y con la funcion predict, estimamos la inclinacion peligrosa del conjunto de datos data_test.</h5>
