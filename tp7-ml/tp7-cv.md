<h3> Funcion create_folds() </h3>

```
create_folds = function(dataframe,n){
  filas = nrow(dataframe)/n
  x = 0
  lista = list()
  for (y in 1:n){
    lista[[y]] <- (c((x*filas+1),(x*filas+filas)))
    x = x + 1
  }
  return (lista)
}
```

<h3> Funcion cross_validation() </h3>

```
create_folds = function(dataframe,n){
  filas = nrow(dataframe)/n
  x = 0
  lista = list()
  for (y in 1:n){
    lista[[y]] <- (c((x*filas+1),(x*filas+filas)))
    x = x + 1
  }
  return (lista)
}
```

<h1> </h1>

|  | Accuracy | Precision | Sensitivity | Specificity |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Media  | 2811  | 414  | 414  | 414  |
| Desviacion Estandar  | 2823  | 334  | 334  | 334  |
