from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

DT_FILE_PATH = 'bitstamp.csv'

DATA_INICIO = '2018-10-10'
DATA_FIM = '2020-10-10'

def getDataSetFile(file_path):
    dt_bitstamp = pd.read_csv(file_path)
    dt_bitstamp.set_index('Timestamp')
    #dt_bitstamp = dt_bitstamp.set_index(pd.DatetimeIndex(dt_bitstamp['Timestamp'].values))
    #dt_bitstamp = pd.read_csv(file_path, iterator=True, chunksize=10000)
    # dt_bitstamp = pd.concat(dt_bitstamp, ignore_index=True)
    # dt_bitstamp = pd.DataFrame(dt_bitstamp, index=pd.date_range(DATA_INICIO, DATA_FIM).values)

    return dt_bitstamp

    #dt_bitstamp = dt_bitstamp.set_index(pd.DatetimeIndex(dt_bitstamp['Timestamp'].values))
    #dt_bitstamp = pd.DataFrame(dt_bitstamp, index=pd.date_range(DATA_INICIO, DATA_FIM).values)  
    #dt_bitstamp = dt_bitstamp.set_index(pd.DatetimeIndex(dt_bitstamp['Timestamp'].values))

    # a = pd.to_datetime(dt_bitstamp['Timestamp'], unit='s').dt_bitstamp.strftime('%Y-%m-%d %H:%M')

    # dt_bitstamp['Timestamp'] = pd.date_range(DATA_INICIO, DATA_FIM, freq='H').values
    # df2 = dt_bitstamp.set_index('Timestamp')

    #print(df['Timestamp'].loc[DATA_INICIO:DATA_FIM])

def simpleMovingAverage(dataSet, period=40):
    ma = dataSet['Close'].rolling(window=period).mean()
    return ma


def movingAverage(dataSet, period=9):
    dataSet['EMA'] = dataSet['Close'].ewm(span=period, adjust=False).mean()


def bollingerBands(dataSet, period=14, deviation=2):
    dataSet['MA'] = simpleMovingAverage(dataSet, period)

    dataSet['STD'] = dataSet['Close'].rolling(window=deviation).std()

    dataSet['BBUpper'] = dataSet['MA'] + (dataSet['STD'] * 2)
    dataSet['BBLower'] = dataSet['MA'] - (dataSet['STD'] * 2)

    column_list = ['MA', 'BBUpper', 'BBLower']
    return column_list

def plotBollingerAndMAverage(dataSet, column_list):
    dataSet[column_list].plot(figsize=(12.2, 6.4))
    plt.title('Close Price')
    plt.xlabel('Close Price')
    plt.ylabel('Price')
    plt.show()


def writeDataFrameToCSV(dataSet, column_list):
    finalDataFrame = dataSet[['Timestamp', 'MA', 'BBUpper', 'BBLower','EMA']]
    print(finalDataFrame.head())

    finalDataFrame = finalDataFrame.set_index(pd.DatetimeIndex(finalDataFrame['Timestamp'].values))
    print(finalDataFrame.head())

    finalDataFrame.to_csv('teste.csv')


def main():
    dataSet = getDataSetFile(DT_FILE_PATH)
    dataSet.head()
    movingAverage(dataSet)
    bands = bollingerBands(dataSet,2)
    # plotBollingerAndMAverage(dataSet, bands)
    writeDataFrameToCSV(dataSet, bands)


if __name__ == '__main__':
    main()
