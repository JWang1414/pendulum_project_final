from matplotlib import pyplot as plt, rc
import pandas as pd
from numpy.core.function_base import linspace

from python.files import ALL_FILES
from python.fit_functions import fit_curve, decay_function

"""
Plot a given dataset
Should be relatively simple. Exclusively for testing purposes.
"""

# Define global variables
FILE_ID = "right"

def main():
    # Define fonts
    font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 22}
    rc('font', **font)

    # Load data
    with open(ALL_FILES[FILE_ID], "r") as f:
        df = pd.read_csv(f)

    # Compress variables
    time = df["time"]
    angle = df["angle"]

    # Plot exponential decay
    popt, pcov = fit_curve(decay_function, time, angle, [3.0] * len(angle),
                           [angle[0], 10, 0], True)

    # Calculate line of best fit
    x_bf = linspace(min(time), max(time), 100)
    y_bf = decay_function(x_bf, *popt)

    # Plot data
    plt.plot(time, angle, '.')
    plt.plot(x_bf, y_bf)
    plt.suptitle(FILE_ID)
    plt.xlabel("time (seconds)")
    plt.ylabel("amplitude (degrees)")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()