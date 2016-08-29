import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def test():
    raw_data = {'Team': ['@JAX', 'HOU', 'NO', '@TB', 'BYE', '@SEA'],
                'Score': ['20-9', '24-17', '27-22', '37-23', '0-0', '27-23'],
                'W/L': ['W', 'W', 'W', 'W', 'N/A', 'W', ],
                'FPTS': [12.50, 27.40, 29.90, 16.06, 0.0, 19.76]}

    df = pd.DataFrame(raw_data, columns=['Team', 'Score', 'W/L', 'FPTS'])

    print(df)
    num = [0,1,2,3,4,5]
    plt.bar(num, df['FPTS'])
    plt.plot(df['FPTS'])
    plt.ylabel('some numbers')
    plt.show()
