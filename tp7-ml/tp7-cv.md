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
  
  #saco especies con muy pocos datos
  data_train_ceros <- data_train
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
  
  PaloBorracho <- which(data_train_ceros$especie == "Palo borracho")
  PaloBorracho <- sample(PaloBorracho,length(PaloBorracho))
  data_train_ceros <- data_train_ceros[-PaloBorracho,]
  
  
  
  dataframe <- data_train_ceros
  n = 10
  #mezclar dataframe
  set.seed(42)
  rows <- sample(nrow(dataframe))
  dataframe <- dataframe[rows, ]
  
  
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
    #Clase mayoritararia inclinacion peligrosa = 0, la reduzco
    unos <- training_set %>% filter(inclinacion_peligrosa == "si")
    ceros <- training_set %>% filter(inclinacion_peligrosa == "no")
    
    splitted <- sample(1:nrow(ceros),replace = F, size = 3551) 
    ceros <- ceros[ splitted, ]
    training_set <- rbind(ceros,unos)
    
    
    train_formula<-formula(inclinacion_peligrosa~altura+circ_tronco_cm+seccion+especie)
    tree_model_4<-rpart(train_formula,data=training_set)
    
    preds_tree_probs=predict(tree_model_4,validation_set)
    #print(preds_tree_probs)
    preds_tree=ifelse(preds_tree_probs[,2] >=0.5,'si','no')
    #print(preds_tree)
    resultados_validation<-data.frame(inclinacion_peligrosa=preds_tree)
    
    resultados_validation %>% group_by(inclinacion_peligrosa) %>% summarise(total=n())
  
    print("------------------------------------")
    print(y)    
    print(TP(validation_set,resultados_validation))
    print(FP(validation_set,resultados_validation))
    print(FN(validation_set,resultados_validation))
    print(TN(validation_set,resultados_validation))
    print("---------")
    print(accuracy(validation_set,resultados_validation))
    print(precision(validation_set,resultados_validation))
    print(sensitivity(validation_set,resultados_validation))
    print(specificity(validation_set,resultados_validation))
    
    
    a[y] = accuracy(validation_set,resultados_validation)
    p[y] = precision(validation_set,resultados_validation)
    s1[y] = sensitivity(validation_set,resultados_validation)
    s2[y] = specificity(validation_set,resultados_validation)
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
| Media  | 0.7415849  | 0.2386344  | 0.6058162  | 0.7586076  |
| Desviacion Estandar  | 0.01163642  | 0.007823274  | 0.03866692  | 0.01646398  |
