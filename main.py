import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from login_ui import Ui_Login_Ui
from sqlite3 import Error
from table import Ui_Dialog
import sys
import PyQt5
from menu import menu
from PrisonerRecords import PrisonerRecords
import hashing

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)





class Main:
	
	

	def __init__(self):

		#variables
		self.ref = 0
		self.conn = sqlite3.connect('se_db.db')		
		app = QtWidgets.QApplication(sys.argv)
		self.login = QtWidgets.QMainWindow()
		self.login_ui = Ui_Login_Ui()
		self.login_ui.setupUi(self.login)
		self.login.show()
		self.login_ui.pushButton.clicked.connect(self.loginNow)

		#for quick testing login. delete later
		self.login_ui.lineEdit.setText("0")
		self.login_ui.lineEdit_2.setText("admin")
		#end

		sys.exit(app.exec_())	
	


	def loginNow(self):
		user_id = self.login_ui.lineEdit.text()
		password = self.login_ui.lineEdit_2.text()

		#print("details: " , username , password)

		cur = self.conn.cursor()
		cur.execute("SELECT password,access_level,staff_name from staff where staff_id = ?", (user_id,) )

		rows = cur.fetchall()

		if(len(rows) == 0):
			print("incorrect username")
		else:
			password_db = rows[0][0]

			access_level = rows[0][1]

			username = rows[0][2]

			# if(password == password_db):
			# 	self.login.hide()
			print("hash from db: " , password_db)
			if(hashing.matchHash(password,password_db)):
				print("hash match")
				self.login.hide()


				#depending on access level correct window open krni hai
				self.ref = menu(user_id,username,access_level) #send username as well (for password changing)
				self.ref.show()
			else:
				print("incorrect password")



		#print(rows[0][0]) 
		#first result ka first element (which is required password cause query only returns one result and only one coloumn)

						


		



		
if __name__ == "__main__":
	x = Main()







