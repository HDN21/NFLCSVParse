import pandas as pd
import numpy as np

def QBStats():

    df = pd.read_csv('../NFLDB/2015_QBvsDef.csv')
    df1 = pd.read_csv('../NFLDB/2015_QB_Split.csv')

    #df1 = pd.DataFrame(df)
    #df.to_csv('../NFLDB/test.csv',index=False)

    print(df.loc[df['Team'].isin(['QB vs Falcons'])].to_string(index=False))
    print(df1[(df1['Player'] == 'Cam Newton') & (df1['SPLIT'] == 'VS. ATL')])

    #print(df.to_string(index=False))

    #print(df1)
