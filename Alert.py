
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


from Alert_UI import Ui_Dialog
import sys

import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Alert:
	def __init__(self,message):


		self.diag = QtWidgets.QDialog()
		self.table_ui = Ui_Dialog()
		self.table_ui.setupUi(self.diag)
		self.table_ui.label.setText(message)

		self.diag.exec_()

	
