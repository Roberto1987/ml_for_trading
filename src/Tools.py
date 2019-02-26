import os
import pandas as p
import math

p.options.mode.chained_assignment = None


# LOAD MULTIPLE CSV IN A FOLDER
def load_resource(path):
    df_rames = {}
    print(os.getcwd())
    for i in list(os.listdir(path)):
        label = i.split('.')[0]
        df_rames[label] = p.read_csv(path + '/' + i, index_col='Date')
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
    df[1:] = (df[1:] / df[:-1].values) - 1
    df[0] = 0
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


# FILL EMPTY DATA FROM THE LAST VALID VALUE . -->
def forwardfill_data(df: p.DataFrame):
    return df.fillna(method='ffill')


def stochastic_sum(x: list):
    return (sum(x) == 1)

# Evaluate a portfolio using daily returns

def portfolio_eval(prices: p.DataFrame, allocations: list, investment, start_day=None, end_day=None):
    if len(prices.iloc[0]) != len(allocations):
        raise Exception('Allocation vector size:{}, number of columns: {}. '
                        'Please correct the allocation vector'.format(len(allocations), len(prices.iloc[0])))

    if not stochastic_sum(allocations):
        raise Exception('Allocation of the portfolio is not sum to 1: please revise the allocation percentage')


    # Normalization:
    prices = prices / prices.iloc[0]
    # Allocate
    prices = prices * allocations  # may require to multiply each column separately
    # Money in
    prices = prices * investment
    # Portfolio value
    prices['port_values'] = prices.sum(axis=1)
    return prices


# Cumulative returns, first price divided by last price , subtract 1
def cumulative_returns(df: p.DataFrame):
    return (df.iloc[-1] / df.iloc[0]) - 1

    pass


def average_daily_returns(df: p.DataFrame):
    return df.mean()


def std_daily_returns(df: p.DataFrame):
    return df.std()


def risk(df: p.DataFrame):
    pass


def sharp_ratio(df: p.DataFrame, sampling_rate, free_risk_return=0):
    return math.sqrt(sampling_rate) * (average_daily_returns(df) - free_risk_return) / (std_daily_returns(df))
