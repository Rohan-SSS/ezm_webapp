import random
import time
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

def generate_custom_data(num_points):
    df = pd.read_csv('data/EURUSD_M30.csv', sep='\t')
    df = df.rename({'Time':'time', 'Open':'open', 'High':'high', 'Low':'low', 'Close':'close'}, axis=1)
    df = df.drop('Volume', axis=1)
    df = df[-200:]
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

