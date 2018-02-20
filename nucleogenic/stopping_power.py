import os
import pandas as pd
import numpy as np
from matplotlib.pyplot import figure, plot, show
from matplotlib.figure import Figure
from scipy import interpolate as interp

direc = 'stopping_powers'
ext = '.txt'

txt_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ext]

stopping = {}
stopping_data = {}

for f in txt_files:
    name = f.split('.')[0]
    df = pd.read_csv(os.path.join(direc, f), header=None)
    df.columns = ['Energy', 'StoppingPower']
    stopping[name] = df.set_index('Energy').squeeze()
    stopping_data[name] = stopping[name]

class YieldFigure(Figure):
    def __init__(self, *args, **kwargs):

        figtitle = kwargs.pop('figtitle', 'testfigure')
        Figure.__init__(self, *args, **kwargs)
        self.text(0.5, 0.95, figtitle, ha='center')


def stopping_power_func(target, min_energy, max_energy):

    for name in stopping:
        x_alpha_interps = np.linspace(min_energy, max_energy, num=100, endpoint=True)
        for i in x_alpha_interps:
            if not i in stopping[name].index:
                stopping[name].loc[i] = np.nan

        stopping[name] = stopping[name].sort_index().interpolate(method='index')

    return stopping_data[name], x_alpha_interps, stopping[target]


def stopping_plot(target, min_energy, max_energy):
    stopping_data[name], x_alpha_interps, stopping[target] = stopping_power_func(target, min_energy, max_energy)
    titlevar = 'Stopping Power for '
    titlevar += target
    fig = figure(FigureClass=YieldFigure, figtitle=titlevar)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Alpha Energy (MeV)')
    ax.set_ylabel('Stopping Power (MeV/(mg/cm²))')
    ax.plot(stopping_data[target].index, stopping_data[target], 'o')
    ax.plot(stopping[target].index, stopping[target])
    show()
    return fig
