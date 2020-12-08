from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

DT_FILE_PATH = 'bitstamp.csv'

DATA_INICIO = '2000-10-10'
DATA_FIM = '2010-10-10'

def getDataSetFile(file_path):
    dt_bitstamp = pd.read_csv(file_path)
    print(dt_bitstamp.head())
    dt_bitstamp = pd.DataFrame(dt_bitstamp, index=pd.date_range(DATA_INICIO, DATA_FIM, freq='H').values)
    #dt_bitstamp = dt_bitstamp.set_index(pd.DatetimeIndex(dt_bitstamp['Timestamp'].values))
    print(dt_bitstamp.head())

    return dt_bitstamp
    #print(df['Timestamp'].loc[DATA_INICIO:DATA_FIM])


def movingAverage(dataSet, period=9):
    pass


def bollingerBands(dataSet, period=14, deviation=2):
    dataSet['SMA'] = dataSet['Close'].rolling(window=period).mean()

    dataSet['STD'] = dataSet['Close'].rolling(window=deviation).std()

    dataSet['Upper'] = dataSet['SMA'] + (dataSet['STD'] * 2)
    dataSet['Lower'] = dataSet['SMA'] - (dataSet['STD'] * 2)

    column_list = ['SMA', 'Upper', 'Lower']
    return column_list

def plotBollingerAndMAverage(column_list):
    dataSet[show_list].plot(figsize=(12.2, 6.4))
    plt.title('Close Price')
    plt.xlabel('Close Price')
    plt.ylabel('Price')
    plt.show()


def main():
    dataSet = getDataSetFile(DT_FILE_PATH)

    dataSet.to_csv('teste.csv')

if __name__ == '__main__':
    main()
