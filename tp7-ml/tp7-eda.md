<h2> Punto 2 </h2>
<h3>a. ¿Cual es la distribución de las clase inclinacion_peligrosa? </h3>
<h4>La clase inclinacion_peligrosa tiene mayor cantidad de casos con valor "no".</h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/2a.PNG?raw=true)


<h3> </h3>
<h3>2) b. ¿Se puede considerar alguna sección más peligrosa que otra? </h3>
<h4>Podriamos decir que la seccion 4 es mas peligrosa, ya que es la que tiene mas casos con valor "si", pero no es mucho a comparacion con las demas. Asique no podriamos considerar una seccion mas peligrosa que otra.</h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/2b.PNG?raw=true)

<h3> </h3>
<h3>2) c. ¿Se puede considerar alguna especie más peligrosa que otra? </h3>
<h4>Podriamos decir que la especie Morera es mas peligrosa, ya que es la que tiene mas casos con valor "si", pero es la especie que mas casos tiene, en total tiene 10564. Las demas especies tiene muchos menos casos, por lo que no podriamos considerar esta especie como la mas peligrosa.</h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/2c.PNG?raw=true)

<h3> </h3>

<h2> Punto 3 </h2>
<h3>b. Generar un histograma de frecuencia para la variable circ_tronco_cm. Probar con diferentes  números de bins.   </h3>
<h4> 5 bins </h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/3b5.PNG?raw=true)

<h4> 20 bins </h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/3b20.PNG?raw=true)

<h4> 100 bins </h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/3b100.PNG?raw=true)


<h3>c. Repetir el punto b) pero separando por la clase de la variable inclinación_peligrosa</h3>
<h4> 5 bins </h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/3c5.PNG?raw=true)

<h4> 20 bins </h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/3c20.PNG?raw=true)

<h4> 100 bins </h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/3c100.PNG?raw=true)


<h3>d. Crear una nueva variable categórica de nombre circ_tronco_cm_cat a partir circ_tronco_cm, en donde puedan asignarse solo  4 posibles valores [ muy alto, alto, medio, bajo ]. Utilizar la información del punto a. para seleccionar los puntos de corte para cada categoría</h3>
<h4> Teniendo en cuenta la cantidad de datos, decidi hacer los cortes para que en cada categoria hubiera una cantidad de datos parecida, excepto en la categoria 'Muy alto', ya que hay menos casos. </h4>

![alt text](https://github.com/sofiabarbeito/ia-uncuyo-2021/blob/main/tp7-ml/graficos/3d.PNG?raw=true)
