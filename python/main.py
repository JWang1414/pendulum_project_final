from matplotlib import rc
from helper_functions import *
from fit_functions import *
from files import *

# Files names found in files.py
FILE_NAME = "left"
CURRENT_FILE = ALL_FILES[FILE_NAME]

# Define fit functions
FUNCTION_INDEX = 1
FIT_FUNCTIONS = [linear, quadratic, exponential, square_root]
CURRENT_FUNCTION = FIT_FUNCTIONS[FUNCTION_INDEX]

# Define figure settings
TITLE = FILE_NAME
FIGURE_SIZE = (8, 6)

# Plot settings
PERIOD_VS_ANGLE = True
DECAY_VS_ANGLE = False

if PERIOD_VS_ANGLE:
    TITLE += ", period"

elif DECAY_VS_ANGLE:
    TITLE += ", decay"

def plot_data(x, y, y_err, x_err, xlabel, ylabel):
    """
    Plots data with error bars, fits a curve to it, and plots the residuals.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :param x_err: Error on independent variable.
    :param xlabel: Label for x-axis.
    :param ylabel: Label for y-axis.
    :return: Nothing
    """
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex="all", figsize=FIGURE_SIZE)

    # Plot data with error bar
    ax1.errorbar(x, y, y_err, x_err, fmt="o")

    # Plot line of best fit
    popt = fit_data(ax1, CURRENT_FUNCTION, x, y, y_err)

    # Plot residuals
    plot_residuals(ax2, CURRENT_FUNCTION, popt, x, y, y_err)

    # Set plot settings
    fig_settings(fig, xlabel, ylabel)


def fig_settings(figure, xlabel, ylabel):
    """
    Default figure settings. Shows the figure.
    :param figure: Figure to adjust
    :param xlabel: Label for x-axis
    :param ylabel: Label for y-axis
    :return:
    """
    figure.suptitle(TITLE)
    figure.supxlabel(xlabel)
    figure.supylabel(ylabel)
    figure.tight_layout()
    figure.show()


def plot_period_vs_angle(df):
    # Define variables
    periods, periods_err = average_periods(df)
    angles = every_nth_angle(df, 10)
    angles_err = [2.0] * len(angles)

    # Clean data
    outlier_management(angles, periods, periods_err, angles_err)

    # Plot everything
    print(periods_err)
    plot_data(angles, periods, periods_err, angles_err,
              "Initial Angle (degrees)", "Period (seconds)")


def plot_tau_vs_angle(df):
    # Define variables
    tau, tau_err = tau_list(df, 10)
    angles = every_nth_angle(df, 10)
    angles = angles[:len(tau)]
    angles_err = [2.0] * len(angles)

    # Clean data
    control_uncertainties(tau_err, 0.1)

    # Plot everything
    plot_data(angles, tau, tau_err, angles_err,
              "Initial Angle (degrees)", "Decay Constant (seconds)")


def main():
    # Define fonts
    font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 22}
    rc('font', **font)

    # Load csv file
    with open(CURRENT_FILE, "r") as f:
        df = pd.read_csv(f)

    # Plot data
    if PERIOD_VS_ANGLE:
        plot_period_vs_angle(df)
    if DECAY_VS_ANGLE:
        plot_tau_vs_angle(df)

if __name__ == "__main__":
    main()