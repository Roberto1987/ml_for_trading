import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
import pandas as p


def error(line,data):

    # line: tuple/list/array c0, c1, slope and y-intercept
    # data: 2d array of point (x,y)

    # err:  sum of squared differences , (Y' - Y)**2
    err = np.sum((data[:,1]- (line[0] * data[:,0] + line[1])) ** 2 )
    return  err


def test_run():
    l_orig = np.float32([4,2])
    print ('Original line: C0 = {}, C1 = {}'.format(l_orig[0], l_orig[1]))
    Xorig = np.linspace(0,10,21)
    Yorig = l_orig[0]*Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label ='Original line')

    # Generate noisy data points

    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig,Yorig + noise])
    plt.plot(data[:,0], data[:,1], 'go', label = 'Data points')

test_run()