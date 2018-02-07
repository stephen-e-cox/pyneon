#!/usr/bin/python

import sys

import PySide2
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMessageBox

# Create the application object
app = QApplication(sys.argv)

# Create a simple dialog box
msgBox = QMessageBox()
msgBox.setText("Hello World - using PySide version " + PySide2.__version__)
msgBox.exec_()