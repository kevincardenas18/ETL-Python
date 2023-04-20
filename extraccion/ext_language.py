import traceback
import pandas as pd

def extraer_language ():

    try: 
        
        filename = 'C:/Users/kevin/VirtualBox VMs/tpm/vms/language.csv'

        languages = pd.read_csv(filename)

        return languages

    except:
        traceback.print_exc()
    finally:
        pass