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
		self.conn = sqlite3.connect('prison.db')
		
		app = QtWidgets.QApplication(sys.argv)
		self.login = QtWidgets.QMainWindow()
		self.login_ui = Ui_Login_Ui()
		self.login_ui.setupUi(self.login)
		self.login.show()
		self.login_ui.pushButton.clicked.connect(self.loginNow)

		#for quick testing login. delete later
		self.login_ui.lineEdit.setText("nabeel")
		self.login_ui.lineEdit_2.setText("12345")
		#end

		sys.exit(app.exec_())	
	


	def loginNow(self):
		username = self.login_ui.lineEdit.text()
		password = self.login_ui.lineEdit_2.text()

		#print("details: " , username , password)

		cur = self.conn.cursor()
		cur.execute("SELECT password,access_level from login where username = ?", (username,) )

		rows = cur.fetchall()

		if(len(rows) == 0):
			print("incorrect username")
		else:
			password_db = rows[0][0]

			access_level = rows[0][1]

			if(password == password_db):
				self.login.hide()


				#depending on access level correct window open krni hai
				self.ref = menu(username,access_level) #send username as well (for password changing)
				self.ref.show()
			else:
				print("incorrect password")



		#print(rows[0][0]) 
		#first result ka first element (which is required password cause query only returns one result and only one coloumn)

						


		



		
if __name__ == "__main__":
	x = Main()







