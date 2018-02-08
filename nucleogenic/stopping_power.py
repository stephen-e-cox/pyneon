import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate as interp

direc = 'stopping_powers'
ext = '.txt'

txt_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ext]

stopping = {}

for f in txt_files:
    name = f.split('.')[0]
    df = pd.read_csv(os.path.join(direc, f), header=None)
    df.columns = ['Energy', 'StoppingPower']
    stopping[name] = df.set_index('Energy').squeeze()

def stoppingpower(target,min_energy,max_energy):

    for name in stopping:
        x_alpha_interps = np.linspace(min_energy, max_energy, num=100, endpoint=True)
        for i in x_alpha_interps:
            if not i in stopping[name].index:
                stopping[name].loc[i] = np.nan

        stopping[name] = stopping[name].sort_index().interpolate(method='index')

    return stopping[target]


