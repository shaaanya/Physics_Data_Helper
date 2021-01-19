import matplotlib.pyplot as plt
import os

def plot_f(x, y, draw_data, function, name, road='./pictures'):
    fig = plt.figure()
    plt.plot(x, y)
    plt.plot(draw_data[0], draw_data[1])

    plt.ylabel(function)
    save(road, name, fmt='png')


def save(road , name='', fmt='png'):
    pwd = os.getcwd()
    road = road + '{}'.format(fmt)
    iPath = road
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
    plt.close()
