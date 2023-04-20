# this file is a kind of python startup module used for manual unit testing

import traceback

from extraccion.ext_country import  extraer_country
from extraccion.ext_category import extraer_category
from transformacion.tra_category import transformar_category
from extraccion.per_country import persistir_country
from extraccion.per_category import persistir_category

try:

    print ("Ejemplo de extracción de Países desde una BD")
    countries=extraer_country()
    print(countries.head())

    print ("Ejemplo de la persistencia de Países en una BD")
    persistir_country(countries)

    print ("Ejemplo de extracción de Categorias desde un CSV")
    categories=extraer_category()
    print(categories.dtypes)
    print(categories.head())

    print ("Ejemplo de transformación de Categorias")
    new_categories=transformar_category(categories)
    print(new_categories.dtypes)
    print(new_categories.head())

    print ("Ejemplo de la persistencia de Categorias en una BD")
    persistir_category(new_categories)

except:
    traceback.print_exc()
finally:
    pass