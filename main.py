import DepthChartParser
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

    DepthChartParser.retrieveDepthCharts()
    
if __name__ == "__main__":
    main()