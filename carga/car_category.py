# import traceback
# from util.db_conn import Db_Connection
# import pandas as pd
# from sqlalchemy import text

# def cargar_category ():
#     try:
#         type = 'postgres'
#         host = '10.10.10.2'
#         port = '5432'
#         user = 'postgres'
#         pwd = 'postgres'
#         db = 'stg_dvdrental'

#         con_db_stg = Db_Connection(type, host, port, user, pwd, db)
#         ses_db_stg = con_db_stg.start()
#         if ses_db_stg == -1:
#             raise Exception("El tipo de base de datos " + type + " no es válido")
#         elif ses_db_stg == -2:
#             raise Exception("Error al establecer la conexión de pruebas")        
       
#         sql_sentence = text("MERGE INTO public.dim_categoria car_ca USING (SELECT category_id, name FROM public.ext_category) AS ext_ca ON car_ca.category_id = ext_ca.category_id WHEN MATCHED THEN UPDATE SET name = ext_ca.name WHEN NOT MATCHED THEN INSERT (category_id, name) VALUES (ext_ca.category_id, ext_ca.name)")
#         with ses_db_stg.begin() as conn:
#             conn.execute(sql_sentence)

#     except:
#         traceback.print_exc()
#     finally:
#         con_db_stg.stop()

# import traceback
# from util.db_conn import Db_Connection
# import psycopg2
# import pandas as pd
# from sqlalchemy import text

# def cargar_category():
#     try:
#         type = 'postgres'
#         host = '10.10.10.2'
#         port = '5432'
#         user = 'postgres'
#         pwd = 'postgres'
#         db_stg = 'stg_dvdrental'
#         db_sor = 'sor_dvdrental'

#         con_db_stg = Db_Connection(type, host, port, user, pwd, db_stg)
#         ses_db_stg = con_db_stg.start()
#         if ses_db_stg == -1:
#             raise Exception("El tipo de base de datos " + type + " no es válido")
#         elif ses_db_stg == -2:
#             raise Exception("Error al establecer la conexión de pruebas")        

#         con_db_sor = Db_Connection(type, host, port, user, pwd, db_sor)
#         ses_db_sor = con_db_sor.start()
#         if ses_db_sor == -1:
#             raise Exception("El tipo de base de datos " + type + " no es válido")
#         elif ses_db_sor == -2:
#             raise Exception("Error al establecer la conexión de pruebas")  

#         # Paso 1: Obtener datos de la tabla de origen
#         data = pd.read_sql("SELECT * FROM public.ext_category", ses_db_stg)

#         # Paso 2: Cargar los datos en la tabla destino
#         data.to_sql('dim_categoria', con=ses_db_sor, schema='public', if_exists='append', index=False)

#         # Paso 3: Actualizar registros duplicados
#         sql_sentence = text("UPDATE public.categoria AS dest SET name = src.name FROM public.category AS src WHERE dest.category_id = src.category_id")
#         with ses_db_sor.begin() as conn:
#             conn.execute(sql_sentence)

#     except:
#         traceback.print_exc()
#     finally:
#         con_db_stg.stop()
#         con_db_sor.stop()


import traceback
from util.db_conn import Db_Connection
import psycopg2
import pandas as pd
from sqlalchemy import text

def cargar_category():
    try:
        type = 'postgres'
        host = '10.10.10.2'
        port = '5432'
        user = 'postgres'
        pwd = 'postgres'
        db_stg = 'stg_dvdrental'
        db_sor = 'sor_dvdrental'

        con_db_stg = Db_Connection(type, host, port, user, pwd, db_stg)
        ses_db_stg = con_db_stg.start()
        if ses_db_stg == -1:
            raise Exception("El tipo de base de datos " + type + " no es válido")
        elif ses_db_stg == -2:
            raise Exception("Error al establecer la conexión de pruebas")        

        con_db_sor = Db_Connection(type, host, port, user, pwd, db_sor)
        ses_db_sor = con_db_sor.start()
        if ses_db_sor == -1:
            raise Exception("El tipo de base de datos " + type + " no es válido")
        elif ses_db_sor == -2:
            raise Exception("Error al establecer la conexión de pruebas")  

    # Leer los datos de la tabla ext_category en un dataframe
        data = pd.read_sql("SELECT category_id, name FROM ext_category", ses_db_stg)

        # Renombrar las columnas del DataFrame para que coincidan con los nombres de columna de la tabla en la base de datos de destino
        data = data.rename(columns={"category_id": "cat_bus_id", "name": "nombre"})

        # Crear TABLA temporAL en sor_dvdrental
        sql_temp = text("""
        CREATE TABLE IF NOT EXISTS temp_categoria (
            CAT_BUS_ID INTEGER NOT NULL,
            NOMBRE VARCHAR(100) NOT NULL
        )
    """)
        with ses_db_sor.begin() as conn:
            conn.execute(sql_temp)

        #Caraga de datos al la tabla temporal
        data.to_sql('temp_categoria', ses_db_sor, schema='public', if_exists='replace', index=False, method='multi', chunksize=1000)

        sql_sentence = text("MERGE INTO public.dim_categoria car_ca USING (SELECT cat_bus_id, nombre FROM public.temp_categoria) AS ext_ca ON car_ca.cat_bus_id = ext_ca.cat_bus_id WHEN MATCHED THEN UPDATE SET nombre = ext_ca.nombre WHEN NOT MATCHED THEN INSERT (cat_bus_id, nombre) VALUES (ext_ca.cat_bus_id, ext_ca.nombre)")
        with ses_db_sor.begin() as conn:
            conn.execute(sql_sentence)

        #Borrar tabla temporal
        sql_drop_temp = text("DROP TABLE IF EXISTS temp_categoria;")
        with ses_db_sor.begin() as conn:
            conn.execute(sql_drop_temp)

    except:
        traceback.print_exc()
    finally:
        con_db_stg.stop()
        con_db_sor.stop()