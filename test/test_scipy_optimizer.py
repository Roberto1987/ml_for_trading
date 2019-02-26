import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
import pandas as p


def f(X):
    Y = (X - 1.5)**2 + 0.5
    print('X = {}, Y = {}'.format(X, Y))
    return Y


def test_run():
    Xguess = 0.0
    min_result = opt.minimize(f, Xguess, method='SLSQP', options={'disp': True})
    print("Minima found at:")
    print('X = {}, Y = {}'.format(min_result.x, min_result.fun))

    # Plot function values, mark minima
    Xplot = np.linspace(0.5, 2.5, 21)
    Yplot = f(Xplot)
    plt.plot(Xplot,Yplot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title('Minima of an objective function')
    plt.show()


def error(line,data):

    # line: tuple/list/array c0, c1, slope and y-intercept
    # data: 2d array of point (x,y)

    # err:  sum of squared differences , (Y' - Y)**2
    err = np.sum((data[:,1]- (line[0] * data[:,0] + line[1])) ** 2 )
    return  err


test_run()
