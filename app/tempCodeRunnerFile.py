"""
Este script permite al usuario seleccionar una columna de datos de población o área de un archivo CSV 
y generar un gráfico de torta o de barras basado en la selección. 

Requisitos:
- Python 3.x instalado
- Las bibliotecas `inquirer`, `matplotlib` y `csv` deben estar instaladas.

Para instalar las dependencias necesarias, ejecuta en tu terminal:
    pip install inquirer matplotlib

Uso:
- Ejecuta el script en un entorno de Python compatible.
- Sigue las indicaciones en la terminal para seleccionar la columna de datos y la región que deseas graficar.

Autor: [Tu Nombre]
Fecha: [Fecha]
"""

# Importaciones necesarias
import inquirer
import csv
import matplotlib.pyplot as plt

# Ruta al archivo CSV con los datos
path = './app/data.csv'

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

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        countries = []
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            if country_dict['Continent'] == region:
                countries.append(country_dict['Country/Territory'])
                try:
                    if choice in ['Growth Rate', 'World Population Percentage', 'Density (per km²)']:
                        data.append(float(country_dict[choice]))
                    else:
                        data.append(int(country_dict[choice]))
                except ValueError:
                    print(f"Error al convertir el valor: {country_dict[choice]} de la columna {choice}")
                    break
        
        try:
            if choice in ['Growth Rate', 'World Population Percentage', 'Density (per km²)']:
                # Preparar datos para gráfico de torta
                final_data = {countries[i]: data[i] for i in range(len(data))}
                sorted_data = dict(sorted(final_data.items(), key=lambda item: item[1], reverse=True))
                
                # Crear gráfico de torta
                fig, ax = plt.subplots()
                ax.pie(sorted_data.values(), labels=sorted_data.keys(), autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  # Asegurar que el gráfico de torta sea un círculo perfecto
                
                plt.savefig('chart.jpg')
                plt.close()
            else:
                # Preparar datos para gráfico de barras
                final_data = {countries[i]: data[i] for i in range(len(data))}
                sorted_data = dict(sorted(final_data.items(), key=lambda item: item[1], reverse=True))
                
                # Crear gráfico de barras
                fig, ax = plt.subplots()
                ax.bar(sorted_data.keys(), sorted_data.values())
                
                plt.savefig('bars.jpg')
                plt.close()
        except Exception as e:
            print(f'Error al generar el gráfico: {e}')
        
        return sorted_data

# Ejecutar la función principal
country_historical_population(path)
