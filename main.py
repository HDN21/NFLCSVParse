import DepthChartParser
import chartingNFLStats
import pandas as pd
from pandas import DataFrame, Series


def main():

    #QBParse.QBStats()
    #test.test()

    #url = 'http://www.cbssports.com/nfl/stats/teamsort/nfl/year-2015-season-regular-category-total-type-offense'
    # url = 'https://www.teamrankings.com/nfl/stat/passing-play-pct'
    # dframe_list = pd.io.html.read_html(url)
    # dframe2 = dframe_list[0]
    # #dframe3 = dframe2[['Team', '2015', '2014']]
    # dframe3 = DataFrame(data=dframe2, columns=['Team','2015','2014'])
    # print(dframe3)

    #print(DepthChartParser.retrieveDepthCharts())

    # df1 = DepthChartParser.retrieveDepthCharts()
    # df2 = DepthChartParser.readMaddenRatings()
    #
    # df3 = DepthChartParser.combineDepthWithMadded(df1,df2)
    #
    # df4 = DepthChartParser.returnMatchUp(df3)

    df = pd.read_csv('week1matchup.csv')
    df1 = df.set_index('Team')

    chartingNFLStats.chartOffvsDef(df1)

if __name__ == "__main__":
    main()