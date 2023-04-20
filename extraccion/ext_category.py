import traceback
import pandas as pd

def extraer_category ():

    try: 
        
        filename = 'C:/Users/kevin/VirtualBox VMs/tpm/vms/category.csv'

        categories = pd.read_csv(filename)

        return categories

    except:
        traceback.print_exc()
    finally:
        pass