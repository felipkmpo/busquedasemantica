# -*- coding: utf-8 -*-
"""semantic_search_students.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X9KWT3f4E9JkOacxdK6pFZKZZTwRcEqp

## Instalando dependencias necesarias
"""

# Commented out IPython magic to ensure Python compatibility.
#instalamos librerias sentence-trasnformers
# %pip install -U sentence-transformers pandas
#install pandas
#install sentence-transformers
# importamos libreria pandas
import pandas as pd

#importamos modulo "util" y "sentence trasnformers" incluidas dentro de las librerias sentence_transformers
#pip install sentence-transformers

from sentence_transformers import SentenceTransformer
from sentence_transformers import util

"""## Entendiendo el dataset"""

# https://www.kaggle.com/datasets/omarhanyy/imdb-top-1000?resource=download
# TODO: Cargar el archivo del dataset con  pandas
#from google.colab import files
#uploaded = files.upload()

# TODO: mostrar los primeros 5 registros de dataframe
pelis = pd.read_csv("IMDBtop1000.csv")
#print(pelis.head())

"""## Usando Sentence Transformer para crear embeddings"""

#cargamos en la variable "model" un modelo de sentence transformes pre-entrenado llamado "all minilm-l6-v2",
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#Esta línea de código genera incrustaciones para las descripciones de las películas de su conjunto de datos utilizando el modelo Sentence Transformers preentrenado que cargamos anteriormente.
embeddings = model.encode(pelis['Description'],batch_size=64,show_progress_bar=True)

#Esta línea de código añade una nueva columna llamada 'embeddings' a su DataFrame pelis y almacena los embeddings
#generados en esa columna. También convierte las incrustaciones de una matriz NumPy a una lista.
pelis['embeddings'] = embeddings.tolist()

"""## Calculando la similitud usando la métrica de similitud por coseno"""

def compute_similarity(example, query_embedding):
    embedding = example['embeddings']
    similarity = util.cos_sim(embedding, query_embedding).item()
    return similarity



"""df=pelis #definimos la variable df para que dentro de esta quede incluido el dataframe pelis
query_description = input("Enter a movie description: ")
query_embedding = model.encode([query_description])[0]
df['similarity'] = df.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
df = df.sort_values(by='similarity', ascending=False)

df.head()['Title']
"""
## Ejecuntando la búsqueda
df = pelis

while True:
    query_description = input("ingrese descripcion de pelicula o escriba 'salir' para detener la busuqeda: ")
    if query_description.lower() == 'salir':
        break

    query_embedding = model.encode([query_description])[0]
    df['similarity'] = df.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
    df = df.sort_values(by='similarity', ascending=False)

    print(df.head()['Title'])

print("busqueda finalizada.")

