import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu_ui import Ui_Menu
from sqlite3 import Error
from table import Ui_Dialog
from login_ui import Ui_Login_Ui
import sys
from AddRecords import AddRecords
from PrisonerRecords import PrisonerRecords
import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class menu:
	def __init__(self):
		self.conn = sqlite3.connect('prison.db')
		

		self.Menu = QtWidgets.QMainWindow()
		ui = Ui_Menu()
		ui.setupUi(self.Menu)
		ui.pushButton.clicked.connect(self.showPris)

	def show(self):
		self.Menu.show();

	def showPris(self):
		pop = PrisonerRecords()
		

			