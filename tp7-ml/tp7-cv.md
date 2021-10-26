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
cross_validation = function(dataframe,n){
  data_train_ceros <- dataframe
  rboldelcielo <- which(data_train_ceros$especie == "rbol del cielo") #length 1
  #rboldelcielo <- sample(rboldelcielo,length(rboldelcielo))
  data_train_ceros <- data_train_ceros[data_train_ceros$especie != "rbol del cielo",]
  
  Maiten <- which(data_train_ceros$especie == "Maiten") #length 1
  #Maiten <- sample(Maiten,length(Maiten))
  #data_train_ceros <- data_train_ceros[-Maiten,]
  data_train_ceros <- data_train_ceros[data_train_ceros$especie != "Maiten",]
  
  Arabia <- which(data_train_ceros$especie == "Arabia")
  Arabia <- sample(Arabia,length(Arabia))
  data_train_ceros <- data_train_ceros[-Arabia,]
  
  Algarrobo <- which(data_train_ceros$especie == "Algarrobo")
  Algarrobo <- sample(Algarrobo,length(Algarrobo))
  data_train_ceros <- data_train_ceros[-Algarrobo,]
  
  
  
  
  
  #mezclar dataframe
  set.seed(42)
  rows <- sample(nrow(data_train_ceros))
  dataframe <- data_train_ceros[rows, ]
  
  
  folds = create_folds(dataframe,n)
  
  a = c(1:10)
  p = c(1:10)
  s1 = c(1:10)
  s2 = c(1:10)
  for (y in 1:n){
    validation_set_index = seq(folds[[y]][1],folds[[y]][2],1)
    validation_set = dataframe[validation_set_index,]
    
    
    if (y == 1){
      training_set_index = seq(folds[[2]][1],folds[[2]][2])
      for (x in 3:n){
        if (x != y){
          training_set_index = append(training_set_index,seq(folds[[x]][1],folds[[x]][2]))
        }
      }
      
    }else{
      training_set_index = seq(folds[[1]][1],folds[[1]][2])
      for (x in 2:n){
        if (x != y){
          training_set_index = append(training_set_index,seq(folds[[x]][1],folds[[x]][2]))
        }
      }
    }
    
    
    
    
    training_set <- dataframe[training_set_index,]
    
    
    train_formula<-formula(inclinacion_peligrosa~altura+circ_tronco_cm+lat+long+seccion+especie)
    tree_model<-rpart(train_formula,data=training_set)
    #print(tree_model)
		# obtenemos la predicción
		p=predict(tree_model,validation_set,type='class')
		#print(p)
	#	preds_tree=ifelse(p[,2] >=0.5,'si','no')
    resultados_validation<-data.frame(inclinacion_peligrosa=p)
    #comparar incl pelogrosa de resultados_validation con incl peligrosa de training set
    
    #print(resultados_validation)
    
    #print("------------------------------------")
    #print(y)    
    #print(TP(training_set,resultados_validation))
    #print(FP(training_set,resultados_validation))
    #print(FN(training_set,resultados_validation))
    #print(TN(training_set,resultados_validation))
    #print("---------")
    #print(accuracy(training_set,resultados_validation))
    #print(precision(training_set,resultados_validation))
    #print(sensitivity(training_set,resultados_validation))
    #print(specificity(training_set,resultados_validation))
    
    a[y] = accuracy(training_set,resultados_validation)
    p[y] = precision(training_set,resultados_validation)
    s1[y] = sensitivity(training_set,resultados_validation)
    s2[y] = specificity(training_set,resultados_validation)
  }
  print("Accuracy")
  print("Media: ")
  print(mean(a))
  print("Desviacion estandar: ")
  print(sd(a))
  
  print("Precision")
  print("Media: ")
  print(mean(p))
  print("Desviacion estandar: ")
  print(sd(p))
  
  print("Sensitivity")
  print("Media: ")
  print(mean(s1))
  print("Desviacion estandar: ")
  print(sd(s1))
  
  print("Specificity")
  print("Media: ")
  print(mean(s2))
  print("Desviacion estandar: ")
  print(sd(s2))
  
}
```

<h1> </h1>

|  | Accuracy | Precision | Sensitivity | Specificity |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Media  | 0.8891066  | -  | 0  | 1  |
| Desviacion Estandar  | 0.0008004518  | -  | 0  | 0  |
