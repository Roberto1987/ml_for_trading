import os
import pandas as p


# LOAD MULTIPLE CSV IN A FOLDER
def load_resource(path):
    df_rames = {}
    print(os.getcwd())
    for i in list(os.listdir(path)):
        label = i.split('.')[0]
        df_rames[label] = p.read_csv(path + '/' + i)
        print('Source file {} loaded'.format(label))
    return df_rames


# DROP VOLUME
def drop_volume(dataframes: dict):
    for i in dataframes.values():
        i.drop(columns='Volume', axis=1, inplace=True)


# AGGREGATE MULTIPLE STOCKS BY A SINGLE VALUE (OPEN,CLOSE,HIGH...)
def multistock(df_list: dict, label: str):
    df_mesh = p.DataFrame()
    for i in df_list:
        print(i)
        df_mesh[i] = df_list[i][label]
    return df_mesh


# COMPUTE DAILY RETURNS ON ONE COLUMNS

def daily_returns(df: p.DataFrame):
    print('Processing daily returns for dataframe : {}'.format(df.name))
    df = (df[1:] / df[:-1].values) - 1
    df[1] = 0
    return df


# COMPUTE BOLLINGER BANDS
def bollinger_bands(df: p.DataFrame, std: p.DataFrame):
    upper_band, lower_band = df + 2 * std, df - 2 * std
    return upper_band, lower_band


# COMPUTE ROLLING MEAN/ MOVING AVERAGE
def rolling_mean(df, label, window):
    return df[label].rolling(window).mean()


# COMPUTE ROLLING Standard Deviation
def rolling_std(df, label, window):
    return df[label].rolling(window).std()


# FILL EMPTY DATA FROM THE FIRST VALID VALUE  <-- .
def backfill_data(df: p.DataFrame):
    return df.fillna(method='bfill')


# FILL EMPTY DATA FROM THE LASTVALID VALUE . -->
def forwardfill_data(df: p.DataFrame):
    return df.fillna(method='ffill')
