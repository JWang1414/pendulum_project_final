import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chi2


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


def quadratic(x, a, b, c):
    """
    Quadratic function.
    :param x: Independent variable.
    :param a: Multiplication factor.
    :param b: x-displacement.
    :param c: y-displacement.
    :return: Dependent variable.
    """
    a = np.array(a)

    return a * (x - b)**2 + c


def exponential(x, a, b, c, d):
    """
    Exponential function.
    :param x: Independent variable.
    :param a: Multiplication factor. (In front)
    :param b: Multiplication factor. (In exponent)
    :param c: x-displacement.
    :param d: y-displacement.
    :return: Dependent variable.
    """
    a = np.array(a)
    b = np.array(b)

    first = np.exp(b * (x - c))
    return a * first + d


# noinspection PyTupleAssignmentBalance
def fit_curve(function, x, y, y_err):
    """
    Use scipy.optimize.curve_fit to fit a curve to data.
    :param function: The function used to fit values.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :return: Optimized values and uncertainties.
    """
    popt, pcov = curve_fit(function, x, y,
                           sigma=y_err, absolute_sigma=True)

    pcov = np.sqrt(np.diag(pcov))
    print(f"Optimized values: {popt}\nUncertainties: {pcov}")

    return popt, pcov


def print_goodness_of_fit(function, popt, x, y, y_err):
    """
    Calculate and print goodness of fit.
    :param function: function used to fit data.
    :param popt: Optimized values.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :return: Nothing
    """
    # Calculate values
    chi_squared_fit = function(x, *popt)
    chi_squared = np.sum(((y - chi_squared_fit) /
                          y_err) ** 2)
    dof = len(x) - len(popt)

    # Print values
    print(f"Chi-squared: {chi_squared}")
    print(f"Degrees of Freedom: {dof}")
    print(f"Chi-squared probability: {1 - chi2.cdf(chi_squared, dof)}")


def fit_data(function, x, y, y_err):
    """
    Fit a line of best fit, and plot it on top of the data.
    Goodness of fit is printed.
    :param function: Function used to fit data.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :return: Nothing
    """
    # Fit curve
    popt, _ = fit_curve(function, x, y, y_err)

    # Determine goodness of fit
    print_goodness_of_fit(function, popt, x, y, y_err)

    # Plot line of best fit
    x_bf = np.linspace(x[0], x[-1], 1000)
    y_bf = function(x_bf, *popt)
    plt.plot(x_bf, y_bf)
