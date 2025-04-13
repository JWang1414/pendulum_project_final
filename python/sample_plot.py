from matplotlib import pyplot as plt
import pandas as pd
from numpy.core.function_base import linspace

from python.files import ALL_FILES
from python.fit_functions import find_tau, fit_curve, decay_function

"""
Plot a given dataset
Should be relatively simple. Exclusively for testing purposes.
"""

# Define global variables
FILE_ID = "50g"

def main():
    # Load data
    with open(ALL_FILES[FILE_ID], "r") as f:
        df = pd.read_csv(f)

    # Compress variables
    time = df["time"]
    angle = df["angle"]

    # Plot exponential decay
    popt, pcov = fit_curve(decay_function, time, angle, [3.0] * len(angle),
                           [angle[0], 10, 0], False)

    x_bf = linspace(min(time), max(time), 100)
    y_bf = decay_function(x_bf, *popt)

    # Plot data
    plt.plot(time, angle, '.')
    plt.plot(x_bf, y_bf)
    plt.title(FILE_ID)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()