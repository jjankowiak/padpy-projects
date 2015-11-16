import pandas as pd
from os import path

def read_defs(folder):
    defs = pd.read_json(path.join(folder, 'defs.txt'), typ = 'series')
    return defs
    