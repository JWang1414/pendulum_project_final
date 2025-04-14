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


def decay_function(x, a, b, c):
    a = np.array(a)
    b = np.array(b)

    return a * np.exp(-x / b) + c


# noinspection PyTupleAssignmentBalance
def fit_curve(function, x, y, y_err, init=None, out=True):
    """
    Use scipy.optimize.curve_fit to fit a curve to data.
    :param function: The function used to fit values.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :param init: Initial values for the fit. (Optional)
    :param out: Whether to print output. By default, True.
    :return: Optimized values and uncertainties.
    """
    popt, pcov = curve_fit(function, x, y,
                           sigma=y_err, absolute_sigma=True,
                           p0=init)

    pcov = np.sqrt(np.diag(pcov))
    if out:
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


def fit_data(figure: plt.Axes, function, x, y, y_err):
    """
    Fit a line of best fit, and plot it on top of the data.
    Goodness of fit is printed.
    :param figure: The figure to plot on.
    :param function: Function used to fit data.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :return: Optimized fit values.
    """
    # Fit curve
    popt, _ = fit_curve(function, x, y, y_err)

    # Determine goodness of fit
    print_goodness_of_fit(function, popt, x, y, y_err)

    # Plot line of best fit
    x_bf = np.linspace(min(x), max(x), 1000)
    y_bf = function(x_bf, *popt)
    figure.plot(x_bf, y_bf)

    return popt


def plot_residuals(figure: plt.Axes, function, popt, x, y, y_err):
    """
    Plots the residuals of the fit.
    :param figure: Figure to plot on.
    :param function: Optimal fit function.
    :param popt: Optimized fit values.
    :param x: Independent variable.
    :param y: Dependent variable.
    :param y_err: Error on dependent variable.
    :return: Nothing
    """
    y_bf = function(x, *popt)
    residuals = y - y_bf
    figure.errorbar(x, residuals, y_err, fmt="o")
    figure.axhline(0, color="red", linestyle="--")


def find_tau(t, theta, theta_err):
    """
    Uses curve_fit to find the decay constant.
    :param t: Time
    :param theta: Angle / amplitude
    :param theta_err: Error on theta
    :return: Tau and its uncertainty
    """
    popt, pcov = fit_curve(decay_function, t, theta, theta_err,
                           [theta[0], 10, 0], False)
    return popt[1], pcov[1]


def tau_list(df, n):
    """
    Creates a list of decay constants for each initial angle, from one large dataframe.
    :param df: Dataframe, assumed to have columns "time" and "angle"
    :param n: Jump between tau calculations
    :return: Two lists. One of the tau values, the other of the uncertainties.
    """
    # Define variables
    time = df["time"].tolist()
    amp = df["angle"].tolist()
    amp_err = [1.0] * len(amp)

    # Calculate tau for numerous initial angles
    result = []
    uncertainties = []
    length = len(time) - 100
    for i in range(0, length, n):
        temp1, temp2 = find_tau(time[i:], amp[i:], amp_err[i:])
        result.append(temp1)
        uncertainties.append(temp2)

    return result, uncertainties