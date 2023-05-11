import traceback
import pandas as pd

def extraer_language ():

    try: 
        
        filename = 'D:/tpm/vms/language.csv'

        languages = pd.read_csv(filename)

        return languages

    except:
        traceback.print_exc()
    finally:
        pass