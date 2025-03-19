import matplotlib.pyplot as plt
from matplotlib import rc
from helper_functions import *
from os import getcwd

# Reformatting this so that PyCharm can autocomplete the file name
FILE = "data_clean/symmetry_left_clean.csv"
FILE_PATH = getcwd() + "/" + FILE

def plot_periods(df):
    # Define variables
    periods, periods_err = average_periods(df)
    angles = every_nth_angle(df, 10)
    angles_err = [0.2] * len(angles)

    # Plot data with error bars
    plt.errorbar(angles, periods, periods_err, angles_err, fmt="o")

    # Set plot settings
    plt.xlabel("Angle (degrees)")
    plt.ylabel("Period (seconds)")
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
    plot_periods(df)

if __name__ == "__main__":
    main()