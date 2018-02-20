import PySide2
from matplotlib.pyplot import figure, plot, show
from matplotlib.figure import Figure
import matplotlib
# matplotlib.use('Qt5Agg')
# matplotlib.rcParams['backend.qt5'] = 'PySide2'

from nucleogenic.neon_yield import yieldcalc
from nucleogenic.cross_section import xsection_plot
from nucleogenic.stopping_power import stopping_plot

class YieldFigure(Figure):
    def __init__(self, *args, **kwargs):

        figtitle = kwargs.pop('figtitle', 'testfigure')
        Figure.__init__(self, *args, **kwargs)
        self.text(0.5, 0.95, figtitle, ha='center')

#
target = 'Zircon'
yieldinstance, min_energy, max_energy = yieldcalc(target, 'O18', 0.3491, 0.002012405, 15.9994)
#
titlevar = 'Yield for '
titlevar += target
fig = figure(FigureClass=YieldFigure, figtitle=titlevar)
ax = fig.add_subplot(111)
ax.set_xlabel('Alpha Energy (MeV)')
ax.set_ylabel('Yield (²¹Ne/⁴He)')
ax.plot(yieldinstance.index, yieldinstance)
show()


#yieldplot = xsection_plot('O18')
#
# stoppingplot = stopping_plot('Zircon', min_energy, max_energy)
