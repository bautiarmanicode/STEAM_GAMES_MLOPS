# Funciones utiles para ETL Y EDA
from textblob import TextBlob
import datetime
import inspect
import re
import matplotlib.pyplot as plt
import inspect
import pandas as pd
import gzip
import os

def data_type_check(df):
    # Create a dictionary to store the data summary
    dataframe = {"columna": [], "%_no_nulos": [], "%_nulos": [], "total_nulos": [], "tipo_dato": []}
    # Header
    print("\n" + "=" * 40)
    print(" Resumen del dataframe:")
    print("\n" + "=" * 40)
    for columna in df.columns:
        # Calcular el porcentaje de no nulos
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        # Obtener el tipo de dato directamente
        tipo_dato = df[columna].dtype  
        # Append la informacion a un diccionario
        dataframe["columna"].append(columna)
        dataframe["%_no_nulos"].append(round(porcentaje_no_nulos, 2))
        dataframe["%_nulos"].append(round(100 - porcentaje_no_nulos, 2))
        dataframe["total_nulos"].append(df[columna].isnull().sum())
        dataframe["tipo_dato"].append(tipo_dato)
    # Creamos el dataframe
    df_info = pd.DataFrame(dataframe)
    print("Dimensiones: ", df.shape)
    print(df_info)    

    


def analisis_sentimiento(review):
    
    if review is None:
        return 1
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    if polarity < -0.2:
        return 0
    elif polarity > 0.2:
        return 2
    else:
        return 1

   
def ej_review_sentimiento(reviews, sentiments):    
    for sentiment_value in range(3):
        print(f"En la sección de evaluación de sentimientos, se presentan los siguientes ejemplos de reseñas para {sentiment_value}:")
        sentiment_reviews = [review for review, sentiment in zip(reviews, sentiments) if sentiment == sentiment_value]        
        for i, review in enumerate(sentiment_reviews[:3], start=1):
            print(f"Reseña: {i}: {review}")        
        print("\n")


def duplicados_columna(df, columna): 
    #Se filtran las filas duplicadas
    duplicated_rows = df[df.duplicated(subset=columna, keep=False)]
    if duplicated_rows.empty:
        return "No hay duplicados"    
    #se ordenan las filas duplicadas para comparar entre sí
    duplicated_rows_sorted = duplicated_rows.sort_values(by=columna)
    return duplicated_rows_sorted


def filtrar_valores_letras(values):
    return [value for value in values if isinstance(value, str)]


def descomprimir_archivos_gz(archivos_gz, carpeta_destino):
    for archivo_gz in archivos_gz:
        with gzip.open(archivo_gz, 'rb') as f_in:
            contenido = f_in.read()
            archivo_destino = os.path.join(carpeta_destino, os.path.splitext(os.path.basename(archivo_gz))[0])
            with open(archivo_destino, 'wb') as f_out:
                f_out.write(contenido)
        print(f'Archivo descomprimido: {archivo_destino}')

    
def data_type_check_EDA(df):
    # Crear un diccionario para almacenar el resumen de los datos
    dataframe = {"columna": [], "no_nulos": [], "%_no_nulos": [], "nulos": [], "%_nulos": [], "tipo_dato": []}
    # Obtener el nombre del DataFrame
    nombre_df = [nombre for nombre, var in inspect.currentframe().f_back.f_locals.items() if var is df][0]
    # Imprimir el resumen del DataFrame
    print("\n" + "=" * 40)
    print(f" Resumen del DataFrame '{nombre_df}': ")
    print("\n" + "=" * 40)
    for columna in df.columns:
        # Calcular el porcentaje y la cantidad de valores no nulos
        cantidad_no_nulos = df[columna].count()
        cantidad_nulos = df[columna].isnull().sum()
        total_valores = len(df[columna])
        # Calcular el porcentaje de valores no nulos y nulos
        porcentaje_no_nulos = (cantidad_no_nulos / total_valores) * 100
        porcentaje_nulos = (cantidad_nulos / total_valores) * 100
        # Obtener el tipo de dato de la columna
        tipo_dato = df[columna].dtype  
        # Añadir la información al diccionario
        dataframe["columna"].append(columna)
        dataframe["no_nulos"].append(cantidad_no_nulos)
        dataframe["%_no_nulos"].append(round(porcentaje_no_nulos, 2))
        dataframe["nulos"].append(cantidad_nulos)
        dataframe["%_nulos"].append(round(porcentaje_nulos, 2))
        dataframe["tipo_dato"].append(tipo_dato)
    # Crear un DataFrame con el resumen de los datos
    df_info = pd.DataFrame(dataframe)
    print("Dimensiones: ", df.shape)
    print(df_info)
    
    # Ordenar el DataFrame por el porcentaje de valores nulos de forma descendente
    df_info = df_info.sort_values(by='%_nulos', ascending=False)
    # Graficar el porcentaje de valores nulos y no nulos por columna
    fig, ax = plt.subplots(figsize=(8, 6))
    bars1 = ax.barh(df_info['columna'], df_info['%_nulos'], color='lightcoral', label='Nulos')
    bars2 = ax.barh(df_info['columna'], df_info['%_no_nulos'], left=df_info['%_nulos'], color='lightgreen', label='No Nulos')
    # Agregar un contador de nulos y no nulos en cada barra
    for bar1, bar2, columna, no_nulos, nulos in zip(bars1, bars2, df_info['columna'], df_info['no_nulos'], df_info['nulos']):
        plt.text(bar1.get_width() - 20, bar1.get_y() + bar1.get_height()/2, f" {nulos}", va='center', ha='right', color='black', fontsize=13)
        plt.text(bar1.get_width() + 1, bar2.get_y() + bar2.get_height()/2, f"{no_nulos}", va='center', ha='left', color='black', fontsize=13)

    ax.set_xlabel('Porcentaje de valores')
    ax.set_ylabel('Columna')
    ax.set_title(f'Cantidad de valores nulos y no nulos por columna en {nombre_df}')
    ax.legend()
    ax.invert_yaxis()
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    # Mover la leyenda a la izquierda y abajo del gráfico
    plt.legend(loc='lower left', bbox_to_anchor=(0.0, -0.15), frameon=False)
    
    plt.show()

