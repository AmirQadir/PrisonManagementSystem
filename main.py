import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import menu
from login_ui import Ui_Login_Ui
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
		self.ref = 0

		
		app = QtWidgets.QApplication(sys.argv)
		self.login = QtWidgets.QMainWindow()
		login_ui = Ui_Login_Ui()
		login_ui.setupUi(self.login)
		self.login.show()
		login_ui.pushButton.clicked.connect(self.loginNow)
		sys.exit(app.exec_())	
	
	def prisonerRecords(self):
		#pop = PrisonerRecords() #new window
		pass

	def loginNow(self):
		#pop = PrisonerRecords()
		self.login.hide()
		self.ref = menu()
		self.ref.show()
		print("hello")
		



		
if __name__ == "__main__":
	x = Main()







