import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
import pandas as p


def error(line, data):
    # Compute error between given line model and observed data

    # PARAMETERS
    # line: tuple/list/array c0, c1, slope and y-intercept
    # data: 2d array of point (x,y)
    # RETURNS error, as scalar

    # METRIC: Sm of squared Y-axis differences
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err


def test_run():
    # Define original line

    l_orig = np.float32([4, 2])
    print('Original line: C0 = {}, C1 = {}'.format(l_orig[0], l_orig[1]))
    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label='Original line')

    # Generate noisy data points

    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label='Data points')

    # Try to fit a line to this data
    l_fit = fit_line(data, error)
    print("Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1]))
    plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0)


def fit_line(data, error_func):
    # generate initial guess for line model
    l = np.float32([0, np.mean(data[:, 1])])  # slope = 0, intercept = mean

    # Plot initial guess (optional)
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label='Initial Guess')

    # Call optimizer to minimize error function
    result = opt.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp': True})
    return result.x


test_run()
plt.show()
