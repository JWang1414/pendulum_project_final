import matplotlib.pyplot as plt
from matplotlib import rc
from helper_functions import *
from fit_functions import *
from os import getcwd

# Reformatting this so that PyCharm can autocomplete the file name
FILE = "data_clean/250grams_clean.csv"
FILE_PATH = getcwd() + "/" + FILE

FUNCTION_INDEX = 0
FIT_FUNCTIONS = [linear, quadratic, exponential]
CURRENT_FUNCTION = FIT_FUNCTIONS[FUNCTION_INDEX]


def plot_periods(df):
    # Define variables
    periods, periods_err = average_periods(df)
    angles = every_nth_angle(df, 10)
    angles_err = [1.0] * len(angles)

    # Clean data
    outlier_management(angles, periods, periods_err, angles_err)

    # Plot data with error bars
    plt.errorbar(angles, periods, periods_err, angles_err, fmt="o")

    # Plot line of best fit
    fit_data(CURRENT_FUNCTION, angles, periods, periods_err)

    # Set plot settings
    plt.xlabel("Initial Angle (degrees)")
    plt.ylabel("Period (seconds)")
    plt.tight_layout()
    plt.show()


def plot_tau(df):
    # Define variables
    tau, tau_err = tau_list(df, 10)
    angles = every_nth_angle(df, 10)
    angles = angles[:len(tau)]
    angles_err = [1.0] * len(angles)

    # Plot data with error bar
    plt.errorbar(angles, tau, tau_err, angles_err, fmt="o")

    # Plot line of best fit
    fit_data(CURRENT_FUNCTION, angles, tau, tau_err)

    # Set plot settings
    plt.xlabel("Initial Angle (degrees)")
    plt.ylabel("Time constant (seconds)")
    plt.tight_layout()
    plt.show()


def main():
    # Define fonts
    font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 22}
    rc('font', **font)

    # Load csv file
    with open(FILE_PATH, "r") as f:
        df = pd.read_csv(f)

    # Plot data
    # plot_periods(df)
    plot_tau(df)

if __name__ == "__main__":
    main()