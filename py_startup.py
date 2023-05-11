# this file is a kind of python startup module used for manual unit testing

import traceback

from extraccion.ext_country import  extraer_country
from extraccion.ext_city import  extraer_city
from extraccion.ext_address import  extraer_address
from extraccion.ext_customer import  extraer_customer
from extraccion.ext_store import  extraer_store
from extraccion.ext_staff import  extraer_staff
from extraccion.ext_payment import  extraer_payment
from extraccion.ext_rental import  extraer_rental
from extraccion.ext_inventory import  extraer_inventory
from extraccion.ext_film import  extraer_film
from extraccion.ext_film_actor import  extraer_film_actor
from extraccion.ext_actor import  extraer_actor
from extraccion.ext_film_category import  extraer_film_category
from extraccion.ext_category import extraer_category
from transformacion.tra_category import transformar_category
from extraccion.ext_language import extraer_language
from extraccion.per_country import persistir_country
from extraccion.per_city import  persistir_city
from extraccion.per_address import  persistir_address
from extraccion.per_customer import  persistir_customer
from extraccion.per_store import  persistir_store
from extraccion.per_staff import  persistir_staff
from extraccion.per_payment import  persistir_payment
from extraccion.per_rental import  persistir_rental
from extraccion.per_inventory import  persistir_inventory
from extraccion.per_film import  persistir_film
from extraccion.per_film_actor import  persistir_film_actor
from extraccion.per_actor import  persistir_actor
from extraccion.per_film_category import  persistir_film_category
from extraccion.per_category import persistir_category
from extraccion.per_language import persistir_language
from carga.car_category import cargar_category

try:

    # print ("Ejemplo de extracción de Países desde una BD")
    # countries=extraer_country()
    # print(countries.head())

    # print ("Ejemplo de la persistencia de Países en una BD")
    # persistir_country(countries)

    # print ("Ejemplo de extracción de Ciudades desde una BD")
    # cities=extraer_city()
    # print(cities.head())

    # print ("Ejemplo de la persistencia de Ciudades en una BD")
    # persistir_city(cities)

    # print ("Ejemplo de extracción de Direcciones desde una BD")
    # addresses=extraer_address()
    # print(addresses.head())

    # print ("Ejemplo de la persistencia de Direcciones en una BD")
    # persistir_address(addresses)

    # print ("Ejemplo de extracción de Clientes desde una BD")
    # customers=extraer_customer()
    # print(customers.head())

    # print ("Ejemplo de la persistencia de Clientes en una BD")
    # persistir_customer(customers)

    # print ("Ejemplo de extracción de Tiendas desde una BD")
    # stores=extraer_store()
    # print(stores.head())

    # print ("Ejemplo de la persistencia de Tiendas en una BD")
    # persistir_store(stores)

    # print ("Ejemplo de extracción de Personal desde una BD")
    # staffs=extraer_staff()
    # print(staffs.head())

    # print ("Ejemplo de la persistencia de Personal en una BD")
    # persistir_staff(staffs)

    # print ("Ejemplo de extracción de Pagos desde una BD")
    # payments=extraer_payment()
    # print(payments.head())

    # print ("Ejemplo de la persistencia de Pagos en una BD")
    # persistir_payment(payments)

    # print ("Ejemplo de extracción de Rentas desde una BD")
    # rentals=extraer_rental()
    # print(rentals.head())

    # print ("Ejemplo de la persistencia de Rentas en una BD")
    # persistir_rental(rentals)

    # print ("Ejemplo de extracción de Inventarios desde una BD")
    # inventories=extraer_inventory()
    # print(inventories.head())

    # print ("Ejemplo de la persistencia de Inventarios en una BD")
    # persistir_inventory(inventories)

    # print ("Ejemplo de extracción de Peliculas desde una BD")
    # films=extraer_film()
    # print(films.head())

    # print ("Ejemplo de la persistencia de Peliculas en una BD")
    # persistir_film(films)

    # print ("Ejemplo de extracción de Actores de cine desde una BD")
    # film_actors=extraer_film_actor()
    # print(film_actors.head())

    # print ("Ejemplo de la persistencia de Actores de cine en una BD")
    # persistir_film_actor(film_actors)

    # print ("Ejemplo de extracción de Actores desde una BD")
    # actors=extraer_actor()
    # print(actors.head())

    # print ("Ejemplo de la persistencia de Actores en una BD")
    # persistir_actor(film_actors)

    # print ("Ejemplo de extracción de Categoria de peliculas desde una BD")
    # film_categories=extraer_film_category()
    # print(film_categories.head())

    # print ("Ejemplo de la persistencia de Categoria de peliculas en una BD")
    # persistir_film_category(film_categories)

    # print ("Ejemplo de extracción de Categorias desde un CSV")
    # categories=extraer_category()
    # print(categories.dtypes)
    # print(categories.head())

    # print ("Ejemplo de transformación de Categorias")
    # new_categories=transformar_category(categories)
    # print(new_categories.dtypes)
    # print(new_categories.head())

    # print ("Ejemplo de la persistencia de Categorias en una BD")
    # persistir_category(new_categories)

    # print ("Ejemplo de extracción de Lenguajes desde un CSV")
    # languages=extraer_language()
    # print(languages.dtypes)
    # print(languages.head())

    # print ("Ejemplo de la persistencia de Lenguajes en una BD")
    # persistir_language(languages)

    cargar_category()

except:
    traceback.print_exc()
finally:
    pass