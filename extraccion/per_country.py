import traceback
from util.db_conn import Db_Connection
import pandas as pd

def persistir_country (countries):

    try:
        type = 'postgres'
        host = '10.10.10.2'
        port = '5432'
        user = 'postgres'
        pwd = 'postgres'
        db = 'stg_dvdrental'

        con_db_stg = Db_Connection(type, host, port, user, pwd, db)
        ses_db_stg= con_db_stg.start()
        if ses_db_stg == -1:
            raise Exception("El tipo de base de datos " + type + " no es válido")
        elif ses_db_stg == -2:
            raise Exception("Error al establecer la conexión de pruebas")        
        
        countries.to_sql('ext_country', ses_db_stg, if_exists='replace', index=False)

    except:
        traceback.print_exc()
    finally:
        pass