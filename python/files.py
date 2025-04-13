from os import getcwd

CURRENT_DIR = getcwd() + "/"
DATA_DIR = CURRENT_DIR + "data_clean/"

ALL_FILES = {
    "50g": DATA_DIR + "50g_clean.csv",
    "100g": DATA_DIR + "100g_clean.csv",
    "200g": DATA_DIR + "200g_clean.csv",
    "300g": DATA_DIR + "300g_clean.csv",
    "500g": DATA_DIR + "500g_clean.csv",
    "length1": DATA_DIR + "length1_clean.csv",
    "length2": DATA_DIR + "length2_clean.csv",
    "length3": DATA_DIR + "length3_clean.csv",
    "length4": DATA_DIR + "length4_clean.csv",
    "length5": DATA_DIR + "length5_clean.csv",
    "length6": DATA_DIR + "length6_clean.csv",
    "left": DATA_DIR + "symmetry_left_clean.csv",
    "right": DATA_DIR + "symmetry_right_clean.csv"
}

LENGTH_FILES = [
    ALL_FILES["length1"],
    ALL_FILES["length2"],
    ALL_FILES["length3"],
    ALL_FILES["length4"],
    ALL_FILES["length5"],
    ALL_FILES["length6"]
]

MASS_FILES = [
    ALL_FILES["50g"],
    ALL_FILES["100g"],
    ALL_FILES["200g"],
    ALL_FILES["300g"],
    ALL_FILES["500g"]
]