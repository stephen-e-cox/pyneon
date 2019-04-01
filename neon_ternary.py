import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
import ternary
import numpy as np


def plot_tern(data_point):

    # Scatter Plot
    scale = 100
    figure, tax = ternary.figure(scale=scale)
    figure.set_size_inches(10, 10)
    tax.set_title("Neon Isotopes", fontsize=20)
    tax.boundary(linewidth=2.0)
    tax.gridlines(multiple=10, color="black")

    tax.left_axis_label("Neon-22", offset=0.1)
    tax.right_axis_label("Neon-21", offset=0.1)
    tax.bottom_axis_label("Neon-20", offset=-0.05)

    # Air
    points = []
    points.append([90.48, 00.27, 09.25])
    tax.scatter(points, marker='s', color='red', label="Air")

    # Cosmogenic (Quartz; Schaefer et al. 1999)
    points = []
    points.append([35.59, 28.47, 35.94])

    tax.scatter(points, marker='s', color='green', label="Cosmogenic (Quartz)")

    # Cosmogenic (Pyroxene; Schaefer et al. 1999)
    points = []
    points.append([29.67, 32.64, 37.69])
    tax.scatter(points, marker='s', color='blue', label="Cosmogenic (Pyroxene)")

    # Mantle
    points = []
    points.append([92.80, 00.47, 06.73])
    tax.scatter(points, marker='s', color='purple', label="Mantle")

    # Nucleogenic (Bulk Crustal)
    points = []
    points.append([08.39, 89.73, 01.88])
    tax.scatter(points, marker='s', color='grey', label="Nucleogenic (Bulk Crust)")

    points = []
    points.append(data_point)
    points.append([84.79769871, 2.695266087, 12.50703521])
    points.append([89.37663091, 0.376920847, 10.24644825])
    points.append([83.08293978, 3.729719571, 13.18734065])
    points.append([89.44536548, 0.354278712, 10.20035581])
    points.append([80.96525495, 4.904465607, 14.13027944])
    points.append([89.69828162, 0.355471802, 9.946246576])
    points.append([73.35719139, 8.5538114, 18.08899721])
    points.append([88.97094597, 0.457847705, 10.57120633])
    points.append([79.32092083, 5.552525018, 15.12655415])
    tax.scatter(points, marker='s', color='black', label="Data")

    tax.legend()
    tax.ticks(axis='lbr', multiple=10, linewidth=1, offset=0.012)
    tax.clear_matplotlib_ticks()

    tax.show()
