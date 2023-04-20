import traceback
from util.db_conn import Db_Connection
import pandas as pd

def extraer_payment ():

    try:
        type = 'postgres'
        host = '10.10.10.2'
        port = '5432'
        user = 'postgres'
        pwd = 'postgres'
        db = 'dvdrental'

        con_db_trx = Db_Connection(type, host, port, user, pwd, db)
        ses_db_trx = con_db_trx.start()
        if ses_db_trx == -1:
            raise Exception("El tipo de base de datos " + type + " no es válido")
        elif ses_db_trx == -2:
            raise Exception("Error al establecer la conexión de pruebas")        
        
        payments = pd.read_sql('SELECT * FROM payment',ses_db_trx)
        return payments

    except:
        traceback.print_exc()
    finally:
        pass