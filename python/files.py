from os import getcwd

CURRENT_DIR = getcwd() + "/"
DATA_DIR = CURRENT_DIR + "data_clean/"

ALL_FILES = {
    "11_cm": DATA_DIR + "11cm_clean.csv",
    "16_cm": DATA_DIR + "16cm_clean.csv",
    "23_cm": DATA_DIR + "23cm_clean.csv",
    "32_cm": DATA_DIR + "32cm_clean.csv",
    "50_grams": DATA_DIR + "50grams_clean.csv",
    "150_grams": DATA_DIR + "150grams_clean.csv",
    "200_grams": DATA_DIR + "200grams_clean.csv",
    "250_grams": DATA_DIR + "250grams_clean.csv",
    "left": DATA_DIR + "symmetry_left_clean.csv",
    "right": DATA_DIR + "symmetry_right_clean.csv"
}

LENGTH_FILES = [
    ALL_FILES["11_cm"],
    ALL_FILES["16_cm"],
    ALL_FILES["23_cm"],
    ALL_FILES["32_cm"]
]

MASS_FILES = [
    ALL_FILES["50_grams"],
    ALL_FILES["150_grams"],
    ALL_FILES["200_grams"],
    ALL_FILES["250_grams"]
]