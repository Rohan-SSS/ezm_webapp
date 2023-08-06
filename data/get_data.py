from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from ta.trend import MACD

df = pd.read_csv('data/EURUSD_M30.csv', sep='\t')
df = df.rename({'Time':'time', 'Open':'open', 'High':'high', 'Low':'low', 'Close':'close'}, axis=1)
df = df.drop('Volume', axis=1)
df = df[-200::1]

def generate_custom_data(num_points):

    data = []

    for i in range(num_points):
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

def generate_macd(num_points):
    macd_indicator = MACD(close=df['close'], window_slow=26, window_fast=12, window_sign=9, fillna=True)
    df['macd_line'] = macd_indicator.macd()
    df['macd_signal'] = macd_indicator.macd_signal()

    data = []

    for i in range(num_points):
        row = df.iloc[i]
        
        timestamp_str = row['time']
        macd_line = row['macd_line']
        macd_signal = row['macd_signal']
        timestamp = int(datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S').timestamp()) * 1000
        
        data_point = {
            "date": timestamp,
            "macd_line": macd_line,
            "macd_signal": macd_signal
        }

        data.append(data_point)

    return data
