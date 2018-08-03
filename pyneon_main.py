#!/usr/bin/python

import sys
import os
import PySide2
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QInputDialog

qt_app = QApplication(sys.argv)


mineral_list = []
direc = 'nucleogenic/stopping_powers'
ext = '.txt'
txt_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ext]
for f in txt_files:
    name = f.split('.')[0]
    mineral_list.append(name)

class PyNeonLayout(QWidget):
    ''' An example of PySide/PyQt absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''

    def __init__(self):
        # Initialize the object as a QWidget and
        # set its title and minimum width
        QWidget.__init__(self)
        self.setWindowTitle('PyNeon')
        self.setMinimumWidth(800)

        # Create the QHBoxLayout that lays out the whole form
        self.layout = QHBoxLayout()
        self.layout.addStretch(1)

        # Create the QVBoxLayout that lays out the whole form
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(self.right_layout)

        # Create the form layout that manages the labeled controls
        self.left_form_layout = QFormLayout()
        self.right_form_layout = QFormLayout()

        # The minerals that we want to make available
        self.minerals = mineral_list

        # Create and fill the combo box to choose the mineral
        self.mineral = QComboBox(self)
        self.mineral.addItems(self.minerals)

        self.component1 = QComboBox(self)
        self.component1.addItems(['Cosmogenic','Nucleogenic','Air','Mantle','Solar Wind'])

        self.component2 = QComboBox(self)
        self.component2.addItems(['Cosmogenic', 'Nucleogenic', 'Air', 'Mantle', 'Solar Wind'])

        self.component3 = QComboBox(self)
        self.component3.addItems(['Cosmogenic', 'Nucleogenic', 'Air', 'Mantle', 'Solar Wind'])

        # Add it to the form layout with a label
        self.left_form_layout.addRow('Mineral:', self.mineral)
        self.right_form_layout.addRow('Component 1:', self.component1)
        self.right_form_layout.addRow('Component 2:', self.component2)
        self.right_form_layout.addRow('Component 3:', self.component3)

        # Create the entry control to specify a d18O
        # and set its placeholder text
        self.d18O = QLineEdit(self)
        self.d18O.setPlaceholderText("e.g. '+6' or '-2'")

        # Create the entry controls to specify signals
        # and set their placeholder text
        self.Ne20 = QLineEdit(self)
        self.Ne20.setPlaceholderText("e.g. 12000 or 1.00e-17")

        self.Ne21 = QLineEdit(self)
        self.Ne21.setPlaceholderText("e.g. 35.8 or 2.98e-20")

        self.Ne22 = QLineEdit(self)
        self.Ne22.setPlaceholderText("e.g. 1227 or 1.02e-18")

        # Add them to the form layout with a label
        self.left_form_layout.addRow('δ¹⁸O:', self.d18O)
        self.right_form_layout.addRow('²⁰Ne:', self.Ne20)
        self.right_form_layout.addRow('²¹Ne:', self.Ne21)
        self.right_form_layout.addRow('²²Ne:', self.Ne22)

        # Create and add the label to show the yield text
        self.yield_uranium238 = QLabel('', self)
        self.yield_uranium235 = QLabel('', self)
        self.yield_thorium232 = QLabel('', self)
        self.left_form_layout.addRow('Yield from ²³⁸U:', self.yield_uranium238)
        self.left_form_layout.addRow('Yield from ²³⁵U:', self.yield_uranium235)
        self.left_form_layout.addRow('Yield from ²³²Th:', self.yield_thorium232)

        # Add the form layout to the main VBox layout
        self.left_layout.addLayout(self.left_form_layout)
        self.right_layout.addLayout(self.right_form_layout)

        # Add stretch to separate the form layout from the button
        self.layout.addStretch(1)
        self.left_layout.addStretch(1)
        self.right_layout.addStretch(1)

        # Create a horizontal box layout to hold the button
        self.left_button_box = QHBoxLayout()
        self.right_button_box = QHBoxLayout()
        
        # Add stretch to push the button to the far right
        self.left_button_box.addStretch(1)
        self.right_button_box.addStretch(1)

        # Create the build button with its caption
        self.build_yield_button = QPushButton('Show yields', self)
        self.build_deconv_button = QPushButton('Deconvolve', self)

        # Add it to the button box
        self.left_button_box.addWidget(self.build_yield_button)
        self.right_button_box.addWidget(self.build_deconv_button)

        # Add the button box to the bottom of the main VBox layout
        self.left_layout.addLayout(self.left_button_box)
        self.right_layout.addLayout(self.right_button_box)

        # Set the VBox layout as the window's main layout
        self.setLayout(self.layout)

        self.build_yield_button.clicked.connect(self.click_yield)

    def click_yield(self):
        print('Clicked Yield Button.')
        

    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()


# Create an instance of the application window and run it
app = PyNeonLayout()
app.run()

print(app.Ne22.text())

# # Create the application object
# app = QApplication(sys.argv)
# window = QWidget()
#
# # Create a simple dialog box
# inputBox = QInputDialog()
# inputBox.
#
# msgBox = QMessageBox()
# msgBox.setText("Hello World - using PySide version " + PySide2.__version__)
# msgBox.exec_()
#
