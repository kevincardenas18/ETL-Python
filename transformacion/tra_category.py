import traceback
import pandas as pd
from datetime import datetime

def transformar_category (categories):

    try: 
        
        categories['now'] = datetime.now()

        return categories

    except:
        traceback.print_exc()
    finally:
        pass