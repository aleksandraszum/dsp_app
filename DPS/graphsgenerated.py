import os

import matplotlib.pyplot as plt
import numpy as np
from .algorithms import kronecker, step, rectangle, triangle, exp_signal, sinus, aliasing


def kronecker_graphs():
    x, y = kronecker()
    kronecker_graphs_c = save_fig(1, x, y, 'kronecker_c.svg')
    kronecker_graphs_d = save_fig(2, x[20990:21010], y[20990:21010], 'kronecker_d.svg')
    return kronecker_graphs_c, kronecker_graphs_d


def step_graphs():
    x, y, x2, y2 = step()
    plt.figure(frameon=False)
    plt.plot(x[0:1049], y[0:1049], 'b', x[1050], y[1050], 'bo', x[1051::], y[1051::], 'b', x2, y2, 'b--')
    step_graphs_c = 'step_c.svg'
    plt.savefig(os.path.join(os.path.dirname(__file__), 'static', step_graphs_c))
    plt.close()

    plt.figure(frameon=False)
    plt.plot(x[1030:1070], y[1030:1070], 'bo')
    step_graphs_d = 'step_d.svg'
    plt.savefig(os.path.join(os.path.dirname(__file__), 'static', step_graphs_d))
    plt.close()
    return step_graphs_c, step_graphs_d


def rectangle_graphs():
    x, y, x2, x3, y2 = rectangle(l=1000)
    plt.figure(frameon=False)
    plt.plot(x[0:249], y[0:249], 'b', x[250], y[250], 'bo', x[750], y[750], 'bo', x[251:749], y[251:749], 'b', x[751::],
             y[751::], 'b', x2, y2, 'b--', x3, y2, 'b--')
    rectangle_graphs_c = 'rectangle_c.svg'
    plt.savefig(os.path.join(os.path.dirname(__file__), 'static', rectangle_graphs_c))
    plt.close()

    x, y, x2, x3, y2 = rectangle(l=100)
    plt.figure(frameon=False)
    plt.plot(x, y, 'b.')
    rectangle_graphs_d = 'rectangle_d.svg'
    plt.savefig(os.path.join(os.path.dirname(__file__), 'static', rectangle_graphs_d))
    plt.close()
    return rectangle_graphs_c, rectangle_graphs_d


def triangle_graphs():
    x, y = triangle()
    triangle_graphs_c= save_fig(1, x, y, 'triangle_c.svg')
    triangle_graphs_d = save_fig(2, x, y, 'triangle_d.svg')
    return triangle_graphs_c, triangle_graphs_d


def exp_graphs():
    x1 = np.arange(0, 20, 1 / 256)
    y1 = exp_signal(2, x1)
    x2 = np.arange(0, 20, 1)
    y2 = exp_signal(2, x2)
    exp_graphs_c = save_fig(1, x1, y1, 'exp_c.svg')
    exp_graphs_d = save_fig(2, x2, y2, 'exp_d.svg')
    return exp_graphs_c, exp_graphs_d


def sinusoidal_graphs():
    x, y = sinus(1, 0, 1, 256, 5, 0)
    sinusoidal_graphs_c = save_fig(1, x, y, 'sinusoidal_c.svg')
    sinusoidal_graphs_d = save_fig(2, x, y, 'sinusoidal_d.svg')
    return sinusoidal_graphs_c, sinusoidal_graphs_d


def aliasing_graphs():
    x1, x2, y1, y2, y3 = aliasing()
    plt.figure(frameon=False)
    plt.plot(x1, y1, '--', x1, y2, '--', x2, y3, 'o')
    aliasing_svg = 'aliasing_svg.svg'
    plt.savefig(os.path.join(os.path.dirname(__file__), 'static', aliasing_svg))
    plt.close()
    return aliasing_svg


def save_fig(typ, x, y, name):
    if typ == 1:
        plt.figure(frameon=False)
        plt.plot(x, y)
        plt.savefig(os.path.join(os.path.dirname(__file__), 'static', name))
        plt.close()

    else:
        plt.figure(frameon=False)
        plt.plot(x, y, 'o')
        plt.savefig(os.path.join(os.path.dirname(__file__), 'static', name))
        plt.close()

    return name
