from matplotlib import pyplot as plt
import pandas as pd
from python.files import ALL_FILES

"""
Plot a given dataset
Should be relatively simple. Exclusively for testing purposes.
"""

# Define global variables
FILE_ID = "length2"

def main():
    # Load data
    with open(ALL_FILES[FILE_ID], "r") as f:
        df = pd.read_csv(f)

    # Plot data
    plt.plot(df["time"], df["angle"], '.')
    plt.title(FILE_ID)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()