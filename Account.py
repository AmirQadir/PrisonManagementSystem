import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from menu import Ui_Menu
from sqlite3 import Error
from Account_UI import Ui_Dialog
import sys
import PyQt5
import hashing

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Account:
	def __init__(self):
		self.conn = sqlite3.connect('prison.db')

		self.diag = QtWidgets.QDialog()
		self.account_ui = Ui_Dialog()
		self.account_ui.setupUi(self.diag)
		#self.table_ui.pushButton.clicked.connect(self.viewRecords)
		#self.table_ui.pushButton_2.clicked.connect(self.addRecords)
		self.account_ui.pushButton_4.clicked.connect(self.resetPassword)
		self.viewRecords()
		self.diag.exec_()
		


	def resetPassword(self):
#		print("Reset password clicked")

		row = self.account_ui.tableWidget.currentRow()
		
		selected_username = (self.account_ui.tableWidget.item(row,1).text() )
		print(selected_username)

		if selected_username == "admin":
			print("Cant change admin/admin password.")
			return

		newPass = "12345"
		my_hash = hashing.getHash(newPass)

		rr = []

		rr.append(my_hash)
		rr.append(selected_username)
		
		cur = self.conn.cursor()
		cur.execute("Update login Set password=? where username=?",rr)
		self.conn.commit()

		print("Reset password of: " , selected_username , " to " ,  newPass)
		print("Hash: " , my_hash)

	def addRecords(self):
		pop = AddRecords()
		self.viewRecords()
		
	def deleteRecords(self):
		r = self.table_ui.tableWidget.currentRow()
		id=self.table_ui.tableWidget.item(r,0).text()
		print(id)
		statement='DELETE FROM Prisoner WHERE ID=?'

		cur = self.conn.cursor()
		cur.execute(statement, (id,))
		self.conn.commit()
		self.viewRecords()

	def viewRecords(self):
		print("hello")
		cur = self.conn.cursor()
		cur.execute("SELECT id , username from login")

		rows = cur.fetchall()

		self.account_ui.tableWidget.setRowCount(len(rows)) #Number of records jitna

		itr1 = 0
		itr2 = 0
		for record in rows:
			itr2 = 0
			for eachrecord in record:
				print(eachrecord," ..")
				self.account_ui.tableWidget.setItem(itr1,itr2,QTableWidgetItem(str(eachrecord)))
				itr2 = itr2 + 1
				# print("I am here", str(eachrecord))
			itr1 = itr1 + 1

		
