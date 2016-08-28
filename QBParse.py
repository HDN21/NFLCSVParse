import pandas as pd
import numpy as np

def QBStats():

    df = pd.read_csv('../NFLDB/2015_QBvsDef.csv')

    #df1 = pd.DataFrame(df)
    #df.to_csv('../NFLDB/test.csv',index=False)

    print(df.to_string(index=False))

    #print(df1)
