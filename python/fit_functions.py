import numpy as np

def linear(x, m, b):
    """
    Linear function.
    :param x: Independent variable.
    :param m: Slope.
    :param b: y-intercept.
    :return: Dependent variable.
    """
    # Convert values to numpy array
    m = np.array(m)

    return m * x + b