Para entender mas o menos que hace cada notebook, se va a ir explicando que hace cada una o cual es el principal objetivo de estas de forma clara y breve:


1. Cross Validation

* random_forest_cross_validation:
	- Selecciona los atributos y aplica One-Hot Encoding a las variables categóricas.
	- Realiza validación cruzada de 10 pliegues por cada proteína objetivo.
	- Se entrena el modelo con RandomForestRegressor en cada pliegue y se evalúa el rendimiento.
	- Calcula las métricas como R2 y RMSE por cada pliegue.
	- Se realiza un promedio por cada proteína y un promedio global de las métricas.
	- Guarda todos los resultados en un archivo CSV

* visualizacion_csv:
	- Lee un archivo CSV de resultados (generados en la notebook: random_forest_cross_validation)
	- Genera un mapa de calor del archivo CSV de resultados.
	- Se realiza un promedio global de R2 de los valores del CSV.

* predictions_random_forest_ja:
	- Entrena modelos Random Forest por cada proteína a predecir.
	- Guarda cada modelo de Random Forest como una serialización
	- Toma el dataset de nanopartículas que nos adjunto Jair
	- Realiza las predicciones por cada uno de los modelos de Random Forest
	- Guarda los resultados en otro CSV con las respectivas predicciones.

2. Clustering

* projections_of_proteins:
	- Lee el CSV del dataset de nanopartículas. (individual_proteins_dataset.csv)
	- Con el CSV y un atributo categórico, muestra una proyección 2D.
	- Cada nanopartícula está pintada en función de un atributo categórico y sus categorías.
	- Con los mismos parámetros podemos obtener una proyección 3D.

* transformation_binary_proteins
	- Transforma los valores de las proteínas en valores binarios.
	- Si el valor de una proteína es 0, entonces lo deja tal cual.
	- En caso de que sea distinta de 0, entonces le coloca el valor 1.
	- Se utiliza para poder utilizar la distancia Jaccard para la proyección UMAP y para el K-means.
	

* kmeans_clustering:
	- Carga los datos de las proteínas (tal y como están o en binario).
	- Ejecuta K-Means variando la cantidad de clusters entre 2 y 250.
	- Evalúa el modelo usando el Silhouette Score:
		- Lo hace con la métrica Jaccard en caso de que los datos de las proteínas sean binarios.
		- Lo hace con otra métrica (como la Coseno o la Euclidiana) en otro caso.
	- Gráfica los puntajes para ver el número optimo de clusters.

* frequency_categories:
	- Muestra gráficos en barra mostrando que tan frecuente es una categoría de cada atributo categórico
	- Filtra el DataFrame conservando las filas donde  el valor de los atributos categóricos aparece al menos 25 veces (este valor puede ser modificado).
	- Es decir que filtra el valor de los atributos categóricos en función de la frecuencia de aparición

	- Realiza una Proyección 2D de cada atributo categórico
	- Cada nanopartícula está pintada en función de un atributo categórico y sus categorías
	- La Proyección puede utilizar varias métricas como:
		- Jaccard (hay que transformar las proteínas a binario)
		- Cosine.
		- Euclidean.