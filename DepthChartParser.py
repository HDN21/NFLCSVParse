import pandas as pd
from pandas import DataFrame, Series

def retrieveDepthCharts():

    depthChartUrl = 'http://www.ourlads.com/nfldepthcharts/pfdepthcharts.aspx'
    depthChartData = pd.io.html.read_html(depthChartUrl)
    dframeData = depthChartData[0]
    df = DataFrame(data=dframeData, columns={0, 1, 3, 5})
    df = df.rename(columns={0: 'Team', 1: 'Position', 3: 'Starter', 5: 'Second'})
    df2 = df.dropna()
    df2 = df2.ix[1:]

    df2['Starter'].replace({'\s[A-Za-z\d\/]*$':''},regex=True,inplace=True)
    #df2['Second'].replace({'\s[A-Za-z\d\/]*$':''}, regex=True,inplace=True)

    df2['Last Name'],df2['First Name'] = zip(*df2['Starter'].map(lambda x:x.split(', ')))
    #df2['SecondLastName'],df2['SecondFirstName'] = zip(*df2['Second'].map(lambda x:x.split(', ')))

    df3 = df2[['Team','Position','Last Name','First Name']]

    #print(df3)

    return(df3)

def readMaddenRatings():

    df = pd.read_csv('NFLDB/madden17ratings.csv')
    df1 = df[['Team','Last Name','First Name','Overall']]

    return(df1)

def combineDepthWithMadded(df1,df2):

    df1['Last Name'] = df1['Last Name'].str.upper()
    df1['First Name'] = df1['First Name'].str.upper()
    df2['Last Name'] = df2['Last Name'].str.upper()
    df2['First Name'] = df2['First Name'].str.upper()

    df3 = pd.merge(df1,df2,on=['Team','Last Name','First Name'])

    df3.to_csv('out.csv',index=False)

    return(df3)