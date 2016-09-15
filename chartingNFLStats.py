import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame

def chartOffvsDef(df):
    #print(df)
    #sns.kdeplot(df.Overall)
    offlist = ['LWR', 'RWR', 'LT', 'LG', 'C', 'RG', 'RT', 'TE', 'QB', 'RB', 'FB']
    deflist = ['LDE', 'NT', 'RDT', 'SAM', 'SILB', 'RILB', 'WLB', 'LCB', 'SS', 'FS', 'RCB', 'DT', 'RDE', 'SLB', 'MLB',
               'WLB', 'DE', 'OLB', 'ILB', 'NB']
    dfOff = df[df.Position.isin(offlist)]
    #dfOff = dfOff.set_index('Team')
    dfDef = df[df.Position.isin(deflist)]
    #dfDef = dfDef.set_index('Team')

    # dataset1 = df.loc['CAR']['Overall']
    # dataset2 = df.loc['DEN']['Overall']
    dataset1 = dfOff.loc['CAR']
    dataset1a = dataset1[['Position','Overall']]
    # dataset2 = dfDef.loc['DEN']['Overall']
    print(dataset1a)
    # print(dataset2)

    #plt.hist(dataset1a['Overall'],color='red',alpha=0.5)
    # plt.hist(dataset2,normed=True,color='blue',alpha=0.5)
   # plt.show()
