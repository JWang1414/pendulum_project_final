from matplotlib import rc
from helper_functions import *
from fit_functions import *
from main import plot_data
from files import *

# Define the file list here. Fit function must be defined in main.py
FILE_LIST = LENGTH_FILES


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
    # plot_tau_vs_mass(df_list)
    plot_tau_vs_length(df_list)

if __name__ == "__main__":
    main()