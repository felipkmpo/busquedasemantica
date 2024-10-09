# -*- coding: utf-8 -*-
"""semantic_search_students.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X9KWT3f4E9JkOacxdK6pFZKZZTwRcEqp

## Instalando dependencias necesarias
"""#importamos libreria pandas


#importamos libreria pandas, modulo "util" y "sentence trasnformers" incluidas dentro de las librerias sentence_transformers

import pandas as pd
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

"""## Entendiendo el dataset"""

# TODO: mostrar los primeros 5 registros de dataframe
pelis = pd.read_csv("IMDBtop1000.csv")
#print(pelis.head())

"""## Usando Sentence Transformer para crear embeddings"""

#cargamos en la variable "model" un modelo de sentence transformes pre-entrenado llamado "all minilm-l6-v2",
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#Esta línea de código genera incrustaciones para las descripciones de las películas de su conjunto de datos utilizando el modelo Sentence Transformers preentrenado que cargamos anteriormente.
embeddings = model.encode(pelis['Description'],batch_size=64,show_progress_bar=True)

"""Esta línea de código añade una nueva columna llamada 'embeddings' a su DataFrame pelis y almacena los embeddings
generados en esa columna. También convierte las incrustaciones de una matriz NumPy a una lista."""
pelis['embeddings'] = embeddings.tolist()

"""## Calculando la similitud usando la métrica de similitud por coseno, el código define una función llamada compute_similarity que calcula la similitud entre dos embeddings, utilizando la similitud del coseno."""

def compute_similarity(example, query_embedding):
    embedding = example['embeddings']
    similarity = util.cos_sim(embedding, query_embedding).item()
    return similarity

## Ejecuntando la búsqueda
# Creamos un nuevo dataframe vacío para almacenar los resultados de búsqueda
df_results = pd.DataFrame()
#creamos un ciclo while con el fin de realizar varias busquedas hasta que el usuario decida detener la busqueda
while True:
    query_description = input("Ingrese descripción de la película o escriba 'salir' para detener la búsqueda: ")
    if query_description.lower() == 'salir':
        break

    query_embedding = model.encode([query_description])[0]
    pelis['similarity'] = pelis.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
    pelis = pelis.sort_values(by='similarity', ascending=False)
    pelis['Description_Cast'] = pelis['Description'] + ' ' + pelis['Cast']

    # Seleccionamos las columnas relevantes
    search_result = pelis[['Title', 'Description_Cast', 'similarity']].head()

    # Guardamos los resultados en el nuevo dataframe
    df_results = pd.concat([df_results, search_result])

    print(search_result)



# Imprimimos o guardamos el dataframe con todos los resultados
print("Resultados acumulados:")
print(df_results)
print("Busqueda Finalizada.")




"""df = pelis

while True:
    query_description = input("ingrese descripcion de pelicula o escriba 'salir' para detener la busuqeda: ")
    if query_description.lower() == 'salir':
        break

    query_embedding = model.encode([query_description])[0]
    df['similarity'] = df.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
    df = df.sort_values(by='similarity', ascending=False)

    print(df.head()['Title'])

print("busqueda finalizada.")"""

