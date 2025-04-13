from matplotlib import rc
from helper_functions import *
from fit_functions import *
from main import plot_data
from files import *
import numpy as np

# Define the file list here. Fit function must be defined in main.py
FILE_LIST = LENGTH_FILES

# Define fit settings
# [0] Period vs. mass
# [1] Period vs. length
# [2] Decay vs. mass
# [3] Decay vs. length
PLOT_CHOICE = 0

# Masses and length
MASSES = [50, 100, 200, 300, 500]
LENGTHS = [52.1, 46.8, 38.0, 30.5, 21.2, 17.2]


def get_decay(df):
    """
    Use find_tau to calculate tau for a given dataframe.
    :param df: Dataframe. Assumed to have "time" and "angle" columns.
    :return: tau and tau_err.
    """
    t = df["time"]
    angle = df["angle"]
    angle_err = [1.0] * len(angle)
    return find_tau(t, angle, angle_err)


def get_multiple_taus(df_list):
    """
    From numerous dataframes, calculate tau for each one.
    :param df_list: List of dataframes. All are assumed to have "time" and "angle" columns.
    :return: A list of tau and a list of tau_err.
    """
    list_of_tau = []
    list_of_tau_err = []
    for df in df_list:
        temp, temp2 = get_decay(df)
        list_of_tau.append(temp)
        list_of_tau_err.append(temp2)
    return list_of_tau, list_of_tau_err


def plot_tau_vs_mass(df_list):
    # Calculate tau for each mass
    list_of_tau, list_of_tau_err = get_multiple_taus(df_list)
    list_mass = [50, 150, 200, 250]

    # Plot everything
    plot_data(list_mass, list_of_tau, list_of_tau_err, [0.2] * len(list_mass),
              "Mass (grams)", "Decay Constant (seconds)")


def plot_tau_vs_length(df_list):
    # Calculate tau for each length
    list_of_tau, list_of_tau_err = get_multiple_taus(df_list)
    list_length = [11, 16, 23, 32]

    # Plot everything
    plot_data(list_length, list_of_tau, list_of_tau_err, [0.2] * len(list_length),
              "Length (cm)", "Decay Constant (seconds)")


def get_period(df):
    # Find the cutoff for small angles
    for idx, value in df["angles"].iteritems():
        if value < 20:
            break
        df.drop(index=idx, inplace=True)

    # Calculate the average period
    periods = find_periods(df)
    avg_period = np.mean(periods)

    # Calculate uncertainty
    uncertainty = np.std(periods)/np.sqrt(len(periods))

    return avg_period, uncertainty


def get_multiple_periods(df_list):
    list_of_periods = []
    list_of_periods_err = []
    for df in df_list:
        period, unc = get_period(df)
        list_of_periods.append(period)
        list_of_periods_err.append(unc)
    return list_of_periods, list_of_periods_err


def plot_period_vs_mass(df_list):
    periods, periods_err = get_multiple_periods(df_list)
    plot_data(MASSES, periods, periods_err, [0.2] * len(periods),
              "Mass (grams)", "Period length (seconds)")


def plot_period_vs_length(df_list):
    periods, periods_err = get_multiple_periods(df_list)
    plot_data(LENGTHS, periods, periods_err, [0.5] * len(periods),
              "Length (cm)", "Period length (seconds)")


def main():
    # Define fonts
    font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 22}
    rc('font', **font)

    # Load csv files
    df_list = []
    for file in FILE_LIST:
        with open(file, "r") as f:
            df = pd.read_csv(f)
            df_list.append(df)

    # Plot data
    match PLOT_CHOICE:
        case 0:
            plot_period_vs_mass(df_list)
        case 1:
            plot_period_vs_length(df_list)
        case 2:
            plot_tau_vs_mass(df_list)
        case 3:
            plot_tau_vs_length()

if __name__ == "__main__":
    main()