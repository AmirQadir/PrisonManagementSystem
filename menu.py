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
	def __init__(self,user):
		self.conn = sqlite3.connect('prison.db')
		self.username = user

		self.Menu = QtWidgets.QMainWindow()
		self.ui = Ui_Menu()
		self.ui.setupUi(self.Menu)
		self.ui.pushButton.clicked.connect(self.PrisRecords)
		self.ui.pushButton_7.clicked.connect(self.updatePass)
		self.ui.pushButton_4.clicked.connect(self.logout)
		self.ui.label_4.setText(self.username)

	def logout(self):
		print("logout")
		self.Menu.close()

	def show(self):
		self.Menu.show();

	def PrisRecords(self):

		#read text boxes and do stuff
		print(self.username)
		pop = PrisonerRecords()

	
	def updatePass(self):
		if self.username == "admin":
			print("Cant change admin/admin password.")
			return

		newPass = self.ui.textEdit.toPlainText()


		rr = []

		rr.append(newPass)
		rr.append(self.username)
		
		cur = self.conn.cursor()
		cur.execute("Update login Set password=? where username=?",rr)
		self.conn.commit()
		
		print("updated: " , newPass)

			