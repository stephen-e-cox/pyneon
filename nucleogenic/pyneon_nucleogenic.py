import PySide2
import matplotlib
# matplotlib.use('Qt5Agg')
# matplotlib.rcParams['backend.qt5'] = 'PySide2'

from neon_yield import yieldcalc
from cross_section import xsection_plot



#
#
yieldinstance = yieldcalc('Aragonite', 'O18', 0.4795, 0.002012405, 15.9994)
#
yieldplot = xsection_plot('O18')
#
