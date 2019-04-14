import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import Ui_Menu
from sqlite3 import Error
from table import Ui_Dialog
import sys
from PrisonerRecords import PrisonerRecords
import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)





class Main:
	
	

	def __init__(self):

		#variables
		self.diag = 0


		print("constructor")
		app = QtWidgets.QApplication(sys.argv)
		menu = QtWidgets.QMainWindow()
		menu_ui = Ui_Menu()
		menu_ui.setupUi(menu)
		menu.show()
		menu_ui.pushButton.clicked.connect(self.prisonerRecords)
		sys.exit(app.exec_())	
	
	def prisonerRecords(self):
		pop = PrisonerRecords() #new window
		




		
if __name__ == "__main__":
	x = Main()







