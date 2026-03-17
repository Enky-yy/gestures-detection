import pandas as pd
import numpy as np

def load_datasets(path):

    df = pd.read_csv(path)

    x= df.iloc[:,1:].values
    y= df.iloc[:,0].values

    return x,y