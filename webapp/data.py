import pandas as pd

def ds():
    ds = pd.read_csv("Data.csv")
    return ds

def get_name():
    return ds().name

def get_price():
    return ds().original_price

def get_data(name,col):
    data = ds().loc[ds()['name']==name][col]
    data = next(iter(data), 'no match')
    return data