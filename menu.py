import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from menu_ui import Ui_Menu
from sqlite3 import Error
from StaffRecords_UI import Ui_Dialog
from login_ui import Ui_Login_Ui
from Alert_UI import Ui_Dialog
import sys
from AddRecords import AddRecords
from PrisonerRecords import PrisonerRecords
from StaffRecords import StaffRecords
from Alert import Alert
from Account import Account
from video import video
#from main import main
import PyQt5
import hashing
from shutil import copyfile
import datetime




if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class menu:
	def __init__(self,user_id,username,access_level):
		self.conn = sqlite3.connect('prison.db')
		self.username = username
		self.user_id = user_id
		self.access = access_level

		self.Menu = QtWidgets.QMainWindow()
		self.ui = Ui_Menu()
		self.ui.setupUi(self.Menu)
		self.ui.pushButton.clicked.connect(self.PrisRecords)
		self.ui.pushButton_7.clicked.connect(self.updatePass)
		self.ui.pushButton_4.clicked.connect(self.logout)
		self.ui.pushButton_2.clicked.connect(self.StaffRecord)
		self.ui.pushButton_3.clicked.connect(self.showVideo)
		self.ui.pushButton_6.clicked.connect(self.Account)
		self.ui.pushButton_5.clicked.connect(self.backup)
		
		this_user = self.user_id + " " + self.username  
		self.ui.label_4.setText(this_user)
		print("acccess level: " , access_level)

		if access_level == 0:
			pass #all allowed

		elif access_level == 1: #guard
			self.ui.pushButton_6.setEnabled(False) #account
			self.ui.label.setText("Guard Panel")
			
		else: #not staff or admin
			self.ui.pushButton_6.setEnabled(False) #account
			self.ui.pushButton_3.setEnabled(False) #video
			self.ui.label.setText("Staff Panel")


	def backup(self):
		print("creating backup")
		currentDT = datetime.datetime.now()
		path = str(currentDT) + '.db'
		path = path.replace(':','-')

		copyfile('se_db.db', path)
		self.ui.label_5.setText("Backup created")
		print("Backup created as " , path )


	def logout(self):
		print("logout")
		self.Menu.close()
		#something = Main(0)

	def Account(self):
		acc = Account()

	def show(self):
		self.Menu.show();

	def showVideo(self):
		vid = video()
		vid.show_webcam()
		msg = Alert("Suspicious Activity has been Detected")
		

	def StaffRecord(self):
		print("Working")
		idk = StaffRecords()

	def PrisRecords(self):

		#read text boxes and do stuff
		print(self.username)
		pop = PrisonerRecords(self.access)

	
	def updatePass(self):
		if self.username == "admin":
			print("Cant change admin/admin password.")
			return

		newPass = self.ui.textEdit.toPlainText()
		my_hash = hashing.getHash(newPass)

		rr = []

		rr.append(my_hash)
		rr.append(self.username)
		
		cur = self.conn.cursor()
		cur.execute("Update login Set password=? where username=?",rr)
		self.conn.commit()
		
		print("updated db with this password and this hash: " , newPass , " " ,  my_hash)

			