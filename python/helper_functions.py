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
    Intended to be used in conjunction with average_periods.
    :param df: Pandas dataframe. It is assumed the second column is angular position.
    :param n: Jump length. For example, if n = 3, then every third angle will be returned
    :return: A list of every nth angle.
    """
    result = []

    for i in range(0, len(df.index) - 1, n):
        result.append(df.iat[i, 1])

    return result

def control_uncertainties(std, threshold):
    """
    Find uncertainties that are too small and replace them with the threshold.
    :param std: Standard deviation for each data point
    :param threshold: Threshold for outlier detection
    :return: Nothing
    """
    for i in range(len(std)):
        if std[i] < threshold:
            std[i] = threshold

    return

def find_outliers(std, threshold):
    """
    Find the potential outliers in the data.
    Based on the standard deviation.
    :param std: Standard deviation for each data point
    :param threshold: Threshold for outlier detection
    :return: A list of the indices for the outliers.
    """
    indices = []

    for i in range(len(std)):
        if std[i] > threshold:
            indices.append(i)

    return indices

def wipe_outliers(x, y, y_err, x_err):
    """
    Removes outliers from the data.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :param x_err: Error on independent variable.
    :return: Nothing
    """
    # Find outliers
    outliers = find_outliers(y_err, 0.1)

    # Remove outliers
    i = 0
    while i < len(x):
        if i in outliers:
            x.pop(i)
            y.pop(i)
            y_err.pop(i)
            x_err.pop(i)
        else:
            i += 1

    return

def outlier_management(x, y, y_err, x_err):
    """
    Combines numerous functions to manage outliers.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :param x_err: Error on independent variable.
    :return: Nothing
    """
    control_uncertainties(y_err, 0.001)
    wipe_outliers(x, y, y_err, x_err)