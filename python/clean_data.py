import pandas as pd
from scipy.signal import find_peaks
from os import getcwd

# Define the input and output files
INPUT = getcwd() + "/data/symmetry_left.csv"
OUTPUT = getcwd() + "/data_clean/symmetry_left_clean.csv"

# Important note: The above file structure is defined for my project
# structure on a Linux Ubuntu system.
# If you're on another OS, you're on your own.

def clean_data(df):
    """
    Clean pendulum data by extracting all the peaks
    :param df: Dataframe with data. Assumed to have "angle" column.
    :return: A copy of the initial dataframe with just the peaks.
    """
    # Load data into 1D array
    angles = df["angle"]

    # Find peaks
    peaks = find_peaks(angles, distance=3)[0]

    # Create a new dataframe with just peaks
    peaks_df = df.iloc[peaks]

    return peaks_df

def double_clean(df):
    """
    Clean the pendulum data for both sides. That is, find
    the peaks on the left side and the right side.
    :param df: Dataframe with data. Assumed to have "angle" column.
    :return: Two copies of the initial dataframe with just the peaks. Both sides.
    """
    # Clean the data set for positive values
    clean1 = clean_data(df)

    # Make a new dataframe with flipped angles
    new_df = df.copy()
    new_df["angle"] = -new_df["angle"]

    # Clean the dataset for negative values
    clean2 = clean_data(new_df)

    return clean1, clean2

def main():
    # Load data
    with open(INPUT, "r") as f:
        df = pd.read_csv(f)

    # Pass into cleaning function
    # Optionally use double_clean to clean for both sides
    clean_df = clean_data(df)

    # Create new .csv files with clean data
    clean_df.to_csv(OUTPUT, index=False)

if __name__ == "__main__":
    main()