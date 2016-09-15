import pandas as pd
from pandas import DataFrame

def retrieveDepthCharts():

    depthChartUrl = 'http://www.ourlads.com/nfldepthcharts/pfdepthcharts.aspx'
    depthChartData = pd.io.html.read_html(depthChartUrl)
    dframeData = depthChartData[0]
    df = DataFrame(data=dframeData, columns={0, 1, 3})
    df = df.rename(columns={0: 'Team', 1: 'Position', 3: 'Starter'})
    df2 = df.dropna()
    df2 = df2.ix[1:]

    df2['Starter'].replace({'\s[A-Za-z\d\/]*$':''},regex=True,inplace=True)
    #df2['Second'].replace({'\s[A-Za-z\d\/]*$':''}, regex=True,inplace=True)

    df2['Last Name'],df2['First Name'] = zip(*df2['Starter'].map(lambda x:x.split(', ')))
    #df2['SecondLastName'],df2['SecondFirstName'] = zip(*df2['Second'].map(lambda x:x.split(', ')))

    df3 = df2[['Team','Position','Last Name','First Name']]

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

    df3.to_csv('week1.csv',index=False)

    return(df3)

def returnMatchUp(df):

    dfOff = pd.DataFrame()
    dfDef = pd.DataFrame()
    dfmatchup = pd.DataFrame()
    offlist = ['LWR','RWR','LT','LG','C','RG','RT','TE','QB','RB','FB']
    deflist = ['LDE','NT','RDT','SAM','SILB','RILB','WLB','LCB','SS','FS','RCB','DT','RDE','SLB','MLB','WLB','DE','OLB','ILB','NB']
    dfOff = df[df.Position.isin(offlist)]
    dfOff = dfOff.set_index('Team')
    dfDef = df[df.Position.isin(deflist)]
    dfDef = dfDef.set_index('Team')

    df1 = pd.read_csv('NFLDB/NFL16Schedule.csv')
    df2 = df1[['Away', 'Home', 'Week']]

    teams = []
    dfm = []

    for i in range(0, len(df2)):
        if df2.iloc[i]['Week'] == 1:
            teams.append(df2.iloc[i]['Away'])
            teams.append(df2.iloc[i]['Home'])

    # for item in teams:
    #     dfm.append(dfOff.loc[item])
    #     dfm.append(dfDef.loc[item])
    # for i in len(teams):

    i=0
    while i <= len(teams)-2:
        dfm.append(dfOff.loc[teams[i]])
        i+=1
        dfm.append(dfDef.loc[teams[i]])
        dfm.append(dfOff.loc[teams[i]])
        i-=1
        dfm.append(dfDef.loc[teams[i]])
        i+=2

    results = pd.concat(dfm)
    results.to_csv('week1matchup.csv')

    return(results)

    # print(dfOff)
    # print(dfDef)
    # for item in teams:
    #     print(teams)
    #     print(item)
    #     # dfmatchup.append(dfOff['Team']==item)
    #     # dfmatchup.append(dfDef['Team']==item)
    #     # print(dfmatchup)

    # dfmatchup = df[df.Team.isin(teams)]
    # dfmatchup.reindex(teams)

    # i=0
    # j=2
    # while j <= len(teams):
    #     df[df.Team.isin(teams[i:j])].to_csv('week1matchups.csv',mode='a',index=False)
    #     i+=2
    #     j+=2

    # print(dfmatchup)


