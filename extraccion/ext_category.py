import traceback
import pandas as pd

def extraer_category ():

    try: 
        
        filename = 'D:/tpm/vms/category.csv'

        categories = pd.read_csv(filename)

        return categories

    except:
        traceback.print_exc()
    finally:
        pass