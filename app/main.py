"""
Este script permite al usuario seleccionar una columna de datos de población o área de un archivo CSV 
y generar un gráfico de torta o de barras basado en la selección. 

Requisitos:
- Python 3.x instalado
- Las bibliotecas `inquirer`, `matplotlib` y `pandas` deben estar instaladas.

Para instalar las dependencias necesarias, ejecuta en tu terminal:
    pip install inquirer matplotlib pandas

Uso:
- Ejecuta el script en un entorno de Python compatible.
- Sigue las indicaciones en la terminal para seleccionar la columna de datos y la región que deseas graficar.

Autor: David
Fecha: 4-Sept-24
"""

# Importaciones necesarias
import inquirer
import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV con los datos
path = './data.csv'

def menu_options():
    """
    Muestra un menú con las opciones de columnas de datos disponibles para graficar.

    Returns:
        str: La columna seleccionada por el usuario.
    """
    questions = [
        inquirer.List('column',
                      message="¿Qué columna deseas graficar?",
                      choices=[
                          '2022 Population',
                          '2020 Population',
                          '2015 Population',
                          '2010 Population',
                          '2000 Population',
                          '1990 Population',
                          '1980 Population',
                          '1970 Population',
                          'Area (km²)',
                          'Density (per km²)',
                          'Growth Rate',
                          'World Population Percentage',
                      ],
        ),
    ]
    options = inquirer.prompt(questions)
    choice = options["column"]

    return choice

def menu_regions():
    """
    Muestra un menú con las opciones de regiones disponibles para graficar.

    Returns:
        str: La región seleccionada por el usuario.
    """
    questions = [
        inquirer.List('column',
                      message="¿Qué región deseas graficar?",
                      choices=[
                          'Asia',
                          'Europe',
                          'Africa',
                          'Oceania',
                          'North America',
                          'South America',
                      ],
        ),
    ]
    options = inquirer.prompt(questions)
    regions = options["column"]

    return regions

def country_historical_population(path):
    """
    Genera un gráfico basado en la selección de columna y región del usuario.

    Args:
        path (str): Ruta al archivo CSV que contiene los datos.

    Returns:
        dict: Diccionario con los datos ordenados.
    """
    choice = menu_options()
    region = menu_regions()

    # Leer el archivo CSV usando pandas
    df = pd.read_csv(path)

    # Filtrar los datos por región seleccionada
    df_region = df[df['Continent'] == region].copy()  # Utilizamos .copy() para evitar la advertencia

    # Convertir la columna seleccionada a tipo numérico, manejando errores
    df_region.loc[:, choice] = pd.to_numeric(df_region[choice], errors='coerce')

    # Eliminar filas con valores NaN en la columna seleccionada
    df_region = df_region.dropna(subset=[choice])

    try:
        if choice in ['Growth Rate', 'World Population Percentage', 'Density (per km²)']:
            # Preparar datos para gráfico de torta
            sorted_data = df_region.sort_values(by=choice, ascending=False)

            # Crear gráfico de torta
            fig, ax = plt.subplots()
            ax.pie(sorted_data[choice], labels=sorted_data['Country/Territory'], autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Asegurar que el gráfico de torta sea un círculo perfecto
            
            plt.savefig(f'./imgs/{region}_chart_view.jpg')
            plt.close()
        else:
            # Preparar datos para gráfico de barras
            sorted_data = df_region.sort_values(by=choice, ascending=False)

            # Crear gráfico de barras
            fig, ax = plt.subplots()
            ax.bar(sorted_data['Country/Territory'], sorted_data[choice])
            
            plt.savefig(f'./imgs/{region}_bars_view_final.jpg')
            plt.close()
    except Exception as e:
        print(f'Error al generar el gráfico: {e}')
    
    return sorted_data

# Ejecutar la función principal
country_historical_population(path)
