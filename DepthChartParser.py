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

    df2['Starter'].replace({'\s[A-Za-z\d\/]*$':''}, regex=True,inplace=True)
    df2['Second'].replace({'\s[A-Za-z\d\/]*$':''}, regex=True,inplace=True)

    print(df2.head(5).to_string(index=False))

    return(df2.head(32).to_string(index=False))

