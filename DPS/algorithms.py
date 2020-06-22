import numpy as np
from math import pi, sin
import scipy
from scipy import signal


def kronecker():
    length = 21
    x = np.arange(-length, length, 0.001);
    y = np.zeros(len(x))
    y[21000] = 1
    return x, y


def step():
    lenght = 21
    x = np.linspace(-lenght, lenght, lenght * 100 + 1)
    y = np.zeros(len(x))

    for i in range(len(x)):
        if x[i] == 0:
            y[i] = 0.5
        if x[i] > 0:
            y[i] = 1

    x2 = np.zeros(11)
    y2 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    return x, y, x2, y2


def rectangle(l):
    x = np.linspace(-1, 1, l, endpoint=False)
    y = np.zeros(len(x))
    x2 = [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5]
    x3 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    y2 = [0, 0.2, 0.4, 0.6, 0.8, 1]

    for i in range(len(x)):
        if abs(x[i]) == 0.5:
            y[i] = 0.5
        if abs(x[i]) < 0.5:
            y[i] = 1
    return x, y, x2, x3, y2


def triangle():
    x = np.linspace(0, 51, 51)
    y = scipy.signal.triang(51)
    return x, y


def exp_signal(a, x):
    y = [a**X for X in x]
    y = np.array(y)
    return y


def sinus(A, tp, tk, fp, f, phi):
    x = np.arange(tp, tk, 0.01)
    y = [A*sin(2*pi*f*t + phi) for t in x]
    y = np.array(y)
    return x, y


def aliasing():
    f = 256
    x = np.arange(0, 10, 1 / f)
    y1 = [sin(t) for t in x]
    y2 = [sin(5 * t) for t in x]

    x2 = [0, pi, 2 * pi, 3 * pi, pi / 2, 1.5 * pi, 2.5 * pi]
    y3 = [sin(t) for t in x2]
    return x, x2, y1, y2, y3
