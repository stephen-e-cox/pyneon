import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
import ternary
import numpy as np

# Scatter Plot
scale = 100
figure, tax = ternary.figure(scale=scale)
figure.set_size_inches(10, 10)
tax.set_title("Argon Isotopes", fontsize=20)
tax.boundary(linewidth=2.0)
tax.gridlines(multiple=10, color="black")

tax.left_axis_label("Argon-36", offset=0.1)
tax.right_axis_label("Argon-38", offset=0.1)
tax.bottom_axis_label("Argon-40", offset=-0.05)

# Air
points = []
points.append([99.6035, 0.0629, 0.3336])
tax.scatter(points, marker='s', color='red', label="Air")

# Radiogenic (All 40Ar)
points = []
points.append([100, 0, 0])

tax.scatter(points, marker='s', color='grey', label="Radiogenic")

# Cosmogenic (Young Ca) 38/36 from Renne, Farley, at al. 2001, 40/36 from Kaiser and Zahringer 1968
points = []
points.append([7.14, 69.04, 23.81])
tax.scatter(points, marker='s', color='blue', label="Cosmogenic (Young from Ca)")

# Cosmogenic (Old Ca) 38/36 from Renne, Farley, at al. 2001, 40/36 from Kaiser and Zahringer 1968
points = []
points.append([11.11, 51.85, 37.04])
tax.scatter(points, marker='s', color='green', label="Cosmogenic (Old from Ca)")


tax.legend()
tax.ticks(axis='lbr', multiple=10, linewidth=1, offset=0.012)
tax.clear_matplotlib_ticks()

tax.show()