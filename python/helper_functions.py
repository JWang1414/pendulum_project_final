import pandas as pd
import numpy as np

def find_periods(df: pd.DataFrame):
    """
    Calculate the period length for each data point in the dataframe.
    :param df: Pandas dataframe. It is assumed the first column is time.
    :return: A list of all the period lengths.
    """
    periods = []
    rows = len(df.index)

    # Calculate the time between each data point
    for i in range(rows - 1):
        period = df.iat[i + 1, 0] - df.iat[i, 0]
        periods.append(period)

    return periods

def average_periods(df: pd.DataFrame):
    """
    Calculate the average period length for each data point in the dataframe.
    The average is taken over 10 data points.
    :param df: Pandas dataframe. It is assumed the first column is time.
    :return: Two list. One of the average periods, the other of the standard deviations.
    """
    periods = find_periods(df)
    avg_periods = []
    std_list = []

    # Calculate the average period length
    for i in range(0, len(periods), 10):
        temp = periods[i:i + 10]
        avg_periods.append(np.mean(temp))
        std_list.append(np.std(temp))

    return avg_periods, std_list

def every_nth_angle(df: pd.DataFrame, n: int):
    """
    Creates a list of every nth angle in the dataframe.
    :param df: Pandas dataframe. It is assumed the second column is angular position.
    :param n: Jump length. For example, if n = 3, then every third angle will be returned
    :return: A list of every nth angle.
    """
    result = []

    for i in range(0, len(df.index), n):
        result.append(df.iat[i, 1])

    return result