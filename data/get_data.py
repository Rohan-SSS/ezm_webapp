from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from ta.trend import MACD
from ta.momentum import StochRSIIndicator

df = pd.read_csv('data/EURUSD_M30.csv', sep='\t')
df = df.rename({'Time':'time', 'Open':'open', 'High':'high', 'Low':'low', 'Close':'close'}, axis=1)
df = df.drop('Volume', axis=1)
df = df[-200::1]

def generate_custom_data():

    data = []

    for i in range(df.shape[0]):
        row = df.iloc[i]
        
        timestamp_str = row['time']
        open_value = row['open']
        high_value = row['high']
        low_value = row['low']
        close_value = row['close']
        
        timestamp = int(datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S').timestamp()) * 1000
        
        data_point = {
            "date": timestamp,
            "value": close_value,
            "open": open_value,
            "low": low_value,
            "high": high_value
        }

        data.append(data_point)

    return data

def generate_macd():
    macd_indicator = MACD(close=df['close'], window_slow=26, window_fast=12, window_sign=9, fillna=True)
    df['macd_line'] = macd_indicator.macd()
    df['macd_signal'] = macd_indicator.macd_signal()

    data = []

    for i in range(df.shape[0]):
        row = df.iloc[i]
        
        timestamp_str = row['time']
        macd_line = row['macd_line'].round(6)
        macd_signal = row['macd_signal'].round(6)
        timestamp = int(datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S').timestamp()) * 1000
        
        data_point = {
            "date": timestamp,
            "macd_line": macd_line,
            "macd_signal": macd_signal
        }

        data.append(data_point)

    return data


def get_stochastic_rsi():
    stochastic_rsi = StochRSIIndicator(close=df['close'], window=14, fillna=True)
    df['stochastic_k'] = stochastic_rsi.stochrsi_k()
    df['stochastic_d'] = stochastic_rsi.stochrsi_d()

    data = []

    for i in range(df.shape[0]):
        row = df.iloc[i]

        timestamp_str = row['time']
        stochastic_k = row['stochastic_k'].round(2)
        stochastic_d = row['stochastic_d'].round(2)
        timestamp = int(datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S').timestamp()) * 1000

        data_point = {
            "date": timestamp,
            "stochastic_k": stochastic_k,
            "stochastic_d": stochastic_d
        }

        data.append(data_point)
    
    return data

